print("Game score manager")
print("1. Add Score")
print("2. View Scores")
print("3. Exit")
choice = input("Enter your choice: ")
if choice == "1":
    name = input("Enter your name: ")
    score = input("Enter your score: ")

    file = open("scores.txt", "a")
    file.write(name + " - " + score + "\n")
    file.close()
    print("Your score has been saved!")
elif choice == "2":
    file = open("scores.txt", "r")
    scores = file.readlines()
    file.close()
    print("\n All scores")
    if len(scores) == 0:
        print("There are no scores yet.")
    else:
        for i in scores:
            print(i.strip())
elif choice == "3":
    print("Thanks for using the game score manager!")
else:
    print("That is not a valid option.")
