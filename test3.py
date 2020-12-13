# func(a=3, b=5)
# func(**{'a':3, 'b':5})

def func(**keywords):
  for kw in keywords:
    print(kw, ":", keywords[kw])
func(a=1, b=2, c=3, d=4)