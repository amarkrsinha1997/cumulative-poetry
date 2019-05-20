import argparse
sysParser = argparse.ArgumentParser()
sysParser.add_argument('--reveal-for-day', nargs=1, help="",
                       dest="forWhichDay", type=int)
sysParser.add_argument('--recite', action="store_true",
                       help="", dest="shouldRecite")

BEGINING_SENTENCE = "This is"
IN_VALID_DAY_MESSAGE = "Invalid Day"

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
    def __init__(self, args):
        self.args = args

    def checkArgs(self, args=self.args):

        if self._noArgsCheck(args):
            sysParser.print_help()
            raise NoArgsException("Need either of the args.")

        if self._onlyOneArgsCheck(args):
            raise OnlyOneArgsExeception(
                "Either one of both --recite and --reveal-for-day should be used.")

    def _noArgsCheck(self, args):
        return not args.get('shouldRecite') and not args.get('forWhichDay')

    def _onlyOneArgsCheck(self, args):
        return args.get('shouldRecite') and args.get('forWhichDay')


class Poet:

    def __init__(self, poem):
        self.poem = poem

    def revealForDay(self, forWhichDay=1):
        # initiated message
        talesRevealed = BEGINING_SENTENCE

        if forWhichDay > len(self.poem):
            raise InValidDay(IN_VALID_DAY_MESSAGE)

        talesToBeRevealed = self.poem[:forWhichDay]
        talesToBeRevealed.reverse()

        talesRevealed += "\n\t".join(talesToBeRevealed)

        return talesRevealed

    def recite(self):
        totalDays = len(self.poem) + 1
        revealTales = ""

        for day in range(1, totalDays):
            tale = self.revealForDay(day)
            revealTales += "Day {0} -\n".format(day)
            revealTales += tale
            revealTales += "\n"

        return revealTales


if __name__ == "__main__":
    poet = Poet()
    args = sysParser.parse_args()
    args = vars(args)

    parser = Parser(args)
    parser.checkArgs()

    shouldRecite = args['shouldRecite']

    if shouldRecite:
        tale = poet.recite()
        print(tale)
    else:
        forWhichDay = args['forWhichDay'][0]
        tale = poet.revealForDay(forWhichDay)
        print(tale)
