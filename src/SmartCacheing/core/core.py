"""
Author: Louis Goodnews
Date: 2025-08-09
"""

import time

from datetime import datetime
from threading import Event, RLock, Thread
from typing import Any, Dict, Final, List, Optional, Self

from DateUtil import DateUtil
from Logger import Logger


__all__: Final[List[str]] = [
    "CacheItem",
    "Cache",
    "CacheService",
]


class CacheItem:
    """
    A cache item.

    This class is used to store a cache item.

    Attributes:
        created_at (datetime): The created at time datetime object.
        expires_at (datetime): The expires at time datetime object.
        id (int): The id of the cache item.
        time_to_live (int): The time to live in seconds.
        value (Any): The value of the cache item.
    """

    def __init__(
        self,
        id: int,
        time_to_live: int,
        value: Any,
    ) -> None:
        """
        Initialize the cache item.

        :param id: The id of the cache item
        :type id: int
        :param time_to_live: The time to live in seconds
        :type time_to_live: int
        :param value: The value of the cache item
        :type value: Any

        :return: None
        :rtype: None
        """

        # Store the created at time in a final variable
        self._created_at: Final[datetime] = DateUtil.now()

        # Calculate and store the expires at time in a final variable
        self._expires_at: datetime = DateUtil.increment(
            amount=time_to_live,
            obj=self._created_at,
            what="seconds",
        )

        # Store the id in a final variable
        self._id: Final[int] = id

        # Store the time to live in a final variable
        self._time_to_live: Final[int] = time_to_live

        # Store the value in a final variable
        self._value: Final[Any] = value

    @property
    def created_at(self) -> datetime:
        """
        Returns the created at time datetime object.

        :return: The created at time
        :rtype: datetime
        """

        # Return the created at time
        return self._created_at

    @property
    def expires_at(self) -> datetime:
        """
        Returns the expires at time datetime object.

        :return: The expires at time
        :rtype: datetime
        """

        # Return the expires at time
        return self._expires_at

    @expires_at.setter
    def expires_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the expires at time datetime object.

        :param value: The expires at time
        :type value: datetime

        :return: None
        :rtype: None
        """

        # Check if the expires at time is a past time
        if self._expires_at < value:
            # Log a warning message
            self._logger.warning(
                message="Expires at time cannot be set to a past time. Aborting."
            )

            # Return early if the expires at time is a past time
            return

        # Set the expires at time
        self._expires_at = value

    @property
    def id(self) -> int:
        """
        Returns the id of the cache item.

        :return: The id of the cache item
        :rtype: int
        """

        # Return the id
        return self._id

    @property
    def time_to_live(self) -> int:
        """
        Returns the time to live in seconds.

        :return: The time to live
        :rtype: int
        """

        # Return the time to live
        return self._time_to_live

    @property
    def value(self) -> Any:
        """
        Returns the value of the cache item.

        :return: The value of the cache item
        :rtype: Any
        """

        # Return the value
        return self._value

    def __contains__(
        self,
        key: str,
    ) -> bool:
        """
        Checks if the stored value contains the given key.

        Returns True if the value supports key-based lookup and the key exists,
        otherwise False.

        :param key: The key to search for
        :type key: str

        :return: True if key is present, False otherwise
        :rtype: bool
        """

        # Get the value
        value: Any = self._value

        # Check if the value supports key-based lookup
        if not hasattr(
            value,
            "__contains__",
        ):
            # Return False if the value does not support key-based lookup
            return False

        try:
            # Return True if the key is present, False otherwise
            return key in value
        except Exception:
            # Return False if the key is not present
            return False

    def __repr__(self) -> str:
        """
        Returns the string representation of the cache item.

        :return: The string representation of the cache item
        :rtype: str
        """

        # Return the string representation of the cache item
        return f"<CacheItem(created_at={self.created_at}, expires_at={self.expires_at}, id={self.id}, time_to_live={self.time_to_live}, value={self.value})>"

    def __str__(self) -> str:
        """
        Returns the string representation of the cache item.

        :return: The string representation of the cache item
        :rtype: str
        """

        # Return the string representation of the cache item
        return self.__repr__()

    def contains_key(
        self,
        key: str,
    ) -> bool:
        """
        Checks if the stored value contains the given key.

        Returns True if the value supports key-based lookup and the key exists,
        otherwise False.

        :param key: The key to search for
        :type key: str

        :return: True if key is present, False otherwise
        :rtype: bool
        """

        # Return the result of the comparison
        return self.__contains__(key=key)

    def get(self) -> Any:
        """
        Returns the value of the cache item.

        :return: The value of the cache item
        :rtype: Any
        """

        # Return the value
        return self._value

    def is_expired(self) -> bool:
        """
        Returns True if the cache item is expired, False otherwise.

        :return: True if the cache item is expired, False otherwise
        :rtype: bool
        """

        # Return True if the cache item is expired, False otherwise
        return DateUtil.now() > self._expires_at


class CacheItemFactory:
    """
    A factory class for creating cache items.
    """

    BASE_ID: int = 10000

    @classmethod
    def create(
        cls,
        value: Any,
        time_to_live: int = 300,
    ) -> CacheItem:
        """
        Creates a cache item.

        :param time_to_live: The time to live in seconds. Defaults to 300.
        :type time_to_live: int
        :param value: The value of the cache item
        :type value: Any

        :return: The cache item
        :rtype: CacheItem
        """

        # Return the cache item
        cache_item: CacheItem = CacheItem(
            id=cls.BASE_ID,
            time_to_live=time_to_live,
            value=value,
        )

        # Increment the base id
        cls.BASE_ID += 1

        # Return the cache item
        return cache_item


class CacheItemBuilder:
    """
    A builder class for creating cache items.

    This class is used to build cache items.
    """

    def __init__(self) -> None:
        """
        Initialize the builder.

        :return: None
        :rtype: None
        """

        # Initialize the configuration dict
        self._configuration: Final[Dict[str, Any]] = {}

    def build(self) -> CacheItem:
        """
        Builds the cache item.

        :return: The cache item
        :rtype: CacheItem
        """

        return CacheItemFactory.create(
            value=self._configuration["value"],
            time_to_live=self._configuration["time_to_live"],
        )

    def with_time_to_live(
        self,
        value: int,
    ) -> Self:
        """
        Sets the time to live of the cache item.

        :param value: The time to live in seconds
        :type value: int

        :return: The builder
        :rtype: Self
        """

        # Store the time to live
        self._configuration["time_to_live"] = value

        # Return the builder
        return self

    def with_value(
        self,
        value: Any,
    ) -> Self:
        """
        Sets the value of the cache item.

        :param value: The value of the cache item
        :type value: Any

        :return: The builder
        :rtype: Self
        """

        # Store the value
        self._configuration["value"] = value

        # Return the builder
        return self


class Cache:
    """
    A class for caching objects.

    This class is used to cache objects.

    Attributes:
        lock (RLock): The lock.
        logger (Logger): The logger.
        storage (Dict[int, CacheItem]): The storage.
    """

    def __init__(self) -> None:
        """
        Initialize the cache.

        :return: None
        :rtype: None
        """

        # Initialize the lock
        self._lock: Final[RLock] = RLock()

        # Initialize the logger
        self._logger: Final[Logger] = Logger.get_logger(name=self.__class__.__name__)

        # Initialize the storage
        self._storage: Final[Dict[int, CacheItem]] = {}

    @property
    def storage(self) -> Dict[int, CacheItem]:
        """
        Returns the storage of the cache.

        :return: The storage of the cache
        :rtype: Dict[int, CacheItem]
        """

        # Return the storage
        return self._storage

    def __contains__(
        self,
        key: int,
    ) -> bool:
        """
        Checks if the cache contains the given key.

        :param key: The key to check
        :type key: int

        :return: True if the cache contains the given key, False otherwise
        :rtype: bool
        """

        # Check if the cache contains the given key
        with self._lock:
            # Return True if the cache contains the given key, False otherwise
            return key in self._storage and not self._storage[key].is_expired()

    def __repr__(self) -> str:
        """
        Returns the string representation of the cache.

        :return: The string representation of the cache
        :rtype: str
        """

        # Return the string representation of the cache
        return f"<Cache(storage={self.storage})>"

    def __str__(self) -> str:
        """
        Returns the string representation of the cache.

        :return: The string representation of the cache
        :rtype: str
        """

        # Return the string representation of the cache
        return self.__repr__()

    def add(
        self,
        value: Any,
        time_to_live: int = 300,
    ) -> int:
        """
        Adds a cache item to the cache.

        :param value: The value of the cache item
        :type value: Any
        :param time_to_live: The time to live in seconds. Defaults to 300.
        :type time_to_live: int

        :return: The ID of the cache item
        :rtype: int
        """

        with self._lock:
            # Initialize the builder
            builder: CacheItemBuilder = CacheItemBuilder()

            # Set the value and time to live
            builder.with_value(value=value).with_time_to_live(time_to_live=time_to_live)

            # Build the cache item
            cache_item: CacheItem = builder.build()

            # Store the cache item under its ID
            self._storage[cache_item.id] = cache_item

            # Log the cache item addition
            self._logger.info(
                message=f"Cache item added with ID {cache_item.id} and time to live {cache_item.time_to_live} seconds"
            )

            # Return the ID of the cache item
            return cache_item.id

    def clear(self) -> None:
        """
        Clears the cache.

        :return: None
        :rtype: None
        """

        with self._lock:
            # Clear the storage
            self._storage.clear()

            # Log the cache clearing
            self._logger.info(message="Cache cleared")

    def get(
        self,
        key: int,
    ) -> Optional[CacheItem]:
        """
        Gets a cache item from the cache.

        :param key: The ID of the cache item
        :type key: int

        :return: The cache item or None if not found
        :rtype: Optional[CacheItem]
        """

        with self._lock:
            # Return the cache item or None if not found
            return self._storage.get(
                key,
                None,
            )

    def get_by_key(
        self,
        key: str,
    ) -> Optional[CacheItem]:
        """
        Gets a cache item from the cache by its key.

        :param key: The key of the cache item
        :type key: str

        :return: The cache item or None if not found
        :rtype: Optional[CacheItem]
        """

        # Check if the cache item exists
        with self._lock:
            # Return the cache item or None if not found
            return next(
                (
                    cache_item
                    for cache_item in self._storage.values()
                    if not cache_item.is_expired() and key in cache_item
                ),
                None,
            )

    def invalidate(
        self,
        key: int,
    ) -> None:
        """
        Invalidates a cache item in the cache.

        :param key: The ID of the cache item
        :type key: int

        :return: None
        :rtype: None
        """

        # Initialize the cache item to None
        cache_item: Optional[CacheItem] = None

        with self._lock:
            # Remove the cache item
            cache_item = self._storage.pop(
                key,
                None,
            )

        # Check if the cache item exists
        if not cache_item:
            # Log a warning message
            self._logger.warning(
                message=f"Cache item with ID {key} does not exist. Aborting invalidation."
            )

            # Return early if the cache item does not exist
            return

        # Log the cache item invalidation
        self._logger.info(message=f"Cache item invalidated with ID {key}")

    def invalidate_expired(self) -> None:
        """
        Invalidates expired cache items in the cache.

        :return: None
        :rtype: None
        """

        # Get the expired cache items
        expired_ids: List[int] = [
            cache_item.id
            for cache_item in self._storage.values()
            if cache_item.is_expired()
        ]

        # Check if there are expired cache items
        if len(expired_ids) == 0:
            # Log a warning message
            self._logger.warning(
                message="No expired cache items found. Aborting invalidation."
            )

            # Return early if no expired cache items are found
            return

        # Invalidate the expired cache items
        for expired_id in expired_ids:
            # Invalidate the cache item
            self.invalidate(key=expired_id)

        # Log the cache item invalidation
        self._logger.info(message="Expired cache items invalidated")

    def remove(
        self,
        key: int,
    ) -> None:
        """
        Removes a cache item from the cache.

        :param key: The ID of the cache item
        :type key: int

        :return: None
        :rtype: None
        """

        # Initialize the cache item to None
        cache_item: Optional[CacheItem] = None

        with self._lock:
            # Remove the cache item
            cache_item = self._storage.pop(
                key,
                None,
            )

        # Check if the cache item exists
        if not cache_item:
            # Log a warning message
            self._logger.warning(
                message=f"Cache item with ID {key} does not exist. Aborting removal."
            )

            # Return early if the cache item does not exist
            return

        # Log the cache item removal
        self._logger.info(message=f"Cache item removed with ID {key}")

    def set(
        self,
        value: CacheItem,
    ) -> None:
        """
        Sets a cache item in the cache.

        :param value: The cache item
        :type value: CacheItem

        :return: None
        :rtype: None
        """

        with self._lock:
            # Set the cache item
            self._storage[value.id] = value

        # Log the cache item setting
        self._logger.info(message=f"Cache item set with ID {value.id}")

    def size(self) -> int:
        """
        Returns the size of the cache.

        :return: The size of the cache
        :rtype: int
        """

        # Return the size of the cache
        return len(self._storage)


class CacheService:
    """
    A service for managing a cache.

    This service provides a thread-safe interface for managing a cache.
    It also provides a background thread for periodic cleanup of expired cache items.

    Attributes:
        last_operation_at (datetime): The last operation at time.
        logger (Logger): The logger.
        storage (Cache): The storage.
        stop_event (Event): The stop event.
        thread (Thread): The thread.
        time_to_live (int): The time to live.
    """

    def __init__(
        self,
        time_to_live: int = 300,
    ) -> None:
        """
        Initialize the cache service.

        :param time_to_live: The time to live in seconds. Defaults to 300.
        :type time_to_live: int

        :return: None
        :rtype: None
        """

        # Initialize the last operation at time
        self._last_operation_at: datetime = DateUtil.now()

        # Initialize the logger
        self._logger: Final[Logger] = Logger.get_logger(name=self.__class__.__name__)

        # Initialize the time to live
        self._time_to_live: Final[int] = time_to_live

        # Initialize the storage
        self._storage: Final[Cache] = Cache()

        # Initialize the stop event
        self._stop_event = Event()

        # Initialize the thread
        self._thread = Thread(
            daemon=True,
            target=self._periodic_cleanup,
        )

        # Start the thread
        self._thread.start()

        # Log the cache service start
        self._logger.info(
            message=f"CacheService started with cleanup interval {time_to_live} seconds"
        )

    @property
    def last_operation_at(self) -> datetime:
        """
        Returns the last operation at time of the cache service.

        :return: The last operation at time of the cache service
        :rtype: datetime
        """

        # Return the last operation at time
        return self._last_operation_at

    @last_operation_at.setter
    def last_operation_at(
        self,
        value: datetime,
    ) -> None:
        """
        Sets the last operation at time of the cache service.

        :param value: The last operation at time of the cache service
        :type value: datetime

        :return: None
        :rtype: None
        """

        # Check if the last operation at time is a past time
        if self._last_operation_at > value:
            # Log a warning message
            self._logger.warning(
                message="Last operation at time cannot be set to a past time. Aborting."
            )

            # Return early if the last operation at time is a past time
            return

        # Set the last operation at time
        self._last_operation_at = value

    @property
    def storage(self) -> Cache:
        """
        Returns the storage of the cache service.

        :return: The storage of the cache service
        :rtype: Cache
        """

        # Return the storage
        return self._storage

    def _periodic_cleanup(self) -> None:
        """
        Runs a periodic cleanup of the cache.

        :return: None
        :rtype: None
        """

        # Run the periodic cleanup
        while not self._stop_event.is_set():

            # Wait for the next cleanup interval
            time.sleep(float(self._time_to_live))

            # Log the periodic cache cleanup
            self._logger.debug(message="Running periodic cache cleanup")

            # Invalidate expired cache items
            self._storage.invalidate_expired()

            # Log the periodic cache cleanup completion
            self._logger.debug(message="Periodic cache cleanup completed")

            # Update the last operation at time
            self._last_operation_at = DateUtil.now()

    def add(
        self,
        value: Any,
        time_to_live: int = 300,
    ) -> int:
        """
        Adds a cache item to the cache.

        :param value: The value of the cache item
        :type value: Any
        :param time_to_live: The time to live in seconds. Defaults to 300.
        :type time_to_live: int

        :return: The ID of the cache item
        :rtype: int
        """

        # Add the cache item
        return self._storage.add(
            value=value,
            time_to_live=time_to_live,
        )

    def get(
        self,
        key: int,
    ) -> Optional[Any]:
        """
        Gets a cache item from the cache.

        :param key: The ID of the cache item
        :type key: int

        :return: The cache item or None if not found
        :rtype: Optional[Any]
        """

        # Get the cache item
        cacheitem: Optional[CacheItem] = self._storage.get(key=key)

        # Check if the cache item exists
        if not cacheitem:
            # Log a warning message
            self._logger.warning(
                message=f"Cache item with ID {key} does not exist. Aborting retrieval."
            )

            # Return early if the cache item does not exist
            return None

        # Return the cache item
        return cacheitem.value

    def get_by_key(
        self,
        key: str,
    ) -> Optional[CacheItem]:
        """
        Gets a cache item from the cache.

        :param key: The key of the cache item
        :type key: str

        :return: The cache item or None if not found
        :rtype: Optional[CacheItem]
        """

        # Check if the cache item exists
        if key not in self._storage:
            # Log a warning message
            self._logger.warning(
                message=f"Cache item with key {key} does not exist. Aborting retrieval."
            )

            # Return early if the cache item does not exist
            return None

        # Get the cache item
        return self._storage.get_by_key(key=key)

    def remove(
        self,
        key: int,
    ) -> None:
        """
        Removes a cache item from the cache.

        :param key: The ID of the cache item
        :type key: int

        :return: None
        :rtype: None
        """

        # Remove the cache item
        self._storage.remove(key=key)

    def shutdown(self) -> None:
        """
        Stops the background cleanup thread gracefully.

        :return: None
        :rtype: None
        """

        # Log the cache service shutdown initiation
        self._logger.info(message="CacheService shutdown initiated")

        # Set the stop event
        self._stop_event.set()

        # Wait for the thread to finish
        self._thread.join()

        # Log the cache service shutdown completion
        self._logger.info(message="CacheService shutdown complete")

    def size(self) -> int:
        """
        Returns the size of the cache.

        :return: The size of the cache
        :rtype: int
        """

        # Return the size of the cache
        return self._storage.size()
