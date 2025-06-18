#built-in socket module
import socket ## Create network connections (TCP/IP) ## Scan and interact with other systems over a networ
def scan(target):
    print(f"scan port on {target}")
    for port in range(1, 1025):
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(0.5)
            result= s.connect_ex((target,port))
            if result == 0:
               print(f"Port{port} is open")
            s.close()

        except:
        
         pass
    
target_ip = input("Enter IP address or hostname: ")
scan(target_ip)



    