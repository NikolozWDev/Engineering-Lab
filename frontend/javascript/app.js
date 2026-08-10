creating edutech site for edutech academy
describe("Basic test",() => {
    const {assert, config} = require('chai');
    config.truncateThreshold = 0;

    before(function() {
        loadMyTemplateLanguage();
    });

    it("Existence of functions", () => {
      assert(typeof html === "function", "html() is not defined");
      assert(typeof head === "function", "head() is not defined");
      assert(typeof title === "function", "title() is not defined");
      assert(typeof body === "function", "body() is not defined");
      assert(typeof script === "function", "script() is not defined");
      assert(typeof link === "function", "link() is not defined");
      assert(typeof div === "function", "div() is not defined");
      assert(typeof span === "function", "span() is not defined");
      assert(typeof img === "function", "img() is not defined");
      assert(typeof br === "function", "br() is not defined");
      assert(typeof hr === "function", "hr() is not defined");
    });

    it('sample tests', function() {
// https://github.com/codewars/codewars.com/issues/3168
      assert.strictEqual(
        html({},[
            head({},[
            title({},['Hello, world!']),
            script({
              type:'text/javascript',
                    src:'js/index.js'
                }),
                link({
                    rel:'stylesheet',
                    href:'css/style.css'
                })
          ]),
            body({},[
                'Hello, world!'
            ])
        ])
      ,'<html><head><title>Hello, world!</title><script type="text/javascript" src="js/index.js"></script><link rel="stylesheet" href="css/style.css" /></head><body>Hello, world!</body></html>');
    });
});

import javascript
import random
const { assert } = require('chai');

describe("Tests", () => {
  it("test", () => {
    assert.strictEqual(area(5,4),12);
    assert.strictEqual(area(10,6),48);
    assert.strictEqual(area(13,5),60);
    assert.strictEqual(area(12,5),54.54);
  });
});

import codewars from codewars.com

chai.config.truncateThreshold=0;


describe("Sample tests", () => {
  it("Should pass sample tests", () => {
    assert.strictEqual(contamination("abc","z"), "zzz")
    assert.strictEqual(contamination("","z"), "")
    assert.strictEqual(contamination("abc",""), "")
    assert.strictEqual(contamination("_3ebzgh4","&"), "&&&&&&&&")
    assert.strictEqual(contamination("//case"," "), "      ")
  });
});

const { assert } = require("chai");

describe("Duel Ground", function() {
  
  const ERROR_MARGIN = 1e-6;
  
  function act(p, q, expected) {
    const actual = f(p, q)
        , msg = `p = ${p}, q = ${q}`;
    if (expected === null) {
      assert.isNull(actual, msg);
    } else {
      assert.isArray(actual, msg);
      assert.lengthOf(actual, 2, msg);
      for (let i = 0; i < expected.length; i++) {
        assert.isNumber(actual[i], msg);
        assert.approximately(actual[i], expected[i], ERROR_MARGIN, msg);
      }
    }
  }

const strictEqual = require('chai').assert.strictEqual;

function doTest(n, k, expected) {
  const actual = findKthNumber(n, k);
  strictEqual(actual, expected, `for input n = ${n}n, k = ${k}n`)
}

describe("Sample tests", () => {
  it("should return correct k-th number with same bits", () => {
    doTest(9n, 2n, 12n)
    doTest(17n, 2n, 20n)
    doTest(31n, 5n, 62n)
    doTest(1n, 1n, 2n)
  })
})

// added more features
const Test = require('@codewars/test-compat');

describe("Kata Tests",function(){
  it("Standard Tests", function(){
    var Goku = new Warrior();

const { assert } = require('chai');

describe('Example tests', () => {
  it('should test knight moves', () => {
    let arr = [['a1', 'c1', 2], ['a1', 'f1', 3], ['a1', 'f3', 3], ['a1', 'f4', 4], ['a1', 'f7', 5]];
    for (let i of arr) assert.equal(knight(i[0], i[1]), i[2], `knight('${i[0]}', '${i[1]}') should return ${i[2]}`);
  });
});

const { assert } = require('chai');

describe("Example tests", function() {
    it("should pass basic tests", function() {
        assert.strictEqual(finance(5), 105);
        assert.strictEqual(finance(6), 168);
        assert.strictEqual(finance(8), 360);
        assert.strictEqual(finance(15), 2040);
    });
});

const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("Framed Reflection", () => {
  it("Fixed tests", () => {
    assert.strictEqual(mirror('Hello World'), '*********\n* olleH *\n* dlroW *\n*********');
    assert.strictEqual(mirror('Codewars'), '************\n* srawedoC *\n************'); 
  })
});

npm install -g serve
serve -s build
npm install
npm run build
npm create vite@latest AI-chat --template react

function increment(n) {return n + 1};
function id(n) {return n};
function sqr(n) {return n * n};

const naturalNumbers = new Stream(0, id, increment);

console.log(naturalNumbers.head()) // 0
console.log(naturalNumbers.tail().head()) // 1
console.log(naturalNumbers.tail().tail().head()) // 2


working with react and state, props AI-chat
finished projects and uploaded it
tailwindcss is worst
added react Django rest project
solved tasks
solved 6kyu tasks
added 6kyu logic
javascript added
worked fullstackweb-project
data- attribute and JS logic
adding JS in back-end
changed and adding logics in JS
changed another device

added game
made algorithms
made good things

finished last project ordinary modifing app.js organized code and 
added some tools modified it
refined evertything
added modified ~ \/
s
Exit
10 % 10


app.js
modified


<<<<<<< HEAD

back-end modified1


document.querySelector('#jeimi').classList.add('openbar')


modified2

modified3 dev2
=======
modified (another pc) (fixed)

new branch :
(modified file)
(update app.js again and fixed all problem)
>>>>>>> 8048768592b5b4b47f48feb85f9c0972163c6ee8


Modified app.js and added object functions


learning JS

modified and starting to add more tools
find to write a code
