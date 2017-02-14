def magic(numList):
	s = map(str,numList)
	s = ''.join(s)
	return s

def calcS(key):
	size = len(key) 
	S = range(256) #preenche S 
	j=0

	for i in range(0,256):
		j = (j + S[i] + key[i%size]) % 256 #executa operacao
		S[i], S[j] = S[j], S[i] #swap
	return S

def proc(S,text):
	i=0
	j=0
	vet = []
	for p in range(0,len(text)): #percorre o texto
		i = (i+1)%256
		j = (j+S[i])%256;
		S[i], S[j] = S[j], S[i]
		vet.append (S[(S[i] + S[j]) % 256]) #salva os valores no vetor de retorno 

	return vet

def RC4(convKey,text):
	key = keyConvert(convKey)
	S = calcS(key)
	vet = proc(S,text)
	answer = []
	for i in range (0,len(text)):
		answer.append(chr((ord(text[i])^vet[i]))) #executa XOR do caracter da entrada com o numero de retorno da funcao
	return magic(answer)

def keyConvert(key): #funcao que converte a chave em seus respectivos numeros
	return [ord(c) for c in key]


	

