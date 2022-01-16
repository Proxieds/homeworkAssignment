from Cat import Cat
from Dog import Dog
from Data import Data


def testPart1():
    """
    Tests the first part of the takehome assignment
    Create a new cat object, set name to Garfield and insert into Cat table
    """
    cat = Cat()
    print("Name is currently %s" % cat.getName())
    cat.setName("Garfield")
    print("Name has been changed to %s" % cat.getName())

    data = Data("database")
    data.insert("Cat", cat)


def testPart2():
    """
    Tests additional features added onto the base object class
    Tests a variety of methods and expected behaviors informally.
    """
    cat = Cat("Garfield")
    print("First cat's age: %d" % cat.getAge())
    secondCat = Cat("Grumpy Cat")
    print("Second cat with initial name: %s" % secondCat.getName())
    cat.speak()
    cat.speak("Optional Message in speak")
    print(cat.getName())
    print(secondCat.getName())
    print("Testing cat speak increments the age by 1 after every 5th speak: ")
    for _ in range(5):
        cat.speak()
        print("Number of Speaks: %d Age: %d" %
              (cat.getNumberOfSpeaks(), cat.getAge()))
    print("Testing the set/get names function: ")
    print("List of names for first cat")
    print(cat.getNames())
    print("Setting cat's name to Spunky")
    cat.setName("Spunky")
    print("List of names for first cat")
    print(cat.getNames())
    print("Average Name Length for cat: %.2f" % cat.getAverageNameLength())

    print("Creating Dog Object: ")
    dog = Dog("Odie")
    print("Dog's name: %s" % dog.getName())


def main():
    """
    main process goes here
    """
    print("Part 1: ")
    testPart1()

    print("Part 2: Informal Tests for Additional Functionality: ")
    testPart2()


if __name__ == "__main__":
    main()
