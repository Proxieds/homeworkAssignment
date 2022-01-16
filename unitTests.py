# Using Python's unit testing framework
import unittest
from Cat import Cat
from Dog import Dog


class UnitTests(unittest.TestCase):

    def test_Age(self):
        """
        Asserts initial age of the cat is within [5,10] over multiple iterations
        """
        print("Testing the initial age of the cat is between 5 and 10... ")
        # Start of initial age interval is 5
        start = 5
        # End of initial age interval is 10
        end = 10
        for _ in range(100):
            # Create a new Cat object in each iteration
            cat = Cat()
            # Add 1 to end since range is zero based.
            self.assertTrue(cat.getAge() in range(start, end+1))
        print("Success: Age of cats were between 5 and 10")

    def test_Speak(self):
        """
        Checks speak messages for cats and dogs as well as age incrementing properly after every 5th speak
        """
        print("Testing speak functionality... ")
        cat = Cat()
        dog = Dog()
        initialCatAge = cat.getAge()
        initialDogAge = dog.getAge()
        speakIterations = 100
        for _ in range(speakIterations):
            cat.speak()
            dog.speak()
            print("Number of Speaks: %d Cat's Age: %d Dog's Age: %d " %
                  (cat.getNumberOfSpeaks(), cat.getAge(), dog.getAge()))
        # Assert that the initial age + (number of times spoken / 5) is equal to the current age of the objects
        self.assertEqual(cat.getAge(), initialCatAge + (speakIterations / 5))
        self.assertEqual(dog.getAge(), initialDogAge + (speakIterations / 5))
        # Test optional speak
        cat.speak("Optional Cat Speak")
        dog.speak("Optional Dog Speak")
        # After the 101th speak, the age should not be different from above
        self.assertEqual(cat.getAge(), initialCatAge + (speakIterations / 5))
        self.assertEqual(dog.getAge(), initialDogAge + (speakIterations / 5))
        print("Success: Age of cat and dog increases every 5th time it speaks")

    def test_SetGetNames(self):
        """
        Check that set name properly updates the name history of objects and handles duplicate/empty cases
        """
        print("Testing the set/get names functionality... ")
        cat = Cat()
        dog = Dog("Odie")
        # Should be 0 as no name was provided upon construction
        self.assertEqual(len(cat.getNames()), 0)
        # Should be 1 since Odie was provided for a name upon construction
        print(dog.getNames())
        self.assertEqual(len(dog.getNames()), 1)
        cat.setName("Garfield")
        cat.setName("Spunky")
        # Test duplicate case name
        cat.setName("Garfield")

        dog.setName("Duke")
        dog.setName("Leo")
        # Test empty case
        dog.setName("")
        # Garfield and Spunky
        self.assertEqual(len(cat.getNames()), 2)
        # Odie, Duke and Leo
        self.assertEqual(len(dog.getNames()), 3)

        print("Success: set/get names are updating and retrieving the names collection properly")

    def test_AverageNameLength(self):
        """
        Check that the average length of names is being properly calculated
        """
        print("Testing average name length functioanlity... ")
        # Start off with 4 letter names
        controlLength = 4
        dog = Dog("Odie")
        dog.setName("Duke")
        dog.setName("Loki")
        # Should be equal to the control since each name is of length 4
        self.assertEqual(dog.getAverageNameLength(), controlLength)
        # Test with a larger name
        dog.setName("A fairly long name for a dog")
        # New average should be greater than control of 4 now
        newAverageLength = dog.getAverageNameLength()
        self.assertTrue(newAverageLength > controlLength)
        # Test with a short name
        dog.setName("Rex")
        # New average should be less than the previous average length
        self.assertTrue(dog.getAverageNameLength() < newAverageLength)

        print("Success: Average name length is being affected by the setting larger or smaller names for the object")


if __name__ == "__main__":
    unittest.main()
