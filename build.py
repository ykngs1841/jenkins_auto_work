import os
import subprocess
import sys
from datetime import datetime

# ===== 날짜 및 경로 설정 =====
BUILD_DATE = datetime.now().strftime("%y%m%d")
#PROJECT_ROOT = os.getcwd()                            # Docker로 인하여 삭제 진행 # 절대경로 설정
SRC_ROOT = "/app"
BUILD_DIR = "/build"                                   # OS 연결 -> Docker로 인하여 수정 
SRC_FILE = os.path.join(SRC_ROOT, "src", "main.cpp")
OUTPUT_FILE = f"app_{BUILD_DATE}.exe"     
RESULT_FILE = f"build_result_{BUILD_DATE}.txt"            # 산출물 생성
log_file = os.path.join(BUILD_DIR, f"build_log_{BUILD_DATE}.txt")                  # ===== 로그 파일 경로 =====

print(f"=== Build Start : {BUILD_DATE} ===", flush=True)

# build 디렉토리 생성
os.makedirs(BUILD_DIR, exist_ok=True)

# ===== 컴파일 명령 정의=====
cmd = [
    #r"C:\msys64\mingw64\bin\g++.exe",       # Docker로 인하여 삭제 진행 #C++ 컴파일러
    "g++",
    SRC_FILE,    # 컴파일러 대상 지정
    "-o",        # Output ->이름 명명  
    os.path.join(BUILD_DIR, OUTPUT_FILE)
    os.path.join(BUILD_DIR, RESULT_FILE)
]
# ===== 디버깅 ======
print("=== DEBUG ===", flush=True)
# Docker 도입으로 불필요 print("g++ exists:", os.path.exists(r"C:\msys64\mingw64\bin\g++.exe"))  #PATH 문제 발생
print("SRC_FILE exists:", os.path.exists(SRC_FILE), flush=True)
print("CMD:", cmd, flush=True)
print("=============", flush=True)


# ===== 컴파일 실행 =====
result = subprocess.run( # 외부 명령어 실행
    cmd,
    capture_output=True,
    text=True            # 출력형태 str 
)

# ===== 실패 처리 =====
if result.returncode != 0:
    print("Build FAILED")
    print("=== STDOUT ===")
    print(result.stdout)
    print("=== STDERR ===")
    print(result.stderr)

    with open(log_file, "w") as f:
        f.write("=== STDOUT ===\n")
        f.write(result.stdout + "\n")
        f.write("=== STDERR ===\n")
        f.write(result.stderr)

    sys.exit(1)

# ===== 성공 처리 =====

with open(log_file, "w") as f:   # 열린 파일을 f로 명명
    f.write(result.stdout)       # 해당 파일에 작성
    print("Build SUCCESS")
    f.write(f"Output: {OUTPUT_FILE}\n")

with open(RESULT_FILE, "w") as f:
    f.write(f"Date: {BUILD_DATE}\n")
    f.write(f"Output: {RESULT_FILE}\n")