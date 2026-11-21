def collatz(n):
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps

if __name__ == "__main__":
    best = max(range(1, 10_000), key=collatz)
    print(f"Longest chain under 10k: {best} ({collatz(best)} steps)")
