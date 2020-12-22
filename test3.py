# func(a=3, b=5)
# func(**{'a':3, 'b':5})

def func(**keywords):
  for kw in keywords:
    print(kw, ":", keywords[kw])
func(a=1, b=2, c=3, d=4)

# func(3, 5)
# func(*(3, 5))

def func(*arguments):
  for arg in arguments:
    print(arg)
func(1, 2, 3, 4)

def kansu1(a):
  print(a)

kansu1(88)
kansu1(a=77)

def kansu2(a, b):
  print(a + b)

kansu2(40, 60)
kansu2(40, b=60)
kansu2(a=40, b=60)
kansu2(b=40, a=60)
kansu2(*(40, 61))
kansu2(*[40, 62])
kansu2(*"えび")
kansu2(**{'a':40, 'b':63})