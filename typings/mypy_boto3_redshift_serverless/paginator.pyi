"""
Type annotations for redshift-serverless service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_redshift_serverless import RedshiftServerlessClient
    from mypy_boto3_redshift_serverless.paginator import (
        ListEndpointAccessPaginator,
        ListNamespacesPaginator,
        ListRecoveryPointsPaginator,
        ListSnapshotsPaginator,
        ListUsageLimitsPaginator,
        ListWorkgroupsPaginator,
    )

    client: RedshiftServerlessClient = boto3.client("redshift-serverless")

    list_endpoint_access_paginator: ListEndpointAccessPaginator = client.get_paginator("list_endpoint_access")
    list_namespaces_paginator: ListNamespacesPaginator = client.get_paginator("list_namespaces")
    list_recovery_points_paginator: ListRecoveryPointsPaginator = client.get_paginator("list_recovery_points")
    list_snapshots_paginator: ListSnapshotsPaginator = client.get_paginator("list_snapshots")
    list_usage_limits_paginator: ListUsageLimitsPaginator = client.get_paginator("list_usage_limits")
    list_workgroups_paginator: ListWorkgroupsPaginator = client.get_paginator("list_workgroups")
    ```
"""
from datetime import datetime
from typing import Iterator, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import UsageLimitUsageTypeType
from .type_defs import (
    ListEndpointAccessResponseTypeDef,
    ListNamespacesResponseTypeDef,
    ListRecoveryPointsResponseTypeDef,
    ListSnapshotsResponseTypeDef,
    ListUsageLimitsResponseTypeDef,
    ListWorkgroupsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListEndpointAccessPaginator",
    "ListNamespacesPaginator",
    "ListRecoveryPointsPaginator",
    "ListSnapshotsPaginator",
    "ListUsageLimitsPaginator",
    "ListWorkgroupsPaginator",
)

class ListEndpointAccessPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListEndpointAccess)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators.html#listendpointaccesspaginator)
    """

    def paginate(
        self,
        *,
        vpcId: str = None,
        workgroupName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEndpointAccessResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListEndpointAccess.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators.html#listendpointaccesspaginator)
        """

class ListNamespacesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListNamespaces)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators.html#listnamespacespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNamespacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListNamespaces.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators.html#listnamespacespaginator)
        """

class ListRecoveryPointsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListRecoveryPoints)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators.html#listrecoverypointspaginator)
    """

    def paginate(
        self,
        *,
        endTime: Union[datetime, str] = None,
        namespaceName: str = None,
        startTime: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRecoveryPointsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListRecoveryPoints.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators.html#listrecoverypointspaginator)
        """

class ListSnapshotsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListSnapshots)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators.html#listsnapshotspaginator)
    """

    def paginate(
        self,
        *,
        endTime: Union[datetime, str] = None,
        namespaceArn: str = None,
        namespaceName: str = None,
        ownerAccount: str = None,
        startTime: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSnapshotsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListSnapshots.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators.html#listsnapshotspaginator)
        """

class ListUsageLimitsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListUsageLimits)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators.html#listusagelimitspaginator)
    """

    def paginate(
        self,
        *,
        resourceArn: str = None,
        usageType: UsageLimitUsageTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUsageLimitsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListUsageLimits.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators.html#listusagelimitspaginator)
        """

class ListWorkgroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListWorkgroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators.html#listworkgroupspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorkgroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListWorkgroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators.html#listworkgroupspaginator)
        """
