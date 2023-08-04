import unittest

from evque import EvQue


class TestEvQueue(unittest.TestCase):
    def setUp(self):
        self.ev_queue = EvQue()

    def test_singleton(self):
        another_ev_queue = EvQue()
        self.assertIs(self.ev_queue, another_ev_queue)

    def test_subscribe_unsubscribe(self):
        def handler(arg):
            pass

        # No handlers subscribed yet
        with self.assertRaises(ValueError):
            self.ev_queue.unsubscribe('topic1', handler)

        # Subscribe
        self.ev_queue.subscribe('topic1', handler, handler)
        self.assertIn('topic1', self.ev_queue._topics)
        self.assertIn(handler, self.ev_queue._topics['topic1'])

        # Unsubscribe
        self.ev_queue.unsubscribe('topic1', handler, handler)
        self.assertNotIn(handler, self.ev_queue._topics['topic1'])

    def test_publish_run_until(self):
        self.result = None

        def handler(arg):
            self.result = arg

        self.ev_queue.subscribe('topic1', handler)

        # Before publish
        self.assertIsNone(self.result)
        self.assertTrue(self.ev_queue.empty())

        # Publish
        self.ev_queue.publish('topic1', 10, 'Hello, World!')
        self.assertFalse(self.ev_queue.empty())

        # Before run_until
        self.assertIsNone(self.result)

        # run_until
        self.ev_queue.run_until(15)
        self.assertEqual(self.result, 'Hello, World!')
        self.assertTrue(self.ev_queue.empty())

    def test_empty(self):
        self.result = None

        def handler(arg):
            self.result = arg

        self.ev_queue.subscribe('topic1', handler)
        self.ev_queue.publish('topic1', 10, 'Hello, World!')

        self.assertFalse(self.ev_queue.empty())

        self.ev_queue.run_until(5)  # Not yet delivered
        self.assertFalse(self.ev_queue.empty())

        self.ev_queue.run_until(10)  # Delivered
        self.assertTrue(self.ev_queue.empty())


if __name__ == "__main__":
    unittest.main()
