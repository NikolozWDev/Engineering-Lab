import java.util.concurrent.*;
import java.util.*;

public class TaskScheduler {
    private final ScheduledExecutorService executor;
    private final Map<String, ScheduledFuture<?>> scheduledTasks;
    
    public TaskScheduler(int threadPoolSize) {
        this.executor = Executors.newScheduledThreadPool(threadPoolSize);
        this.scheduledTasks = new ConcurrentHashMap<>();
    }
    
    public void scheduleTask(String taskId, Runnable task, long delay, TimeUnit timeUnit) {
        ScheduledFuture<?> future = executor.schedule(() -> {
            try {
                task.run();
            } finally {
                scheduledTasks.remove(taskId);
            }
        }, delay, timeUnit);
        
        scheduledTasks.put(taskId, future);
    }
    
    public void scheduleRecurringTask(String taskId, Runnable task, long initialDelay, long period, TimeUnit timeUnit) {
        ScheduledFuture<?> future = executor.scheduleAtFixedRate(() -> {
            try {
                task.run();
            } catch (Exception e) {
                System.err.println("Task " + taskId + " failed: " + e.getMessage());
            }
        }, initialDelay, period, timeUnit);
        
        scheduledTasks.put(taskId, future);
    }
    
    public boolean cancelTask(String taskId) {
        ScheduledFuture<?> future = scheduledTasks.remove(taskId);
        if (future != null) {
            return future.cancel(false);
        }
        return false;
    }
    
    public Set<String> getActiveTasks() {
        return new HashSet<>(scheduledTasks.keySet());
    }
    
    public void shutdown() {
        executor.shutdown();
        try {
            if (!executor.awaitTermination(5, TimeUnit.SECONDS)) {
                executor.shutdownNow();
            }
        } catch (InterruptedException e) {
            executor.shutdownNow();
        }
    }
    
    public static void main(String[] args) {
        TaskScheduler scheduler = new TaskScheduler(4);
        
        scheduler.scheduleTask("one-time-task", () -> {
            System.out.println("One-time task executed");
        }, 2, TimeUnit.SECONDS);
        
        scheduler.scheduleRecurringTask("recurring-task", () -> {
            System.out.println("Recurring task executed at " + System.currentTimeMillis());
        }, 1, 3, TimeUnit.SECONDS);
        
        try {
            Thread.sleep(10000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        
        scheduler.cancelTask("recurring-task");
        scheduler.shutdown();
    }
}
