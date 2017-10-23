class Stack {
  constructor() {
    this.stackList = [];
  }

  length() {
    return this.stackList.length;
  }

  push(item) {
    return this.stackList.push(item);
  }

  pop() {
    return this.stackList.pop();
  }

  peek() {
    return this.stackList[this.length() - 1];
  }

  isEmpty() {
    return this.length() === 0;
  }

  search(item) {
    return this.stackList.indexOf(item);
  }

  stackToString() {
    return this.stackList.toString();
  }
}

module.exports = Stack;