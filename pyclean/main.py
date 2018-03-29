from pyclean import VERSION
from pyclean.func import cleanup
import os, argparse

def main():
    parser = argparse.ArgumentParser(description='PyClean')

    parser.add_argument(
        '--version', action='version',
        version='%(prog)s '+VERSION)

    parser.add_argument(
        '--show', help='Show all working files which culd be delete.',
        action='store_true')

    args = parser.parse_args()
    cleanup(args)
