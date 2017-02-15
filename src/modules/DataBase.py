import sqlite3

class DataBase:
    def __init__(self, path):
        self.sql = open(path)
        self.sql = self.sql.read()
        self.db = sqlite3.connect("testdb.db")
        self.cur = self.db.cursor()

        try:
            self.cur.executescript(self.sql)
        except sqlite3.DatabaseError as err:
            print("Error: ", err)
        else:
            print("База данных успешно созданна!!!1")

        def __del__():
            self.db.close()

        def putDataInDB(numBrokeSupply, 
                        numLawsuitsNow, 
                        numLawsuitsPast, 
                        companyAge,
                        financPosition,
                        numberOfClient,
                        quality,
                        dateOfDelivery,
                        name,
                        email,
                        site,
                        phoneNumber,
                        listingName,
                        price,
                        description):
            pass

        def getData():
            pass


if __name__ == "__main__":
    db = DataBase("../../sql/DB.sql")