class Stats:
    bulls = None
    cows = None

    def __init__(self, bulls, cows):
        self.bulls = bulls
        self.cows = cows

    def __repr__(self):
        return f"Bulls = {self.bulls} & Cows = {self.cows}"
