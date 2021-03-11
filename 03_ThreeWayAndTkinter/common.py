from dataclasses import dataclass

@dataclass
class Coords:
    row: int
    column: int

class ButtonMeta:
    def __init__(self, coords: Coords, handler):
        self.coords = coords
        self.handler = handler