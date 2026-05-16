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

The application contains a Python function that executes a system ping command using the subprocess module.

Initial implementation:

```python
command = "ping -c 1 " + host
return subprocess.check_output(command, shell=True)

## How the Application Works

The application contains a function called `ping_host()` which executes a system ping command against a provided host.

Example:

```python
from app.vulnerable_app import ping_host

response = ping_host("google.com")
print(response)
