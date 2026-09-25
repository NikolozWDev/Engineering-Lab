import threading
import time
import uuid
from collections import deque
from enum import Enum

class JobStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    DONE = "done"
    FAILED = "failed"

class Job:
    def __init__(self, func, args=None, kwargs=None, priority=0):
        self.id = str(uuid.uuid4())[:8]
        self.func = func
        self.args = args or ()
        self.kwargs = kwargs or {}
        self.priority = priority
        self.status = JobStatus.PENDING
        self.result = None
        self.error = None
        self.created_at = time.time()
        self.started_at = None
        self.finished_at = None

class JobQueue:
    def __init__(self, workers=2):
        self.queue = deque()
        self.jobs = {}
        self.lock = threading.Lock()
        self.workers = workers
        self.running = False
        self.threads = []

    def submit(self, func, args=None, kwargs=None, priority=0):
        job = Job(func, args, kwargs, priority)
        with self.lock:
            self.jobs[job.id] = job
            if priority > 0:
                self.queue.appendleft(job)
            else:
                self.queue.append(job)
        return job.id

    def _worker(self):
        while self.running:
            job = None
            with self.lock:
                if self.queue:
                    job = self.queue.popleft()
            
            if not job:
                time.sleep(0.05)
                continue
            
            job.status = JobStatus.RUNNING
            job.started_at = time.time()
            
            try:
                job.result = job.func(*job.args, **job.kwargs)
                job.status = JobStatus.DONE
            except Exception as e:
                job.error = str(e)
                job.status = JobStatus.FAILED
            finally:
                job.finished_at = time.time()

    def start(self):
        if self.running:
            return
        self.running = True
        for _ in range(self.workers):
            t = threading.Thread(target=self._worker, daemon=True)
            t.start()
            self.threads.append(t)

    def stop(self, timeout=5):
        self.running = False
        for t in self.threads:
            t.join(timeout=timeout)
        self.threads.clear()

    def get(self, job_id):
        return self.jobs.get(job_id)

    def wait(self, job_id, timeout=None):
        deadline = time.time() + timeout if timeout else None
        while True:
            job = self.jobs.get(job_id)
            if not job:
                return None
            if job.status in (JobStatus.DONE, JobStatus.FAILED):
                return job
            if deadline and time.time() > deadline:
                return job
            time.sleep(0.02)

    def stats(self):
        counts = {s: 0 for s in JobStatus}
        for job in self.jobs.values():
            counts[job.status] += 1
        return {
            "total": len(self.jobs),
            "queued": len(self.queue),
            **{s.value: counts[s] for s in JobStatus}
        }

if __name__ == "__main__":
    q = JobQueue(workers=3)
    q.start()

    def slow_add(a, b):
        time.sleep(0.3)
        return a + b

    def fail():
        raise ValueError("nope")

    ids = [q.submit(slow_add, (i, i * 2)) for i in range(5)]
    ids.append(q.submit(fail))

    for jid in ids:
        job = q.wait(jid, timeout=3)
        print(job.id, job.status.value, job.result, job.error)
