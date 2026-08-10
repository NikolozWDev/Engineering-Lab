import random

class QuantumCryptographer:
    def __init__(self, key_length):
        self.key = [random.randint(0, 1) for _ in range(key_length)]
        self.state = []

    def encode(self, message):
        encoded = []
        for i, bit in enumerate(message):
            key_bit = self.key[i % len(self.key)]
            encoded_bit = bit ^ key_bit
            self.state.append(encoded_bit)
            encoded.append(encoded_bit)
        return encoded

    def decode(self, encoded_message):
        decoded = []
        for i, bit in enumerate(encoded_message):
            key_bit = self.key[i % len(self.key)]
            decoded_bit = bit ^ key_bit
            decoded.append(decoded_bit)
        return decoded

    def mutate_key(self):
        index = random.randint(0, len(self.key) - 1)
        self.key[index] ^= 1

    def get_state(self):
        return self.state

    def __str__(self):
        return f"Key: {self.key}"


def solution(number):
    if number < 0:
        return 0
    list_numbers = []
    result_numbers = []
    for i in range(number):
        list_numbers.append(i)
    j = 0
    while j < len(list_numbers):
        if j >= len(list_numbers):
            break
        if list_numbers[j] % 3 == 0 or list_numbers[j] % 5 == 0:
            result_numbers.append(list_numbers[j])
        j += 1
    return sum(result_numbers)

import math
import datetime

