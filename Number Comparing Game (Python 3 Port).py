#!/usr/bin/env python3

import random, math


print("To exit the program: type 'exit'\n")

def CompareNumbers(num1, num2):
    if num1 < 0:
        Result = "Think of a bigger number\n"
    elif num1 > 100:
        Result = "Think of a smaller number\n"
    else:
        if num1 > num2:
            Result = str(num1) + " is greater than " + str(num2) + "\n"
        elif num1 < num2:
            Result = str(num1) + " is less than " + str(num2) + "\n"
        elif num1 == num2:
            Result = str(num1) + " is equal to " + str(num2) + "\n"
    return Result

while True:
    personNumber   = input("Guess a number: ")
    computerNumber = random.randint(-1, 101)
    if personNumber == "pi" or personNumber == "π" or personNumber == "Pi":
        personNumber  = "math.pi"
    if personNumber == "exit":
        exit()
    personNumber = int(personNumber)

    if personNumber < 0:
        print("Think of a bigger number\n")
    elif personNumber > 100:
        print("Think of a smaller number\n")
    else:
        Answer = CompareNumbers(personNumber, computerNumber)
        print(Answer)
