instructions = ("R3, R1, R4, L4, R3, R1, R1, L3, L5, L5, L3, R1, R4, L2,"
                " L1, R3, L3, R2, R1, R1, L5, L2,"
                " L1, R2, L4, R1, L2, L4, R2, R2,"
                " L2, L4, L3, R1, R4, R3, L1, R1, L5, R4, L2, R185, L2,"
                " R4, R49, L3, L4, R5, R1, R1, L1,"
                " L1, R2, L1, L4, R4, R5, R4, L3, L5, R1, R71, L1, R1,"
                " R186, L5, L2, R5, R4, R1, L5, L2, R3,"
                " R2, R5, R5, R4, R1, R4, R2, L1, R4, L1, L4, L5,"
                " L4, R4, R5, R1, L2, L4, L1, L5, L3, L5,"
                " R2, L5, R4, L4, R3, R3, R1, R4, L1, L2, R2, L1,"
                " R4, R2, R2, R5, R2, R5, L1, R1, L4, R5, R4, R2,"
                " R4, L5, R3, R2, R5, R3, L3, L5, L4, L3,"
                " L2, L2, R3, R2, L1, L1, L5, R1, L3, R3, R4, R5,"
                " L3, L5, R1, L3, L5, L5, L2, R1, L3, L1,"
                " L3, R4, L1, R3, L2, L2, R3, R3, R4, R4, R1, L4, R1, L5"
                )


current_direction = ['N', 'E', 'S', 'W']

movement = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }

current_state = 0  # index of the direction I am in
current_positions = [0, 0]
instructions = instructions.split(', ')

visited = [[0, 0]]

for each in instructions:
    if each[0] == "L":
        current_state = (current_state - 1) % 4
    else:
        current_state = (current_state + 1) % 4

    for step in range(int(each[1:])):
        curr_move = movement[current_direction[current_state]]
        current_positions[0] += curr_move[0]
        current_positions[1] += curr_move[1]
        if current_positions not in visited:
            visited.append([current_positions[0], current_positions[1]])
        else:
            print(abs(current_positions[0]) + abs(current_positions[1]))
            exit()  
    print(each, current_positions)
print(abs(current_positions[0]) + abs(current_positions[1]))
