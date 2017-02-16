import sqlite3
import os 

class DataBase:
    def __init__(self, path):
        self.sql = open(path)
        self.sql = self.sql.read()

        if self.__checkFileThis("partnerdb.db"):
            os.remove("partnerdb.db")
                       

        self.db = sqlite3.connect("partnerdb.db")
        self.cur = self.db.cursor()

        try:
            self.cur.executescript(self.sql)
        except sqlite3.DatabaseError as err:
            print("Error: ", err)
        else:
            print("База данных успешно созданна!!!1")

    def __del__(self):
        self.db.close()

    def __checkFileThis(self, file):
        for i in os.listdir("."):
            if i == file:
                return True
        return False

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