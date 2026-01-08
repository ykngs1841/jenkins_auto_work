import os
import subprocess
import sys
from datetime import datetime

# ===== 날짜 및 경로 설정 =====
BUILD_DATE = datetime.now().strftime("%y%m%d")
PROJECT_ROOT = os.getcwd()                             # 절대경로 설정
BUILD_DIR = os.path.join(PROJECT_ROOT, "build")        # OS 연결
SRC_FILE = os.path.join(PROJECT_ROOT, "src", "main.cpp")
OUTPUT_FILE = f"app_{BUILD_DATE}.exe"                  # 산출물 생성

print(f"=== Build Start : {BUILD_DATE} ===")

# build 디렉토리 생성
os.makedirs(BUILD_DIR, exist_ok=True)

# ===== 컴파일 명령 정의=====
cmd = [
    "C:\msys64\mingw64\bin\g++",       # C++ 컴파일러
    SRC_FILE,    # 컴파일러 대상 지정
    "-o",        # Output ->이름 명명  
    os.path.join(BUILD_DIR, OUTPUT_FILE)
]

# ===== 컴파일 실행 =====
result = subprocess.run( # 외부 명령어 실행
    cmd,
    capture_output=True,
    text=True            # 출력형태 str 
)

# ===== 로그 파일 경로 =====
log_file = os.path.join(BUILD_DIR, f"build_log_{BUILD_DATE}.txt")

# ===== 실패 처리 =====
if result.returncode != 0:
    print("Build FAILED")
    print(result.stderr)

    with open(log_file, "w") as f:
        f.write(result.stderr)     #로그 파일 에러메세지 기록

    sys.exit(1)

# ===== 성공 처리 =====
with open(log_file, "w") as f:
    f.write(result.stdout)

print("Build SUCCESS")
print(f"Output: {OUTPUT_FILE}")