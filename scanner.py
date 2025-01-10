import nmap

scanner = nmap.PortScanner()

print("Port Scanner\n")

# getting ip address
ip_add = input("Please enter your IP address: ")
print("The IP address entered is:", ip_add)

# type of scan
resp = input("""\nPlease select the type of scan you want to run:
1) Ping scan
2) TCP SYN scan
3) TCP connect scan
4) UDP scan
5) Aggressive scan
Enter your choice: """)

print("Nmap version:", scanner.nmap_version())

# Run the type of scan based on choice

if resp == '1':
    scanner.scan(ip_add, arguments='-sn')
    print("Scan info:", scanner.scaninfo())
    print("Host status:", scanner[ip_add].state())
elif resp == '2':
    scanner.scan(ip_add, '1-1024', '-sS')
    print("Scan info:", scanner.scaninfo())
    print("Open ports:", scanner[ip_add]['tcp'].keys())
elif resp == '3':
    scanner.scan(ip_add, '1-1024', '-sT')
    print("Scan info:", scanner.scaninfo())
    print("Open ports:", scanner[ip_add]['tcp'].keys())
elif resp == '4':
    scanner.scan(ip_add, '1-1024', '-sU')
    print("Scan info:", scanner.scaninfo())
    print("Open ports:", scanner[ip_add]['udp'].keys())
elif resp == '5':
    scanner.scan(ip_add, '1-1024', '-A')
    print("Scan info:", scanner.scaninfo())
    print("Open ports:", scanner[ip_add]['tcp'].keys())
else:
    print("Please enter a valid option.")


# Print additional details if scan ran successfully
print("\nIP Status:", scanner[ip_add].state())
print("Protocols found:", scanner[ip_add].all_protocols())
