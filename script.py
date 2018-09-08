"""Calculate medians using sliding window
"""
import argparse
import sys

from sliding_window import SlidingWindow

MIN_WINDOW_SIZE = 2

def calculate_and_print_medians(
        input_file, output_file, sliding_window_size):
    """Calculate median using sliding window on delays from input_file
    and store results to output file

    Args:
        input_file (file object): File with delays
        output_file (file object): Output file to store medians
        sliding_window_size (int): Size of sliding window
    """
    sliding_window = SlidingWindow(sliding_window_size)

    for line in input_file:
        # Fail fast here if value is not int
        line = line.rstrip()
        if not line:
            # Skip empty lines
            continue
        delay = int(line)
        sliding_window.add_delay(delay)
        median = sliding_window.get_median()
        output_file.write('%d\r\n' % median)

def is_valid_window_size(value):
    """Validate window size and raise ArgumentTypeError.

    Should be positive integer greater than 1.

    Args:
        value (int): window size value

    Returns:
        Window size converted to int
    """
    def raise_argparse_error(value):
        """Raise ArgumentTypeError with expected window size description
        """
        raise argparse.ArgumentTypeError(
            '%s is an invalid window size. '
            'Should be integer greater or equal %d' % (value, MIN_WINDOW_SIZE))
    try:
        value = int(value)
    except (ValueError, TypeError):
        raise_argparse_error(value)
    if value < MIN_WINDOW_SIZE:
        raise_argparse_error(value)
    return value

def main(arguments):
    """Main script

    Calculate sliding window median for measurements in file
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'infile', help="Input file", type=argparse.FileType('r'))
    parser.add_argument(
        'sliding_window_size', help="Input file",
        type=is_valid_window_size)
    parser.add_argument('-o', '--outfile', help="Output file",
                        default=sys.stdout, type=argparse.FileType('w'))
    args = parser.parse_args(arguments)
    # Calculate medians and print into file
    calculate_and_print_medians(
        args.infile, args.outfile,
        args.sliding_window_size)
    # Close file handlers
    args.infile.close()
    args.outfile.close()

if __name__ == '__main__':
    main(sys.argv[1:])
