import math

caramt = int(input("How many cars are there?: "))
people = int(input("How many people are there?: "))
seats = caramt * 5
carneed = seats - people

if carneed >= 0:
  print("There are enough seats")
elif carneed < 0:
  x = carneed + 5
  y = carneed / 5
  pos = abs(int(math.ceil(y)))
  print("Another", pos, "is/are needed")

