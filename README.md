# medians-exercise
Sliding window that stores measurements and calculates their median

## Current time-complexity

Every time window is moved one measurement forward, all measurements in a window are being sorted to find a median. Timesort algorithm is used for sorting which results in O(*n* log*n*), where n is the sliding window size. We iterate over all measurements once, so resulting complexity is O(*measurements_number window_size* log*window_size*) Window size is constant but can be a big number. So, while complexity here is O(*n*) (sorting complexity does not depend on input size, but depend on sliding window size), this constant can be big enough to actually affect performance and should be optimized
