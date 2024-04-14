
FROM flink:latest

# Install python3 and pip3
RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev wget && rm -rf /var/lib/apt/lists/*
RUN ln -s /usr/bin/python3 /usr/bin/python

# Install PyFlink
ENV FLINK_VERSION="1.19.0"
WORKDIR /opt/flink
RUN wget https://archive.apache.org/dist/flink/flink-${FLINK_VERSION}/python/apache-flink-${FLINK_VERSION}.tar.gz \
    && wget https://archive.apache.org/dist/flink/flink-${FLINK_VERSION}/python/apache-flink-libraries-${FLINK_VERSION}.tar.gz
RUN pip3 install /opt/flink/apache-flink-${FLINK_VERSION}.tar.gz && pip3 install /opt/flink/apache-flink-libraries-${FLINK_VERSION}.tar.gz

# Download required connectors
RUN wget -P /opt/flink/lib https://repo1.maven.org/maven2/org/apache/flink/flink-sql-connector-kafka/3.1.0-1.18/flink-sql-connector-kafka-3.1.0-1.18.jar
