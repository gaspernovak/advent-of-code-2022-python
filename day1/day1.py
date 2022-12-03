inventory_sums = []
top_three = []
sum_totals = 0
with open('sample_input.txt', 'r') as text:
    lines = text.read().split("\n\n")
    inventory = [line.split("\n") for line in lines]
    for col in range(len(inventory)):
        for row in range(len(inventory[col])):
            sum_totals += int(inventory[col][row])
        inventory_sums.append(sum_totals)
        sum_totals = 0

print(f"Part 1: {max(inventory_sums)}")

for i in range(3):
    top_three.append(max(inventory_sums))
    inventory_sums.remove(top_three[-1])

print(f"Part 2: {sum(top_three)}")
