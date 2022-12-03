with open('input.txt', 'r') as text:
    choices = text.read().split()

total_score = 0

# X - lose
# Y - draw
# Z - win

rock = 1
paper = 2
scissors = 3

for i in range(len(choices)):
    if choices[i] == "A":
        my_choice = choices[i+1]
        if my_choice == "X":
            total_score += 0 + scissors
        elif my_choice == "Y":
            total_score += 3 + rock
        elif my_choice == "Z":
            total_score += 6 + paper

    if choices[i] == "B":
        my_choice = choices[i+1]
        if my_choice == "X":
            total_score += 0 + 1
        elif my_choice == "Y":
            total_score += 3 + paper
        elif my_choice == "Z":
            total_score += 6 + scissors

    if choices[i] == "C":
        my_choice = choices[i+1]
        if my_choice == "X":
            total_score += 0 + paper
        elif my_choice == "Y":
            total_score += 3 + scissors
        elif my_choice == "Z":
            total_score += 6 + rock

print(total_score)