import heapq
import time

# Representasi graf sebagai adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 4, 'E': 2},
    'C': {'F': 5},
    'D': {'G': 1},
    'E': {'G': 3},
    'F': {'G': 2},
    'G': {}
}

# Fungsi rekursif untuk pencarian jalur optimal
def dfs_recursive(graph, node, target, path, cost, visited):
    if node == target:
        return (cost, path)
    
    visited.add(node)
    best_cost = float('inf')
    best_path = None
    
    for neighbor, weight in graph[node].items():
        if neighbor not in visited:
            total_cost, sub_path = dfs_recursive(graph, neighbor, target, path + [neighbor], cost + weight, visited)
            if total_cost < best_cost:
                best_cost = total_cost
                best_path = sub_path
    
    visited.remove(node)
    return (best_cost, best_path)

# Fungsi iteratif menggunakan Dijkstra
def dijkstra_iterative(graph, start, target):
    heap = [(0, start, [start])]  # (cost, node, path)
    visited = set()
    
    while heap:
        cost, node, path = heapq.heappop(heap)
        
        if node in visited:
            continue
        visited.add(node)
        
        if node == target:
            return (cost, path)
        
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(heap, (cost + weight, neighbor, path + [neighbor]))
    
    return (float('inf'), None)

# Pengujian dan perbandingan waktu
start_node = 'A'
target_node = 'G'

# Rekursif
start_time = time.time()
recursive_cost, recursive_path = dfs_recursive(graph, start_node, target_node, [start_node], 0, set())
recursive_time = time.time() - start_time

# Iteratif
start_time = time.time()
iterative_cost, iterative_path = dijkstra_iterative(graph, start_node, target_node)
iterative_time = time.time() - start_time

# Hasil
print("Rekursif:")
print(f"Jalur: {recursive_path}, Biaya: {recursive_cost}, Waktu: {recursive_time:.6f} detik")

print("\nIteratif:")
print(f"Jalur: {iterative_path}, Biaya: {iterative_cost}, Waktu: {iterative_time:.6f} detik")