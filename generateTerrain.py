import math

class HexesAssigned:
    
    
    desert = 0
    hills = 0
    forest = 0
    mountains = 0
    field = 0
    pasture = 0

    def __str__(self):
        return f"{self.desert}, {self.hills}, {self.mountains}, {self.forest}, {self.field}, {self.pasture}"

def hexCounter(radius):
    if type(radius) is int and radius > 1:
        # derived from mathematics
        return 3 * radius * (radius - 1) + 1
    elif radius == "large":
        return 30
    else:
        raise Exception("Radius must be an integer greater than 1")

def hexAssigner(hex_count):
    hexesAssigned = HexesAssigned()

    small = hex_count / 20
    medium = hex_count / 5
    large = hex_count / 8

    small_floor = math.floor(small)
    medium_floor = math.floor(medium)
    large_floor = math.floor(large)

    leftover_hexes = hex_count - (small_floor + 2 * medium_floor + 2 * large_floor)
    if leftover_hexes > 0:
        division_remainders = [small - small_floor, medium - medium_floor, large - large_floor]
        division_remainders.sort(reverse=1)



    hexesAssigned.desert = small_floor
    hexesAssigned.hills = medium_floor
    hexesAssigned.mountains = medium_floor
    hexesAssigned.forest = large_floor
    hexesAssigned.field = large_floor
    hexesAssigned.pasture = large_floor


    #leftover_hexes = hex_count - (3*floor20 + 2*floor16 + floor5)
            
    return hexesAssigned

def generateTerrain(radius = 3):
    hex_count = hexCounter(radius)
    hexes_assigned = hexAssigner(hex_count)

    print(hexes_assigned)