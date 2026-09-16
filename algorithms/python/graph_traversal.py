from collections import deque

class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed
    
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
    
    def add_edge(self, src, dst):
        self.add_node(src)
        self.add_node(dst)
        self.graph[src].append(dst)
        
        if not self.directed:
            self.graph[dst].append(src)
    
    def bfs(self, start):
        if start not in self.graph:
            return []
        
        visited = set()
        queue = deque([start])
        order = []
        
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            
            visited.add(node)
            order.append(node)
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        
        return order
    
    def dfs(self, start):
        if start not in self.graph:
            return []
        
        visited = set()
        order = []
        
        def traverse(node):
            visited.add(node)
            order.append(node)
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    traverse(neighbor)
        
        traverse(start)
        return order
    
    def has_path(self, src, dst):
        return dst in self.bfs(src)
    
    def shortest_path(self, src, dst):
        if src not in self.graph:
            return None
        
        visited = {src}
        queue = deque([(src, [src])])
        
        while queue:
            node, path = queue.popleft()
            
            if node == dst:
                return path
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return None

if __name__ == "__main__":
