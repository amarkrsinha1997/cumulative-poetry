import unittest
from poet import Poet
from poem import Poem, POEM


class poetTest(unittest.TestCase): # TODO - class name is supposed to be capital 
    def test_reveal_for_day_1(self):
        poet = Poet(Poem(POEM))
        actualTale = poet.revealForDay(1)
        expectedTale = "This is the house that Jack built."

        self.assertEqual(actualTale, expectedTale)

    def test_reveal_for_day_5(self): # TODO - try to see if you can  use multi-line strings
        poet = Poet(Poem(POEM))
        actualTale = poet.revealForDay(5)

        expectedTale = "This is the dog that worried\n\t" \
            + "the cat that killed\n\t" \
            + "the rat that ate\n\t" \
            + "the malth that lay in\n\t" \
            + "the house that Jack built." \

        self.assertEqual(actualTale, expectedTale)        

    def test_recite_contains_day(self): # TODO - hard to understand, what is Tale Day? The initial problem has no such word.
        poet = Poet(Poem(POEM))
        tale = poet.recite()

        actualTaleDay = len(poet.poem.getPoem()) # TODO - don't invent words
        expectedTaleDay = tale.count("Day")
        self.assertEqual(actualTaleDay, expectedTaleDay)
        

    def test_recite_reveal_everyday_tale(self): # TODO - the test can be more specific, like how many days should exist? What should be the length of the poem? 
        poet = Poet(Poem(POEM))
        tale = poet.recite()

        actualTaleDay = len(poet.poem.getPoem())
        expectedTaleDay = tale.count("Day")
        
        for day in range(1, actualTaleDay + 1):
            dayString = "Day {0} -".format(day)
            self.assertNotEqual(tale.index(dayString), -1) # TODO Complicated way of saying that something should exist. Is there is a simpler method to do that.


    def test_should_be_able_to_echo_for_reveal_day_1(self):
        poet = Poet(Poem(POEM), True)

        actualTale = poet.revealForDay(1)
        expectedTale = "This is the house that Jack built.\n\tthe house that Jack built."

        self.assertEqual(actualTale, expectedTale)

if __name__ == "__main__":
    unittest.main()