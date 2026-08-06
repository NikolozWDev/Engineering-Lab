function gameCall(userChoice) {
  const options = ['rock', 'paper', 'scissors'];
  const computerChoice = options[Math.floor(Math.random() * options.length)];
  if (userChoice === computerChoice) return `Tie! Both chose ${userChoice}`;
  if (
    (userChoice === 'rock' && computerChoice === 'scissors') ||
    (userChoice === 'scissors' && computerChoice === 'paper') ||
    (userChoice === 'paper' && computerChoice === 'rock')
  ) {
    return `Win! You chose ${userChoice} and computer chose ${computerChoice}`;
  } else {
    return `Lose! You chose ${userChoice} and computer chose ${computerChoice}`;
  }
}

function whichHand(word) {
  left = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
  right = ['y', 'h', 'n', 'u', 'j', 'i', 'k', 'm', 'o', 'l', 'p']
  hasLeft = false
  hasRight = false
  for (let char of word) {
      if (left.includes(char)) {
          hasLeft = true
      }
      if (right.includes(char)) {
          hasRight = true
      }
      if (hasLeft && hasRight) {
          return "BOTH"
      }
  }
  if(hasLeft) {return "LEFT"}
  if(hasRight) {return "RIGHT"}
  
  return "NONE"
}


const { config, expect } = require("chai");

// Disable truncating the content of arrays when printing them on the console
config.truncateThreshold = 0;

const testEncode = (message, deck, hint) =>
	describe(`encode message '${message}'`, () =>
		it(`should return '${deck?.join(" ") || null}'`, () =>
			expect(encode(message)).to.deep.equal(deck, hint)));

const testDecode = (deck, message, hint) =>
	describe(`decode deck '${deck.join(" ")}'`, () =>
		it(`should return '${message}'`, () =>
			expect(decode(deck)).to.deep.equal(message, hint)));

testEncode(
	"A",
	// prettier-ignore
	[
		"AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "TC", "JC", "QC", "KC",
		"AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "TD", "JD", "QD", "KD",
		"AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "TH", "JH", "QH", "KH",
		"AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "TS", "JS", "KS", "QS"
	],
	"The message 'A' corresponds to the second permutation of the deck of cards (its numeric value is equal to 1)",
);


class DataHandler {
  static count = 0;
  #privateData;

  constructor(data) {
    if (!Array.isArray(data)) throw new TypeError('Data must be an array');
    this.#privateData = data;
    DataHandler.count++;
  }

  static getCount() {
    return DataHandler.count;
  }

  get data() {
    return this.#privateData;
  }

  set data(newData) {
    if (!Array.isArray(newData)) throw new TypeError('Data must be an array');
    this.#privateData = newData;
  }

  add(item) {
    this.#validateItem(item);
    this.#privateData.push(item);
  }

  remove(item) {
    const index = this.#privateData.indexOf(item);
    if (index !== -1) this.#privateData.splice(index, 1);
  }

