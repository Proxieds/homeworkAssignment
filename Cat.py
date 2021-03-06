# Import random for use within assigning random ages on initialization
import random


class Cat:
    """
    Cat object definition
    """

    def __init__(self, name=None, age=None, favoriteFood=None):
        """
        initialization
          name             : name of cat
          age              : count of symbol
          favoriteFood     : the cat's favorite food
          previousNames    : set of all the names that the cat has previously had
          numberOfSpeaks   : Counter for all the times that this cat has spoken
        """
        # Optional name for cat can be specified in construction, default is None otherwise
        self.__name = name or ""
        # Adding 1 to stop value as stop value is not inclusive in range i.e [5,10)
        self.__age = random.randrange(start=5, stop=11)
        self.__favoriteFood = favoriteFood
        # Initializes previous names collection with the name from construction if an optional name is given
        self.__previousNames = {self.__name} if self.__name else set()
        self.__numberOfSpeaks = 0

    def getName(self):
        """
        Gets the name of the cat
        """
        return self.__name

    def getAge(self):
        """
        Gets the age of the cat
        """
        return self.__age

    def getFavoriteFood(self):
        """
        Gets the favorite food of the cat
        """
        return self.__favoriteFood

    def getNumberOfSpeaks(self):
        """
        Gets the number of times the cat has spoken
        """
        return self.__numberOfSpeaks

    def setName(self, name):
        """
        Sets the name of the cat and adds the name to the set of previous names 
        Base condition is that the name is not empty or "None", otherwise update the 
        """
        # Check that a valid name is provided
        if name:
            self.__name = name
            # Don't have to check for duplicates names prior to adding to the collection when using a set
            self.__previousNames.add(self.getName())

    def setAge(self, age):
        """
        Sets the age of the cat
        """
        self.__age = age

    def setFavoriteFood(self, favoriteFood):
        """
        Sets the favorite food of the cat
        """
        self.__favoriteFood = favoriteFood

    def setNumberOfSpeaks(self, count):
        """
        Sets the number of times the cat has spoken
        """
        self.__numberOfSpeaks = count

    def speak(self, optionalMessage=None):
        """
        Prints optional message or "Meow" to stdout if it does not exist, also increments age by 1 after speaking five times
        """
        print(optionalMessage if optionalMessage else "meow")
        self.setNumberOfSpeaks(self.getNumberOfSpeaks() + 1)
        # Increments age by 1 every time the number of speaks is divisible evenly by 5
        if self.getNumberOfSpeaks() % 5 is 0:
            self.setAge(self.getAge() + 1)

    def getNames(self):
        """ 
        Returns a collection of all the names that this cat previously had
        """
        return self.__previousNames

    def getAverageNameLength(self):
        """
        Returns the average length of all previous names for this cat
        """
        # Cast value to float otherwise the return results in integer division where the value is rounded to the nearest integer
        totalLetters = float(sum(len(name) for name in self.getNames()))
        return totalLetters / len(self.__previousNames)
