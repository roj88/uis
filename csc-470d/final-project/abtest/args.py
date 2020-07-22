import os
import sys
import argparse



def getOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Parses command.")
    parser.add_argument("-f", "--file_name", type=str, help="Input file.")
    parser.add_argument("-t", "--type", type=str, help="Input data type (T/F).")
    parser.add_argument("-a", "--alpha", type=float, help="Alpha value.")
    parser.add_argument("-p", "--power", type=float, help="Power value.")
    options = parser.parse_args(args)
    return options


