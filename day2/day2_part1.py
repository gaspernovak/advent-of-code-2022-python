
with open('input.txt', 'r') as text:
    choices = text.read().split()
    #choices = [choices.split() for choices in text]
    print(choices)
    
total_score = 0
for i in range(len(choices)):
    if choices[i] == "A":
        my_choice = choices[i+1]
        if my_choice == "Y":
            total_score += 6 + 2
        elif my_choice == "X":
            total_score += 3 + 1
        elif my_choice == "Z":
            total_score += 0 + 3

    if choices[i] == "B":
        my_choice = choices[i+1]
        if my_choice == "X":
            total_score += 0 + 1
        elif my_choice == "Y":
            total_score += 3 + 2
        elif my_choice == "Z":
            total_score += 6 + 3

    if choices[i] == "C":
        my_choice = choices[i+1]
        if my_choice == "Z":
            total_score += 3 + 3
        elif my_choice == "Y":
            total_score += 0 + 2
        elif my_choice == "X":
            total_score += 6 + 1

print(total_score)