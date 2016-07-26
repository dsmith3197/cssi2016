from random import randint 

answer = randint(1,10)
guessed = False

while guessed != True:
	print "-" * 80
	guess = input('Guess a number between 1-10\n')
	print "*" * 80
	if guess == answer:
		print "You got it!"
		guessed = True
	elif guess > answer:
		print "Too high"
	else:
		print "Too low" 