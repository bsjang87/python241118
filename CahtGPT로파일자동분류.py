import os
import shutil

# 다운로드 폴더 경로
download_folder = r"C:\Users\student\Downloads"

# 대상 폴더 정의
folders = {
    "images": ["jpg", "jpeg"],
    "data": ["csv", "xlsx"],
    "docs": ["txt", "doc", "pdf"],
    "archive": ["zip"],
}

# 대상 폴더 생성
for folder in folders.keys():
    folder_path = os.path.join(download_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# 파일 이동
for filename in os.listdir(download_folder):
    file_path = os.path.join(download_folder, filename)
    
    # 폴더가 아닌 파일만 처리
    if os.path.isfile(file_path):
        # 확장자 추출 및 정리
        ext = filename.split(".")[-1].lower()  # 확장자를 소문자로 비교
        
        # 파일 이동
        moved = False
        for folder, extensions in folders.items():
            if ext in extensions:
                destination = os.path.join(download_folder, folder, filename)
                shutil.move(file_path, destination)
                print(f"Moved: {filename} -> {folder}")
                moved = True
                break
        
        # 미처리 파일 출력 (선택 사항)
        if not moved:
            print(f"Skipped: {filename}")
