#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        lis = 1
        for j in i:
            if lis == len(i):
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
            lis = lis + 1
        print()
