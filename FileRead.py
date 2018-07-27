#다른 파일의 내용을 읽어서 출력하는 프로그램

with open('MYPAGE') as file:
    content1 = file.read()


with open('MYPAGE') as file:
    content2 = file.readlines()

print(content1)    
print(content2)

num=1
for line in content2:
    print(str(num) + ":" + line)
    num=num+1