import unittest
from producer import Producer

class TestProducer(unittest.TestCase):
    def setUp(self):
        self.producer = Producer()

    def test_call(self):
        self.assertEqual(self.producer.call(1), 1)
        self.assertEqual(self.producer.call(2), 1)
        self.assertEqual(self.producer.call(3), 2)
        self.assertEqual(self.producer.call(5), 5)
        self.assertEqual(self.producer.call(10), 55)

if __name__ == '__main__':
    unittest.main()