#By Isabelle.
#Checks a single number and lists all of its factors (except 1 and itself)

import math

num = int(input("Pick a number to undergo the primality test!\n"))
root = int(round(math.sqrt(num)))
prime = True
for looper in range(2,root + 1): #53225 should normally be 3
	if num % 2 == 0 or num % 3 == 0 or num % 5 == 0: #End if number is even
		print("{} is divisible by a prime number from 2 and 5. Silly you, stop wasting my time.".format(num))
		prime = False
		break
	elif looper % 2 == 0 or looper % 3 == 0 or looper % 5 == 0:
		continue
	else:
		if num % looper == 0:
			print("{} can be divided by {}.".format(num, looper))
			looper += 1
			prime = False
			break
		else:
			print("{} cannot be divided by {}.".format(num, looper)) #delete
			looper += 1
	        
if prime == True:
	print("{} is prime".format(num))
else:
	print("{} is not prime.".format(num))
