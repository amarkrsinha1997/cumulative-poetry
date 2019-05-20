import argparse


BEGINING_SENTENCE = "This is "

RECITE = '--recite'
RECITE_DEST = 'shouldRecite'

REVEAL_FOR_DAY = '--reveal-for-day'
REVEAL_FOR_DAY_DEST = 'forWhichDay'

# Error Message
IN_VALID_DAY_MESSAGE = "Invalid Day"
POEM_LIST_EMPTY_MESSAGE = "Poem shall contain some lines."
NO_ARGS_MESSAGE = "Need either of the args."
ONLY_ONE_ARGS_MESSAGE = "Either one of both {0} and {1} should be used.".format(RECITE, REVEAL_FOR_DAY)

POEM = [
    'the house that Jack built.',
    'the malth that lay in',
    'the rat that ate',
    'the cat that killed',
    'the dog that worried',
    'that cow with the crumpled horn that tossed',
    'the maiden all forlorn that milked',
    'the man all tattered and torn that kissed',
    'the priest all shaven and shorn that married',
    'the rooster that crowed in the morn that woke',
    'the farmer sowing his corn that kept',
    'the horse and the hound and the horn that belonged to'
]


class InValidDay(Exception):
    pass


class NoArgsException(Exception):
    pass


class OnlyOneArgsExeception(Exception):
    pass


class Poem:
    def __init__(self, poem):
        self.poem = poem

    def getPoem(self):
        return self.poem


class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.add_args()
        self.args = self.parse_args()

    def parse_args(self):
        args = self.parser.parse_args()
        return vars(args)

    def add_args(self):
        self.parser.add_argument(REVEAL_FOR_DAY, nargs=1, help="",
                                 dest=REVEAL_FOR_DAY_DEST, type=int)
        self.parser.add_argument(RECITE, action="store_true",
                                 help="", dest=RECITE_DEST)

    def checkArgs(self):
        if self._noArgsCheck(self.args):
            self.parser.print_help()
            raise NoArgsException(NO_ARGS_MESSAGE)

        if self._onlyOneArgsCheck(self.args):
            raise OnlyOneArgsExeception(ONLY_ONE_ARGS_MESSAGE)

    def getArgs(self):
        return self.args

    def _noArgsCheck(self, args):
        return not args.get(RECITE_DEST) and not args.get(REVEAL_FOR_DAY_DEST)

    def _onlyOneArgsCheck(self, args):
        return args.get(RECITE_DEST) and args.get(REVEAL_FOR_DAY_DEST)


class Poet:

    def __init__(self, poem):
        if len(poem.getPoem()) == 0:
            raise ValueError(POEM_LIST_EMPTY_MESSAGE)
        self.poem = poem

    def revealForDay(self, forWhichDay=1):
        # initiated message
        talesRevealed = BEGINING_SENTENCE

        poem = self.poem.getPoem()

        if forWhichDay > len(poem):
            raise InValidDay(IN_VALID_DAY_MESSAGE)

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

    shouldRecite = args[RECITE_DEST]

    if shouldRecite:
        tale = poet.recite()
        print(tale)
    else:
        forWhichDay = args[REVEAL_FOR_DAY_DEST][0]
        tale = poet.revealForDay(forWhichDay)
        print(tale)
