# GAME SCORES MANAGER
# Topics: read(n) | readlines() | Loop Through File | Filter Lines | Copy Odd Lines

# PART 1 -- Quick Preview
n = int(input("How many characters do you want to preview? "))
file = open("game-scores.txt", "r")
print(file.read(n))
file.close()
print()

# PART 2 -- All Scores as a List
file = open("game-scores.txt", "r")
lines = file.readlines()
file.close()

print("Total scores:", len(lines))
for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())
print()

# PART 3 -- Filter Scores
word = input("Hide scores starting with: ")
file = open("game-scores.txt", "r")

for line in file:
    if line.startswith(word):
        print("hide ->", line.strip())
    else:
        print("show ->", line.strip())

file.close()
print()

# PART 4 -- Copy Odd Scores to New File
file = open("game-scores.txt", "r")
lines = file.readlines()
file.close()

out = open("odd-scores.txt", "w")

for i in range(0, len(lines), 2):
    out.write(lines[i])

out.close()

print("Odd scores saved to odd-scores.txt")