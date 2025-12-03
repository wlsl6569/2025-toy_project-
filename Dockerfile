# 실행될 환경 설정 파이썬3.11 최대한 가벼운 환경
FROM python:3.11-slim

# 컨테이너 경로 생성, 여기서 작업할거라고 지정
WORKDIR /app

# 패키지 복사
COPY requirements.txt /app/requirements.txt
# 패키지 설치,  || true 하면 앞에꺼 오류나도 진행
RUN pip install -r requirements.txt || true

# 작업내용도 컨테이너 workdir로 카피
COPY . /app

CMD ["python", "main.py"]


# cmd 에서 docker image 만들고 실행하기 

#docker build -t textgame .
#docker run textgame

'''

# ⭐ 1) Docker 이미지 목록 보기 (만든 이미지 확인)
docker images

# ⭐ 2) 실행 중인 컨테이너 보기
docker ps

# ⭐ 3) 중지된 것 포함 모든 컨테이너 보기
docker ps -a

# ⭐ 4) 컨테이너 삭제
docker rm <컨테이너_이름_또는_ID>

# ⭐ 5) 이미지 삭제
docker rmi <이미지_이름_또는_ID>

# ⭐ 6) (참고) 컨테이너 강제 삭제
docker rm -f <컨테이너_이름>

'''