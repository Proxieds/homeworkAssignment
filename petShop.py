from Cat import Cat
from Dog import Dog
from Data import Data
# Time library is used in the logStats() method for execution time
import time


def saveTest():
    """
    Creates a cat/dog with name and insert it into the database.
    """
    data = Data("database")
    # Begin Transaction
    data.beginTran()
    garfield = Cat("Garfield")
    odie = Dog("Odie")
    data.insert("Cat", garfield)
    data.insert("Dog", odie)
    # Commit Transactions
    data.commit()


def savePetShop():
    """
    Creates 3 nameless cats and dogs and performs an insert into the database that persists through transactions.
    Also shows an example where a rollback would be needed and reverts all other changes made after the transaction started and returns.
    """
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
    """
    Logs stats about the above functions like execution time.
    """
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
