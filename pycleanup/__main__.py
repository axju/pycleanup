'''The main function to pars the command-line parameter'''
from pycleanup import VERSION, DIR_KIND, FILE_KIND
from pycleanup.func import cleanup, print_infos
import os, argparse

def main():
    parser = argparse.ArgumentParser(description='PyClean')

    parser.add_argument(
        '--version', action='version',
        version='pyclean '+VERSION)

    for name, data in DIR_KIND.items():
        parser.add_argument('--'+name, help=data.get('help', ''), action='store_true')

    for name, data in FILE_KIND.items():
        parser.add_argument('--'+name, help=data.get('help', ''), action='store_true')

    args = parser.parse_args()

    if sum([ 1 for a in vars(args).values( ) if a]) == 0:
        cwd = os.getcwd()
        print_infos(cwd)

    else:
        cwd = os.getcwd()
        cleanup(cwd, vars(args))

if __name__ == '__main__':
    main()
