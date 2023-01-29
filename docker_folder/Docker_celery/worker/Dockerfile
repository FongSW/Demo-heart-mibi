# FROM python:3.9

# COPY ./requirements.txt requirements.txt
# RUN pip3 install --upgrade pip -r requirements.txt
FROM python:3.9

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get -y install curl
RUN apt-get install libgomp1
# install Tesseract and its developer tools
RUN apt-get -y install tesseract-ocr libtesseract-dev
RUN apt-get -y install ffmpeg libsm6 libxext6

COPY ./requirements.txt requirements.txt
RUN pip3 install --upgrade pip -r requirements.txt
RUN pip install glob2
#celery -A main.celery worker --loglevel=info -Q universities,university --concurrency=3 eventlet
# CMD ["celery", "-A", "app.index.celery", "worker", "--loglevel=info", "-Q extract_data", "--concurrency=1", "-P", "eventlet"]
CMD ["celery", "-A", "app.index.celery", "worker", "--loglevel=info"]