class LRU {
  constructor(cap = 3) { this.cap = cap; this.map = new Map(); }
  get(k) {
    if (!this.map.has(k)) return undefined;
    const v = this.map.get(k);
    this.map.delete(k); this.map.set(k, v);
    return v;
  }
  set(k, v) {
    if (this.map.has(k)) this.map.delete(k);
    this.map.set(k, v);
    if (this.map.size > this.cap) this.map.delete(this.map.keys().next().value);
  }
}

const c = new LRU(2);
c.set("a", 1); c.set("b", 2); c.set("c", 3);
console.log([...c.map.keys()]); // ['b', 'c']
