# evque: Event Queue with Topics

[![PyPI version](https://badge.fury.io/py/evque.svg)](https://badge.fury.io/py/evque)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

**evque** is a Python library that provides a simple event queue with support for topics. It allows you to manage events published to different topics and deliver them to their respective event handlers based on their delivery time.

## Installation

You can install **evque** from PyPI using pip:

```bash
pip install evque
```

## Features

- **Event Queue:** Manage events and their delivery times in a priority queue.
- **Topic Support:** Subscribe and publish events to different topics.
- **Singleton Instance:** Share a single event queue instance across modules in your application.

## Usage

```python
from evque import subscribe, publish, run_until, empty, increase_clock, reset_clock, now

# Subscribe to a topic
def event_handler(arg):
    print(f"Event received with argument: {arg}")

subscribe('topic1', event_handler)

# Publish an event to be delivered at time 10
publish('topic1', 10, "Hello, World!")

# Run events until time 15
run_until(15)

# Check if there are undelivered events in the queue
if empty():
    print("No undelivered events in the queue.")
```

## License

This library is licensed under the GNU General Public License v3.0. For more details, see the [LICENSE.txt](https://github.com/ahmad-siavashi/evque/blob/main/LICENSE.txt) file.

## Contributing

Contributions to **evque** are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request on the [GitHub repository](https://github.com/ahmad-siavashi/evque).

## Acknowledgements

The "evque" library is inspired by the concept of event queues used in discrete event simulation and event-driven programming.
