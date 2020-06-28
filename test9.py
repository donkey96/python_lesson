class NewStyleClassBase(object):

  def test_method(self, msg):
    print('NewStyleClassBase: {}'.format(msg))

class NewStyleClass(NewStyleClassBase):

  def test_method(self, msg):
    print('NewStyleClass: {}'.format(msg))
    super().test_method(msg)

new = NewStyleClass()
new.test_method('method call')

# メソッドの種類
class TestClass:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  # インスタンスメソッド
  def sample_instancemethod(self, display_x=True, display_y=True):
    if display_x:
      print('x is {}'.format(self.x))
    if display_y:
      print('y is {}'.format()(self.y))

  test_class_1 = TestClass(100, 50)
  test_class_1.sample_instancemethod(display_x=False)
  # クラスメソッド
  @classmethod
  def sample_classmethod(cls, arg_1):
    pass
  # スタティックメソッド
  @staticmethod
  def sample_staticmethod(arg_1, arg_2):
    pass