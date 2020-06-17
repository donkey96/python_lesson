import datetime

# タプル
def get_today():

    today = datetime.datetime.today()
    value = (today.year, today.month, today.day)

    return value

test_tuple = get_today()

print(test_tuple)
print(test_tuple[0])
print(test_tuple[1])
print(test_tuple[2])

# リスト
test_list_1 = ['python', 'izm', 'com']
print(test_list_1)

print('---------------------------------')

test_list_1.insert(1, '-')
test_list_1.insert(3, '.')

print(test_list_1)

test_list_1.insert(0, 'http://wwww.')

print(test_list_1)