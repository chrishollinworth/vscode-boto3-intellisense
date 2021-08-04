"""
Type annotations for identitystore service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_identitystore import IdentityStoreClient

    client: IdentityStoreClient = boto3.client("identitystore")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    DescribeGroupResponseTypeDef,
    DescribeUserResponseTypeDef,
    FilterTypeDef,
    ListGroupsResponseTypeDef,
    ListUsersResponseTypeDef,
)

__all__ = ("IdentityStoreClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class IdentityStoreClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/identitystore.html#IdentityStore.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        IdentityStoreClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/identitystore.html#IdentityStore.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#can_paginate)
        """
    def describe_group(self, *, IdentityStoreId: str, GroupId: str) -> DescribeGroupResponseTypeDef:
        """
        Retrieves the group metadata and attributes from `GroupId` in an identity store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/identitystore.html#IdentityStore.Client.describe_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#describe_group)
        """
    def describe_user(self, *, IdentityStoreId: str, UserId: str) -> DescribeUserResponseTypeDef:
        """
        Retrieves the user metadata and attributes from `UserId` in an identity store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/identitystore.html#IdentityStore.Client.describe_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#describe_user)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/identitystore.html#IdentityStore.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#generate_presigned_url)
        """
    def list_groups(
        self,
        *,
        IdentityStoreId: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["FilterTypeDef"] = None
    ) -> ListGroupsResponseTypeDef:
        """
        Lists the attribute name and value of the group that you specified in the
        search.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/identitystore.html#IdentityStore.Client.list_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#list_groups)
        """
    def list_users(
        self,
        *,
        IdentityStoreId: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["FilterTypeDef"] = None
    ) -> ListUsersResponseTypeDef:
        """
        Lists the attribute name and value of the user that you specified in the search.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/identitystore.html#IdentityStore.Client.list_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/client.html#list_users)
        """
