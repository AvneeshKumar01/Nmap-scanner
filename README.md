# Port Scanner Script

## Overview

This is a Python-based **Port Scanner** script that utilizes the `nmap` module to perform various types of network scans on a specified IP address. It provides a simple and interactive interface for users to choose different scanning techniques to assess network security and discover open ports.

## Features

- **Interactive Input**: Users can input the target IP address and choose the desired scan type.
- **Multiple Scan Types**:
  1. **Ping Scan**: Quickly checks if the target host is online.
  2. **TCP SYN Scan**: Performs a stealthy TCP SYN scan to detect open ports.
  3. **TCP Connect Scan**: Completes a full TCP connection for port scanning.
  4. **UDP Scan**: Identifies open UDP ports on the target.
  5. **Aggressive Scan**: Performs detailed scanning with OS detection and service version detection.
- Displays:
  - Nmap version being used.
  - Host status (up or down).
  - Protocols found on the target host.
  - Details about open ports.

## Requirements

- **Python 3.6+**
- **Nmap module**: Install the `python-nmap` library.
  ```bash
  pip install python-nmap
