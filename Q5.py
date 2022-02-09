import random

randnum = random.randint(1, 10)
userchoice = int(input("Pick a whole number: "))

if randnum == userchoice:
  print("Correct")
else:
  print("Not what I was thinking")