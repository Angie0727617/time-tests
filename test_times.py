# test_times.py
from times import time_range, compute_overlap_time


def test_given_input():
    # setup
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    # call the function under test
    result = compute_overlap_time(large, short)

    # expected output (you can paste the actual printed output here)
    expected = [
        ('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
        ('2010-01-12 10:38:00', '2010-01-12 10:45:00')
    ]

    # assertion
    assert result == expected
