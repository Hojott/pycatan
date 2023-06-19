class Hex:
    """ Base class for a hex
    """
    def __init__(self, type):
        self.type: str = type

class LandHex(Hex):
    """ Class for a hex on land
    """
    def __init__(self, type):
        super().__init__(type)

class OceanHex(Hex):
    """ Class for an ocean hex, at the edge of the board
    """
    def __init__(self, type):
        super().__init__(type)
