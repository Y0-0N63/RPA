# 왜 초기화해? -> 나중에 변수 만들면 간섭 문제가 생길 수 있음!
# 변수 종류별로 초기화 방식이 다름~
i = 0
num = int(input("1~9 사이의 정수를 입력해주세요. >> "))

if num > 0 and num < 10 :
  for i in range (1, 10) :
    print(f"{num} x {i} = {num * i}")
# ⭐⭐⭐ 콜론&들여쓰기 ⭐⭐⭐
else :
  print ("1~9 사이의 정수를 입력해주세요.")