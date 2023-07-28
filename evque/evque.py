from dataclasses import dataclass, field
from typing import Callable
import heapq

__all__ = ['evque']

class EvQueue:
    '''
    A simple event queue with support for topics.
    
    Parameters
    ----------
    _instance: keeps the only created instance of the class
    '''
    
    _instance = None
    
    def __new__(cls):
        '''
        This class is overriden to enforce a singleton pattern.
        '''
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
        topic : str
            The topic to unsubscribe from.
        handler : Callable
            The handler function to be removed from the topic.
        """
        if topic in self._topics:
            self._topics[topic].remove(handler)


    def publish(self, topic: str, delivery_time: float, *args, **kwargs):
        """
        Publish an event to a topic with a specific delivery time.

        Parameters
        ----------
        topic : str
            The topic to publish the event to.
        delivery_time : float
            The time at which the event should be delivered.
        *args : list
            Variable-length argument list to be passed to the event handlers.
        **kwargs : dict
            Arbitrary keyword arguments to be passed to the event handlers.

        Raises
        ------
        KeyError
            If the specified topic does not exist.
        """
        if topic not in self._topics:
            raise KeyError(f"Topic '{topic}' does not exist.")

        event = (delivery_time, topic, args, kwargs)
        heapq.heappush(self._events, event)


    def run_until(self, target_time: float):
        """
        Process events in the queue until the target time is reached.

        Parameters
        ----------
        target_time : float
            The time until which events should be processed.
        """
        while self._events and self._events[0][0] <= target_time:
            event_time, topic, args, kwargs = heapq.heappop(self._events)

            if topic in self._topics:
                for handler in self._topics[topic]:
                    handler(*args, **kwargs)


    def empty(self, ) -> bool:
        """
        Check if there are any undelivered events in the queue.

        Returns
        -------
        bool
            True if there are undelivered events in the queue, False otherwise.
        """
        return not bool(self._events)

# Create a singleton instance of EventQueue
evque = EvQueue()
