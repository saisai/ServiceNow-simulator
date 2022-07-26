#!/bin/bash
sudo unlink /var/run/supervisor.sock
sudo kill -s SIGTERM $(sudo supervisorctl pid)
cd /home/ubuntu/ServiceNow-simulator/startpage
source environment/bin/activate
supervisord -c /home/ubuntu/ServiceNow-simulator/supervisord.conf
