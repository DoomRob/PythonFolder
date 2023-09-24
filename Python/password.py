import random
import array

# The Maxinum length of the password of your choice
MAX_LEN = 12

dights = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']

# combines all the character array
list_combined = dights + lower_case + upper_case + symbols

# randomly selects one character
digits_random = random.choice(dights)
lowercase_random = random.choice(lower_case)
uppercase_random = random.choice(upper_case)
symbols_random = random.choice(symbols)

# generates a 12 letter password with at least a dight, symbol uppercase and lowercase letter
password = digits_random + lowercase_random + uppercase_random + symbols_random
for x in range(MAX_LEN - 4):
    password = password + random.choice(list_combined)
    # converts the password into an array
    password_list = array.array('u', password)
    random.shuffle(password_list)

password = ""
for x in password_list:
    password = password + x

print(password)