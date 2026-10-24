import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.TimeUnit;
import java.util.function.Supplier;

public class ObjectPool<T> implements AutoCloseable {
    private final BlockingQueue<T> pool;
    private final Supplier<T> factory;
    private final int capacity;
    private volatile boolean closed = false;

    public ObjectPool(int capacity, Supplier<T> factory) {
        this.capacity = capacity;
        this.factory = factory;
        this.pool = new LinkedBlockingQueue<>(capacity);

        for (int i = 0; i < capacity; i++) {
            pool.offer(factory.get());
        }
    }

    public T acquire() throws InterruptedException {
        if (closed) {
            throw new IllegalStateException("Pool is closed");
        }
        return pool.take();
    }

    public T acquire(long timeout, TimeUnit unit) throws InterruptedException {
        if (closed) {
            throw new IllegalStateException("Pool is closed");
        }
        T obj = pool.poll(timeout, unit);
        if (obj == null) {
            throw new IllegalStateException("No object available within timeout");
        }
        return obj;
    }

    public void release(T obj) {
        if (obj == null || closed) return;
        pool.offer(obj);
    }

    public int available() {
        return pool.size();
    }

    public int inUse() {
        return capacity - pool.size();
    }

    @Override
    public void close() {
        closed = true;
        pool.clear();
    }

    public static void main(String[] args) throws Exception {
        ObjectPool<StringBuilder> pool = new ObjectPool<>(3, StringBuilder::new);

        StringBuilder sb = pool.acquire();
        sb.append("hello");
        System.out.println("acquired: " + sb + " | in use: " + pool.inUse());
        pool.release(sb);

        System.out.println("available: " + pool.available());

        StringBuilder a = pool.acquire();
        StringBuilder b = pool.acquire();
        StringBuilder c = pool.acquire();

        try {
            pool.acquire(100, TimeUnit.MILLISECONDS);
        } catch (IllegalStateException e) {
            System.out.println("expected: " + e.getMessage());
        }

        pool.release(a);
        pool.release(b);
        pool.release(c);
        pool.close();
    }
}
