class Hamiltonian:
    def __init__(self, start):
        self.start = start
        self.cycle = []
        self.hasCycle = False

    def findCycle(self):
        self.cycle.append(self.start)
        self.solve(self.start)
 
    def solve(self, vertex):
        if vertex == self.start and len(self.cycle) == N + 1:
            self.hasCycle = True
            self.displayCycle()
            return
        for i in range(len(vertices)):
            if G[vertex][i] == 1 and visited[i] == 0:
                nbr = i
                visited[nbr] = 1
                self.cycle.append(nbr)
                self.solve(nbr)
                visited[nbr] = 0
                self.cycle.pop()
 
    def displayCycle(self):
        names = []
        for v in self.cycle:
            names.append(vertices[v])
        print(*names)
 
N=int(input("Enter the number of vertices: "))
vertices = []
for i in range(N):
    v=input("Enter vertex: ")
    vertices.append(v)

e=int(input("Enter the number of edges: "))
G=[]
for i in range(N):
    G.append([])
    for j in range(N):
        G[i].append(0)
for i in range(e):
    src=input("Enter source: ")
    dst=input("Enter destination: ")
    G[vertices.index(src)][vertices.index(dst)] = 1
    G[vertices.index(dst)][vertices.index(src)] = 1
visited = [0 for x in range(len(vertices))]

hamiltonian = Hamiltonian(0)
print("Hamiltonian Cycles: ")
hamiltonian.findCycle()

if not hamiltonian.hasCycle:
    print("No Hamiltonian Cycle")