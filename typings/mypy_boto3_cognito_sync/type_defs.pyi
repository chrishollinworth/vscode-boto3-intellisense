"""
Type annotations for cognito-sync service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_cognito_sync.type_defs import BulkPublishRequestTypeDef

    data: BulkPublishRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import BulkPublishStatusType, OperationType, PlatformType, StreamingStatusType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "BulkPublishRequestTypeDef",
    "BulkPublishResponseTypeDef",
    "CognitoStreamsTypeDef",
    "DatasetTypeDef",
    "DeleteDatasetRequestTypeDef",
    "DeleteDatasetResponseTypeDef",
    "DescribeDatasetRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeIdentityPoolUsageRequestTypeDef",
    "DescribeIdentityPoolUsageResponseTypeDef",
    "DescribeIdentityUsageRequestTypeDef",
    "DescribeIdentityUsageResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetBulkPublishDetailsRequestTypeDef",
    "GetBulkPublishDetailsResponseTypeDef",
    "GetCognitoEventsRequestTypeDef",
    "GetCognitoEventsResponseTypeDef",
    "GetIdentityPoolConfigurationRequestTypeDef",
    "GetIdentityPoolConfigurationResponseTypeDef",
    "IdentityPoolUsageTypeDef",
    "IdentityUsageTypeDef",
    "ListDatasetsRequestTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListIdentityPoolUsageRequestTypeDef",
    "ListIdentityPoolUsageResponseTypeDef",
    "ListRecordsRequestTypeDef",
    "ListRecordsResponseTypeDef",
    "PushSyncOutputTypeDef",
    "PushSyncTypeDef",
    "PushSyncUnionTypeDef",
    "RecordPatchTypeDef",
    "RecordTypeDef",
    "RegisterDeviceRequestTypeDef",
    "RegisterDeviceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SetCognitoEventsRequestTypeDef",
    "SetIdentityPoolConfigurationRequestTypeDef",
    "SetIdentityPoolConfigurationResponseTypeDef",
    "SubscribeToDatasetRequestTypeDef",
    "TimestampTypeDef",
    "UnsubscribeFromDatasetRequestTypeDef",
    "UpdateRecordsRequestTypeDef",
    "UpdateRecordsResponseTypeDef",
)

class BulkPublishRequestTypeDef(TypedDict):
    IdentityPoolId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CognitoStreamsTypeDef(TypedDict):
    StreamName: NotRequired[str]
    RoleArn: NotRequired[str]
    StreamingStatus: NotRequired[StreamingStatusType]

class DatasetTypeDef(TypedDict):
    IdentityId: NotRequired[str]
    DatasetName: NotRequired[str]
    CreationDate: NotRequired[datetime]
    LastModifiedDate: NotRequired[datetime]
    LastModifiedBy: NotRequired[str]
    DataStorage: NotRequired[int]
    NumRecords: NotRequired[int]

class DeleteDatasetRequestTypeDef(TypedDict):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str

class DescribeDatasetRequestTypeDef(TypedDict):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str

class DescribeIdentityPoolUsageRequestTypeDef(TypedDict):
    IdentityPoolId: str

class IdentityPoolUsageTypeDef(TypedDict):
    IdentityPoolId: NotRequired[str]
    SyncSessionsCount: NotRequired[int]
    DataStorage: NotRequired[int]
    LastModifiedDate: NotRequired[datetime]

class DescribeIdentityUsageRequestTypeDef(TypedDict):
    IdentityPoolId: str
    IdentityId: str

class IdentityUsageTypeDef(TypedDict):
    IdentityId: NotRequired[str]
    IdentityPoolId: NotRequired[str]
    LastModifiedDate: NotRequired[datetime]
    DatasetCount: NotRequired[int]
    DataStorage: NotRequired[int]

class GetBulkPublishDetailsRequestTypeDef(TypedDict):
    IdentityPoolId: str

class GetCognitoEventsRequestTypeDef(TypedDict):
    IdentityPoolId: str

class GetIdentityPoolConfigurationRequestTypeDef(TypedDict):
    IdentityPoolId: str

class PushSyncOutputTypeDef(TypedDict):
    ApplicationArns: NotRequired[List[str]]
    RoleArn: NotRequired[str]

class ListDatasetsRequestTypeDef(TypedDict):
    IdentityPoolId: str
    IdentityId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListIdentityPoolUsageRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListRecordsRequestTypeDef(TypedDict):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str
    LastSyncCount: NotRequired[int]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SyncSessionToken: NotRequired[str]

class RecordTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]
    SyncCount: NotRequired[int]
    LastModifiedDate: NotRequired[datetime]
    LastModifiedBy: NotRequired[str]
    DeviceLastModifiedDate: NotRequired[datetime]

class PushSyncTypeDef(TypedDict):
    ApplicationArns: NotRequired[Sequence[str]]
    RoleArn: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class RegisterDeviceRequestTypeDef(TypedDict):
    IdentityPoolId: str
    IdentityId: str
    Platform: PlatformType
    Token: str

class SetCognitoEventsRequestTypeDef(TypedDict):
    IdentityPoolId: str
    Events: Mapping[str, str]

class SubscribeToDatasetRequestTypeDef(TypedDict):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str
    DeviceId: str

class UnsubscribeFromDatasetRequestTypeDef(TypedDict):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str
    DeviceId: str

class BulkPublishResponseTypeDef(TypedDict):
    IdentityPoolId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetBulkPublishDetailsResponseTypeDef(TypedDict):
    IdentityPoolId: str
    BulkPublishStartTime: datetime
    BulkPublishCompleteTime: datetime
    BulkPublishStatus: BulkPublishStatusType
    FailureMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCognitoEventsResponseTypeDef(TypedDict):
    Events: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterDeviceResponseTypeDef(TypedDict):
    DeviceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDatasetResponseTypeDef(TypedDict):
    Dataset: DatasetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDatasetResponseTypeDef(TypedDict):
    Dataset: DatasetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasetsResponseTypeDef(TypedDict):
    Datasets: List[DatasetTypeDef]
    Count: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeIdentityPoolUsageResponseTypeDef(TypedDict):
    IdentityPoolUsage: IdentityPoolUsageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListIdentityPoolUsageResponseTypeDef(TypedDict):
    IdentityPoolUsages: List[IdentityPoolUsageTypeDef]
    MaxResults: int
    Count: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeIdentityUsageResponseTypeDef(TypedDict):
    IdentityUsage: IdentityUsageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdentityPoolConfigurationResponseTypeDef(TypedDict):
    IdentityPoolId: str
    PushSync: PushSyncOutputTypeDef
    CognitoStreams: CognitoStreamsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SetIdentityPoolConfigurationResponseTypeDef(TypedDict):
    IdentityPoolId: str
    PushSync: PushSyncOutputTypeDef
    CognitoStreams: CognitoStreamsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecordsResponseTypeDef(TypedDict):
    Records: List[RecordTypeDef]
    Count: int
    DatasetSyncCount: int
    LastModifiedBy: str
    MergedDatasetNames: List[str]
    DatasetExists: bool
    DatasetDeletedAfterRequestedSyncCount: bool
    SyncSessionToken: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateRecordsResponseTypeDef(TypedDict):
    Records: List[RecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

PushSyncUnionTypeDef = Union[PushSyncTypeDef, PushSyncOutputTypeDef]

class RecordPatchTypeDef(TypedDict):
    Op: OperationType
    Key: str
    SyncCount: int
    Value: NotRequired[str]
    DeviceLastModifiedDate: NotRequired[TimestampTypeDef]

class SetIdentityPoolConfigurationRequestTypeDef(TypedDict):
    IdentityPoolId: str
    PushSync: NotRequired[PushSyncUnionTypeDef]
    CognitoStreams: NotRequired[CognitoStreamsTypeDef]

class UpdateRecordsRequestTypeDef(TypedDict):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str
    SyncSessionToken: str
    DeviceId: NotRequired[str]
    RecordPatches: NotRequired[Sequence[RecordPatchTypeDef]]
    ClientContext: NotRequired[str]
