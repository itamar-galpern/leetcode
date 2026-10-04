class UnionFind:

    def __init__(self, n):
        self.parent = {}
        self.height = {}

        for i in range(n):
            self.parent[i] = i
            self.height[i] = 0
    
    def find(self, k):
        p = self.parent[k]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.height[p1] > self.height[p2]:
            self.parent[p2] = p1
        elif self.height[p1] < self.height[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.height[p2] += 1
        return True

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = len(isConnected)
        union_find = UnionFind(provinces)

        for city_a in range(len(isConnected)):
            for city_b in range(city_a+1, len(isConnected[0])):
                if isConnected[city_a][city_b] and union_find.union(city_a, city_b):
                    provinces -= 1
        
        return provinces
        