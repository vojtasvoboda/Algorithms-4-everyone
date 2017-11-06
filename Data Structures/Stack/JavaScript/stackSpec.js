const chai = require('chai')
const Stack = require('./stack')

describe('Stack', function () {
  let stack;

  beforeEach(function () {
    chai.should();
    stack = new Stack();
  })

  context('when pushing', function () {
    it('should add the item at the top of the stack', function () {
      stack.push('a');
      stack.length().should.equal(1);
      stack.push('b');
      stack.length().should.equal(2);
    })
  })

  context('when popping', function () {
    it('should remove and return the top element', function () {
      stack.push('a');
      stack.push('b');
      stack.push('c');
      const poppedElement = stack.pop();
      poppedElement.should.equal('c');
      stack.length().should.equal(2);
    })

    it('should return undefined if stack is empty', function () {
      const poppedElement = stack.pop();
      (poppedElement === undefined).should.be.true;
    })
  })

  context('when peeking', function () {
    it('should return the top element', function () {
      stack.push('a');
      stack.push('b');
      stack.push('c');
      const peekedElement = stack.peek();
      peekedElement.should.equal('c');
      stack.length().should.equal(3);
    })

    it('should return undefined if stack is empty', function () {
      const peekedElement = stack.peek();
      (peekedElement === undefined).should.be.true;
    })
  })

  context('when checking if empty', function () {
    it('should return true if empty', function () {
      stack.isEmpty().should.be.true;
    })

    it('should return false if not empty', function () {
      stack.push(Math.random());
      stack.isEmpty().should.be.false;
    })
  })

  context('when searching', function () {
    it('should return the first index of the item if found', function () {
      stack.push('a');
      stack.push('b');
      stack.push('c');
      stack.push('b');
      stack.push('c');
      stack.search('b').should.equal(1);
      stack.search('c').should.equal(2);
    })

    it('should return -1 if not found', function () {
      stack.search('b').should.equal(-1);
    })
  })

  context('when converting to string', function () {
    it('should return a string with all the elements', function () {
      stack.push('a');
      stack.push('b');
      stack.push(1);
      stack.push(2);
      const strStack = stack.stackToString();
      strStack.should.equal('a,b,1,2');
    })
  })
})
