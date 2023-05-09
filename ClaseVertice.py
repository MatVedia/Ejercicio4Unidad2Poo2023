class Vertice ():
	def __init__(self, x, y):
		self.__x = x
		self.__y = y
	
	def __str__(self):
		return "({}, {})".format(self.__x, self.__y)
	
	def getX(self):
		return self.__x
	
	def setX(self, nuevoValor):
		self.__x = nuevoValor
	
	def getY(self):
		return self.__y
	
	def setY(self, nuevoValor):
		self.__y =nuevoValor