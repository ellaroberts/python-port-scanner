# Python Port Scanner

This project is a simple TCP port scanner built in Python that scans a target host for open ports.

## Features
- Scans a range of ports on a target IP address
- Identifies open ports using TCP connections
- Demonstrates basic network scanning techniques

## Tools Used
- Python
- Socket library

## How It Works
The scanner attempts to connect to each port on the target system.  
If a connection is successful, the port is marked as open.

## How to Run
1. Run the script:
   python port_scanner.py

2. Enter a target IP address (e.g. 127.0.0.1)

## Example Output
Port 80 is open  
Port 443 is open  

## What I Learned
- How TCP connections work
- Basics of port scanning and network enumeration
- How attackers identify open services on a network
