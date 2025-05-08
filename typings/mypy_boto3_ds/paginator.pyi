"""
Type annotations for ds service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_ds.client import DirectoryServiceClient
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

    session = Session()
    client: DirectoryServiceClient = session.client("ds")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeClientAuthenticationSettingsRequestPaginateTypeDef,
    DescribeClientAuthenticationSettingsResultTypeDef,
    DescribeDirectoriesRequestPaginateTypeDef,
    DescribeDirectoriesResultTypeDef,
    DescribeDomainControllersRequestPaginateTypeDef,
    DescribeDomainControllersResultTypeDef,
    DescribeLDAPSSettingsRequestPaginateTypeDef,
    DescribeLDAPSSettingsResultTypeDef,
    DescribeRegionsRequestPaginateTypeDef,
    DescribeRegionsResultTypeDef,
    DescribeSharedDirectoriesRequestPaginateTypeDef,
    DescribeSharedDirectoriesResultTypeDef,
    DescribeSnapshotsRequestPaginateTypeDef,
    DescribeSnapshotsResultTypeDef,
    DescribeTrustsRequestPaginateTypeDef,
    DescribeTrustsResultTypeDef,
    DescribeUpdateDirectoryRequestPaginateTypeDef,
    DescribeUpdateDirectoryResultTypeDef,
    ListCertificatesRequestPaginateTypeDef,
    ListCertificatesResultTypeDef,
    ListIpRoutesRequestPaginateTypeDef,
    ListIpRoutesResultTypeDef,
    ListLogSubscriptionsRequestPaginateTypeDef,
    ListLogSubscriptionsResultTypeDef,
    ListSchemaExtensionsRequestPaginateTypeDef,
    ListSchemaExtensionsResultTypeDef,
    ListTagsForResourceRequestPaginateTypeDef,
    ListTagsForResourceResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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

if TYPE_CHECKING:
    _DescribeClientAuthenticationSettingsPaginatorBase = Paginator[
        DescribeClientAuthenticationSettingsResultTypeDef
    ]
else:
    _DescribeClientAuthenticationSettingsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeClientAuthenticationSettingsPaginator(
    _DescribeClientAuthenticationSettingsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/DescribeClientAuthenticationSettings.html#DirectoryService.Paginator.DescribeClientAuthenticationSettings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#describeclientauthenticationsettingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClientAuthenticationSettingsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeClientAuthenticationSettingsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/DescribeClientAuthenticationSettings.html#DirectoryService.Paginator.DescribeClientAuthenticationSettings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#describeclientauthenticationsettingspaginator)
        """

if TYPE_CHECKING:
    _DescribeDirectoriesPaginatorBase = Paginator[DescribeDirectoriesResultTypeDef]
