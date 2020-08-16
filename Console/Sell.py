from Console.LoopOutPut import printDesign
from Objects import Data


# class Sell:

def runSellLoop(history):
    history = history
    print('...Running...SellLoop')
    myInput = None
    exitWord = "exit"
    while myInput != exitWord:
        myInput = printDesign('sell')
        sellCommands(myInput)

    print('...Exiting...SellLoop')


def sellCommands(myInput):
    if myInput == "setTicker":
        setSellTicker(myInput)
    if myInput == "":
        return


def setSellTicker(sellTicker):
    print('setSellTicker: ' + sellTicker)
    myInput = None
    exitWord = "exit"
    while myInput != exitWord:
        myInput = printDesign(sellTicker)
    sellCommands(myInput)
    Data.setTicker(sellTicker)
