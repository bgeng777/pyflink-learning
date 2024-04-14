from pyflink.table import (EnvironmentSettings, TableEnvironment)

def process_table():
    env_settings = (
        EnvironmentSettings
        .new_instance()
        .in_streaming_mode()
        .build()
    )
    t_env = TableEnvironment.create(EnvironmentSettings.in_streaming_mode())


    t_env.execute_sql(
        f"""
    CREATE TABLE kafka_input_topic (
    action STRING
    ) WITH (
    'connector' = 'kafka',
    'topic' = 'input_topic',
    'properties.bootstrap.servers' = 'kafka:9092',
    'properties.group.id' = 'test',
    'scan.startup.mode' = 'earliest-offset',
    'format' = 'json',
    'json.ignore-parse-errors' = 'true'
    )
    """)
    
    t_env.execute_sql(
        f"""
    CREATE TABLE print_sink (
    action STRING
    ) WITH (
    'connector' = 'print'
    )
    """)

    t_env.execute_sql("""
    INSERT INTO print_sink SELECT * FROM kafka_input_topic
    """).print()

if __name__ == "__main__":
    process_table()
