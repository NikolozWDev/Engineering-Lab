import java.util.concurrent.atomic.AtomicInteger;
import java.util.function.Supplier;

public class CircuitBreaker {
    public enum State { CLOSED, OPEN, HALF_OPEN }

    private final int failureThreshold;
    private final long openTimeoutMs;
    private final AtomicInteger failures = new AtomicInteger(0);
    private volatile State state = State.CLOSED;
    private volatile long openedAt = 0;

    public CircuitBreaker(int failureThreshold, long openTimeoutMs) {
        this.failureThreshold = failureThreshold;
        this.openTimeoutMs = openTimeoutMs;
    }

    public <T> T call(Supplier<T> action) {
        if (state == State.OPEN) {
            if (System.currentTimeMillis() - openedAt >= openTimeoutMs) {
                state = State.HALF_OPEN;
            } else {
                throw new IllegalStateException("Circuit is open");
            }
        }

        try {
            T result = action.get();
            reset();
            return result;
        } catch (RuntimeException e) {
            recordFailure();
            throw e;
        }
    }

    private void recordFailure() {
        if (state == State.HALF_OPEN) {
            trip();
            return;
        }

        if (failures.incrementAndGet() >= failureThreshold) {
            trip();
        }
    }

    private void trip() {
        state = State.OPEN;
        openedAt = System.currentTimeMillis();
    }

    private void reset() {
        failures.set(0);
        state = State.CLOSED;
    }

    public State getState() {
        return state;
    }

    public static void main(String[] args) throws InterruptedException {
        CircuitBreaker cb = new CircuitBreaker(2, 500);

        Supplier<String> flaky = () -> {
            if (Math.random() < 0.8) {
                throw new RuntimeException("service down");
            }
            return "ok";
        };

        for (int i = 0; i < 5; i++) {
            try {
                System.out.println("call " + i + ": " + cb.call(flaky));
            } catch (RuntimeException e) {
                System.out.println("call " + i + " failed: " + e.getMessage() + " | state: " + cb.getState());
            }
        }

        Thread.sleep(600);
        try {
            System.out.println("after wait: " + cb.call(() -> "recovered"));
        } catch (RuntimeException e) {
            System.out.println("still failing: " + e.getMessage());
        }
        System.out.println("final state: " + cb.getState());
    }
}
