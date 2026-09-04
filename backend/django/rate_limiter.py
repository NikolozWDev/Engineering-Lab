import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, max_requests, window_seconds):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(list)
    
    def allow_request(self, client_id):
        now = time.time()
        window_start = now - self.window_seconds
        
        self.requests[client_id] = [
            timestamp for timestamp in self.requests[client_id]
            if timestamp > window_start
        ]
        
        if len(self.requests[client_id]) < self.max_requests:
            self.requests[client_id].append(now)
            return True
        
        return False
    
    def get_remaining_requests(self, client_id):
        now = time.time()
        window_start = now - self.window_seconds
        
        recent_requests = [
            timestamp for timestamp in self.requests[client_id]
            if timestamp > window_start
        ]
        
        return max(0, self.max_requests - len(recent_requests))
    
    def reset_client(self, client_id):
        self.requests[client_id] = []
    
    def cleanup(self):
        now = time.time()
        window_start = now - self.window_seconds
        
        for client_id in list(self.requests.keys()):
            self.requests[client_id] = [
                timestamp for timestamp in self.requests[client_id]
                if timestamp > window_start
            ]
            
            if not self.requests[client_id]:
                del self.requests[client_id]

if __name__ == "__main__":
    limiter = RateLimiter(max_requests=3, window_seconds=10)
