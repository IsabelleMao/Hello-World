#Style guide: New 'lines' shall be in the same print statement, or directly following an input.
import math #Very funny, I know

#the new line function
def nl():
    print("------------------------------------------")
    
    
#The function for adding
def add_func():
    print("Alright. Enter a list of numbers you want added, EACH SEPARATED BY A SPACE, and I'll return to you the sum!")
    nl()
    numbers = input()
    numbers = split(numbers)
    result = add(*numbers)
    nl()
    print("The sum of your numbers is {}".format(result))
    
#add all arguments together
def add(*args):
    total_sum = 0
    length = len(args)
    for number in range(length):
        total_sum += args[number]
    return total_sum

#The function for subtracting
def subtract_func():
    print("Certainly. Enter a single number to subtract from.")
    nl()
    original = float(input())
    nl()
    print("Now, enter a number/numbers you want subtracted from {}. Separate more than one number with a space".format(original))
    nl()
    subtract_this = input()
    nl()
    subtract_this = split(subtract_this)
    result = subtract(original, *subtract_this)
    print("Your result is {}".format(result))
            
#subtract an unknown amount of numbers from a given number
def subtract(original, *args):
    length = len(args)
    for sub in range(length):
        original -= args[sub]
        return original

#multiply all the numbers together
def multiply_func():
    print("Mhm. Enter all the numbers you want to multiply together, each separated by a space.")
    nl()
    numbers = input()
    numbers = split(numbers)
    result = multiply(*numbers)
    nl()
    print("The product of your numbers is {}".format(result))
  
#multiply all the numbers together
def multiply(*args):
    product = 1
    length = len(args)
    for number in range(length):
        product *= args[number]
    return product

#divide a number by an unknown amount of numbers
def divide(original, *args):
    length = len(args)
    for sub in range(length):
        original /= args[sub]
    return original
    
#The function for dividing
def divide_func():
    print("Stupendous! Enter the dividend")
    nl()
    dividend = float(input())
    nl()
    print("Now, enter a number/numbers you want to divide {} by. Separate more than one number with a space".format(dividend))
    nl()
    divisors = input()
    nl()
    divisors = split(divisors)
    quotient = divide(dividend, *divisors)
    print("Your result is {}".format(quotient))
    
#solve for x in a quadratic formula 
def quadratic_equation(a, b, c):
    discriminant = (b**2) - (4 * a * c)
    if discriminant < 0: #No solutions, 'cause they're imaginary
        return [0]
    elif discriminant == 0: #Only one solution
        return [1, -b/2*a]
    else:
        sol1 = (-b + math.sqrt(discriminant))
        sol1 /= (2 * a)
        sol2 = (-b - math.sqrt(discriminant))
        sol2 /= (2 * a)
        return [2, sol1, sol2]
#the function for the quadratic equation
def quadratic_equation_func():
    print("Okay! Please enter your a-value")
    nl()
    a = float(input())
    nl()
    print("Please enter your b-value")
    nl()
    b = float(input())
    nl()
    print("Almost there! c-value please")
    nl()
    c = float(input())
    result = quadratic_equation(a, b, c)
    if result[0] == 0:
        nl()
        print("With the values you gave me, there are no real solutions.")
    elif result[0] == 1:
        nl()
        print("There is exactly one solution: {}".format(result[1]))
    else:
        nl()
        print("There are TWO solutions! One is {} and the other is {}".format(result[1], result[2]))
    
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
    SUBTRACT
    MULTIPLY
    DIVIDE
    EXPONENT - WIP
    -------------
    -FORMULAS-
    -------------
    QUADRATIC FORMULA
    
    format: COMMAND- function
    Type the command to do the function. Note: not case sensitive :)
    """
    print("Enter HELP for a list of possible actions.")
    nl()
    while True:
        print("ready for a new command")
        nl()
        command = input().lower().strip()
      #there would be a nl here
        nl()
      #print help
        if command == "help":
            print(stupid_calc.__doc__)
      #exit
        elif command == "exit":
            print("Hope you had fun. Enjoy your day!")
            return
      #add
        elif command == "add":
            add_func()
      #subtract
        elif command == "subtract":
            subtract_func()
      #multiply
        elif command == "multiply":
            multiply_func()
       #divide
        elif command == "divide":
            divide_func()
       #quadratic equation/formula
        elif command == "quadratic formula" or command == "quadratic equation" or command == "qe":
            quadratic_equation_func()
        nl()

stupid_calc()
