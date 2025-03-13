class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = []
        self.folded = False

    def __str__(self):
        return f"{self.name} ({self.chips} chips)"

    def __repr__(self):
        return self.__str__()
