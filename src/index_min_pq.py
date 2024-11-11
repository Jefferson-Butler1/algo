class IndexMinPQ:
    def __init__(self):
        self._heap = [[None, None]]
        self._key_to_index = {}
    
    def is_empty(self):
        return len(self._heap) == 1
    
    def enqueue(self, key, priority):
        if key in self._key_to_index:
            raise ValueError(f"Key {key} already exists in the queue")
        
        self._heap.append([priority, key])
        current_index = len(self._heap) - 1
        self._key_to_index[key] = current_index
        
        self._swim(current_index)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        
        min_key = self._heap[1][1]
        
        self._swap(1, len(self._heap) - 1)
        self._heap.pop()
        del self._key_to_index[min_key]
        
        if not self.is_empty():
            self._sink(1)
            
        return min_key
    
    def reduce_priority(self, key, new_priority):
        if key not in self._key_to_index:
            raise KeyError(f"Key {key} not found in queue")
            
        index = self._key_to_index[key]
        old_priority = self._heap[index][0]
        
        if new_priority >= old_priority:
            raise ValueError("New priority must be less than current priority")
            
        self._heap[index][0] = new_priority
        self._swim(index)
    
    def _swim(self, index):
        while index > 1 and self._greater(index // 2, index):
            self._swap(index, index // 2)
            index = index // 2
    
    def _sink(self, index):
        heap_size = len(self._heap) - 1
        while 2 * index <= heap_size:
            j = 2 * index
            
            if j < heap_size and self._greater(j, j + 1):
                j += 1
                
            if not self._greater(index, j):
                break
                
            self._swap(index, j)
            index = j
    
    def _greater(self, i, j):
        return self._heap[i][0] > self._heap[j][0]
    
    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
        self._key_to_index[self._heap[i][1]] = i
        self._key_to_index[self._heap[j][1]] = j
