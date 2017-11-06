from heapq import heappop, heappush
from copy import deepcopy
import random

import time
def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst] 
    l = [] # empty list that will store current permutation
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]
       for p in permutation(remLst):
           l.append([m] + p)
    return l

class Fila:
    def __init__(self):
        self.fila= []
    def obtener(self):
        return self.fila.pop()
    def meter(self,e):
        self.fila.insert(0,e)
        return len(self.fila)
    @property
    def longitud(self):
        return len(self.fila)

class Pila:
    def __init__(self):
        self.pila= []
    def obtener(self):
        return self.pila.pop()
    def meter(self,e):
        self.pila.append(e)
        return len(self.pila)
    @property
    def longitud(self):
        return len(self.pila)


def flatten(L):
    while len(L) > 0:
        yield L[0]
        L = L[1]

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

    def BFS(self,ni):
        visitados =[]
        f=Fila()
        f.meter(ni)
        while(f.longitud>0):
            na = f.obtener()
            visitados.append(na)
            ln = self.vecinos[na]
            for nodo in ln:
                if nodo not in visitados:
                    f.meter(nodo)
        return visitados
    
    def DFS(self,ni):
        visitados =[]
        f=Pila()
        f.meter(ni)
        while(f.longitud>0):
            na = f.obtener()
            visitados.append(na)
            ln = self.vecinos[na]
            for nodo in ln:
                if nodo not in visitados:
                    f.meter(nodo)
        return visitados
    
    def shortest(self, v): # Dijkstra's algorithm
        q = [(0, v, ())] # arreglo "q" de las "Tuplas" de lo que se va a almacenar dondo 0 es la distancia, v el nodo y () el "camino" hacia el
        dist = dict() #diccionario de distancias 
        visited = set() #Conjunto de visitados
        while len(q) > 0: #mientras exista un nodo pendiente
            (l, u, p) = heappop(q) # Se toma la tupla con la distancia menor
            if u not in visited: # si no lo hemos visitado
                visited.add(u) #se agrega a visitados
                dist[u] = (l,u,list(flatten(p))[::-1] + [u])  	#agrega al diccionario
            p = (u, p) #Tupla del nodo y el camino
            for n in self.vecinos[u]: #Para cada hijo del nodo actual
                if n not in visited: #si no lo hemos visitado
                    el = self.E[(u,n)] #se toma la distancia del nodo acutal hacia el nodo hijo
                    heappush(q, (l + el, n, p)) #Se agrega al arreglo "q" la distancia actual mas la ditanacia hacia el nodo hijo, el nodo hijo n hacia donde se va, y el camino
        return dist #regresa el diccionario de distancias

    def kruskal(self):
        e = deepcopy(self.E)
        arbol = Grafo()
        peso = 0
        comp = dict()
        t = sorted(e.keys(), key = lambda k: e[k], reverse=True)
        nuevo = set()
        while len(t) > 0 and len(nuevo) < len(self.V):
            #print(len(t)) 
            arista = t.pop()
            w = e[arista]    
            del e[arista]
            (u,v) = arista
            c = comp.get(v, {v})
            if u not in c:
                #print('u ',u, 'v ',v ,'c ', c)
                arbol.conecta(u,v,w)
                peso += w
                nuevo = c.union(comp.get(u,{u}))
                for i in nuevo:
                    comp[i]= nuevo
        print('MST con peso', peso, ':', nuevo, '\n', arbol.E)
        return arbol

    def vecinoMasCercano(self):
        ni = random.choice(list(self.V))
        result=[ni]
        while len(result) < len(self.V):
            ln = set(self.vecinos[ni])
            le = dict()
            res =(ln-set(result))
            for nv in res:
                le[nv]=self.E[(ni,nv)]
            menor = min(le, key=le.get)
            result.append(menor)
            ni=menor
        return result
        
        

    
			
g= Grafo()
g.conecta('M','E', 8.9)
g.conecta('M','In', 8.6)
g.conecta('M','P', 8.6)
g.conecta('M','It', 10)
g.conecta('M','Ar', 7)
g.conecta('M','Al', 9.3)
g.conecta('M','J', 10.5)
g.conecta('M','F', 9.1)
g.conecta('M','B', 6.5)
g.conecta('E','It', 1.3)
g.conecta('E','P', 0.4)
g.conecta('E','It', 1.4)
g.conecta('E','Ar', 9.5)
g.conecta('E','Al', 1.6)
g.conecta('E','J', 10.8)
g.conecta('E','F', 0.8)
g.conecta('E','B', 7.6)
g.conecta('In','P', 1.5)
g.conecta('In','It', 1.4)
g.conecta('In','Ar', 10.5)
g.conecta('In','Al', 0.7)
g.conecta('In','J', 9.5)
g.conecta('In','F', 0.7)
g.conecta('In','B', 8.6)
g.conecta('P','It', 1.8)
g.conecta('P','Ar', 9.2)
g.conecta('P','Al', 1.9)
g.conecta('P','J', 11)
g.conecta('P','F', 1.1)
g.conecta('P','B', 7.3)
g.conecta('It','Ar', 10.9)
g.conecta('It','Al', 0.9)
g.conecta('It','J', 9.7)
g.conecta('It','F', 0.9)
g.conecta('It','B', 9)
g.conecta('Ar','Al', 11.1)
g.conecta('Ar','J', 17.4)
g.conecta('Ar','F', 10.3)
g.conecta('Ar','B', 1.9)
g.conecta('Al','J', 9.1)
g.conecta('Al','F', 0.8)
g.conecta('Al','B', 9.2)
g.conecta('J','F', 9.9)
g.conecta('J','B', 16.7)
g.conecta('F','B', 8.4)



print(g.kruskal())
#print(g.shortest('c'))


print(g)
k = g.kruskal()
print([print(x, k.E[x]) for x in k.E])

for r in range(10):
    ni = random.choice(list(k.V))
    dfs =  k.DFS(ni)
    c = 0
    #print(dfs)
    #print(len(dfs))
    for f in range(len(dfs) -1):
            c += g.E[(dfs[f],dfs[f+1])]
            print(dfs[f], dfs[f+1], g.E[(dfs[f],dfs[f+1])] )
            
    c += g.E[(dfs[-1],dfs[0])]
    print(dfs[-1], dfs[0], g.E[(dfs[-1],dfs[0])])
    print('costo',c)

dfs = g.vecinoMasCercano()
print(dfs)
c=0
for f in range(len(dfs) -1):
    c += g.E[(dfs[f],dfs[f+1])]
    print(dfs[f], dfs[f+1], g.E[(dfs[f],dfs[f+1])] )
    
c += g.E[(dfs[-1],dfs[0])]
print(dfs[-1], dfs[0], g.E[(dfs[-1],dfs[0])])
print('costo',c)



data = list('abcde')
#data = ['mty','saltillo', 'chi']
tim=time.clock()
per = permutation(data)
print(time.clock()-tim)
