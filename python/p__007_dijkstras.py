class IndexedMinHeap:
    def __init__(self):
        self.heap = []  # Stores (distance, node_id)
        self.pos = {}  # Maps node_id -> index in self.heap

    def push_or_update(self, node_id, dist):
        if node_id not in self.pos:
            self.heap.append((dist, node_id))
            self.pos[node_id] = len(self.heap) - 1
            self._sift_up(len(self.heap) - 1)
        elif dist < self.heap[self.pos[node_id]][0]:
            idx = self.pos[node_id]
            self.heap[idx] = (dist, node_id)
            self._sift_up(idx)

    def pop(self):
        if not self.heap:
            return None
        root_dist, root_node = self.heap[0]
        last_val = self.heap.pop()
        del self.pos[root_node]

        if self.heap:
            self.heap[0] = last_val
            self.pos[last_val[1]] = 0
            self._sift_down(0)
        return root_node, root_dist

    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        if idx > 0 and self.heap[idx][0] < self.heap[parent][0]:
            self._swap(idx, parent)
            self._sift_up(parent)

    def _sift_down(self, idx):
        smallest = idx
        left, right = 2 * idx + 1, 2 * idx + 2
        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right
        if smallest != idx:
            self._swap(idx, smallest)
            self._sift_down(smallest)

    def _swap(self, i, j):
        self.pos[self.heap[i][1]], self.pos[self.heap[j][1]] = j, i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


def dijkstra(graph, start_node):
    distances = {node: float("inf") for node in graph}
    distances[start_node] = 0
    pq = IndexedMinHeap()
    pq.push_or_update(start_node, 0)
    visited = set()

    while pq.heap:
        current_node, current_dist = pq.pop()
        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            if neighbor in visited:
                continue
            new_dist = current_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                pq.push_or_update(neighbor, new_dist)
    return distances
