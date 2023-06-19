from math import floor

class hexAssign:
    def __init__(self):

        self.desertNum: int = 0
        self.hillNum: int = 0
        self.forestNum: int = 0
        self.mountainNum: int = 0
        self.fieldNum: int = 0
        self.pastureNum: int = 0

    def generateTerrain(self, radius: int = 3):
        hex_count: int = self.hexCounter(radius)
        sfloor, mfloor, hfloor = self.hexDivider(hex_count)
        hexes_assigned = self.hexAssigner(sfloor, mfloor, hfloor)

        return hexes_assigned

    def hexCounter(self, radius):
        if type(radius) is int and radius > 1:
            # derived from mathematics
            return 3 * radius * (radius - 1) + 1
        elif radius == "large":
            return 30
        else:
            raise Exception("Radius must be an integer greater than 1")

    def hexDivider(self, hex_count):
        small = hex_count / 20
        medium = hex_count / 5
        large = hex_count / 8

        small_floor = floor(small)
        medium_floor = floor(medium)
        large_floor = floor(large)

        leftover_hexes = hex_count - (small_floor + 2 * medium_floor + 2 * large_floor)
        if leftover_hexes > 0:
            division_remainders = [small - small_floor, medium - medium_floor, large - large_floor]
            division_remainders.sort(reverse=1)

        #leftover_hexes = hex_count - (3*floor20 + 2*floor16 + floor5)
        return (small_floor, medium_floor, large_floor)

    def hexAssigner(self, small_floor: int, medium_floor: int, large_floor: int):
        self.desert = small_floor
        self.hills = medium_floor
        self.mountains = medium_floor
        self.forest = large_floor
        self.field = large_floor
        self.pasture = large_floor

        return f"{self.desert}, {self.hills}, {self.mountains}, {self.forest}, {self.field}, {self.pasture}"