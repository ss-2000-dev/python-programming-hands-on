# num1 = int(input("num1:"))
# num2 = int(input("num2:"))
# print(f"num1 + num2 = {num1 + num2}")

try:
  num1 = int(input("num1:"))
  num2 = int(input("num2:"))
  print(f"num1 + num2 = {num1 + num2}")
except ValueError:
    print("整数値を入力してください")