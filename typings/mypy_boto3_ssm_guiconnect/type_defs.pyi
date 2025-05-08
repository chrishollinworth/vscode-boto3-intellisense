"""
Type annotations for ssm-guiconnect service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_guiconnect/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_ssm_guiconnect.type_defs import DeleteConnectionRecordingPreferencesRequestTypeDef

    data: DeleteConnectionRecordingPreferencesRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import Union

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ConnectionRecordingPreferencesOutputTypeDef",
    "ConnectionRecordingPreferencesTypeDef",
    "ConnectionRecordingPreferencesUnionTypeDef",
    "DeleteConnectionRecordingPreferencesRequestTypeDef",
    "DeleteConnectionRecordingPreferencesResponseTypeDef",
    "GetConnectionRecordingPreferencesResponseTypeDef",
    "RecordingDestinationsOutputTypeDef",
    "RecordingDestinationsTypeDef",
    "ResponseMetadataTypeDef",
    "S3BucketTypeDef",
    "UpdateConnectionRecordingPreferencesRequestTypeDef",
    "UpdateConnectionRecordingPreferencesResponseTypeDef",
)

class DeleteConnectionRecordingPreferencesRequestTypeDef(TypedDict):
    ClientToken: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class S3BucketTypeDef(TypedDict):
    BucketName: str
    BucketOwner: str

class DeleteConnectionRecordingPreferencesResponseTypeDef(TypedDict):
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RecordingDestinationsOutputTypeDef(TypedDict):
    S3Buckets: List[S3BucketTypeDef]

class RecordingDestinationsTypeDef(TypedDict):
    S3Buckets: Sequence[S3BucketTypeDef]

class ConnectionRecordingPreferencesOutputTypeDef(TypedDict):
    KMSKeyArn: str
    RecordingDestinations: RecordingDestinationsOutputTypeDef

class ConnectionRecordingPreferencesTypeDef(TypedDict):
    KMSKeyArn: str
    RecordingDestinations: RecordingDestinationsTypeDef

class GetConnectionRecordingPreferencesResponseTypeDef(TypedDict):
    ClientToken: str
    ConnectionRecordingPreferences: ConnectionRecordingPreferencesOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectionRecordingPreferencesResponseTypeDef(TypedDict):
    ClientToken: str
    ConnectionRecordingPreferences: ConnectionRecordingPreferencesOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

ConnectionRecordingPreferencesUnionTypeDef = Union[
    ConnectionRecordingPreferencesTypeDef, ConnectionRecordingPreferencesOutputTypeDef
]

class UpdateConnectionRecordingPreferencesRequestTypeDef(TypedDict):
    ConnectionRecordingPreferences: ConnectionRecordingPreferencesUnionTypeDef
    ClientToken: NotRequired[str]