else:
    _DescribeDirectoriesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDirectoriesPaginator(_DescribeDirectoriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/DescribeDirectories.html#DirectoryService.Paginator.DescribeDirectories)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#describedirectoriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDirectoriesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeDirectoriesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/DescribeDirectories.html#DirectoryService.Paginator.DescribeDirectories.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#describedirectoriespaginator)
        """

if TYPE_CHECKING:
    _DescribeDomainControllersPaginatorBase = Paginator[DescribeDomainControllersResultTypeDef]
else:
    _DescribeDomainControllersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDomainControllersPaginator(_DescribeDomainControllersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/DescribeDomainControllers.html#DirectoryService.Paginator.DescribeDomainControllers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#describedomaincontrollerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDomainControllersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeDomainControllersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/DescribeDomainControllers.html#DirectoryService.Paginator.DescribeDomainControllers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#describedomaincontrollerspaginator)
        """

if TYPE_CHECKING:
    _DescribeLDAPSSettingsPaginatorBase = Paginator[DescribeLDAPSSettingsResultTypeDef]
else:
    _DescribeLDAPSSettingsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeLDAPSSettingsPaginator(_DescribeLDAPSSettingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/DescribeLDAPSSettings.html#DirectoryService.Paginator.DescribeLDAPSSettings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#describeldapssettingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeLDAPSSettingsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeLDAPSSettingsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/DescribeLDAPSSettings.html#DirectoryService.Paginator.DescribeLDAPSSettings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#describeldapssettingspaginator)
        """

if TYPE_CHECKING:
    _DescribeRegionsPaginatorBase = Paginator[DescribeRegionsResultTypeDef]
else:
    _DescribeRegionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeRegionsPaginator(_DescribeRegionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/DescribeRegions.html#DirectoryService.Paginator.DescribeRegions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#describeregionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeRegionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeRegionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/DescribeRegions.html#DirectoryService.Paginator.DescribeRegions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#describeregionspaginator)
        """

if TYPE_CHECKING:
    _DescribeSharedDirectoriesPaginatorBase = Paginator[DescribeSharedDirectoriesResultTypeDef]
else:
    _DescribeSharedDirectoriesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSharedDirectoriesPaginator(_DescribeSharedDirectoriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/DescribeSharedDirectories.html#DirectoryService.Paginator.DescribeSharedDirectories)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#describeshareddirectoriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSharedDirectoriesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSharedDirectoriesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/DescribeSharedDirectories.html#DirectoryService.Paginator.DescribeSharedDirectories.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#describeshareddirectoriespaginator)
        """

if TYPE_CHECKING:
    _DescribeSnapshotsPaginatorBase = Paginator[DescribeSnapshotsResultTypeDef]
else:
    _DescribeSnapshotsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSnapshotsPaginator(_DescribeSnapshotsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/DescribeSnapshots.html#DirectoryService.Paginator.DescribeSnapshots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#describesnapshotspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSnapshotsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSnapshotsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/DescribeSnapshots.html#DirectoryService.Paginator.DescribeSnapshots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#describesnapshotspaginator)
        """

if TYPE_CHECKING:
    _DescribeTrustsPaginatorBase = Paginator[DescribeTrustsResultTypeDef]
else:
    _DescribeTrustsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTrustsPaginator(_DescribeTrustsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/DescribeTrusts.html#DirectoryService.Paginator.DescribeTrusts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#describetrustspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTrustsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeTrustsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/DescribeTrusts.html#DirectoryService.Paginator.DescribeTrusts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#describetrustspaginator)
        """

if TYPE_CHECKING:
    _DescribeUpdateDirectoryPaginatorBase = Paginator[DescribeUpdateDirectoryResultTypeDef]
else:
    _DescribeUpdateDirectoryPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeUpdateDirectoryPaginator(_DescribeUpdateDirectoryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/DescribeUpdateDirectory.html#DirectoryService.Paginator.DescribeUpdateDirectory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#describeupdatedirectorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeUpdateDirectoryRequestPaginateTypeDef]
    ) -> PageIterator[DescribeUpdateDirectoryResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/DescribeUpdateDirectory.html#DirectoryService.Paginator.DescribeUpdateDirectory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#describeupdatedirectorypaginator)
        """

if TYPE_CHECKING:
    _ListCertificatesPaginatorBase = Paginator[ListCertificatesResultTypeDef]
else:
    _ListCertificatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListCertificatesPaginator(_ListCertificatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/ListCertificates.html#DirectoryService.Paginator.ListCertificates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#listcertificatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCertificatesRequestPaginateTypeDef]
    ) -> PageIterator[ListCertificatesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/ListCertificates.html#DirectoryService.Paginator.ListCertificates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#listcertificatespaginator)
        """

if TYPE_CHECKING:
    _ListIpRoutesPaginatorBase = Paginator[ListIpRoutesResultTypeDef]
else:
    _ListIpRoutesPaginatorBase = Paginator  # type: ignore[assignment]

class ListIpRoutesPaginator(_ListIpRoutesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/ListIpRoutes.html#DirectoryService.Paginator.ListIpRoutes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#listiproutespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIpRoutesRequestPaginateTypeDef]
    ) -> PageIterator[ListIpRoutesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/ListIpRoutes.html#DirectoryService.Paginator.ListIpRoutes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#listiproutespaginator)
        """

if TYPE_CHECKING:
    _ListLogSubscriptionsPaginatorBase = Paginator[ListLogSubscriptionsResultTypeDef]
else:
    _ListLogSubscriptionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListLogSubscriptionsPaginator(_ListLogSubscriptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/ListLogSubscriptions.html#DirectoryService.Paginator.ListLogSubscriptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#listlogsubscriptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLogSubscriptionsRequestPaginateTypeDef]
    ) -> PageIterator[ListLogSubscriptionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/ListLogSubscriptions.html#DirectoryService.Paginator.ListLogSubscriptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#listlogsubscriptionspaginator)
        """

if TYPE_CHECKING:
    _ListSchemaExtensionsPaginatorBase = Paginator[ListSchemaExtensionsResultTypeDef]
else:
    _ListSchemaExtensionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSchemaExtensionsPaginator(_ListSchemaExtensionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/ListSchemaExtensions.html#DirectoryService.Paginator.ListSchemaExtensions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#listschemaextensionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSchemaExtensionsRequestPaginateTypeDef]
    ) -> PageIterator[ListSchemaExtensionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/ListSchemaExtensions.html#DirectoryService.Paginator.ListSchemaExtensions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#listschemaextensionspaginator)
        """

if TYPE_CHECKING:
    _ListTagsForResourcePaginatorBase = Paginator[ListTagsForResourceResultTypeDef]
else:
    _ListTagsForResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListTagsForResourcePaginator(_ListTagsForResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/ListTagsForResource.html#DirectoryService.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#listtagsforresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsForResourceRequestPaginateTypeDef]
    ) -> PageIterator[ListTagsForResourceResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/paginator/ListTagsForResource.html#DirectoryService.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators/#listtagsforresourcepaginator)
        """
