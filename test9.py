class NewStyleClassBase(object):

  def test_method(self, msg):
    print('NewStyleClassBase: {}'.format(msg))

class NewStyleClass(NewStyleClassBase):

  def test_method(self, msg):
    print('NewStyleClass: {}'.format(msg))
    super().test_method(msg)

new = NewStyleClass()
new.test_method('method call')

# メソッドの種類
import datetime

class TestClass:

  # スタティックメソッド
  @staticmethod
  def sample_staticmethod(x, y):
    return x + y

# インスタンス化しないで呼び出し
print(TestClass.sample_staticmethod(10, 100))

# インスタンス化してからも呼び出せる
test_class = TestClass()
print(test_class.sample_staticmethod(100, 1000))

# モジュールのインポート
import sys

sys.path.append('~/Desktop/learning/python_lesson')

import calc
print(calc.plus_value(1, 1))

# lambda式
def plus_value_2(num_1, num_2):
  return num_1 + num_2

print(plus_value_2(10, 100))

l_func = lambda num_1, num_2: num_1 + num_2
print(l_func(10, 100))