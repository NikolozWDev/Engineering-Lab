class MemoryPool:
    def __init__(self, block_size, num_blocks):
        self.block_size = block_size
        self.num_blocks = num_blocks
        self.pool = [bytearray(block_size) for _ in range(num_blocks)]
        self.free_blocks = list(range(num_blocks))
        self.used_blocks = {}
    
    def allocate(self):
        if not self.free_blocks:
            raise MemoryError("Pool exhausted")
        
        block_id = self.free_blocks.pop()
        self.used_blocks[block_id] = self.pool[block_id]
        return block_id
    
    def free(self, block_id):
        if block_id in self.used_blocks:
            self.free_blocks.append(block_id)
            del self.used_blocks[block_id]
            return True
        return False
    
    def write(self, block_id, data):
        if block_id not in self.used_blocks:
            return False
        
        block = self.pool[block_id]
        if len(data) > self.block_size:
            return False
        
        block[:len(data)] = data
        return True
    
    def read(self, block_id):
        if block_id not in self.used_blocks:
            return None
        return bytes(self.pool[block_id])
    
    def available_blocks(self):
        return len(self.free_blocks)
    
    def used_block_count(self):
        return len(self.used_blocks)

if __name__ == "__main__":
    pool = MemoryPool(64, 4)
