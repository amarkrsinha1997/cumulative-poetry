import unittest
from poet import Poetry


class PoetryTest(unittest.TestCase):
    def test_reveal_for_day_1(self):
        poetry = Poetry()
        actualTale = poetry.revealForDay(1)
        expectedTale = "This is the house that Jack built.\n\t"

        self.assertEqual(actualTale, expectedTale)

    def test_reveal_for_day_5(self):
        poetry = Poetry()
        actualTale = poetry.revealForDay(5)

        expectedTale = "This is the dog that worried\n\t" \
            + "the cat that killed\n\t" \
            + "the rat that ate\n\t" \
            + "the malth that lay in\n\t" \
            + "the house that Jack built.\n\t" \

        self.assertEqual(actualTale, expectedTale)        

if __name__ == "__main__":
    unittest.main()