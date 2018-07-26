import random
# 로또 번호는 1~46, 총 6개 당첨번호가 있다.

today=[]

# today.append(random.randrange(1, 46, 1))
# today.append(random.randrange(1, 46, 1))
# today.append(random.randrange(1, 46, 1))
# today.append(random.randrange(1, 46, 1))
# today.append(random.randrange(1, 46, 1))
# today.append(random.randrange(1, 46, 1))

#while문으로 변경한 코드
count=0

while count<6 :
    today.append(random.randrange(1, 46, 1))
    count=count+1

print("오늘의 추천번호는" + str(today[0]) + "," +  str(today[1]) + "," +  str(today[2]) + "," +  str(today[3]) + "," +  str(today[4]) + "," +  str(today[5]) + "," +  "입니다.")