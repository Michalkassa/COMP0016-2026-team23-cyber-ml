from pathlib import Path

import pandas as pd

from cyberml.data import label_requests, load_access_log, load_attack_labels

FIXTURES = Path(__file__).parent / "fixtures"


def test_label_requests_uses_ban_window():
    access = load_access_log(FIXTURES)
    labels = load_attack_labels(FIXTURES)
    is_attack = label_requests(access, labels)
    flagged = access.loc[is_attack, ["ip_id", "path"]].values.tolist()
    assert flagged == [["ip_a", "/admin"], ["ip_c", "/xmlrpc.php"]]


def test_label_requests_lookback_includes_triggering_requests():
    access = load_access_log(FIXTURES)
    labels = load_attack_labels(FIXTURES)
    is_attack = label_requests(access, labels, lookback=pd.Timedelta(minutes=10))
    assert set(access.loc[is_attack & (access["ip_id"] == "ip_a"), "path"]) == {
        "/wp-login.php",
        "/admin",
    }
    assert not is_attack[access["ip_id"] == "ip_b"].any()


def test_still_banned_at_export_is_open_ended():
    labels = load_attack_labels(FIXTURES)
    assert labels["unban_time"].isna().sum() == 1
    access = load_access_log(FIXTURES)
    is_attack = label_requests(access, labels)
    assert is_attack[access["ip_id"] == "ip_c"].all()
