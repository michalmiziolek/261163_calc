
import sys

first_number = int(sys.argv[1])
second_number = int(sys.argv[3])

print("First number:", first_number)
print("Second number:", second_number)
if sys.argv[2] == "+":
    print(first_number + second_number)
if sys.argv[2] == "-":
    print(first_number - second_number)
if sys.argv[2] == "*":
    print(first_number * second_number)
if second_number == 0:
    print("We cant divide by zero")
else:
    print(first_number / second_number)

