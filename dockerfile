FROM python:3.9

WORKDIR /app
# 소스 복사
COPY . .
RUN pip3 install -r requirements.txt --no-cache-dir