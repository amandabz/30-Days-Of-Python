# Generate password
# Example 1 (better)

import random
import string


def generate_password(length):
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation)
    for i in range(length))
    return password


length = int(input("Enter password length: "))
password = generate_password(length)
print("Generated password:", password)


# Example 2 (worst)

import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
number = "12345567890"
symbol = "%$&!*)(="

use_for = lower_case + upper_case + number + symbol
length_for_pass = 8

password = "".join(random.sample(use_for, length_for_pass))

print("Your generate password is:", password)


# Calculadora

def calculator():
    def add(num1, num2):
        return num1 + num2

    def subtract(num1, num2):
        return num1 - num2

    def multiply(num1, num2):
        return num1 * num2

    def divide(num1, num2):
        return num1 / num2

    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    choice = input("Escoja una elección (1/2/3/4): ")

    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))

    if choice == "1":
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == "2":
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == "3":
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == "4":
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Opción no válida")

calculator()
