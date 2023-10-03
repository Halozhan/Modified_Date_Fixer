import tkinter
from tkinter import filedialog

import os
import re
import datetime


# 파일의 생성일자와 수정일자를 변경하는 함수
def change_file_dates(filepath, date_str):
    try:
        file_date = datetime.datetime.strptime(date_str, '%Y%m%d%H%M%S')
        os.utime(filepath, (file_date.timestamp(), file_date.timestamp()))
        print(f"파일 '{filepath}'의 생성일자와 수정일자가 변경되었습니다.")
    except ValueError:
        print(f"파일 '{filepath}'에서 유효한 날짜를 추출할 수 없습니다.")


# 작업 디렉토리 설정
tkinter_app = tkinter.Tk()
tkinter_app.withdraw()
directory = filedialog.askdirectory(parent=tkinter_app, initialdir="/", title='Please select a directory')
print(f"dir_path : {directory}")
if not directory:
    exit()

# 디렉토리 내 모든 파일에 대해 반복 (하위 폴더 포함)
for root, _, files in os.walk(directory):
    for filename in files:
        filepath = os.path.join(root, filename)

        # 파일 이름에서 숫자만 추출
        numeric_part = re.sub(r'\D', '', filename)
        date_str = numeric_part[:14]  # 앞 14자리 숫자를 날짜로 가정
        print(date_str)
        if len(date_str) != 14:
            print(f"파일 '{filepath}'에서 유효한 날짜를 추출할 수 없습니다.")
            continue

        # 파일의 생성일자와 수정일자 변경
        change_file_dates(filepath, date_str)
