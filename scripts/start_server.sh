#!/bin/bash
cd /home/ubuntu/ServiceNow-simulator/startpage
source environment/bin/activate
supervisord -c /home/ubuntu/ServiceNow-simulator/supervisord.conf
