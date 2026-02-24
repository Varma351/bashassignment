#!/bin/bash

LOG_DIR="logs"
OUTPUT_FILE="alerts.log"

mkdir -p "$LOG_DIR"

echo "[*] Collecting logs from system journal..."

# Export important logs from systemd journal
sudo journalctl -u ssh > "$LOG_DIR/ssh.log" 2>/dev/null
sudo journalctl -p err > "$LOG_DIR/errors.log" 2>/dev/null
sudo journalctl > "$LOG_DIR/system.log" 2>/dev/null

echo "[+] Logs exported to $LOG_DIR/"

echo "[*] Starting analysis..."

> "$OUTPUT_FILE"

for file in "$LOG_DIR"/*.log; do
    [ -f "$file" ] || continue
    fname=$(basename "$file")

    # Failed SSH login detection
    grep -nE "Failed password" "$file" |
    while read -r line; do
        echo "[Failed SSH Login] $fname:$line" >> "$OUTPUT_FILE"
    done

    # Sudo usage detection
    grep -nE "sudo" "$file" |
    while read -r line; do
        echo "[Sudo Usage] $fname:$line" >> "$OUTPUT_FILE"
    done

    # Authentication failure detection
    grep -nE "authentication failure" "$file" |
    while read -r line; do
        echo "[Authentication Failure] $fname:$line" >> "$OUTPUT_FILE"
    done

    # Root access detection
    grep -nE "session opened for user root" "$file" |
    while read -r line; do
        echo "[Root Access] $fname:$line" >> "$OUTPUT_FILE"
    done
done

count=$(wc -l < "$OUTPUT_FILE")

echo "[✔] Log collection and analysis complete."
echo "Total alerts detected: $count"
echo "Report saved to: $OUTPUT_FILE"