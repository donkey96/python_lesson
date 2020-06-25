def test_func(num_1, num_2, oprn=1):

  if oprn == 1:
    print('足し算開始')
    print(num_1 + num_2)

  elif oprn == 2:
    print('引き算開始')
    print(num_1 - num_2)
  
  elif oprn == 3:
    print('掛け算開始')
    print(num_1 * num_2)
  
  elif oprn == 4:
    print('割り算開始')
    print(num_1 / num_2)

  else:
    print('不明なオペレーション指定です')

test_func(100, 10)
test_func(100, 10, 4)

# 関数
def test_function():
  print('call test_function')

class TestClass:
  # メソッド
  def test_method():
    print('call test_method')

print('--------------------')
print(test_function)
print(TestClass.test_method)

print('--------------------')
print(type(test_function))
print(type(TestClass.test_method))

print('--------------------')
t = TestClass()
print(test_function)
print(t.test_method)