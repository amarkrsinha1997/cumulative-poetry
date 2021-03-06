
import constant
from parser import Parser
from poem import Poem, POEM
from poet import Poet
from echoFormatters import EchoFormatter, NoEchoFormatter
from randomOrdering import RandomOrdering, NoRandomOrdering, RandomSeedOrdering

class Main:

    @staticmethod
    def getEcho(args):
        if args[constant.ECHO_DEST]:
            echo = EchoFormatter()
        else:
            echo = NoEchoFormatter()
        return echo

    @staticmethod
    def getRandom(args): 
        if args[constant.RANDOM_DEST] and args[constant.SEED_DEST]:
            seedValue = args[constant.SEED_DEST][0]
            random = RandomSeedOrdering(seedValue)
        elif args[constant.RANDOM_DEST]:
            random = RandomOrdering()
        else:
            random = NoRandomOrdering()
        return random

    @staticmethod
    def run():
        parser = Parser()
        parser.checkArgs()
        args = parser.getArgs()



        poem = Poem(POEM, Main.getRandom(args))
        poet = Poet(poem, Main.getEcho(args))
        shouldRecite = args[constant.RECITE_DEST]

        if shouldRecite:
            tale = poet.recite()
            print(tale)
        else:
            forWhichDay = args[constant.REVEAL_FOR_DAY_DEST][0]
            tale = poet.revealForDay(forWhichDay)
            print(tale)


if __name__ == "__main__":
    Main.run()