#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    i = len(sys.argv) - 1
    if i == 0:
        print("0 arguments.")
    elif i == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(i)0

    for y in range(i):
    print("{}: {}".format(y + 1, sys.argv[y + 1]))
