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

circuits: list[list[Connection]] = []

def search_circuit(start_conn: Connection, already_searched: list[Connection] = []) -> tuple[list[Connection], list[Connection], int]:
    already_searched = list(set(already_searched))
    searched = 1
    out_arr: list[Connection] = [start_conn]
    if not start_conn in already_searched:
        already_searched.append(start_conn)
    for conn in start_conn.pos1_connections:
        if conn in already_searched:
            continue
        already_searched.append(conn)
        found_connections, searched_connections, this_searched = search_circuit(conn, already_searched)
        out_arr += found_connections
        already_searched += searched_connections
        searched += this_searched
    for conn in start_conn.pos2_connections:
        if conn in already_searched:
            continue
        already_searched.append(conn)
        found_connections, searched_connections, this_searched = search_circuit(conn, already_searched)
        out_arr += found_connections
        already_searched += searched_connections
        searched += this_searched
    return (out_arr, already_searched, searched)

def get_positions_from_circuit(circuit: list[Connection]) -> list[Vector3]:
    out: list[Vector3] = []
    for connection in circuit:
        if not connection.pos1 in out:
            out.append(connection.pos1)
        if not connection.pos2 in out:
            out.append(connection.pos2)
    return out

i = 0
while not len(connections) == 0:
    start_time = time.time()
    this_circuit, already_searched, searched = search_circuit(connections[0], [])
    end_time = time.time()
    for connection in this_circuit:
        connections.remove(connection)
    circuits.append(this_circuit)
    i += 1

circuit_positions: list[list[Vector3]] = []

for circuit in circuits:
    circuit_positions.append(get_positions_from_circuit(circuit))

circuit_positions = sorted(circuit_positions, key=lambda pos_list: len(pos_list), reverse=True)
out = len(circuit_positions[0]) * len(circuit_positions[1]) * len(circuit_positions[2])
print(out)