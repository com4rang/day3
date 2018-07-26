# def Hello(username) :
#     # name=input("What is your name : ")
#     print("Hello, %s"  %username.title() + "!")


# Hello('yujung')


def hello(name='jun', age='10') :
    print("Hello, " + name)
    print(age + "years old")

name = input("What is your Name: ")
age = input("How old are you? ")
hello(name, age)
hello(name)
hello()