#!/bin/bash
cd /home/ubuntu/ServiceNow-simulator
source environment/bin/activate
supervisord -c supervisord.conf
