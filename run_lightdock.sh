#!/bin/bash

# Run lightdock in the background
lgd_run.py -s scoring.conf setup.json 10 -c 1 &

# Capture the PID of the application
APP_PID=$!

# Print "running" initially
echo "running"

# Loop to print "running" every 10 minutes
while kill -0 $APP_PID 2>/dev/null; do
    sleep 10m
    echo "running"
done

# Print "finished process" after the process has completed
echo "finished process"
