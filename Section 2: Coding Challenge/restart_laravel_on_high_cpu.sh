#!/bin/bash

SERVICE_NAME="php5-fpm.service"

CPU_THRESHOLD=80

# Get the PID of the Laravel backend process
PID=$(ps aux | grep "[l]aravel" | awk '{print $2}')

if [ -z "$PID" ]; then
  echo "Laravel backend process not found."
  exit 1
fi

CPU_USAGE=$(ps -p $PID -o %cpu | awk 'NR==2 {print int($1)}')

# Check if CPU usage exceeds the threshold
if [ "$CPU_USAGE" -gt "$CPU_THRESHOLD" ]; then
  echo "CPU usage ($CPU_USAGE%) exceeds the threshold ($CPU_THRESHOLD%). Restarting $SERVICE_NAME..."
  
  sudo systemctl restart $SERVICE_NAME

  if [ $? -eq 0 ]; then
    echo "$SERVICE_NAME restarted successfully."
  else
    echo "Failed to restart $SERVICE_NAME."
    exit 1
  fi
else
  echo "CPU usage ($CPU_USAGE%) is within the threshold ($CPU_THRESHOLD%). No action taken."
fi