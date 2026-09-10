class StorageManager {
    constructor(storageType = 'localStorage', prefix = '') {
        this.storage = storageType === 'session' ? sessionStorage : localStorage;
        this.prefix = prefix;
    }

    key(name) {
        return this.prefix ? `${this.prefix}:${name}` : name;
    }

    set(name, value, ttl = null) {
        const item = {
            value: value,
            expires: ttl ? Date.now() + ttl * 1000 : null
        };
        this.storage.setItem(this.key(name), JSON.stringify(item));
    }

    get(name, fallback = null) {
        const raw = this.storage.getItem(this.key(name));
        if (!raw) return fallback;

        try {
            const item = JSON.parse(raw);
            
            if (item.expires && Date.now() > item.expires) {
                this.remove(name);
                return fallback;
            }
            
            return item.value;
        } catch (e) {
            return fallback;
        }
    }

    has(name) {
        return this.get(name, undefined) !== undefined;
    }

    remove(name) {
        this.storage.removeItem(this.key(name));
    }

    clear() {
        if (!this.prefix) {
            this.storage.clear();
            return;
        }
        
        const keysToRemove = [];
        for (let i = 0; i < this.storage.length; i++) {
            const key = this.storage.key(i);
            if (key.startsWith(`${this.prefix}:`)) {
                keysToRemove.push(key);
            }
        }
        
        keysToRemove.forEach(key => this.storage.removeItem(key));
    }

    keys() {
        const result = [];
        const prefix = this.prefix ? `${this.prefix}:` : '';
        
        for (let i = 0; i < this.storage.length; i++) {
            const key = this.storage.key(i);
            if (!prefix || key.startsWith(prefix)) {
                result.push(prefix ? key.slice(prefix.length) : key);
            }
        }
        
        return result;
    }

    size() {
        return this.keys().length;
    }
}
