#!/bin/bash
cd /home/ubuntu/ServiceNow-simulator/startpage
source environment/bin/activate
supervisord -c supervisord.conf
