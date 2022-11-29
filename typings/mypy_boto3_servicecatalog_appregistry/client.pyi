"""
Type annotations for servicecatalog-appregistry service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_servicecatalog_appregistry import AppRegistryClient

    client: AppRegistryClient = boto3.client("servicecatalog-appregistry")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import ResourceTypeType
from .paginator import (
    ListApplicationsPaginator,
    ListAssociatedAttributeGroupsPaginator,
    ListAssociatedResourcesPaginator,
    ListAttributeGroupsForApplicationPaginator,
    ListAttributeGroupsPaginator,
)
from .type_defs import (
    AppRegistryConfigurationTypeDef,
    AssociateAttributeGroupResponseTypeDef,
    AssociateResourceResponseTypeDef,
    CreateApplicationResponseTypeDef,
    CreateAttributeGroupResponseTypeDef,
    DeleteApplicationResponseTypeDef,
    DeleteAttributeGroupResponseTypeDef,
    DisassociateAttributeGroupResponseTypeDef,
    DisassociateResourceResponseTypeDef,
    GetApplicationResponseTypeDef,
    GetAssociatedResourceResponseTypeDef,
    GetAttributeGroupResponseTypeDef,
    GetConfigurationResponseTypeDef,
    ListApplicationsResponseTypeDef,
    ListAssociatedAttributeGroupsResponseTypeDef,
    ListAssociatedResourcesResponseTypeDef,
    ListAttributeGroupsForApplicationResponseTypeDef,
    ListAttributeGroupsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    SyncResourceResponseTypeDef,
    UpdateApplicationResponseTypeDef,
    UpdateAttributeGroupResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("AppRegistryClient",)

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

class AppRegistryClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AppRegistryClient exceptions.
        """
    def associate_attribute_group(
        self, *, application: str, attributeGroup: str
    ) -> AssociateAttributeGroupResponseTypeDef:
        """
        Associates an attribute group with an application to augment the application's
        metadata with the group's attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.associate_attribute_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#associate_attribute_group)
        """
    def associate_resource(
        self, *, application: str, resourceType: ResourceTypeType, resource: str
    ) -> AssociateResourceResponseTypeDef:
        """
        Associates a resource with an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.associate_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#associate_resource)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#close)
        """
    def create_application(
        self, *, name: str, clientToken: str, description: str = None, tags: Dict[str, str] = None
    ) -> CreateApplicationResponseTypeDef:
        """
        Creates a new application that is the top-level node in a hierarchy of related
        cloud resource abstractions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.create_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#create_application)
        """
    def create_attribute_group(
        self,
        *,
        name: str,
        attributes: str,
        clientToken: str,
        description: str = None,
        tags: Dict[str, str] = None
    ) -> CreateAttributeGroupResponseTypeDef:
        """
        Creates a new attribute group as a container for user-defined attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.create_attribute_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#create_attribute_group)
        """
    def delete_application(self, *, application: str) -> DeleteApplicationResponseTypeDef:
        """
        Deletes an application that is specified either by its application ID or name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.delete_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#delete_application)
        """
    def delete_attribute_group(self, *, attributeGroup: str) -> DeleteAttributeGroupResponseTypeDef:
        """
        Deletes an attribute group, specified either by its attribute group ID or name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.delete_attribute_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#delete_attribute_group)
        """
    def disassociate_attribute_group(
        self, *, application: str, attributeGroup: str
    ) -> DisassociateAttributeGroupResponseTypeDef:
        """
        Disassociates an attribute group from an application to remove the extra
        attributes contained in the attribute group from the application's metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.disassociate_attribute_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#disassociate_attribute_group)
        """
    def disassociate_resource(
        self, *, application: str, resourceType: ResourceTypeType, resource: str
    ) -> DisassociateResourceResponseTypeDef:
        """
        Disassociates a resource from application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.disassociate_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#disassociate_resource)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#generate_presigned_url)
        """
    def get_application(self, *, application: str) -> GetApplicationResponseTypeDef:
        """
        Retrieves metadata information about one of your applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.get_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#get_application)
        """
    def get_associated_resource(
        self, *, application: str, resourceType: ResourceTypeType, resource: str
    ) -> GetAssociatedResourceResponseTypeDef:
        """
        Gets the resource associated with the application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.get_associated_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#get_associated_resource)
        """
    def get_attribute_group(self, *, attributeGroup: str) -> GetAttributeGroupResponseTypeDef:
        """
        Retrieves an attribute group, either by its name or its ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.get_attribute_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#get_attribute_group)
        """
    def get_configuration(self) -> GetConfigurationResponseTypeDef:
        """
        Retrieves a `TagKey` configuration from an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.get_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#get_configuration)
        """
    def list_applications(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListApplicationsResponseTypeDef:
        """
        Retrieves a list of all of your applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.list_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#list_applications)
        """
    def list_associated_attribute_groups(
        self, *, application: str, nextToken: str = None, maxResults: int = None
    ) -> ListAssociatedAttributeGroupsResponseTypeDef:
        """
        Lists all attribute groups that are associated with specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.list_associated_attribute_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#list_associated_attribute_groups)
        """
    def list_associated_resources(
        self, *, application: str, nextToken: str = None, maxResults: int = None
    ) -> ListAssociatedResourcesResponseTypeDef:
        """
        Lists all of the resources that are associated with the specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.list_associated_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#list_associated_resources)
        """
    def list_attribute_groups(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListAttributeGroupsResponseTypeDef:
        """
        Lists all attribute groups which you have access to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.list_attribute_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#list_attribute_groups)
        """
    def list_attribute_groups_for_application(
        self, *, application: str, nextToken: str = None, maxResults: int = None
    ) -> ListAttributeGroupsForApplicationResponseTypeDef:
        """
        Lists the details of all attribute groups associated with a specific
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.list_attribute_groups_for_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#list_attribute_groups_for_application)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all of the tags on the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#list_tags_for_resource)
        """
    def put_configuration(self, *, configuration: "AppRegistryConfigurationTypeDef") -> None:
        """
        Associates a `TagKey` configuration to an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.put_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#put_configuration)
        """
    def sync_resource(
        self, *, resourceType: ResourceTypeType, resource: str
    ) -> SyncResourceResponseTypeDef:
        """
        Syncs the resource with current AppRegistry records.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.sync_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#sync_resource)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#untag_resource)
        """
    def update_application(
        self, *, application: str, name: str = None, description: str = None
    ) -> UpdateApplicationResponseTypeDef:
        """
        Updates an existing application with new attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.update_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#update_application)
        """
    def update_attribute_group(
        self,
        *,
        attributeGroup: str,
        name: str = None,
        description: str = None,
        attributes: str = None
    ) -> UpdateAttributeGroupResponseTypeDef:
        """
        Updates an existing attribute group with new details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.update_attribute_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#update_attribute_group)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListApplications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/paginators.html#listapplicationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_associated_attribute_groups"]
    ) -> ListAssociatedAttributeGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListAssociatedAttributeGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/paginators.html#listassociatedattributegroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_associated_resources"]
    ) -> ListAssociatedResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListAssociatedResources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/paginators.html#listassociatedresourcespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_attribute_groups"]
    ) -> ListAttributeGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListAttributeGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/paginators.html#listattributegroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_attribute_groups_for_application"]
    ) -> ListAttributeGroupsForApplicationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListAttributeGroupsForApplication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/paginators.html#listattributegroupsforapplicationpaginator)
        """
