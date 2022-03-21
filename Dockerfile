FROM python:latest
WORKDIR /app
COPY ./requirements.txt ./
RUN apt update && apt upgrade -y &&\
    pip install -r requirements.txt
CMD ["bash"]
