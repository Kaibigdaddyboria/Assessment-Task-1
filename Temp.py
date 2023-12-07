#Determines if the users input is valid and then converts it into the chosen temperature 
def FarenheittoCelcius():
  print("You have chosen Fahrenheit to Celsius")
  f = (input("Enter Fahrenheit:"))
  if f.isdigit():
    f = int(f)
    c = (f - 32) * 5 / 9
    print(f"{f} Degrees Fahrenheit converted into Celsius is {c} degrees")
  else:
    print("Invalid Input")
def CelciustoFarenheit():
  print("You have chosen Celsius to Fahrenheit")
  c = (input("Enter Celsius:"))
  if c.isdigit:
    c = int(c)
    f = (c * 9 / 5) + 32
    print(f"{c} Degrees Celsius converted into fahrenheit is {f} degrees")
  else:
    print("Invalid Input")
#Presents a UI for the user
print("Enter:")
print("1 For Fahrenheit to Celsius")
print("2 For Celsius to Fahrenheit")
#Makes the code repeat if the input is invalid
while True:
  process = input("Choose ")
  #Determines if the users input is valid
  if process.isdigit():
    #Processes the users response and responds accordingly
    if process == "1":
      FarenheittoCelcius()
      break
    elif process == "2":      
      CelciustoFarenheit()
      break
    else:
      print("Input valid number")
      continue
  else:
    print("Input number")
    continue
print("Thank you for using this converter")