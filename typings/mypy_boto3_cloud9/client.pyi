# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for cloud9 service client

Usage::

    ```python
    import boto3
    from mypy_boto3_cloud9 import Cloud9Client

    client: Cloud9Client = boto3.client("cloud9")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_cloud9.paginator import (
    DescribeEnvironmentMembershipsPaginator,
    ListEnvironmentsPaginator,
)
from mypy_boto3_cloud9.type_defs import (
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


class Exceptions:
    BadRequestException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    ConcurrentAccessException: Type[Boto3ClientError]
    ConflictException: Type[Boto3ClientError]
    ForbiddenException: Type[Boto3ClientError]
    InternalServerErrorException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    NotFoundException: Type[Boto3ClientError]
    TooManyRequestsException: Type[Boto3ClientError]


class Cloud9Client:
    """
    [Cloud9.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloud9.html#Cloud9.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloud9.html#Cloud9.Client.can_paginate)
        """

    def create_environment_ec2(
        self,
        name: str,
        instanceType: str,
        description: str = None,
        clientRequestToken: str = None,
        subnetId: str = None,
        automaticStopTimeMinutes: int = None,
        ownerArn: str = None,
        tags: List["TagTypeDef"] = None,
        connectionType: Literal["CONNECT_SSH", "CONNECT_SSM"] = None,
    ) -> CreateEnvironmentEC2ResultTypeDef:
        """
        [Client.create_environment_ec2 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloud9.html#Cloud9.Client.create_environment_ec2)
        """

    def create_environment_membership(
        self, environmentId: str, userArn: str, permissions: Literal["read-write", "read-only"]
    ) -> CreateEnvironmentMembershipResultTypeDef:
        """
        [Client.create_environment_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloud9.html#Cloud9.Client.create_environment_membership)
        """

    def delete_environment(self, environmentId: str) -> Dict[str, Any]:
        """
        [Client.delete_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloud9.html#Cloud9.Client.delete_environment)
        """

    def delete_environment_membership(self, environmentId: str, userArn: str) -> Dict[str, Any]:
        """
        [Client.delete_environment_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloud9.html#Cloud9.Client.delete_environment_membership)
        """

    def describe_environment_memberships(
        self,
        userArn: str = None,
        environmentId: str = None,
        permissions: List[Literal["owner", "read-write", "read-only"]] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeEnvironmentMembershipsResultTypeDef:
        """
        [Client.describe_environment_memberships documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloud9.html#Cloud9.Client.describe_environment_memberships)
        """

    def describe_environment_status(
        self, environmentId: str
    ) -> DescribeEnvironmentStatusResultTypeDef:
        """
        [Client.describe_environment_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloud9.html#Cloud9.Client.describe_environment_status)
        """

    def describe_environments(self, environmentIds: List[str]) -> DescribeEnvironmentsResultTypeDef:
        """
        [Client.describe_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloud9.html#Cloud9.Client.describe_environments)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloud9.html#Cloud9.Client.generate_presigned_url)
        """

    def list_environments(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListEnvironmentsResultTypeDef:
        """
        [Client.list_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloud9.html#Cloud9.Client.list_environments)
        """

    def list_tags_for_resource(self, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloud9.html#Cloud9.Client.list_tags_for_resource)
        """

    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloud9.html#Cloud9.Client.tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloud9.html#Cloud9.Client.untag_resource)
        """

    def update_environment(
        self, environmentId: str, name: str = None, description: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloud9.html#Cloud9.Client.update_environment)
        """

    def update_environment_membership(
        self, environmentId: str, userArn: str, permissions: Literal["read-write", "read-only"]
    ) -> UpdateEnvironmentMembershipResultTypeDef:
        """
        [Client.update_environment_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloud9.html#Cloud9.Client.update_environment_membership)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_environment_memberships"]
    ) -> DescribeEnvironmentMembershipsPaginator:
        """
        [Paginator.DescribeEnvironmentMemberships documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloud9.html#Cloud9.Paginator.DescribeEnvironmentMemberships)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_environments"]
    ) -> ListEnvironmentsPaginator:
        """
        [Paginator.ListEnvironments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloud9.html#Cloud9.Paginator.ListEnvironments)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
