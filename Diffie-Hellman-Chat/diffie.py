from random import randint


class diffieHellman:
	def __init__(self):
		self.q = pow(2,101)-69
		self.a = pow(2,80)-65
	def getY(self):
		self.x = randint(0,self.q)
		return pow(self.a,self.x,self.q)
	def getKey(self,y):
		return pow(y,self.x,self.q)





