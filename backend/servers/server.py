@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(decode("yvvi"), "beer")
        test.assert_equals(decode("Blf zoivzwb szw 10 yvvih"), "You already had 10 beers")
        test.assert_equals(decode("Ovg'h hdrn rm gsv ulfmgzrm!"), "Let's swim in the fountain!")
        test.assert_equals(decode({"brand": "Starobrno" }), "Input is not a string")
        test.assert_equals(decode("Tl slnv, blf'iv wifmp"), "Go home, you're drunk") 
        test.assert_equals(decode("Hfiv r xzm wzmxv lm xlk'h xzi, slow nb yvvi"), "Sure i can dance on cop's car, hold my beer")
        test.assert_equals(decode(True), "Input is not a string")
        test.assert_equals(decode("Hvv? R'n mlg gszg wifmp, r xzm hgroo gzpv nb xolgsvh luu"), "See? I'm not that drunk, i can still take my clothes off")
        test.assert_equals(decode(123), "Input is not a string")
        test.assert_equals(decode(["Beer"]), "Input is not a string")

class AdvancedDataProcessor:
    _instance_count = 0

    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError("Data must be a list")
        self._data = data
        AdvancedDataProcessor._instance_count += 1

    @classmethod
    def get_instance_count(cls):
        return cls._instance_count

    @staticmethod
    def validate_data(data):
        if not all(isinstance(item, (int, float)) for item in data):
            raise ValueError("All items must be numeric")
        return True

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self.validate_data(new_data)
        self._data = new_data

    def mean(self):
        if not self._data:
            raise ValueError("Data list is empty")
        return sum(self._data) / len(self._data)

    def median(self):
        if not self._data:
            raise ValueError("Data list is empty")
        sorted_data = sorted(self._data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def add_data(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be numeric")
        self._data.append(value)

class AdvancedDataAnalyzer(AdvancedDataProcessor):
    def __init__(self, data):
        super().__init__(data)

    def variance(self):
        mean_value = self.mean()
        return sum((x - mean_value) ** 2 for x in self._data) / len(self._data)

    def standard_deviation(self):
        return self.variance() ** 0.5

# Usage example:
if __name__ == "__main__":
    processor = AdvancedDataAnalyzer([10, 20, 30, 40])
    print("Mean:", processor.mean())
    print("Median:", processor.median())
    print("Variance:", processor.variance())
    print("Std Dev:", processor.standard_deviation())
    print("Instance Count:", AdvancedDataProcessor.get_instance_count())


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)

    def total(self):
        return sum(p.price for p in self.items)

    def show(self):
        print("Cart Items:")
        for p in self.items:


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = 5
print(f"The factorial of {number} is {factorial(number)}")

// connecting wifi
import codewars_test as test
from solution import solution

@test.describe("Sample tests")
def sample_tests():
    
    @test.it("Should return 3 for n=4")
    def _():
        test.assert_equals(solution(4), 3)
        
    @test.it("Should return 8 for n=6")
    def _():
        test.assert_equals(solution(6), 8)
    

import codewars_test as test
import solution

def fix_tester(input: str, expected: str):
    output = solution.circle_mender(input)
    
    message = (f"You haven't fixed my circle :(\n"
               f"Input:\n{input}\n"           
               f"Output:\n{output}\n"         
               f"Expected:\n{expected}\n"     
               f"Can you try again?")
    test.expect(output == expected, message)

from solution import Vector
import codewars_test as test

@test.describe("Vector tests")
def vector_tests():
    
    @test.it("Example tests")
    def example_tests():
        
        a = Vector([1, 2])
        b = Vector([3, 4])
        
        test.expect(a.add(b).equals(Vector([4, 6])))
        
        
        a = Vector([1, 2, 3])
        b = Vector([3, 4, 5])

    def total_price(self):
        price = self.product.down_price if self.product.down_price != "0.00" else self.product.price
        return price * self.number
    total_price = property(total_price)

added models in Basket page. model basket. new database

import codewars_test as test
from solution import alphabetic


def dotest(s, expected):
    test.assert_equals(alphabetic(s), expected)


@test.describe("Tests")
def test_group():
    @test.it("Sample tests")
    def test_case():
        for s, expected in [('asd', False), ('codewars', False), ('door', True), ('cell', True), ('z', True),
                            ('', True), ]:
            dotest(s, expected)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'masteruser',
        'PASSWORD': '12345678',
        'HOST': 'w3-django-project.cdxmgq9zqqlr.us-east-1.rds.amazonaws.com',
        'PORT': '5432'
    }
}


created CRUD operation easly
running server again
running server firstpro
generating structure
running
added JS in back-end
adding images and filefields for more settings
made changes in server and databases to login the user (logout to)
recognize all servers by adminPanel
settings, urls, views, templates, jinja and more features
added django
practicing back-end
python code
int code
back-end with servers

added another branch
instaled python
studying python syntax
