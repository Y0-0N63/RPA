# 임의의 정수를 받아서 1~정수까지 합을 구하는 프로그램
# 정수의 합을 구하는 로직은 함수(sumfunc)로 만들기

num = int(input("정수를 입력해주세요. >> "))

def sumfunc(num) :
  total = 0
  for i in range(1, num + 1) :
    total += i
  return total

if num < 0 :
  print ("정수를 다시 입력해주세요.")
else : 
  result = sumfunc(num)
  print("1부터 ", num, "까지의 합 >> ", result)