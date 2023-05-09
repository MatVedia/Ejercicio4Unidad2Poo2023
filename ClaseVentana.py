from ClaseVertice import Vertice

class Ventana ():
	def __init__(self, titulo="Inicio", xSup=0, ySup=0, xInf=500, yInf=500):
		self.__titulo = titulo
		self.__verticeSupIzqui = Vertice(xSup, ySup)
		self.__verticeInfDere = Vertice(xInf, yInf)
	
	def alto(self):
		return self.__verticeInfDere.getY() - self.__verticeSupIzqui.getY()
	
	def ancho(self):
		return self.__verticeInfDere.getX() - self.__verticeSupIzqui.getX()
	
	def getTitulo(self):
		return self.__titulo
		
	def mostrar(self):
		print ("verSupIzqui {} verInfDere {}".format(self.__verticeSupIzqui, self.__verticeInfDere))
	
	def moverDerecha(self, cantLugares=1):
		self.__verticeSupIzqui.setX(self.__verticeSupIzqui.getX() + cantLugares)
		self.__verticeInfDere.setX(self.__verticeInfDere.getX() + cantLugares)
		
	def moverIzquierda(self, cantLugares=1):
		self.__verticeSupIzqui.setX(self.__verticeSupIzqui.getX() - cantLugares)
		self.__verticeInfDere.setX(self.__verticeInfDere.getX() - cantLugares)
	
	def subir(self, cantLugares=1):
		self.__verticeSupIzqui.setY(self.__verticeSupIzqui.getY() + cantLugares)
		self.__verticeInfDere.setY(self.__verticeInfDere.getY() + cantLugares)
	
	def bajar(self, cantLugares=1):
		self.__verticeSupIzqui.setY(self.__verticeSupIzqui.getY() - cantLugares)
		self.__verticeInfDere.setY(self.__verticeInfDere.getY() - cantLugares)