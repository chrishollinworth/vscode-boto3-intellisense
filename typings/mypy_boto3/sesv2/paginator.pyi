"""
Type annotations for sesv2 service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sesv2/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_sesv2.client import SESV2Client
    from mypy_boto3_sesv2.paginator import (
        ListMultiRegionEndpointsPaginator,
        ListReputationEntitiesPaginator,
        ListResourceTenantsPaginator,
        ListTenantResourcesPaginator,
        ListTenantsPaginator,
    )

    session = Session()
    client: SESV2Client = session.client("sesv2")

    list_multi_region_endpoints_paginator: ListMultiRegionEndpointsPaginator = client.get_paginator("list_multi_region_endpoints")
    list_reputation_entities_paginator: ListReputationEntitiesPaginator = client.get_paginator("list_reputation_entities")
    list_resource_tenants_paginator: ListResourceTenantsPaginator = client.get_paginator("list_resource_tenants")
    list_tenant_resources_paginator: ListTenantResourcesPaginator = client.get_paginator("list_tenant_resources")
    list_tenants_paginator: ListTenantsPaginator = client.get_paginator("list_tenants")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListMultiRegionEndpointsRequestPaginateTypeDef,
    ListMultiRegionEndpointsResponseTypeDef,
    ListReputationEntitiesRequestPaginateTypeDef,
    ListReputationEntitiesResponseTypeDef,
    ListResourceTenantsRequestPaginateTypeDef,
    ListResourceTenantsResponseTypeDef,
    ListTenantResourcesRequestPaginateTypeDef,
    ListTenantResourcesResponseTypeDef,
    ListTenantsRequestPaginateTypeDef,
    ListTenantsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListMultiRegionEndpointsPaginator",
    "ListReputationEntitiesPaginator",
    "ListResourceTenantsPaginator",
    "ListTenantResourcesPaginator",
    "ListTenantsPaginator",
)

if TYPE_CHECKING:
    _ListMultiRegionEndpointsPaginatorBase = Paginator[ListMultiRegionEndpointsResponseTypeDef]
else:
    _ListMultiRegionEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMultiRegionEndpointsPaginator(_ListMultiRegionEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2/paginator/ListMultiRegionEndpoints.html#SESV2.Paginator.ListMultiRegionEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sesv2/paginators/#listmultiregionendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMultiRegionEndpointsRequestPaginateTypeDef]
    ) -> PageIterator[ListMultiRegionEndpointsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2/paginator/ListMultiRegionEndpoints.html#SESV2.Paginator.ListMultiRegionEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sesv2/paginators/#listmultiregionendpointspaginator)
        """

if TYPE_CHECKING:
    _ListReputationEntitiesPaginatorBase = Paginator[ListReputationEntitiesResponseTypeDef]
else:
    _ListReputationEntitiesPaginatorBase = Paginator  # type: ignore[assignment]

class ListReputationEntitiesPaginator(_ListReputationEntitiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2/paginator/ListReputationEntities.html#SESV2.Paginator.ListReputationEntities)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sesv2/paginators/#listreputationentitiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListReputationEntitiesRequestPaginateTypeDef]
    ) -> PageIterator[ListReputationEntitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2/paginator/ListReputationEntities.html#SESV2.Paginator.ListReputationEntities.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sesv2/paginators/#listreputationentitiespaginator)
        """

if TYPE_CHECKING:
    _ListResourceTenantsPaginatorBase = Paginator[ListResourceTenantsResponseTypeDef]
else:
    _ListResourceTenantsPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourceTenantsPaginator(_ListResourceTenantsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2/paginator/ListResourceTenants.html#SESV2.Paginator.ListResourceTenants)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sesv2/paginators/#listresourcetenantspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourceTenantsRequestPaginateTypeDef]
    ) -> PageIterator[ListResourceTenantsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2/paginator/ListResourceTenants.html#SESV2.Paginator.ListResourceTenants.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sesv2/paginators/#listresourcetenantspaginator)
        """

if TYPE_CHECKING:
    _ListTenantResourcesPaginatorBase = Paginator[ListTenantResourcesResponseTypeDef]
else:
    _ListTenantResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTenantResourcesPaginator(_ListTenantResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2/paginator/ListTenantResources.html#SESV2.Paginator.ListTenantResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sesv2/paginators/#listtenantresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTenantResourcesRequestPaginateTypeDef]
    ) -> PageIterator[ListTenantResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2/paginator/ListTenantResources.html#SESV2.Paginator.ListTenantResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sesv2/paginators/#listtenantresourcespaginator)
        """

if TYPE_CHECKING:
    _ListTenantsPaginatorBase = Paginator[ListTenantsResponseTypeDef]
else:
    _ListTenantsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTenantsPaginator(_ListTenantsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2/paginator/ListTenants.html#SESV2.Paginator.ListTenants)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sesv2/paginators/#listtenantspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTenantsRequestPaginateTypeDef]
    ) -> PageIterator[ListTenantsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2/paginator/ListTenants.html#SESV2.Paginator.ListTenants.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sesv2/paginators/#listtenantspaginator)
        """
