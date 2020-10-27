eigo = ['a', 'b', 'c', 'd', 'e', 'f']

char = eigo[2]

print(char)

char = eigo[-1]

print(char)

chars = eigo[1:4]

print(chars)

chars = eigo[3:]

print(chars)

chars = eigo[:4]

print(chars)

chars[3] = 'z'

print(chars)

chars = eigo+ ['g', 'h', 'i']

print(chars)

del chars[3]

print(chars)

chars[3] = 'd'

print(chars)

chars[0:2] = ['Hello', 'World']

print(chars)