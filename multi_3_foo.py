# 問題1
# 3の倍数の時に、fooと出力
for i in range(1, 10):
  print()
  print(f"{i}の段")
  for j in range(1, 10):
    if (i * j) % 3 == 0:
      print("foo ", end="")
    else:
      print(f"{i * j:3d} ", end="")
    # print(f"{i * j:3d} ", end="")