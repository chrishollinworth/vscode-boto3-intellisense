# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for sms service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_sms import SMSClient
    from mypy_boto3_sms.paginator import (
        GetConnectorsPaginator,
        GetReplicationJobsPaginator,
        GetReplicationRunsPaginator,
        GetServersPaginator,
        ListAppsPaginator,
    )

    client: SMSClient = boto3.client("sms")

    get_connectors_paginator: GetConnectorsPaginator = client.get_paginator("get_connectors")
    get_replication_jobs_paginator: GetReplicationJobsPaginator = client.get_paginator("get_replication_jobs")
    get_replication_runs_paginator: GetReplicationRunsPaginator = client.get_paginator("get_replication_runs")
    get_servers_paginator: GetServersPaginator = client.get_paginator("get_servers")
    list_apps_paginator: ListAppsPaginator = client.get_paginator("list_apps")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_sms.type_defs import (
    GetConnectorsResponseTypeDef,
    GetReplicationJobsResponseTypeDef,
    GetReplicationRunsResponseTypeDef,
    GetServersResponseTypeDef,
    ListAppsResponseTypeDef,
    PaginatorConfigTypeDef,
    VmServerAddressTypeDef,
)

__all__ = (
    "GetConnectorsPaginator",
    "GetReplicationJobsPaginator",
    "GetReplicationRunsPaginator",
    "GetServersPaginator",
    "ListAppsPaginator",
)


class GetConnectorsPaginator(Boto3Paginator):
    """
    [Paginator.GetConnectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Paginator.GetConnectors)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetConnectorsResponseTypeDef]:
        """
        [GetConnectors.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Paginator.GetConnectors.paginate)
        """


class GetReplicationJobsPaginator(Boto3Paginator):
    """
    [Paginator.GetReplicationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Paginator.GetReplicationJobs)
    """

    def paginate(
        self, replicationJobId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetReplicationJobsResponseTypeDef]:
        """
        [GetReplicationJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Paginator.GetReplicationJobs.paginate)
        """


class GetReplicationRunsPaginator(Boto3Paginator):
    """
    [Paginator.GetReplicationRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Paginator.GetReplicationRuns)
    """

    def paginate(
        self, replicationJobId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetReplicationRunsResponseTypeDef]:
        """
        [GetReplicationRuns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Paginator.GetReplicationRuns.paginate)
        """


class GetServersPaginator(Boto3Paginator):
    """
    [Paginator.GetServers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Paginator.GetServers)
    """

    def paginate(
        self,
        vmServerAddressList: List["VmServerAddressTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetServersResponseTypeDef]:
        """
        [GetServers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Paginator.GetServers.paginate)
        """


class ListAppsPaginator(Boto3Paginator):
    """
    [Paginator.ListApps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Paginator.ListApps)
    """

    def paginate(
        self, appIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAppsResponseTypeDef]:
        """
        [ListApps.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sms.html#SMS.Paginator.ListApps.paginate)
        """
