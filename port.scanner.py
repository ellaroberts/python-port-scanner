import socket
target = input("Enter a website or IP address to scan: ")
print("Scanning target: ", target)
ports = range(1.101) #broader range to scan to find unexpected or hidden services
print("Ports we will scan:", ports)

print(f"\nScanning target: {target}\n")

for port in ports:
    print("Checking port", port)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a TCP connection tool so we can try to connect to this port
    
    s.settimeout(1) #timeout so scanner doesnt get stuck waiting on a port
    
    result = s.connect_ex((target, port)) #tries to connect to port, target and port needs the host and the service

    if result == 0:
        print("Port", port, "is open")
        s.close()

