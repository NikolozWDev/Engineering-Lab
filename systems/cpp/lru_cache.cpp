#include <iostream>
#include <unordered_map>
#include <list>
#include <optional>
#include <string>

template<typename K, typename V>
class LRUCache {
private:
    size_t capacity;
    std::list<std::pair<K, V>> items;
    std::unordered_map<K, typename std::list<std::pair<K, V>>::iterator> index;

public:
    explicit LRUCache(size_t cap) : capacity(cap) {}

    void put(const K& key, const V& value) {
        auto it = index.find(key);
        if (it != index.end()) {
            it->second->second = value;
            items.splice(items.begin(), items, it->second);
            return;
        }

        if (items.size() >= capacity) {
            auto last = items.back();
            index.erase(last.first);
            items.pop_back();
        }

        items.emplace_front(key, value);
        index[key] = items.begin();
    }

    std::optional<V> get(const K& key) {
        auto it = index.find(key);
        if (it == index.end()) {
            return std::nullopt;
        }
        items.splice(items.begin(), items, it->second);
        return it->second->second;
    }

    bool contains(const K& key) const {
        return index.find(key) != index.end();
    }

    void remove(const K& key) {
        auto it = index.find(key);
        if (it == index.end()) return;
        items.erase(it->second);
        index.erase(it);
    }

    size_t size() const { return items.size(); }

    std::vector<K> keys() const {
        std::vector<K> result;
        for (const auto& p : items) result.push_back(p.first);
        return result;
    }

    void clear() {
        items.clear();
        index.clear();
    }
};

int main() {
    LRUCache<std::string, int> cache(3);

    cache.put("a", 1);
    cache.put("b", 2);
    cache.put("c", 3);
    cache.get("a");
    cache.put("d", 4);

    for (const auto& k : cache.keys()) {
        std::cout << k << " ";
    }
    std::cout << "\n";

    auto val = cache.get("b");
    std::cout << "b: " << (val ? std::to_string(*val) : "miss") << "\n";

    cache.remove("c");
    std::cout << "size: " << cache.size() << "\n";

    return 0;
}
