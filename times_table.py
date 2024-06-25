# 問題1
# 九九の段の出力
for i in range(1, 10):
  print()
  print(f"{i}の段")
  for j in range(1, 10):
    print(f"{i * j:2d} ", end="")
    