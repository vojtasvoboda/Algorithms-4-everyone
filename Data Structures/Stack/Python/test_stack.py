"""Test module for stack.py"""

import unittest
from random import randrange
from stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(randrange(10))
        self.assertEqual(len(self.stack), 1)

        self.stack.push(randrange(10))
        self.assertEqual(len(self.stack), 2)

    def test_pop(self):
        self.assertRaises(IndexError, self.stack.pop)

        self.stack.push('a')
        self.stack.push('b')
        self.stack.push('c')
        popped_item = self.stack.pop()
        self.assertEqual(popped_item, 'c')
        self.assertEqual(len(self.stack), 2)

    def test_peek(self):
        self.assertRaises(IndexError, self.stack.peek)

        self.stack.push('a')
        self.stack.push('b')
        self.stack.push('c')
        peeked_item = self.stack.peek()
        self.assertEqual(peeked_item, 'c')
        self.assertEqual(len(self.stack), 3)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())

        self.stack.push(randrange(10))
        self.assertFalse(self.stack.is_empty())

    def test_search(self):
        self.stack.push('a')
        self.stack.push('b')
        self.stack.push('c')
        index = self.stack.find('b')
        self.assertEqual(index, 1)

        index = self.stack.find('c')
        self.assertEqual(index, 2)

    def test_str(self):
        hello = ['h', 'e', 'l', 'l', 'o']
        for char in hello:
            self.stack.push(char)
        self.assertEqual(str(hello), str(self.stack))

        hello.append('world')
        self.stack.push('world')
        self.assertEqual(str(hello), str(self.stack))

if __name__ == '__main__':
    unittest.main()
