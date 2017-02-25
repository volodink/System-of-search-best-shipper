import random
import os
import codecs

class DataGenerator:   
    def __init__(self, pathToDict):
        if os.name == "nt":
            self.file = codecs.open(pathToDict, "r", "utf_8_sig")
        else:
            self.file = open(pathToDict)
        self.file = self.file.readlines()

    # def __init__(self):
    #     pass
    
    def __getRandomName(self, number):
        name = self.file[random.randint(0, len(self.file) - 1) ][:-1]
        for i in range(number - 1):
            name = name + " " + self.file[random.randint(0, len(self.file) - 1)][:-1]
        
        return name

    def __getListingName(self, numb):
        relList = ["Арабика Сантос", "Арабика Медельин", "Арабика Тарразу", "Арабика Блу Маунтин", "Арабиен Мокко",
                    "Арабика Майсор", "Арабика", "Арабика Килиманджаро", "Арабика Кона", "Арабика с острова Ява",
                    "Арабика с острова Суматра", "Арабика Харар"]

        return tuple(tuple((i, random.uniform(100, 2000)) for i in random.sample(relList, numb))) 

    def getTranslateWord(self, name):
        #Заменяем пробелы и преобразуем строку к нижнему регистру
        name = name.lower()
        #
        transtable = ((u"щ", u"sch"), (u"ё", u"yo"), (u"ж", u"zh"), (u"ц", u"ts"), (u"ч", u"ch"),
            (u"ш", u"sh"), (u"ы", u"yi"), (u"ю", u"yu"), (u"я", u"ya"), (u"а", u"a"), (u"б", u"b"),
            (u"в", u"v"), (u"г", u"g"), (u"д", u"d"), (u"е", u"e"), (u"з", u"z"), (u"и", u"i"),
            (u"й", u"j"), (u"к", u"k"),  (u"л", u"l"), (u"м", u"m"),  (u"н", u"n"), (u"о", u"o"),
            (u"п", u"p"), (u"р", u"r"), (u"с", u"s"), (u"т", u"t"), (u"у", u"u"), (u"ф", u"f"),
            (u"х", u"h"), (u"э", u"e"), (u"ь", u""),
        )
        for symb_in, symb_out in transtable:
            name = name.replace(symb_in, symb_out)
        return name
    


    def getPartnerData(self, number):
        data = {}
        for i in range(number): 
            contact = {}
            listingName = {}
            reliability = {}


            contact["name"] = self.__getRandomName(random.randint(1,3))
            contact["phoneNumber"] = "+7" + str(random.randint(900, 999)) + str(random.randint(1000000, 9999999))
            contact["email"] = "".join(self.getTranslateWord(contact["name"]).split(" ")) + \
                                random.choice(("@gmail.com", "@mail.ru", "@yandex.ru", "@rambler.ru"))
            contact["site"] = "".join([self.getTranslateWord(i) for i in contact["name"].split(" ")]) + \
                                random.choice((".ru", ".com", ".uk", ".us"))

            reliability["numBrokeSupply"] = random.randint(0, 100)
            reliability["numLawsuitsNow"] = random.randint(0, 5)
            reliability["numLawsuitsPast"] = random.randint(0, 30)
            reliability["companyAge"] = random.randint(1, 80)
            reliability["financPosition"] = random.uniform(300000, 50000000)
            reliability["numberOfClient"] = random.randint(0, 100)
            
            
            data[i] = {"contact": contact,
                       "quality": random.randint(1, 10), 
                       "dateOfDelivery": random.randint(1, 90),
                       "listingName":  self.__getListingName(random.randint(1, 12)),
                       "reliability": reliability}
        
        return data

if __name__ == "__main__":
    dataGen = DataGenerator("../sortDict.txt")
    num = 1
    data = dataGen.getPartnerData(num)
    print(data)
    
    
    # for i in range(100):
    #     print(name.getRandomName(random.randint(1, 5)))
    # print(DataGenerator().getRandomPhoneNumber())
