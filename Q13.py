import random

userscore = 0
x = 0

while x < 5:
  x = x + 1
  user = int(input("Enter a number between 1 and 6: "))
  if user < 1 and user > 6:
    print("Error")
  comp = random.randint(1, 6)
  if user == comp:
    userscore = userscore + 10
    print("Your number matches!")

print(userscore)





