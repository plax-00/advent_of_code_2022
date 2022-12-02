with open('input.txt', 'r') as f:
    calories = []
    elf_sum = 0
    for line in f.readlines():
        food = line[:-1]
        if food:
            elf_sum += int(food)
        else:
            calories.append(elf_sum)
            elf_sum = 0
    calories.append(elf_sum)
    calories.sort(reverse=True)


print(f'Part one: {calories[0]}')
print(f'Part two: {sum(calories[:3])}')
