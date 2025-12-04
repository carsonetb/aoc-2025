lines = open("input.txt").readlines()

position = 50
password = 0

# Loop through each line, because there is an instruction every
# line.
for line in lines:
    # L moves in the negative direction (pretty arbitrary but
    # is consistent with the instructions), and R moves in the 
    # positive direction. This number will be multiplied by the 
    # difference instruction and then used to modify the position.
    if line[0] == "L":
        direction = -1
    elif line[0] == "R":
        direction = 1
    else:
        # First character is neither L nor R, which is expected.
        print("Malformed input.")

        # Quit so we don't run code where 'direction' isn't defined.
        quit()

    # Take everything in the line but the first character,
    # which is either L or R, this is the difference (non-signed
    # of course) the ticker is moving for this instruction.
    difference = int(line[1:])

    # This basically repeats the same instruction for as many 
    # times as the ticker will tick. There is certainly a better,
    # mathematical way to do this but the way this code works 
    # is certainly more intuitive, and easy to understand and write.
    for _ in range(difference):
        # Add only the direction this time, which is only -1 or 1.
        position += direction

        # Modulo the position by 100, meaning that if the position
        # is 100 it will be set to 0, and if it is -1 it will be set 
        # to 99.
        position = position % 100
        
        if position == 0:
            password += 1

print(password)