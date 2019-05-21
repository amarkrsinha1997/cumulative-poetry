import argparse
import constant
from exceptions import InValidDay

from parser import Parser

from poem import Poem, POEM

class Poet:

    def __init__(self, poem):
        if len(poem.getPoem()) == 0:
            raise ValueError(constant.POEM_LIST_EMPTY_MESSAGE)
        self.poem = poem

    def revealForDay(self, forWhichDay=1):
        # initiated message
        talesRevealed = constant.BEGINING_SENTENCE

        poem = self.poem.getPoem()

        if forWhichDay > len(poem):
            raise InValidDay(constant.IN_VALID_DAY_MESSAGE)

        talesToBeRevealed = poem[:forWhichDay]
        talesToBeRevealed.reverse()

        talesRevealed += "\n\t".join(talesToBeRevealed)

        return talesRevealed

    def recite(self, poem=[]):
        if not poem:
            poem = self.poem.getPoem()
            totalDays = len(poem) + 1
            talesForEachDay = ["Day {0} -\n{1}".format(day, self.revealForDay(day))
                            for day in range(1, totalDays)]
            return '\n\n'.join(talesForEachDay)
        else:
            # poem by others 
            return '\n\n'.join(poem)

if __name__ == "__main__":
    poem = Poem(POEM)
    poet = Poet(poem)

    parser = Parser()
    parser.checkArgs()
    args = parser.getArgs()

    shouldRecite = args[constant.RECITE_DEST]

    if shouldRecite:
        tale = poet.recite()
        print(tale)
    else:
        forWhichDay = args[constant.REVEAL_FOR_DAY_DEST][0]
        tale = poet.revealForDay(forWhichDay)
        print(tale)
