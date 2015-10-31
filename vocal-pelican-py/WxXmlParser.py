#!/usr/bin/python
#
# Title:WxXmlParser.py
# Description:read and parse a weather service XML file
# Development Environment:OS X 10.8.5/Python 2.7.2
# Author:G.S. Cole (guycole at gmail dot com)
#
import datetime
import time
import rfc822
import sys
import unicodedata
import xml.parsers.expat

class WxXmlParser:
    buffer = 'xxx'

    dewpoint = 0
    humidity = 0
    latitude = 0.0
    location = 'Unknown'
    longitude = 0.0
    observationTime = 'Unknown'
    pressure = 0
    stationId = 'Unknown'
    temperature = 0.0
    visibility = 0
    weather = 'No Weather'
    windDirection = 0
    windGust = 0
    windSpeed = 0

    def getDewPoint(self):
        """
        dewpoint in C
        """
        return self.dewpoint

    def getHumidity(self):
        """
        relative humidity
        """
        return self.humidity

    def getLatitude(self):
        """
        latitude
        """
        return self.latitude

    def getLocation(self):
        """
        location
        """
        return self.location

    def getLongitude(self):
        """
        longitude
        """
        return self.longitude

    def getObservationTime(self):
        """
        observation time
        """
        return self.observationTime

    def getPressure(self):
        """
        pressure
        """
        return self.pressure

    def getStationId(self):
        """
        station identifier
        """
        return self.stationId

    def getTemperature(self):
        """
        temperature in C
        """
        return self.temperature

    def getTimeStamp(self):
        """
        return database friendly observation time

        Mon, 17 Jun 2013 13:55:00 -0700
        (2013, 6, 17, 13, 55, 0, 0, 1, 0, -25200)
        """
        parsedTime = rfc822.parsedate_tz(self.observationTime)
        result = datetime.datetime.fromtimestamp(rfc822.mktime_tz(parsedTime))
        return result

    def getVisibility(self):
        """
        visibility
        """
        return self.visibility

    def getWeather(self):
        """
        weather
        """
        return self.weather

    def getWindDirection(self):
        """
        wind direction
        """
        return self.windDirection

    def getWindGust(self):
        """
        wind gusts in knots
        """
        return self.windGust

    def getWindSpeed(self):
        """
        wind speed in knots
        """
        return self.windSpeed

    def start_element(self, name, attrs):
        """
        start of XML tag
        """
#        print 'start:', name, attrs

    def end_element(self, name):
        """
        ending XML tag
        """
        if name == 'dewpoint_c':
            self.dewpoint = float(self.buffer)

        if name == 'relative_humidity':
            self.humidity = float(self.buffer)

        if name == 'latitude':
            self.latitude = float(self.buffer)

        if name == 'location':
            self.location = self.buffer

        if name == 'longitude':
            self.longitude = float(self.buffer)

        if name == 'observation_time_rfc822':
            self.observationTime = self.buffer

        if name == 'pressure_mb':
            self.pressure = float(self.buffer)

        if name == 'station_id':
            self.stationId = self.buffer

        if name == 'temp_c':
            self.temperature = float(self.buffer)

        if name == 'visibility_mi':
            self.visibility = float(self.buffer)

        if name == 'weather':
            self.weather = self.buffer

        if name == 'wind_degrees':
            self.windDirection = float(self.buffer)

        if name == 'wind_gust_kt':
            self.windGust = float(self.buffer)

        if name == 'wind_kt':
            self.windSpeed = float(self.buffer)

    def char_data(self, data):
        """
        text between start and end tag
        """
#        self.buffer = repr(data)
        self.buffer = data

    def execute(self, fileName):
        """
        read and parse XML file
        """
#       print "execute read:%s" % (fileName)

        inFile = open(fileName, 'r')
        rawXml = inFile.read()
        inFile.close()

        p = xml.parsers.expat.ParserCreate()
        p.StartElementHandler = self.start_element
        p.EndElementHandler = self.end_element
        p.CharacterDataHandler = self.char_data
        p.Parse(rawXml)

print 'start'

#
# argv[1] = test filename
#
if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileName = sys.argv[1]

    xmlParser = WxXmlParser()
    xmlParser.execute('samples/KAAT.1371505741')
    xmlParser.execute('samples/KSIY.1375076941')
    print "dewpoint:%s" % (xmlParser.getDewPoint())
    print "humidity:%s" % (xmlParser.getHumidity())
    print "latitude:%s" % (xmlParser.getLatitude())
    print "longitude:%s" % (xmlParser.getLongitude())
    print "location:%s" % (xmlParser.getLocation())
    print "time:%s" % (xmlParser.getObservationTime())
    print "pressure:%s" % (xmlParser.getPressure())
    print "station:%s" % (xmlParser.getStationId())
    print "temperature:%s" % (xmlParser.getTemperature())
    print "visibility:%s" % (xmlParser.getVisibility())
    print "weather:%s" % (xmlParser.getWeather())
    print "wind direction:%s" % (xmlParser.getWindDirection())
    print "wind gust:%s" % (xmlParser.getWindGust())
    print "wind speed:%s" % (xmlParser.getWindSpeed())

print 'stop'

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
