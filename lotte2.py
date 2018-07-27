# 로또번호 중복 없이 여섯개 축출하기 random.sample()
# import random

# today=[li for li in range(1,47)]

# ran_num=random.sample(today,6)
# print(ran_num)

#한문장으로 처리today=random.sample(range(1,47),6)

# 중복된 숫자가 today 리스트에 없으면 수행
import random

today=[]

for i in range(1,7):
    while ran_num in today:
        ran_num=random.randrange(1, 46, 1)
        today.append(ran_num)