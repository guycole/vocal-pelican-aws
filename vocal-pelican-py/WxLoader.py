#
# Title:WxLoader.py
# Description:
# Development Environment:OS X 10.8.5/Python 2.7.2
# Legalise:Copyright (C) 2013 Digital Burro, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#

from WxXmlParser import WxXmlParser

class WxLoader:

    def execute(self, weatherDb, wxXmlParser):
        """
        words
        """
#        print "loader execute:%s" % (wxXmlParser.getStationId())

        stationId = wxXmlParser.getStationId()
        timeStamp = wxXmlParser.getTimeStamp()
        dewPoint = wxXmlParser.getDewPoint()
        humidity = wxXmlParser.getHumidity()
        pressure = wxXmlParser.getPressure()
        temperature = wxXmlParser.getTemperature()
        visibility = wxXmlParser.getVisibility()
        weather = wxXmlParser.getWeather()
        windDirection = wxXmlParser.getWindDirection()
        windGust = wxXmlParser.getWindGust()
        windSpeed = wxXmlParser.getWindSpeed()
        latitude = wxXmlParser.getLatitude()
        longitude = wxXmlParser.getLongitude()

#
# check for duplicate
#

        sql = "select id from raw_sample where station_id = '%s' and time_stamp = '%s'" % (stationId, timeStamp)
        cursor = weatherDb.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        cursor.close()

        if (row == None):
            sql = "insert into raw_sample(station_id, time_stamp, dew_point, humidity, pressure, temperature, visibility, wind_direction, wind_gust, wind_speed, latitude, longitude, weather) values('%s','%s', %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, '%s')" % (stationId, timeStamp, dewPoint, humidity, pressure, temperature, visibility, windDirection, windGust, windSpeed, latitude, longitude, weather)
            cursor = weatherDb.cursor()
            cursor.execute(sql)
            weatherDb.commit()
            cursor.close()
            return 1

        return 0

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
