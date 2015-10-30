#!/usr/bin/python
#
# Title:WxCollector.py
# Description: 
# Development Environment:OS X 10.8.5/Python 2.7.2
# Legalise:Copyright (C) 2013 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import os
import sys
import time
import yaml

from os import system

class WxCollector:

    def collection(self, collectionDirectory, curl, baseUrl, stations):
        """
        collect weather files
        """
        timeNow = int(round(time.time()));

        os.chdir(collectionDirectory)

        for station in stations:
            print station
            fileName = "%s.%d" % (station, timeNow)
            print fileName

            command = "%s %s%s.xml > %s" % (curl, baseUrl, station, fileName)
            print command

#            system(command)

    def execute(self, applicationDirectory, curl, baseUrl):
        """
        prepare for collection
        """
        fileName = "%s/stations.dat" % (applicationDirectory)

        inFile = open(fileName, 'r')
        stations = inFile.readlines()
        inFile.close()

        print stations

        collectionDirectory = "%s/collected" % (applicationDirectory)

        self.collection(collectionDirectory, curl, baseUrl, stations)

print 'start'

#
# argv[1] = configuration filename
#
if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
    else:
        fileName = "config.yaml"

    configuration = yaml.load(file(fileName))

    applicationDirectory = configuration['applicationDirectory']
    curl = configuration['curl']
    baseUrl = configuration['baseUrl']

    wxCollector = WxCollector()
    wxCollector.execute(applicationDirectory, curl, baseUrl)

print 'stop'

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
