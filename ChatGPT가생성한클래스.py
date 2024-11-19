class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Skill: {self.skill}")

# 테스트 코드
if __name__ == "__main__":
    # 1. Person 클래스 객체 생성 및 정보 출력
    p1 = Person(1, "Alice")
    p1.printInfo()  # 예상 출력: ID: 1, Name: Alice

    # 2. Manager 클래스 객체 생성 및 정보 출력
    m1 = Manager(2, "Bob", "CTO")
    m1.printInfo()  # 예상 출력: ID: 2, Name: Bob, Title: CTO

    # 3. Employee 클래스 객체 생성 및 정보 출력
    e1 = Employee(3, "Charlie", "Python")
    e1.printInfo()  # 예상 출력: ID: 3, Name: Charlie, Skill: Python

    # 4. Manager의 title 변경 후 출력
    m1.title = "CEO"
    m1.printInfo()  # 예상 출력: ID: 2, Name: Bob, Title: CEO

    # 5. Employee의 skill 변경 후 출력
    e1.skill = "Java"
    e1.printInfo()  # 예상 출력: ID: 3, Name: Charlie, Skill: Java

    # 6. Person 객체를 리스트로 관리
    people = [Person(4, "David"), Manager(5, "Eve", "Manager"), Employee(6, "Frank", "C++")]
    for person in people:
        person.printInfo()

    # 7. Manager 클래스 객체 생성 및 다중 출력
    m2 = Manager(7, "Grace", "HR Manager")
    m2.printInfo()  # 예상 출력: ID: 7, Name: Grace, Title: HR Manager

    # 8. Employee 클래스 객체 생성 및 다중 출력
    e2 = Employee(8, "Hank", "Data Analysis")
    e2.printInfo()  # 예상 출력: ID: 8, Name: Hank, Skill: Data Analysis

    # 9. Manager와 Employee 섞어서 리스트로 관리
    staff = [m1, e1, m2, e2]
    for s in staff:
        s.printInfo()

    # 10. Person 클래스 정보 검증
    p2 = Person(9, "Ivy")
    assert p2.id == 9
    assert p2.name == "Ivy"
    p2.printInfo()  # 예상 출력: ID: 9, Name: Ivy
