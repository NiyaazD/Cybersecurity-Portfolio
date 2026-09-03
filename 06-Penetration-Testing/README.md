# Penetration Testing

## Overview

This project demonstrates practical penetration testing techniques performed against a controlled local virtual machine environment.

The assessment covered network service discovery, vulnerability identification, exploitation, and verification of access obtained through a vulnerable service.

---

## Assessment Stages

### Stage 1 – Service Discovery

Nmap was used to perform a service version scan against the target machine.

**Target IP:**

`192.168.1.7`

The following services were identified:

| Port | Service | Version |
|------|---------|---------|
| 21 | FTP | ProFTPD 1.3.3c |
| 22 | SSH | OpenSSH 7.2p2 |
| 80 | HTTP | Apache httpd 2.4.18 |

The discovered services were reviewed for potential vulnerabilities and misconfigurations.

---

### Stage 2 – Vulnerability Research

The discovered services were researched using Metasploit.

The FTP service running **ProFTPD 1.3.3c** was identified as vulnerable to a known backdoor vulnerability.

The Metasploit module used to identify the vulnerability was:

`exploit/unix/ftp/proftpd_133c_backdoor`

The vulnerability is associated with a compromised ProFTPD source package released in late 2010 and allows remote command execution on vulnerable systems.

---

### Stage 3 – Exploitation

The identified ProFTPD vulnerability was exploited using the Metasploit module:

`exploit/unix/ftp/proftpd_133c_backdoor`

After configuring the target and payload, the exploit successfully established a command shell session on the target machine.

This demonstrated that the vulnerable FTP service could be used to achieve remote command execution.

---

### Stage 4 – Access Verification

The obtained command shell was used to verify access to the target system.

The evidence includes terminal output demonstrating the privileges obtained after successful exploitation.

---

## Evidence

Assessment evidence is stored in the `Assessment-Evidence` directory.

The evidence includes:

- `Penetration-Testing-Assessment.pdf`
- `penetration_testing.pdf`

`Penetration-Testing-Assessment.pdf` contains the documented assessment findings and supporting screenshots. :contentReference[oaicite:0]{index=0}

---

## Tools Used

- Nmap
- Metasploit Framework
- Kali Linux
- Virtual Machine environment

---

## Learning Outcomes

This project provided practical experience with:

- Network service enumeration
- Service version identification
- Vulnerability research
- Metasploit module selection
- Exploitation of a known vulnerability
- Establishing a command shell
- Verifying access following exploitation
- Documenting penetration testing findings

---

## Security Considerations

The activities documented in this project were performed against a controlled virtual machine environment for educational and cybersecurity training purposes.

Penetration testing should only be performed against systems where explicit authorization has been provided.

---

**Author:** Niyaaz Dawjee