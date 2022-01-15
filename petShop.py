from Cat import Cat
from Dog import Dog
from Data import Data
import time


def saveTest(verbose=True):
    data = Data("database")
    # Begin Transaction
    data.beginTran()
    garfield = Cat("Garfield")
    odie = Dog("Odie")
    data.insert("Cat", garfield)
    data.insert("Dog", odie)
    # Commit Transactions
    data.commit()


def savePetShop(verbose=True):
    data = Data("database")
    # Begin Transaction
    data.beginTran()
    for _ in range(3):
        namelessCat = Cat()
        namelessDog = Dog()
        data.insert("Cat", namelessCat)
        data.insert("Dog", namelessDog)
    # Commit Transactions if all prior inserts were successful
    data.commit()

    print("Insertion Error Case: ")
    data.beginTran()
    for _ in range(3):
        namelessCat = Cat()
        namelessDog = Dog()
        try:
            # Checks that the objects have a name prior to making the insertion
            assert(namelessCat.getName() is not " ")
            data.insert("Cat", namelessCat)
            data.insert("Dog", namelessDog)
        except:
            # Rollsback the database when an insertion fails
            print("Error occurred when attempting to insert into a table")
            data.rollback()
            return
    # Commit Transactions if all prior inserts were successful
    data.commit()


def logStats():
    start_time = time.time()
    saveTest()
    print("--- SaveTest() Runtime:  %s seconds ---" %
          (time.time() - start_time))

    start_time = time.time()
    savePetShop()
    print("--- SavePetShop() Runtime:  %s seconds ---" %
          (time.time() - start_time))


def main():
    """
    main process goes here
    """
    print("Save Test: ")
    saveTest()

    print("Save Petshop: ")
    savePetShop()

    print("Log Stats: ")
    logStats()


if __name__ == "__main__":
    main()
