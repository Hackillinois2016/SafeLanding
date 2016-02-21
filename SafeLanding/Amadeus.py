class Amadeus:
    def __init__(self, dest, dep, ret):
        self.destination = dest
        self.departure = dep
        self.planeRet = ret
    def getDepartureDate(self):
        return self.departure
    def printData(self):
        print "destination = " + self.destination + "\n"
        print "departure date = " + self.departure + "\n"
        print "return date = " + self.planeRet + "\n"
