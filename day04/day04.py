with open('input.txt', 'r') as f:
    input = f.read().split('\n')[:-1]

sum1 = 0
sum2 = 0

for line in input:
    # The first and second ranges as lists of ints
    range1 = [int(i) for i in line.split(',')[0].split('-')]
    range2 = [int(i) for i in line.split(',')[1].split('-')]

    # If the ranges have the same start or end they will always overlap
    if range1[0] == range2[0] or range1[1] == range2[1]:
        sum1 += 1
        sum2 += 1
        continue

    # Check for complete overlaps by comparing the starts and ends of the ranges
    if (range1[0] > range2[0] and range1[1] < range2[1]) or (range2[0] > range1[0] and range2[1] < range1[1]):
        sum1 += 1
        sum2 += 1
        continue

    # Check for partial overlaps
    if (range1[0] < range2[0] and range1[1] >= range2[0]) or (range2[0] < range1[0] and range2[1] >= range1[0]):
        sum2 += 1


print(f'Part one: {sum1}')
print(f'Part two: {sum2}')
