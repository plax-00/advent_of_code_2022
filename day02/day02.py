with open('input.txt') as f:
    input = f.readlines()

score1 = 0
score2 = 0

for line in input:
    match line:
        case 'A X\n':
            score1 += 1
            score1 += 3

            score2 += 3
        case 'B X\n':
            score1 += 1

            score2 += 1
        case 'C X\n':
            score1 += 1
            score1 += 6

            score2 += 2
        case 'A Y\n':
            score1 += 2
            score1 += 6

            score2 += 1
            score2 += 3
        case 'B Y\n':
            score1 += 2
            score1 += 3

            score2 += 2
            score2 += 3
        case 'C Y\n':
            score1 += 2

            score2 += 3
            score2 += 3
        case 'A Z\n':
            score1 += 3

            score2 += 2
            score2 += 6
        case 'B Z\n':
            score1 += 3
            score1 += 6

            score2 += 3
            score2 += 6
        case 'C Z\n':
            score1 += 3
            score1 += 3

            score2 += 1
            score2 += 6

print(f'Part one: {score1}')
print(f'Part two: {score2}')
