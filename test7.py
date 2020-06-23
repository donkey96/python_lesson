# for文
for_sample = []
for_sample.append("python")
for_sample.append("-")
for_sample.append("izm")
for_sample.append("for")
for_sample.append("statement")
for_sample.append("sample")

for value in 'ABCDEF':
  print(value)

test_list_1 =[['https', 'www'], ['python-izm', 'com']]

for value in test_list_1:
  print(value)

for value_1, value_2 in test_list_1:
  print(value_1, value_2)

# while文
counter = 0

while True:
  counter += 1
  print(counter)
  if counter == 10:
    break

# continue
for num in range(100):

  if num % 10:
    continue

  print(num)

# range
for i in range(-2,10):
  print(i)
  