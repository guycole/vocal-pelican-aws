#!/usr/bin/python
#
# Title:WxParserLoader.py
# Description:
# Development Environment:OS X 10.8.5/Python 2.7.2
# Legalise:Copyright (C) 2013 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#
import pgdb
import os
import sys
import yaml

from WxLoader import WxLoader
from WxXmlParser import WxXmlParser

class WxParserLoader:

    def execute(self, sourceDirectory, dataBase, dataBaseUser):
        """
        discover, parse and load weather files
        """
        weatherDb = pgdb.connect(database = dataBase, user = dataBaseUser, password = '')

        targets = os.listdir(sourceDirectory)

        success = 0
        failure = 0

        for target in targets:
            fileName = "%s/%s" % (sourceDirectory, target)

            try:
                wxXmlParser = WxXmlParser()
                wxXmlParser.execute(fileName)

                if wxXmlParser.getStationId() == 'Unknown':
                    failure = failure+1
                else:
                    wxLoader = WxLoader()
                    retStat = wxLoader.execute(weatherDb, wxXmlParser)

                    if retStat > 0:
                        success = success+1
                    else:
                        failure = failure+1
            except:
                failure = failure+1
                print 'exception noted'

            os.remove(fileName)

        print "end success:%d failure:%d" % (success, failure)

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
    dataBase = configuration['dataBase']
    dataBaseUser = configuration['dataBaseUser']

    wxParserLoader = WxParserLoader()
    wxParserLoader.execute(sourceDirectory, dataBase, dataBaseUser)

print 'stop'


#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
