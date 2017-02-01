############################################################
#Virtual elevator settings
max_floor = 51 #the highest floor possible for the elevator
min_floor = 2 #the lowest floor possible for the elevator
resting_floor = int(round((max_floor + min_floor)/2))
#The floor the elevator rests on, because it's halfway

############################################################

#helper functions

#Get the absolute value of a number.
def absolute_difference(value1, value2):
    difference = value1 - value2
    if difference >= 0:
        return difference
    else:
        return -difference #If the number is below 0, return the positive form of it.
    
#Force user to enter a valid integer
def force_number(message):
    while True:
        try:
            number = int(input(message))
            break
        except: #if there's an error
            print("Please enter a valid integer!!!")
    return number

#THE ERROR LIES HERE
def real_floor(message):
  floor = force_number(message)
  while (floor < min_floor or floor > max_floor):
    print("The elevator can't go on that floor!")
    floor = int(input(message))
  else:
    return floor
    
  
############################################################   

def elevate(pressed_floor, desired_floor): #Elevator for 1 person
    
    current_floor = resting_floor
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
          
your_floor = real_floor("Which floor are you currently on?")
destination = real_floor("Which floor do you want to go to?")
elevate(your_floor, destination)
