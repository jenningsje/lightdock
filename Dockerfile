# start from base
FROM ubuntu:18.04

# install system-wide deps for python and node
RUN apt-get -yqq update && \
    apt-get -yqq install python3-pip python3-dev curl gnupg && \
    apt-get install -y wget

# install anaconda
RUN pip3 install virtualenv
RUN virtualenv venv && \
    . venv/bin/activate

# Set the working directory inside the container
RUN pip3 install Cython==3.0.9

# Copy the Python script into the container
COPY hello_world.py . 

# start app
CMD [ "python3", "hello_world.py" ]