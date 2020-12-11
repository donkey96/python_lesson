hex = [x * 16 for x in range(1, 9)]

# for x in range(1, 9):
#   hex.append(x * 16)

print(hex)

strheight = "170,168,180,17x,165"

height = [int(x) for x in strheight.split(',') if x.isdigit()]

print(height)

data = [[x+y*3 for x in range(3)] for y in range(4)]

print(data)

data0 = [[0 for x in range(3)] for y in range(4)]

print(data0)