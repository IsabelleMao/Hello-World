#Style guide: New 'lines' shall be in the same print statement, or directly following an input.
import math #Very funny, I know

#make the input easier to read
def ezyfy(raw):
    dupe = raw
    #All in lowercase, no extra spaces.
    raw = dupe.lower().strip()
    return raw

#add all arguments together
def add(*args):
    total_sum = 0
    length = len(args)
    for number in range(length):
        total_sum += args[number]
    return total_sum

#subtract an unknown amount of numbers from a given number
def subtract(original, *args):
  length = len(args)
  for sub in range(length):
    original -= args[sub]
  return original
  
#solve for x in a quadratic formula 
#NOT DONE IMPLEMENTING
def quadratic_equation(a, b, c):
    discriminant = (b**2) - (4 * a * c)
    if discriminant < 0: #No solutions, 'cause they're imaginary
        return [0]
    elif discriminant == 0: #Only one solution
        return [1, -b/2*a]
    else:
        sol1 = (-b + discriminant) / 2 * a
        sol2 = (-b - discriminant) / 2 * a
        return [2, sol1, sol2]
      
    
#split by space and return as a list of float numbers
def split(arg):
    arg = arg.split()
    arg = [float(x) for x in arg]
    return arg
#Split stuff by space, then hand in as parameter.

#------------------------------------------#

#main calculator
def stupid_calc():
  
    """
    Possible Actions:
    
    EXIT- exit the program
    
    -COMMONLY USED-
    -------------
    ADD
    DIVIDE - WIP
    SUBTRACT
    MULTIPLY- WIP
    SUBTRACT
    -------------
    -FORMULAS-
    -------------
    QUADRATIC FORMULA
    
    format: COMMAND- function
    Type the command to do the function. Note: not case sensitive :)
    """
    print("""Enter HELP for a list of possible actions.
------------------------------------------""")
    while True:
        print("""ready for a new command
------------------------------------------""")
        command = input()
        command = ezyfy(command)
        print("------------------------------------------")
      
      #print help
        if command == "help":
            print(stupid_calc.__doc__)
      #exit
        elif command == "exit":
            print("Hope you had fun. Enjoy your day!")
            return
          
      #add
        elif command == "add":
            print("""Alright. Enter a list of numbers you want added, EACH SEPARATED BY A SPACE, and I'll return to you the sum!
------------------------------------------""")
            numbers = input()
            numbers = split(numbers)
            result = add(*numbers)
            print("""------------------------------------------
The sum of your numbers is {}""".format(result))

      #subtract
        elif command == "subtract":
            print("""Certainly. Enter a single number to subtract from.
------------------------------------------""")
            original = float(input())
            print("------------------------------------------")
            print("""Now, enter a number/numbers you want subtracted from {}. Separate more than one number with a space.
------------------------------------------""".format(original))
            subtract_this = input()
            print("------------------------------------------")
            subtract_this = split(subtract_this)
            result = subtract(original, *subtract_this)
            print("""Your result is {}
------------------------------------------""".format(result))
        elif command == "quadratic formula":
            print("""Okay! Please enter your a-value
------------------------------------------""")
            a = int(input())
            print("""------------------------------------------
            Please enter your b-value
------------------------------------------""")
            b = int(input())
            print("""------------------------------------------
            Almost there! c-value please
------------------------------------------""")
            c = int(input())
            result = quadratic_equation(a, b, c)
            if result[0] == 0:
                print("With the values you gave me, there are no real solutions.")
            elif result[0] == 1:
                print("There is exactly one solution: {}").format(result[2])
            else:
                print("There are TWO solutions! One is {} and the other is {}".format(result[1], result[2]))

stupid_calc()
