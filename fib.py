cache = {}

def fib(n):
  if n <=1:
    return n
  
  # if the result is in the cache
  if n in cache:
    return cache[n]

  # if the result is not in the cache
    # do the expensive calculation
  
  result = fib(n-1) + fib(n-2)

  # Store the result from the expensive calculation
  cache[n] = result

  return result

  # 0, 1, 1, 2, 3, 5, 8, 13, 21
  print(fib(10)) # 5
  print(cache)