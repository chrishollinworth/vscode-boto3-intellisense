"""
Type annotations for sms service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_sms.client import SMSClient
    from mypy_boto3_sms.paginator import (
        GetConnectorsPaginator,
        GetReplicationJobsPaginator,
        GetReplicationRunsPaginator,
        GetServersPaginator,
        ListAppsPaginator,
    )

    session = Session()
    client: SMSClient = session.client("sms")

    get_connectors_paginator: GetConnectorsPaginator = client.get_paginator("get_connectors")
    get_replication_jobs_paginator: GetReplicationJobsPaginator = client.get_paginator("get_replication_jobs")
    get_replication_runs_paginator: GetReplicationRunsPaginator = client.get_paginator("get_replication_runs")
    get_servers_paginator: GetServersPaginator = client.get_paginator("get_servers")
    list_apps_paginator: ListAppsPaginator = client.get_paginator("list_apps")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetConnectorsRequestPaginateTypeDef,
    GetConnectorsResponseTypeDef,
    GetReplicationJobsRequestPaginateTypeDef,
    GetReplicationJobsResponseTypeDef,
    GetReplicationRunsRequestPaginateTypeDef,
    GetReplicationRunsResponseTypeDef,
    GetServersRequestPaginateTypeDef,
    GetServersResponseTypeDef,
    ListAppsRequestPaginateTypeDef,
    ListAppsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetConnectorsPaginator",
    "GetReplicationJobsPaginator",
    "GetReplicationRunsPaginator",
    "GetServersPaginator",
    "ListAppsPaginator",
)

if TYPE_CHECKING:
    _GetConnectorsPaginatorBase = Paginator[GetConnectorsResponseTypeDef]
else:
    _GetConnectorsPaginatorBase = Paginator  # type: ignore[assignment]

class GetConnectorsPaginator(_GetConnectorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms/paginator/GetConnectors.html#SMS.Paginator.GetConnectors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators/#getconnectorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetConnectorsRequestPaginateTypeDef]
    ) -> PageIterator[GetConnectorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms/paginator/GetConnectors.html#SMS.Paginator.GetConnectors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators/#getconnectorspaginator)
        """

if TYPE_CHECKING:
    _GetReplicationJobsPaginatorBase = Paginator[GetReplicationJobsResponseTypeDef]
else:
    _GetReplicationJobsPaginatorBase = Paginator  # type: ignore[assignment]

class GetReplicationJobsPaginator(_GetReplicationJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms/paginator/GetReplicationJobs.html#SMS.Paginator.GetReplicationJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators/#getreplicationjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetReplicationJobsRequestPaginateTypeDef]
    ) -> PageIterator[GetReplicationJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms/paginator/GetReplicationJobs.html#SMS.Paginator.GetReplicationJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators/#getreplicationjobspaginator)
        """

if TYPE_CHECKING:
    _GetReplicationRunsPaginatorBase = Paginator[GetReplicationRunsResponseTypeDef]
else:
    _GetReplicationRunsPaginatorBase = Paginator  # type: ignore[assignment]

class GetReplicationRunsPaginator(_GetReplicationRunsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms/paginator/GetReplicationRuns.html#SMS.Paginator.GetReplicationRuns)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators/#getreplicationrunspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetReplicationRunsRequestPaginateTypeDef]
    ) -> PageIterator[GetReplicationRunsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms/paginator/GetReplicationRuns.html#SMS.Paginator.GetReplicationRuns.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators/#getreplicationrunspaginator)
        """

if TYPE_CHECKING:
    _GetServersPaginatorBase = Paginator[GetServersResponseTypeDef]
else:
    _GetServersPaginatorBase = Paginator  # type: ignore[assignment]

class GetServersPaginator(_GetServersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms/paginator/GetServers.html#SMS.Paginator.GetServers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators/#getserverspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetServersRequestPaginateTypeDef]
    ) -> PageIterator[GetServersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms/paginator/GetServers.html#SMS.Paginator.GetServers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators/#getserverspaginator)
        """

if TYPE_CHECKING:
    _ListAppsPaginatorBase = Paginator[ListAppsResponseTypeDef]
else:
    _ListAppsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAppsPaginator(_ListAppsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms/paginator/ListApps.html#SMS.Paginator.ListApps)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators/#listappspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAppsRequestPaginateTypeDef]
    ) -> PageIterator[ListAppsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms/paginator/ListApps.html#SMS.Paginator.ListApps.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators/#listappspaginator)
        """
