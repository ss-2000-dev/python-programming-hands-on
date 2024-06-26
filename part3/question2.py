# 5 が入っている要素番号を格納するための配列を用意
index = []

# 入力した数字を格納する配列を一応用意
input_numbers = []

# 数字を 10 回入力する for ループ
for i in range(10):
  num = int(input(f"{i + 1}回目:"))
  
  # 入力した数字を配列として保存
  input_numbers.append(num)
  
  # 入力した数字が 5 であれば何番目にあるのかを記録
  if(num == 5):
    index.append(i + 1)

# 何番目の要素に 5 があるのか表示する
print("5は入力した数字の", end="")
for i in range(len(index)):
  if(len(index) >= 1 and i != len(index) - 1):
    print(f"{index[i]}、", end="")
  else:
    print(f"{index[i]}番目", end="")

print("にあります")