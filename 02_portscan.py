#! /usr/bin/python3


#program to scan the ports range 1-1000

import socket
from termcolor import colored

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


host=input("enter the host IP address to scan : ")

def portscanner(port):
	if sock.connect_ex((host,port)):
		print(colored("port {} is closed" .format(port), 'red'))
	else:
		print(colored("port {} is open" .format(port), 'green'))

for port in range(1, 1000):
	portscanner(port)
