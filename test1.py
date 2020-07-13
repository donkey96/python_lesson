test_set_1 = set({'python', '-', 'izm', '.', 'com'})

print(test_set_1.isdisjoint({'python', 'izm'}))
print(test_set_1.isdisjoint({1, 2, 3}))

print('-------------------------------')

print(test_set_1.issubset({'python', 'izm'}))
print(test_set_1.issubset({'www', 'python', '-', 'izm', '.', 'com'}))

# issubsetと同じ
print(test_set_1 <= {'python', 'izm'})
print(test_set_1 <= {'www', 'python', '-', 'izm', '.', 'com'})

print('-------------------------------')

print(test_set_1.issuperset({'python', 'izm'}))
print(test_set_1.issuperset({'www', 'python', '-', 'izm', '.', 'com'}))

# issupersetと同じ
print(test_set_1 >= {'python', 'izm'})
print(test_set_1 >= {'www', 'python', '-', 'izm', '.', 'com'})

test_set_2 = {'python', 'izm', 'com'}

print(test_set_2.union({'python', 'www'}))
print(test_set_2.intersection({'python', 'www'}))
print(test_set_2.difference({'python', 'www'}))
print(test_set_2.symmetric_difference({'python', 'www'}))