class AdvancedCalculator:
    def __init__(self, values):
        self.values = values
        self.history = []

    def add_value(self, value):
        self.values.append(value)
        self.history.append(('add', value))

    def remove_value(self, value):
        if value in self.values:
            self.values.remove(value)
            self.history.append(('remove', value))

    def sum(self):
        total = sum(self.values)
        self.history.append(('sum', total))
        return total

    def product(self):
        result = 1
        for v in self.values:
            result *= v
        self.history.append(('product', result))
        return result

    def mean(self):
        if not self.values:
            return None
        mean_value = self.sum() / len(self.values)
        self.history.append(('mean', mean_value))
        return mean_value

    def median(self):
        sorted_vals = sorted(self.values)
        n = len(sorted_vals)
        if n == 0:
            return None
        mid = n // 2
        if n % 2 == 0:
            median_value = (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
        else:
            median_value = sorted_vals[mid]
        self.history.append(('median', median_value))
        return median_value

    def variance(self):
        if len(self.values) < 2:
            return None
        mean_value = self.mean()
        var = sum((x - mean_value) ** 2 for x in self.values) / (len(self.values) - 1)
        self.history.append(('variance', var))
        return var

    def std_dev(self):
        var = self.variance()
        if var is None:
            return None
        std = math.sqrt(var)
        self.history.append(('std_dev', std))
        return std

    def reset(self):
        self.values.clear()
        self.history.clear()

    def get_history(self):
        return self.history

    def current_time(self):
        return datetime.datetime.now()

    def __str__(self):
        return f"Values: {self.values}"

import codewars_test as test
from solution import histogram

@test.describe("tests")
def _():
    @test.it("Sample Tests")
    def _():
        test.assert_equals(histogram([1, 1, 0, 1, 3, 2, 6], 1), [1, 3, 1, 1, 0, 0, 1])
        test.assert_equals(histogram([1, 1, 0, 1, 3, 2, 6], 2), [4, 2, 0, 1])
        test.assert_equals(histogram([], 1), [])
        test.assert_equals(histogram([8], 1), [0, 0, 0, 0, 0, 0, 0, 0, 1])

def eq_all(iterable):
    res = list(iterable)
    length = len(res)
    submit = True
    i = 0
    while i < length:
        if res[i] == res[i + 1]:
            pass
        else:
            submit = False
            break
        if i == length - 1 and submit != False:
            break
        elif i + 1 == length - 1:
            break
        i += 1
    return submit

def goldbach(even_number):
    result_arr = []
    prime_nums = []
    
    # first loop shows prime numbers range of even_number, which appends in prime_nums array
    i = 1
    while i <= even_number:
        i_is_prime = True
        j = 2
        while j < i:
            if i % j == 0:
                i_is_prime = False
                break
            j += 1
        if i_is_prime and i != 1:
            prime_nums.append(i)
        i += 1
    
    # second loop gives all prime numbers sum for give even_number. which appends in result_arr array
    k = 0
    while k <= len(prime_nums) - 1:
        t = k
        while t <= len(prime_nums) - 1:
            if prime_nums[k] + prime_nums[t] == even_number:
                result_arr.append([prime_nums[k], prime_nums[t]])
            t += 1
        k += 1
    
    # return result
    return result_arr

def is_sator_square(tablet):
    n = len(tablet)
    for i in range(n):
        for j in range(n):
            if tablet[i][j] != tablet[j][i]:
                return False
            if tablet[i][j] != tablet[n-1-i][n-1-j]:
                return False
    return True

def factorial(n):
    if n < 0:
        return None  # Factorial not defined for negative numbers
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
print(factorial(5))  # Output: 120

import sys
def recursive_function(n):
    if n <= 0:
        return 0
    else:
        return n + recursive_function(n - 1)

total = 0
for i in range(1, 101):
    total += recursive_function(i)
print("Total sum:", total)

import sys
sys.setrecursionlimit(10**7)

# Generate a large graph with random weights
import random

NUM_NODES = 1000
graph = {i: [] for i in range(NUM_NODES)}

# Randomly connect nodes with weights
for _ in range(NUM_NODES * 5):  # sparse graph
    u = random.randint(0, NUM_NODES - 1)
    v = random.randint(0, NUM_NODES - 1)
    if u != v:
        weight = random.uniform(1, 10)
        graph[u].append((v, weight))

# Recursive function to find all paths from start to end with sum greater than a threshold


# Generate a list of numbers from 1 to 20
numbers = list(range(1, 21))

# Initialize an empty list to store squares of even numbers
even_squares = []

# Loop through the numbers
for num in numbers:
    # Check if the number is even
    if num % 2 == 0:
        # Calculate the square and add to the list
        square = num ** 2
        even_squares.append(square)

# Print the list of squares
print("Squares of even numbers from 1 to 20:")
for sq in even_squares:
    print(sq)

def greet(name):
    return f"Hello, {name}!"

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def list_operations(lst):
    lst.append(100)
    lst.remove(lst[0])
    return lst

def main():
    names = ["Alice", "Bob", "Charlie"]
    for name in names:
        message = greet(name)
        print(message)
    number = 10
    fact = factorial(number)
    print(f"Factorial of {number} is {fact}")
    sample_list = [1, 2, 3, 4, 5]
    updated_list = list_operations(sample_list)
    print(f"Updated list: {updated_list}")
    for i in range(1, 6):


def vert_mirror(strng):
    # Split the string into lines
    lines = strng.split('\n')
    # Reverse each line
    reversed_lines = [line[::-1] for line in lines]
    # Join back
    return '\n'.join(reversed_lines)

def hor_mirror(strng):
    # Split into lines
    lines = strng.split('\n')
    # Reverse the order of lines
    reversed_lines = lines[::-1]
    # Join back
    return '\n'.join(reversed_lines)

def oper(fct, s):
    return fct(s)

@test.describe('Tests')
     
def fixed_tests():
    def testing(n, expected):
        actual = c(n)
        test.assert_equals(actual, expected)
        
    @test.it('Basic Tests c')
    def basic_tests1():
        testing(423128, 0)
        testing(1369, 4)
        testing(2999824, 28)
        testing(11710084, 64)
        testing(1, 1)
        testing(4, 4)
        testing(4096576, 160)
        testing(2019, 0)

from solution import game
import codewars_test as test

@test.describe('Testing...')
def _():
    @test.it('"Fixed tests')
    def _():
        test.assert_equals(game(0), [0])
        test.assert_equals(game(1), [1, 2])
        test.assert_equals(game(8), [32])

@test.describe("Example Test Cases")
def example_tests():

    @test.it("Start equals target")
    def _():
        test.assert_equals(
            min_moves_with_promotion("b4", "b4"), 0)

    @test.it("Simple pawn forward move")
    def _():
        test.assert_equals(
            min_moves_with_promotion("b4", "b5"), 1)

    @test.it("Pawn reaches promotion square")
    def _():
        test.assert_equals(
            min_moves_with_promotion("b7", "b8"), 1)

test.describe('Example Tests')
example_tests = (
	(100,(25,38,55,46,82),(64,90,37,25,58)),
	(200,(61,83,37,55,92,35,68,72),(90,81,36,114,67,25,31,84)),
	(300,(98,112,121,95,63),(120,94,90,88,30),(116,144,45,200,32)),
	(400,(186,78,56,67,78,127,78,192),(78,67,208,45,134,212,82,99),(327,160,49,246,109,98,44,57)),
	(500,(345,168,122,269,151),(56,189,404,129,101),(364,129,209,163,379),(520,224,154,74,420)),
)
example_sols = (
	(1,(3,2)),
	(0,(6,7)),
	(0,(2,)),
	(2,(0,2,5)),
	(-1,()),
)

import codewars_test as test
from solution import delete_nth

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(
            delete_nth([20, 37, 20, 21], 1),
            [20, 37, 21],
            "From list [20, 37, 20, 21], 1 you get",
        )
        test.assert_equals(
            delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3),
            [1, 1, 3, 3, 7, 2, 2, 2],
            "From list [1, 1, 3, 3, 7, 2, 2, 2, 2], 3 you get",
        )
        test.assert_equals(
            delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3),
            [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5],
            "From list [1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3 you get",
        )
        test.assert_equals(
            delete_nth([1, 1, 1, 1, 1], 5),
            [1, 1, 1, 1, 1],
            "From list [1, 1, 1, 1, 1], 5 you get",
        )
        test.assert_equals(delete_nth([], 5), [], "From list [], 5 you get")
        test.assert_equals(
            delete_nth([12, 39, 19, 39, 39, 19, 12], 1), 
            [12, 39, 19],
            "From list [12, 39, 19, 39, 39, 19, 12], 1 you get",
        )    

