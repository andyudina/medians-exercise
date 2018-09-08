"""Sliding window module

Exports SlidingWindow class, which stores network delays
and provides and interface to calculate median over delays
"""
from statistics import median

# Minimum length of delays array, which is required to calculate median
MIN_LEN_TO_CALCULATE_MEDIAN = 2

class SlidingWindow:
    """Calculate the median over a set of network delay measurements.

    The measurements are stored in a sliding window,
    which limits the number of items. Provides interfaces to adds a delay
    value to the window and to return the median of the delays calculated over
    the items from the sliding window
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


class SlidingWindowOptimized:
    """Calculate the median over a set of network delay measurements.

    Use optimized algorithm to avoid sorts after measurement is added
    """

    def __init__(self, sliding_window_size):
        """
        Args:
            sliding_window_size (int): size of the sliding window
        """
        self._sliding_window_size = sliding_window_size
        # Delays in current window sorted by value
        self.delays = []
        # Delays in current window sorted by order number
        # (first arrived is on first place in the list)
        self._delays_sequential_order = []

    def add_delay(self, new_delay):
        """Add network delay to sliding window and move window forward if needed

        Maintains list of delays sorted by value and by order number

        Args:
          network_delay (int): value of delay to be stored
        """
        # Add new_delay to sorted list of delays
        for index, delay in enumerate(self.delays):
            if delay > new_delay:
                self.delays = \
                    self.delays[:index] + \
                    [new_delay] + \
                    self.delays[index:]
                break
        else:
            self.delays = self.delays + [new_delay]
        # Add new delay to list of measurements in sequential order
        self._delays_sequential_order.append(new_delay)
        # Return if window limit is not overflown
        if len(self.delays) <= self._sliding_window_size:
            return
        # Move window one step forward by
        # removing the earliest element from delays list
        earliest_measurement = self._delays_sequential_order[0]
        # Remove earliest element in place
        self.delays.remove(earliest_measurement)
        self._delays_sequential_order = self._delays_sequential_order[1:]

    def get_median(self):
        """
        Calculate median for previously sorted list
        Returns -1 if there is only one value in the window
        """
        delays_size = len(self.delays)
        if delays_size < MIN_LEN_TO_CALCULATE_MEDIAN:
            return -1
        # Odd number of elements in list
        if delays_size % 2 == 1:
            return self.delays[delays_size // 2]
        # Even number of elements in delay list
        middle_element_index = delays_size // 2
        return (
            self.delays[middle_element_index - 1] +
            self.delays[middle_element_index]) / 2
