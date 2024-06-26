# 前の数字を保存しておく変数の用意
before_number = 0

# 前の数の同じ回数をカウントする変数を用意しておく
count = 0

# 数字を 10 回入力する for ループ
for i in range(10):
  num = int(input(f"{i + 1}回目:"))
  # 初回は count しない
  if(i == 0):
    before_number = num
  # 前の数字と比較して同じであればカウントを１増やす
  elif(num == before_number): 
    before_number = num
    count = count + 1
  # それ以外は入力した数字を保存しておく
  else:
    before_number = num

# カウントの回数が 10 回であれば「perfect」と表示する
if(count == 10):
  print("perfect")
# それ以外は回数を表示する
else:
  print(f'{count}回')