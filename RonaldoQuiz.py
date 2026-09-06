score = 0
print(" " * 50 + "Score:", score)
print()
print("===== RONALDO QUIZ =====")
print()

print("1. How many Champions Leagues does Ronaldo have?")
print("A. 3")
print("B. 6")
print("C. 5")
answer = input("Answer: ")
if answer.upper() == "C":
    score += 10
    print("Correct! +10")
else:
    score -= 5
    print("Wrong! -5")
print()
print(" " * 50 + "Score:", score)
print()

print("2. How many times did Ronaldo win the Ballon d'Or?")
print("A. 8")
print("B. 2")
print("C. 5")
answer = input("Answer: ")
if answer.upper() == "C":
 score += 10
 print("Correct! +10")
else:
 score -= 5
print("Wrong! -5")
print()
print(" " * 50 + "Score:", score)
print()
print("3. Who is better Messi or Ronaldo?")
print("A. Messi")
print("B. Ronaldo")
answer = input("Answer: ")
if answer.upper() == "B":
    score += 10
    print("Correct! +10")
else:
    score -= 5
    print("Wrong! -5")
print()
print("===== QUIZ FINISHED =====")
print("Final Score:", score)