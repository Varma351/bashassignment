#!/bin/bash

# Set main project directory i am using same directory
PROJECT_DIR="$(pwd)"

# Folder to back up (this same project folder)
SOURCE_DIR="$PROJECT_DIR"

# Folder where backups will be stored
BACKUP_DIR="$PROJECT_DIR/backups"

# Log file path
LOG_FILE="$BACKUP_DIR/backup.log"

# Date & time for filename
DATE=$(date +"%Y-%m-%d_%H-%M")

# Backup filename
BACKUP_FILE="$BACKUP_DIR/backup_$DATE.tar.gz"

# Create backup directory if it doesn’t exist
mkdir -p "$BACKUP_DIR"

echo "---------------------------------------------------"
echo "Starting backup process..."
echo " Date: $(date)"
echo "---------------------------------------------------"

# Perform backup (compress the entire folder)
tar -czf "$BACKUP_FILE" "$SOURCE_DIR" 2>>"$LOG_FILE"

# Check if backup succeeded
if [ $? -eq 0 ]; then
    echo "Backup created successfully: $BACKUP_FILE"
    echo "$(date) - SUCCESS - Backup created: $BACKUP_FILE" >> "$LOG_FILE"
else
    echo "Backup failed!"
    echo "$(date) - FAILED - Backup failed!" >> "$LOG_FILE"
fi

# Show backup size
if [ -f "$BACKUP_FILE" ]; then
    echo "Backup size: $(du -h "$BACKUP_FILE" | cut -f1)"
fi

echo "---------------------------------------------------"
echo " Backup completed and logged at: $LOG_FILE"

