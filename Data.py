class Data:
    """
    Data object definition
    """

    def __init__(self, database=None):
        """
        initialization
          database   : name of database to connect to
        """
        print("Connecting to database")

    def beginTran(self):
        print("Beginning a transaction")

    def commit(self):
        print("Committing transaction")

    def rollback(self):
        print("Rolling back transaction")

    def insert(self, table, object):
        print("Inserting " + object.getName() + " into table " + table)
