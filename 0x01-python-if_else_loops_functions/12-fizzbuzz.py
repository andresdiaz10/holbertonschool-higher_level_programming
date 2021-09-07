#!/usr/bin/python3
def fizzbuzz():
    for n1 in range(1, 101):
        if n1 % 3 == 0 and n1 % 5 == 0:
            print("FizzBuzz ", end="")
        elif n1 % 3 == 0:
            print("Fizz ", end="")
        elif n1 % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(n1), end="")
