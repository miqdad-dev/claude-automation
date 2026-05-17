import unittest
from consumer import Consumer

class TestConsumer(unittest.TestCase):
    def setUp(self):
        self.consumer = Consumer()

    def test_fib(self):
        self.assertEqual(self.consumer.fib(0), 0)
        self.assertEqual(self.consumer.fib(1), 1)
        self.assertEqual(self.consumer.fib(2), 1)
        self.assertEqual(self.consumer.fib(3), 2)
        self.assertEqual(self.consumer.fib(5), 5)
        self.assertEqual(self.consumer.fib(10), 55)

if __name__ == '__main__':
    unittest.main()