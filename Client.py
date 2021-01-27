class Client:
    def __init__(self, clientNumber, clientName):
        self.id = clientNumber
        self.name = clientName

    def getName(self):
        return self.name

    def getNumber(self):
        return self.id

    def __repr__(self):
        return str(self.id) + " ~ " + self.name