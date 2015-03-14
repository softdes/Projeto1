from random import randint

print("""
	How is your PARANORMALITY?
	Let's see how many steps you take
	to guess a number between 1 and 10
 
 """)
number = randint(1,10)
guess = -1
steps = 0

while number != guess:    
	guess = int(input("Please pick a number between 1 and 10 \n"))

	if guess < number:
		print("Too low")
	elif guess > number: # elif means else if
		print ("Too high")

if steps == 1:
	print("Congratulations! You are a medium!")
elif steps > 1 and steps < 4:
	print ("You have potential but need to develop your skills")
elif steps > 4:
	print ("I'm sorry to inform that you are a muggle")

