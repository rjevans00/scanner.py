#!/bin/python3 

import sys #allows to enter cmd line arguments amongst other things.
import socket
from datetime import datetime

#define target

if len(sys.argv) == 2:
       target = socket.gethostbyname(sys.argv[1]) #translate host name to IPV4
       
else:
       print("Invalid amount of arguments.")
       print("Syntax: python3 scanner.py <ip>")
       sys.exit()
             
             
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("." * 50)

try: 
        for port in range(50,85):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1) #float
                result = s.connect_ex((target,port)) #returns error indicator
                print("Checking port {}".format(port))
                if result == 0:
                        print("Port {} is open".format(port))
                s.close()
                
except KeyboardInterrupt:
       print("\n"'Exiting program.')
       sys.exit
       
except socket.gaierror:
       print("Hostname could not be resolved.")
       sys.exit()
              
except socket.error:
       print("couldn't connect to server.")
       sys.exit()              
                       
                       			 


           
