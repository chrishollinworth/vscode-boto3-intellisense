"""
Main interface for cognito-sync service type definitions.

Usage::

    ```python
    from mypy_boto3_cognito_sync.type_defs import CognitoStreamsTypeDef

    data: CognitoStreamsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CognitoStreamsTypeDef",
    "DatasetTypeDef",
    "IdentityPoolUsageTypeDef",
    "IdentityUsageTypeDef",
    "PushSyncTypeDef",
    "RecordTypeDef",
    "BulkPublishResponseTypeDef",
    "DeleteDatasetResponseTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeIdentityPoolUsageResponseTypeDef",
    "DescribeIdentityUsageResponseTypeDef",
    "GetBulkPublishDetailsResponseTypeDef",
    "GetCognitoEventsResponseTypeDef",
    "GetIdentityPoolConfigurationResponseTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListIdentityPoolUsageResponseTypeDef",
    "ListRecordsResponseTypeDef",
    "RecordPatchTypeDef",
    "RegisterDeviceResponseTypeDef",
    "SetIdentityPoolConfigurationResponseTypeDef",
    "UpdateRecordsResponseTypeDef",
)

CognitoStreamsTypeDef = TypedDict(
    "CognitoStreamsTypeDef",
    {"StreamName": str, "RoleArn": str, "StreamingStatus": Literal["ENABLED", "DISABLED"]},
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

PushSyncTypeDef = TypedDict(
    "PushSyncTypeDef", {"ApplicationArns": List[str], "RoleArn": str}, total=False
)

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

BulkPublishResponseTypeDef = TypedDict(
    "BulkPublishResponseTypeDef", {"IdentityPoolId": str}, total=False
)

DeleteDatasetResponseTypeDef = TypedDict(
    "DeleteDatasetResponseTypeDef", {"Dataset": "DatasetTypeDef"}, total=False
)

DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef", {"Dataset": "DatasetTypeDef"}, total=False
)

DescribeIdentityPoolUsageResponseTypeDef = TypedDict(
    "DescribeIdentityPoolUsageResponseTypeDef",
    {"IdentityPoolUsage": "IdentityPoolUsageTypeDef"},
    total=False,
)

DescribeIdentityUsageResponseTypeDef = TypedDict(
    "DescribeIdentityUsageResponseTypeDef", {"IdentityUsage": "IdentityUsageTypeDef"}, total=False
)

GetBulkPublishDetailsResponseTypeDef = TypedDict(
    "GetBulkPublishDetailsResponseTypeDef",
    {
        "IdentityPoolId": str,
        "BulkPublishStartTime": datetime,
        "BulkPublishCompleteTime": datetime,
        "BulkPublishStatus": Literal["NOT_STARTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"],
        "FailureMessage": str,
    },
    total=False,
)

GetCognitoEventsResponseTypeDef = TypedDict(
    "GetCognitoEventsResponseTypeDef", {"Events": Dict[str, str]}, total=False
)

GetIdentityPoolConfigurationResponseTypeDef = TypedDict(
    "GetIdentityPoolConfigurationResponseTypeDef",
    {
        "IdentityPoolId": str,
        "PushSync": "PushSyncTypeDef",
        "CognitoStreams": "CognitoStreamsTypeDef",
    },
    total=False,
)

ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {"Datasets": List["DatasetTypeDef"], "Count": int, "NextToken": str},
    total=False,
)

ListIdentityPoolUsageResponseTypeDef = TypedDict(
    "ListIdentityPoolUsageResponseTypeDef",
    {
        "IdentityPoolUsages": List["IdentityPoolUsageTypeDef"],
        "MaxResults": int,
        "Count": int,
        "NextToken": str,
    },
    total=False,
)

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
    },
    total=False,
)

_RequiredRecordPatchTypeDef = TypedDict(
    "_RequiredRecordPatchTypeDef",
    {"Op": Literal["replace", "remove"], "Key": str, "SyncCount": int},
)
_OptionalRecordPatchTypeDef = TypedDict(
    "_OptionalRecordPatchTypeDef", {"Value": str, "DeviceLastModifiedDate": datetime}, total=False
)


class RecordPatchTypeDef(_RequiredRecordPatchTypeDef, _OptionalRecordPatchTypeDef):
    pass


RegisterDeviceResponseTypeDef = TypedDict(
    "RegisterDeviceResponseTypeDef", {"DeviceId": str}, total=False
)

SetIdentityPoolConfigurationResponseTypeDef = TypedDict(
    "SetIdentityPoolConfigurationResponseTypeDef",
    {
        "IdentityPoolId": str,
        "PushSync": "PushSyncTypeDef",
        "CognitoStreams": "CognitoStreamsTypeDef",
    },
    total=False,
)

UpdateRecordsResponseTypeDef = TypedDict(
    "UpdateRecordsResponseTypeDef", {"Records": List["RecordTypeDef"]}, total=False
)
