class PubSub {
    constructor() {
        this.topics = new Map();
    }

    sub(topic, handler) {
        if (!this.topics.has(topic)) {
            this.topics.set(topic, new Set());
        }
        this.topics.get(topic).add(handler);
        return () => this.unsub(topic, handler);
    }

    unsub(topic, handler) {
        const handlers = this.topics.get(topic);
        if (!handlers) return false;
        const removed = handlers.delete(handler);
        if (handlers.size === 0) this.topics.delete(topic);
        return removed;
    }

    pub(topic, payload) {
        const handlers = this.topics.get(topic);
        if (!handlers) return 0;
        let count = 0;
        for (const handler of [...handlers]) {
            try {
                handler(payload);
                count++;
            } catch (e) {
                console.error(`pubsub error on "${topic}":`, e.message);
            }
        }
        return count;
    }

    topics_list() {
        return [...this.topics.keys()];
    }
}

const bus = new PubSub();

const off = bus.sub("order:created", order => {
    console.log("new order:", order.id);
});

bus.sub("order:created", order => {
    console.log("notify email:", order.email);
});

bus.pub("order:created", { id: 42, email: "a@b.com" });
console.log("topics:", bus.topics_list());

off();
console.log("after unsub:", bus.pub("order:created", { id: 43, email: "c@d.com" }));
