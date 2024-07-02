import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]

print("Welcome to the password generator")
letters_count = int(input("How many letters would you like in your password: "))
numbers_count = int(input("How many numbers would you like in your password: "))
symbols_count = int(input("How many symbols would you like in your password: "))

password = []

for i in range(0, letters_count): 
    password.append(letters[random.randint(0, len(letters) - 1)])

for i in range(0, numbers_count): 
    password.append(numbers[random.randint(0, len(numbers) - 1)])

for i in range(0, symbols_count): 
    password.append(symbols[random.randint(0, len(symbols) - 1)])

random.shuffle(password)
password_str = ""

for i in password:
    password_str = password_str + i

print(password_str)