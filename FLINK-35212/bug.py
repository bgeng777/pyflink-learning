from pyflink.common.types import Row
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common import Types, WatermarkStrategy, Configuration
from pyflink.table import EnvironmentSettings, TableEnvironment
from pyflink.table import StreamTableEnvironment, Schema
from pyflink.datastream.functions import ProcessFunction, MapFunction
from pyflink.common.time import Instant


# init task env
config = Configuration()
config.set_string("python.execution-mode", "thread")
# config.set_string("python.execution-mode", "process")
config.set_string("python.client.executable", "/usr/local/Caskroom/miniconda/base/envs/myenv/bin/python")
config.set_string("python.executable", "/usr/local/Caskroom/miniconda/base/envs/myenv/bin/python")

env = StreamExecutionEnvironment.get_execution_environment(config)
table_env = StreamTableEnvironment.create(env)

# create a batch TableEnvironment
table = table_env.from_elements([(1, 'Hi'), (2, 'Hello')]).alias("id", "content")
table_env.create_temporary_view("test_table", table)

result_table = table_env.sql_query("select *, NOW() as dt from test_table")
result_ds = table_env.to_data_stream(result_table)

# def test_func(row):
#     return row

# result_ds.map(test_func).print()
result_ds.print()

env.execute()