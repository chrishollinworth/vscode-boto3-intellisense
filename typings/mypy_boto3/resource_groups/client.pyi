"""
Type annotations for resource-groups service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_resource_groups import ResourceGroupsClient

    client: ResourceGroupsClient = boto3.client("resource-groups")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import GroupLifecycleEventsDesiredStatusType
from .paginator import ListGroupResourcesPaginator, ListGroupsPaginator, SearchResourcesPaginator
from .type_defs import (
    CreateGroupOutputTypeDef,
    DeleteGroupOutputTypeDef,
    GetAccountSettingsOutputTypeDef,
    GetGroupConfigurationOutputTypeDef,
    GetGroupOutputTypeDef,
    GetGroupQueryOutputTypeDef,
    GetTagsOutputTypeDef,
    GroupConfigurationItemTypeDef,
    GroupFilterTypeDef,
    GroupResourcesOutputTypeDef,
    ListGroupResourcesOutputTypeDef,
    ListGroupsOutputTypeDef,
    ResourceFilterTypeDef,
    ResourceQueryTypeDef,
    SearchResourcesOutputTypeDef,
    TagOutputTypeDef,
    UngroupResourcesOutputTypeDef,
    UntagOutputTypeDef,
    UpdateAccountSettingsOutputTypeDef,
    UpdateGroupOutputTypeDef,
    UpdateGroupQueryOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ResourceGroupsClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    MethodNotAllowedException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]

class ResourceGroupsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ResourceGroupsClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#close)
        """
    def create_group(
        self,
        *,
        Name: str,
        Description: str = None,
        ResourceQuery: "ResourceQueryTypeDef" = None,
        Tags: Dict[str, str] = None,
        Configuration: List["GroupConfigurationItemTypeDef"] = None
    ) -> CreateGroupOutputTypeDef:
        """
        Creates a resource group with the specified name and description.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Client.create_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#create_group)
        """
    def delete_group(self, *, GroupName: str = None, Group: str = None) -> DeleteGroupOutputTypeDef:
        """
        Deletes the specified resource group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Client.delete_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#delete_group)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#generate_presigned_url)
        """
    def get_account_settings(self) -> GetAccountSettingsOutputTypeDef:
        """
        Retrieves the current status of optional features in Resource Groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Client.get_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#get_account_settings)
        """
    def get_group(self, *, GroupName: str = None, Group: str = None) -> GetGroupOutputTypeDef:
        """
        Returns information about a specified resource group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Client.get_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#get_group)
        """
    def get_group_configuration(self, *, Group: str = None) -> GetGroupConfigurationOutputTypeDef:
        """
        Retrieves the service configuration associated with the specified resource
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Client.get_group_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#get_group_configuration)
        """
    def get_group_query(
        self, *, GroupName: str = None, Group: str = None
    ) -> GetGroupQueryOutputTypeDef:
        """
        Retrieves the resource query associated with the specified resource group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Client.get_group_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#get_group_query)
        """
    def get_tags(self, *, Arn: str) -> GetTagsOutputTypeDef:
        """
        Returns a list of tags that are associated with a resource group, specified by
        an ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Client.get_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#get_tags)
        """
    def group_resources(
        self, *, Group: str, ResourceArns: List[str]
    ) -> GroupResourcesOutputTypeDef:
        """
        Adds the specified resources to the specified group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Client.group_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#group_resources)
        """
    def list_group_resources(
        self,
        *,
        GroupName: str = None,
        Group: str = None,
        Filters: List["ResourceFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListGroupResourcesOutputTypeDef:
        """
        Returns a list of ARNs of the resources that are members of a specified resource
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Client.list_group_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#list_group_resources)
        """
    def list_groups(
        self,
        *,
        Filters: List["GroupFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListGroupsOutputTypeDef:
        """
        Returns a list of existing Resource Groups in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Client.list_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#list_groups)
        """
    def put_group_configuration(
        self, *, Group: str = None, Configuration: List["GroupConfigurationItemTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Attaches a service configuration to the specified group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Client.put_group_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#put_group_configuration)
        """
    def search_resources(
        self,
        *,
        ResourceQuery: "ResourceQueryTypeDef",
        MaxResults: int = None,
        NextToken: str = None
    ) -> SearchResourcesOutputTypeDef:
        """
        Returns a list of Amazon Web Services resource identifiers that matches the
        specified query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Client.search_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#search_resources)
        """
    def tag(self, *, Arn: str, Tags: Dict[str, str]) -> TagOutputTypeDef:
        """
        Adds tags to a resource group with the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Client.tag)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#tag)
        """
    def ungroup_resources(
        self, *, Group: str, ResourceArns: List[str]
    ) -> UngroupResourcesOutputTypeDef:
        """
        Removes the specified resources from the specified group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Client.ungroup_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#ungroup_resources)
        """
    def untag(self, *, Arn: str, Keys: List[str]) -> UntagOutputTypeDef:
        """
        Deletes tags from a specified resource group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Client.untag)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#untag)
        """
    def update_account_settings(
        self, *, GroupLifecycleEventsDesiredStatus: GroupLifecycleEventsDesiredStatusType = None
    ) -> UpdateAccountSettingsOutputTypeDef:
        """
        Turns on or turns off optional features in Resource Groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Client.update_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#update_account_settings)
        """
    def update_group(
        self, *, GroupName: str = None, Group: str = None, Description: str = None
    ) -> UpdateGroupOutputTypeDef:
        """
        Updates the description for an existing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Client.update_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#update_group)
        """
    def update_group_query(
        self, *, ResourceQuery: "ResourceQueryTypeDef", GroupName: str = None, Group: str = None
    ) -> UpdateGroupQueryOutputTypeDef:
        """
        Updates the resource query of a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Client.update_group_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#update_group_query)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_group_resources"]
    ) -> ListGroupResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Paginator.ListGroupResources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/paginators.html#listgroupresourcespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_groups"]) -> ListGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Paginator.ListGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/paginators.html#listgroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["search_resources"]
    ) -> SearchResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/resource-groups.html#ResourceGroups.Paginator.SearchResources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/paginators.html#searchresourcespaginator)
        """
