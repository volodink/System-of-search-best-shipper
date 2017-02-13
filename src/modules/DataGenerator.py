import random
import os

class DataGenerator:   
    def __init__(self, pathToDict):
        self.file = open(pathToDict)
        self.file = self.file.readlines()
    
    def getRandomName(self, number):
        name = ""
        for i in range(number):
            name = name + " " + self.file[random.randint(0, len(self.file))][:-1]
        
        return name

if __name__ == "__main__":
    name = DataGenerator("../sortDict.txt")
    for i in range(100):
        print(name.getRandomName(random.randint(1, 5)))
