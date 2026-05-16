# SAST Scan in Azure DevOps Pipeline

## Project Topic
DevOps Security and Compliance

---

# Project Objective

This project demonstrates how to integrate a Static Application Security Testing (SAST) tool into a CI/CD pipeline using Azure DevOps Pipelines.

The project includes:
- a vulnerable Python application
- automated testing
- automated security scanning
- vulnerability remediation

---

# Technologies Used

- Python 3.11
- GitHub
- Azure DevOps Pipelines
- Bandit
- Pytest

---

# What is SAST?

SAST (Static Application Security Testing) is a security testing method that analyzes source code without executing the application.

It helps developers identify vulnerabilities early in the software development lifecycle.

---

# SAST Tool Used

## Bandit

Bandit is a security linter designed specifically for Python applications.

It scans Python source code and identifies common security vulnerabilities such as:
- command injection
- insecure subprocess usage
- hardcoded passwords
- unsafe deserialization

Official documentation:
https://bandit.readthedocs.io/

---

# Application Description

The application created for this project is a small Python utility that executes a network ping command against a specified host.

Its purpose is not to provide a complete networking tool, but to simulate a realistic scenario where a developer uses operating system commands inside an application.

The application contains a function named `ping_host()` which receives a hostname or IP address as input and executes the Linux `ping` command using Python's `subprocess` module.

Example:

```python
from app.vulnerable_app import ping_host

response = ping_host("google.com")
print(response)
```

When executed on Linux, the function runs a command similar to:

```bash
ping -c 1 google.com
```

The initial implementation intentionally used an insecure subprocess configuration in order to demonstrate how SAST tools identify security vulnerabilities during automated CI/CD execution.

The vulnerable implementation was:

```python
import subprocess

def ping_host(host):
    command = "ping -c 1 " + host
    return subprocess.check_output(command, shell=True)
```

The issue with this implementation is the use of:

```python
shell=True
```

When shell execution is enabled, user input may be interpreted directly by the operating system shell. This creates the possibility of command injection attacks.

For example, an attacker could attempt to inject additional commands such as:

```text
google.com && malicious_command
```

This type of vulnerability is classified as:
- CWE-78: OS Command Injection

Bandit successfully identified this issue during the security scanning stage of the Azure DevOps pipeline.

After the vulnerability was detected, the application was remediated using a safer subprocess implementation:

```python
import subprocess

def ping_host(host):
    return subprocess.check_output(["ping", "-c", "1", host])
```

The remediated version removes shell interpretation and safely passes command arguments directly to the operating system.