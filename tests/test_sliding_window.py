"""Test suit for SlidingWindow class
"""
import unittest

from sliding_window import SlidingWindow

SLIDING_WINDOW_SIZE = 3

class TestAddDelay(unittest.TestCase):
    """Test case for SlidingWindow.add_delay interface
    """

    def test_delay_is_added(self):
        """Delay is added to the end of sliding window
        """
        sliding_window = SlidingWindow(SLIDING_WINDOW_SIZE)
        network_delay = 100
        sliding_window.add_delay(network_delay)
        self.assertListEqual(sliding_window.delays, [network_delay])

    def test_sliding_window_size_is_correct(self):
        """We limit the number of measurements in sliding window
        """
        sliding_window = SlidingWindow(SLIDING_WINDOW_SIZE)
        network_delay = 100
        for _ in range(SLIDING_WINDOW_SIZE + 1):
            sliding_window.add_delay(network_delay)
        self.assertEqual(len(sliding_window.delays), SLIDING_WINDOW_SIZE)

    def test_window_moves_when_new_element_is_added(self):
        """Sliding window moves forward when new element is added
        """
        sliding_window = SlidingWindow(SLIDING_WINDOW_SIZE)
        network_delays = [100, 101, 102, 103]
        for delay in network_delays:
            sliding_window.add_delay(delay)
        expected_window = [101, 102, 103]
        self.assertListEqual(sliding_window.delays, expected_window)


class TestGetMedian(unittest.TestCase):
    """Test case for SlidingWindow.get_median interface
    """

    def test_only_one_delay_in_window(self):
        """Return -1 if window consists only of one delay
        """
        sliding_window = SlidingWindow(SLIDING_WINDOW_SIZE)
        sliding_window.delays = [100]
        self.assertEqual(sliding_window.get_median(), -1)

    def test_odd_number_of_values_in_window(self):
        """Return value of ((n + 1)/2)th item of sorted measurements array
        """
        sliding_window = SlidingWindow(SLIDING_WINDOW_SIZE)
        sliding_window.delays = [100, 102, 101]
        self.assertEqual(sliding_window.get_median(), 101)

    def test_even_number_of_values_in_window(self):
        """Return value of [((n)/2)th item + ((n)/2 + 1)th item ] /2 of
        sorted measurements array
        """
        sliding_window = SlidingWindow(SLIDING_WINDOW_SIZE)
        sliding_window.delays = [100, 102]
        self.assertEqual(sliding_window.get_median(), 101)
