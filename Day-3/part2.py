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
    search_start_index = 0
    this = 0
    for battery in range(12, 0, -1):
        largest_index = find_largest(line[:(-(battery-1) if battery-1 > 0 else len(line)+1)][search_start_index:]) + search_start_index
        search_start_index = largest_index + 1
        this += int(line[largest_index]) * 10**(battery-1)
    out += this

print(out)