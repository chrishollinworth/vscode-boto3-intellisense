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
from typing import Any, Dict, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import EndpointAccessTypeType
from .paginator import (
    ListEndpointsPaginator,
    ListOutpostsWithS3Paginator,
    ListSharedEndpointsPaginator,
)
from .type_defs import (
    CreateEndpointResultTypeDef,
    ListEndpointsResultTypeDef,
    ListOutpostsWithS3ResultTypeDef,
    ListSharedEndpointsResultTypeDef,
)

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
    OutpostOfflineException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class S3OutpostsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/s3outposts.html#S3Outposts.Client)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/s3outposts.html#S3Outposts.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/s3outposts.html#S3Outposts.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client.html#close)
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
        Creates an endpoint and associates it with the specified Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/s3outposts.html#S3Outposts.Client.create_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client.html#create_endpoint)
        """
    def delete_endpoint(self, *, EndpointId: str, OutpostId: str) -> None:
        """
        Deletes an endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/s3outposts.html#S3Outposts.Client.delete_endpoint)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/s3outposts.html#S3Outposts.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client.html#generate_presigned_url)
        """
    def list_endpoints(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListEndpointsResultTypeDef:
        """
        Lists endpoints associated with the specified Outpost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/s3outposts.html#S3Outposts.Client.list_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client.html#list_endpoints)
        """
    def list_outposts_with_s3(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListOutpostsWithS3ResultTypeDef:
        """
        Lists the Outposts with S3 on Outposts capacity for your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/s3outposts.html#S3Outposts.Client.list_outposts_with_s3)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client.html#list_outposts_with_s3)
        """
    def list_shared_endpoints(
        self, *, OutpostId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListSharedEndpointsResultTypeDef:
        """
        Lists all endpoints associated with an Outpost that has been shared by Amazon
        Web Services Resource Access Manager (RAM).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/s3outposts.html#S3Outposts.Client.list_shared_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/client.html#list_shared_endpoints)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_endpoints"]) -> ListEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/s3outposts.html#S3Outposts.Paginator.ListEndpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/paginators.html#listendpointspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_outposts_with_s3"]
    ) -> ListOutpostsWithS3Paginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/s3outposts.html#S3Outposts.Paginator.ListOutpostsWithS3)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/paginators.html#listoutpostswiths3paginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_shared_endpoints"]
    ) -> ListSharedEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/s3outposts.html#S3Outposts.Paginator.ListSharedEndpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/paginators.html#listsharedendpointspaginator)
        """
