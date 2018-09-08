# medians-exercise
Sliding window that stores measurements and calculates their median

## Time complexity

### Current time-complexity

Every time window is moved one measurement forward, all measurements in a window are being sorted to find a median. Timesort algorithm is used for sorting which results in O(*n* log*n*), where n is the sliding window size. We iterate over all measurements once, so resulting complexity is O(*measurements_number window_size* log*window_size*) Window size is constant but can be a big number. So, while complexity here is O(*n*) (sorting complexity does not depend on input size, but depend on sliding window size), this constant can be big enough to actually affect performance and should be optimized

### Optimized algorithm time-complexity

- Maintain two lists with measurements: sorted by measurements values and with measurements in the original order. 
- Add value to first sorted list preserving the ascending order (worst case scenario will have to iterate over the whole window and append new value at the end of the list -> O(*window_size*)). 
- Append new value to the end of the second list.
- If window limits are exceeded, remove the first element of the list with the original order from both lists -> worst case scenario this will take O(*window_size*)

Now on each step we spend O(*window_size*) time instead of O(*window_size* log*window_size*)

### Test & Profile

1. Run tests ```python3 -m unittest discover tests```
2. Profile code ```python3 -m cProfile -o timeStats.profile script.py [input file name] [window size]```
Will store results to timeStats.profile
