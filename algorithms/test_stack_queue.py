import unittest
from stack_queue import Queue, Stack


class StackQueueTests(unittest.TestCase):
    def test_stack_lifo(self):
        stack = Stack([1, 2])
        stack.push(3)
        self.assertEqual(stack.peek(), 3)
        self.assertEqual([stack.pop(), stack.pop(), stack.pop()], [3, 2, 1])
        self.assertFalse(stack)
        with self.assertRaises(IndexError):
            stack.pop()

    def test_queue_fifo(self):
        queue = Queue([1, 2])
        queue.enqueue(3)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual([queue.dequeue(), queue.dequeue(), queue.dequeue()], [1, 2, 3])
        self.assertEqual(len(queue), 0)
        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_empty_peek(self):
        for structure in (Stack(), Queue()):
            with self.assertRaises(IndexError):
                structure.peek()


if __name__ == "__main__":
    unittest.main()
