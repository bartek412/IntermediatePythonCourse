import time
import functools


@functools.lru_cache(100)
def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result


start = time.time()
for i in range(1, 35):
    print('{} - {} czas: {}'.format(i, fib(i), time.time() - start))
print('calkowity czas:', time.time() - start)
print(fib.cache_info())
