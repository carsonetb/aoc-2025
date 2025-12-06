lines = open("input.txt").readlines()
numbers, symbols = lines[:-1], lines[-1]

def tokenize_line(line: str) -> list[str]:
    token = ""
    out = []
    for char in line:
        if (char == " " or char == "\n")and not token == "":
            out.append(token)
            token = ""
        if char == " " or char == "\n":
            continue
        token += char
    if token != "":
        out.append(token)
    return out

tokenized_numbers = []
for line in numbers:
    tokenized_numbers.append(tokenize_line(line))

tokenized_symbols = tokenize_line(symbols)

sums_products: list[int] = [0 for _ in range(len(tokenized_symbols))]

for i in range(len(tokenized_symbols)):
    sum_product = int(tokenized_numbers[0][i])
    add_type = tokenized_symbols[i]
    for j in range(1, len(tokenized_numbers)):
        if add_type == "*":
            sum_product *= int(tokenized_numbers[j][i])
        elif add_type == "+":
            sum_product += int(tokenized_numbers[j][i])
    sums_products[i] = sum_product

print(sum(sums_products))