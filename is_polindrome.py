import timeit
from functools import partial

'''
In this task I need to create a new function is_palindrome3 which would be faster than is_palindrome1 and is_palindrome2
'''

def is_palindrome1(w):
  return w[::-1] == w

def is_palindrome2(w):
  while len(w) > 1:
    if w[0] != w[-1]:
      return False
    w = w[1:-1]
  return True

def is_palindrome3(w):
  median = len(w) // 2 - 1
  return w[:median + 1] == w[:median + 1:-1]

print(is_palindrome3('kazak'))

if __name__ == '__main__':
  name = 'kaak'
  funcs = (is_palindrome1, is_palindrome2, is_palindrome3)
  times = []
  for func in funcs:
      times_local = timeit.Timer(partial(func, name)).repeat(1000, 1000)
      times.append(min(times_local)/1000)
  for func, time in zip(funcs, times):
    print(f'Execution time for {func.__name__} is {time} seconds')

'''
def is_palindrome3(w):
  #5.185619997973845e-07 seconds
  l, r = 0, len(w) - 1
  median = len(w) // 2 - 1
  while l <= median:
    if w[l] != w[r]:
      return False
    l += 1
    r -= 1
  return True

def is_palindrome3(w):
  #3.800680001404544e-07 seconds
  median = len(w) // 2 - 1
  return w[:median + 1] == w[:median + 1:-1]

def is_palindrome3(w):
  #3.610550002122181e-07 seconds
  for i in range(len(w)//2 - 1):
    if w[i] != w[-1 - i]:
      return False
  return True
  
def is_palindrome3(w):
  #7.570109999996966e-07 seconds
  median = len(w) // 2 - 1
  first_half = w[:median + 1]
  second_half = w[:median + 1:-1]
  for one, two in zip(first_half, second_half):
    if one != two:
      return False
  return True
'''