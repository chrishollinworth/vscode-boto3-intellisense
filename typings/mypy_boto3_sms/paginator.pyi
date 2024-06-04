"""
Type annotations for sms service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators.html)

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

from .type_defs import (
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sms.html#SMS.Paginator.GetConnectors)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators.html#getconnectorspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetConnectorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sms.html#SMS.Paginator.GetConnectors.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators.html#getconnectorspaginator)
        """

class GetReplicationJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sms.html#SMS.Paginator.GetReplicationJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators.html#getreplicationjobspaginator)
    """

    def paginate(
        self, *, replicationJobId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetReplicationJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sms.html#SMS.Paginator.GetReplicationJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators.html#getreplicationjobspaginator)
        """

class GetReplicationRunsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sms.html#SMS.Paginator.GetReplicationRuns)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators.html#getreplicationrunspaginator)
    """

    def paginate(
        self, *, replicationJobId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetReplicationRunsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sms.html#SMS.Paginator.GetReplicationRuns.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators.html#getreplicationrunspaginator)
        """

class GetServersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sms.html#SMS.Paginator.GetServers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators.html#getserverspaginator)
    """

    def paginate(
        self,
        *,
        vmServerAddressList: List["VmServerAddressTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetServersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sms.html#SMS.Paginator.GetServers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators.html#getserverspaginator)
        """

class ListAppsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sms.html#SMS.Paginator.ListApps)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators.html#listappspaginator)
    """

    def paginate(
        self, *, appIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAppsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sms.html#SMS.Paginator.ListApps.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators.html#listappspaginator)
        """
