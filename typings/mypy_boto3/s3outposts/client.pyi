"""
Type annotations for s3outposts service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_s3outposts import S3OutpostsClient

    client: S3OutpostsClient = boto3.client("s3outposts")
    ```
"""
import sys
from typing import Any, Dict, Type

from botocore.client import BaseClient, ClientMeta

from .literals import EndpointAccessTypeType
from .paginator import ListEndpointsPaginator
from .type_defs import CreateEndpointResultTypeDef, ListEndpointsResultTypeDef

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

class S3OutpostsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3outposts.html#S3Outposts.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        S3OutpostsClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3outposts.html#S3Outposts.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client.html#can_paginate)
        """
    def create_endpoint(
        self,
        *,
        OutpostId: str,
        SubnetId: str,
        SecurityGroupId: str,
        AccessType: EndpointAccessTypeType = None,
        CustomerOwnedIpv4Pool: str = None
    ) -> CreateEndpointResultTypeDef:
        """
        Amazon S3 on Outposts Access Points simplify managing data access at scale for
        shared datasets in S3 on Outposts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3outposts.html#S3Outposts.Client.create_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client.html#create_endpoint)
        """
    def delete_endpoint(self, *, EndpointId: str, OutpostId: str) -> None:
        """
        Amazon S3 on Outposts Access Points simplify managing data access at scale for
        shared datasets in S3 on Outposts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3outposts.html#S3Outposts.Client.delete_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client.html#delete_endpoint)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3outposts.html#S3Outposts.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client.html#generate_presigned_url)
        """
    def list_endpoints(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListEndpointsResultTypeDef:
        """
        Amazon S3 on Outposts Access Points simplify managing data access at scale for
        shared datasets in S3 on Outposts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3outposts.html#S3Outposts.Client.list_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client.html#list_endpoints)
        """
    def get_paginator(self, operation_name: Literal["list_endpoints"]) -> ListEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3outposts.html#S3Outposts.Paginator.ListEndpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/paginators.html#listendpointspaginator)
        """
