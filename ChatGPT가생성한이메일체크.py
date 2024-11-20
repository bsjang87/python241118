import re

def is_valid_email(email):
    """
    이메일 유효성을 검사하는 함수.
    :param email: 검사할 이메일 주소
    :return: 유효하면 True, 그렇지 않으면 False
    """
    #raw string notation : 소문자 r을 붙이는 표현식
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_regex, email) is not None

# 샘플 이메일 리스트
emails = [
    "test@example.com",      # 유효
    "user.name+tag@domain.co",  # 유효
    "invalid-email@",         # 유효하지 않음
    "user@domain",            # 유효하지 않음 (TLD 없음)
    "user@domain.c",          # 유효하지 않음 (TLD 너무 짧음)
    "123@numbers.com",        # 유효
    "user@sub.domain.com",    # 유효
    "user@-domain.com",       # 유효하지 않음 (도메인 시작 부호)
    "user@domain..com",       # 유효하지 않음 (점 연속)
    "user@domain.toolongtld", # 유효하지 않음 (TLD 너무 김)
]

# 각 이메일 검사 및 출력
for email in emails:
    print(f"{email}: {'Valid' if is_valid_email(email) else 'Invalid'}")
