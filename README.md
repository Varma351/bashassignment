# Basic Linux Shell Scripts

## About

This repository contains simple Bash scripts that I created while learning Linux shell scripting. These programs are beginner-level and help me understand basic commands and automation.

---

## Files

### 1. q1_system_info.sh  
This script shows system details like:
- Hostname  
- User  
- Date and time  
- OS and kernel version  
- CPU, memory, disk usage  
- IP address  

Run:
```bash
chmod +x q1_system_info.sh
./q1_system_info.sh
```

---

### 2. q2_file_manager.sh  
This is a simple file management system.

Options:
1. Create file  
2. Display file  
3. Copy file  
4. Move file  
5. Delete file  
6. Exit  

Run:
```bash
chmod +x q2_file_manager.sh
./q2_file_manager.sh
```

---

### 3. q3_log_analyzer.sh  
This script collects and checks system logs.

It detects:
- Failed SSH logins  
- Sudo usage  
- Authentication failures  
- Root access  

It saves the report in `alerts.log`.

Run:
```bash
chmod +x q3_log_analyzer.sh
sudo ./q3_log_analyzer.sh
```

---

### 4. q4_backup.sh  
This script creates a backup of the current project folder.

- Creates a backup folder  
- Compresses files using tar  
- Saves log in `backup.log`  

Run:
```bash
chmod +x q4_backup.sh
./q4_backup.sh
```

---

### 5. Q5_user_report.sh  
This script generates a user security report.

It:
- Lists all system users  
- Shows accounts with UID 0 (root privileges)  
- Detects accounts without passwords  
- Shows currently logged-in users  
- Displays recent login history  

The report is saved in `user_security_report.txt`.

Run:
```bash
chmod +x Q5_user_report.sh
sudo ./Q5_user_report.sh
```

---