#!/usr/bin/python
#
# Title:WxParserLoader.py
# Description:
# Development Environment:OS X 10.8.5/Python 2.7.2
# Author:G.S. Cole (guycole at gmail dot com)
#
import os
import sys
import yaml

from WxLoader import WxLoader
from WxXmlParser import WxXmlParser

class WxParserLoader:

    def execute(self, collectedDir):
        """
        discover, parse and load weather files
        """
        success = 0
        failure = 0

        targets = os.listdir(collectedDir)
        for target in targets:
            fileName = "%s/%s" % (collectedDir, target)

            wxXmlParser = WxXmlParser()
            wxXmlParser.execute(fileName)

            station_id = wxXmlParser.key_value['station_id']
            if len(station_id) < 1:
                failure = failure+1
            else:
                wxLoader = WxLoader()
                if wxLoader.execute(wxXmlParser.key_value):
                    success = success+1
                else:
                    failure = failure+1

        print "end success:%d failure:%d" % (success, failure)

print 'start WxParserLoader'

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

    wxParserLoader = WxParserLoader()
    wxParserLoader.execute(collectedDir)

print 'stop WxParserLoader'

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
