lines = open("input.txt").readlines()

def find_largest(line: str) -> int:
    largest = 0
    largest_index = -1
    index = 0
    for character in line:
        as_int = int(character)
        if as_int > largest:
            largest = as_int
            largest_index = index
        index += 1
    return largest_index

out = 0

for line in lines:
    line = line.strip()
    largest_index = find_largest(line[:-1])
    second_largest_index = find_largest(line[largest_index + 1:]) + largest_index + 1
    out += int(line[largest_index]) * 10 + int(line[second_largest_index])

print(out)