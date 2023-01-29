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
# RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
# RUN apt-get -y install curl
# RUN pip3 install libgomp1
# RUN brew install libomp
# RUN pip install sqlalchemy
# RUN curl -sSL https://get.docker.com/ | sh --ask-become-pass


# RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz \
#   && tar xzvf docker-17.04.0-ce.tgz \
#   && mv docker/docker /usr/local/bin \
#   && rm -r docker docker-17.04.0-ce.tgz 
