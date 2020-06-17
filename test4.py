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
test_list_1 = ['1', '2', '3', '2', '1']
print(test_list_1)

print('---------------------------------')

test_list_1.remove('2')

print(test_list_1)