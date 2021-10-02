"""
Write a program that asks the user to enter a programming language. If they enter python, then print
out the message “This program was written in Python.” Otherwise nothing should happen (no else
statement is necessary).
"""

lang = input("Insert the language: ")

if lang.lower() == "python":
    print("This program was written in Python")

