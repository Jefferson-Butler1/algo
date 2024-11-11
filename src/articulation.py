class ArticulationPointFinder:
    def __init__(self, graph):
        self.graph = graph
        self.time = 0
        n = len(graph.adj)
        
        self.disc = [-1] * n
        self.low = [-1] * n
        self.parent = [-1] * n
        self.is_articulation_point = [False] * n
        
        for i in range(n):
            if self.disc[i] == -1:
                self._dfs(i)
    
    def _dfs(self, u):
        children = 0
        self.disc[u] = self.low[u] = self.time
        self.time += 1
        
        for v in self.graph.neighbors(u):
            if self.disc[v] == -1:
                children += 1
                self.parent[v] = u
                self._dfs(v)
                
                self.low[u] = min(self.low[u], self.low[v])
                
                if self.parent[u] == -1 and children > 1:
                    self.is_articulation_point[u] = True
                    
                if self.parent[u] != -1 and self.low[v] >= self.disc[u]:
                    self.is_articulation_point[u] = True
                    
            elif v != self.parent[u]:
                self.low[u] = min(self.low[u], self.disc[v])
