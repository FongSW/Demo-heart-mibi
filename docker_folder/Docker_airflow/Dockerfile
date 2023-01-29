FROM apache/airflow:2.4.1-python3.10
# install
USER root
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get -y install curl
RUN apt-get install libgomp1

USER airflow
COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt
RUN pip install tensorflow
RUN pip install glob2
RUN pip install scikit-optimize
RUN pip install wheel
RUN pip install lightgbm
RUN pip install intel-openmp

