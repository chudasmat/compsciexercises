import random

randnum = random.randint(1, 3)

if randnum == 1:
  print("Walk 10km")
elif randnum == 2:
  print("Run 5km")
elif randnum == 3:
  print("Swim 1km")
else:
  print("Error")