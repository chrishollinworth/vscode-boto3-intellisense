# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for mediastore-data service client

Usage::

    ```python
    import boto3
    from mypy_boto3_mediastore_data import MediaStoreDataClient

    client: MediaStoreDataClient = boto3.client("mediastore-data")
    ```
"""
import sys
from typing import IO, Any, Dict, Type, Union

from botocore.client import ClientMeta

from mypy_boto3_mediastore_data.paginator import ListItemsPaginator
from mypy_boto3_mediastore_data.type_defs import (
    DescribeObjectResponseTypeDef,
    GetObjectResponseTypeDef,
    ListItemsResponseTypeDef,
    PutObjectResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MediaStoreDataClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ContainerNotFoundException: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    ObjectNotFoundException: Type[BotocoreClientError]
    RequestedRangeNotSatisfiableException: Type[BotocoreClientError]


class MediaStoreDataClient:
    """
    [MediaStoreData.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore-data.html#MediaStoreData.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore-data.html#MediaStoreData.Client.can_paginate)
        """

    def delete_object(self, Path: str) -> Dict[str, Any]:
        """
        [Client.delete_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore-data.html#MediaStoreData.Client.delete_object)
        """

    def describe_object(self, Path: str) -> DescribeObjectResponseTypeDef:
        """
        [Client.describe_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore-data.html#MediaStoreData.Client.describe_object)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore-data.html#MediaStoreData.Client.generate_presigned_url)
        """

    def get_object(self, Path: str, Range: str = None) -> GetObjectResponseTypeDef:
        """
        [Client.get_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore-data.html#MediaStoreData.Client.get_object)
        """

    def list_items(
        self, Path: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListItemsResponseTypeDef:
        """
        [Client.list_items documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore-data.html#MediaStoreData.Client.list_items)
        """

    def put_object(
        self,
        Body: Union[bytes, IO[bytes]],
        Path: str,
        ContentType: str = None,
        CacheControl: str = None,
        StorageClass: Literal["TEMPORAL"] = None,
        UploadAvailability: Literal["STANDARD", "STREAMING"] = None,
    ) -> PutObjectResponseTypeDef:
        """
        [Client.put_object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore-data.html#MediaStoreData.Client.put_object)
        """

    def get_paginator(self, operation_name: Literal["list_items"]) -> ListItemsPaginator:
        """
        [Paginator.ListItems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore-data.html#MediaStoreData.Paginator.ListItems)
        """
