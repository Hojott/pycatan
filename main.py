from generateTerrain import generateTerrain

input = input()
if input != "large":
    input = int(input)

if __name__ == "__main__":
    generateTerrain(input)