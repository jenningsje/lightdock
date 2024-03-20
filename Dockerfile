# start from base
FROM ubuntu:18.04

# install system-wide deps for python and node
RUN apt-get -yqq update && \
    apt-get -yqq install python3-pip python3-dev curl gnupg && \
    apt-get install -y wget

# add requirements.txt to /opt/app
COPY requirements.txt /opt/app/requirements.txt

# set working directory to /opt/app
WORKDIR /opt/app

# install anaconda and all software requirements in requirements.txt
RUN pip3 install virtualenv
RUN virtualenv venv && \
    . venv/bin/activate

# Copy the Python script into /opt/app
COPY . /opt/app

# start app
CMD [ "python3", "hello_world.py" ]