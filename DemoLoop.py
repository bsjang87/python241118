# DemoLoop.py

#while구문
value = 5
while value > 0:
    print(value)
    value -= 1

#for in 구문
lst = [100, "python", 3.14]
for item in lst:
    print(item, type(item))

print("---dict형태---")
fruits = {"apple" : "red", "kiwi" : "green"}
for k, v in fruits.items():
    print(k, v)

print("---range()함수---")
print(list(range(10)))
print(list(range(2000, 2025)))
print(list(range(11, 32)))

for i in range(10):
    print(i)

print("---리스트 내장---")
lst = list(range(1, 11))
print(lst)
print([i**2 for i in lst if i > 5])
tp = ("apple", "kiwi", "orange")
print([len(i) for i in tp])

print("---필터링 함수---")
lst = [10, 25, 30]
itemL = filter(None, lst)
for item in itemL:
    print(item)

#함수 정의
def getBiggerThan20(i):
    return i > 20

print("---필터링 함수 있음---")
itemL = filter(getBiggerThan20, lst)
for item in itemL:
    print(item)

print("---람다 함수 있음---")
itemL = filter(lambda x:x>20, lst)
for item in itemL:
    print(item)