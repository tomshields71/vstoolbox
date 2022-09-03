import random

fname = input("What is your first name? ")

shoes = input("What shoes do you like? ")
if shoes == "Converse" or shoes == "converse":
   print("Nice, casual is always in!")
elif shoes == "Nike" or shoes == "nike":
   print("Just do it!")
else:
   print("Those are nice too.")

age = int(input("How old are you? "))
if age <= 18:
   print(str(age) + " is a good age to start exploring style.")
elif age < 25:
   print("Pretty close to knowing your style.")
else:
   print("You must have a good sense of your style already.")

print("I think I might know your style.")

top = input("So, " + fname + ", what is your favorite top? ")

r = random.randint(1, 3)
if r == 1:
   print("That’s a good choice.")
elif r == 2:
   print("Sounds nice.")
else:
   print("How unusual.")

bottom = input("What about your choice of bottom? ")
if bottom == "cargo pants":
   print("I also like cargo pants.")
else:
   print("I like those as well.")

print("You can’t go wrong with those")

x = input("Anything else you want to add? ")
print("Well, " + fname + ", it was awesome getting to know your style.")