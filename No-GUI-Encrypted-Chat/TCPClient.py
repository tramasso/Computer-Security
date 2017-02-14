import socket
from threading import Thread
import sys
import os
import SDES
import RC4
key = ''
cript = 'SDES'
def sendMessage(s):
	global key
	global cript
	while True:
		encMessage = ''
		message = raw_input()
		if(message == ':key'):
			key = raw_input('Digite a nova Key >> ')
			message = raw_input()
		if(message == ':cript'):
			cript = raw_input('SDES ou RC4? >> ')
			message = raw_input()
		if (cript == 'SDES'):
			encMessage = SDES.encryptMessage(str(key),message)
		if(cript == 'RC4'):
			encMessage = RC4.RC4(str(key),message)
		s.send(encMessage)
		print ('Sent: ' + message)
	s.close()

def receiveMessage(s):

	while True:

		data = s.recv(1024)
		if not data:
			break

		message = str(data)
		
		if (cript == 'SDES'):
			decMessage = SDES.decryptMessage(str(key),message)
		if(cript == 'RC4'):
			decMessage = RC4.RC4(str(key),message)
		print('Received: ' + decMessage)
	s.close()	

def Connect():
	global key
	ip = raw_input("Digite o IP >> ")
	port = raw_input("Digite a porta >> ")
	key = raw_input("Digite a key >> ")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.bind(('0.0.0.0',int(port)))
		s.listen(1)
		c, addr = s.accept()	
		print("Connection from: "  + str(addr) )
		#print ("Connection from: " + str(addr))

		t1 = Thread( target = receiveMessage, args = (c,)).start()
		t2 = Thread( target = sendMessage, args = (c,)).start()
	except:

		s.connect((str(ip),int(port)))
		addr = (str(ip),int(port))

		#ex.window3.textBrowser.append("Connected to: " + str(addr))
		print ("Connected to: " + str(addr))

		t1 = Thread( target = receiveMessage, args = (s,)).start()
		t2 = Thread( target = sendMessage, args = (s,)).start()


if __name__ == '__main__':
    Connect()


