# Developed & Programmed By 7Q1
# iG -> @thrudespair

import random
import time
import os

userName = os.getlogin()
numbers = '0123456789'
abc = 'abcdefghijklmnopqrstuvwxyz'
all = numbers + abc
passList = []
_b = 0


# <!---------------------------------------- >
# Pervent ValueError:
print("[+] Input Number Only!")
while True:
  try:
    times = int(input('[?] How many passowrds >> '))
    break
  except:
    print("[+] Input Number Only!")
while True:
  try:
    chr = int(input('[?] How many Character >> '))
    break
  except:
    print("[+] Input Number Only!")

# Passwords Generator:
for i in range(times):
  password = "".join(random.sample(all, chr))
  passList.append(password)
print("Processing . . .")
for i in passList:
  i = i + "\n"
  with open(f'C:\\Users\\{userName}\\Desktop\\passGen.txt', 'a') as f:
    f.write(i)
input("[+] Lists Saved AS (passGen.txt) In Desktop.\n\nPress Enter To exit . . .")
# exit()
# <!---------------------------------------- >
