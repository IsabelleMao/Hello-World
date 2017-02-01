############################################################
#helper functions
def absolute_difference(value1, value2): #get the absolute value of a number.
    difference = value1 - value2
    if difference >= 0:
        return difference
    else:
        return -difference #If the number is below 0, return the positive form of it.
    
def force_number(message): #force user to enter a valid integer
    while True:
        try:
            number = int(input(message))
            break
        except ValueError:
            print("Please enter a valid integer!!!")
        except NameError:
            print("Please enter a valid integer!!!")
        except SyntaxError:
            print("Please enter a valid integer!!!")
        except TypeError:
            print("Please enter a valid integer!!!")
    return number

############################################################    

#Virtual elevator settings
max_floor = 36
min_floor = -1
resting_floor = (absolute_difference(max_floor, min_floor))/2


def elevate(pressed_floor, desired_floor): #Elevator for 1 person
    
    current_floor = 1
    print("The elevator is currently on floor {}".format(current_floor))
    
    while(current_floor != pressed_floor): #If the elevator is not at the current floor yet
        
    #Get the elevator to pick up the person
        if(current_floor < pressed_floor): #if elevator is lower
            current_floor += 1 #go up
            print("The elevator is now on floor {}".format(current_floor))
        else:
            current_floor -= 1 #go down
            print("The elevator is now on floor {}".format(current_floor))
    print("The elevator has picked you up.")
    
    pre_difference = pressed_floor - desired_floor
    difference = absolute_difference(pressed_floor, desired_floor) 
    for i in range(difference):
        if (current_floor > desired_floor): #if you want to go down
            current_floor -= 1
            print("The elevator goes down, to floor {}".format(current_floor))
        else:
            current_floor += 1
            print("The elevator goes up, to floor {}".format(current_floor))
    print("You're here!")
          
your_floor = force_number("Which floor are you currently on?")
destination = force_number("Which floor do you want to go to?")
elevate(your_floor, destination)
