x = 1000
while x > 0:
    print("what do you want to do")
    answer = input()
    if answer == "Set a 60 minute timer":
        time.sleep(60)
        print("60 seconds is done")
    if answer == "Random Number":
        import random
        x = random.randint(1, 6)
        print(x)
    
    
