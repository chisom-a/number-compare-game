#!/usr/bin/env python3

import random, math
import tkinter as tk
from tkinter import *
import tkinter.messagebox as tkMessageBox

CheatMode = False
personMin = 0
personMax = 100

def GuessButton():
    global CheatMode, personMin, personMax
    personNumber = InputNumberBox.get()
    if personNumber == "cheat computer" or personNumber == "Cheat computer":
        CheatMode = True
    elif personNumber == "decheat computer" or personNumber == "Decheat computer":
        CheatMode = False

    if personNumber == "pi" or personNumber == "π" or personNumber == "Pi":
        personNumber  = "math.pi"
    if CheatMode == True:
        computerNumber = random.randint(0, 10)
        personMin = -1000
        personMax = 1000
    else:
        computerNumber = random.randint(-1, 101)
        personMin = 0
        personMax = 100
    try:
        personNumber = int(personNumber)
        Answer = CompareNumbers(personNumber, computerNumber)
        tkMessageBox.showinfo("Result", Answer)
    except (NameError, SyntaxError, TypeError, ValueError):
        tkMessageBox.showinfo("Warning", "Please type in a number in the box")

def CompareNumbers(num1, num2):
    if num1 < personMin:
        Result = "Think of a bigger number\n"
    elif num1 > personMax:
        Result = "Think of a smaller number\n"
    else:
        if num1 > num2:
            Result = str(num1) + " is greater than " + str(num2) + "\n"
        elif num1 < num2:
            Result = str(num1) + " is less than " + str(num2) + "\n"
        elif num1 == num2:
            Result = str(num1) + " is equal to " + str(num2) + "\n"
    return Result


mainWindow = tk.Tk()
mainWindow.geometry("400x100")

try:
    mainWindow.iconphoto(True, tk.PhotoImage(file='Number Comparing Game Icon.png'))
except:
    tkMessageBox.showinfo("Icon Warning", "Couldn't find icon for this application. Will be using the default icon.")
mainWindow.title('Number Comparing Game (Python3 TK Port)')

def HelpButton():
    instructionText = "Type in a number & click the button to see a comparison between your number and a another number\n\nNOTE: There's a secret in this program! Can you find it?!"
    tkMessageBox.showinfo("Help", instructionText)

helpButton = tk.Button(mainWindow, text=" Help ", command=HelpButton)
helpButton.pack(side=BOTTOM)

compareButton = tk.Button(mainWindow, text="\nCompare\n", command=GuessButton)
compareButton.pack(side = RIGHT)

L1 = Label(mainWindow, text="Number: ")
L1.pack(side=LEFT)

InputNumberBox = Entry(mainWindow, bd=3, bg="gray99")
InputNumberBox.pack(side=LEFT)

L3 = Label(mainWindow, text=" ")
L3.pack(side=LEFT)

mainWindow.eval('tk::PlaceWindow . center')
mainWindow.mainloop()
