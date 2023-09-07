#!/usr/bin/python3
import sys
if __name__ == '__main__':
    sys.argv.pop(0)
    res = 0
    for number in sys.argv:
        res += int(number)
    print("{}".format(res))
