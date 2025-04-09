#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

rand_password = []
for num in range(0,nr_numbers):
    rand_password.append(random.choice(numbers))
print(rand_password)

rand_letter = []
for letter in range(0,nr_letters):
    rand_password.append(random.choice(letters))
print(rand_password)

rand_symb = []
for letter in range(0,nr_symbols):
    rand_password.append(random.choice(symbols))
print(rand_password)

random.shuffle(rand_password)
ran_pass= ""
for char in rand_password:
    ran_pass += char

print(ran_pass)
