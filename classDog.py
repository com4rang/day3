class Dog():
    def __init__(self, name, age) :
        self.name = name
        self.age = age
# name, age 
# sit, roll_over명령 수행하는 클래스

    def sit(self, count):
        print(self.name + "가 " + str(count) + "번 앉았네요")


    def roll_over(self):
        print(self.name + "가 굴렀습니다")


# 파이썬에서 클래스변수 생성
my_dog = Dog('Will', 3)
print(my_dog.name)
print(my_dog.age)

#호출하기
my_dog.sit(3)
my_dog.roll_over()