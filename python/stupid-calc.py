#I wonder what this does??
import math

#Make the input easier to read
def ezyfy(raw):
  dupe = raw
  #All in lowercase, no extra spaces.
  raw = dupe.lower().strip()
  return raw

#Add all arguments together
def add(*args):
  total_sum = 0
  length = len(args)
  for number in range(length):
    total_sum += args[number]
  return total_sum

#Split stuff by space, then hand in as parameter.

#Main.
def stupid_calc():
  
  """
  Possible Actions:
  
  EXIT- exit the program
  
  -COMMONLY USED-
  -------------
  ADD
  DIVIDE
  SUBTRACT
  MULTIPLY
  SUBTRACT
  -------------
  
  format: COMMAND- function
  Type the command to do the function. Note: not case sensitive :)
  """
  print("Enter HELP for a list of possible actions.")
  while True:
      print("ready for a new command")
      command = input("")
      command = ezyfy(command)
      
      #Print help docs
      if command == "help":
        print(stupid_calc.__doc__)
        
      #Quit everything!!!
      elif command == "exit":
        print("Hope you had fun. Enjoy your day!")
        #quit
        return
      
      #add
      elif command == "add":
        print("Alright. Enter a list of numbers you want added, EACH SEPARATED BY A SPACE, and I'll return to you the sum!")
        numbers = input()
        numbers = numbers.split()
        numbers = [int(x) for x in numbers]
        print("The sum of your numbers is {}".format(add(*numbers)))

stupid_calc()
