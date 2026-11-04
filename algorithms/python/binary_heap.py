class BinaryHeap:
    def __init__(self, max_heap=True):
        self.heap = []
        self.max_heap = max_heap

    def _compare(self, a, b):
        return a > b if self.max_heap else a < b

    def push(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise IndexError("heap is empty")
        top = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._sift_down(0)
        return top

    def peek(self):
        if not self.heap:
            raise IndexError("heap is empty")
        return self.heap[0]

    def _sift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self._compare(self.heap[idx], self.heap[parent]):
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                break

    def _sift_down(self, idx):
        n = len(self.heap)
        while True:
            best = idx
            left = 2 * idx + 1
            right = 2 * idx + 2
            if left < n and self._compare(self.heap[left], self.heap[best]):
                best = left
            if right < n and self._compare(self.heap[right], self.heap[best]):
                best = right
            if best == idx:
                break
            self.heap[idx], self.heap[best] = self.heap[best], self.heap[idx]
            idx = best

    def __len__(self):
        return len(self.heap)

if __name__ == "__main__":
    max_h = BinaryHeap(max_heap=True)
    for x in [5, 3, 8, 1, 9, 2]:
        max_h.push(x)
    print([max_h.pop() for _ in range(len(max_h))])

    min_h = BinaryHeap(max_heap=False)
    for x in [5, 3, 8, 1, 9, 2]:
        min_h.push(x)
    print([min_h.pop() for _ in range(len(min_h))])
