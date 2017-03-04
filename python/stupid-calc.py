#I wonder what this does??
import math

#Make the input easier to read
def ezyfy(raw):
  #All in lowercase, no extra spaces.
  raw = raw.lower().strip()
  return raw

#Add all arguments together.
def add(*args):
  total_sum = 0
  indices = len(args)
  for number in range(indices):
    total_sum += args[number]
  return total_sum

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
      print("Ready for a command!")
      command = input()
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
        print("Alright. Enter a list of things you'd like added, each separated by a space.")
        #Get numbers and make a list
        numbers = input()
        numbers = numbers.split()
        numbers = [int(x) for x in numbers]
        
        print("The sum of the numbers is {}".format(add(*numbers)))
        
stupid_calc()
