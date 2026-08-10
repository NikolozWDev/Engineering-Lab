const array = [primary_numbers]

<script>
  document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.createElement('input');
    searchInput.type = 'text';
    searchInput.placeholder = 'Search projects...';
    searchInput.style.marginBottom = '10px';

    // Insert the search box at the top of the projects section
    const projectsSection = document.querySelector('section:nth-of-type(3)');
    projectsSection.insertBefore(searchInput, projectsSection.firstChild);

    // Select all project articles
    const projectArticles = projectsSection.querySelectorAll('article');

    // Add input event listener for real-time filtering
    searchInput.addEventListener('input', () => {
      const searchTerm = searchInput.value.toLowerCase();

      projectArticles.forEach(article => {
        const title = article.querySelector('h3').textContent.toLowerCase();
        const description = article.querySelector('p').textContent.toLowerCase();

        if (title.includes(searchTerm) || description.includes(searchTerm)) {
          article.style.display = '';
        } else {
          article.style.display = 'none';
        }
      });
    });
  });
</script>

no problems resolved
describe("Example tests", function() {
  it("Basic tests", function() {
    assert.strictEqual(solve("codewars", 1, 5), "cawedors");
    assert.strictEqual(solve("codingIsFun", 2, 100), "conuFsIgnid");
    assert.strictEqual(solve("FunctionalProgramming", 2, 15), "FuargorPlanoitcnmming");
    assert.strictEqual(solve("abcdefghijklmnopqrstuvwxyz", 0, 20), "utsrqponmlkjihgfedcbavwxyz");
    assert.strictEqual(solve("abcdefghijklmnopqrstuvwxyz", 5, 20), "abcdeutsrqponmlkjihgfvwxyz");
  });
});

  for (let test of tests) {
    
    it(`Words: ${test.array}; character: '${test.character}'`, function() {
    
      let userResult = frame(test.array,test.character);
      test.test = userResult === test.output;
      if (!test.test) {
        console.log(`<LOG::Input>Array:\n  [${test.array.map(w => `"${w}"`).join(', ')}]\nCharacter: '${test.character}'`.replace('\n', '<:LF:>'));
        console.log(`<LOG::Expected>${test.output.replace('\n', '<:LF:>')}\n`);
        console.log(`<TAB::Actual>${(userResult || '[no result]').replace('\n', '<:LF:>')}\n`);
      }
      assert(test.test, "Your result is not a correct frame");
    });
  }

function Warrior(n){
  this._name = n;
  this.name = function(n){
    if(n) this._name = n;
    return this._name;
  }
}

Warrior.prototype.toString = function(){
  return "Hi! my name's " + this.name();
}

const Test = require('@codewars/test-compat');

describe("Tests", () => {
  it("test", () => {
var game = new SnakesLadders();
Test.assertEquals(game.play(1, 1), "Player 1 is on square 38", "Should return: 'Player 1 is on square 38'");
Test.assertEquals(game.play(1, 5), "Player 1 is on square 44", "Should return: 'Player 1 is on square 44'");
Test.assertEquals(game.play(6, 2), "Player 2 is on square 31", "Should return: 'Player 2 is on square 31'");
Test.assertEquals(game.play(1, 1), "Player 1 is on square 25", "Should return: 'Player 1 is on square 25'");
  });
});

const { assert } = require('chai');

describe("Silly addition", () => {
  it("Real addition", () => {
    assert.strictEqual(add(2, 11), 13);
    assert.strictEqual(add(0, 1), 1);
    assert.strictEqual(add(0, 0), 0);
  });
  
  it("Silly addition", () => {
    assert.strictEqual(add(16, 18), 214);
    assert.strictEqual(add(26, 39), 515);
    assert.strictEqual(add(122, 81), 1103);
  });
  
  it("Big addition", () => {
    assert.strictEqual(add(1222, 30277), 31499);
    assert.strictEqual(add(1236, 30977), 31111013);
    assert.strictEqual(add(38810, 1383), 391193);
    assert.strictEqual(add(49999, 49999), 818181818);
  });
});


const assert = require('assert');

describe("Basic tests", function() {
  describe("correct sequence of arrows", function() {
    it("dec_arrow_pin_code('1→↑→')  ==>  [1, 2, 5, 6]", function() {
      assert.deepStrictEqual(decArrowPinCode("1→↑→"), [1, 2, 5, 6]);
    });
    it("dec_arrow_pin_code('1*2↓')  ==>  [1, 1, 1, 0]", function() {
      assert.deepStrictEqual(decArrowPinCode("1*2↓"), [1, 1, 1, 0]);
    });
    it("dec_arrow_pin_code('0*2↑')  ==>  [0, 0, 0, 1]", function() {
      assert.deepStrictEqual(decArrowPinCode("0*2↑"), [0, 0, 0, 1]);
    });
    it("dec_arrow_pin_code('0↑↑↑')  ==>  [0, 1, 4, 7]", function() {
      assert.deepStrictEqual(decArrowPinCode("0↑↑↑"), [0, 1, 4, 7]);
    });
  });
