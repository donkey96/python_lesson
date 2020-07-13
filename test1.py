comp_list = [i * ii  for i in range(1, 10) for ii in range(1, 10)]

print(comp_list)

comp_dict = {str(i): i * i for i in range(10)}

print(comp_dict)

comp_set = {str(i * i) for i in range(10)}

print(comp_set)