print("박상윤은 서울대학교 기계공학부 24학번 이다\n")
print("박상윤은 술을 개많이 처먹는다\n")
print("돈이 많은 부자이다\n")
print("정수 2개를 입력하세요 :")

a = int(input("첫 번째 정수: "))
print("\n")
b = int(input("두 번째 정수: "))
print("\n")

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
if b != 0:
    print(f"{a} / {b} = {a / b}")
else:
    print("0으로 나눌 수 없습니다.")
