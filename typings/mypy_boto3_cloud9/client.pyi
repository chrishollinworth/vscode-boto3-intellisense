"""
Type annotations for cloud9 service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_cloud9 import Cloud9Client

    client: Cloud9Client = boto3.client("cloud9")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ConnectionTypeType,
    ManagedCredentialsActionType,
    MemberPermissionsType,
    PermissionsType,
)
from .paginator import DescribeEnvironmentMembershipsPaginator, ListEnvironmentsPaginator
from .type_defs import (
    CreateEnvironmentEC2ResultTypeDef,
    CreateEnvironmentMembershipResultTypeDef,
    DescribeEnvironmentMembershipsResultTypeDef,
    DescribeEnvironmentsResultTypeDef,
    DescribeEnvironmentStatusResultTypeDef,
    ListEnvironmentsResultTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagTypeDef,
    UpdateEnvironmentMembershipResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("Cloud9Client",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentAccessException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]

class Cloud9Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/cloud9.html#Cloud9.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        Cloud9Client exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/cloud9.html#Cloud9.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/client.html#can_paginate)
        """
    def create_environment_ec2(
        self,
        *,
        name: str,
        instanceType: str,
        description: str = None,
        clientRequestToken: str = None,
        subnetId: str = None,
        imageId: str = None,
        automaticStopTimeMinutes: int = None,
        ownerArn: str = None,
        tags: List["TagTypeDef"] = None,
        connectionType: ConnectionTypeType = None,
        dryRun: bool = None
    ) -> CreateEnvironmentEC2ResultTypeDef:
        """
        Creates an Cloud9 development environment, launches an Amazon Elastic Compute
        Cloud (Amazon EC2) instance, and then connects from the instance to the
        environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/cloud9.html#Cloud9.Client.create_environment_ec2)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/client.html#create_environment_ec2)
        """
    def create_environment_membership(
        self, *, environmentId: str, userArn: str, permissions: MemberPermissionsType
    ) -> CreateEnvironmentMembershipResultTypeDef:
        """
        Adds an environment member to an Cloud9 development environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/cloud9.html#Cloud9.Client.create_environment_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/client.html#create_environment_membership)
        """
    def delete_environment(self, *, environmentId: str) -> Dict[str, Any]:
        """
        Deletes an Cloud9 development environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/cloud9.html#Cloud9.Client.delete_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/client.html#delete_environment)
        """
    def delete_environment_membership(self, *, environmentId: str, userArn: str) -> Dict[str, Any]:
        """
        Deletes an environment member from an Cloud9 development environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/cloud9.html#Cloud9.Client.delete_environment_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/client.html#delete_environment_membership)
        """
    def describe_environment_memberships(
        self,
        *,
        userArn: str = None,
        environmentId: str = None,
        permissions: List[PermissionsType] = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> DescribeEnvironmentMembershipsResultTypeDef:
        """
        Gets information about environment members for an Cloud9 development
        environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/cloud9.html#Cloud9.Client.describe_environment_memberships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/client.html#describe_environment_memberships)
        """
    def describe_environment_status(
        self, *, environmentId: str
    ) -> DescribeEnvironmentStatusResultTypeDef:
        """
        Gets status information for an Cloud9 development environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/cloud9.html#Cloud9.Client.describe_environment_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/client.html#describe_environment_status)
        """
    def describe_environments(
        self, *, environmentIds: List[str]
    ) -> DescribeEnvironmentsResultTypeDef:
        """
        Gets information about Cloud9 development environments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/cloud9.html#Cloud9.Client.describe_environments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/client.html#describe_environments)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/cloud9.html#Cloud9.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/client.html#generate_presigned_url)
        """
    def list_environments(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListEnvironmentsResultTypeDef:
        """
        Gets a list of Cloud9 development environment identifiers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/cloud9.html#Cloud9.Client.list_environments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/client.html#list_environments)
        """
    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        Gets a list of the tags associated with an Cloud9 development environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/cloud9.html#Cloud9.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/client.html#list_tags_for_resource)
        """
    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds tags to an Cloud9 development environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/cloud9.html#Cloud9.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from an Cloud9 development environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/cloud9.html#Cloud9.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/client.html#untag_resource)
        """
    def update_environment(
        self,
        *,
        environmentId: str,
        name: str = None,
        description: str = None,
        managedCredentialsAction: ManagedCredentialsActionType = None
    ) -> Dict[str, Any]:
        """
        Changes the settings of an existing Cloud9 development environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/cloud9.html#Cloud9.Client.update_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/client.html#update_environment)
        """
    def update_environment_membership(
        self, *, environmentId: str, userArn: str, permissions: MemberPermissionsType
    ) -> UpdateEnvironmentMembershipResultTypeDef:
        """
        Changes the settings of an existing environment member for an Cloud9 development
        environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/cloud9.html#Cloud9.Client.update_environment_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/client.html#update_environment_membership)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_environment_memberships"]
    ) -> DescribeEnvironmentMembershipsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/cloud9.html#Cloud9.Paginator.DescribeEnvironmentMemberships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/paginators.html#describeenvironmentmembershipspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_environments"]
    ) -> ListEnvironmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/cloud9.html#Cloud9.Paginator.ListEnvironments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/paginators.html#listenvironmentspaginator)
        """
