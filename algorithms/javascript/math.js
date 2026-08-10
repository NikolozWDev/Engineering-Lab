class BlackjackStrategy {
  constructor() {}

  decideAction(playerHand, dealerUpCard, canSplit = false, canDouble = false) {
    const total = this.getHandTotal(playerHand);
    const isSoft = this.isSoftHand(playerHand);
    const pair = this.isPair(playerHand);
    const dealerCardValue = this.getCardValue(dealerUpCard);

    // Handle pairs (split)
    if (pair && canSplit) {
      return this.splitDecision(playerHand[0], dealerCardValue);
    }

    // Handle soft hands
    if (isSoft) {
      return this.softHandDecision(total, dealerCardValue, canDouble);
    }

    // Handle hard hands
    return this.hardHandDecision(total, dealerCardValue, canDouble);
  }

  getHandTotal(hand) {
    let total = 0;
    let aces = 0;
    for (const card of hand) {
      const value = this.getCardValue(card);
      total += value;
      if (value === 11) aces++;
    }
    // Adjust for aces
    while (total > 21 && aces > 0) {
      total -= 10;
      aces--;
    }
    return total;
  }

  isSoftHand(hand) {
    let total = 0;
    let aces = 0;
    for (const card of hand) {
      const value = this.getCardValue(card);
      total += value;
      if (value === 11) aces++;
    }
    return aces > 0 && total <= 21;
  }

  isPair(hand) {
    return hand.length === 2 && hand[0] === hand[1];
  }

  getCardValue(card) {
    if (typeof card === 'number') return card;
    const rank = card.toString().toUpperCase();
    if (['J', 'Q', 'K'].includes(rank)) return 10;
    if (rank === 'A') return 11;
    return parseInt(rank, 10);
  }

  splitDecision(card, dealerCard) {
    // Basic splitting strategy
    if (card === 'A') {
      return 'Split'; // Always split Aces
    }
    if (card === 8) {
      return 'Split'; // Always split 8s
    }
    if (card === 2 || card === 3) {
      if (dealerCard >= 4 && dealerCard <= 7) {
        return 'Split';
      }
    }
    if (card === 4) {
      if (dealerCard === 5 || dealerCard === 6) {
        return 'Split';
      }
    }
    if (card === 6) {
      if (dealerCard >= 3 && dealerCard <= 6) {
        return 'Split';
      }
    }
    if (card === 9) {
      if ([2, 3, 4, 5, 6, 8, 9].includes(dealerCard)) {
        return 'Split';
      }
    }
    return 'Hit'; // Default fallback
  }

  softHandDecision(total, dealerCard, canDouble) {
    // Soft totals strategy
    if (total >= 19) {
      return 'Stand';
    }
    if (total === 18) {
      if (dealerCard >= 9 || dealerCard === 1) {
        return 'Hit';
      } else if (canDouble) {
        return 'Double';
      } else {
        return 'Stand';
      }
    }
    if (total === 17) {
      if (canDouble && dealerCard >= 3 && dealerCard <= 6) {
        return 'Double';
      } else {
        return 'Hit';
      }
    }
    if (total <= 16) {
      if (canDouble && dealerCard >= 4 && dealerCard <= 6) {
        return 'Double';
      } else {
        return 'Hit';
      }
    }
    return 'Stand';
  }

  hardHandDecision(total, dealerCard, canDouble) {
    // Hard totals strategy
    if (total >= 17) {
      return 'Stand';
    }
    if (total >= 13 && total <= 16) {
      if (dealerCard >= 2 && dealerCard <= 6) {
        return 'Stand';
      } else {
        return 'Hit';
      }
    }
    if (total === 12) {
      if (dealerCard >= 4 && dealerCard <= 6) {
        return 'Stand';
      } else {
        return 'Hit';
      }
    }
    if (total === 11 && canDouble) {
      return 'Double';
    }
    if (total === 10 && canDouble && dealerCard <= 9) {
      return 'Double';
    }
    if (total === 9 && canDouble && dealerCard >= 3 && dealerCard <= 6) {
      return 'Double';
    }
    return 'Hit';
  }
}

// Example usage:
const blackjackAI = new BlackjackStrategy();

const playerHand = [8, 8]; // Example hand
const dealerUpCard = '9'; // Dealer's visible card
const canSplit = true;
const canDouble = true;

const decision = blackjackAI.decideAction(playerHand, dealerUpCard, canSplit, canDouble);
console.log(`Decision: ${decision}`); // e.g., "Split" or "Hit" or "Stand"


function shouldPlayerHit(playerTotal, dealerCard, isSoftHand) {
  // Basic blackjack strategy for hard hands
  if (!isSoftHand) {
    if (playerTotal <= 11) {
      return true; // Always hit on 11 or less
    } else if (playerTotal >= 17) {
      return false; // Stand on 17 or more
    } else if (playerTotal >= 12 && playerTotal <= 16) {
      if (dealerCard >= 7) {
        return true; // Hit if dealer shows 7 or higher
      } else {
        return false; // Stand if dealer shows 2-6
      }
    }
  } else {
    // Soft hand strategy (with ace counted as 11)
    if (playerTotal <= 17) {
      return true;
    } else {
      return false;
    }
  }
}

// Example usage:
const playerTotal = 16;
const dealerCard = 10;
const isSoftHand = false; // true if hand includes an Ace counted as 11

if (shouldPlayerHit(playerTotal, dealerCard, isSoftHand)) {
  console.log("Player should Hit");
} else {
  console.log("Player should Stand");
}

