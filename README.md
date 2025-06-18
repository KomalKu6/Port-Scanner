# Port-Scanner   Day 1 – Cybersecurity Automation Tools

Write a Python script that scans open ports on a target IP

------------------------------
What I learnt:
------------------------------
socket module (network hacking basics)
IP addressing & port scanning logic
Python loops + error handling

Goal -> Scan a target (hostname/IP) for open ports

To Learn: 
- Python socket programming
- How TCP connection scanning works
- Port scanning automation (like a mini-Nmap)
- Error handling, user input, and modular code design

  🔧 Features:
- Scans **ports 1–1024**
- Uses TCP to check if a port is open
- Fast scanning with `timeout`
- Clean CLI interface

Line-by-Line Explanation
Line	            What it Does
import socket: 	  Brings in Python's low-level networking module
socket.socket(): 	Creates a new TCP socket
connect_ex():     Attempts to connect to the port
result == 0:     	Means port is open
settimeout(0.5): 	Prevents hanging on unresponsive ports
try/except: 	    Avoids crashes from network errors

----------------------------------------------------  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
-----------------------------------------------------
-> We create a TCP socket:
-> AF_INET: means IPv4
-> SOCK_STREAM: means TCP connection
-> This is like opening a door and knocking on a port.

note:
connect_ex() -> returns a numeric error code, which is easier to check (0 = success)
socket.socket() -> Creates a new TCP socket
socket.AF_INET: IPv4 address family
socket.SOCK_STREAM: TCP socket (not UDP)
s.settimeout(0.5): Timeout in seconds (faster scanning)
s.connect_ex(): Tries to connect to (target, port)
Returns 0 → Success (port is open)
Any other code → Failed (port closed or filtered)

Why Are We Scanning Ports?
Port scanning = digital door knocking
Real Example:
Hacker scans a cloud IP. Finds port 8080 open.
Tries HTTP request: sees Jenkins login page.
Default creds work. Full server access.

