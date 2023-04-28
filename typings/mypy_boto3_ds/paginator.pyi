"""
Type annotations for ds service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_ds import DirectoryServiceClient
    from mypy_boto3_ds.paginator import (
        DescribeClientAuthenticationSettingsPaginator,
        DescribeDirectoriesPaginator,
        DescribeDomainControllersPaginator,
        DescribeLDAPSSettingsPaginator,
        DescribeRegionsPaginator,
        DescribeSharedDirectoriesPaginator,
        DescribeSnapshotsPaginator,
        DescribeTrustsPaginator,
        DescribeUpdateDirectoryPaginator,
        ListCertificatesPaginator,
        ListIpRoutesPaginator,
        ListLogSubscriptionsPaginator,
        ListSchemaExtensionsPaginator,
        ListTagsForResourcePaginator,
    )

    client: DirectoryServiceClient = boto3.client("ds")

    describe_client_authentication_settings_paginator: DescribeClientAuthenticationSettingsPaginator = client.get_paginator("describe_client_authentication_settings")
    describe_directories_paginator: DescribeDirectoriesPaginator = client.get_paginator("describe_directories")
    describe_domain_controllers_paginator: DescribeDomainControllersPaginator = client.get_paginator("describe_domain_controllers")
    describe_ldaps_settings_paginator: DescribeLDAPSSettingsPaginator = client.get_paginator("describe_ldaps_settings")
    describe_regions_paginator: DescribeRegionsPaginator = client.get_paginator("describe_regions")
    describe_shared_directories_paginator: DescribeSharedDirectoriesPaginator = client.get_paginator("describe_shared_directories")
    describe_snapshots_paginator: DescribeSnapshotsPaginator = client.get_paginator("describe_snapshots")
    describe_trusts_paginator: DescribeTrustsPaginator = client.get_paginator("describe_trusts")
    describe_update_directory_paginator: DescribeUpdateDirectoryPaginator = client.get_paginator("describe_update_directory")
    list_certificates_paginator: ListCertificatesPaginator = client.get_paginator("list_certificates")
    list_ip_routes_paginator: ListIpRoutesPaginator = client.get_paginator("list_ip_routes")
    list_log_subscriptions_paginator: ListLogSubscriptionsPaginator = client.get_paginator("list_log_subscriptions")
    list_schema_extensions_paginator: ListSchemaExtensionsPaginator = client.get_paginator("list_schema_extensions")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""
import sys
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ClientAuthenticationTypeType
from .type_defs import (
    DescribeClientAuthenticationSettingsResultTypeDef,
    DescribeDirectoriesResultTypeDef,
    DescribeDomainControllersResultTypeDef,
    DescribeLDAPSSettingsResultTypeDef,
    DescribeRegionsResultTypeDef,
    DescribeSharedDirectoriesResultTypeDef,
    DescribeSnapshotsResultTypeDef,
    DescribeTrustsResultTypeDef,
    DescribeUpdateDirectoryResultTypeDef,
    ListCertificatesResultTypeDef,
    ListIpRoutesResultTypeDef,
    ListLogSubscriptionsResultTypeDef,
    ListSchemaExtensionsResultTypeDef,
    ListTagsForResourceResultTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DescribeClientAuthenticationSettingsPaginator",
    "DescribeDirectoriesPaginator",
    "DescribeDomainControllersPaginator",
    "DescribeLDAPSSettingsPaginator",
    "DescribeRegionsPaginator",
    "DescribeSharedDirectoriesPaginator",
    "DescribeSnapshotsPaginator",
    "DescribeTrustsPaginator",
    "DescribeUpdateDirectoryPaginator",
    "ListCertificatesPaginator",
    "ListIpRoutesPaginator",
    "ListLogSubscriptionsPaginator",
    "ListSchemaExtensionsPaginator",
    "ListTagsForResourcePaginator",
)

class DescribeClientAuthenticationSettingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.DescribeClientAuthenticationSettings)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describeclientauthenticationsettingspaginator)
    """

    def paginate(
        self,
        *,
        DirectoryId: str,
        Type: ClientAuthenticationTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeClientAuthenticationSettingsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.DescribeClientAuthenticationSettings.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describeclientauthenticationsettingspaginator)
        """

class DescribeDirectoriesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.DescribeDirectories)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describedirectoriespaginator)
    """

    def paginate(
        self, *, DirectoryIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDirectoriesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.DescribeDirectories.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describedirectoriespaginator)
        """

class DescribeDomainControllersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.DescribeDomainControllers)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.DescribeDomainControllers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describedomaincontrollerspaginator)
        """

class DescribeLDAPSSettingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.DescribeLDAPSSettings)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describeldapssettingspaginator)
    """

    def paginate(
        self,
        *,
        DirectoryId: str,
        Type: Literal["Client"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLDAPSSettingsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.DescribeLDAPSSettings.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describeldapssettingspaginator)
        """

class DescribeRegionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.DescribeRegions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describeregionspaginator)
    """

    def paginate(
        self,
        *,
        DirectoryId: str,
        RegionName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeRegionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.DescribeRegions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describeregionspaginator)
        """

class DescribeSharedDirectoriesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.DescribeSharedDirectories)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.DescribeSharedDirectories.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describeshareddirectoriespaginator)
        """

class DescribeSnapshotsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.DescribeSnapshots)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.DescribeSnapshots.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describesnapshotspaginator)
        """

class DescribeTrustsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.DescribeTrusts)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.DescribeTrusts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describetrustspaginator)
        """

class DescribeUpdateDirectoryPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.DescribeUpdateDirectory)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describeupdatedirectorypaginator)
    """

    def paginate(
        self,
        *,
        DirectoryId: str,
        UpdateType: Literal["OS"],
        RegionName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeUpdateDirectoryResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.DescribeUpdateDirectory.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describeupdatedirectorypaginator)
        """

class ListCertificatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.ListCertificates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listcertificatespaginator)
    """

    def paginate(
        self, *, DirectoryId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCertificatesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.ListCertificates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listcertificatespaginator)
        """

class ListIpRoutesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.ListIpRoutes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listiproutespaginator)
    """

    def paginate(
        self, *, DirectoryId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIpRoutesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.ListIpRoutes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listiproutespaginator)
        """

class ListLogSubscriptionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.ListLogSubscriptions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listlogsubscriptionspaginator)
    """

    def paginate(
        self, *, DirectoryId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLogSubscriptionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.ListLogSubscriptions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listlogsubscriptionspaginator)
        """

class ListSchemaExtensionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.ListSchemaExtensions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listschemaextensionspaginator)
    """

    def paginate(
        self, *, DirectoryId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSchemaExtensionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.ListSchemaExtensions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listschemaextensionspaginator)
        """

class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listtagsforresourcepaginator)
    """

    def paginate(
        self, *, ResourceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/ds.html#DirectoryService.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listtagsforresourcepaginator)
        """
