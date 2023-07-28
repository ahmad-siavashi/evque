from .evque import EvQueue

# Create a singleton instance of EventQueue
event_queue = EvQueue()

# Expose the functions directly from the singleton instance
subscribe = event_queue.subscribe
publish = event_queue.publish
run_until = event_queue.run_until
empty = event_queue.empty

