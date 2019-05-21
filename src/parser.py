import argparse

import constant
from exceptions import NoArgsException, OnlyOneArgsExeception


class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.add_args()
        self.args = self.parse_args()

    def parse_args(self):
        args = self.parser.parse_args()
        return vars(args)

    def add_args(self):
        self.parser.add_argument(constant.REVEAL_FOR_DAY, nargs=1, help="",
                                 dest=constant.REVEAL_FOR_DAY_DEST, type=int)
        self.parser.add_argument(constant.RECITE, action="store_true",
                                 help="", dest=constant.RECITE_DEST)

    def checkArgs(self):
        if self._noArgsCheck(self.args):
            self.parser.print_help()
            raise NoArgsException(constant.NO_ARGS_MESSAGE)

        if self._onlyOneArgsCheck(self.args):
            raise OnlyOneArgsExeception(constant.ONLY_ONE_ARGS_MESSAGE)

    def getArgs(self):
        return self.args

    def _noArgsCheck(self, args):
        return not args.get(constant.RECITE_DEST) and not args.get(constant.REVEAL_FOR_DAY_DEST)

    def _onlyOneArgsCheck(self, args):
        return args.get(constant.RECITE_DEST) and args.get(constant.REVEAL_FOR_DAY_DEST)
