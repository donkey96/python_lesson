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

  # インスタンスメソッド
  def sample_instancemethod(self, arg_1):
    pass
  # クラスメソッド
  @classmethod
  def sample_classmethod(cls, arg_1):
    pass
  # スタティックメソッド
  @staticmethod
  def sample_staticmethod(arg_1, arg_2):
    pass