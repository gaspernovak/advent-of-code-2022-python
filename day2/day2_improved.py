
games = []

with open('input.txt', 'r') as text:
    games = [choices.split() for choices in text]
    
#my choices
#rock - X
#paper - Y
#scissors - Z

opponent_choices = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

choice_values = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

beats = {
    "X": "Z",
    "Y": "X",
    "Z": "Y"
}

def part1():
    total_score = 0
    for game in games:
        if opponent_choices[game[0]] == game[1]:
            total_score += 3 + choice_values[game[1]] # draw
        elif beats[opponent_choices[game[0]]] == game[1]:
            total_score += choice_values[game[1]] #opponent wins
        else:
            total_score += choice_values[game[1]] + 6 #you win
    return total_score

def part2():
    total_score = 0
    for game in games:
        if game[1] == "Y":
            total_score += 3 + choice_values[beats[opponent_choices[game[0]]]] # draw
        elif game[1] == "X":
            total_score += choice_values[beats[opponent_choices[game[0]]]] #opponent wins
        else:
            if choice_values[beats[opponent_choices[game[0]]]] == 3:
                total_score += 6 + 1
            else:
                total_score += 6 + choice_values[beats[opponent_choices[game[0]]]] + 1
            
    return total_score
    pass

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")