import java.util.concurrent.*;
import java.util.*;

public class ProcessManager {
    private final ExecutorService executorService;
    private final Map<String, Process> processes;
    private final ScheduledExecutorService monitorExecutor;
    
    public ProcessManager(int poolSize) {
        this.executorService = Executors.newFixedThreadPool(poolSize);
        this.processes = new ConcurrentHashMap<>();
        this.monitorExecutor = Executors.newSingleThreadScheduledExecutor();
        startMonitoring();
    }
    
    public String startProcess(String name, Runnable task) {
        String processId = name + "_" + System.currentTimeMillis();
        
        Process process = new Process(processId, name);
        processes.put(processId, process);
        
        executorService.submit(() -> {
            process.setStatus("RUNNING");
            process.setStartTime(System.currentTimeMillis());
            
            try {
                task.run();
                process.setStatus("COMPLETED");
            } catch (Exception e) {
                process.setStatus("FAILED");
                process.setError(e.getMessage());
            } finally {
                process.setEndTime(System.currentTimeMillis());
            }
        });
        
        return processId;
    }
    
    public void stopProcess(String processId) {
        Process process = processes.get(processId);
        if (process != null && process.getStatus().equals("RUNNING")) {
            process.setStatus("STOPPED");
            process.setEndTime(System.currentTimeMillis());
        }
    }
    
    public Process getProcess(String processId) {
        return processes.get(processId);
    }
    
    public List<Process> getAllProcesses() {
        return new ArrayList<>(processes.values());
    }
    
    public List<Process> getProcessesByStatus(String status) {
        List<Process> result = new ArrayList<>();
        for (Process process : processes.values()) {
            if (process.getStatus().equals(status)) {
                result.add(process);
            }
        }
        return result;
    }
    
    private void startMonitoring() {
        monitorExecutor.scheduleAtFixedRate(() -> {
            for (Process process : processes.values()) {
                if (process.getStatus().equals("RUNNING")) {
                    long runningTime = System.currentTimeMillis() - process.getStartTime();
                    process.setRunningTime(runningTime);
                }
            }
        }, 1, 1, TimeUnit.SECONDS);
    }
    
    public void shutdown() {
        executorService.shutdown();
        monitorExecutor.shutdown();
        try {
            if (!executorService.awaitTermination(5, TimeUnit.SECONDS)) {
                executorService.shutdownNow();
            }
        } catch (InterruptedException e) {
            executorService.shutdownNow();
        }
    }
    
    public static class Process {
        private final String id;
        private final String name;
        private String status;
        private long startTime;
        private long endTime;
        private long runningTime;
        private String error;
        
        public Process(String id, String name) {
            this.id = id;
            this.name = name;
            this.status = "PENDING";
        }
        
        public String getId() { return id; }
        public String getName() { return name; }
        public String getStatus() { return status; }
        public void setStatus(String status) { this.status = status; }
        public long getStartTime() { return startTime; }
        public void setStartTime(long startTime) { this.startTime = startTime; }
        public long getEndTime() { return endTime; }
        public void setEndTime(long endTime) { this.endTime = endTime; }
        public long getRunningTime() { return runningTime; }
        public void setRunningTime(long runningTime) { this.runningTime = runningTime; }
        public String getError() { return error; }
        public void setError(String error) { this.error = error; }
        
        @Override
        public String toString() {
            return String.format("Process{id='%s', name='%s', status='%s', runningTime=%dms}", 
                id, name, status, runningTime);
        }
    }
    
    public static void main(String[] args) {
        ProcessManager manager = new ProcessManager(4);
        
        manager.startProcess("data-processor", () -> {
            try {
                Thread.sleep(3000);
                System.out.println("Data processing completed");
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });
        
        manager.startProcess("file-watcher", () -> {
            try {
                Thread.sleep(5000);
                System.out.println("File watching completed");
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });
        
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        
        for (Process process : manager.getAllProcesses()) {
            System.out.println(process);
        }
        
        manager.shutdown();
    }
}
