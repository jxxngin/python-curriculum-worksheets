# 3주 워밍업: 강아지 나이 변환기
# 강아지의 1년은 사람의 약 7년이래요. 강아지 나이를 사람 나이로 바꿔 주는 프로그램이에요.
# 이 코드에는 오류가 3개 숨어 있어요. 실행해서 오류 메시지를 읽고 고쳐 보세요!
# 먼저 type()으로 input()이 돌려주는 값이 어떤 종류인지 확인해 보세요.

dog_name = input("강아지 이름: ")
dog_age = input("강아지 나이(살): ")

print(type(dog_age))    # <class 'str'> 이 나오나요? str은 '글자'라는 뜻이에요.

human_age = dog_age * 7
print(type(human_age))

print(dog_name + "는 사람 나이로 " + human_age + "살이에요!")
print(dog_name + "야, 오래오래 건강해!)
