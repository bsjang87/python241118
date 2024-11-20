import sqlite3
import random

class ElectronicsDatabase:
    """
    전자제품 데이터를 관리하는 SQLite 데이터베이스 클래스.
    제품 정보를 삽입, 수정, 삭제, 조회할 수 있는 기능을 제공합니다.
    """
    
    def __init__(self, db_name="electronics.db"):
        """
        클래스 초기화 메서드.
        데이터베이스 연결을 생성하고, 테이블이 없을 경우 생성합니다.
        
        :param db_name: 데이터베이스 파일 이름 (기본값: electronics.db)
        """
        self.connection = sqlite3.connect(db_name)  # SQLite 데이터베이스 연결 생성
        self.cursor = self.connection.cursor()      # 커서 객체 생성
        self.create_table()                         # 테이블 생성 메서드 호출

    def create_table(self):
        """
        전자제품 정보를 저장할 테이블을 생성합니다.
        테이블이 이미 존재하는 경우 아무 작업도 하지 않습니다.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS electronics (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 제품 ID (자동 증가)
                product_name TEXT NOT NULL,                   -- 제품명
                price REAL NOT NULL                           -- 제품 가격
            )
        """)
        self.connection.commit()  # 변경사항 저장

    def insert_product(self, product_name, price):
        """
        새로운 전자제품 데이터를 테이블에 삽입합니다.
        
        :param product_name: 제품명 (문자열)
        :param price: 제품 가격 (실수형)
        """
        self.cursor.execute("""
            INSERT INTO electronics (product_name, price)
            VALUES (?, ?)  -- ?는 SQL 쿼리에서 파라미터를 지정하는 자리 표시자
        """, (product_name, price))  # 제품명과 가격 데이터를 삽입
        self.connection.commit()  # 변경사항 저장

    def update_product(self, product_id, product_name=None, price=None):
        """
        특정 ID를 가진 제품의 정보를 수정합니다.
        제품명 또는 가격만 변경할 수 있으며, 둘 다 변경도 가능합니다.
        
        :param product_id: 수정할 제품의 ID (정수형)
        :param product_name: 새로운 제품명 (기본값: None)
        :param price: 새로운 가격 (기본값: None)
        """
        query = "UPDATE electronics SET "
        parameters = []
        # 수정할 제품명과 가격을 조건에 따라 추가
        if product_name:
            query += "product_name = ?, "
            parameters.append(product_name)
        if price:
            query += "price = ?, "
            parameters.append(price)
        query = query.rstrip(", ")  # 마지막 쉼표 제거
        query += " WHERE product_id = ?"  # ID 조건 추가
        parameters.append(product_id)
        self.cursor.execute(query, parameters)  # 쿼리 실행
        self.connection.commit()  # 변경사항 저장

    def delete_product(self, product_id):
        """
        특정 ID를 가진 제품 데이터를 삭제합니다.
        
        :param product_id: 삭제할 제품의 ID (정수형)
        """
        self.cursor.execute("""
            DELETE FROM electronics WHERE product_id = ?
        """, (product_id,))  # 지정된 ID의 데이터 삭제
        self.connection.commit()  # 변경사항 저장

    def select_all_products(self):
        """
        테이블에 저장된 모든 제품 데이터를 조회합니다.
        
        :return: 모든 제품 데이터를 포함하는 리스트
                 각 제품은 (product_id, product_name, price) 형태의 튜플로 반환됩니다.
        """
        self.cursor.execute("""
            SELECT * FROM electronics
        """)
        return self.cursor.fetchall()  # 모든 결과를 리스트로 반환

    def close_connection(self):
        """
        데이터베이스 연결을 종료합니다.
        """
        self.connection.close()


# 샘플 데이터 생성 및 테스트를 위한 함수
def generate_sample_data(db):
    """
    샘플 전자제품 데이터를 데이터베이스에 삽입합니다.
    총 100개의 임의의 제품명이 생성되며, 가격은 50~2000 사이에서 무작위로 설정됩니다.
    
    :param db: ElectronicsDatabase 객체
    """
    product_names = ["Smartphone", "Laptop", "Tablet", "Smartwatch", "TV", 
                     "Headphones", "Speaker", "Camera", "Printer", "Monitor"]
    for _ in range(100):
        product_name = random.choice(product_names) + f" Model-{random.randint(100, 999)}"  # 임의의 모델명 생성
        price = round(random.uniform(50, 2000), 2)  # 임의의 가격 생성
        db.insert_product(product_name, price)  # 데이터베이스에 삽입


# 클래스와 샘플 데이터를 테스트하는 코드
if __name__ == "__main__":
    # 데이터베이스 객체 생성
    db = ElectronicsDatabase()

    # 샘플 데이터 생성 및 삽입
    generate_sample_data(db)

    # 전체 제품 데이터 조회
    products = db.select_all_products()
    print(f"총 제품 수: {len(products)}")
    for product in products[:10]:  # 처음 10개의 데이터 출력
        print(product)

    # 제품 수정
    db.update_product(1, product_name="Updated Laptop Model-123", price=1200.99)

    # 제품 삭제
    db.delete_product(2)

    # 수정 및 삭제 후 데이터 조회
    products = db.select_all_products()
    print(f"수정/삭제 후 총 제품 수: {len(products)}")
    for product in products[:10]:
        print(product)

    # 데이터베이스 연결 종료
    db.close_connection()
