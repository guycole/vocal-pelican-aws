#
# Title:WxLoader.py
# Description:
# Development Environment:OS X 10.8.5/Python 2.7.2
# Author:G.S. Cole (guycole at gmail dot com)
#
import datetime
import rfc822

import os

import boto.ses

from boto.exception import JSONResponseError
from boto.dynamodb2.table import Table

class WxLoader:

    def execute(self, observation):
        station_id = observation['station_id']

        raw_time = observation['observation_time_rfc822']
        parsed_time = datetime.datetime.fromtimestamp(rfc822.mktime_tz(rfc822.parsedate_tz(raw_time)))

        epoch = datetime.datetime.utcfromtimestamp(0)
        delta = int((parsed_time - epoch).total_seconds())

        observation['ObservationTime'] = delta
        observation['StationId'] = station_id

        composite_key = "%s_%d" % (station_id, delta)
        observation['CompositeKey'] = composite_key

        region = os.environ['AWS_DEFAULT_REGION']
        accessKey = os.environ['AWS_ACCESS_KEY']
        secretKey = os.environ['AWS_SECRET_KEY']

        try:
            connx = boto.dynamodb2.connect_to_region(region, aws_access_key_id=accessKey, aws_secret_access_key=secretKey)
            obs_table = Table('VocalPelicanObservation', connection = connx)
            test_row = obs_table.get_item(CompositeKey=composite_key)
        except JSONResponseError as responseError:
            # authentication problem
            print responseError
        except boto.dynamodb2.exceptions.ItemNotFound as responseError:
            # not found implies safe to add
            return obs_table.put_item(observation)

        return False

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
