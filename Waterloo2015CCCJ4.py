#Problem J4: Arrival Time

departure_time = input()
split_departure = list(departure_time) #The time of departure, split into a list.

#Split the list
departure_hour = split_departure[0:2]
departure_minute = split_departure[3:5]

#Change the split list to integers.
departure_hour = int("".join(departure_hour))
departure_minute = int("".join(departure_minute))

#The start and end of the rush hours
rh_start_1 = 7
rh_end_1 = 10
rh_start_2 = 15
rh_end_2 = 19

#Set the current time
hour = departure_hour
minute = departure_minute
#For the 120 minutes it usually takes Fiona to commute
for counter in range(1, 121):
    #If it's currently rush hour
    if hour >= rh_start_1 and hour < rh_end_1 or hour >= rh_start_2 and hour < rh_end_2:
        #Twice as slow if rush hour
        minute += 2
    else:
        #Normal speed if normal time
        minute += 1
    if minute >= 60:
        minute = 0
        #Reset hour
        hour += 1
    if hour == 24:
        hour = 0

#Add fake zeroes if required.
if hour < 10:
    hour = str(hour)
    hour = "0" + hour
if minute < 10:
    minute = str(minute)
    minute = "0" + minute

#Make a valid output.
output = hour , ":" , minute
output = "".join(output)
print(output)
