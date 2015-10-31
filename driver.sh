#!/bin/bash
#
# Title:driver.sh
#
# Description:
#   drive vocal pelican collection/load cycle
#
# Development Environment:
#   OS X 10.10.5
#
# Author:
#   G.S. Cole (guycole at gmail dot com)
#
# Maintenance History:
#   $Id$
#
#   $Log$
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
#AWS_ACCESS_KEY_ID = "bogus"; export AWS_ACCESS_KEY_ID
#AWS_SECRET_ACCESS_KEY = "bogus"; export AWS_SECRET_ACCESS_KEY
#
mkdir collected
python ./vocal-pelican-py/WxCollector.py config.yaml
#
python ./vocal-pelican-py/WxParserLoader.py config.yaml
#