# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for s3outposts service client

Usage::

    ```python
    import boto3
    from mypy_boto3_s3outposts import S3OutpostsClient

    client: S3OutpostsClient = boto3.client("s3outposts")
    ```
"""
import sys
from typing import Any, Dict, Type

from botocore.client import ClientMeta

from mypy_boto3_s3outposts.paginator import ListEndpointsPaginator
from mypy_boto3_s3outposts.type_defs import CreateEndpointResultTypeDef, ListEndpointsResultTypeDef

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("S3OutpostsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class S3OutpostsClient:
    """
    [S3Outposts.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3outposts.html#S3Outposts.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3outposts.html#S3Outposts.Client.can_paginate)
        """

    def create_endpoint(
        self, OutpostId: str, SubnetId: str, SecurityGroupId: str
    ) -> CreateEndpointResultTypeDef:
        """
        [Client.create_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3outposts.html#S3Outposts.Client.create_endpoint)
        """

    def delete_endpoint(self, EndpointId: str, OutpostId: str) -> None:
        """
        [Client.delete_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3outposts.html#S3Outposts.Client.delete_endpoint)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3outposts.html#S3Outposts.Client.generate_presigned_url)
        """

    def list_endpoints(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListEndpointsResultTypeDef:
        """
        [Client.list_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3outposts.html#S3Outposts.Client.list_endpoints)
        """

    def get_paginator(self, operation_name: Literal["list_endpoints"]) -> ListEndpointsPaginator:
        """
        [Paginator.ListEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/s3outposts.html#S3Outposts.Paginator.ListEndpoints)
        """
