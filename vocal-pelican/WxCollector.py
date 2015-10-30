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

    def execute(self, sourceDirectory, curl, baseUrl, stations):
        """
        collect weather files
        """
        timeNow = int(round(time.time()));
        print timeNow

        os.chdir(sourceDirectory)

        for station in stations:
            print station
            fileName = "%s.%d" % (station, timeNow)
            print fileName

            command = "%s %s%s.xml > %s" % (curl, baseUrl, station, fileName)
            print command

            system(command)
            

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
    sourceDirectory = configuration['sourceDirectory']
    curl = configuration['curl']
    baseUrl = configuration['baseUrl']

    stations = [
        'KRDD', 'KRBL', 'KCIC', 'KACV', 'KCEC', 'KSIY', 'KMFR', 'KLMT', 'KLKV', 'KAAT',
        'KUKI', 'KMHR', 'KSTS', 'KSUU', 'KSCK', 'KSFO', 'KMRY', 'KAPC', 'KCCR', 'KSJC',
        'KBOK', 'KSXT', 'KRBG', 'KOTH', 'KEUG', 'KSLE', 'KUAO', 'KHIO', 'KPDX', 'KDLS',
        'KKLS', 'KCLS', 'KOLM', 'KCLM', 'KPAE', 'KSEA', 'KELN', 'KSKA', 'KCOE', 'KLWS',
        'KRDM', 'KGCD', 'KBDN', 'KBNO', 'KONO', 'KPDT', 'KMAN', 'KENV', 'KLOL', 'KRNO',
        'KPAO', 'KHWD', 'KOAK', 'KSQL', 'KRHV', 'KHAF'];

    wxCollector = WxCollector()
    wxCollector.execute(sourceDirectory, curl, baseUrl, stations)

print 'stop'


#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
