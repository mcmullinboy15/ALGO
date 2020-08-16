class TimeSpan:
    def __init__(self, _from=None, to=None):
        self._from = _from
        self.to = to

    def getFrom(self):
        return self._from

    def getTo(self):
        return self.to

    def __str__(self):
        return "from: "+str(self._from) + ", to: " + str(self.to)
