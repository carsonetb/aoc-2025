ranges = open("input.txt").read().splitlines()

def conv_tuple(string: str) -> tuple[int, int]:
    return (int(string.strip().split("-")[0]), int(string.strip().split("-")[1]))

for i in range(len(ranges)):
    ranges[i] = conv_tuple(ranges[i])

ranges = sorted(ranges, key=lambda arg: arg[0], reverse=False)

out = 0
index = 0
while True:
    this = ranges[index]
    next_item = ranges[index + 1]
    if next_item[0] <= this[1]:
        # It is possible that the next one is *inside* of this one, so we need to max the highs.
        ranges[index] = (this[0], max(this[1], next_item[1]))
        ranges.pop(index + 1)
    else:
        out += this[1] - this[0] + 1
        index += 1
    if index == len(ranges) - 1:
        break

out += ranges[-1][1] - ranges[-1][0] + 1
print(out)