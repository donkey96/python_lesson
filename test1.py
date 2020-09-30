val = 5

if val > len([1,2,3,4]):
  print("Hello!")

if "ABC" == "abc":
  print("これはTrueです")
elif "あいう" == "あいう":
  print("この漢字比較はTrueです")
else:
  print("これはFalseです")

if "def" in "ABCDEFGHIJKLMN":
  print("文字列は含まれてません")
elif "おかき" in "あいうえおかきくけこ":
  print("文字列は含まれています")