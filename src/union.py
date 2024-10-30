class WeightedQuickUnion:

    def __init__(self, n):
        self.count = n
        self.parent = list(range(n))
        self.size = [1] * n 

    def find(self, p, root = None):
        assert(p)
        if p == self.parent[p]: 
            return p
        self.parent[p] = self.find(p, root)
        return self.parent[p]

    def findOld(self, p):
        while p != self.parent[p]:
            p = self.parent[p]
        return p
    def connected(self, p, q):
        return self.find(p)
