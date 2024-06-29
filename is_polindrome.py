import timeit
from functools import partial

def is_palindrome1(w):
  return w[::-1] == w

def is_palindrome2(w):
  while len(w) > 1:
    if w[0] != w[-1]:
      return False
    w = w[1:-1]
  return True

def is_palindrome3(w):
  for i in range(len(w)//2 - 1):
    if w[i] != w[-1 - i]:
      return False
  return True

print(is_palindrome3('hello'))

if __name__ == '__main__':
  name = 'kaak'
  funcs = (is_palindrome1, is_palindrome2, is_palindrome3)
  times = []
  for func in funcs:
      times_local = timeit.Timer(partial(func, name)).repeat(100, 1000)
      times.append(min(times_local)/1000)
  for func, time in zip(funcs, times):
    print(f'Execution time for {func.__name__} is {time} seconds')