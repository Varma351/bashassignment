#!/bin/bash

# Hostname
HOSTNAME=$(hostname)

# Current User
USER_NAME=$(whoami)

# Date and Time
DATE_TIME=$(date)

# OS Name
if [ -f /etc/os-release ]; then
    OS_NAME=$(grep "^NAME=" /etc/os-release | cut -d= -f2 | tr -d '"')
else
    OS_NAME=$(uname -s)
fi

# Kernel Version
KERNEL_VERSION=$(uname -r)

# CPU Usage
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print 100 - $8 "%"}')

# Memory Usage
MEMORY_USAGE=$(free -m | awk 'NR==2{printf "%s MB / %s MB (%.2f%%)", $3,$2,$3*100/$2 }')

# Disk Usage (Root)
DISK_USAGE=$(df -h / | awk 'NR==2{printf "%s / %s (%s)", $3,$2,$5}')

# IP Address (Auto-detect active interface)
IP_ADDRESS=$(hostname -I | awk '{print $1}')

echo "=============================================="
echo "Hostname        : $HOSTNAME"
echo "User            : $USER_NAME"
echo "Date & Time     : $DATE_TIME"
echo "OS              : $OS_NAME"
echo "Kernel Version  : $KERNEL_VERSION"
echo "----------------------------------------------"
echo "CPU Usage       : $CPU_USAGE"
echo "Memory Usage    : $MEMORY_USAGE"
echo "Disk Usage      : $DISK_USAGE"
echo "IP Address      : $IP_ADDRESS"
echo "=============================================="