#클래스 상속하는 개념
class Cal():
    def __init__(self, value):
        self.value=value

    def result(self):
        print(self.value)

    def add(self, input_value):
        self.value += input_value
        
    def sub(self, input_value):
        self.value -= input_value

    def mul(self, input_value):
        self.value *= input_value

    def div(self, input_value):
        #예외 처리 구문 만들어 주기 
        #오류 날 부분을 try구문안에 넣어 준다.
        #오류가 나면 실행할 부분은 except부분에 기재한다.ZeroDivisionError

        try:
            self.value /= input_value
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다")
        finally:
            print("나누기 실행완료")
              

# Cal클래서의 함수들을 상속 받는다.
class SaFeCal(Cal):
    def __init__(self, value):
        self.value = value

#부모클래스로 부터 물려받은 함수를 그대로 사용할 수 있지만
# 신이 가신 함수로 메소드를 오버라이딩해서 사용할 수 있다.
    def div(self, input_value):
        if (input_value == 0):
            self.value=0
        else:
            self.value /= input_value


cal1 = Cal(0)
cal1.result()
cal1.div(0)
cal1.result()
cal2=SaFeCal(0)
cal2.add(1)
cal2.result()
# cal2.div(0)
# cal2.result()

# cal1.add(1)
# cal1.result()
