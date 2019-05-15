import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--reveal-for-day', nargs=1, help="", dest="revealDay", type=int)
parser.add_argument('--recite', action="store_true", help="", dest="shouldRecite")


class Poetry:
    tales = [
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

    def __init__(self):
        pass

    def revealForDay(self, revealDay=1):
        # initiated message
        talesRevealed = "This is "

        if revealDay > len(self.tales):
            return "Invalid Day"

        talesToBeRevealed = self.tales[:revealDay]
        talesToBeRevealed.reverse()

        for tale in talesToBeRevealed:
            talesRevealed += "{0}\n\t".format(tale)

        return talesRevealed

    def recite(self):
        totalDays = len(self.tales) + 1
        revealTales = ""
    
        for day in range(1, totalDays):
            tale = self.revealForDay(day)
            revealTales += "Day {0} -\n".format(day)
            revealTales += tale
            revealTales += "\n"

        return revealTales

    def checkArgs(self, args):
        shouldRecite = args['shouldRecite']
        revealDayArg = args['revealDay']

        if not shouldRecite and not revealDayArg:
            parser.print_help()
            print("\n")
            raise Exception("Need either of the args.")

        if shouldRecite and revealDayArg:
            print("Either one of the args should be given not both.")

if __name__ == "__main__":
    poetry = Poetry()
    args = parser.parse_args()
    args = vars(args)

    poetry.checkArgs(args)

    shouldRecite = args['shouldRecite']
    
    if shouldRecite:
        tale = poetry.recite()
        print(tale)
    else:
        revealDay = args['revealDay'][0]
        tale = poetry.revealForDay(revealDay)
        print(tale)