FROM pyflink:latest
COPY read_kafka_and_print.py submit.sh /opt/flink/
RUN chmod 777 /opt/flink/submit.sh