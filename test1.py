class PropertyTest(object):

  def __init__(self, url):
    self._url = url

  def get_url(self):
    print('-- get_url --')
    return self._url

  url = property(get_url)

prop = PropertyTest('https://www.python-izm.com/')

print(prop.url)