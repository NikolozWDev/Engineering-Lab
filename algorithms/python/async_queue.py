import asyncio
from collections import deque

class AsyncQueue:
    def __init__(self, max_size=10):
        self.queue = deque()
        self.max_size = max_size
        self.not_empty = asyncio.Condition()
        self.not_full = asyncio.Condition()
    
    async def put(self, item):
        async with self.not_full:
            while len(self.queue) >= self.max_size:
                await self.not_full.wait()
            self.queue.append(item)
            
            async with self.not_empty:
                self.not_empty.notify()
    
    async def get(self):
        async with self.not_empty:
            while not self.queue:
                await self.not_empty.wait()
            item = self.queue.popleft()
            
            async with self.not_full:
                self.not_full.notify()
            
            return item
    
    def size(self):
        return len(self.queue)
    
    def empty(self):
        return len(self.queue) == 0
    
    def full(self):
        return len(self.queue) >= self.max_size

async def producer(queue, producer_id):
    for i in range(5):
        await queue.put(f"producer_{producer_id}_item_{i}")
        print(f"Producer {producer_id} added item {i}")
        await asyncio.sleep(0.1)

async def consumer(queue, consumer_id):
    for _ in range(10):
        item = await queue.get()
        print(f"Consumer {consumer_id} got: {item}")
        await asyncio.sleep(0.2)

async def main():
    queue = AsyncQueue(max_size=5)
    
    producers = [producer(queue, i) for i in range(2)]
    consumers = [consumer(queue, i) for i in range(2)]
    
    await asyncio.gather(*producers, *consumers)

if __name__ == "__main__":
    asyncio.run(main())
