rucksacks = []

with open('input.txt', 'r') as text:
    rucksacks = text.read().split("\n")
    rucksacks = [[item[:int(len(item)/2)], item[int(len(item)/2):]] for item in rucksacks]

def char_to_alphabet_index(letter):
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter.lower()) - (96 - 26)

def part1():
    numbers = []
    for item in rucksacks:
        words = []
        for word in item:
            words.append(set([letter for letter in word]))
        words = (list(words[0].intersection(words[1])))
        for i in words:
            numbers.append(char_to_alphabet_index(i))
    return sum(numbers)

def part2():
    groups = list(zip(*[iter([item[0]+item[1] for item in rucksacks])]*3))
    badges = []
    for group in groups:
        letters = []
        for item in group:
            letters.append(set([letter for letter in item]))
        badges.append(char_to_alphabet_index(list(letters[0].intersection(letters[1]).intersection(letters[2]))[0]))
    return sum(badges)

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
