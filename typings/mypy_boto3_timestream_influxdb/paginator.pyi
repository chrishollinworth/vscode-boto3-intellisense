"""
Type annotations for timestream-influxdb service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_timestream_influxdb import TimestreamInfluxDBClient
    from mypy_boto3_timestream_influxdb.paginator import (
        ListDbInstancesPaginator,
        ListDbParameterGroupsPaginator,
    )

    client: TimestreamInfluxDBClient = boto3.client("timestream-influxdb")

    list_db_instances_paginator: ListDbInstancesPaginator = client.get_paginator("list_db_instances")
    list_db_parameter_groups_paginator: ListDbParameterGroupsPaginator = client.get_paginator("list_db_parameter_groups")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListDbInstancesOutputTypeDef,
    ListDbParameterGroupsOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListDbInstancesPaginator", "ListDbParameterGroupsPaginator")

class ListDbInstancesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/timestream-influxdb.html#TimestreamInfluxDB.Paginator.ListDbInstances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/paginators.html#listdbinstancespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDbInstancesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/timestream-influxdb.html#TimestreamInfluxDB.Paginator.ListDbInstances.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/paginators.html#listdbinstancespaginator)
        """

class ListDbParameterGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/timestream-influxdb.html#TimestreamInfluxDB.Paginator.ListDbParameterGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/paginators.html#listdbparametergroupspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDbParameterGroupsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/timestream-influxdb.html#TimestreamInfluxDB.Paginator.ListDbParameterGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/paginators.html#listdbparametergroupspaginator)
        """
