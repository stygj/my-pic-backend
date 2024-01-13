FROM python:3.11.6-slim

RUN mkdir -p /app
COPY . /app/
WORKDIR /app
# 이미지를 업로드할 디렉토리 생성
RUN mkdir -p /app/images

RUN pip3 install poetry
# poetry lock에서 requirements.txt 생성
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip3 install --no-cache-dir -r requirements.txt

# pycache 생성 방지
ENV PYTHONDONTWRITEBYTECODE 1
# 성능 향상을 위한 streams 버퍼링
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app
ENV API_ENV=release

# app 실행
CMD gunicorn app.main:app --bind 0.0.0.0:8000 -w 3 -k uvicorn.workers.UvicornWorker