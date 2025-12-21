"""
Type annotations for cloudfront service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_cloudfront.client import CloudFrontClient
    from mypy_boto3_cloudfront.paginator import (
        ListCloudFrontOriginAccessIdentitiesPaginator,
        ListConnectionFunctionsPaginator,
        ListConnectionGroupsPaginator,
        ListDistributionTenantsByCustomizationPaginator,
        ListDistributionTenantsPaginator,
        ListDistributionsByConnectionFunctionPaginator,
        ListDistributionsByConnectionModePaginator,
        ListDistributionsByTrustStorePaginator,
        ListDistributionsPaginator,
        ListDomainConflictsPaginator,
        ListInvalidationsForDistributionTenantPaginator,
        ListInvalidationsPaginator,
        ListKeyValueStoresPaginator,
        ListOriginAccessControlsPaginator,
        ListPublicKeysPaginator,
        ListStreamingDistributionsPaginator,
        ListTrustStoresPaginator,
    )

    session = Session()
    client: CloudFrontClient = session.client("cloudfront")

    list_cloud_front_origin_access_identities_paginator: ListCloudFrontOriginAccessIdentitiesPaginator = client.get_paginator("list_cloud_front_origin_access_identities")
    list_connection_functions_paginator: ListConnectionFunctionsPaginator = client.get_paginator("list_connection_functions")
    list_connection_groups_paginator: ListConnectionGroupsPaginator = client.get_paginator("list_connection_groups")
    list_distribution_tenants_by_customization_paginator: ListDistributionTenantsByCustomizationPaginator = client.get_paginator("list_distribution_tenants_by_customization")
    list_distribution_tenants_paginator: ListDistributionTenantsPaginator = client.get_paginator("list_distribution_tenants")
    list_distributions_by_connection_function_paginator: ListDistributionsByConnectionFunctionPaginator = client.get_paginator("list_distributions_by_connection_function")
    list_distributions_by_connection_mode_paginator: ListDistributionsByConnectionModePaginator = client.get_paginator("list_distributions_by_connection_mode")
    list_distributions_by_trust_store_paginator: ListDistributionsByTrustStorePaginator = client.get_paginator("list_distributions_by_trust_store")
    list_distributions_paginator: ListDistributionsPaginator = client.get_paginator("list_distributions")
    list_domain_conflicts_paginator: ListDomainConflictsPaginator = client.get_paginator("list_domain_conflicts")
    list_invalidations_for_distribution_tenant_paginator: ListInvalidationsForDistributionTenantPaginator = client.get_paginator("list_invalidations_for_distribution_tenant")
    list_invalidations_paginator: ListInvalidationsPaginator = client.get_paginator("list_invalidations")
    list_key_value_stores_paginator: ListKeyValueStoresPaginator = client.get_paginator("list_key_value_stores")
    list_origin_access_controls_paginator: ListOriginAccessControlsPaginator = client.get_paginator("list_origin_access_controls")
    list_public_keys_paginator: ListPublicKeysPaginator = client.get_paginator("list_public_keys")
    list_streaming_distributions_paginator: ListStreamingDistributionsPaginator = client.get_paginator("list_streaming_distributions")
    list_trust_stores_paginator: ListTrustStoresPaginator = client.get_paginator("list_trust_stores")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListCloudFrontOriginAccessIdentitiesRequestPaginateTypeDef,
    ListCloudFrontOriginAccessIdentitiesResultTypeDef,
    ListConnectionFunctionsRequestPaginateTypeDef,
    ListConnectionFunctionsResultTypeDef,
    ListConnectionGroupsRequestPaginateTypeDef,
    ListConnectionGroupsResultTypeDef,
    ListDistributionsByConnectionFunctionRequestPaginateTypeDef,
    ListDistributionsByConnectionFunctionResultTypeDef,
    ListDistributionsByConnectionModeRequestPaginateTypeDef,
    ListDistributionsByConnectionModeResultTypeDef,
    ListDistributionsByTrustStoreRequestPaginateTypeDef,
    ListDistributionsByTrustStoreResultTypeDef,
    ListDistributionsRequestPaginateTypeDef,
    ListDistributionsResultTypeDef,
    ListDistributionTenantsByCustomizationRequestPaginateTypeDef,
    ListDistributionTenantsByCustomizationResultTypeDef,
    ListDistributionTenantsRequestPaginateTypeDef,
    ListDistributionTenantsResultTypeDef,
    ListDomainConflictsRequestPaginateTypeDef,
    ListDomainConflictsResultTypeDef,
    ListInvalidationsForDistributionTenantRequestPaginateTypeDef,
    ListInvalidationsForDistributionTenantResultTypeDef,
    ListInvalidationsRequestPaginateTypeDef,
    ListInvalidationsResultTypeDef,
    ListKeyValueStoresRequestPaginateTypeDef,
    ListKeyValueStoresResultTypeDef,
    ListOriginAccessControlsRequestPaginateTypeDef,
    ListOriginAccessControlsResultTypeDef,
    ListPublicKeysRequestPaginateTypeDef,
    ListPublicKeysResultTypeDef,
    ListStreamingDistributionsRequestPaginateTypeDef,
    ListStreamingDistributionsResultTypeDef,
    ListTrustStoresRequestPaginateTypeDef,
    ListTrustStoresResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListCloudFrontOriginAccessIdentitiesPaginator",
    "ListConnectionFunctionsPaginator",
    "ListConnectionGroupsPaginator",
    "ListDistributionTenantsByCustomizationPaginator",
    "ListDistributionTenantsPaginator",
    "ListDistributionsByConnectionFunctionPaginator",
    "ListDistributionsByConnectionModePaginator",
    "ListDistributionsByTrustStorePaginator",
    "ListDistributionsPaginator",
    "ListDomainConflictsPaginator",
    "ListInvalidationsForDistributionTenantPaginator",
    "ListInvalidationsPaginator",
    "ListKeyValueStoresPaginator",
    "ListOriginAccessControlsPaginator",
    "ListPublicKeysPaginator",
    "ListStreamingDistributionsPaginator",
    "ListTrustStoresPaginator",
)

if TYPE_CHECKING:
    _ListCloudFrontOriginAccessIdentitiesPaginatorBase = Paginator[
        ListCloudFrontOriginAccessIdentitiesResultTypeDef
    ]
else:
    _ListCloudFrontOriginAccessIdentitiesPaginatorBase = Paginator  # type: ignore[assignment]

class ListCloudFrontOriginAccessIdentitiesPaginator(
    _ListCloudFrontOriginAccessIdentitiesPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListCloudFrontOriginAccessIdentities.html#CloudFront.Paginator.ListCloudFrontOriginAccessIdentities)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listcloudfrontoriginaccessidentitiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCloudFrontOriginAccessIdentitiesRequestPaginateTypeDef]
    ) -> PageIterator[ListCloudFrontOriginAccessIdentitiesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListCloudFrontOriginAccessIdentities.html#CloudFront.Paginator.ListCloudFrontOriginAccessIdentities.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listcloudfrontoriginaccessidentitiespaginator)
        """

