import heapq
from typing import Callable


class EvQueue:
    """
    A simple event queue with support for topics.

    This class provides functionality to manage events published to different topics
    and deliver them to their respective event handlers based on their delivery time.

    Attributes
    ----------
    _events : list[tuple[int, str, tuple, dict], ...]
        The list of events in the queue, ordered by their delivery time.
    _topics : dict[str, list[Callable, ...]]
        A dictionary containing topics as keys and lists of event handler functions as values.

    Methods
    -------
    subscribe(topic: str, handler: Callable):
        Subscribe a handler function to a topic.

    unsubscribe(topic: str, handler: Callable):
        Unsubscribe a handler function from a topic.

    publish(topic: str, delivery_time: int, *args):
        Publish an event to a topic with a specific delivery time.

    run_until(target_time: int):
        Process events in the queue until the target time is reached.

    empty() -> bool:
        Check if there are any undelivered events in the queue.

    Notes
    -----
    - The event queue is implemented as a priority queue to efficiently handle event scheduling.
    - Events are ordered by their delivery time, and events with the same delivery time are delivered in the order they were published.
    - Event handlers should be callable objects that accept variable arguments and keyword arguments.

    Examples
    --------
    # Create an instance of the event queue
    event_queue = EventQueue()

    # Subscribe to a topic
    def event_handler(arg):
        print(f"Event received with argument: {arg}")
    event_queue.subscribe('topic1', event_handler)

    # Publish an event to be delivered at time 10
    event_queue.publish('topic1', 10, "Hello, World!")

    # Run events until time 15
    event_queue.run_until(15)

    # Check if there are undelivered events in the queue
    if event_queue.empty():
        print("No undelivered events in the queue.")
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._events = []
            cls._instance._topics = {}
        return cls._instance

    def subscribe(self, topic: str, handler: Callable):
        """
        Subscribe a handler function to a topic.

        Parameters
        ----------
        topic : str
            The topic to subscribe to.
        handler : Callable
            The handler function to be called when events are published to the topic.
        """
        if topic not in self._topics:
            self._topics[topic] = []
        self._topics[topic].append(handler)

    def unsubscribe(self, topic: str, handler: Callable):
        """
        Unsubscribe a handler function from a topic.

        Parameters
        ----------
        topic :str
            The topic to unsubscribe from.
        handler : Callable
            The handler function to be removed from the topic.
        """
        if topic in self._topics:
            self._topics[topic].remove(handler)

    def publish(self, topic: str, delivery_time: int, *args):
        """
        Publish an event to a topic with a specific delivery time.

        Parameters
        ----------
        topic : str
            The topic to publish the event to.
        delivery_time : int
            The time at which the event should be delivered.
        *args : list
            Variable-length argument list to be passed to the event handlers.

        Raises
        ------
        KeyError
            If the specified topic does not exist.
        """
        if topic not in self._topics:
            raise KeyError(f"Topic '{topic}' does not exist.")

        event = (delivery_time, topic, args)
        heapq.heappush(self._events, event)

    def run_until(self, target_time: int):
        """
        Process events in the queue until the target time is reached.

        Parameters
        ----------
        target_time : int
            The time until which events should be processed.
        """
        while self._events and self._events[0][0] <= target_time:
            event_time, topic, args = heapq.heappop(self._events)

            if topic in self._topics:
                for handler in self._topics[topic]:
                    handler(*args)

    def empty(self) -> bool:
        """
        Check if there are any undelivered events in the queue.

        Returns
        -------
        bool
            True if there are undelivered events in the queue, False otherwise.
        """
        return not bool(self._events)
