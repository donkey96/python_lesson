color = ["white", "black", "red", "blue", "yellow"]
color2 = ["green", "brown", "purple", "pink"]
color[4] = "gray"
del color[0]

pic = color[0] + " and " + color[3]
total_color = color + color2
slice = color[1:3]
slice2 = color[:2]
slice3 = color[1:]

print(color[1])
print(pic)
print(total_color)
print(slice)
print(slice2)
print(slice3)