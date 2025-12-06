split_double_newline = open("input.txt").read().split("\n\n")
ranges = split_double_newline[0].splitlines()
available = split_double_newline[1].splitlines()

tuple_ranges: list[tuple[int, int]] = []
all_fresh = []
for i in range(len(ranges)):
    line = ranges[i]
    low, high = line.split("-")
    tuple_ranges.append((int(low), int(high)))

out = 0

for item in available:
    for tuple_range in tuple_ranges:
        if int(item) >= tuple_range[0] and int(item) <= tuple_range[1]:
            out += 1
            break

print(out)