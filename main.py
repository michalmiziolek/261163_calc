# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


import sys




first_number = int(sys.argv[1])
second_number = int(sys.argv[3])


if sys.argv[2] == "+":
    print(first_number + second_number)
if sys.argv[2] == "-":
    print(first_number - second_number)
if sys.argv[2] == "*":
    print(first_number * second_number)
if sys.argv[2] == "/":
    print(first_number / second_number)

