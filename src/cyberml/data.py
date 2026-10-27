"""Loading and labelling the Wendover web-log dataset (see data/DATACARD-wendover.md)."""

from pathlib import Path

import pandas as pd

NO_LOOKBACK = pd.Timedelta(0)
DEFAULT_DIR = Path(__file__).resolve().parents[2] / "data" / "raw" / "wendover"


def load_access_log(data_dir: Path = DEFAULT_DIR) -> pd.DataFrame:
    df = pd.read_csv(data_dir / "access_log.csv", parse_dates=["timestamp"])
    return df.sort_values("timestamp", ignore_index=True)


def load_attack_labels(data_dir: Path = DEFAULT_DIR) -> pd.DataFrame:
    """Ban windows; ``unban_time`` is NaT where the IP was still banned at export."""
    df = pd.read_csv(data_dir / "attack_labels.csv", parse_dates=["ban_time"])
    df["still_banned_at_export"] = df["unban_time"].eq("still_banned_at_export")
    df["unban_time"] = pd.to_datetime(df["unban_time"].mask(df["still_banned_at_export"]))
    return df


def label_requests(
    access: pd.DataFrame,
    labels: pd.DataFrame,
    lookback: pd.Timedelta = NO_LOOKBACK,
) -> pd.Series:
    """Return a boolean Series: was the request's IP inside a fail2ban ban window?

    fail2ban bans an IP *after* it crosses a threshold, so the requests that
    triggered the ban precede ``ban_time``. ``lookback`` extends each window
    backwards to include them. The choice belongs in the evaluation protocol.
    """
    windows = labels[["ip_id", "ban_time", "unban_time"]]
    req = access[["ip_id", "timestamp"]].reset_index()
    merged = req.merge(windows, on="ip_id", how="inner")
    open_ended = merged["unban_time"].isna()
    inside = (merged["timestamp"] >= merged["ban_time"] - lookback) & (
        open_ended | (merged["timestamp"] <= merged["unban_time"])
    )
    hit = merged.loc[inside, "index"].unique()
    return pd.Series(access.index.isin(hit), index=access.index, name="is_attack")
