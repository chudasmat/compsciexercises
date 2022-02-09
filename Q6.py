watchavg = float(input("How long do you spend on average watching TV?: "))

if watchavg < 2:
  print("That should be ok")
elif watchavg >= 2 and watchavg <= 4:
  print("That will rot your brain")
else:
  print("That is too much TV")