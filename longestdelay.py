f=open("final.txt","r")
d=[]
c=[]
new=[]
for i in f:
	new.append(i.split())
new.reverse()
print("output node")
o=int(input())
class Edge:
	def __init__(self, source, dest, weight):

		self.source = source
		self.dest = dest
		self.weight = weight

class Graph:
	def __init__(self, edges, N):
		self.adjList = [[] for _ in range(N)]
		for edge in edges:
			self.adjList[edge.source].append(edge)


def DFS(graph, v, discovered, departure, time):
	discovered[v] = True
	for e in graph.adjList[v]:
		u = e.dest
		if not discovered[u]:
			time = DFS(graph, u, discovered, departure, time)
	departure[time] = v
	time = time + 1
	return time

def findLongestDistance(graph, source, N):
	departure = [-1] * N
	discovered = [False] * N
	time = 0
	for i in range(N):
		if not discovered[i]:
			time = DFS(graph, i, discovered, departure, time)
	cost = [float('inf')] * N
	cost[source] = 0
	for i in reversed(range(N)):
		v = departure[i]
		for e in graph.adjList[v]:
			u = e.dest
			w = e.weight * -1
			if cost[v] != float('inf') and cost[v] + w < cost[u]:
				cost[u] = cost[v] + w
	for i in range(N):
		d.append(i)
		b=cost[i]*-1
		c.append(b)
		a=max(c)
	for i in range(N):
		b=cost[i]*-1
		if(b==a):
			print("longest delay", (source, i), "=", (cost[i] * -1),"ns")

inpt_add=[]
output_add=[]
edgeList =[]
form_add=[]
add=[]
wire=[]
for i in range(len(new)):
    if(len(new[i])==6):
        a=new[i]
        inpt_add.append(a)
    if(len(new[i])==7):
        a=new[i]
        output_add.append(a)
    if (len(new[i]) == 5):
        a = new[i]
        form_add.append(a)

for f in form_add:
	a=(int(f[0]))
	b=(int(f[3].replace("gat","")))
	a1=(int(f[-1]))
	edgeList.append(Edge(a,b,a1))

for f in inpt_add:
	a=(int(f[0]))
	a1=(int(f[-1]))
	edgeList.append(Edge(a,a,a1))

for i in range(len(new)):
	a=new[i]
	if (len(a) == 2):
		wire.append(a)
ip = [i for i in new if i not in wire]

for i in range(len(ip)):
	a=ip[i]
	add.append(a[0])

ip1 = [i for i in ip if i not in inpt_add]
add1=[]
for i in range(len(output_add)):
	a=output_add[i]
	add1.append(a[0])


if __name__ == '__main__':
	for i in range(len(output_add)):
		b1=output_add[i]
		a=int(b1[0])
		d1=int(b1[-1])
		d2=int(b1[-2])
		d3=d1+d2
		b=wire[i]
		for j in range(len(b)):
			a1=int(b[j])
			edgeList.append(Edge(a,a1,d3))


	N = len(ip)+1
	graph = Graph(edgeList,N)
	findLongestDistance(graph,o,N)
