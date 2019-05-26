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

    @mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(shouldRecite=False, forWhichDay=[2]))
    def test_should_not_recite(self, mock_parser):
        parser = Parser()
        parser.checkArgs()
        self.assertEqual(parser.getArgs(), {"shouldRecite":False, "forWhichDay": [2]})

    @mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(shouldRecite=True, forWhichDay=None))
    def test_should_recite(self, mock_parser):
        parser = Parser()
        parser.checkArgs()
        self.assertEqual(parser.getArgs(), {"shouldRecite":True, "forWhichDay": None})

