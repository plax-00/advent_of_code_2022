with open('input.txt', 'r') as f:
    input = f.read()

def main(window_size):
    chars = {}
    start = 0
    end = window_size

    def add_to_chars(char):
        if not chars.get(char):
            chars[char] = 1
        else:
            chars[char] += 1


    for char in input[start:end]:
        add_to_chars(char)

    while True:
        if len(chars) == window_size:
            break

        if chars[input[start]] == 1:
            chars.pop(input[start])
        else:
            chars[input[start]] -= 1
        start += 1

        add_to_chars(input[end])
        end += 1

    return end

print(f'Part one: {main(4)}')
print(f'Part two: {main(14)}')

