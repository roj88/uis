import os
import sys
import argparse


def get_options(args=sys.argv[1:]):
    """
    Parse command line arguments.

    Args:
        args (list): Arguments from command line.

    Returns:
        Dict of parsed items.
    """
    parser = argparse.ArgumentParser(description="Parses command.")

    # add parsed arguments
    parser.add_argument("-f", "--file_name", type=str, help="Input file.")
    parser.add_argument("-t", "--type", type=str, help="Input data type (T/F).")
    parser.add_argument("-a", "--alpha", type=float, help="Alpha value.")
    parser.add_argument("-p", "--power", type=float, help="Power value.")

    # get dict of parsed arguments
    options = parser.parse_args(args)

    # return parsed items dict
    return options


