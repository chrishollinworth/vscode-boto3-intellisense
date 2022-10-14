"""
Type annotations for ds service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_ds import DirectoryServiceClient
    from mypy_boto3_ds.paginator import (
        DescribeDirectoriesPaginator,
        DescribeDomainControllersPaginator,
        DescribeSharedDirectoriesPaginator,
        DescribeSnapshotsPaginator,
        DescribeTrustsPaginator,
        ListIpRoutesPaginator,
        ListLogSubscriptionsPaginator,
        ListSchemaExtensionsPaginator,
        ListTagsForResourcePaginator,
    )

    client: DirectoryServiceClient = boto3.client("ds")

    describe_directories_paginator: DescribeDirectoriesPaginator = client.get_paginator("describe_directories")
    describe_domain_controllers_paginator: DescribeDomainControllersPaginator = client.get_paginator("describe_domain_controllers")
    describe_shared_directories_paginator: DescribeSharedDirectoriesPaginator = client.get_paginator("describe_shared_directories")
    describe_snapshots_paginator: DescribeSnapshotsPaginator = client.get_paginator("describe_snapshots")
    describe_trusts_paginator: DescribeTrustsPaginator = client.get_paginator("describe_trusts")
    list_ip_routes_paginator: ListIpRoutesPaginator = client.get_paginator("list_ip_routes")
    list_log_subscriptions_paginator: ListLogSubscriptionsPaginator = client.get_paginator("list_log_subscriptions")
    list_schema_extensions_paginator: ListSchemaExtensionsPaginator = client.get_paginator("list_schema_extensions")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    DescribeDirectoriesResultTypeDef,
    DescribeDomainControllersResultTypeDef,
    DescribeSharedDirectoriesResultTypeDef,
    DescribeSnapshotsResultTypeDef,
    DescribeTrustsResultTypeDef,
    ListIpRoutesResultTypeDef,
    ListLogSubscriptionsResultTypeDef,
    ListSchemaExtensionsResultTypeDef,
    ListTagsForResourceResultTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeDirectoriesPaginator",
    "DescribeDomainControllersPaginator",
    "DescribeSharedDirectoriesPaginator",
    "DescribeSnapshotsPaginator",
    "DescribeTrustsPaginator",
    "ListIpRoutesPaginator",
    "ListLogSubscriptionsPaginator",
    "ListSchemaExtensionsPaginator",
    "ListTagsForResourcePaginator",
)

class DescribeDirectoriesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ds.html#DirectoryService.Paginator.DescribeDirectories)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describedirectoriespaginator)
    """

    def paginate(
        self, *, DirectoryIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDirectoriesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ds.html#DirectoryService.Paginator.DescribeDirectories.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describedirectoriespaginator)
        """

class DescribeDomainControllersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ds.html#DirectoryService.Paginator.DescribeDomainControllers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describedomaincontrollerspaginator)
    """

    def paginate(
        self,
        *,
        DirectoryId: str,
        DomainControllerIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDomainControllersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ds.html#DirectoryService.Paginator.DescribeDomainControllers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describedomaincontrollerspaginator)
        """

class DescribeSharedDirectoriesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ds.html#DirectoryService.Paginator.DescribeSharedDirectories)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describeshareddirectoriespaginator)
    """

    def paginate(
        self,
        *,
        OwnerDirectoryId: str,
        SharedDirectoryIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSharedDirectoriesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ds.html#DirectoryService.Paginator.DescribeSharedDirectories.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describeshareddirectoriespaginator)
        """

class DescribeSnapshotsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ds.html#DirectoryService.Paginator.DescribeSnapshots)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describesnapshotspaginator)
    """

    def paginate(
        self,
        *,
        DirectoryId: str = None,
        SnapshotIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSnapshotsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ds.html#DirectoryService.Paginator.DescribeSnapshots.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describesnapshotspaginator)
        """

class DescribeTrustsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ds.html#DirectoryService.Paginator.DescribeTrusts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describetrustspaginator)
    """

    def paginate(
        self,
        *,
        DirectoryId: str = None,
        TrustIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTrustsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ds.html#DirectoryService.Paginator.DescribeTrusts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describetrustspaginator)
        """

class ListIpRoutesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ds.html#DirectoryService.Paginator.ListIpRoutes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listiproutespaginator)
    """

    def paginate(
        self, *, DirectoryId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIpRoutesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ds.html#DirectoryService.Paginator.ListIpRoutes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listiproutespaginator)
        """

class ListLogSubscriptionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ds.html#DirectoryService.Paginator.ListLogSubscriptions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listlogsubscriptionspaginator)
    """

    def paginate(
        self, *, DirectoryId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLogSubscriptionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ds.html#DirectoryService.Paginator.ListLogSubscriptions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listlogsubscriptionspaginator)
        """

class ListSchemaExtensionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ds.html#DirectoryService.Paginator.ListSchemaExtensions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listschemaextensionspaginator)
    """

    def paginate(
        self, *, DirectoryId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSchemaExtensionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ds.html#DirectoryService.Paginator.ListSchemaExtensions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listschemaextensionspaginator)
        """

class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ds.html#DirectoryService.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listtagsforresourcepaginator)
    """

    def paginate(
        self, *, ResourceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/ds.html#DirectoryService.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listtagsforresourcepaginator)
        """
