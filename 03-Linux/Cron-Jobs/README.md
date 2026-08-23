# Cron Jobs

## Overview

This project demonstrates the use of Linux `cron` jobs to automate scheduled tasks. It was completed as part of my HyperionDev Cyber Security Bootcamp.

The project includes examples of configuring scheduled tasks and verifying that they execute as expected.

---

## Cron Jobs Included

### NetworkManager Restart

A scheduled cron job was configured to restart the Linux NetworkManager service automatically at **4:00 PM each day**.

The job uses `systemctl` to restart the service:

```bash
systemctl restart NetworkManager
```

This demonstrates how cron can be used to automate routine system administration tasks.

### Cron Job Demonstration

The project also includes a second cron-job exercise demonstrating the creation and scheduling of an automated task.

The accompanying screenshot provides evidence of the configured cron job.

---

## Evidence

- `netman_job.jpg` — Evidence of the NetworkManager scheduled task
- `prank_job.jpg` — Evidence of the additional cron-job exercise

---

## Skills Demonstrated

- Linux cron scheduling
- Crontab configuration
- Linux system administration
- `systemctl`
- Service management
- Task automation
- Troubleshooting scheduled jobs

---

## Technologies Used

- Linux
- Bash
- Cron
- systemd / systemctl

---

## Learning Outcomes

This project developed my understanding of Linux task scheduling and demonstrated how cron can be used to automate recurring administrative tasks.

It also provided practical experience configuring, testing, and troubleshooting scheduled jobs.

---

## Future Improvements

Possible enhancements include:

- Adding logging for scheduled tasks
- Redirecting cron output to log files
- Monitoring whether scheduled jobs completed successfully
- Creating additional automated maintenance tasks
- Adding error handling and notifications

---

**Author:** Niyaaz Dawjee