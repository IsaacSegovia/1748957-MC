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
