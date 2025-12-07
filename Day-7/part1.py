from __future__ import annotations
from pygame import Vector2
from copy import deepcopy

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
        self.tachyon_positions: list[Vector2] = [deepcopy(start_position)]
        self.end_y = end_y
        self.line_length = line_length
        self.total_splits = 0
        self.total_created = 0
    
    def revalidate_tachyons(self):
        to_remove: list[int] = []
        for i, position in enumerate(self.tachyon_positions):
            for j, other in enumerate(self.tachyon_positions):
                if j != i and position == other and not j in to_remove:
                    to_remove.append(i)
                    break
        for index in sorted(to_remove, reverse=True):
            self.tachyon_positions.pop(index)
    
    def at_column(self, column: int) -> bool:
        for position in self.tachyon_positions:
            if position.x == column:
                return True
        return False

    # Returns whether the tachyons have reached the end.
    def update(self) -> bool:
        to_remove: list[int] = []
        to_append: list[Vector2] = []
        split_indices: list[int] = []
        for i, position in enumerate(self.tachyon_positions):
            position.y += 1
            if position in self.splitter_positions:
                self.total_splits += 1
                to_remove.append(i)
                moved_left = Vector2(position.x - 1, position.y)
                moved_right = Vector2(position.x + 1, position.y)
                to_append.append(moved_left)
                to_append.append(moved_right)

                if not self.at_column(moved_left.x):
                    split_indices.append(moved_left.x)
                if not self.at_column(moved_right.x):
                    split_indices.append(moved_right.x)
        for index in sorted(to_remove, reverse=True):
            self.tachyon_positions.pop(index)
        for val in to_append:
            self.tachyon_positions.append(val)
        self.revalidate_tachyons()
        self.total_created += len(set(split_indices))

        if self.tachyon_positions[0].y == self.end_y:
            return True
        
    def visualize(self):
        # for y in range(self.end_y + 1):
        #     for x in range(self.line_length):
        #         pos = Vector2(x, y)
        #         if pos == self.start_position:
        #             print("S", end="")
        #         elif pos in self.splitter_positions:
        #             print("^", end="")
        #         elif pos in self.tachyon_positions:
        #             print("|", end="")
        #         else:
        #             print(".", end="")
        #     print()
        print(f"Num tachyons: {len(self.tachyon_positions)}")
        print(f"Num splits: {self.total_splits}")

text = open("input.txt").read()
world = World.create_world(text)
while not world.update():
    continue
print(world.total_splits)