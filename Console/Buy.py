from Console.LoopOutPut import printDesign
from Objects import Data

# class Buy:
buyTicker = ""


def runBuyLoop(history):
    print('...Running...BuyLoop')
    myInput = None
    exitWord = "exit"
    while myInput != exitWord:
        myInput = printDesign(history + "/buy")
        buyCommands(myInput)
    print('...Exiting...BuyLoop')


def buyCommands(myInput):
    if myInput == "setTicker":
        setBuyTicker(myInput)
    if myInput == "":
        return


def setBuyTicker(buyTicker):
    print('ticker: ' + buyTicker)
    Data.setTicker(buyTicker)
