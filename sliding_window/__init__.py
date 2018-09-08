"""Sliding window module

Exports SlidingWindow class, which stores network delays and provides and interface to calculate median over delays
"""

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