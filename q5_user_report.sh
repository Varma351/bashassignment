#!/bin/bash

# File where the report will be stored
REPORT_FILE="user_security_report.txt"

# Start message for terminal user
echo "Generating user security report..."

# Write report header with date/time
echo "Report generated on: $(date)" > "$REPORT_FILE"
echo "----------------------------------------" >> "$REPORT_FILE"

# List all user accounts present in the system
# /etc/passwd stores user account details.
# We extract only the username field (first field).

echo "All system users:" >> "$REPORT_FILE"
cut -d: -f1 /etc/passwd >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# Find accounts having UID 0
# UID 0 means root-level privileges.
# Normally only 'root' should appear here.

echo "Accounts with UID 0 (root privileges):" >> "$REPORT_FILE"
awk -F: '$3 == 0 {print $1}' /etc/passwd >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

#  Detect accounts without passwords
# Password hashes are stored in /etc/shadow.
# Empty password field may indicate weak security.
# sudo is used because shadow file needs root access.
# Errors are hidden if permission is denied.

echo "Accounts with no password set:" >> "$REPORT_FILE"
sudo awk -F: '($2 == "" ) {print $1}' /etc/shadow 2>/dev/null >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

#Show users currently logged into the system
# 'who' displays active login sessions.

echo "Currently logged-in users:" >> "$REPORT_FILE"
who >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# Show recent login history
# 'last -n 5' shows last 5 login records from wtmp log.
# Useful to detect suspicious or unknown logins.

echo "Recent login history:" >> "$REPORT_FILE"
last -n 5 >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# Footer section of report
echo "----------------------------------------" >> "$REPORT_FILE"
echo "Report saved to $REPORT_FILE"

# Completion message for terminal
echo "User report generated successfully."
