class Pila:
	def __init__(self):
		self.pila=[]

	def obtener(self):
		return self.pila.pop()
	def meter(self,e):
		self.pila.append(e)
		return len(self.pila)
	@property
	def longitud(self):
		return len(self.pila)

class Grafo:
 
    def __init__(self):
        self.V = set() # un conjunto
        self.E = dict() # un mapeo de pesos de aristas
        self.vecinos = dict() # un mapeo
 
    def agrega(self, v):
        self.V.add(v)
        if not v in self.vecinos: # vecindad de v
            self.vecinos[v] = set() # inicialmente no tiene nada
 
    def conecta(self, v, u, peso=1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v, u)] = self.E[(u, v)] = peso # en ambos sentidos
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)
 
    def complemento(self):
        comp= Grafo()
        for v in self.V:
            for w in self.V:
                if v != w and (v, w) not in self.E:
                    comp.conecta(v, w, 1)
        return comp
 
def DFS(grafo,ni):
    visitados=[ni]
    p=Pila()
    p.meter(ni)
    while (p.longitud>0):
        na=p.obtener()
        visitados.append(na)
        ln=grafo.vecinos[na]
        for nodo in ln:
            if nodo not in visitados:
                p.meter(nodo)
    return visitados


grafo=Grafo()
grafo.conecta('a','b')
grafo.conecta('a','c')
grafo.conecta('a','d')
grafo.conecta('b','e')
grafo.conecta('c','f')
grafo.conecta('c','g')
grafo.conecta('d','h')
grafo.conecta('e','i')
print(DFS(grafo,'a'))   #EL RESULTADO ES= ['a', 'a', 'c', 'g', 'f', 'b', 'e', 'i', 'd', 'h']
