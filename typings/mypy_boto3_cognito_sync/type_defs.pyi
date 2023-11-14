"""
Type annotations for cognito-sync service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cognito_sync.type_defs import BulkPublishRequestRequestTypeDef

    data: BulkPublishRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import BulkPublishStatusType, OperationType, PlatformType, StreamingStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "BulkPublishRequestRequestTypeDef",
    "BulkPublishResponseTypeDef",
    "CognitoStreamsTypeDef",
    "DatasetTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteDatasetResponseTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeIdentityPoolUsageRequestRequestTypeDef",
    "DescribeIdentityPoolUsageResponseTypeDef",
    "DescribeIdentityUsageRequestRequestTypeDef",
    "DescribeIdentityUsageResponseTypeDef",
    "GetBulkPublishDetailsRequestRequestTypeDef",
    "GetBulkPublishDetailsResponseTypeDef",
    "GetCognitoEventsRequestRequestTypeDef",
    "GetCognitoEventsResponseTypeDef",
    "GetIdentityPoolConfigurationRequestRequestTypeDef",
    "GetIdentityPoolConfigurationResponseTypeDef",
    "IdentityPoolUsageTypeDef",
    "IdentityUsageTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListIdentityPoolUsageRequestRequestTypeDef",
    "ListIdentityPoolUsageResponseTypeDef",
    "ListRecordsRequestRequestTypeDef",
    "ListRecordsResponseTypeDef",
    "PushSyncTypeDef",
    "RecordPatchTypeDef",
    "RecordTypeDef",
    "RegisterDeviceRequestRequestTypeDef",
    "RegisterDeviceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SetCognitoEventsRequestRequestTypeDef",
    "SetIdentityPoolConfigurationRequestRequestTypeDef",
    "SetIdentityPoolConfigurationResponseTypeDef",
    "SubscribeToDatasetRequestRequestTypeDef",
    "UnsubscribeFromDatasetRequestRequestTypeDef",
    "UpdateRecordsRequestRequestTypeDef",
    "UpdateRecordsResponseTypeDef",
)

BulkPublishRequestRequestTypeDef = TypedDict(
    "BulkPublishRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

BulkPublishResponseTypeDef = TypedDict(
    "BulkPublishResponseTypeDef",
    {
        "IdentityPoolId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CognitoStreamsTypeDef = TypedDict(
    "CognitoStreamsTypeDef",
    {
        "StreamName": str,
        "RoleArn": str,
        "StreamingStatus": StreamingStatusType,
    },
    total=False,
)

DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "IdentityId": str,
        "DatasetName": str,
        "CreationDate": datetime,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "DataStorage": int,
        "NumRecords": int,
    },
    total=False,
)

DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
    },
)

DeleteDatasetResponseTypeDef = TypedDict(
    "DeleteDatasetResponseTypeDef",
    {
        "Dataset": "DatasetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
    },
)

DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "Dataset": "DatasetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIdentityPoolUsageRequestRequestTypeDef = TypedDict(
    "DescribeIdentityPoolUsageRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

DescribeIdentityPoolUsageResponseTypeDef = TypedDict(
    "DescribeIdentityPoolUsageResponseTypeDef",
    {
        "IdentityPoolUsage": "IdentityPoolUsageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIdentityUsageRequestRequestTypeDef = TypedDict(
    "DescribeIdentityUsageRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
    },
)

DescribeIdentityUsageResponseTypeDef = TypedDict(
    "DescribeIdentityUsageResponseTypeDef",
    {
        "IdentityUsage": "IdentityUsageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBulkPublishDetailsRequestRequestTypeDef = TypedDict(
    "GetBulkPublishDetailsRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

GetBulkPublishDetailsResponseTypeDef = TypedDict(
    "GetBulkPublishDetailsResponseTypeDef",
    {
        "IdentityPoolId": str,
        "BulkPublishStartTime": datetime,
        "BulkPublishCompleteTime": datetime,
        "BulkPublishStatus": BulkPublishStatusType,
        "FailureMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCognitoEventsRequestRequestTypeDef = TypedDict(
    "GetCognitoEventsRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

GetCognitoEventsResponseTypeDef = TypedDict(
    "GetCognitoEventsResponseTypeDef",
    {
        "Events": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityPoolConfigurationRequestRequestTypeDef = TypedDict(
    "GetIdentityPoolConfigurationRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

GetIdentityPoolConfigurationResponseTypeDef = TypedDict(
    "GetIdentityPoolConfigurationResponseTypeDef",
    {
        "IdentityPoolId": str,
        "PushSync": "PushSyncTypeDef",
        "CognitoStreams": "CognitoStreamsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityPoolUsageTypeDef = TypedDict(
    "IdentityPoolUsageTypeDef",
    {
        "IdentityPoolId": str,
        "SyncSessionsCount": int,
        "DataStorage": int,
        "LastModifiedDate": datetime,
    },
    total=False,
)

IdentityUsageTypeDef = TypedDict(
    "IdentityUsageTypeDef",
    {
        "IdentityId": str,
        "IdentityPoolId": str,
        "LastModifiedDate": datetime,
        "DatasetCount": int,
        "DataStorage": int,
    },
    total=False,
)

_RequiredListDatasetsRequestRequestTypeDef = TypedDict(
    "_RequiredListDatasetsRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
    },
)
_OptionalListDatasetsRequestRequestTypeDef = TypedDict(
    "_OptionalListDatasetsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListDatasetsRequestRequestTypeDef(
    _RequiredListDatasetsRequestRequestTypeDef, _OptionalListDatasetsRequestRequestTypeDef
):
    pass

ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "Datasets": List["DatasetTypeDef"],
        "Count": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIdentityPoolUsageRequestRequestTypeDef = TypedDict(
    "ListIdentityPoolUsageRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListIdentityPoolUsageResponseTypeDef = TypedDict(
    "ListIdentityPoolUsageResponseTypeDef",
    {
        "IdentityPoolUsages": List["IdentityPoolUsageTypeDef"],
        "MaxResults": int,
        "Count": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRecordsRequestRequestTypeDef = TypedDict(
    "_RequiredListRecordsRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
    },
)
_OptionalListRecordsRequestRequestTypeDef = TypedDict(
    "_OptionalListRecordsRequestRequestTypeDef",
    {
        "LastSyncCount": int,
        "NextToken": str,
        "MaxResults": int,
        "SyncSessionToken": str,
    },
    total=False,
)

class ListRecordsRequestRequestTypeDef(
    _RequiredListRecordsRequestRequestTypeDef, _OptionalListRecordsRequestRequestTypeDef
):
    pass

ListRecordsResponseTypeDef = TypedDict(
    "ListRecordsResponseTypeDef",
    {
        "Records": List["RecordTypeDef"],
        "NextToken": str,
        "Count": int,
        "DatasetSyncCount": int,
        "LastModifiedBy": str,
        "MergedDatasetNames": List[str],
        "DatasetExists": bool,
        "DatasetDeletedAfterRequestedSyncCount": bool,
        "SyncSessionToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PushSyncTypeDef = TypedDict(
    "PushSyncTypeDef",
    {
        "ApplicationArns": List[str],
        "RoleArn": str,
    },
    total=False,
)

_RequiredRecordPatchTypeDef = TypedDict(
    "_RequiredRecordPatchTypeDef",
    {
        "Op": OperationType,
        "Key": str,
        "SyncCount": int,
    },
)
_OptionalRecordPatchTypeDef = TypedDict(
    "_OptionalRecordPatchTypeDef",
    {
        "Value": str,
        "DeviceLastModifiedDate": Union[datetime, str],
    },
    total=False,
)

class RecordPatchTypeDef(_RequiredRecordPatchTypeDef, _OptionalRecordPatchTypeDef):
    pass

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "Key": str,
        "Value": str,
        "SyncCount": int,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "DeviceLastModifiedDate": datetime,
    },
    total=False,
)

RegisterDeviceRequestRequestTypeDef = TypedDict(
    "RegisterDeviceRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "Platform": PlatformType,
        "Token": str,
    },
)

RegisterDeviceResponseTypeDef = TypedDict(
    "RegisterDeviceResponseTypeDef",
    {
        "DeviceId": str,
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

SetCognitoEventsRequestRequestTypeDef = TypedDict(
    "SetCognitoEventsRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "Events": Dict[str, str],
    },
)

_RequiredSetIdentityPoolConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredSetIdentityPoolConfigurationRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)
_OptionalSetIdentityPoolConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalSetIdentityPoolConfigurationRequestRequestTypeDef",
    {
        "PushSync": "PushSyncTypeDef",
        "CognitoStreams": "CognitoStreamsTypeDef",
    },
    total=False,
)

class SetIdentityPoolConfigurationRequestRequestTypeDef(
    _RequiredSetIdentityPoolConfigurationRequestRequestTypeDef,
    _OptionalSetIdentityPoolConfigurationRequestRequestTypeDef,
):
    pass

SetIdentityPoolConfigurationResponseTypeDef = TypedDict(
    "SetIdentityPoolConfigurationResponseTypeDef",
    {
        "IdentityPoolId": str,
        "PushSync": "PushSyncTypeDef",
        "CognitoStreams": "CognitoStreamsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubscribeToDatasetRequestRequestTypeDef = TypedDict(
    "SubscribeToDatasetRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
        "DeviceId": str,
    },
)

UnsubscribeFromDatasetRequestRequestTypeDef = TypedDict(
    "UnsubscribeFromDatasetRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
        "DeviceId": str,
    },
)

_RequiredUpdateRecordsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRecordsRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityId": str,
        "DatasetName": str,
        "SyncSessionToken": str,
    },
)
_OptionalUpdateRecordsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRecordsRequestRequestTypeDef",
    {
        "DeviceId": str,
        "RecordPatches": List["RecordPatchTypeDef"],
        "ClientContext": str,
    },
    total=False,
)

class UpdateRecordsRequestRequestTypeDef(
    _RequiredUpdateRecordsRequestRequestTypeDef, _OptionalUpdateRecordsRequestRequestTypeDef
):
    pass

UpdateRecordsResponseTypeDef = TypedDict(
    "UpdateRecordsResponseTypeDef",
    {
        "Records": List["RecordTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
