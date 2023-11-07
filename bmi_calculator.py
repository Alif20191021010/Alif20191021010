def bmi(w,h):
  w: float; h: float
  mean2 = (w/(h**2))
  print("Your BMI is: ",mean2)
  if(mean2<18.5):
      print("You are underweight.")
  elif(mean2>=18.5 and mean2<=24.5):
      print("Your are healthy.")
  elif(mean2>=25 and mean2<=29.5):
      print("Your are overweight.")
  else:
      print("You are fat.")
w = float(input("Enter your weight : "))
h = float(input("Enter your hight : "))
bmi(w,h)
