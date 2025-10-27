import datetime
from times import time_range, compute_overlap_time


def test_non_overlapping_ranges():
    """Two time ranges that do not overlap"""
    range1 = time_range("2025-10-26 10:00:00", "2025-10-26 11:00:00")
    range2 = time_range("2025-10-26 12:00:00", "2025-10-26 13:00:00")
    overlap = compute_overlap_time(range1, range2)
    assert overlap == []


def test_multiple_intervals_with_overlap():
    """Two time ranges with several intervals each, overlapping"""
    range1 = time_range("2025-10-26 10:00:00", "2025-10-26 12:00:00", number_of_intervals=2)
    range2 = time_range("2025-10-26 11:00:00", "2025-10-26 13:00:00", number_of_intervals=2)
    overlap = compute_overlap_time(range1, range2)
    # At least one overlap should exist
    assert any(start < end for start, end in overlap)


def test_end_starts_exactly_same_time():
    """Two ranges where one ends exactly when the other starts"""
    range1 = time_range("2025-10-26 10:00:00", "2025-10-26 11:00:00")
    range2 = time_range("2025-10-26 11:00:00", "2025-10-26 12:00:00")
    overlap = compute_overlap_time(range1, range2)
    assert overlap == []

