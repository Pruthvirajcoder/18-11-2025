# random password genarator

import random
import string

pass_len = 12
newpass= (string.ascii_letters + string.digits + string.punctuation)
password =""
for i in range(pass_len):
    password += (random.choice(newpass))

print("your random password is :", password)

  