from __future__ import annotations
from pygame import Vector2
from copy import deepcopy, copy

class Tachyon:
    def __init__(self, position: Vector2, paths: int = 1):
        self.position = position
        self.paths = paths

class World:
    @staticmethod
    def create_world(string: str) -> World:
        lines = string.splitlines()
        start_position: Vector2 | None = None
        splitter_positions: list[Vector2] = []
        end_y: int = len(lines) - 1
        line_length: int | None = None
        for y, line in enumerate(lines):
            line_length = len(line)
            for x, char in enumerate(lines[y]):
                if char == "S":
                    start_position = Vector2(x, y)
                if char == "^":
                    splitter_positions.append(Vector2(x, y))
        return World(start_position, splitter_positions, end_y, line_length)

    def __init__(self, start_position: Vector2, splitter_positions: list[Vector2], end_y: int, line_length: int):
        self.start_position = start_position
        self.splitter_positions: list[Vector2] = splitter_positions
        self.tachyons: list[Tachyon] = [Tachyon(deepcopy(start_position))]
        self.end_y = end_y
        self.line_length = line_length
    
    def exists(self, pos: Vector2) -> Tachyon | None:
        for tachyon in self.tachyons:
            if tachyon.position == pos:
                return tachyon
    
    def propogate_path(self, pos: Vector2, to_move: Tachyon):
        at_new = self.exists(pos)
        if at_new:
            at_new.paths += to_move.paths
        else:
            self.tachyons.append(Tachyon(pos, to_move.paths))
        
    # Returns whether the tachyons have reached the end.
    def update(self) -> bool:
        initial_tachyons = copy(self.tachyons)
        for tachyon in initial_tachyons:
            if tachyon.position in self.splitter_positions:
                self.propogate_path(Vector2(tachyon.position.x - 1, tachyon.position.y + 1), tachyon)
                self.propogate_path(Vector2(tachyon.position.x + 1, tachyon.position.y + 1), tachyon)
                self.tachyons.remove(tachyon)
            else:
                tachyon.position.y += 1
        
        if self.tachyons[0].position.y == self.end_y:
            return True
        
    def visualize(self):
        for y in range(self.end_y + 1):
            for x in range(self.line_length):
                pos = Vector2(x, y)
                if pos == self.start_position:
                    print("S", end="")
                elif pos in self.splitter_positions:
                    print("^", end="")
                elif self.exists(pos):
                    print("|", end="")
                else:
                    print(".", end="")
            print()
        print(f"Num paths: {self.get_total_paths()}")
    
    def get_total_paths(self) -> int:
        out = 0
        for tachyon in self.tachyons:
            out += tachyon.paths
        return out

text = open("input.txt").read()
world = World.create_world(text)
while not world.update():
    continue
print(world.get_total_paths())