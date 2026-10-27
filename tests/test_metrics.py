import pytest

from cyberml.metrics import recall_at_fpr


def test_recall_at_zero_fpr():
    y = [0, 0, 0, 0, 1, 1]
    s = [0.1, 0.2, 0.3, 0.9, 0.95, 0.5]
    recall, thr = recall_at_fpr(y, s, 0.0)
    assert thr == 0.9
    assert recall == 0.5


def test_recall_at_25pct_fpr_allows_one_false_positive():
    y = [0, 0, 0, 0, 1, 1]
    s = [0.1, 0.2, 0.3, 0.9, 0.95, 0.5]
    recall, _ = recall_at_fpr(y, s, 0.25)
    assert recall == 1.0


def test_requires_both_classes():
    with pytest.raises(ValueError):
        recall_at_fpr([1, 1], [0.1, 0.2], 0.1)
