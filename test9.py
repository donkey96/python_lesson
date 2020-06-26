class Country:
  
  def __init__(self, country_name):
    self.country_name = country_name

class City(Country):

  def __init__(self, country_name, city_name):
    super().__init__(country_name)
    self.city_name = city_name

classes = []
classes.append(City('Japan', 'Tokyo'))
classes.append(City('USA', 'Washington, D.C.'))

for test_cls in classes:
  print('==== Class ====')
  print('contry_name --> ' + test_cls.country_name)
  print('city_name --> ' + test_cls.city_name)

# Pyton 2系のみ存在する新旧スタイル
'''
class OldStyleClass:
  pass

class NewStyleClass(object):
  pass

print type(OldStyleClass)
print type(NewStyleClass)
'''
# Pyton 3系での新スタイル
class NewStyleClass:
  pass

print(type(NewStyleClass))