# 베이스 이미지 (리눅스)
FROM ubuntu:22.04

# 기본 환경 설정 (비대화형)
ENV DEBIAN_FRONTEND=noninteractive

# 패키지 설치 (Python + g++ + git)
RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-pip \
        g++ \
        git && \
    apt-get clean

# python 명령어 통일
RUN ln -s /usr/bin/python3 /usr/bin/python

# 빌드 전용 디렉터리 (컨테이너 내부)
RUN mkdir -p /build && chmod -R 777 /build

# 작업 디렉토리
WORKDIR /app

# 기본 명령 (컨테이너 실행 시)
CMD ["bash"]
