#!/bin/bash
# -------------------------------------------------
# Script Name: q1_system_info.sh
# Description: Displays important system information
# Author: Your Name
# Date: $(date)
# -------------------------------------------------

echo "****************************"
echo "       system info          "
echo "****************************"

echo "Hostname: $(hostname)"

echo "Logged in user: $USER"

echo "Current date & time: $(date)"

echo "System Uptime:"
uptime -p

echo "Operating System:"
grep PRETTY_NAME /etc/os-release | cut -d= -f2

echo "Kernel Version: $(uname -r)"

echo "CPU Model:"
lscpu | grep "Model name" | cut -d: -f2

echo "Memory Usage:"
free -h

echo "Disk Usage:"
df -h /

echo "IP Address:"
hostname -I

echo "****************************"
echo "           End              "
echo "****************************"

