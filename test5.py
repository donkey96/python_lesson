test_list = ['https', 'www', 'python', 'izm', 'com']

print(test_list[:4])
print(test_list[2:])
print(test_list[::2])
print(test_list[3:5])
print(test_list[-1:])
print(test_list[:-1])
print(test_list[::-1])
print(test_list[:999])

test_list[1:3] = ('WWW', 'PYTHON')

print(test_list)

# コメントアウト
# 通常のコメントアウト
# print("test 1")
print("test 2") # ここにも書ける

# 複数行のコメントアウトのように扱う
'''
print('test 3')
print("test 4")
'''

# ネストさせた擬似複数行コメントアウト
'''
print("test 5")
"""
print('test 6')
"""
'''