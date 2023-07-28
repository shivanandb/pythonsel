FROM  python:3.9.9-slim

#install required python packages.
RUN  mkdir -p /smokeTest
WORKDIR /smokeTest
ENV PYTHONPATH=/smokeTest

# install dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# copy source 
COPY . /smokeTest
WORKDIR /smokeTest

CMD python smoketest.py

