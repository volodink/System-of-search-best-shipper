class DataBase:
    def __init__(self, path):
		self.sql = open(path)
		self.sql = self.sql.read()
		print(sql)
		
		
if __name__ == "__main__":
	db = DataBase("../../sql/DB.sql")