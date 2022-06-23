'''
A* algorithm for graphs
'''

import sys
import queue
import math
import heapq

class AStar:
    def __init__(self, n, adj, cost, x, y):
        # See the explanations of these fields in the starter for friend_suggestion        
        self.n = n
        self.adj = adj
        self.cost = cost
        self.inf = n*10**6
        self.dist = [self.inf]*n
        self.visited = [False]*n
        self.proc=[]
        self.workset = []
        self.poten=[0]*n
        # Coordinates of the nodes
        self.x = x
        self.y = y

    # See the explanation of this method in the starter for friend_suggestion
    def clear(self):
            self.dist = [self.inf]*n
            self.visited = [False]*n
            self.proc=[]
        #del self.workset[0:len(self.workset)]

    def potential(self,v,t):
            #print("v",v)
            #print("t",t)
            poten=math.sqrt((self.x[v]-self.x[t])**2+(self.y[v]-self.y[t])**2)
            return poten


    def relax(self,q,v,distance,measure):
        #print("self.dist",self.dist)
        if self.dist[v]>distance:
            self.dist[v]=distance
            heapq.heappush(q,(self.dist[v]+measure,v))
            #print("heap",q)
            self.proc.append(v)

    def extract_min(self,q):
        r,v=heapq.heappop(q)
        return r,v

    def process(self,v,q,t,adj,cost):
        for u,w in zip(adj[v],cost[v]):
            if not self.visited[u]:
                self.relax(q,u,self.dist[v]+w,self.potential(u,t))

    # See the explanation of this method in the starter for friend_suggestion
    def visit(self, q, p, v, dist, measure):
        # Implement this method yourself

        pass

    # Returns the distance from s to t in the graph
    def query(self, s, t):
        self.clear()
        q = []
        #print(self.potential(s,t))
        #print(self.dist)
        self.relax(q,s,0,self.potential(s,t))
        #print(self.dist)
        #print("q",q)

        if s==t:
            return 0

        while len(q)!=0:
            r,v=self.extract_min(q)

            if v==t:
                return(self.dist[t] if self.dist[t]!=self.inf else -1)

            if not self.visited[v]:
                self.process(v,q,t,adj,cost)
                self.visited[v]=True
        return -1





def readl():
    return map(int, sys.stdin.readline().split())

if __name__ == '__main__':
    n,m = readl()
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for i in range(n):
        a, b = readl()
        x[i] = a
        y[i] = b
    for e in range(m):
        u,v,c = readl()
        adj[u-1].append(v-1)
        cost[u-1].append(c)
    t, = readl()
    astar = AStar(n, adj, cost, x, y)
    out=[]
    for i in range(t):
        s, t = readl()
        out.append(astar.query(s-1, t-1))

    print(*out,sep="\n")
