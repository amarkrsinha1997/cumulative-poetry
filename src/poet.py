import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--reveal-for-day', nargs=1, help="", dest="revealDay", type=int)
parser.add_argument('--recite', action="store_true", help="")


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


if __name__ == "__main__":
    poetry = Poetry()
    args = parser.parse_args()
    args = vars(args)
    
    shouldRecite = args['recite']
    revealDayArg = args['revealDay']


    if not shouldRecite and not revealDayArg:
        parser.print_help()
        print("\n")
        raise Exception("Need either of the args.")

    if shouldRecite:
        pass
    else:
        revealDay = revealDayArg[0]
        tale = poetry.revealForDay(revealDay)
        print(tale)