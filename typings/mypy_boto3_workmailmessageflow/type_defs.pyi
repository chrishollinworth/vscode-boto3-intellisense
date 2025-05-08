"""
Type annotations for workmailmessageflow service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmailmessageflow/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_workmailmessageflow.type_defs import GetRawMessageContentRequestTypeDef

    data: GetRawMessageContentRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

from botocore.response import StreamingBody

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
else:
    from typing import Dict
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "GetRawMessageContentRequestTypeDef",
    "GetRawMessageContentResponseTypeDef",
    "PutRawMessageContentRequestTypeDef",
    "RawMessageContentTypeDef",
    "ResponseMetadataTypeDef",
    "S3ReferenceTypeDef",
)

class GetRawMessageContentRequestTypeDef(TypedDict):
    messageId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class S3ReferenceTypeDef(TypedDict):
    bucket: str
    key: str
    objectVersion: NotRequired[str]

class GetRawMessageContentResponseTypeDef(TypedDict):
    messageContent: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class RawMessageContentTypeDef(TypedDict):
    s3Reference: S3ReferenceTypeDef

class PutRawMessageContentRequestTypeDef(TypedDict):
    messageId: str
    content: RawMessageContentTypeDef