def row_sum_odd_numbers(n):
    odd = n * (n - 1) + 1
    arr = [odd]
    sum = 0
    i = 1
    while i < n:
        odd += 2
        arr.append(odd)
        i += 1
    for j in arr:
        sum += j
    return sum

@test.describe("Sample Tests")
def _():
    ga = GeneticAlgorithm()

    @test.describe("Short goal")
    def short_goal_tests():
        goal = "1110110111101101"
        simple = simple_match_fitness(goal)

        @test.it("Default iterations")
        def default_iterations():
            test.assert_equals(ga.run(simple, len(goal), 0.6, 0.002), goal)

        @test.it("Defined iterations")
        def defined_iterations():
            test.assert_equals(ga.run(simple, len(goal), 0.6, 0.002, 100), goal)

@test.describe("minimum_percentage")
def tests():
    @test.it("Sample Tests")
    def samples():
        tests = (
            ( (76,),             76 ),
            ( (50, 100),         50 ),
            ( (50, 50),           0 ),
            ( (100, 100, 100),  100 ),
            ( (65, 80, 80, 90),  15 )
        )
        for foods, expected in tests:
            message = f"Testing for {foods}"
            submitted = minimum_percentage(foods[:])
            test.assert_equals(submitted, expected, message)

@test.describe('Example tests')
def example_tests():

    @test.it('Sample test')
    def sample_tests():

        rope = get_rope_length(200, 0.5)
        test.assert_equals(rope, 115)

        rope = get_rope_length(10, 0.5)
        test.assert_equals(rope, 5)


    @test.it('Do not eat anything')
    def test_edge_no_eat():
        rope = get_rope_length(200, 0.0)
        test.assert_equals(rope, 0);


    @test.it('Eat all grass')
    def test_edge_eat_all():
        rope = get_rope_length(200, 1.0)


def _test_teknonymize(input_, actual, expected):
    if actual != expected:
        print(f"<LOG::-Input>{input_}")
        print(f"<TAB::-Actual>{json.dumps(actual, default=str)}")
        print(f"<TAB::-Expected>{json.dumps(expected, default=str)}")
        test.fail("Test failed")
    else:
        test.assert_equals(actual, expected)


@test.describe("Sample Tests")
def _():
    def get_example():
        persons = [_person() for _ in range(8)]
        dates = ['1000-01-01', '1020-01-01', '1021-02-01', '1023-11-28', '1047-01-01', '1043-11-01', '1045-01-01', '1046-01-01']
        sexes = ['m', 'f', 'm', 'm', 'f', 'f', 'f', 'm']
        names = 'abcdhefg'
        dates = map(datetime.fromisoformat, dates)
        for p, n, d, s in zip(persons, names, dates, sexes):
            p['name'] = n


@test.describe('Walk Validator - fixed tests')
def sample_tests():
    @test.it ("should return true for a valid walk")
    def _():
        test.assert_equals(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), True, 'should return True');
    @test.it ("should return false if walk is too long")
    def _():
        test.assert_equals(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']), False, 'should return False');
    @test.it ("should return false if walk is too short")
    def _():
        test.assert_equals(is_valid_walk(['w']), False, 'should return False');
    @test.it ("should return false if walk does not bring you back to start")
    def _():        
        test.assert_equals(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), False, 'should return False');

import codewars_test as test
from solution import luck_check

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(luck_check('5555'), True)

from solution import carmichael
import codewars_test as test

