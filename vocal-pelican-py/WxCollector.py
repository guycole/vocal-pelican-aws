#!/usr/bin/python
#
# Title:WxCollector.py
# Description: Collect stations contained in stations.dat
# Development Environment:OS X 10.8.5/Python 2.7.2
# Author:G.S. Cole (guycole at gmail dot com)
#
import os
import sys
import time
import yaml

from os import system

class WxCollector:

    def collection(self, collectedDir, curl, baseUrl, stations):
        """
        collect weather files
        """
        timeNow = int(round(time.time()));

        os.chdir(collectedDir)

        for station in stations:
            # kill newline
            temp = station.split('|')

            fileName = "%s.%d" % (temp[0], timeNow)

            command = "%s %s%s.xml > %s" % (curl, baseUrl, temp[0], fileName)
            print command
            system(command)

    def execute(self, collectedDir, curl, baseUrl):
        """
        prepare for collection
        """
        inFile = open('stations.dat', 'r')
        stations = inFile.readlines()
        inFile.close()

        self.collection(collectedDir, curl, baseUrl, stations)

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

    collectedDir = configuration['collectedDir']
    curl = configuration['curl']
    baseUrl = configuration['baseUrl']

    wxCollector = WxCollector()
    wxCollector.execute(collectedDir, curl, baseUrl)

print 'stop'

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
