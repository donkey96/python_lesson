test_list_1 = [100, 200, 300]
test_list_2 = [100, 200, 300]
test_list_3 = [300, 200, 100]

test_tuple_1 = (100, 200, 300)
test_str_1 = 'python-izm'

print(test_list_1 == test_list_2)
print(test_list_1 == test_list_3)
print('----------------------------')
print(test_list_1 == test_tuple_1)
print(test_str_1 == 'python-izm')
print('----------------------------')
print(test_list_1 is test_list_2)
print(id(test_list_1))
print(id(test_list_1) == id(test_list_1))
print(test_list_1 is test_list_1)