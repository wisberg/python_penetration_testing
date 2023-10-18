import nmap

scanner = nmap.PortScanner()

print("Welcome, this is an NMAP automation tool.")
print("<-------------------------------------->")

ip_addr = input("Please enter the IP Address you want to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("\n Select the type of scan you would like to perform. \n 1) SYN ACK Scan \n 2) UDP Scan \n 3) Comprehensive Scan \n")

print("You have selected option: ", resp)

if resp == '1':
    print('NMAP Version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -O', sudo=True)
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    
    for host in scanner.all_hosts():
        print("Host: %s (%s)" % (host, scanner[host].hostname()))
        if 'osclass' in scanner[host]:
            print("OS: %s" % scanner[host]['osclass'][0]['osfamily'])
        else:
            print("OS information not available for this host.")


elif resp == '2':
    print('NMAP Version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU', sudo=True)
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print('NMAP Version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU -sV -sC -A -O', sudo=True)
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports (TCP): ", list(scanner[ip_addr]['tcp'].keys()))
    print("Open Ports (UDP): ", list(scanner[ip_addr]['udp'].keys()))
    for host in scanner.all_hosts():
        print("Host: %s (%s)" % (host, scanner[host].hostname()))
        print("OS: %s" % scanner[host]['osclass'][0]['osfamily'])
else:
    exit