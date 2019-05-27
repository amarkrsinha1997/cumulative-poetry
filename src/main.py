
import constant
from parser import Parser
from poem import Poem, POEM
from poet import Poet
from echoFormatters import EchoFormatter, NoEchoFormatter


class Main:
    @staticmethod
    def run():
        parser = Parser()
        parser.checkArgs()
        args = parser.getArgs()

        poem = Poem(POEM)

        if args['shouldEcho']:
            echo = EchoFormatter()
        else:
            echo = NoEchoFormatter()

        poet = Poet(poem, echo)
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