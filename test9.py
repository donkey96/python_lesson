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

# ジェネレータ
def func_sample():
  yield('おはよう')
  yield('こんにちは')
  yield('こんばんは')

for i in func_sample():
  print(i)

f = func_sample()
print(next(f))
print(next(f))
print(next(f))

gen_sample = (i for i in 'おはよう こんにちは こんばんは'.split())

print(gen_sample)
for i in gen_sample:
  print(i)

# ファイルの読み書き
f = open('read.txt', 'r')

for row in f:
  print(row)

f.close()

f = open('write.txt', 'w')

f.write('Pythonでファイルに書き込みました!')

f.close()

fin_sjis = open('read.txt', 'r', encoding='utf-8')
fout_euc = open('euc-jp.txt', 'w', encoding='euc_jp')
fout_utf = open('utf-8.txt', 'w', encoding='utf-8')

for row in fin_sjis:
  fout_euc.write(row)
  fout_utf.write(row)

fin_sjis.close()
fout_euc.close()
fout_utf.close()