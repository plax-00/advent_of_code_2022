from copy import deepcopy

with open('input.txt', 'r') as f:
    input = f.read()

# Get only the lines containing the stacks of crates
stack_lines = input.split('\n\n')[0].split('\n')[:-1]

# Get number of stacks from the stack numbering
num_stacks = [int(c) for c in input.split('\n\n')[0].split('\n')[-1].split()][-1]

# Initialize stacks as empty lists
stacks = [[] for _ in range(num_stacks)]

# Some cursed loops to get the input into a usable format
for line in reversed(stack_lines):
    for i, j in zip(range(num_stacks), range(0, len(stack_lines[0]), 4)):
        if line[j + 1] != ' ':
            stacks[i].append(line[j + 1])

# A slightly less cursed loop to get the instructions into a usable format
instructions = []
for line in input.split('\n\n')[1].split('\n')[:-1]:
    instructions.append([int(num) for ind, num in enumerate(line.split(' ')) if ind % 2 != 0])

# Pop and append according to the instructions
def part_one(stacks):
    for inst in instructions:
        for _ in range(inst[0]):
            source = stacks[inst[1] - 1]
            dest = stacks[inst[2] - 1]
            dest.append(source.pop())

    top_row = ''.join([stack[-1] for stack in stacks])
    print(f'Part one: {top_row}')

# Follow instructions with list slicing and extending
def part_two(stacks):
    for inst in instructions:
        stacks[inst[2] - 1].extend(stacks[inst[1] - 1][-inst[0]:])
        stacks[inst[1] - 1] = stacks[inst[1] - 1][:-inst[0]]

    top_row = ''.join([stack[-1] for stack in stacks])
    print(f'Part two: {top_row}')

part_one(deepcopy(stacks))
part_two(deepcopy(stacks))
