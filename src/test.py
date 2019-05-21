import unittest
from poet import Poet
from poem import Poem, POEM


class poetTest(unittest.TestCase):
    def test_reveal_for_day_1(self):
        poet = Poet(Poem(POEM))
        actualTale = poet.revealForDay(1)
        expectedTale = "This is the house that Jack built."

        self.assertEqual(actualTale, expectedTale)

    def test_reveal_for_day_5(self):
        poet = Poet(Poem(POEM))
        actualTale = poet.revealForDay(5)

        expectedTale = "This is the dog that worried\n\t" \
            + "the cat that killed\n\t" \
            + "the rat that ate\n\t" \
            + "the malth that lay in\n\t" \
            + "the house that Jack built." \

        self.assertEqual(actualTale, expectedTale)        

    def test_recite_contains_day(self):
        poet = Poet(Poem(POEM))
        tale = poet.recite()

        actualTaleDay = len(poet.poem.getPoem())
        expectedTaleDay = tale.count("Day")
        self.assertEqual(actualTaleDay, expectedTaleDay)
        

    def test_recite_reveal_everyday_tale(self):
        poet = Poet(Poem(POEM))
        tale = poet.recite()

        actualTaleDay = len(poet.poem.getPoem())
        expectedTaleDay = tale.count("Day")
        
        for day in range(1, actualTaleDay + 1):
            dayString = "Day {0} -".format(day)
            self.assertNotEqual(tale.index(dayString), -1)

if __name__ == "__main__":
    unittest.main()