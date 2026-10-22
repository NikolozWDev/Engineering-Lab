#include <iostream>
#include <vector>
#include <mutex>
#include <condition_variable>
#include <optional>
#include <thread>
#include <chrono>

template<typename T>
class RingBuffer {
private:
    std::vector<T> buffer;
    size_t head = 0;
    size_t tail = 0;
    size_t count = 0;
    size_t capacity;
    std::mutex mtx;
    std::condition_variable not_empty;
    std::condition_variable not_full;
    bool closed = false;

public:
    explicit RingBuffer(size_t cap) : buffer(cap), capacity(cap) {}

    bool push(const T& item) {
        std::unique_lock<std::mutex> lock(mtx);
        not_full.wait(lock, [this] { return count < capacity || closed; });
        if (closed) return false;

        buffer[tail] = item;
        tail = (tail + 1) % capacity;
        ++count;
        not_empty.notify_one();
        return true;
    }

    std::optional<T> pop() {
        std::unique_lock<std::mutex> lock(mtx);
        not_empty.wait(lock, [this] { return count > 0 || closed; });
        if (count == 0) return std::nullopt;

        T item = buffer[head];
        head = (head + 1) % capacity;
        --count;
        not_full.notify_one();
        return item;
    }

    void close() {
        std::lock_guard<std::mutex> lock(mtx);
        closed = true;
        not_empty.notify_all();
        not_full.notify_all();
    }

    size_t size() const {
        std::lock_guard<std::mutex> lock(const_cast<std::mutex&>(mtx));
        return count;
    }

    bool empty() const { return size() == 0; }
    bool full() const { return size() == capacity; }
};

int main() {
    RingBuffer<int> rb(4);

    std::thread producer([&rb] {
        for (int i = 0; i < 8; ++i) {
            rb.push(i);
            std::cout << "push: " << i << "\n";
            std::this_thread::sleep_for(std::chrono::milliseconds(50));
        }
        rb.close();
    });

    std::thread consumer([&rb] {
        while (auto item = rb.pop()) {
            std::cout << "pop: " << *item << "\n";
            std::this_thread::sleep_for(std::chrono::milliseconds(80));
        }
    });

    producer.join();
    consumer.join();
    return 0;
}
