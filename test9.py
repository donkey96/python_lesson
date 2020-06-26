def test_func(code, name, kana, *args, **kwargs):
  print(code, name, kana)
  print(args)
  print(kwargs)

test_func(
  100, 'python-izm', 'パイソンイズム',
  'JP', 'US',
  email='xxx', city='Tokyo'
)
