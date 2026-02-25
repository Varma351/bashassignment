# 🐧 Bash Assignment – Linux User Security & Audit Scripts

This repository contains Bash scripts created as part of a Linux / Cybersecurity assignment.
The scripts focus on **user auditing, security checks, login monitoring, and system reporting** using standard Linux command-line tools.

---

## 📌 Features

* List all system users
* Detect root-privileged accounts (UID 0)
* Identify accounts without passwords
* Show currently logged-in users
* Display recent login history
* Generate a formatted security report file

The scripts demonstrate use of common Linux tools such as:

* `awk`
* `cut`
* `who`
* `last`
* `sudo` access to `/etc/shadow`

---

## 📂 Example Script Functionality

The main script generates a report containing:

* All users in `/etc/passwd`
* Root-level accounts
* Password status from `/etc/shadow`
* Active sessions
* Login history

Example output:

```
User Security Report
---------------------
All system users:
root
daemon
kali

Accounts with UID 0:
root

Currently logged in users:
kali tty7 still logged in
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Varma351/bashassignment.git
cd bashassignment
```

### 2. Make the script executable

```bash
chmod +x scriptname.sh
```

### 3. Run the script

```bash
./scriptname.sh
```

Some checks may require administrator permission:

```bash
sudo ./scriptname.sh
```

---

## 🎯 Learning Objectives

This project demonstrates:

* Linux user management concepts
* System security auditing basics
* Log inspection techniques
* Bash scripting automation
* File parsing using command-line tools

---

## 👨‍💻 Author

**Tharun Varma K**
Student Project – Linux & Cybersecurity

---

## 📜 License

This project is created for educational purposes only.
