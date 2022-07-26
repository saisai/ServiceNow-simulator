#!/bin/bash
kill -9 $(ps -ef | grep supervisord | awk '{print $2}')
cd /home/ubuntu/ServiceNow-simulator/startpage
source environment/bin/activate
supervisord -c /home/ubuntu/ServiceNow-simulator/supervisord.conf
