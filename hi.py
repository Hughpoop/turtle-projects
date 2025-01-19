import random
def function_one():
    numberGuess = random.randint(1, 100)
    input = ("type in a number if your number is greater than the computers number it will say so and same for the less")
    print("press 'q' to quit the program (remember to lowercase)")
while input <> numberGuess:
    function_one()
    
    
