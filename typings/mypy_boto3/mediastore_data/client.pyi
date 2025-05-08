"""
Type annotations for mediastore-data service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore_data/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mediastore_data.client import MediaStoreDataClient

    session = Session()
    client: MediaStoreDataClient = session.client("mediastore-data")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListItemsPaginator
from .type_defs import (
    DeleteObjectRequestTypeDef,
    DescribeObjectRequestTypeDef,
    DescribeObjectResponseTypeDef,
    GetObjectRequestTypeDef,
    GetObjectResponseTypeDef,
    ListItemsRequestTypeDef,
    ListItemsResponseTypeDef,
    PutObjectRequestTypeDef,
    PutObjectResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("MediaStoreDataClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ContainerNotFoundException: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    ObjectNotFoundException: Type[BotocoreClientError]
    RequestedRangeNotSatisfiableException: Type[BotocoreClientError]

class MediaStoreDataClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data.html#MediaStoreData.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore_data/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MediaStoreDataClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data.html#MediaStoreData.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore_data/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore_data/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore_data/client/#generate_presigned_url)
        """

    def delete_object(self, **kwargs: Unpack[DeleteObjectRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an object at the specified path.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data/client/delete_object.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore_data/client/#delete_object)
        """

    def describe_object(
        self, **kwargs: Unpack[DescribeObjectRequestTypeDef]
    ) -> DescribeObjectResponseTypeDef:
        """
        Gets the headers for an object at the specified path.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data/client/describe_object.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore_data/client/#describe_object)
        """

    def get_object(self, **kwargs: Unpack[GetObjectRequestTypeDef]) -> GetObjectResponseTypeDef:
        """
        Downloads the object at the specified path.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data/client/get_object.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore_data/client/#get_object)
        """

    def list_items(self, **kwargs: Unpack[ListItemsRequestTypeDef]) -> ListItemsResponseTypeDef:
        """
        Provides a list of metadata entries about folders and objects in the specified
        folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data/client/list_items.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore_data/client/#list_items)
        """

    def put_object(self, **kwargs: Unpack[PutObjectRequestTypeDef]) -> PutObjectResponseTypeDef:
        """
        Uploads an object to the specified path.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data/client/put_object.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore_data/client/#put_object)
        """

    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_items"]
    ) -> ListItemsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore_data/client/#get_paginator)
        """
