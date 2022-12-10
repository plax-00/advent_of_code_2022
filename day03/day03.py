with open('input.txt', 'r') as f:
    input = f.read().split('\n')[:-1]

sum1 = 0
sum2 = 0

# Function that uses ascii values to return priority as defined by the problem
def get_priority(char):
    ascii = ord(char)
    if ascii > 96:
        return ascii - 96
    else:
        return ascii - 38

for line in input:
    # Split the string into two halves
    mid = len(line) // 2
    comp1 = line[:mid]
    comp2 = line[mid:]

    # Dictionary for all characters in the first half
    comp1_dict = {}
    for char in comp1:
        comp1_dict[char] = True

    # For each char in the second half lookup in the dict
    for char in comp2:
        if comp1_dict.get(char) is not None:
            sum1 += get_priority(char)
            break

# Go through input in groups of 3
for i in range(0, len(input), 3):
    group = [input[i], input[i+1], input[i+2]]

    # Dict of all chars in first elf
    elf1 = {}
    for char in group[0]:
        elf1[char] = True

    # Dict of only matching chars in second elf
    elf2 = {}
    for char in group[1]:
        if elf1.get(char) is not None:
            elf2[char] = True

    # Chars in elf 3 matching the elf2 dict must match in all 3 elves
    for char in group[2]:
        if elf2.get(char) is not None:
            sum2 += get_priority(char)
            break

print(f'Part one: {sum1}')
print(f'Part two: {sum2}')
