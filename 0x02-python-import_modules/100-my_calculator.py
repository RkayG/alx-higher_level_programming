#!/usr/bin/python3
""" program for simple arithmetic """
from calculator_1 import add, sub, mul, div
from sys import argv, exit

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = {'+': add, '-': sub, '*': mul, '/': div}

    op = argv[2]
    if op not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    print("{} {} {} = {}".format(a, op, b, operator[op](a, b)))
