"""
Main interface for timestream-influxdb service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_timestream_influxdb import (
        Client,
        ListDbClustersPaginator,
        ListDbInstancesForClusterPaginator,
        ListDbInstancesPaginator,
        ListDbParameterGroupsPaginator,
        TimestreamInfluxDBClient,
    )

    session = Session()
    client: TimestreamInfluxDBClient = session.client("timestream-influxdb")

    list_db_clusters_paginator: ListDbClustersPaginator = client.get_paginator("list_db_clusters")
    list_db_instances_for_cluster_paginator: ListDbInstancesForClusterPaginator = client.get_paginator("list_db_instances_for_cluster")
    list_db_instances_paginator: ListDbInstancesPaginator = client.get_paginator("list_db_instances")
    list_db_parameter_groups_paginator: ListDbParameterGroupsPaginator = client.get_paginator("list_db_parameter_groups")
    ```
"""

from .client import TimestreamInfluxDBClient
from .paginator import (
    ListDbClustersPaginator,
    ListDbInstancesForClusterPaginator,
    ListDbInstancesPaginator,
    ListDbParameterGroupsPaginator,
)

Client = TimestreamInfluxDBClient

__all__ = (
    "Client",
    "ListDbClustersPaginator",
    "ListDbInstancesForClusterPaginator",
    "ListDbInstancesPaginator",
    "ListDbParameterGroupsPaginator",
    "TimestreamInfluxDBClient",
)
