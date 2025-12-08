from pygame import Vector3
import time
import sys

sys.setrecursionlimit(3000)

lines = open("input.txt").readlines()
positions: list[Vector3] = []
for line in lines:
    split_space = line.strip().split(",")
    positions.append(Vector3(int(split_space[0]), int(split_space[1]), int(split_space[2])))

class Connection:
    def __init__(self, pos1: Vector3, pos2: Vector3):
        self.pos1 = pos1
        self.pos2 = pos2
        self.distance = pos1.distance_to(pos2)
        self.pos1_connections: list[Connection] = []
        self.pos2_connections: list[Connection] = []
    
    def __str__(self):
        return f"<Connection from {self.pos1} to {self.pos2} with distance {self.distance}>"

    def __repr__(self):
        return f"<Connection from {self.pos1} to {self.pos2} with distance {self.distance}>"

def get_positions_in_circuit(start_con: Connection, searched_positions: dict[float, bool]) -> list[Vector3]:
    out_arr: list[Vector3] = []
    if not searched_positions.get(start_con.pos1.length()):
        searched_positions[start_con.pos1.length()] = True
        out_arr.append(start_con.pos1)
        for conn in start_con.pos1_connections:
            out_arr += get_positions_in_circuit(conn, searched_positions)
    if not searched_positions.get(start_con.pos2.length()):
        searched_positions[start_con.pos2.length()] = True
        out_arr.append(start_con.pos2)
        for conn in start_con.pos2_connections:
            out_arr += get_positions_in_circuit(conn, searched_positions)
    return out_arr

connected_by_positions: dict[float, Connection] = {}

possible_connections: list[Connection] = []
for pos1 in positions:
    for pos2 in positions:
        if pos1 != pos2:
            hashable_conn = pos1.distance_to(pos2)
            if connected_by_positions.get(hashable_conn):
                continue
            possible_connections.append(Connection(pos1, pos2))
            connected_by_positions[hashable_conn] = possible_connections[-1]

possible_connections = sorted(possible_connections, key=lambda connection: connection.distance)

connections: list[Connection] = []

for this_connection in possible_connections:
    connections.append(this_connection)
    for connection in connections:
        if this_connection.pos1 == connection.pos1:
            this_connection.pos1_connections.append(connection)
            connection.pos1_connections.append(this_connection)
        if this_connection.pos2 == connection.pos1:
            this_connection.pos2_connections.append(connection)
            connection.pos1_connections.append(this_connection)
        if this_connection.pos1 == connection.pos2:
            this_connection.pos1_connections.append(connection)
            connection.pos2_connections.append(this_connection)
        if this_connection.pos2 == connection.pos2:
            this_connection.pos2_connections.append(connection)
            connection.pos2_connections.append(this_connection)
    circuit_length = len(get_positions_in_circuit(this_connection, {}))
    if circuit_length == len(positions):
        print(this_connection.pos1.x * this_connection.pos2.x)
        quit()