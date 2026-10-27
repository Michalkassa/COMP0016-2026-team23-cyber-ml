"""Detection metrics. The primary comparison is recall at a fixed false-alert budget."""

import numpy as np


def recall_at_fpr(y_true, scores, fpr_budget: float) -> tuple[float, float]:
    """Recall at the strictest threshold whose false-positive rate is <= ``fpr_budget``.

    Higher scores mean more anomalous. Returns ``(recall, threshold)``; a sample is
    flagged when ``score > threshold``.
    """
    y_true = np.asarray(y_true, dtype=bool)
    scores = np.asarray(scores, dtype=float)
    if not 0 <= fpr_budget <= 1:
        raise ValueError("fpr_budget must be in [0, 1]")
    if y_true.all() or not y_true.any():
        raise ValueError("y_true must contain both classes")

    neg = np.sort(scores[~y_true])[::-1]
    allowed_fp = int(np.floor(fpr_budget * len(neg)))
    threshold = neg[allowed_fp] if allowed_fp < len(neg) else -np.inf
    recall = float(np.mean(scores[y_true] > threshold))
    return recall, float(threshold)
