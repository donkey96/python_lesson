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

chars.insert(4, 'e')

print(chars)

eigo.append('g')

print(eigo)

ext = ['h', 'i', 'j', 'k', 'l', 'm']

eigo.extend(ext)

print(eigo)

eigo.remove('h')

print(eigo)

char = eigo.pop()

print(eigo)
print(char)

char = eigo.pop(3)

print(eigo)
print(char)

eigo.clear()

print(eigo)

eigo = ['a', 'b', 'c', 'a', 'b', 'c']

print(eigo.index('c'))

print(eigo.index('c', 3, 6))

print(eigo.count('b'))

eigo.sort()

print(eigo)