data = open("input.txt").read()

import textwrap
formatted: list[tuple[int, int]] = []
split_commas = data.split(",")
for item in split_commas:
    split_dash = item.split("-")
    formatted.append((int(split_dash[0]), int(split_dash[1])))

out = 0

def is_valid(item: int) -> bool:
    length = len(str(item))
    itemstr = str(item)
    if length == 2:
        check = str(item)[0]
        for char in str(item):
            if char != check:
                return False
        return True
    for i in range(1, length // 2 + 1):
        wrapped = textwrap.wrap(itemstr, i)
        if len(wrapped) != 2:
            continue
        valid = True
        check = wrapped[0]
        for sliced in wrapped:
            if sliced != check:
                valid = False
                break
        if not valid:
            continue
        return True
    return False

for item in formatted:
    for i in range(item[0], item[1] + 1):
        if is_valid(i):
            print(i)
            out += i
print(out)