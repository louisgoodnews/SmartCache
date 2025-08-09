"""
Author: Louis Goodnews
Date: 2025-08-09
"""

from core.core import Cache, CacheItem, CacheService


def main() -> None:
    """
    The main function.

    :return: None
    :rtype: None
    """

    # Create a cache service
    cache_service: CacheService = CacheService()

    # Add a cache item
    cache_service.add(
        key=1,
        value="Hello, World!",
    )

    # Get the cache item
    cache_item: CacheItem = cache_service.get_by_key(key=1)

    # Print the cache item
    print(cache_item)

    # Invalidate the cache item
    cache_service.invalidate(key=1)

    # Print the cache item
    print(cache_item)

    # Shutdown the cache service
    cache_service.shutdown()


if __name__ == "__main__":
    main()
