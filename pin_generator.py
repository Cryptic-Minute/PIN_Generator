# Random Pin Generator
# By https://github.com/hacker41d4n/

import random
chars ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+}{"
length = int(input("Enter password length "))
password=""
for i in range(length+1):
    password += random.choice(chars)
print(password)

# Sample output :
#
#
# Enter password length 8
# l#9RX!ufa