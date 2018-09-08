"""Test suit for SlidingWindowOptimized class
"""
import unittest

from sliding_window import SlidingWindowOptimized

SLIDING_WINDOW_SIZE = 3

class TestAddDelay(unittest.TestCase):
    """Test case for SlidingWindowOptimized.add_delay interface
    """

    def test_first_delay_is_added(self):
        """First delay is added correctly
        """
        sliding_window = SlidingWindowOptimized(SLIDING_WINDOW_SIZE)
        network_delay = 100
        sliding_window.add_delay(network_delay)
        self.assertListEqual(sliding_window.delays, [network_delay])

    def test_smaller_delay_is_added_in_the_beggining_of_list(self):
        """Position of new delay in the list depends on delay amount
        Delays are added in ascending order
        """
        sliding_window = SlidingWindowOptimized(SLIDING_WINDOW_SIZE)
        sliding_window.add_delay(102)
        sliding_window.add_delay(100)
        self.assertListEqual(sliding_window.delays, [100, 102])

    def test_the_greater_delay_is_added_in_the_endof_list(self):
        """Delay with greatest amount is added to the end of the list
        """
        sliding_window = SlidingWindowOptimized(SLIDING_WINDOW_SIZE)
        sliding_window.add_delay(100)
        sliding_window.add_delay(102)
        self.assertListEqual(sliding_window.delays, [100, 102])

    def test_window_moves_when_new_element_is_added(self):
        """Sliding window moves forward when new element is added
        """
        sliding_window = SlidingWindowOptimized(SLIDING_WINDOW_SIZE)
        network_delays = [103, 102, 101, 100]
        for delay in network_delays:
            sliding_window.add_delay(delay)
        expected_window = [100, 101, 102]
        self.assertListEqual(sliding_window.delays, expected_window)


class TestGetMedian(unittest.TestCase):
    """Test case for SlidingWindow.get_median interface
    """

    def test_only_one_delay_in_window(self):
        """Return -1 if window consists only of one delay
        """
        sliding_window = SlidingWindowOptimized(SLIDING_WINDOW_SIZE)
        sliding_window.delays = [100]
        self.assertEqual(sliding_window.get_median(), -1)

    def test_odd_number_of_values_in_window(self):
        """Return value of ((n + 1)/2)th item of sorted measurements array
        """
        sliding_window = SlidingWindowOptimized(SLIDING_WINDOW_SIZE)
        sliding_window.delays = [100, 101, 103]
        self.assertEqual(sliding_window.get_median(), 101)

    def test_even_number_of_values_in_window(self):
        """Return value of [((n)/2)th item + ((n)/2 + 1)th item ] /2 of
        sorted measurements array
        """
        sliding_window = SlidingWindowOptimized(SLIDING_WINDOW_SIZE)
        sliding_window.delays = [100, 102]
        self.assertEqual(sliding_window.get_median(), 101)