class MathOperations {
  add(a, b) {
    return a + b;
  }

  subtract(a, b) {
    return a - b;
  }

  multiply(a, b) {
    return a * b;
  }

  divide(a, b) {
    if (b === 0) {
      throw new Error("Division by zero");
    }
    return a / b;
  }

  power(a, b) {
    return Math.pow(a, b);
  }

  sqrt(a) {
    if (a < 0) {
      throw new Error("Square root of negative number");
    }
    return Math.sqrt(a);
  }
}

const math = new MathOperations();
console.log(math.add(5, 3)); // 8
console.log(math.divide(10, 2)); // 5
console.log(math.sqrt(16)); // 4

function generateGradient() {
  const angle = Math.floor(Math.random() * 360);
  const color1 = `hsl(${Math.floor(Math.random() * 360)}, 70%, 50%)`;
  const color2 = `hsl(${Math.floor(Math.random() * 360)}, 70%, 50%)`;
  return `linear-gradient(${angle}deg, ${color1}, ${color2})`;
}

console.log(generateGradient());


import mathIndoction

function factorial2(n) {
  if (n < 0) return undefined // not responding
}

function factorial(n) {
  if (n < 0) return undefined; // Factorial not defined for negative numbers
  if (n === 0 || n === 1) return 1;
  return n * factorial(n - 1);
}

// Example usage:
console.log(factorial(5)); // Output: 120

function solveNQueens(N) {
  const solutions = [];
  const positions = new Array(N).fill(-1);

  function isSafe(row, col) {
    for (let i = 0; i < row; i++) {
      const prevCol = positions[i];
      // Check same column or diagonals
      if (prevCol === col || Math.abs(prevCol - col) === Math.abs(i - row)) {
        return false;
      }
    }
    return true;
  }

  function backtrack(row = 0) {
    if (row === N) {
      solutions.push([...positions]);
      return;
    }
    for (let col = 0; col < N; col++) {
      if (isSafe(row, col)) {
        positions[row] = col;
        backtrack(row + 1);
        // backtrack


import threading
import requests
from bs4 import BeautifulSoup
import queue

# List of URLs to scrape
urls = [
    'https://example.com/page1',
    'https://example.com/page2',
    'https://example.com/page3',
    # Add more URLs as needed
]

# Thread worker function
def fetch_and_parse(q, results):
    while True:
        url = q.get()
        if url is None:
            break
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')


<script>
  // Function to display a greeting message
  function greetUser() {
    alert('Hello! Welcome to my website.');
  }

  // Add event listener to the button after the DOM loads
  document.addEventListener('DOMContentLoaded', function() {
    const button = document.querySelector('button');
    if (button) {
      button.addEventListener('click', greetUser);
    }
  });
</script>

// Define a class called Person
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log(`Hello, my name is ${this.name} and I'm ${this.age} years old.`);
  }
}

// Create an instance of Person
const person1 = new Person('Alice', 25);
person1.greet(); // Output: Hello, my name is Alice and I'm 25 years old.

describe("tests", function() {
    const {assert, config} = require('chai');
    config.truncateThreshold = 0;

    it("Sample tests", function() {
      assert.strictEqual(new Num(123) + new Num(123), 246);
      assert.strictEqual(new Num(15) + new Num(15) + 5, 35);
      assert.strictEqual(new Num(1) * new Num(0) + 5, 5);
      assert.strictEqual(new Num(1) - new Num(10), -9);
      assert.strictEqual(new Num(0) + new Num(0) + 0, 0);
      assert.strictEqual(Math.floor(new Num(5.5)), Math.floor(5.5));
      assert.strictEqual(new Num(100).toString(), "The number is 100")
      assert.strictEqual(new Num(150).valueOf().num, 150, "new Num(150).valueOf().num should be 150")
      assert.typeOf(new Num(150), "object", "typeof new Num should be object")
      assert.typeOf(new Num(150).valueOf().num, "number")
    });
});

const {assert} = require('chai')

describe('Fixed tests', function () {

  describe('Examples', function () {
    it('Single raffle: 1 ticket out of 3', function () {
      assert.strictEqual(raffleOdds([3], [1]), '1/3');
    });

    it('Two raffles: 1 ticket each out of 4', function () {
      assert.strictEqual(raffleOdds([4, 4], [1, 1]), '7/16');
    });

    it('Three raffles with different pool sizes', function () {
      assert.strictEqual(raffleOdds([2, 3, 6], [1, 1, 1]), '13/18');
    });
  });
  
});

// Advanced prime number generator using segmented sieve and wheel factorization
function generatePrimes(limit) {
    if (limit < 2) return [];

    const sqrtLimit = Math.sqrt(limit) | 0;
    const basePrimes = simpleSieve(sqrtLimit);
    const segmentSize = Math.max(sqrtLimit, 32768);
    const primes = [...basePrimes]; // initial primes

    let low = sqrtLimit + 1;
    let high = low + segmentSize - 1;

    while (low <= limit) {
        if (high > limit) high = limit;

        const mark = new Uint8Array(high - low + 1);

        for (let i = 0; i < basePrimes.length; i++) {
            const p = basePrimes[i];
            // Find the start point to mark multiples of p
            let start = Math.ceil(low / p) * p;
            if (start < p * p) start = p * p;
            for (let j = start; j <= high; j += p) {
                mark[j - low] = 1; // mark as composite
