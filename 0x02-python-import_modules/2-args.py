#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argv = sys.argv
    if len(argv) == 1:
        print('{} arguments.'.format(len(argv) - 1))
    elif len(argv) == 2:
        print('{} argument:'.format(len(argv) - 1))
        print('{}: {}'.format(len(argv) - 1, argv[len(argv) - 1]))
    else:
        print('{} arguments:'.format(len(argv) - 1))
        for i in range(1, len(argv)):
            print('{}: {}'.format(i, argv[i]))
