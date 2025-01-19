import random
import turtle
import math
import time
spawnPoint = 1000
woodenSword = 20
woodenPickaxe = 20
woodenShovel = 20
woodenAxe = 20
woodenHoe = 20
stoneSword = 20
stonePickaxe = 20
stoneShovel = 20
stoneAxe = 20
stoneHoe = 20
ironSword = 20
ironPickaxe = 20
ironShovel = 20
ironAxe = 20
ironHoe = 20
goldenSword = 20
goldenPickaxe = 20
goldenShovel = 20
goldenAxe = 20
goldenHoe = 20
diamondSword = 20
diamondPickaxe = 20
diamondShovel = 20
diamondAxe = 20
diamondHoe = 20
bow = 0
crossBow = 0
wood = 0
stone = 0
iron = 0
gold = 0
diamond = 0
achievement = 0
print("Creative or survival?")
answerOne = input()
if answerOne == "creative" or "Creative":
  print("generating world")
  print("What do you want to do")
  answerTwo = input()
  if answerTwo == mine:
    a = random.randint(1, 10)
    if a == 1:
      print("you mined wood")
      wood += 1
    if a == 2:
      print("you mined stone")
      stone += 1
    if a == 3:
      print("")
if answerOne == "survival" or "Survival":
  print("generating world")
  print("What do you want to do")
  answerTwo = input()
  if answerTwo == "mine" or "Mine":
    a = random.randint(1, 10)
    if a == 1:
      print("you mined wood")
      wood += 1
    if a == 2:
      print("you mined stone")
      stone += 1
    if a == 3:
      print("you mined iron!")
      print("you earned an achievement")
      achievement += 1
    if a == 4:
      print("you mined gold")
      achievement+= 1
    if a == 5:
        print("you mined diamond")
        


