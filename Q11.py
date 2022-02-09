starttime = float(input("What is your start time?: "))
endtime = float(input("What is your end time?: "))
speed = 100 / (endtime - starttime)
if speed >= 10:
  print("Fast")
else:
  print(speed)