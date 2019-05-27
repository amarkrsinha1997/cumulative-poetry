import argparse
import constant
from exceptions import InValidDay

from parser import Parser

from poem import Poem, POEM
from echoFormatters import Echo, NoEcho

class Poet:
    def __init__(self, poem, echo):
        if len(poem.getPoem()) == 0:
            raise ValueError(constant.POEM_LIST_EMPTY_MESSAGE)
        self.poem = poem
        self.echo = echo

    def revealForDay(self, forWhichDay=1):
        poem = self.poem.getPoem()

        talesToBeRevealed = poem[:forWhichDay]
        talesToBeRevealed.reverse()

        return constant.BEGINING_SENTENCE + "\n\t".join(self.echo.echo(talesToBeRevealed))


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

    parser = Parser()
    parser.checkArgs()
    args = parser.getArgs()

    poem = Poem(POEM)

    if args['shouldEcho']:
        echo = Echo()
    else:
        echo = NoEcho()

    poet = Poet(poem, echo)
    shouldRecite = args[constant.RECITE_DEST]

    if shouldRecite:
        tale = poet.recite()
        print(tale)
    else:
        forWhichDay = args[constant.REVEAL_FOR_DAY_DEST][0]
        tale = poet.revealForDay(forWhichDay)
        print(tale)
