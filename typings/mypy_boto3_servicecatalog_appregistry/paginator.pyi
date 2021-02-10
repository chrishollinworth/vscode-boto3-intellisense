"""
Main interface for servicecatalog-appregistry service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_servicecatalog_appregistry import AppRegistryClient
    from mypy_boto3_servicecatalog_appregistry.paginator import (
        ListApplicationsPaginator,
        ListAssociatedAttributeGroupsPaginator,
        ListAssociatedResourcesPaginator,
        ListAttributeGroupsPaginator,
    )

    client: AppRegistryClient = boto3.client("servicecatalog-appregistry")

    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_associated_attribute_groups_paginator: ListAssociatedAttributeGroupsPaginator = client.get_paginator("list_associated_attribute_groups")
    list_associated_resources_paginator: ListAssociatedResourcesPaginator = client.get_paginator("list_associated_resources")
    list_attribute_groups_paginator: ListAttributeGroupsPaginator = client.get_paginator("list_attribute_groups")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_servicecatalog_appregistry.type_defs import (
    ListApplicationsResponseTypeDef,
    ListAssociatedAttributeGroupsResponseTypeDef,
    ListAssociatedResourcesResponseTypeDef,
    ListAttributeGroupsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListApplicationsPaginator",
    "ListAssociatedAttributeGroupsPaginator",
    "ListAssociatedResourcesPaginator",
    "ListAttributeGroupsPaginator",
)


class ListApplicationsPaginator(Boto3Paginator):
    """
    [Paginator.ListApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListApplications)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationsResponseTypeDef]:
        """
        [ListApplications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListApplications.paginate)
        """


class ListAssociatedAttributeGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListAssociatedAttributeGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListAssociatedAttributeGroups)
    """

    def paginate(
        self, application: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssociatedAttributeGroupsResponseTypeDef]:
        """
        [ListAssociatedAttributeGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListAssociatedAttributeGroups.paginate)
        """


class ListAssociatedResourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListAssociatedResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListAssociatedResources)
    """

    def paginate(
        self, application: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssociatedResourcesResponseTypeDef]:
        """
        [ListAssociatedResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListAssociatedResources.paginate)
        """


class ListAttributeGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListAttributeGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListAttributeGroups)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAttributeGroupsResponseTypeDef]:
        """
        [ListAttributeGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListAttributeGroups.paginate)
        """
