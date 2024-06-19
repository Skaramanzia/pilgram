import logging
import time
from typing import Dict, Any, Tuple


__VALUE, __TTL = (0, 1)

log = logging.getLogger(__name__)


def cache_ttl_quick(ttl=3600):
    def decorator(func):
        storage: Dict[Any, Tuple[Any, float]] = {}

        def wrapper(*args, **kwargs):
            try:
                # Generate a key based on arguments being passed
                key = args
                # if value is cached and isn't expired then return
                if key in storage:
                    cache_record = storage[key]
                    if cache_record[__TTL] > time.time():
                        return cache_record[__VALUE]
                # calculate value
                result = func(*args, **kwargs)
                # add value to storage and return the resulting value
                storage[key] = (result, time.time() + ttl)
                return result
            except Exception as e:
                log.exception(f"Exception when accessing cache_ttl_quick: {e}")
                return func(*args, **kwargs)
        return wrapper
    return decorator


def __get_oldest_key(storage: dict, ttl: float):
    oldest_time = time.time() + (ttl * 2)
    oldest_key = None
    for key, record in storage.items():
        if record[__TTL] < oldest_time:
            oldest_time = record[__TTL]
            oldest_key = key
    return oldest_key


def cache_sized_ttl_quick(size_limit=256, ttl=3600):
    def decorator(func):
        storage: Dict[Any, Tuple[Any, float]] = {}

        def wrapper(*args, **kwargs):
            try:
                # Generate a key based on arguments being passed
                key = args
                # if value is cached and isn't expired then return
                if key in storage:
                    cache_record = storage[key]
                    if cache_record[__TTL] > time.time():
                        return cache_record[__VALUE]
                # calculate value
                result = func(*args, **kwargs)
                # if cache is full then remove oldest record
                while len(storage) >= size_limit:
                    oldest_key = __get_oldest_key(storage, ttl)
                    storage.pop(oldest_key)
                # add value to storage and return the resulting value
                storage[key] = (result, time.time() + ttl)
                return result
            except Exception as e:
                log.exception(f"Exception when accessing cache_sized_ttl_quick: {e}")
                return func(*args, **kwargs)
        return wrapper
    return decorator


def cache_ttl_single_value(ttl=3600):
    def decorator(func):
        value = None
        time_to_live = time.time()

        def wrapper(*args, **kwargs):
            nonlocal value
            nonlocal time_to_live
            if time_to_live > time.time():
                return value
            value = func(*args, **kwargs)
            time_to_live = time.time() + ttl
            return value
        return wrapper
    return decorator

