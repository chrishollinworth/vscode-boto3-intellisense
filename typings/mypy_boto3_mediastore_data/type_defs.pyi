"""
Type annotations for mediastore-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mediastore_data.type_defs import DeleteObjectRequestRequestTypeDef

    data: DeleteObjectRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import ItemTypeType, UploadAvailabilityType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "DeleteObjectRequestRequestTypeDef",
    "DescribeObjectRequestRequestTypeDef",
    "DescribeObjectResponseTypeDef",
    "GetObjectRequestRequestTypeDef",
    "GetObjectResponseTypeDef",
    "ItemTypeDef",
    "ListItemsRequestRequestTypeDef",
    "ListItemsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutObjectRequestRequestTypeDef",
    "PutObjectResponseTypeDef",
    "ResponseMetadataTypeDef",
)

DeleteObjectRequestRequestTypeDef = TypedDict(
    "DeleteObjectRequestRequestTypeDef",
    {
        "Path": str,
    },
)

DescribeObjectRequestRequestTypeDef = TypedDict(
    "DescribeObjectRequestRequestTypeDef",
    {
        "Path": str,
    },
)

DescribeObjectResponseTypeDef = TypedDict(
    "DescribeObjectResponseTypeDef",
    {
        "ETag": str,
        "ContentType": str,
        "ContentLength": int,
        "CacheControl": str,
        "LastModified": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetObjectRequestRequestTypeDef = TypedDict(
    "_RequiredGetObjectRequestRequestTypeDef",
    {
        "Path": str,
    },
)
_OptionalGetObjectRequestRequestTypeDef = TypedDict(
    "_OptionalGetObjectRequestRequestTypeDef",
    {
        "Range": str,
    },
    total=False,
)

class GetObjectRequestRequestTypeDef(
    _RequiredGetObjectRequestRequestTypeDef, _OptionalGetObjectRequestRequestTypeDef
):
    pass

GetObjectResponseTypeDef = TypedDict(
    "GetObjectResponseTypeDef",
    {
        "Body": StreamingBody,
        "CacheControl": str,
        "ContentRange": str,
        "ContentLength": int,
        "ContentType": str,
        "ETag": str,
        "LastModified": datetime,
        "StatusCode": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ItemTypeDef = TypedDict(
    "ItemTypeDef",
    {
        "Name": str,
        "Type": ItemTypeType,
        "ETag": str,
        "LastModified": datetime,
        "ContentType": str,
        "ContentLength": int,
    },
    total=False,
)

ListItemsRequestRequestTypeDef = TypedDict(
    "ListItemsRequestRequestTypeDef",
    {
        "Path": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListItemsResponseTypeDef = TypedDict(
    "ListItemsResponseTypeDef",
    {
        "Items": List["ItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredPutObjectRequestRequestTypeDef = TypedDict(
    "_RequiredPutObjectRequestRequestTypeDef",
    {
        "Body": Union[bytes, IO[bytes], StreamingBody],
        "Path": str,
    },
)
_OptionalPutObjectRequestRequestTypeDef = TypedDict(
    "_OptionalPutObjectRequestRequestTypeDef",
    {
        "ContentType": str,
        "CacheControl": str,
        "StorageClass": Literal["TEMPORAL"],
        "UploadAvailability": UploadAvailabilityType,
    },
    total=False,
)

class PutObjectRequestRequestTypeDef(
    _RequiredPutObjectRequestRequestTypeDef, _OptionalPutObjectRequestRequestTypeDef
):
    pass

PutObjectResponseTypeDef = TypedDict(
    "PutObjectResponseTypeDef",
    {
        "ContentSHA256": str,
        "ETag": str,
        "StorageClass": Literal["TEMPORAL"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)
