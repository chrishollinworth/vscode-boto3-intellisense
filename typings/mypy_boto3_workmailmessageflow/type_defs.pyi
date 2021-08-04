"""
Type annotations for workmailmessageflow service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmailmessageflow/type_defs.html)

Usage::

    ```python
    from mypy_boto3_workmailmessageflow.type_defs import GetRawMessageContentRequestRequestTypeDef

    data: GetRawMessageContentRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict

from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "GetRawMessageContentRequestRequestTypeDef",
    "GetRawMessageContentResponseTypeDef",
    "PutRawMessageContentRequestRequestTypeDef",
    "RawMessageContentTypeDef",
    "ResponseMetadataTypeDef",
    "S3ReferenceTypeDef",
)

GetRawMessageContentRequestRequestTypeDef = TypedDict(
    "GetRawMessageContentRequestRequestTypeDef",
    {
        "messageId": str,
    },
)

GetRawMessageContentResponseTypeDef = TypedDict(
    "GetRawMessageContentResponseTypeDef",
    {
        "messageContent": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRawMessageContentRequestRequestTypeDef = TypedDict(
    "PutRawMessageContentRequestRequestTypeDef",
    {
        "messageId": str,
        "content": "RawMessageContentTypeDef",
    },
)

RawMessageContentTypeDef = TypedDict(
    "RawMessageContentTypeDef",
    {
        "s3Reference": "S3ReferenceTypeDef",
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

_RequiredS3ReferenceTypeDef = TypedDict(
    "_RequiredS3ReferenceTypeDef",
    {
        "bucket": str,
        "key": str,
    },
)
_OptionalS3ReferenceTypeDef = TypedDict(
    "_OptionalS3ReferenceTypeDef",
    {
        "objectVersion": str,
    },
    total=False,
)

class S3ReferenceTypeDef(_RequiredS3ReferenceTypeDef, _OptionalS3ReferenceTypeDef):
    pass