@test.describe("Fixed tests")
def tests():
    
    @test.it("Should obtain correct result for fixed edge tests with where n is not a positive integer n >= 1")
    def test_carmichael_fixed_edge():
        TESTS = [(0,0),(-3,0),(-4003,0),(-1339185,0)]
        for args in TESTS:
            n, exp = args
            test.assert_equals(carmichael(n), exp, "Returned solution incorrect for input value of n = {}. The correct answer is {}".format(n, exp))
        
    @test.it("Should obtain correct Carmichael function for fixed tests with small n")
    def test_carmichael_fixed_small():
        TESTS = [(1,1),(2,1),(4,2),(5,4),(7,6),(15,4),(30,4),(93,30),(73,72),(49,42),(870,28),(765,48),(118,58),(727,726),(643,642)]
        for args in TESTS:
            n, exp = args

import codewars_test as test
from solution import find_lineup

@test.describe("Example Tests")
def example_tests():
    
    @test.it("Valid Cases") 
    def run_tests():
        
        test.assert_equals(find_lineup([1, 2, 0]), [3, 1, 2])
        test.assert_equals(find_lineup([1, 4, 2, 6, 8, 0, 5, 7, 3]), [6, 1, 3, 9, 2, 7, 4, 8, 5])
        test.assert_equals(find_lineup([0]), [1])

import codewars_test as test
from solution import max_fork

@test.describe("Example Tests")
def example_tests():
    
    @test.it("No Forks")
    def run_tests():
        
        ## No valid knight moves.
        board1 = [['.', 'Q', '.', '.', '.', 'K', '.', '.'],
                  ['.', '.', '.', 'N', '.', '.', '.', '.'],
                  ['.', 'P', '.', '.', '.', 'B', '.', '.'],
                  ['.', '.', 'R', '.', 'P', '.', '.', '.'],   
                  ['.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', 'P', '.', '.', '.', 'p', '.', 'p'],   
                  ['.', '.', 'R', '.', 'p', '.', '.', '.'],
                  ['N', '.', '.', '.', '.', '.', 'n', '.']]

import codewars_test as test
from solution import is_valid_IP

@test.describe("Sample tests")
def _():
    @test.it("Tests")
    def __():

import codewars_test as test
from solution import doors

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(doors(5), 2)
        test.assert_equals(doors(10), 3)
        test.assert_equals(doors(100), 10)

import codewars_test as test
from solution import letters_to_numbers

@test.describe("Sample tests")
def sample_tests():
    test_cases = [
        ["I Love You", 170],
        ["ILoveYou", 170],
        ["ARE YOU HUNGRY?", 356],
        ["oops, i did it again!", 152],
        ["Give me 5!", 73],
        ["Give me five!", 110],
    ]

import codewars_test as test
from solution import round_by_2_decimal_places
from decimal import Decimal

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')

import codewars_test as test
from solution import *

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(FileNameExtractor.extract_file_name("1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION"),"FILE_NAME.EXTENSION")
        test.assert_equals(FileNameExtractor.extract_file_name("1_FILE_NAME.EXTENSION.OTHEREXTENSIONadasdassdassds34"),"FILE_NAME.EXTENSION")


import codewars_test as test
from preloaded import validate
from solution import dance

@test.describe('Example test cases')
def example_tests():
    def run_test(map_str, optimal, desc=''):
        print(desc)
        print(f'Map: \n{map_str}')
        solution = dance(map_str)
        
        if not isinstance(solution, str):
            test.expect(False, "You did not return a string")
            return
        
        valid = validate(map_str, solution)
        print(f"\n \nYour moves: {solution}")
        print("Folded: ")
        print('\n'.join(' '.join(row) for row in valid[0]))
        
        if valid[1] is not True:
            test.expect(False, valid[1])
            return

rom solution import generate_hashtag
import codewars_test as test

@test.describe("Fixed tests")
def tests():
    
    @test.it("Should generate the correct hashtag in fixed tests")
    def test_correct_hashtag_fixed():
        test.assert_equals(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
examples:
	" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false

from solution import de_nico

@test.describe('Fixed Tests')
def fixed_tests():
    @test.it('Simple Cases')
    def example_cases():
        test.assert_equals(de_nico("crazy","cseerntiofarmit on  "),"secretinformation")
        test.assert_equals(de_nico("crazy","cseerntiofarmit on"),"secretinformation")
        test.assert_equals(de_nico("abc","abcd"),"abcd")
        test.assert_equals(de_nico("ba","2143658709"), "1234567890")
        test.assert_equals(de_nico("a","message"),"message")
        test.assert_equals(de_nico("key","eky"),"key")

#!/bin/bash
playPass () {
    # your code
}
playPass "$1" "$2"
import codewars_test as test
from solution import play_pass

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases()

F(0) = 1
M(0) = 0
F(n) = n - M(F(n - 1))
M(n) = n - F(M(n - 1))
