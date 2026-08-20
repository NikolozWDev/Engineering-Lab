class Timer {
    constructor() {
        this.timers = new Map();
        this.intervals = new Map();
    }

    setTimeout(callback, delay, ...args) {
        const id = `timeout_${Date.now()}_${Math.random()}`;
        const timeoutId = setTimeout(() => {
            callback(...args);
            this.timers.delete(id);
        }, delay);
        
        this.timers.set(id, timeoutId);
        return id;
    }

    setInterval(callback, interval, ...args) {
        const id = `interval_${Date.now()}_${Math.random()}`;
        const intervalId = setInterval(callback, interval, ...args);
        
        this.intervals.set(id, intervalId);
        return id;
    }

    clearTimeout(id) {
        const timeoutId = this.timers.get(id);
        if (timeoutId) {
            clearTimeout(timeoutId);
            this.timers.delete(id);
            return true;
        }
        return false;
    }

    clearInterval(id) {
        const intervalId = this.intervals.get(id);
        if (intervalId) {
            clearInterval(intervalId);
            this.intervals.delete(id);
            return true;
        }
        return false;
    }

    clearAll() {
        this.timers.forEach(timeoutId => clearTimeout(timeoutId));
        this.intervals.forEach(intervalId => clearInterval(intervalId));
        this.timers.clear();
        this.intervals.clear();
    }

    getActiveTimers() {
        return {
            timeouts: this.timers.size,
            intervals: this.intervals.size
        };
    }
}

class Debouncer {
    constructor(delay = 300) {
        this.delay = delay;
        this.timeoutId = null;
    }

    debounce(callback) {
        if (this.timeoutId) {
            clearTimeout(this.timeoutId);
        }
        
        this.timeoutId = setTimeout(() => {
            callback();
            this.timeoutId = null;
        }, this.delay);
    }

    cancel() {
        if (this.timeoutId) {
            clearTimeout(this.timeoutId);
            this.timeoutId = null;
        }
    }
}

class Throttler {
    constructor(limit = 300) {
        this.limit = limit;
        this.lastCall = 0;
        this.timeoutId = null;
    }

    throttle(callback) {
        const now = Date.now();
        const timeSinceLastCall = now - this.lastCall;
        
        if (timeSinceLastCall >= this.limit) {
            this.lastCall = now;
            callback();
        } else if (!this.timeoutId) {
            this.timeoutId = setTimeout(() => {
                this.lastCall = Date.now();
                this.timeoutId = null;
                callback();
            }, this.limit - timeSinceLastCall);
        }
    }

    cancel() {
        if (this.timeoutId) {
            clearTimeout(this.timeoutId);
            this.timeoutId = null;
        }
    }
}

const timer = new Timer();
const timeoutId = timer.setTimeout(() => console.log("Timeout executed"), 1000);
const intervalId = timer.setInterval(() => console.log("Interval tick"), 2000);

setTimeout(() => {
    timer.clearInterval(intervalId);
    timer.clearAll();
    console.log("All timers cleared:", timer.getActiveTimers());
}, 5000);

const debouncer = new Debouncer(500);
debouncer.debounce(() => console.log("Debounced execution"));
