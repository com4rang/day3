fruits=['apple', 'banana', 'kiwi']
fruits.append('watermelon')

for fruit in fruits :
   # print( "{}가 있습니다. " .format(fruit))
    print(fruit + "가 있습니다.")

count=len(fruits)

#while문은 조건식을 넣어 참인 동안 실행
index=0
while index < count:
    print(fruits[index] + "를 꺼냈습니다.")
    index=index+1