"""
Type annotations for timestream-influxdb service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/literals.html)

Usage::

    ```python
    from mypy_boto3_timestream_influxdb.literals import DbInstanceTypeType

    data: DbInstanceTypeType = "db.influx.12xlarge"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DbInstanceTypeType",
    "DbStorageTypeType",
    "DeploymentTypeType",
    "ListDbInstancesPaginatorName",
    "ListDbParameterGroupsPaginatorName",
    "LogLevelType",
    "StatusType",
    "TracingTypeType",
)

DbInstanceTypeType = Literal[
    "db.influx.12xlarge",
    "db.influx.16xlarge",
    "db.influx.2xlarge",
    "db.influx.4xlarge",
    "db.influx.8xlarge",
    "db.influx.large",
    "db.influx.medium",
    "db.influx.xlarge",
]
DbStorageTypeType = Literal["InfluxIOIncludedT1", "InfluxIOIncludedT2", "InfluxIOIncludedT3"]
DeploymentTypeType = Literal["SINGLE_AZ", "WITH_MULTIAZ_STANDBY"]
ListDbInstancesPaginatorName = Literal["list_db_instances"]
ListDbParameterGroupsPaginatorName = Literal["list_db_parameter_groups"]
LogLevelType = Literal["debug", "error", "info"]
StatusType = Literal[
    "AVAILABLE", "CREATING", "DELETED", "DELETING", "FAILED", "MODIFYING", "UPDATING"
]
TracingTypeType = Literal["jaeger", "log"]
