lines = open("input.txt").readlines()

def tokenize_line(line: str, split_indices: list[int], ignore_spaces=False) -> list[str]:
    token = ""
    out = []
    index = 0
    for char in line:
        if index in split_indices:
            out.append(token)
            token = ""
        if ignore_spaces and (char == " " or char == "\n"):
            continue
        token += char
        index += 1
    if token.strip() != "":
        out.append(token)
    return out

def get_oper_list(line: str) -> list[str]:
    out: list[str] = []
    for char in line:
        if char == "+" or char == "*":
            out.append(char)
    return out

def get_max_string_length(arr: list[str]) -> int:
    maximum = -1
    for item in arr:
        if len(item) > maximum:
            maximum = len(item)
    return maximum

split_indices: list[int] = []
raw_numbers = lines[:-1]
for i in range(len(raw_numbers[0])):
    all_space = True
    for line in raw_numbers:
        if line[i] != " ":
            all_space = False
            break
    if all_space:
        split_indices.append(i)

numbers, symbols = [tokenize_line(lines[i], split_indices) for i in range(len(lines[:-1]))], get_oper_list(lines[-1])
number_columns: list[list[str]] = [[] for _ in range(len(numbers[0]))]
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        number_columns[j].append(numbers[i][j])

out = 0
index = 0
for column in number_columns:
    max_len = get_max_string_length(column)
    to_add: list[int] = [0 for _ in range(max_len)]
    oper_type = symbols[index]
    place = 0
    this_total = 0
    for _ in range(max_len):
        this_number = ""
        for number in column:
            if place >= len(number):
                continue
            this_number += number[place]
        if this_number.strip() == "":
            place += 1
            continue
        this_number_int = int(this_number)
        if oper_type == "*":
            if this_total == 0:
                this_total = this_number_int
            else:
                this_total *= this_number_int
        elif oper_type == "+":
            this_total += this_number_int
        place += 1
    index += 1
    out += this_total

print(out)
