# Random Pin Generator
# By https://github.com/hacker41d4n/

import random
import sys

# ---- Handle arguments ----
if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <password length>")
    sys.exit(1)

# ---- Variables ----
length      =   int(sys.argv[1])
charset     =   "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+}{"
password    =   str()

# ---- Work -----
for i in range(length):
    password += random.choice(charset)

# --------- Output -------------
print(password)
