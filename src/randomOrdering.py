import random
class RandomOrdering:
    def randomOrdering(self, lines):
        firstLine = lines[0]
        remainingLines = lines[1:]
        random.shuffle(remainingLines)
        return [firstLine] + remainingLines 

class RandomSeedOrdering:
    def __init__(self, seedValue):
        self.seedValue = seedValue

    def randomOrdering(self, lines):
        random.seed(self.seedValue)
        return RandomOrdering().randomOrdering(lines)

class NoRandomOrdering:
    def randomOrdering(self, lines):
        return lines