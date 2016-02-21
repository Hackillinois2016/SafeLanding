import imo_mysql_test
import Amadeus
import AmadeusRunner

#abc
def giveOrigin(origin):
    firstRun = AmadeusRunner.runAmadeus(origin)

    destinations = firstRun.startSearch()

    if destinations == None:
        print "it is none!"
        return None
    return destinations
    
def giveDestination(destination, destinationList):
    found = filter(lambda x: x == destination, destinationList)
    zipCodes = AmadeusRunner.grabZipCodes(found[0])
    tupleList = imo_mysql_test.getIMOSQLQuery(zipCodes)
    return tupleList

def giveDiseases(tupleList):
    return imo_mysql_test.getDiseases(tupleList)

def giveCounts(tupleList):
    return imo_mysql_test.getCounts(tupleList)
