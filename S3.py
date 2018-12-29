import socket
from time import *
print ctime(time())
import sys

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'connection established'
port = 8989

def client():
	node_2_connect  = raw_input("Enter ip address of server: ")
	s.connect((node_2_connect, port))
	print "connected"
	
	server_name = s.recv(1024)
	
	client_name = raw_input('enter username: ')
	s.send(client_name)
	
	while True:
		rep=s.recv(4096)
		print '|',server_name,': ',rep
		mess = raw_input('chat: ')
		if mess == 's3.exit':
			sys.exit()
		s.sendall(mess)

print 'Be a client or server'
print 'S <=> server\nC <=> client'

choice = raw_input('enter option from above menu: ')

if choice == 'S' or choice == 's':
	s.bind(('127.0.0.1',port))
	print 'bound'
	
	s.listen(5)
	print 'listening'
	
	serv_name=raw_input('enter username: ')
	print 'Type "s3.exit" to close the application'

	while True:
		c,addr=s.accept()
		print addr[0],':',addr[1]
		
		c.send(serv_name)
		
		xcx = c.recv(1024)
		
		while True:
			mess=raw_input('chat: ')
			if mess == 's3.exit':
				sys.exit()
			c.send(mess)
			print '|',xcx,': ',c.recv(1024)
        	#c.close()
     
     
if choice == 'C' or choice == 'c':
	client()
