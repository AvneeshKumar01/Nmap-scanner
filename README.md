# Port Scanner Script

## Overview

This project includes both a Python-based **Port Scanner** script and a Bash script to perform various types of network scans on a specified IP address. Both scripts provide interactive interfaces for users to choose different scanning techniques to assess network security and discover open ports.

---

## Features

### **Python Script**
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

### **Bash Script**
- **Easy-to-Use**: The Bash script offers a quick and straightforward way to perform similar scans without requiring Python.
- **Multiple Scan Options**:
  1. **Ping Scan**: Check host availability.
  2. **TCP SYN Scan**: Stealthily detect open ports.
  3. **UDP Scan**: Identify open UDP ports.
  4. **Aggressive Scan**: Includes OS detection and detailed service scans.
- **Interactive Interface**: Users can select scan options from a menu.

---

## Requirements

### **For Python Script**
- **Python 3.6+**
- **Nmap module**: Install the `python-nmap` library.
  ```bash
  pip install python-nmap
  ```

### **For Bash Script**
- **Nmap**: Ensure Nmap is installed on your system.
  ```bash
  # On Linux (Ubuntu/Debian):
  sudo apt install nmap -y

  # On macOS:
  brew install nmap

  # On Windows:
  choco install nmap
  ```

---

## How to Use

### **Python Script**
1. Run the script:
   ```bash
   python3 port_scanner.py
   ```
2. Follow the prompts to input the target IP address and select the scan type.

### **Bash Script**
1. Make the script executable:
   ```bash
   chmod +x port_scanner.sh
   ```
2. Run the script:
   ```bash
   ./port_scanner.sh
   ```
3. Follow the menu to choose your scan type and input the target IP address.

---

## Example Outputs

### **Python Script Example**
```bash
Nmap version: 7.93
Target: 192.168.1.1
Host is up (0.12s latency).
Open ports:
22/tcp   SSH
80/tcp   HTTP
443/tcp  HTTPS
```  

### **Bash Script Example**
```bash
Select Scan Type:
1. Ping Scan
2. TCP SYN Scan
3. UDP Scan
4. Aggressive Scan
5. Exit

Enter your choice: 2
Enter target IP address: 192.168.1.1

...Performing TCP SYN Scan...

PORT    STATE SERVICE
22/tcp  open  ssh
80/tcp  open  http
443/tcp open  https
```

