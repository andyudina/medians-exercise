"""Sliding window module

Exports SlidingWindow class, which stores network delays and provides and interface to calculate median over delays
"""
from statistics import median

# Minimum length of delays array, which is required to calculate median
MIN_LEN_TO_CALCULATE_MEDIAN = 2

class SlidingWindow(object):
    """Calculate the median over a set of network delay measurements.

    The measurements are stored in a sliding window, which limits the number of items. Provides interfaces to adds a delay value to the window and to return the median of the delays calculated over the items from the sliding window
    """

    def __init__(self, sliding_window_size):
        """
        Args:
            sliding_window_size (int): size of the sliding window
        """
        self._sliding_window_size = sliding_window_size
        # List of int: network delays in current window
        self.delays = []

    def add_delay(self, network_delay):
        """
        Add network delay to sliding window and move window forward if needed
        Args:
          network_delay (int): value of delay to be stored
        """
        if len(self.delays) < self._sliding_window_size:
            # Append delay to the end of the list if window is not full
            self.delays.append(network_delay)
            return
        # Move window one step forward
        self.delays = self.delays[1: ] + [network_delay]

    def get_median(self):
        """
        Calculate median of delay values in current window
        Returns -1 if there is only one value in the window
        """
        if len(self.delays) < MIN_LEN_TO_CALCULATE_MEDIAN:
            return -1
        return median(self.delays)
