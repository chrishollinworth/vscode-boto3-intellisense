# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for resource-groups service client

Usage::

    ```python
    import boto3
    from mypy_boto3_resource_groups import ResourceGroupsClient

    client: ResourceGroupsClient = boto3.client("resource-groups")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_resource_groups.paginator import (
    ListGroupResourcesPaginator,
    ListGroupsPaginator,
    SearchResourcesPaginator,
)
from mypy_boto3_resource_groups.type_defs import (
    CreateGroupOutputTypeDef,
    DeleteGroupOutputTypeDef,
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


class ResourceGroupsClient:
    """
    [ResourceGroups.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resource-groups.html#ResourceGroups.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resource-groups.html#ResourceGroups.Client.can_paginate)
        """

    def create_group(
        self,
        Name: str,
        Description: str = None,
        ResourceQuery: "ResourceQueryTypeDef" = None,
        Tags: Dict[str, str] = None,
        Configuration: List["GroupConfigurationItemTypeDef"] = None,
    ) -> CreateGroupOutputTypeDef:
        """
        [Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resource-groups.html#ResourceGroups.Client.create_group)
        """

    def delete_group(self, GroupName: str = None, Group: str = None) -> DeleteGroupOutputTypeDef:
        """
        [Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resource-groups.html#ResourceGroups.Client.delete_group)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resource-groups.html#ResourceGroups.Client.generate_presigned_url)
        """

    def get_group(self, GroupName: str = None, Group: str = None) -> GetGroupOutputTypeDef:
        """
        [Client.get_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resource-groups.html#ResourceGroups.Client.get_group)
        """

    def get_group_configuration(self, Group: str = None) -> GetGroupConfigurationOutputTypeDef:
        """
        [Client.get_group_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resource-groups.html#ResourceGroups.Client.get_group_configuration)
        """

    def get_group_query(
        self, GroupName: str = None, Group: str = None
    ) -> GetGroupQueryOutputTypeDef:
        """
        [Client.get_group_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resource-groups.html#ResourceGroups.Client.get_group_query)
        """

    def get_tags(self, Arn: str) -> GetTagsOutputTypeDef:
        """
        [Client.get_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resource-groups.html#ResourceGroups.Client.get_tags)
        """

    def group_resources(self, Group: str, ResourceArns: List[str]) -> GroupResourcesOutputTypeDef:
        """
        [Client.group_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resource-groups.html#ResourceGroups.Client.group_resources)
        """

    def list_group_resources(
        self,
        GroupName: str = None,
        Group: str = None,
        Filters: List[ResourceFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListGroupResourcesOutputTypeDef:
        """
        [Client.list_group_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resource-groups.html#ResourceGroups.Client.list_group_resources)
        """

    def list_groups(
        self,
        Filters: List[GroupFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListGroupsOutputTypeDef:
        """
        [Client.list_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resource-groups.html#ResourceGroups.Client.list_groups)
        """

    def search_resources(
        self, ResourceQuery: "ResourceQueryTypeDef", MaxResults: int = None, NextToken: str = None
    ) -> SearchResourcesOutputTypeDef:
        """
        [Client.search_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resource-groups.html#ResourceGroups.Client.search_resources)
        """

    def tag(self, Arn: str, Tags: Dict[str, str]) -> TagOutputTypeDef:
        """
        [Client.tag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resource-groups.html#ResourceGroups.Client.tag)
        """

    def ungroup_resources(
        self, Group: str, ResourceArns: List[str]
    ) -> UngroupResourcesOutputTypeDef:
        """
        [Client.ungroup_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resource-groups.html#ResourceGroups.Client.ungroup_resources)
        """

    def untag(self, Arn: str, Keys: List[str]) -> UntagOutputTypeDef:
        """
        [Client.untag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resource-groups.html#ResourceGroups.Client.untag)
        """

    def update_group(
        self, GroupName: str = None, Group: str = None, Description: str = None
    ) -> UpdateGroupOutputTypeDef:
        """
        [Client.update_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resource-groups.html#ResourceGroups.Client.update_group)
        """

    def update_group_query(
        self, ResourceQuery: "ResourceQueryTypeDef", GroupName: str = None, Group: str = None
    ) -> UpdateGroupQueryOutputTypeDef:
        """
        [Client.update_group_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resource-groups.html#ResourceGroups.Client.update_group_query)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_group_resources"]
    ) -> ListGroupResourcesPaginator:
        """
        [Paginator.ListGroupResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resource-groups.html#ResourceGroups.Paginator.ListGroupResources)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_groups"]) -> ListGroupsPaginator:
        """
        [Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resource-groups.html#ResourceGroups.Paginator.ListGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_resources"]
    ) -> SearchResourcesPaginator:
        """
        [Paginator.SearchResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/resource-groups.html#ResourceGroups.Paginator.SearchResources)
        """
