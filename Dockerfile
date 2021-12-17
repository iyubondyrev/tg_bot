FROM ubuntu:20.04
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3
RUN apt-get install -y pip
RUN mkdir /tg_bot/
WORKDIR /tg_bot/
COPY . /tg_bot/
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]
