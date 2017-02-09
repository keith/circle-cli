# -*- coding: utf-8 -*-

from src.helpers import formatter
import unittest

TEST_ROWS = [
    ["12345", "success", "branchname", "abc"],
    ["12345", "success", "branchname-number2", "abc"],
    ["12345", "success", "master", "A long name foo"],
    ["12345", "success", "master", "foo bar"],
    ["12345", "success", "master", "í"],
    ["12345", "success", "master", "foo bar"],
    ["12345", "failure", "foobarbaz", "foo bar"],
    ["12345", "success", "release-whatever", "foo bar"],
    ["12345", "success", "even-more-branches-some-are-long", "foo"],
    ["12345", "success", "master", "a long name bar"],
]


class TestFormatter(unittest.TestCase):
    def test_formatter(self):
        output = formatter.output_rows(TEST_ROWS)
        with open("tests/output_rows.txt") as f:
            self.assertEqual(output, f.read())

    def test_empty_rows(self):
        try:
            self.assertEqual(formatter.output_rows([]), "")
        except IndexError:
            self.fail("Shouldn't have thrown")
