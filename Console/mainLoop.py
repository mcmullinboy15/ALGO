#
#
#
#
# from Console import Buy
# from Console.Buy import Buy
from Console import Buy
from Console import Sell
from Console.LoopOutPut import printDesign
from Objects import Investor


class mainLoop:

    # TODO  This is where I can Add FirstCommands
    def switch(arg):
        switcher = {
            "buy": Buy.runBuyLoop(),  # maybe just runBuyLoop,
            "sell": Sell.runSellLoop(),
            "create": Create.createObject()
        }
        print(switcher.get(arg, "Invalid Command"))

    def firstCommand(self, history):
        print("self: " + self)
        if self == "buy":
            Buy.runBuyLoop(history)
        if self == "sell":
            Sell.runSellLoop(history)
        if self == "create":
            Create.createObject(history)


def createWhat(self, history):
    if self == "Investor":
        Investor.addInvestor(history)


class Create:

    # Move to Create
    def createObject(history):
        print('...Running...CreationLoop')
        myInput = None
        exitWord = "exit"
        while myInput != exitWord:
            myInput = printDesign(history + '/create new')
            createWhat(myInput.capitalize(), history)
        print('...Exiting...CreationLoop')


def main():
    myInput = None
    exitWord = "exit"
    history = "/main"
    while myInput != exitWord:
        myInput = printDesign(history)
        commands = []
        start = 0
        index = 0

        # controlling first command
        if not myInput.__contains__(" "):
            index = len(myInput)
        else:
            index = myInput.index(" ", start)
        print('index: ' + str(index))
        print('start: ' + str(start))
        firstCommand = myInput[start: index]
        print('list: ' + str(firstCommand))
        start = index

        # decide where to go with first command
        # you might need to retrun something like the myInput but maybe not
        # switch(firstCommand)
        mainLoop.firstCommand(firstCommand, history)


if __name__ == '__main__': main()

# supe
# hello
# buy
# NFLX
# exit
# sell
# NFLX
# exit
