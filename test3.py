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

def kansu3(a, b=11):
  print(a, b)

kansu3(33, 22)
kansu3(33, b=22)
kansu3(33)

def kansu4(*args):
  print(args)

kansu4()
kansu4(55)
kansu4(22, 66)

def kansu44(*args):
  for arg in args:
    print(arg)

kansu44(1, 2, 3, 4)

def kansu5(*args, a):
  print(args, a)

kansu5(a=18)
kansu5(11, 22, a=18)

def kansu6(**keywords):
  for kw in keywords:
    print(kw, ":", keywords[kw])

kansu6(a=1, b=2, c=3, d=4)

def kansu7(*, a=77):
  print(a)

kansu7(a=99)

def kansu77(a, b, *, c=77, d=88):
  print(a, b, c, d)

kansu77(11, 22, c=33)