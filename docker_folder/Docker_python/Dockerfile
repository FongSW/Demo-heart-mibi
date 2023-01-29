FROM python:3.9

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get -y install curl
RUN apt-get install libgomp1
# install Tesseract and its developer tools
RUN apt-get -y install tesseract-ocr libtesseract-dev
RUN apt-get -y install ffmpeg libsm6 libxext6
RUN pip install glob2


COPY ./python_requirements.txt requirements.txt
RUN pip3 install --upgrade pip -r requirements.txt

# run fastAPI
CMD ["uvicorn", "app.index:app", "--host", "0.0.0.0", "--port", "8001"]
# run celery
# CMD ["celery", "-A", "app.index.celery", "worker", "--loglevel=info", "-Q universities", "--concurrency=1"]