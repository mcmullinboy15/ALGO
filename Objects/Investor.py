#
#
#
#
from Console import mainLoop

myInvestors = []


class Investor:
    def __init__(self, Name, API_KEY, API_SECRET, APCA_API_BASE_URL="https://paper-api.alpaca.markets"):
        self.APCA_API_BASE_URL = APCA_API_BASE_URL
        self.API_SECRET = API_SECRET
        self.API_KEY = API_KEY
        self.Name = Name

    def getAPI_KEY(self):
        return self.API_KEY

    def getAPI_SECRET(self):
        return self.API_SECRET

    def getAPCA_API_BASE_URL(self):
        return self.APCA_API_BASE_URL

    def getName(self):
        return self.Name


def main():
    Investors = []

    Investor_Dad = Investor('Dad', 'API_KEY_01', 'Secret_API_KEY_01')
    print(Investor_Dad.getAPI_KEY())
    Investor_Grandma = Investor('Grandma', 'API_KEY_02', 'Secret_API_KEY_02')
    print(Investor_Grandma.getAPI_KEY())
    Investor_Allen = Investor('Allen', 'API_KEY_03', 'Secret_API_KEY_03')
    print(Investor_Allen.getAPI_KEY())
    Investor_Scott = Investor('Scott', 'API_KEY_04', 'Secret_API_KEY_04')
    print(Investor_Scott.getAPI_KEY())

    Investors.append(Investor_Dad)
    Investors.append(Investor_Grandma)
    Investors.append(Investor_Allen)
    Investors.append(Investor_Scott)

    for I in Investors:
        print(I.getName())


if __name__ == "__main__": main()


def createInvestor(history):
    temp_name = mainLoop.printDesign(history + "/NAME")
    temp_API_KEY = mainLoop.printDesign(history + "/API_KEY")
    temp_API_SECRET = mainLoop.printDesign(history + "/API_SECRET")
    myInvestor = Investor(temp_name, temp_API_KEY, temp_API_SECRET)

    return myInvestor


def addInvestor(history):
    global name, tempAPI_KEY, tempAPI_SECRET
    print('...Running...addInvestor')
    myInput = None
    exitWord = "exit"
    counter = 0
    while myInput != exitWord:
        myInvestors.append(createInvestor(history))
        myInput = mainLoop.printDesign(history + "/add Another? ('Enter'/'exit')")
    print('...Exiting...addInvestor')
