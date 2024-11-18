# Demo.py

import timeit

# List와 Tuple 생성
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

# 1. 가변성 테스트
print("Before modification:")
print("List:", my_list)
print("Tuple:", my_tuple)

# List는 변경 가능
my_list[0] = 10
print("\nAfter modifying List:")
print("List:", my_list)

# Tuple은 변경 불가능
try:
    my_tuple[0] = 10
except TypeError as e:
    print("\nError modifying Tuple:", e)

# 2. 메모리 사용량 비교
print("\nMemory size:")
print("List size:", my_list.__sizeof__(), "bytes")
print("Tuple size:", my_tuple.__sizeof__(), "bytes")

# 3. 속도 비교
def access_list():
    return my_list[2]

def access_tuple():
    return my_tuple[2]

list_time = timeit.timeit(access_list, number=1000000)
tuple_time = timeit.timeit(access_tuple, number=1000000)

print("\nAccess time (1,000,000 iterations):")
print("List:", list_time, "seconds")
print("Tuple:", tuple_time, "seconds")
