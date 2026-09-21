import random
print("Dice Rolling Simulator")
while True:
    dice = random.randint(1,6)
    print("You rolled a", dice)
    choice = input("Do you want to rool again? ")
    if choice.lower() == "no":
        print("Thanks for playing!")
        break
    elif choice.lower() != "yes":
        print("I dont understand that, rolling again...")