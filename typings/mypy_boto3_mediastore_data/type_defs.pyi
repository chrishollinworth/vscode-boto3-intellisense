"""
Type annotations for mediastore-data service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore_data/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_mediastore_data.type_defs import BlobTypeDef

    data: BlobTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import ItemTypeType, UploadAvailabilityType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
else:
    from typing import Dict, List
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "BlobTypeDef",
    "DeleteObjectRequestTypeDef",
    "DescribeObjectRequestTypeDef",
    "DescribeObjectResponseTypeDef",
    "GetObjectRequestTypeDef",
    "GetObjectResponseTypeDef",
    "ItemTypeDef",
    "ListItemsRequestPaginateTypeDef",
    "ListItemsRequestTypeDef",
    "ListItemsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutObjectRequestTypeDef",
    "PutObjectResponseTypeDef",
    "ResponseMetadataTypeDef",
)

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class DeleteObjectRequestTypeDef(TypedDict):
    Path: str

class DescribeObjectRequestTypeDef(TypedDict):
    Path: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class GetObjectRequestTypeDef(TypedDict):
    Path: str
    Range: NotRequired[str]

ItemTypeDef = TypedDict(
    "ItemTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[ItemTypeType],
        "ETag": NotRequired[str],
        "LastModified": NotRequired[datetime],
        "ContentType": NotRequired[str],
        "ContentLength": NotRequired[int],
    },
)

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListItemsRequestTypeDef(TypedDict):
    Path: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class PutObjectRequestTypeDef(TypedDict):
    Body: BlobTypeDef
    Path: str
    ContentType: NotRequired[str]
    CacheControl: NotRequired[str]
    StorageClass: NotRequired[Literal["TEMPORAL"]]
    UploadAvailability: NotRequired[UploadAvailabilityType]

class DescribeObjectResponseTypeDef(TypedDict):
    ETag: str
    ContentType: str
    ContentLength: int
    CacheControl: str
    LastModified: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetObjectResponseTypeDef(TypedDict):
    Body: StreamingBody
    CacheControl: str
    ContentRange: str
    ContentLength: int
    ContentType: str
    ETag: str
    LastModified: datetime
    StatusCode: int
    ResponseMetadata: ResponseMetadataTypeDef

class PutObjectResponseTypeDef(TypedDict):
    ContentSHA256: str
    ETag: str
    StorageClass: Literal["TEMPORAL"]
    ResponseMetadata: ResponseMetadataTypeDef

class ListItemsResponseTypeDef(TypedDict):
    Items: List[ItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListItemsRequestPaginateTypeDef(TypedDict):
    Path: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]
