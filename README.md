# SmartCache

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

SmartCache is a high-performance, thread-safe object caching library for Python applications. It provides a simple yet powerful API for caching objects with configurable time-to-live (TTL) and automatic cleanup of expired items.

## Features

- 🚀 **Thread-safe** caching implementation
- ⏱️ **Configurable TTL** (Time To Live) for cached items
- 🔄 **Automatic cleanup** of expired cache entries
- 🔍 **Key-based** and **ID-based** item retrieval
- 🏗️ **Builder pattern** for easy cache item creation
- 📊 **Monitoring** of cache operations and statistics
- 🔄 **Background thread** for periodic cleanup
- 🧪 **Fully typed** for better development experience

## Installation

```bash
pip install git+https://github.com/louisgoodnews/SmartCache.git
```

## Quick Start

```python
from smartcache import CacheService

# Initialize the cache service with default TTL of 300 seconds (5 minutes)
cache = CacheService(time_to_live=300)

# Add an item to the cache
item_id = cache.add("my_cached_value", time_to_live=60)  # Cache for 60 seconds

# Retrieve the item
cached_value = cache.get(item_id)
print(f"Cached value: {cached_value}")

# Remove an item from the cache
cache.remove(item_id)
```

## Advanced Usage

### Using the Builder Pattern

```python
from smartcache import CacheItemBuilder

# Create a cache item using the builder pattern
cache_item = (
    CacheItemBuilder()
    .with_value({"user_id": 123, "name": "John Doe"})
    .with_time_to_live(3600)  # 1 hour
    .build()
)

# Add to cache
cache.set(cache_item)
```

### Cache Statistics

```python
# Get the current cache size
size = cache.size()
print(f"Current cache size: {size} items")

# Get the last operation timestamp
last_op = cache.last_operation_at
print(f"Last operation at: {last_op}")
```

## Documentation

### CacheService

The main class that provides the caching functionality.

#### Methods

- `add(value: Any, time_to_live: int = 300) -> int`: Add an item to the cache
- `get(key: int) -> Optional[Any]`: Retrieve an item by its ID
- `get_by_key(key: str) -> Optional[CacheItem]`: Retrieve an item by its key
- `remove(key: int) -> None`: Remove an item from the cache
- `size() -> int`: Get the current number of items in the cache
- `shutdown() -> None`: Gracefully stop the background cleanup thread

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on how to submit pull requests, report issues, or suggest improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Louis Goodnews - [@louisgoodnews](https://github.com/louisgoodnews) - louisgoodnews95@gmail.com

Project Link: [https://github.com/louisgoodnews/Cacheing](https://github.com/louisgoodnews/Cacheing)

## Acknowledgments

- Built using Python
- Uses [DateUtil](https://github.com/louisgoodnews/DateUtil) for date/time operations
- Uses [Logger](https://github.com/louisgoodnews/Logger) for logging

---

<div align="center">
  Made by Louis Goodnews
</div>
