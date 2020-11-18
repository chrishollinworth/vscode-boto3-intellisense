# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for servicecatalog-appregistry service client

Usage::

    ```python
    import boto3
    from mypy_boto3_servicecatalog_appregistry import ServiceCatalogAppRegistryClient

    client: ServiceCatalogAppRegistryClient = boto3.client("servicecatalog-appregistry")
    ```
"""
import sys
from typing import Any, Dict, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_servicecatalog_appregistry.paginator import (
    ListApplicationsPaginator,
    ListAssociatedAttributeGroupsPaginator,
    ListAssociatedResourcesPaginator,
    ListAttributeGroupsPaginator,
)
from mypy_boto3_servicecatalog_appregistry.type_defs import (
    AssociateAttributeGroupResponseTypeDef,
    AssociateResourceResponseTypeDef,
    CreateApplicationResponseTypeDef,
    CreateAttributeGroupResponseTypeDef,
    DeleteApplicationResponseTypeDef,
    DeleteAttributeGroupResponseTypeDef,
    DisassociateAttributeGroupResponseTypeDef,
    DisassociateResourceResponseTypeDef,
    GetApplicationResponseTypeDef,
    GetAttributeGroupResponseTypeDef,
    ListApplicationsResponseTypeDef,
    ListAssociatedAttributeGroupsResponseTypeDef,
    ListAssociatedResourcesResponseTypeDef,
    ListAttributeGroupsResponseTypeDef,
    UpdateApplicationResponseTypeDef,
    UpdateAttributeGroupResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ServiceCatalogAppRegistryClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class ServiceCatalogAppRegistryClient:
    """
    [ServiceCatalogAppRegistry.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicecatalog-appregistry.html#ServiceCatalogAppRegistry.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_attribute_group(
        self, application: str, attributeGroup: str
    ) -> AssociateAttributeGroupResponseTypeDef:
        """
        [Client.associate_attribute_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicecatalog-appregistry.html#ServiceCatalogAppRegistry.Client.associate_attribute_group)
        """

    def associate_resource(
        self, application: str, resourceType: Literal["CFN_STACK"], resource: str
    ) -> AssociateResourceResponseTypeDef:
        """
        [Client.associate_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicecatalog-appregistry.html#ServiceCatalogAppRegistry.Client.associate_resource)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicecatalog-appregistry.html#ServiceCatalogAppRegistry.Client.can_paginate)
        """

    def create_application(
        self, name: str, clientToken: str, description: str = None, tags: Dict[str, str] = None
    ) -> CreateApplicationResponseTypeDef:
        """
        [Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicecatalog-appregistry.html#ServiceCatalogAppRegistry.Client.create_application)
        """

    def create_attribute_group(
        self,
        name: str,
        attributes: str,
        clientToken: str,
        description: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateAttributeGroupResponseTypeDef:
        """
        [Client.create_attribute_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicecatalog-appregistry.html#ServiceCatalogAppRegistry.Client.create_attribute_group)
        """

    def delete_application(self, application: str) -> DeleteApplicationResponseTypeDef:
        """
        [Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicecatalog-appregistry.html#ServiceCatalogAppRegistry.Client.delete_application)
        """

    def delete_attribute_group(self, attributeGroup: str) -> DeleteAttributeGroupResponseTypeDef:
        """
        [Client.delete_attribute_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicecatalog-appregistry.html#ServiceCatalogAppRegistry.Client.delete_attribute_group)
        """

    def disassociate_attribute_group(
        self, application: str, attributeGroup: str
    ) -> DisassociateAttributeGroupResponseTypeDef:
        """
        [Client.disassociate_attribute_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicecatalog-appregistry.html#ServiceCatalogAppRegistry.Client.disassociate_attribute_group)
        """

    def disassociate_resource(
        self, application: str, resourceType: Literal["CFN_STACK"], resource: str
    ) -> DisassociateResourceResponseTypeDef:
        """
        [Client.disassociate_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicecatalog-appregistry.html#ServiceCatalogAppRegistry.Client.disassociate_resource)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicecatalog-appregistry.html#ServiceCatalogAppRegistry.Client.generate_presigned_url)
        """

    def get_application(self, application: str) -> GetApplicationResponseTypeDef:
        """
        [Client.get_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicecatalog-appregistry.html#ServiceCatalogAppRegistry.Client.get_application)
        """

    def get_attribute_group(self, attributeGroup: str) -> GetAttributeGroupResponseTypeDef:
        """
        [Client.get_attribute_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicecatalog-appregistry.html#ServiceCatalogAppRegistry.Client.get_attribute_group)
        """

    def list_applications(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListApplicationsResponseTypeDef:
        """
        [Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicecatalog-appregistry.html#ServiceCatalogAppRegistry.Client.list_applications)
        """

    def list_associated_attribute_groups(
        self, application: str, nextToken: str = None, maxResults: int = None
    ) -> ListAssociatedAttributeGroupsResponseTypeDef:
        """
        [Client.list_associated_attribute_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicecatalog-appregistry.html#ServiceCatalogAppRegistry.Client.list_associated_attribute_groups)
        """

    def list_associated_resources(
        self, application: str, nextToken: str = None, maxResults: int = None
    ) -> ListAssociatedResourcesResponseTypeDef:
        """
        [Client.list_associated_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicecatalog-appregistry.html#ServiceCatalogAppRegistry.Client.list_associated_resources)
        """

    def list_attribute_groups(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListAttributeGroupsResponseTypeDef:
        """
        [Client.list_attribute_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicecatalog-appregistry.html#ServiceCatalogAppRegistry.Client.list_attribute_groups)
        """

    def update_application(
        self, application: str, name: str = None, description: str = None
    ) -> UpdateApplicationResponseTypeDef:
        """
        [Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicecatalog-appregistry.html#ServiceCatalogAppRegistry.Client.update_application)
        """

    def update_attribute_group(
        self, attributeGroup: str, name: str = None, description: str = None, attributes: str = None
    ) -> UpdateAttributeGroupResponseTypeDef:
        """
        [Client.update_attribute_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicecatalog-appregistry.html#ServiceCatalogAppRegistry.Client.update_attribute_group)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Paginator.ListApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicecatalog-appregistry.html#ServiceCatalogAppRegistry.Paginator.ListApplications)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_associated_attribute_groups"]
    ) -> ListAssociatedAttributeGroupsPaginator:
        """
        [Paginator.ListAssociatedAttributeGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicecatalog-appregistry.html#ServiceCatalogAppRegistry.Paginator.ListAssociatedAttributeGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_associated_resources"]
    ) -> ListAssociatedResourcesPaginator:
        """
        [Paginator.ListAssociatedResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicecatalog-appregistry.html#ServiceCatalogAppRegistry.Paginator.ListAssociatedResources)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_attribute_groups"]
    ) -> ListAttributeGroupsPaginator:
        """
        [Paginator.ListAttributeGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/servicecatalog-appregistry.html#ServiceCatalogAppRegistry.Paginator.ListAttributeGroups)
        """
