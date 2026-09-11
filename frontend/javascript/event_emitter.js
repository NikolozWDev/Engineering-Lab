class EventEmitter {
    constructor() {
        this.events = new Map();
    }

    on(event, listener) {
        if (!this.events.has(event)) {
            this.events.set(event, []);
        }
        this.events.get(event).push(listener);
        return () => this.off(event, listener);
    }

    once(event, listener) {
        const wrapper = (...args) => {
            this.off(event, wrapper);
            listener(...args);
        };
        return this.on(event, wrapper);
    }

    off(event, listener) {
        if (!this.events.has(event)) return false;
        
        const listeners = this.events.get(event);
        const index = listeners.indexOf(listener);
        
        if (index === -1) return false;
        
        listeners.splice(index, 1);
        
        if (listeners.length === 0) {
            this.events.delete(event);
        }
        
        return true;
    }

    emit(event, ...args) {
        if (!this.events.has(event)) return 0;
        
        const listeners = [...this.events.get(event)];
        
        for (const listener of listeners) {
            try {
                listener(...args);
            } catch (e) {
                console.error(`Error in listener for "${event}":`, e);
            }
        }
        
        return listeners.length;
    }

    listenerCount(event) {
        return this.events.has(event) ? this.events.get(event).length : 0;
    }

    eventNames() {
        return [...this.events.keys()];
    }

    removeAllListeners(event = null) {
        if (event) {
            this.events.delete(event);
        } else {
            this.events.clear();
        }
    }
}

const emitter = new EventEmitter();

const unsubscribe = emitter.on('user:login', user => {
    console.log(`Welcome ${user.name}`);
});

emitter.once('user:login', user => {
    console.log(`First login for ${user.name}`);
});

emitter.on('user:logout', user => {
    console.log(`Goodbye ${user.name}`);
});
