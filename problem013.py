#!/usr/bin/python3

# Work out the first ten digits of the sum of the following
# one-hundred 50-digit numbers.

if __name__ == "__main__":
    readfile = open('problem013.txt', 'r')
    numlist = readfile.read().split()
    print(repr(sum(int(x) for x in numlist))[:10])
