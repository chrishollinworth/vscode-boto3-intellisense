"""
Type annotations for cloudfront-keyvaluestore service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront_keyvaluestore/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudfront_keyvaluestore import CloudFrontKeyValueStoreClient

    client: CloudFrontKeyValueStoreClient = boto3.client("cloudfront-keyvaluestore")
    ```
"""

import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .paginator import ListKeysPaginator
from .type_defs import (
    DeleteKeyRequestListItemTypeDef,
    DeleteKeyResponseTypeDef,
    DescribeKeyValueStoreResponseTypeDef,
    GetKeyResponseTypeDef,
    ListKeysResponseTypeDef,
    PutKeyRequestListItemTypeDef,
    PutKeyResponseTypeDef,
    UpdateKeysResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CloudFrontKeyValueStoreClient",)

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
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CloudFrontKeyValueStoreClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudfront-keyvaluestore.html#CloudFrontKeyValueStore.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront_keyvaluestore/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudFrontKeyValueStoreClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudfront-keyvaluestore.html#CloudFrontKeyValueStore.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront_keyvaluestore/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudfront-keyvaluestore.html#CloudFrontKeyValueStore.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront_keyvaluestore/client.html#close)
        """

    def delete_key(self, *, KvsARN: str, Key: str, IfMatch: str) -> DeleteKeyResponseTypeDef:
        """
        Deletes the key value pair specified by the key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudfront-keyvaluestore.html#CloudFrontKeyValueStore.Client.delete_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront_keyvaluestore/client.html#delete_key)
        """

    def describe_key_value_store(self, *, KvsARN: str) -> DescribeKeyValueStoreResponseTypeDef:
        """
        Returns metadata information about Key Value Store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudfront-keyvaluestore.html#CloudFrontKeyValueStore.Client.describe_key_value_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront_keyvaluestore/client.html#describe_key_value_store)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudfront-keyvaluestore.html#CloudFrontKeyValueStore.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront_keyvaluestore/client.html#generate_presigned_url)
        """

    def get_key(self, *, KvsARN: str, Key: str) -> GetKeyResponseTypeDef:
        """
        Returns a key value pair.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudfront-keyvaluestore.html#CloudFrontKeyValueStore.Client.get_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront_keyvaluestore/client.html#get_key)
        """

    def list_keys(
        self, *, KvsARN: str, NextToken: str = None, MaxResults: int = None
    ) -> ListKeysResponseTypeDef:
        """
        Returns a list of key value pairs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudfront-keyvaluestore.html#CloudFrontKeyValueStore.Client.list_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront_keyvaluestore/client.html#list_keys)
        """

    def put_key(self, *, Key: str, Value: str, KvsARN: str, IfMatch: str) -> PutKeyResponseTypeDef:
        """
        Creates a new key value pair or replaces the value of an existing key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudfront-keyvaluestore.html#CloudFrontKeyValueStore.Client.put_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront_keyvaluestore/client.html#put_key)
        """

    def update_keys(
        self,
        *,
        KvsARN: str,
        IfMatch: str,
        Puts: List["PutKeyRequestListItemTypeDef"] = None,
        Deletes: List["DeleteKeyRequestListItemTypeDef"] = None
    ) -> UpdateKeysResponseTypeDef:
        """
        Puts or Deletes multiple key value pairs in a single, all-or-nothing operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudfront-keyvaluestore.html#CloudFrontKeyValueStore.Client.update_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront_keyvaluestore/client.html#update_keys)
        """

    def get_paginator(self, operation_name: Literal["list_keys"]) -> ListKeysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudfront-keyvaluestore.html#CloudFrontKeyValueStore.Paginator.ListKeys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront_keyvaluestore/paginators.html#listkeyspaginator)
        """
