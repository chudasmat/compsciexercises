quant = int(input("How many weights do you want to weigh?: "))
totalWeight = 0
x = 1
while x <= quant:
  currentWeight = float(input("Enter a weight: "))
  x = x + 1
  totalWeight = totalWeight + currentWeight

avg = str(totalWeight / quant)
splt = avg.split(".")
print(splt[0] + "." + (splt[1][:2]).rjust(2, "0"))
