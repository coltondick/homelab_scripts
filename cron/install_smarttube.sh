#!/bin/bash
# Set the correct PATH for cron
export PATH=/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/local/sbin

# Run the Python script
/usr/bin/python3 /docker/scripts/cron/install_smarttube.py >>/var/log/install_smarttube.log 2>&1
