#include <atomic>
#include <thread>
#include <iostream>
#include <vector>

class SpinLock {
private:
    std::atomic_flag flag = ATOMIC_FLAG_INIT;

public:
    void lock() {
        while (flag.test_and_set(std::memory_order_acquire)) {
            while (flag.test(std::memory_order_relaxed)) {
                std::this_thread::yield();
            }
        }
    }

    void unlock() {
        flag.clear(std::memory_order_release);
    }

    bool try_lock() {
        return !flag.test_and_set(std::memory_order_acquire);
    }
};

class ScopedSpinLock {
private:
    SpinLock& lock_;

public:
    explicit ScopedSpinLock(SpinLock& lock) : lock_(lock) {
        lock_.lock();
    }

    ~ScopedSpinLock() {
        lock_.unlock();
    }

    ScopedSpinLock(const ScopedSpinLock&) = delete;
    ScopedSpinLock& operator=(const ScopedSpinLock&) = delete;
};

int main() {
    SpinLock lock;
    long counter = 0;
    const int iterations = 100000;

    auto worker = [&] {
        for (int i = 0; i < iterations; ++i) {
            ScopedSpinLock guard(lock);
            ++counter;
        }
    };

    std::vector<std::thread> threads;
    for (int i = 0; i < 4; ++i) {
        threads.emplace_back(worker);
    }

    for (auto& t : threads) {
        t.join();
    }

    std::cout << "counter: " << counter << "\n";
    std::cout << "expected: " << (iterations * 4) << "\n";

    return 0;
}
