# Bash Scripting

## Overview

This project contains Bash scripts developed as part of my HyperionDev Cyber Security Bootcamp. The scripts demonstrate practical Linux system administration, file permissions management, package management, and automation.

---

## Scripts Included

### change_permissions.sh

A Bash script that changes the permissions of objects within a specified folder.

The script:

- Accepts a folder as a command-line argument
- Checks that the required argument was provided
- Uses `chmod` to set permissions to `644`
- Displays a confirmation message

The resulting permissions are:

```text
-rw-r--r--
```

### manage_apt.sh

A Bash script for basic Debian-based Linux system maintenance.

The script:

- Checks whether it is being run with root privileges
- Removes unused dependencies using `apt autoremove`
- Updates the software package database
- Upgrades installed packages
- Displays progress messages to the user

---

## Skills Demonstrated

- Bash scripting
- Linux file permissions
- `chmod`
- Linux package management
- `apt`
- Root privilege checking
- Command-line arguments
- Shell scripting logic
- System maintenance automation

---

## Technologies Used

- Bash
- Linux
- Debian-based package management (`apt`)

---

## Example Usage

### Change file permissions

```bash
sudo ./change_permissions.sh <folder>
```

### Manage system packages

```bash
sudo ./manage_apt.sh
```

---

## Learning Outcomes

This project strengthened my understanding of Linux administration and demonstrated how Bash scripts can be used to automate repetitive system-management tasks.

---

## Future Improvements

Possible enhancements include:

- More detailed error handling
- Logging script activity
- Adding confirmation prompts before destructive operations
- Supporting recursive permission changes
- Adding command-line options for different permission levels

---

**Author:** Niyaaz Dawjee