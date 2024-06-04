"""
Type annotations for cloudfront-keyvaluestore service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront_keyvaluestore/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudfront_keyvaluestore.type_defs import DeleteKeyRequestListItemTypeDef

    data: DeleteKeyRequestListItemTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "DeleteKeyRequestListItemTypeDef",
    "DeleteKeyRequestRequestTypeDef",
    "DeleteKeyResponseTypeDef",
    "DescribeKeyValueStoreRequestRequestTypeDef",
    "DescribeKeyValueStoreResponseTypeDef",
    "GetKeyRequestRequestTypeDef",
    "GetKeyResponseTypeDef",
    "ListKeysRequestRequestTypeDef",
    "ListKeysResponseListItemTypeDef",
    "ListKeysResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutKeyRequestListItemTypeDef",
    "PutKeyRequestRequestTypeDef",
    "PutKeyResponseTypeDef",
    "ResponseMetadataTypeDef",
    "UpdateKeysRequestRequestTypeDef",
    "UpdateKeysResponseTypeDef",
)

DeleteKeyRequestListItemTypeDef = TypedDict(
    "DeleteKeyRequestListItemTypeDef",
    {
        "Key": str,
    },
)

DeleteKeyRequestRequestTypeDef = TypedDict(
    "DeleteKeyRequestRequestTypeDef",
    {
        "KvsARN": str,
        "Key": str,
        "IfMatch": str,
    },
)

DeleteKeyResponseTypeDef = TypedDict(
    "DeleteKeyResponseTypeDef",
    {
        "ItemCount": int,
        "TotalSizeInBytes": int,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeKeyValueStoreRequestRequestTypeDef = TypedDict(
    "DescribeKeyValueStoreRequestRequestTypeDef",
    {
        "KvsARN": str,
    },
)

DescribeKeyValueStoreResponseTypeDef = TypedDict(
    "DescribeKeyValueStoreResponseTypeDef",
    {
        "ItemCount": int,
        "TotalSizeInBytes": int,
        "KvsARN": str,
        "Created": datetime,
        "ETag": str,
        "LastModified": datetime,
        "Status": str,
        "FailureReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKeyRequestRequestTypeDef = TypedDict(
    "GetKeyRequestRequestTypeDef",
    {
        "KvsARN": str,
        "Key": str,
    },
)

GetKeyResponseTypeDef = TypedDict(
    "GetKeyResponseTypeDef",
    {
        "Key": str,
        "Value": str,
        "ItemCount": int,
        "TotalSizeInBytes": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListKeysRequestRequestTypeDef = TypedDict(
    "_RequiredListKeysRequestRequestTypeDef",
    {
        "KvsARN": str,
    },
)
_OptionalListKeysRequestRequestTypeDef = TypedDict(
    "_OptionalListKeysRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListKeysRequestRequestTypeDef(
    _RequiredListKeysRequestRequestTypeDef, _OptionalListKeysRequestRequestTypeDef
):
    pass

ListKeysResponseListItemTypeDef = TypedDict(
    "ListKeysResponseListItemTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

ListKeysResponseTypeDef = TypedDict(
    "ListKeysResponseTypeDef",
    {
        "NextToken": str,
        "Items": List["ListKeysResponseListItemTypeDef"],
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

PutKeyRequestListItemTypeDef = TypedDict(
    "PutKeyRequestListItemTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

PutKeyRequestRequestTypeDef = TypedDict(
    "PutKeyRequestRequestTypeDef",
    {
        "Key": str,
        "Value": str,
        "KvsARN": str,
        "IfMatch": str,
    },
)

PutKeyResponseTypeDef = TypedDict(
    "PutKeyResponseTypeDef",
    {
        "ItemCount": int,
        "TotalSizeInBytes": int,
        "ETag": str,
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

_RequiredUpdateKeysRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateKeysRequestRequestTypeDef",
    {
        "KvsARN": str,
        "IfMatch": str,
    },
)
_OptionalUpdateKeysRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateKeysRequestRequestTypeDef",
    {
        "Puts": List["PutKeyRequestListItemTypeDef"],
        "Deletes": List["DeleteKeyRequestListItemTypeDef"],
    },
    total=False,
)

class UpdateKeysRequestRequestTypeDef(
    _RequiredUpdateKeysRequestRequestTypeDef, _OptionalUpdateKeysRequestRequestTypeDef
):
    pass

UpdateKeysResponseTypeDef = TypedDict(
    "UpdateKeysResponseTypeDef",
    {
        "ItemCount": int,
        "TotalSizeInBytes": int,
        "ETag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
