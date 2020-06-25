print('python', end=' ')
print('-', end=' ')
print('izm', end=' ')
print('com')

# 出力先の変更
f_obj = open('test.txt', 'w')

print('python-izm.com', file=f_obj)

# フォーマット出力
print('-------------------------------------------------------')
print('Pythonの学習サイト : %s' % 'python-izm.com')
print('Pythonの学習サイト : %s-%s.%s' % ('python', 'izm', 'com'))

test_int = 100 + 100
test_str = 'python-izm.com'
print('サイト開設 %d 日目! %s' % (test_int, test_str))

print('Pythonの学習サイト : {}'.format('python-izm.com'))
print('Pythonの学習サイト : {0}-{1}.{2}'.format('python', 'izm', 'com'))

print('サイト開設 {1} 日目! {0}'.format(test_str, test_int))

# 例外処理
print('------------------------------------------------------')

def exception_test(value_1, value_2):
  print('====計算開始====')

  result = 0

  try:
    result = value_1 + value_2
  except:
    print('計算出来ませんでした!')
    raise
  finally:
    print('計算終了')

  return result

try:
  print(exception_test(100, 100))
  print(exception_test(200, 200))
  print(exception_test(300, '300'))
except:
  print('エラーを受け取りました')