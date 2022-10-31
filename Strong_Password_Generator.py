#Strong Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Strong Password Generator!")
the_letters= int(input("How many letters would you like in your password?\n"))
the_symbols = int(input(f"How many symbols would you like?\n"))
the_numbers = int(input(f"How many numbers would you like?\n"))

password= []
for letter in range(1,the_letters+1):
    password.append(random.choice(letters))
for number in range(1,the_symbols+1):
    password.append(random.choice(numbers))
for symbol in range(1,the_numbers+1):
    password.append(random.choice(symbols))

#shuffling the list
random.shuffle(password)

# method to convert password that is in list to string
def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1
final_password=listToString(password)

print(f"Here is your strong password: {final_password}")