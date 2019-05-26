import unittest
from unittest import mock
import argparse

from parser import Parser
from exceptions import OnlyOneArgsExeception

class ParserTest(unittest.TestCase):
    @mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(shouldRecite=True, forWhichDay=2))
    def test_only_arguments_provided(self, mock_parser):
        parser = Parser()
        self.assertRaises(OnlyOneArgsExeception, parser.checkArgs)