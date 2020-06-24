print('python', end=' ')
print('-', end=' ')
print('izm', end=' ')
print('com')

# 出力先の変更
f_obj = open('test.txt', 'w')

print('python-izm.com', file=f_obj)