if TYPE_CHECKING:
    _ListConnectionFunctionsPaginatorBase = Paginator[ListConnectionFunctionsResultTypeDef]
else:
    _ListConnectionFunctionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConnectionFunctionsPaginator(_ListConnectionFunctionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListConnectionFunctions.html#CloudFront.Paginator.ListConnectionFunctions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listconnectionfunctionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConnectionFunctionsRequestPaginateTypeDef]
    ) -> PageIterator[ListConnectionFunctionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListConnectionFunctions.html#CloudFront.Paginator.ListConnectionFunctions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listconnectionfunctionspaginator)
        """

if TYPE_CHECKING:
    _ListConnectionGroupsPaginatorBase = Paginator[ListConnectionGroupsResultTypeDef]
else:
    _ListConnectionGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListConnectionGroupsPaginator(_ListConnectionGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListConnectionGroups.html#CloudFront.Paginator.ListConnectionGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listconnectiongroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConnectionGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListConnectionGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListConnectionGroups.html#CloudFront.Paginator.ListConnectionGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listconnectiongroupspaginator)
        """

if TYPE_CHECKING:
    _ListDistributionTenantsByCustomizationPaginatorBase = Paginator[
        ListDistributionTenantsByCustomizationResultTypeDef
    ]
else:
    _ListDistributionTenantsByCustomizationPaginatorBase = Paginator  # type: ignore[assignment]

class ListDistributionTenantsByCustomizationPaginator(
    _ListDistributionTenantsByCustomizationPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListDistributionTenantsByCustomization.html#CloudFront.Paginator.ListDistributionTenantsByCustomization)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listdistributiontenantsbycustomizationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDistributionTenantsByCustomizationRequestPaginateTypeDef]
    ) -> PageIterator[ListDistributionTenantsByCustomizationResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListDistributionTenantsByCustomization.html#CloudFront.Paginator.ListDistributionTenantsByCustomization.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listdistributiontenantsbycustomizationpaginator)
        """

if TYPE_CHECKING:
    _ListDistributionTenantsPaginatorBase = Paginator[ListDistributionTenantsResultTypeDef]
else:
    _ListDistributionTenantsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDistributionTenantsPaginator(_ListDistributionTenantsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListDistributionTenants.html#CloudFront.Paginator.ListDistributionTenants)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listdistributiontenantspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDistributionTenantsRequestPaginateTypeDef]
    ) -> PageIterator[ListDistributionTenantsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListDistributionTenants.html#CloudFront.Paginator.ListDistributionTenants.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listdistributiontenantspaginator)
        """

if TYPE_CHECKING:
    _ListDistributionsByConnectionFunctionPaginatorBase = Paginator[
        ListDistributionsByConnectionFunctionResultTypeDef
    ]
else:
    _ListDistributionsByConnectionFunctionPaginatorBase = Paginator  # type: ignore[assignment]

class ListDistributionsByConnectionFunctionPaginator(
    _ListDistributionsByConnectionFunctionPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListDistributionsByConnectionFunction.html#CloudFront.Paginator.ListDistributionsByConnectionFunction)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listdistributionsbyconnectionfunctionpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDistributionsByConnectionFunctionRequestPaginateTypeDef]
    ) -> PageIterator[ListDistributionsByConnectionFunctionResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListDistributionsByConnectionFunction.html#CloudFront.Paginator.ListDistributionsByConnectionFunction.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listdistributionsbyconnectionfunctionpaginator)
        """

if TYPE_CHECKING:
    _ListDistributionsByConnectionModePaginatorBase = Paginator[
        ListDistributionsByConnectionModeResultTypeDef
    ]
else:
    _ListDistributionsByConnectionModePaginatorBase = Paginator  # type: ignore[assignment]

class ListDistributionsByConnectionModePaginator(_ListDistributionsByConnectionModePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListDistributionsByConnectionMode.html#CloudFront.Paginator.ListDistributionsByConnectionMode)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listdistributionsbyconnectionmodepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDistributionsByConnectionModeRequestPaginateTypeDef]
    ) -> PageIterator[ListDistributionsByConnectionModeResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListDistributionsByConnectionMode.html#CloudFront.Paginator.ListDistributionsByConnectionMode.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listdistributionsbyconnectionmodepaginator)
        """

if TYPE_CHECKING:
    _ListDistributionsByTrustStorePaginatorBase = Paginator[
        ListDistributionsByTrustStoreResultTypeDef
    ]
else:
    _ListDistributionsByTrustStorePaginatorBase = Paginator  # type: ignore[assignment]

class ListDistributionsByTrustStorePaginator(_ListDistributionsByTrustStorePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListDistributionsByTrustStore.html#CloudFront.Paginator.ListDistributionsByTrustStore)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listdistributionsbytruststorepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDistributionsByTrustStoreRequestPaginateTypeDef]
    ) -> PageIterator[ListDistributionsByTrustStoreResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListDistributionsByTrustStore.html#CloudFront.Paginator.ListDistributionsByTrustStore.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listdistributionsbytruststorepaginator)
        """

if TYPE_CHECKING:
    _ListDistributionsPaginatorBase = Paginator[ListDistributionsResultTypeDef]
else:
    _ListDistributionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDistributionsPaginator(_ListDistributionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListDistributions.html#CloudFront.Paginator.ListDistributions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listdistributionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDistributionsRequestPaginateTypeDef]
    ) -> PageIterator[ListDistributionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListDistributions.html#CloudFront.Paginator.ListDistributions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listdistributionspaginator)
        """

if TYPE_CHECKING:
    _ListDomainConflictsPaginatorBase = Paginator[ListDomainConflictsResultTypeDef]
else:
    _ListDomainConflictsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDomainConflictsPaginator(_ListDomainConflictsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListDomainConflicts.html#CloudFront.Paginator.ListDomainConflicts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listdomainconflictspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDomainConflictsRequestPaginateTypeDef]
    ) -> PageIterator[ListDomainConflictsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListDomainConflicts.html#CloudFront.Paginator.ListDomainConflicts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listdomainconflictspaginator)
        """

if TYPE_CHECKING:
    _ListInvalidationsForDistributionTenantPaginatorBase = Paginator[
        ListInvalidationsForDistributionTenantResultTypeDef
    ]
else:
    _ListInvalidationsForDistributionTenantPaginatorBase = Paginator  # type: ignore[assignment]

class ListInvalidationsForDistributionTenantPaginator(
    _ListInvalidationsForDistributionTenantPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListInvalidationsForDistributionTenant.html#CloudFront.Paginator.ListInvalidationsForDistributionTenant)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listinvalidationsfordistributiontenantpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInvalidationsForDistributionTenantRequestPaginateTypeDef]
    ) -> PageIterator[ListInvalidationsForDistributionTenantResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListInvalidationsForDistributionTenant.html#CloudFront.Paginator.ListInvalidationsForDistributionTenant.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listinvalidationsfordistributiontenantpaginator)
        """

if TYPE_CHECKING:
    _ListInvalidationsPaginatorBase = Paginator[ListInvalidationsResultTypeDef]
else:
    _ListInvalidationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListInvalidationsPaginator(_ListInvalidationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListInvalidations.html#CloudFront.Paginator.ListInvalidations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listinvalidationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInvalidationsRequestPaginateTypeDef]
    ) -> PageIterator[ListInvalidationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListInvalidations.html#CloudFront.Paginator.ListInvalidations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listinvalidationspaginator)
        """

if TYPE_CHECKING:
    _ListKeyValueStoresPaginatorBase = Paginator[ListKeyValueStoresResultTypeDef]
else:
    _ListKeyValueStoresPaginatorBase = Paginator  # type: ignore[assignment]

class ListKeyValueStoresPaginator(_ListKeyValueStoresPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListKeyValueStores.html#CloudFront.Paginator.ListKeyValueStores)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listkeyvaluestorespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListKeyValueStoresRequestPaginateTypeDef]
    ) -> PageIterator[ListKeyValueStoresResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListKeyValueStores.html#CloudFront.Paginator.ListKeyValueStores.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listkeyvaluestorespaginator)
        """

if TYPE_CHECKING:
    _ListOriginAccessControlsPaginatorBase = Paginator[ListOriginAccessControlsResultTypeDef]
else:
    _ListOriginAccessControlsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOriginAccessControlsPaginator(_ListOriginAccessControlsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListOriginAccessControls.html#CloudFront.Paginator.ListOriginAccessControls)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listoriginaccesscontrolspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOriginAccessControlsRequestPaginateTypeDef]
    ) -> PageIterator[ListOriginAccessControlsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListOriginAccessControls.html#CloudFront.Paginator.ListOriginAccessControls.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listoriginaccesscontrolspaginator)
        """

if TYPE_CHECKING:
    _ListPublicKeysPaginatorBase = Paginator[ListPublicKeysResultTypeDef]
else:
    _ListPublicKeysPaginatorBase = Paginator  # type: ignore[assignment]

class ListPublicKeysPaginator(_ListPublicKeysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListPublicKeys.html#CloudFront.Paginator.ListPublicKeys)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listpublickeyspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPublicKeysRequestPaginateTypeDef]
    ) -> PageIterator[ListPublicKeysResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListPublicKeys.html#CloudFront.Paginator.ListPublicKeys.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listpublickeyspaginator)
        """

if TYPE_CHECKING:
    _ListStreamingDistributionsPaginatorBase = Paginator[ListStreamingDistributionsResultTypeDef]
else:
    _ListStreamingDistributionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListStreamingDistributionsPaginator(_ListStreamingDistributionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListStreamingDistributions.html#CloudFront.Paginator.ListStreamingDistributions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#liststreamingdistributionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStreamingDistributionsRequestPaginateTypeDef]
    ) -> PageIterator[ListStreamingDistributionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListStreamingDistributions.html#CloudFront.Paginator.ListStreamingDistributions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#liststreamingdistributionspaginator)
        """

if TYPE_CHECKING:
    _ListTrustStoresPaginatorBase = Paginator[ListTrustStoresResultTypeDef]
else:
    _ListTrustStoresPaginatorBase = Paginator  # type: ignore[assignment]

class ListTrustStoresPaginator(_ListTrustStoresPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListTrustStores.html#CloudFront.Paginator.ListTrustStores)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listtruststorespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTrustStoresRequestPaginateTypeDef]
    ) -> PageIterator[ListTrustStoresResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront/paginator/ListTrustStores.html#CloudFront.Paginator.ListTrustStores.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/paginators/#listtruststorespaginator)
        """
