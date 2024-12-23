FROM python:3.9-slim

SHELL ["/bin/bash", "-c"]
WORKDIR /root

RUN apt update
RUN apt install git -y
RUN mkdir project

WORKDIR /root/project
RUN git clone https://github.com/Dalso13/music_genre_classify_site.git .

RUN python -m venv venv
RUN source venv/bin/activate
RUN python -m pip install --upgrade pip

RUN pip install -r ./requirements.txt
RUN python manage.py migrate

CMD ["python","manage.py","runserver "]