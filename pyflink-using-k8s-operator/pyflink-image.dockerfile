
FROM flink:1.18.1

# Install python3 and pip3
RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev wget && rm -rf /var/lib/apt/lists/*
RUN ln -s /usr/bin/python3 /usr/bin/python

# Install PyFlink
ENV FLINK_VERSION="1.18.1"
WORKDIR /opt/flink

RUN pip3 install apache-flink==1.18.1

# add python script
USER flink
RUN mkdir /opt/flink/usrlib
ADD python_demo.py /opt/flink/usrlib/python_demo.py