  average() {
    if (this.#privateData.length === 0) throw new Error('No data');
    const sum = this.#privateData.reduce((acc, val) => acc + val, 0);
    return sum / this.#privateData.length;
  }

  median() {
    if (this.#privateData.length === 0) throw new Error('No data');
    const sorted = [...this.#privateData].sort((a, b) => a - b);
    const mid = Math.floor(sorted.length / 2);
    if (sorted.length % 2 === 0)
      return (sorted[mid - 1] + sorted[mid]) / 2;
    return sorted[mid];
  }

  #validateItem(item) {
    if (typeof item !== 'number') throw new TypeError('Item must be a number');
  }
}

class AdvancedData extends DataHandler {
  variance() {
    const mean = this.average();
    const squaredDiffs = this.#privateData.map(x => (x - mean) ** 2);
    const sum = squaredDiffs.reduce((a, b) => a + b, 0);
    return sum / this.#privateData.length;
  }

  stdDev() {
    return Math.sqrt(this.variance());
  }
}

const data = new AdvancedData([10, 20, 30]);
console.log(data.average());
console.log(data.median());
console.log(data.variance());
console.log(data.stdDev());
console.log(AdvancedData.getCount());

class AdvancedCalculator {
  // Private fields
  #history = [];

  constructor(initialValue = 0) {
    this.value = initialValue;
  }

  // Static method
  static description() {
    return 'This is a highly advanced calculator class with multiple features.';
  }

  // Getter for history
  get history() {
    return [...this.#history];
  }

  // Method to perform addition
  add(num) {
    this.value += num;
    this.#log(`Added ${num}, new value: ${this.value}`);
    return this;
  }

  // Method to perform subtraction
  subtract(num) {
    this.value -= num;
    this.#log(`Subtracted ${num}, new value: ${this.value}`);
    return this;
  }

  // Method to perform multiplication
  multiply(num) {
    this.value *= num;
    this.#log(`Multiplied by ${num}, new value: ${this.value}`);
    return this;
  }

  // Method to perform division
  divide(num) {
    if (num === 0) {
      throw new Error('Cannot divide by zero!');
    }
    this.value /= num;
    this.#log(`Divided by ${num}, new value: ${this.value}`);
    return this;
  }

  // Private method to log history
  #log(operation) {
    this.#history.push({ operation, timestamp: new Date() });
  }

  // Async method to fetch data from an API and update value
  async fetchAndUpdate(apiUrl) {
    try {
      const response = await fetch(apiUrl);
      const data = await response.json();
      if (data && data.value) {
        this.value = data.value;
        this.#log(`Fetched and updated value to ${this.value}`);
      }
    } catch (error) {
      console.error('Fetch error:', error);
    }
  }
}

// Inheritance example
class AdvancedScientificCalculator extends AdvancedCalculator {
  constructor(initialValue = 0) {
    super(initialValue);
  }

  // Method for power
  power(exponent) {
    this.value = Math.pow(this.value, exponent);
    this.#log(`Raised to the power of ${exponent}, new value: ${this.value}`);
    return this;
  }
}

// Usage:
(async () => {
  const calc = new AdvancedScientificCalculator(10);
  console.log(AdvancedCalculator.description());
  calc.add(5).subtract(3).multiply(2).divide(4).power(3);
  console.log('Current value:', calc.value);
  console.log('History:', calc.history);

  await calc.fetchAndUpdate('https://api.example.com/data');
  console.log('Updated value after fetch:', calc.value);
})();

function bubbleSort(arr) {
  let n = arr.length;
  let swapped;
  do {
    swapped = false;
    for (let i = 0; i < n - 1; i++) {
      if (arr[i] > arr[i + 1]) {
        // Swap
        [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
        swapped = true;
      }
    }
    n--; // Reduce the range for optimization
  } while (swapped);
  return arr;
}

// Example usage:


function quickSort(arr) {
  if (arr.length <= 1) return arr;
  const pivot = arr[Math.floor(arr.length / 2)];
  const left = [];
  const right = [];
  for (let i = 0; i < arr.length; i++) {
    if (i === Math.floor(arr.length / 2)) continue;
    if (arr[i] < pivot) {
      left.push(arr[i]);
    } else {
      right.push(arr[i]);
    }
  }
  return [...quickSort(left), pivot, ...quickSort(right)];
}

function generateRandomArray(size, min, max) {
  const result = [];
  for (let i = 0; i < size; i++) {
    result.push(Math.floor(Math.random() * (max - min + 1)) + min);
  }
  return result;
}

const arraySize = 20;
const minValue = 1;
const maxValue = 100;
const unsortedArray = generateRandomArray(arraySize, minValue, maxValue);
const sortedArray = quickSort(unsortedArray);
console.log('Unsorted:', unsortedArray);
console.log('Sorted:', sortedArray);

function commitTitle(str) {
  const cleanedStr = str.replace(/[^a-z0-9]/gi, '').toLowerCase();
  const reversedStr = cleanedStr.split('').reverse().join('');
  return cleanedStr === reversedStr;
}

console.log(commitTitle("A man, a plan, a canal, Panama"));
console.log(commitTitle("OpenAI"));

describe("Word values", function(){
  const {assert, config} = require('chai');
  config.truncateThreshold = 0;

  it("simple examples", function(){
    assert.deepEqual( wordValue(["codewars","abc","xyz"]), [88,12,225] );
    assert.deepEqual( wordValue(["abc abc","abc abc","abc","abc"]), [12,24,18,24] );
  });
});

const { assert } = require('chai');

describe("Example tests", function() {
  it("Should return the combined weight of just the tennis balls!", function() {
    assert.deepEqual(ballCollector([58, 68, 62, 69, 58]), { weight: 116 });
    assert.deepEqual(ballCollector([60,66,71,68,62]), { weight: 0 });
    assert.deepEqual(ballCollector([58]), { weight: 58 });
    assert.deepEqual(ballCollector([58, 58, 58]), { weight: 174 });
  });
});


const { assert } = require('chai');

describe('Example tests', () => {
  it("Basic Tests",() =>{
    assert.strictEqual(colorProbability("red", "bumpy"), "0.57");
    assert.strictEqual(colorProbability("green", "bumpy"), "0.14");
    assert.strictEqual(colorProbability("yellow", "smooth"), "0.33");
  });
});

const { assert } = require('chai');

describe("Tests", () => {
  it("The smallest 4-parasitic number which ends with a 4 in base 10", () => {
    assert.strictEqual('102564', calculateSpecial(4, 10));
  });
  
  it("The smallest 4-parasitic number which ends with a 4 in base 16", () => {
    assert.strictEqual('104', calculateSpecial(4,16));
  });   
});



function ho(prev) {
  if (prev === undefined) {
    return "Ho!";
  }
  return "Ho " + prev;
}

 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {

    let sum1 = BigInt(l1.reverse().join('');)
    let sum2 = BigInt(l2.reverse().join(''));

    let result = (sum1 + sum2).toString().split('').reverse().map(Number)
    
};

const { assert } = require('chai');

describe("Split Strings", () => {
  it("Basic tests", () => {
    assert.deepEqual(solution("abcdef"), ["ab", "cd", "ef"]);
    assert.deepEqual(solution("abcdefg"), ["ab", "cd", "ef", "g_"]);
    assert.deepEqual(solution(""), []);
  });
});

const { assert } = require("chai");

describe("Sample Tests", () => {
  it("", () => {
    //return a.concat(b) ?
    assert.deepEqual(testit([0],[1]), [0,1], "")
    assert.deepEqual(testit([1,2],[3,4]), [1,2,3,4], "")
    assert.deepEqual(testit([1],[2,3,4]), [1,2,3,4], "")
    assert.deepEqual(testit([1,2,3],[4]), [1,2,3,4], "")
    assert.deepEqual(testit([1,2],[1,2]), [1,1,2,2], "")
    //click "Submit" try more testcase...
  });
});

// happy new year
function willItWorkIn2026() {
  const problems = [
    "AI said it's fine ",
    "Works on my machine! ",
    "It's a feature, not a bug ",
    "The internet told me to do this ",
    "Added more console.log() "
  ];
  
  const randomProblem = problems[Math.floor(Math.random() * problems.length)];
  
  const willWork = Math.random() > 0.5;
  
  if (willWork) {
    return `Yes! Because: "${randomProblem}"`;
  } else {
    return `Nope But: "${randomProblem}"`;
  }
}

function predict2026() {
  console.log("2026 Prediction:");
  console.log("JavaScript will have " + (Math.floor(Math.random() * 10) + 5) + " new frameworks");
  console.log("We'll still not understand Promises");
  console.log(willItWorkIn2026());
}

predict2026();

console.log("\nconsole.log('Hello 2026!'); // Still debugging with this");


function listFromArray(nodesArray) {
   if(nodesArray.length === 0)
       return null;
   const head = nodesArray[0];
   for (let i = 1; i < nodesArray.length; i++)
       nodesArray[i - 1].next = nodesArray[i];

   nodesArray.at(-1).next = null;
   return head;
    }

from solution import sq_in_rect
import codewars_test as test

@test.describe("Tests...")
def _():
    @test.it("Basic Tests")
    def _():
        test.assert_equals(sq_in_rect(5, 5), None)
        test.assert_equals(sq_in_rect(5, 3), [3, 2, 1, 1])
        test.assert_equals(sq_in_rect(3, 5), [3, 2, 1, 1])
        test.assert_equals(sq_in_rect(20, 14), [14, 6, 6, 2, 2, 2])

const chai=require('chai')
const assert=chai.assert
chai.config.truncateThreshold = 0;

describe("Basic tests",function(){
  it("Basic tests",function(){
    assert.deepEqual(sqInRect(5, 5), null)
    assert.deepEqual(sqInRect(5, 3), [3, 2, 1, 1])
    assert.deepEqual(sqInRect(3, 5), [3, 2, 1, 1])
    assert.deepEqual(sqInRect(20, 14), [14, 6, 6, 2, 2, 2])
  })
});

const Test = require('@codewars/test-compat');

describe("Normal operation", function() {
  it ("should open completely and stay open", function() {
    Test.assertEquals(door('P....'+'.'.repeat(10)),'12345'+'5'.repeat(10));
  });
  
  it ("should open completely, then stay open, then close", function() {
    Test.assertEquals(door('P......P......'),
                           '12345554321000');
  });
});

describe("Pause", function() {
  it ("should start opening and pause on second buttonpress", function() {
    Test.assertEquals(door('P.P..'),
                           '12222');
  });
  it ("should resume opening on third buttonpress", function() {
    Test.assertEquals(door('P.P.P....'),
                           '122234555');
  });
});

describe("Obstacle", function() {
  it ("should reverse while opening", function() {
    Test.assertEquals(door('P.O....'),
                           '1210000');
  });
});

describe("Obstacle + Pause", function() {
  it ("should reverse while opening (and allow pause)", function() {
    Test.assertEquals(door('P..OP..P..'),
                           '1232222100');
  });
});

describe("Example", function() {
  it ("should start opening and reverse when obstacle", function() {
    Test.assertEquals(door('..P...O.....'),
                           '001234321000');
  });
});



class Archiver {
    constructor() {
    }

    set temperature(temperature) {
    }

    get temperature() {
    }

    getArchive() {
        return [];
    }
}
function createGame(winningNumber) {
  let attempts = 0; // This variable is stored in the closure's backpack

  return function guess(number) {
    attempts++;
    if (number === winningNumber) {
      return `You win in ${attempts} attempts!`;
    } else {
      return `Try again. It's your ${attempts}th attempt.`;
    }
  }
}

const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold = 0;


function quickSort(arr) {
  if (arr.length <= 1) {
    return arr;
  }
  
  const pivot = arr[Math.floor(arr.length / 2)];
  const left = [];
  const right = [];
  const equal = [];

  for (let el of arr) {
    if (el < pivot) {
      left.push(el);
    } else if (el > pivot) {
      right.push(el);
    } else {
      equal.push(el);
    }
  }

  return [...quickSort(left), ...equal, ...quickSort(right)];
}

console.log(quickSort([3, 6, 8, 10, 1, 2, 1]));



double someNumber = .123 + .456 * Math.Pow(Math.E, .789 * Math.Pow((homeIndex + .22), .012));
algorithm that shows someNumber

thinking passwords
solved algorithms
bodishi mishiko

let array = [10, 23, 25, 62, 45, 23];

solved medium task

let i = 0;
while(i < array.length) {
  console.log(array[i]);
 i = i + 1;
};


there are more tools
yea, yea more tools. your brain is -x number IQ


solve many problems tasks

solved 8 tasks today
good job
more job to require more logic intelect

today solved 3 6kyu Javascript problems in codewars
momiteve
4 7kyu tasks

codding without VScode is bullshit
