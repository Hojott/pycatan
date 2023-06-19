from hexAssigner import hexAssign

input = input()
if input != "large":
    input = int(input)

if __name__ == "__main__":
    hexes = hexAssign()
    print(hexes.generateTerrain(input))