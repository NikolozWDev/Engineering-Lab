import math
import random

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + math.exp(-x))
def sigmoid_derivative(x):
    return x * (1 - x)

# Training data for XOR
inputs = [[0,0], [0,1], [1,0], [1,1]]
expected = [0, 1, 1, 0]

# Initialize weights randomly
w1 = [random.uniform(-1, 1) for _ in range(2)]
w2 = [random.uniform(-1, 1) for _ in range(2)]

learning_rate = 0.5
for epoch in range(10000):
    for inp, target in zip(inputs, expected):
        # Forward pass
        z1 = sum(w * i for w, i in zip(w1, inp))
        a1 = sigmoid(z1)
        z2 = sum(w * a1 for w in w2)
        a2 = sigmoid(z2)

        # Calculate error


def is_palindrome(s):
    # Remove spaces and convert to lowercase for a case-insensitive check
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage:
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")

import uuid

def generate_crypto_uuid():
    # Generate a random UUID (version 4)
    crypto_uuid = uuid.uuid4()
    return str(crypto_uuid)

# Example usage
if __name__ == "__main__":
    print("Crypto UUID:", generate_crypto_uuid())


# Title: Asynchronous Web Scraper with Concurrency Control

import asyncio
import aiohttp
from aiohttp import ClientSession
from bs4 import BeautifulSoup
import async_timeout

class AsyncWebScraper:
    def __init__(self, urls, max_concurrent_tasks=5):
        self.urls = urls
        self.semaphore = asyncio.Semaphore(max_concurrent_tasks)
        self.results = {}

    async def fetch(self, session: ClientSession, url: str):
        async with self.semaphore:
            try:
                with async_timeout.timeout(10):
                    async with session.get(url) as response:
                        response.raise_for_status()
                        html = await response.text()
                        return html
            except Exception as e:
                print(f"Error fetching {url}: {e}")
                return None

    async def parse(self, html: str, url: str):
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.title.string if soup.title else 'No Title'
            self.results[url] = title

    async def scrape_url(self, session: ClientSession, url: str):
        html = await self.fetch(session, url)
        await self.parse(html, url)

    async def run(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.scrape_url(session, url) for url in self.urls]
            await asyncio.gather(*tasks)

    def get_results(self):
        return self.results

# Usage Example
if __name__ == "__main__":
    urls = [
        'https://www.python.org/',
        'https://www.asyncio.org/',
        'https://www.aiohttp.org/',
        'https://www.wikipedia.org/',
        'https://www.github.com/'
    ]

    scraper = AsyncWebScraper(urls, max_concurrent_tasks=3)
    asyncio.run(scraper.run())
    results = scraper.get_results()
    for url, title in results.items():
        print(f"{url} -> {title}")

def seq_to_one(n):
    if n >= 1:
        return list(range(n, 0, -1))
    else:
        return list(range(n, 2))

def delete_nth(order,max_e):
    result = []
    count_item = {}
    for i in order:
        if count_item.get(i, 0) < max_e:
            result.append(i)
            count_item[i] = count_item.get(i, 0) + 1
    return result

def parts_sums(ls):
    total = sum(ls)
    result = [total]
    for num in ls:
        total -= num
        result.append(total)
    return result

def delete_nth(order,max_e):
    result = []
    count_item = {}
    for i in order:
        if count_item.get(i, 0) < max_e:
            result.append(i)
            count_item[i] = count_item.get(i, 0) + 1
    return result

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(how_much_coffee([]), 0)
        test.assert_equals(how_much_coffee(['cw']), 1)
        test.assert_equals(how_much_coffee(['CW']), 2)
        test.assert_equals(how_much_coffee(['cw','CAT']), 3)
        test.assert_equals(how_much_coffee(['cw','CAT','DOG']), 'You need extra sleep')
        test.assert_equals(how_much_coffee(['cw','CAT', 'cw=others']), 3)

# optimize
def find_x(n):
    x = 0
    for i in range(n):
        for j in range(2*n):
            x += i+j
    return x
