import simplejson
import urllib
import urllib2
import re
import Amadeus

class runAmadeus:
    def __init__(self,startCity):
        self.startCity = startCity
        self.travelList = []
        self.listOfZips = []
    def startSearch(self):
        validationList = []
        validationFile = open("destinationList.txt",'r')
        for line in validationFile:
            lineSplit = line.split(',')
            if len(validationList) > 0:
                if lineSplit[1] != validationList[:-1]:
                    validationList.append(lineSplit[1])
            else:
                validationList.append(lineSplit[1])

        found = filter(lambda x: x == self.startCity, validationList)

        if found == []:
            return None
        
        apikey = "API_KEY_HERE"
        link = "https://api.sandbox.amadeus.com/v1.2/flights/inspiration-search?"
        parameters = {"apikey": apikey, "origin": self.startCity, "departure_date": "2016-03-01"}
        data = urllib.urlencode(parameters)
        req = link + data
        request = urllib2.Request(req)
        response = urllib2.urlopen(request)

        json = response.read()
        json = json[60:]
        json = json[:-4]
        json += ","

        bunchOfStrings = re.findall('\{\n([^]]*?)\}\,', json)

        destinationList = []

        for strings in bunchOfStrings:
            destination = strings[21:]
            destination = destination[:3]
            found = filter(lambda x: x == destination, destinationList)
            if not found:
                destinationList.append(destination)
                departure = strings[51:]
                departure = departure[:10]
                returndate = strings[85:]
                returndate = returndate[:10]
                self.travelList.append(Amadeus.Amadeus(destination,departure,returndate))

        return destinationList
    
def grabZipCodes(airportCode):
    airportFile = open("AirportCodesWithZip.txt",'r')
    i = 0

    for airport in airportFile:
        airportSplit = airport.split(',')
        if airportSplit[0] == airportCode:
            #print airportSplit
            zipCodes = airportSplit[4:]
            zipCodes[-1] = zipCodes[-1].replace("\r\n","")
            fixedCodes = []
            for zipC in zipCodes:
                if zipC[0] == '0':
                    zipC = zipC[1:]
                    if zipC[0] == '0':
                        zipC = zipC[1:]
                        if zipC[0] == '0':
                            zipC = zipC[1:]
                fixedCodes.append(zipC)
            airportFile.close()
            return fixedCodes
        
