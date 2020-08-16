OverallHistory = []


def historyToString():
    word = "/"
    for o in OverallHistory:
        print("pre: " + word)
        word + o + "/"
        print("post: " + word)
    return word


def printDesign(history):
    print("::::::::::::::::::::::::::::::::::::::::::")
    return input(':::' + str(historyToString()) + history + '> ')  # TODO
