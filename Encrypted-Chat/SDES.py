from collections import deque
#-------------------------------------
# Simple Des - Lucas de Morais Tramasso
# Seguranca Computacional
# Prof Valerio 
#-------------------------------------
def complete(text):
	if len(text) < 8:
		newText = map(int,str(text))
		while len(newText) < 8:
			newText.insert(0,'0')

		return magic(newText)
	else:
		return text
def magic(numList):
	s = map(str,numList)
	s = ''.join(s)
	return s

def keyGen(key,type):
	keylist = map(int,str(key))

	rotate = -3 if type == '2' else -1

	p10 = [3,5,2,7,4,10,1,9,8,6]
	p8 = [6,3,7,4,8,5,10,9]
	k = []
	#Executa a permutacao inicial de P10
	for i in range (0,10):         
		aux = p10[i]
		k.append(keylist[aux-1])
	#Transforma as duas metades em uma estrutura deque e efetua as rotacoes
	firstHalf = deque(k[:5])      
	secondHalf = deque(k[5:10])
	firstHalf.rotate(rotate)
	secondHalf.rotate(rotate)
	firstHalf = list(deque(firstHalf))
	secondHalf = list(deque(secondHalf))
	#limpa k para receber a permutacao da tabela P8
	del k[:]
	firstHalf.extend(secondHalf)
	#Executa a permutacao da tabela P8
	for i in range (0,8):
		aux = p8[i]
		k.append(firstHalf[aux-1])



	return k # types are k1 or k2

def ipPerm(text,type):
	ptext = map(int,str(text))

	ip = [4,1,3,5,7,2,8,6] if type == '-1' else [2,6,3,1,4,8,5,7]
	
	iptext = []

	for i in range (0,8):
		aux = ip[i]
		iptext.append(ptext[aux-1])
	return iptext # types are -1 or none for regular IP

def EP (text):
	ep = [4,1,2,3,2,3,4,1]
	#etext = map(int,str(text))

	eptext = []

	for i in range (0,8):
		aux = ep[i]
		eptext.append(text[aux-1])

	return eptext

def xor (text,k,size):
	aux = []
	for i in range (0,size):
		aux.append(int(text[i] != k[i]))
	return aux


def S (text,type):
	if type == '0': 
		s = ['01','00','11','10','11','10','01','00','00','10','01','11','11','01','11','10'] 
	if type == '1': 
		s = ['01','01','10','11','10','00','01','11','11','00','01','00','10','01','00','11']
	linha = int(str(text[0])+str(text[3]),2)
	coluna = int(str(text[1])+str(text[2]),2)

	return map(int,str(s[linha*4 + coluna]))

def p4 (text):
	p = [2,4,3,1]
	ptext = []
	for i in range (0,4):
		aux = p[i]
		ptext.append(text[aux-1])
	return ptext

def decrypt(text,key):
	k1 = keyGen(key,'1')
	k2 = keyGen(key,'2')
	aux = ipPerm(text,'1')

	fk = aux[:4]
	rightIP = aux[4:8]
	s0 = S(xor(EP(rightIP),k2,8)[:4],'0')
	s1 = S(xor(EP(rightIP),k2,8)[4:8],'1')
	s0.extend(s1)
	xored = xor(p4(s0),fk,4)


	fk2 = rightIP
	rightIP2 = xored
	s02 = S(xor(EP(rightIP2),k1,8)[:4],'0')
	s12 = S(xor(EP(rightIP2),k1,8)[4:8],'1')
	s02.extend(s12)
	xored2 = xor(p4(s02),fk2,4)

	xored2.extend(rightIP2)
	answer = ipPerm(magic(xored2),'-1')


	return binToChar(magic(answer))

def encrypt(text,key):
	k1 = keyGen(key,'1')
	k2 = keyGen(key,'2')
	aux = ipPerm(text,'1')

	fk = aux[:4]
	rightIP = aux[4:8]
	s0 = S(xor(EP(rightIP),k1,8)[:4],'0')
	s1 = S(xor(EP(rightIP),k1,8)[4:8],'1')
	s0.extend(s1)
	xored = xor(p4(s0),fk,4)


	fk2 = rightIP
	rightIP2 = xored
	s02 = S(xor(EP(rightIP2),k2,8)[:4],'0')
	s12 = S(xor(EP(rightIP2),k2,8)[4:8],'1')
	s02.extend(s12)
	xored2 = xor(p4(s02),fk2,4)

	xored2.extend(rightIP2)
	answer = ipPerm(magic(xored2),'-1')


	return binToChar(magic(answer))

def charToBin(text):
	return "{0:b}".format(ord(text))
def binToChar(binString):
	return chr(int(binString,2)) 

def encryptMessage(convKey,encText):
	keyList = []
	for i in range(0,len(convKey)):
		keyList.append(charToBin(convKey[i])) 
	key = magic(keyList)

	decText = []
	for i in range (0,len(encText)):
		decText.append(encrypt(complete(charToBin(encText[i])),key))
	return magic(decText)
def decryptMessage(convKey,encText):
	keyList = []
	for i in range(0,len(convKey)):
		keyList.append(charToBin(convKey[i])) 
	key = magic(keyList)

	decText = []
	for i in range (0,len(encText)):
		decText.append(decrypt(complete(charToBin(encText[i])),key))
	return magic(decText)

