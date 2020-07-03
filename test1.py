with open('read.txt') as f:

  #
  # 何らかの処理
  #

  print(f.closed)

print(f.closed)

class ContextManagerTest:
  
  def __enter__(self):
    print('__enter__')
    return 'as obj'

  def __exit__(self, exc_type, exc_value, traceback):
    print('__exit__')

with ContextManagerTest() as as_obj:
  print(as_obj)

from contextlib import contextmanager

@contextmanager
def context_manager_test():
  print('enter')
  yield 'as obj'
  print('exit')

with context_manager_test() as as_obj:
  print(as_obj)