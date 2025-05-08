"""
Type annotations for servicecatalog-appregistry service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_servicecatalog_appregistry.client import AppRegistryClient
    from mypy_boto3_servicecatalog_appregistry.paginator import (
        ListApplicationsPaginator,
        ListAssociatedAttributeGroupsPaginator,
        ListAssociatedResourcesPaginator,
        ListAttributeGroupsForApplicationPaginator,
        ListAttributeGroupsPaginator,
    )

    session = Session()
    client: AppRegistryClient = session.client("servicecatalog-appregistry")

    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_associated_attribute_groups_paginator: ListAssociatedAttributeGroupsPaginator = client.get_paginator("list_associated_attribute_groups")
    list_associated_resources_paginator: ListAssociatedResourcesPaginator = client.get_paginator("list_associated_resources")
    list_attribute_groups_for_application_paginator: ListAttributeGroupsForApplicationPaginator = client.get_paginator("list_attribute_groups_for_application")
    list_attribute_groups_paginator: ListAttributeGroupsPaginator = client.get_paginator("list_attribute_groups")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListApplicationsRequestPaginateTypeDef,
    ListApplicationsResponseTypeDef,
    ListAssociatedAttributeGroupsRequestPaginateTypeDef,
    ListAssociatedAttributeGroupsResponseTypeDef,
    ListAssociatedResourcesRequestPaginateTypeDef,
    ListAssociatedResourcesResponseTypeDef,
    ListAttributeGroupsForApplicationRequestPaginateTypeDef,
    ListAttributeGroupsForApplicationResponseTypeDef,
    ListAttributeGroupsRequestPaginateTypeDef,
    ListAttributeGroupsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListApplicationsPaginator",
    "ListAssociatedAttributeGroupsPaginator",
    "ListAssociatedResourcesPaginator",
    "ListAttributeGroupsForApplicationPaginator",
    "ListAttributeGroupsPaginator",
)

if TYPE_CHECKING:
    _ListApplicationsPaginatorBase = Paginator[ListApplicationsResponseTypeDef]
else:
    _ListApplicationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListApplicationsPaginator(_ListApplicationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/paginator/ListApplications.html#AppRegistry.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/paginators/#listapplicationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApplicationsRequestPaginateTypeDef]
    ) -> PageIterator[ListApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/paginator/ListApplications.html#AppRegistry.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/paginators/#listapplicationspaginator)
        """

if TYPE_CHECKING:
    _ListAssociatedAttributeGroupsPaginatorBase = Paginator[
        ListAssociatedAttributeGroupsResponseTypeDef
    ]
else:
    _ListAssociatedAttributeGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssociatedAttributeGroupsPaginator(_ListAssociatedAttributeGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/paginator/ListAssociatedAttributeGroups.html#AppRegistry.Paginator.ListAssociatedAttributeGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/paginators/#listassociatedattributegroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssociatedAttributeGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListAssociatedAttributeGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/paginator/ListAssociatedAttributeGroups.html#AppRegistry.Paginator.ListAssociatedAttributeGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/paginators/#listassociatedattributegroupspaginator)
        """

if TYPE_CHECKING:
    _ListAssociatedResourcesPaginatorBase = Paginator[ListAssociatedResourcesResponseTypeDef]
else:
    _ListAssociatedResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssociatedResourcesPaginator(_ListAssociatedResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/paginator/ListAssociatedResources.html#AppRegistry.Paginator.ListAssociatedResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/paginators/#listassociatedresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssociatedResourcesRequestPaginateTypeDef]
    ) -> PageIterator[ListAssociatedResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/paginator/ListAssociatedResources.html#AppRegistry.Paginator.ListAssociatedResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/paginators/#listassociatedresourcespaginator)
        """

if TYPE_CHECKING:
    _ListAttributeGroupsForApplicationPaginatorBase = Paginator[
        ListAttributeGroupsForApplicationResponseTypeDef
    ]
else:
    _ListAttributeGroupsForApplicationPaginatorBase = Paginator  # type: ignore[assignment]

class ListAttributeGroupsForApplicationPaginator(_ListAttributeGroupsForApplicationPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/paginator/ListAttributeGroupsForApplication.html#AppRegistry.Paginator.ListAttributeGroupsForApplication)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/paginators/#listattributegroupsforapplicationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAttributeGroupsForApplicationRequestPaginateTypeDef]
    ) -> PageIterator[ListAttributeGroupsForApplicationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/paginator/ListAttributeGroupsForApplication.html#AppRegistry.Paginator.ListAttributeGroupsForApplication.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/paginators/#listattributegroupsforapplicationpaginator)
        """

if TYPE_CHECKING:
    _ListAttributeGroupsPaginatorBase = Paginator[ListAttributeGroupsResponseTypeDef]
else:
    _ListAttributeGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAttributeGroupsPaginator(_ListAttributeGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/paginator/ListAttributeGroups.html#AppRegistry.Paginator.ListAttributeGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/paginators/#listattributegroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAttributeGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListAttributeGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry/paginator/ListAttributeGroups.html#AppRegistry.Paginator.ListAttributeGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/paginators/#listattributegroupspaginator)
        """
