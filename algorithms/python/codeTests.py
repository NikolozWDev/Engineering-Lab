def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == "__main__":
    test_arr = [64, 34, 25, 12, 22, 11, 90]


import codewars_test as test
from solution import pascals_triangle

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(pascals_triangle(1), [1],"1 level triangle incorrect");
        test.assert_equals(pascals_triangle(2), [1,1,1],"2 level triangle incorrect");
        test.assert_equals(pascals_triangle(3), [1,1,1,1,2,1],"3 level triangle incorrect");
main formula: n! / k!(n - k)!

import codewars_test as test
from solution import solve

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(solve("abba"),"OK")
        test.assert_equals(solve("abbaa"),"remove one")
        test.assert_equals(solve("abbaab"),"not possible")
        test.assert_equals(solve("madmam"),"remove one")
        test.assert_equals(solve("raydarm"),"not possible")
        test.assert_equals(solve("hannah"),"OK")

import codewars
@test.describe("Thanos Sort")
def test_thanos():
    @test.it("Fixed Tests")
    def test_fixed():
        test.assert_equals(thanos_sort([3,1,4,2]),1, f"Failed for arr = {[3,1,4,2]}")
        test.assert_equals(thanos_sort([1,2,3,4]),4, f"Failed for arr = {[1,2,3,4]}")
        test.assert_equals(thanos_sort([4,3,2,1]),1, f"Failed for arr = {[4,3,2,1]}")
        test.assert_equals(thanos_sort([1]),1, f"Failed for arr = {[1]}")
        test.assert_equals(thanos_sort([2,1]),1, f"Failed for arr = {[2,1]}")
        test.assert_equals(thanos_sort([5,5,5,5]),4, f"Failed for arr = {[5,5,5,5]}")
        test.assert_equals(thanos_sort([1,2,3,7,5,6]),3, f"Failed for arr = {[1,2,3,7,5,6]}")
        test.assert_equals(thanos_sort([10,20,30,5,6,7]),3, f"Failed for arr = {[10,20,30,5,6,7]}")

const { assert } = require('chai');

describe("Tests", () => {
  it("test", () => {
    let abc = 'abcdefghijklmnopqrstuvwxyz';
    let c = new AtbashCipher(abc);
    assert.strictEqual(c.encode('abc'), 'zyx');
    assert.strictEqual(c.encode('zyx'), 'abc');
    assert.strictEqual(c.decode('abc'), 'zyx');
    assert.strictEqual(c.decode('zyx'), 'abc');
  });
});


const assert = require('chai').assert;
describe("Basic tests", function(){
  it("should pass basic examples", function() {
    assert.deepEqual(notPrimes(2, 222), [22, 25, 27, 32, 33, 35, 52, 55, 57, 72, 75, 77]);
    assert.deepEqual(notPrimes(2700, 3000), [2722, 2723, 2725, 2727, 2732, 2733, 2735, 2737, 2752, 2755, 2757, 2772, 2773, 2775]);
    assert.deepEqual(notPrimes(500, 999), [522, 525, 527, 532, 533, 535, 537, 552, 553, 555, 572, 573, 575, 722, 723, 725, 732, 735, 737, 752, 753, 755, 772, 775, 777]);
    assert.deepEqual(notPrimes(999, 2500), [2222, 2223, 2225, 2227, 2232, 2233, 2235, 2252, 2253, 2255, 2257, 2272, 2275, 2277, 2322, 2323, 2325, 2327, 2332, 2335, 2337, 2352, 2353, 2355, 2372, 2373, 2375]);
  });
});


@test.describe('Fixed Tests')
def fixed_tests():
    @test.it('Simple Cases')
    def example_cases():
        test.assert_equals(powers(1), [1])
        test.assert_equals(powers(5), [1, 4])
        test.assert_equals(powers(7), [1, 2, 4])
        test.assert_equals(powers(8), [8])
        test.assert_equals(powers(10), [2, 8])

        test.assert_equals(powers(21), [1, 4, 16])
        test.assert_equals(powers(53), [1, 4, 16, 32])
        test.assert_equals(powers(63), [1, 2, 4, 8, 16, 32])
        test.assert_equals(powers(99), [1, 2, 32, 64])
        test.assert_equals(powers(100), [4, 32, 64])
