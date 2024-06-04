"""
Main interface for timestream-influxdb service.

Usage::

    ```python
    import boto3
    from mypy_boto3_timestream_influxdb import (
        Client,
        ListDbInstancesPaginator,
        ListDbParameterGroupsPaginator,
        TimestreamInfluxDBClient,
    )

    session = boto3.Session()

    client: TimestreamInfluxDBClient = boto3.client("timestream-influxdb")
    session_client: TimestreamInfluxDBClient = session.client("timestream-influxdb")

    list_db_instances_paginator: ListDbInstancesPaginator = client.get_paginator("list_db_instances")
    list_db_parameter_groups_paginator: ListDbParameterGroupsPaginator = client.get_paginator("list_db_parameter_groups")
    ```
"""

from .client import TimestreamInfluxDBClient
from .paginator import ListDbInstancesPaginator, ListDbParameterGroupsPaginator

Client = TimestreamInfluxDBClient

__all__ = (
    "Client",
    "ListDbInstancesPaginator",
    "ListDbParameterGroupsPaginator",
    "TimestreamInfluxDBClient",
)
