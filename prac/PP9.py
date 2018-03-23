import random

num = random.randint(1,9)
print("The seed is %s" % num)

counter = 1

while True:
	inp = int(input("guess the number"))
	
	if inp == num:
		print("you are right")
		break
	elif inp > num:
		print("High")
	else:
		print("Low")
		
	counter += 1

print("You guessed the number in %s chances" % counter)