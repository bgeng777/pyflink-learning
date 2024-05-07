from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common import Types, Configuration
from pyflink.table import DataTypes, StreamTableEnvironment
from datetime import datetime
import pytz


config = Configuration()
config.set_string("python.client.executable", "/usr/local/Caskroom/miniconda/base/envs/myenv/bin/python")
config.set_string("python.executable", "/usr/local/Caskroom/miniconda/base/envs/myenv/bin/python")
env = StreamExecutionEnvironment.get_execution_environment(config)
t_env = StreamTableEnvironment.create(env)
t_env.get_config().set_local_timezone("UTC")
# t_env.get_config().set_local_timezone("GMT-08:00")

input_table = t_env.from_elements(
    [
        (
            "elementA",
            datetime(year=2024, month=4, day=12, hour=8, minute=35),
        ),
        (
            "elementB",
            datetime(year=2024, month=4, day=12, hour=8, minute=35, tzinfo=pytz.utc),
            # datetime(year=2024, month=4, day=12, hour=8, minute=35, tzinfo=pytz.timezone('America/New_York')),
        ),
    ],
    DataTypes.ROW(
        [
            DataTypes.FIELD("name", DataTypes.STRING()),
            DataTypes.FIELD("timestamp", DataTypes.TIMESTAMP_LTZ(3)),
        ]
    ),
)
input_table.execute().print()

# SQL
sql_result = t_env.execute_sql("CREATE VIEW MyView1 AS SELECT TO_TIMESTAMP_LTZ(1712910900000, 3);")
t_env.execute_sql("CREATE TABLE Sink (`t` TIMESTAMP_LTZ) WITH ('connector'='print');")
t_env.execute_sql("INSERT INTO Sink SELECT * FROM MyView1;")
