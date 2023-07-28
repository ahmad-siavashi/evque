# evque

**evque** is a simple event queue library with support for topics. It provides functionality to manage events published to different topics and deliver them to their respective event handlers based on their delivery time.

## Installation

You can install **evque** using `pip`:

```bash
pip install evque
```

## Usage

### Importing the Library

```python
from evque import subscribe, unsubscribe, publish, run_until, empty
```

### Subscribing to a Topic

```python
def event_handler_1(arg1, arg2):
    print(f"Event handler 1 called with arguments: {arg1}, {arg2}")

def event_handler_2():
    print("Event handler 2 called without arguments")

subscribe("topic_a", event_handler_1)
subscribe("topic_a", event_handler_2)
```

### Unsubscribing from a Topic

```python
unsubscribe("topic_a", event_handler_1)
```

### Publishing an Event

```python
publish("topic_a", delivery_time=10.0, arg1=42, arg2="hello")
```

### Processing Events

```python
run_until(15.0)
```

### Checking if Events Queue is Empty

```python
if empty():
    print("No pending events.")
else:
    print("There are undelivered events in the queue.")
```

## Examples

```python
from evque import subscribe, publish, run_until, empty

# Define event handlers
def greet(name):
    print(f"Hello, {name}!")

def farewell(name):
    print(f"Goodbye, {name}!")

# Subscribe handlers to topics
subscribe("greetings", greet)
subscribe("farewells", farewell)

# Publish events to topics
publish("greetings", delivery_time=5.0, name="Alice")
publish("farewells", delivery_time=10.0, name="Bob")

# Process events
run_until(6.0)  # This will trigger the "greet" event
run_until(15.0)  # This will trigger both "greet" and "farewell" events

# Check if the queue is empty
if empty():
    print("All events processed.")
else:
    print("There are undelivered events in the queue.")
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.txt](LICENSE.txt) file for details.