import random
import time
integerPoint = 0
randomOne = random.randint(0, 10)
print(“This game defines a number guessing game”)
time.sleep(2)
print(“In this game you are required to guess numbers”)
time.sleep(2)
print(“3...2...1...”)
time.sleep(3)
print(“GO!!!!!!!!!”)
answerOne = int(input( Guess number 1-10!))
if answerOne = randomOne:
	integerPoint += 1 
    print(“good job you answered correctly”)
    time.sleep(2)
    print(“this time you have to guess a number 1-20”)
    randomTwo = random.randint(1-20)
    print(“3...2...1… Go!!!”)
    answerTwo = int(input(Go guess a number 1-20))
    if answerTwo = randomTwo:
        print(“ Good Job onto the next level”)
    else:
	print(“Sorry you died try next time”)
else:
	print(“Sorry you died try next time”)
	
