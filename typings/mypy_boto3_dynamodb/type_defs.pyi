"""
Type annotations for dynamodb service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/type_defs.html)

Usage::

    ```python
    from mypy_boto3_dynamodb.type_defs import ArchivalSummaryTypeDef

    data: ArchivalSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, List, Set, Union

from boto3.dynamodb.conditions import ConditionBase

from .literals import (
    AttributeActionType,
    BackupStatusType,
    BackupTypeFilterType,
    BackupTypeType,
    BatchStatementErrorCodeEnumType,
    BillingModeType,
    ComparisonOperatorType,
    ConditionalOperatorType,
    ContinuousBackupsStatusType,
    ContributorInsightsActionType,
    ContributorInsightsStatusType,
    DestinationStatusType,
    ExportFormatType,
    ExportStatusType,
    GlobalTableStatusType,
    IndexStatusType,
    KeyTypeType,
    PointInTimeRecoveryStatusType,
    ProjectionTypeType,
    ReplicaStatusType,
    ReturnConsumedCapacityType,
    ReturnItemCollectionMetricsType,
    ReturnValuesOnConditionCheckFailureType,
    ReturnValueType,
    S3SseAlgorithmType,
    ScalarAttributeTypeType,
    SelectType,
    SSEStatusType,
    SSETypeType,
    StreamViewTypeType,
    TableStatusType,
    TimeToLiveStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ArchivalSummaryTypeDef",
    "AttributeDefinitionTypeDef",
    "AttributeValueUpdateTypeDef",
    "AutoScalingPolicyDescriptionTypeDef",
    "AutoScalingPolicyUpdateTypeDef",
    "AutoScalingSettingsDescriptionTypeDef",
    "AutoScalingSettingsUpdateTypeDef",
    "AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef",
    "AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef",
    "BackupDescriptionTypeDef",
    "BackupDetailsTypeDef",
    "BackupSummaryTypeDef",
    "BatchExecuteStatementInputRequestTypeDef",
    "BatchExecuteStatementOutputTypeDef",
    "BatchGetItemInputRequestTypeDef",
    "BatchGetItemInputServiceResourceTypeDef",
    "BatchGetItemOutputTypeDef",
    "BatchStatementErrorTypeDef",
    "BatchStatementRequestTypeDef",
    "BatchStatementResponseTypeDef",
    "BatchWriteItemInputRequestTypeDef",
    "BatchWriteItemInputServiceResourceTypeDef",
    "BatchWriteItemOutputTypeDef",
    "BillingModeSummaryTypeDef",
    "CapacityTypeDef",
    "ConditionCheckTypeDef",
    "ConditionTypeDef",
    "ConsumedCapacityTypeDef",
    "ContinuousBackupsDescriptionTypeDef",
    "ContributorInsightsSummaryTypeDef",
    "CreateBackupInputRequestTypeDef",
    "CreateBackupOutputTypeDef",
    "CreateGlobalSecondaryIndexActionTypeDef",
    "CreateGlobalTableInputRequestTypeDef",
    "CreateGlobalTableOutputTypeDef",
    "CreateReplicaActionTypeDef",
    "CreateReplicationGroupMemberActionTypeDef",
    "CreateTableInputRequestTypeDef",
    "CreateTableInputServiceResourceTypeDef",
    "CreateTableOutputTypeDef",
    "DeleteBackupInputRequestTypeDef",
    "DeleteBackupOutputTypeDef",
    "DeleteGlobalSecondaryIndexActionTypeDef",
    "DeleteItemInputRequestTypeDef",
    "DeleteItemInputTableTypeDef",
    "DeleteItemOutputTypeDef",
    "DeleteReplicaActionTypeDef",
    "DeleteReplicationGroupMemberActionTypeDef",
    "DeleteRequestTypeDef",
    "DeleteTableInputRequestTypeDef",
    "DeleteTableOutputTypeDef",
    "DeleteTypeDef",
    "DescribeBackupInputRequestTypeDef",
    "DescribeBackupOutputTypeDef",
    "DescribeContinuousBackupsInputRequestTypeDef",
    "DescribeContinuousBackupsOutputTypeDef",
    "DescribeContributorInsightsInputRequestTypeDef",
    "DescribeContributorInsightsOutputTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "DescribeExportInputRequestTypeDef",
    "DescribeExportOutputTypeDef",
    "DescribeGlobalTableInputRequestTypeDef",
    "DescribeGlobalTableOutputTypeDef",
    "DescribeGlobalTableSettingsInputRequestTypeDef",
    "DescribeGlobalTableSettingsOutputTypeDef",
    "DescribeKinesisStreamingDestinationInputRequestTypeDef",
    "DescribeKinesisStreamingDestinationOutputTypeDef",
    "DescribeLimitsOutputTypeDef",
    "DescribeTableInputRequestTypeDef",
    "DescribeTableOutputTypeDef",
    "DescribeTableReplicaAutoScalingInputRequestTypeDef",
    "DescribeTableReplicaAutoScalingOutputTypeDef",
    "DescribeTimeToLiveInputRequestTypeDef",
    "DescribeTimeToLiveOutputTypeDef",
    "EndpointTypeDef",
    "ExecuteStatementInputRequestTypeDef",
    "ExecuteStatementOutputTypeDef",
    "ExecuteTransactionInputRequestTypeDef",
    "ExecuteTransactionOutputTypeDef",
    "ExpectedAttributeValueTypeDef",
    "ExportDescriptionTypeDef",
    "ExportSummaryTypeDef",
    "ExportTableToPointInTimeInputRequestTypeDef",
    "ExportTableToPointInTimeOutputTypeDef",
    "FailureExceptionTypeDef",
    "GetItemInputRequestTypeDef",
    "GetItemInputTableTypeDef",
    "GetItemOutputTypeDef",
    "GetTypeDef",
    "GlobalSecondaryIndexAutoScalingUpdateTypeDef",
    "GlobalSecondaryIndexDescriptionTypeDef",
    "GlobalSecondaryIndexInfoTypeDef",
    "GlobalSecondaryIndexTypeDef",
    "GlobalSecondaryIndexUpdateTypeDef",
    "GlobalTableDescriptionTypeDef",
    "GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef",
    "GlobalTableTypeDef",
    "ItemCollectionMetricsTypeDef",
    "ItemResponseTypeDef",
    "KeySchemaElementTypeDef",
    "KeysAndAttributesTypeDef",
    "KinesisDataStreamDestinationTypeDef",
    "KinesisStreamingDestinationInputRequestTypeDef",
    "KinesisStreamingDestinationOutputTypeDef",
    "ListBackupsInputRequestTypeDef",
    "ListBackupsOutputTypeDef",
    "ListContributorInsightsInputRequestTypeDef",
    "ListContributorInsightsOutputTypeDef",
    "ListExportsInputRequestTypeDef",
    "ListExportsOutputTypeDef",
    "ListGlobalTablesInputRequestTypeDef",
    "ListGlobalTablesOutputTypeDef",
    "ListTablesInputRequestTypeDef",
    "ListTablesOutputTypeDef",
    "ListTagsOfResourceInputRequestTypeDef",
    "ListTagsOfResourceOutputTypeDef",
    "LocalSecondaryIndexDescriptionTypeDef",
    "LocalSecondaryIndexInfoTypeDef",
    "LocalSecondaryIndexTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterizedStatementTypeDef",
    "PointInTimeRecoveryDescriptionTypeDef",
    "PointInTimeRecoverySpecificationTypeDef",
    "ProjectionTypeDef",
    "ProvisionedThroughputDescriptionTypeDef",
    "ProvisionedThroughputOverrideTypeDef",
    "ProvisionedThroughputTypeDef",
    "PutItemInputRequestTypeDef",
    "PutItemInputTableTypeDef",
    "PutItemOutputTypeDef",
    "PutRequestTypeDef",
    "PutTypeDef",
    "QueryInputRequestTypeDef",
    "QueryInputTableTypeDef",
    "QueryOutputTypeDef",
    "ReplicaAutoScalingDescriptionTypeDef",
    "ReplicaAutoScalingUpdateTypeDef",
    "ReplicaDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef",
    "ReplicaGlobalSecondaryIndexDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef",
    "ReplicaGlobalSecondaryIndexTypeDef",
    "ReplicaSettingsDescriptionTypeDef",
    "ReplicaSettingsUpdateTypeDef",
    "ReplicaTypeDef",
    "ReplicaUpdateTypeDef",
    "ReplicationGroupUpdateTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreSummaryTypeDef",
    "RestoreTableFromBackupInputRequestTypeDef",
    "RestoreTableFromBackupOutputTypeDef",
    "RestoreTableToPointInTimeInputRequestTypeDef",
    "RestoreTableToPointInTimeOutputTypeDef",
    "SSEDescriptionTypeDef",
    "SSESpecificationTypeDef",
    "ScanInputRequestTypeDef",
    "ScanInputTableTypeDef",
    "ScanOutputTypeDef",
    "ServiceResourceTableRequestTypeDef",
    "SourceTableDetailsTypeDef",
    "SourceTableFeatureDetailsTypeDef",
    "StreamSpecificationTypeDef",
    "TableAutoScalingDescriptionTypeDef",
    "TableBatchWriterRequestTypeDef",
    "TableDescriptionTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagTypeDef",
    "TimeToLiveDescriptionTypeDef",
    "TimeToLiveSpecificationTypeDef",
    "TransactGetItemTypeDef",
    "TransactGetItemsInputRequestTypeDef",
    "TransactGetItemsOutputTypeDef",
    "TransactWriteItemTypeDef",
    "TransactWriteItemsInputRequestTypeDef",
    "TransactWriteItemsOutputTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateContinuousBackupsInputRequestTypeDef",
    "UpdateContinuousBackupsOutputTypeDef",
    "UpdateContributorInsightsInputRequestTypeDef",
    "UpdateContributorInsightsOutputTypeDef",
    "UpdateGlobalSecondaryIndexActionTypeDef",
    "UpdateGlobalTableInputRequestTypeDef",
    "UpdateGlobalTableOutputTypeDef",
    "UpdateGlobalTableSettingsInputRequestTypeDef",
    "UpdateGlobalTableSettingsOutputTypeDef",
    "UpdateItemInputRequestTypeDef",
    "UpdateItemInputTableTypeDef",
    "UpdateItemOutputTypeDef",
    "UpdateReplicationGroupMemberActionTypeDef",
    "UpdateTableInputRequestTypeDef",
    "UpdateTableInputTableTypeDef",
    "UpdateTableOutputTypeDef",
    "UpdateTableReplicaAutoScalingInputRequestTypeDef",
    "UpdateTableReplicaAutoScalingOutputTypeDef",
    "UpdateTimeToLiveInputRequestTypeDef",
    "UpdateTimeToLiveOutputTypeDef",
    "UpdateTypeDef",
    "WaiterConfigTypeDef",
    "WriteRequestTypeDef",
)

ArchivalSummaryTypeDef = TypedDict(
    "ArchivalSummaryTypeDef",
    {
        "ArchivalDateTime": datetime,
        "ArchivalReason": str,
        "ArchivalBackupArn": str,
    },
    total=False,
)

AttributeDefinitionTypeDef = TypedDict(
    "AttributeDefinitionTypeDef",
    {
        "AttributeName": str,
        "AttributeType": ScalarAttributeTypeType,
    },
)

AttributeValueUpdateTypeDef = TypedDict(
    "AttributeValueUpdateTypeDef",
    {
        "Value": Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
        "Action": AttributeActionType,
    },
    total=False,
)

AutoScalingPolicyDescriptionTypeDef = TypedDict(
    "AutoScalingPolicyDescriptionTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": "AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef",
    },
    total=False,
)

_RequiredAutoScalingPolicyUpdateTypeDef = TypedDict(
    "_RequiredAutoScalingPolicyUpdateTypeDef",
    {
        "TargetTrackingScalingPolicyConfiguration": "AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef",
    },
)
_OptionalAutoScalingPolicyUpdateTypeDef = TypedDict(
    "_OptionalAutoScalingPolicyUpdateTypeDef",
    {
        "PolicyName": str,
    },
    total=False,
)

class AutoScalingPolicyUpdateTypeDef(
    _RequiredAutoScalingPolicyUpdateTypeDef, _OptionalAutoScalingPolicyUpdateTypeDef
):
    pass

AutoScalingSettingsDescriptionTypeDef = TypedDict(
    "AutoScalingSettingsDescriptionTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicies": List["AutoScalingPolicyDescriptionTypeDef"],
    },
    total=False,
)

AutoScalingSettingsUpdateTypeDef = TypedDict(
    "AutoScalingSettingsUpdateTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicyUpdate": "AutoScalingPolicyUpdateTypeDef",
    },
    total=False,
)

_RequiredAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef = TypedDict(
    "_RequiredAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef",
    {
        "TargetValue": float,
    },
)
_OptionalAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef = TypedDict(
    "_OptionalAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef",
    {
        "DisableScaleIn": bool,
        "ScaleInCooldown": int,
        "ScaleOutCooldown": int,
    },
    total=False,
)

class AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef(
    _RequiredAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef,
    _OptionalAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef,
):
    pass

_RequiredAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef = TypedDict(
    "_RequiredAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef",
    {
        "TargetValue": float,
    },
)
_OptionalAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef = TypedDict(
    "_OptionalAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef",
    {
        "DisableScaleIn": bool,
        "ScaleInCooldown": int,
        "ScaleOutCooldown": int,
    },
    total=False,
)

class AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef(
    _RequiredAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef,
    _OptionalAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef,
):
    pass

BackupDescriptionTypeDef = TypedDict(
    "BackupDescriptionTypeDef",
    {
        "BackupDetails": "BackupDetailsTypeDef",
        "SourceTableDetails": "SourceTableDetailsTypeDef",
        "SourceTableFeatureDetails": "SourceTableFeatureDetailsTypeDef",
    },
    total=False,
)

_RequiredBackupDetailsTypeDef = TypedDict(
    "_RequiredBackupDetailsTypeDef",
    {
        "BackupArn": str,
        "BackupName": str,
        "BackupStatus": BackupStatusType,
        "BackupType": BackupTypeType,
        "BackupCreationDateTime": datetime,
    },
)
_OptionalBackupDetailsTypeDef = TypedDict(
    "_OptionalBackupDetailsTypeDef",
    {
        "BackupSizeBytes": int,
        "BackupExpiryDateTime": datetime,
    },
    total=False,
)

class BackupDetailsTypeDef(_RequiredBackupDetailsTypeDef, _OptionalBackupDetailsTypeDef):
    pass

BackupSummaryTypeDef = TypedDict(
    "BackupSummaryTypeDef",
    {
        "TableName": str,
        "TableId": str,
        "TableArn": str,
        "BackupArn": str,
        "BackupName": str,
        "BackupCreationDateTime": datetime,
        "BackupExpiryDateTime": datetime,
        "BackupStatus": BackupStatusType,
        "BackupType": BackupTypeType,
        "BackupSizeBytes": int,
    },
    total=False,
)

BatchExecuteStatementInputRequestTypeDef = TypedDict(
    "BatchExecuteStatementInputRequestTypeDef",
    {
        "Statements": List["BatchStatementRequestTypeDef"],
    },
)

BatchExecuteStatementOutputTypeDef = TypedDict(
    "BatchExecuteStatementOutputTypeDef",
    {
        "Responses": List["BatchStatementResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchGetItemInputRequestTypeDef = TypedDict(
    "_RequiredBatchGetItemInputRequestTypeDef",
    {
        "RequestItems": Dict[str, "KeysAndAttributesTypeDef"],
    },
)
_OptionalBatchGetItemInputRequestTypeDef = TypedDict(
    "_OptionalBatchGetItemInputRequestTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
    },
    total=False,
)

class BatchGetItemInputRequestTypeDef(
    _RequiredBatchGetItemInputRequestTypeDef, _OptionalBatchGetItemInputRequestTypeDef
):
    pass

_RequiredBatchGetItemInputServiceResourceTypeDef = TypedDict(
    "_RequiredBatchGetItemInputServiceResourceTypeDef",
    {
        "RequestItems": Dict[str, "KeysAndAttributesTypeDef"],
    },
)
_OptionalBatchGetItemInputServiceResourceTypeDef = TypedDict(
    "_OptionalBatchGetItemInputServiceResourceTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
    },
    total=False,
)

class BatchGetItemInputServiceResourceTypeDef(
    _RequiredBatchGetItemInputServiceResourceTypeDef,
    _OptionalBatchGetItemInputServiceResourceTypeDef,
):
    pass

BatchGetItemOutputTypeDef = TypedDict(
    "BatchGetItemOutputTypeDef",
    {
        "Responses": Dict[
            str,
            List[
                Dict[
                    str,
                    Union[
                        bytes,
                        bytearray,
                        str,
                        int,
                        Decimal,
                        bool,
                        Set[int],
                        Set[Decimal],
                        Set[str],
                        Set[bytes],
                        Set[bytearray],
                        List[Any],
                        Dict[str, Any],
                        None,
                    ],
                ]
            ],
        ],
        "UnprocessedKeys": Dict[str, "KeysAndAttributesTypeDef"],
        "ConsumedCapacity": List["ConsumedCapacityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchStatementErrorTypeDef = TypedDict(
    "BatchStatementErrorTypeDef",
    {
        "Code": BatchStatementErrorCodeEnumType,
        "Message": str,
    },
    total=False,
)

_RequiredBatchStatementRequestTypeDef = TypedDict(
    "_RequiredBatchStatementRequestTypeDef",
    {
        "Statement": str,
    },
)
_OptionalBatchStatementRequestTypeDef = TypedDict(
    "_OptionalBatchStatementRequestTypeDef",
    {
        "Parameters": List[
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ]
        ],
        "ConsistentRead": bool,
    },
    total=False,
)

class BatchStatementRequestTypeDef(
    _RequiredBatchStatementRequestTypeDef, _OptionalBatchStatementRequestTypeDef
):
    pass

BatchStatementResponseTypeDef = TypedDict(
    "BatchStatementResponseTypeDef",
    {
        "Error": "BatchStatementErrorTypeDef",
        "TableName": str,
        "Item": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
    total=False,
)

_RequiredBatchWriteItemInputRequestTypeDef = TypedDict(
    "_RequiredBatchWriteItemInputRequestTypeDef",
    {
        "RequestItems": Dict[str, List["WriteRequestTypeDef"]],
    },
)
_OptionalBatchWriteItemInputRequestTypeDef = TypedDict(
    "_OptionalBatchWriteItemInputRequestTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
    },
    total=False,
)

class BatchWriteItemInputRequestTypeDef(
    _RequiredBatchWriteItemInputRequestTypeDef, _OptionalBatchWriteItemInputRequestTypeDef
):
    pass

_RequiredBatchWriteItemInputServiceResourceTypeDef = TypedDict(
    "_RequiredBatchWriteItemInputServiceResourceTypeDef",
    {
        "RequestItems": Dict[str, List["WriteRequestTypeDef"]],
    },
)
_OptionalBatchWriteItemInputServiceResourceTypeDef = TypedDict(
    "_OptionalBatchWriteItemInputServiceResourceTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
    },
    total=False,
)

class BatchWriteItemInputServiceResourceTypeDef(
    _RequiredBatchWriteItemInputServiceResourceTypeDef,
    _OptionalBatchWriteItemInputServiceResourceTypeDef,
):
    pass

BatchWriteItemOutputTypeDef = TypedDict(
    "BatchWriteItemOutputTypeDef",
    {
        "UnprocessedItems": Dict[str, List["WriteRequestTypeDef"]],
        "ItemCollectionMetrics": Dict[str, List["ItemCollectionMetricsTypeDef"]],
        "ConsumedCapacity": List["ConsumedCapacityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BillingModeSummaryTypeDef = TypedDict(
    "BillingModeSummaryTypeDef",
    {
        "BillingMode": BillingModeType,
        "LastUpdateToPayPerRequestDateTime": datetime,
    },
    total=False,
)

CapacityTypeDef = TypedDict(
    "CapacityTypeDef",
    {
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "CapacityUnits": float,
    },
    total=False,
)

_RequiredConditionCheckTypeDef = TypedDict(
    "_RequiredConditionCheckTypeDef",
    {
        "Key": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "TableName": str,
        "ConditionExpression": str,
    },
)
_OptionalConditionCheckTypeDef = TypedDict(
    "_OptionalConditionCheckTypeDef",
    {
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)

class ConditionCheckTypeDef(_RequiredConditionCheckTypeDef, _OptionalConditionCheckTypeDef):
    pass

_RequiredConditionTypeDef = TypedDict(
    "_RequiredConditionTypeDef",
    {
        "ComparisonOperator": ComparisonOperatorType,
    },
)
_OptionalConditionTypeDef = TypedDict(
    "_OptionalConditionTypeDef",
    {
        "AttributeValueList": List[
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ]
        ],
    },
    total=False,
)

class ConditionTypeDef(_RequiredConditionTypeDef, _OptionalConditionTypeDef):
    pass

ConsumedCapacityTypeDef = TypedDict(
    "ConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": "CapacityTypeDef",
        "LocalSecondaryIndexes": Dict[str, "CapacityTypeDef"],
        "GlobalSecondaryIndexes": Dict[str, "CapacityTypeDef"],
    },
    total=False,
)

_RequiredContinuousBackupsDescriptionTypeDef = TypedDict(
    "_RequiredContinuousBackupsDescriptionTypeDef",
    {
        "ContinuousBackupsStatus": ContinuousBackupsStatusType,
    },
)
_OptionalContinuousBackupsDescriptionTypeDef = TypedDict(
    "_OptionalContinuousBackupsDescriptionTypeDef",
    {
        "PointInTimeRecoveryDescription": "PointInTimeRecoveryDescriptionTypeDef",
    },
    total=False,
)

class ContinuousBackupsDescriptionTypeDef(
    _RequiredContinuousBackupsDescriptionTypeDef, _OptionalContinuousBackupsDescriptionTypeDef
):
    pass

ContributorInsightsSummaryTypeDef = TypedDict(
    "ContributorInsightsSummaryTypeDef",
    {
        "TableName": str,
        "IndexName": str,
        "ContributorInsightsStatus": ContributorInsightsStatusType,
    },
    total=False,
)

CreateBackupInputRequestTypeDef = TypedDict(
    "CreateBackupInputRequestTypeDef",
    {
        "TableName": str,
        "BackupName": str,
    },
)

CreateBackupOutputTypeDef = TypedDict(
    "CreateBackupOutputTypeDef",
    {
        "BackupDetails": "BackupDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGlobalSecondaryIndexActionTypeDef = TypedDict(
    "_RequiredCreateGlobalSecondaryIndexActionTypeDef",
    {
        "IndexName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
    },
)
_OptionalCreateGlobalSecondaryIndexActionTypeDef = TypedDict(
    "_OptionalCreateGlobalSecondaryIndexActionTypeDef",
    {
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
    },
    total=False,
)

class CreateGlobalSecondaryIndexActionTypeDef(
    _RequiredCreateGlobalSecondaryIndexActionTypeDef,
    _OptionalCreateGlobalSecondaryIndexActionTypeDef,
):
    pass

CreateGlobalTableInputRequestTypeDef = TypedDict(
    "CreateGlobalTableInputRequestTypeDef",
    {
        "GlobalTableName": str,
        "ReplicationGroup": List["ReplicaTypeDef"],
    },
)

CreateGlobalTableOutputTypeDef = TypedDict(
    "CreateGlobalTableOutputTypeDef",
    {
        "GlobalTableDescription": "GlobalTableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateReplicaActionTypeDef = TypedDict(
    "CreateReplicaActionTypeDef",
    {
        "RegionName": str,
    },
)

_RequiredCreateReplicationGroupMemberActionTypeDef = TypedDict(
    "_RequiredCreateReplicationGroupMemberActionTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalCreateReplicationGroupMemberActionTypeDef = TypedDict(
    "_OptionalCreateReplicationGroupMemberActionTypeDef",
    {
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": "ProvisionedThroughputOverrideTypeDef",
        "GlobalSecondaryIndexes": List["ReplicaGlobalSecondaryIndexTypeDef"],
    },
    total=False,
)

class CreateReplicationGroupMemberActionTypeDef(
    _RequiredCreateReplicationGroupMemberActionTypeDef,
    _OptionalCreateReplicationGroupMemberActionTypeDef,
):
    pass

_RequiredCreateTableInputRequestTypeDef = TypedDict(
    "_RequiredCreateTableInputRequestTypeDef",
    {
        "AttributeDefinitions": List["AttributeDefinitionTypeDef"],
        "TableName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
    },
)
_OptionalCreateTableInputRequestTypeDef = TypedDict(
    "_OptionalCreateTableInputRequestTypeDef",
    {
        "LocalSecondaryIndexes": List["LocalSecondaryIndexTypeDef"],
        "GlobalSecondaryIndexes": List["GlobalSecondaryIndexTypeDef"],
        "BillingMode": BillingModeType,
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
        "StreamSpecification": "StreamSpecificationTypeDef",
        "SSESpecification": "SSESpecificationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateTableInputRequestTypeDef(
    _RequiredCreateTableInputRequestTypeDef, _OptionalCreateTableInputRequestTypeDef
):
    pass

_RequiredCreateTableInputServiceResourceTypeDef = TypedDict(
    "_RequiredCreateTableInputServiceResourceTypeDef",
    {
        "AttributeDefinitions": List["AttributeDefinitionTypeDef"],
        "TableName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
    },
)
_OptionalCreateTableInputServiceResourceTypeDef = TypedDict(
    "_OptionalCreateTableInputServiceResourceTypeDef",
    {
        "LocalSecondaryIndexes": List["LocalSecondaryIndexTypeDef"],
        "GlobalSecondaryIndexes": List["GlobalSecondaryIndexTypeDef"],
        "BillingMode": BillingModeType,
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
        "StreamSpecification": "StreamSpecificationTypeDef",
        "SSESpecification": "SSESpecificationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateTableInputServiceResourceTypeDef(
    _RequiredCreateTableInputServiceResourceTypeDef, _OptionalCreateTableInputServiceResourceTypeDef
):
    pass

CreateTableOutputTypeDef = TypedDict(
    "CreateTableOutputTypeDef",
    {
        "TableDescription": "TableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackupInputRequestTypeDef = TypedDict(
    "DeleteBackupInputRequestTypeDef",
    {
        "BackupArn": str,
    },
)

DeleteBackupOutputTypeDef = TypedDict(
    "DeleteBackupOutputTypeDef",
    {
        "BackupDescription": "BackupDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGlobalSecondaryIndexActionTypeDef = TypedDict(
    "DeleteGlobalSecondaryIndexActionTypeDef",
    {
        "IndexName": str,
    },
)

_RequiredDeleteItemInputRequestTypeDef = TypedDict(
    "_RequiredDeleteItemInputRequestTypeDef",
    {
        "TableName": str,
        "Key": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
)
_OptionalDeleteItemInputRequestTypeDef = TypedDict(
    "_OptionalDeleteItemInputRequestTypeDef",
    {
        "Expected": Dict[str, "ExpectedAttributeValueTypeDef"],
        "ConditionalOperator": ConditionalOperatorType,
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
    total=False,
)

class DeleteItemInputRequestTypeDef(
    _RequiredDeleteItemInputRequestTypeDef, _OptionalDeleteItemInputRequestTypeDef
):
    pass

_RequiredDeleteItemInputTableTypeDef = TypedDict(
    "_RequiredDeleteItemInputTableTypeDef",
    {
        "Key": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
)
_OptionalDeleteItemInputTableTypeDef = TypedDict(
    "_OptionalDeleteItemInputTableTypeDef",
    {
        "Expected": Dict[str, "ExpectedAttributeValueTypeDef"],
        "ConditionalOperator": ConditionalOperatorType,
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
    total=False,
)

class DeleteItemInputTableTypeDef(
    _RequiredDeleteItemInputTableTypeDef, _OptionalDeleteItemInputTableTypeDef
):
    pass

DeleteItemOutputTypeDef = TypedDict(
    "DeleteItemOutputTypeDef",
    {
        "Attributes": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ItemCollectionMetrics": "ItemCollectionMetricsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteReplicaActionTypeDef = TypedDict(
    "DeleteReplicaActionTypeDef",
    {
        "RegionName": str,
    },
)

DeleteReplicationGroupMemberActionTypeDef = TypedDict(
    "DeleteReplicationGroupMemberActionTypeDef",
    {
        "RegionName": str,
    },
)

DeleteRequestTypeDef = TypedDict(
    "DeleteRequestTypeDef",
    {
        "Key": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
)

DeleteTableInputRequestTypeDef = TypedDict(
    "DeleteTableInputRequestTypeDef",
    {
        "TableName": str,
    },
)

DeleteTableOutputTypeDef = TypedDict(
    "DeleteTableOutputTypeDef",
    {
        "TableDescription": "TableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTypeDef = TypedDict(
    "_RequiredDeleteTypeDef",
    {
        "Key": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "TableName": str,
    },
)
_OptionalDeleteTypeDef = TypedDict(
    "_OptionalDeleteTypeDef",
    {
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)

class DeleteTypeDef(_RequiredDeleteTypeDef, _OptionalDeleteTypeDef):
    pass

DescribeBackupInputRequestTypeDef = TypedDict(
    "DescribeBackupInputRequestTypeDef",
    {
        "BackupArn": str,
    },
)

DescribeBackupOutputTypeDef = TypedDict(
    "DescribeBackupOutputTypeDef",
    {
        "BackupDescription": "BackupDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContinuousBackupsInputRequestTypeDef = TypedDict(
    "DescribeContinuousBackupsInputRequestTypeDef",
    {
        "TableName": str,
    },
)

DescribeContinuousBackupsOutputTypeDef = TypedDict(
    "DescribeContinuousBackupsOutputTypeDef",
    {
        "ContinuousBackupsDescription": "ContinuousBackupsDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeContributorInsightsInputRequestTypeDef = TypedDict(
    "_RequiredDescribeContributorInsightsInputRequestTypeDef",
    {
        "TableName": str,
    },
)
_OptionalDescribeContributorInsightsInputRequestTypeDef = TypedDict(
    "_OptionalDescribeContributorInsightsInputRequestTypeDef",
    {
        "IndexName": str,
    },
    total=False,
)

class DescribeContributorInsightsInputRequestTypeDef(
    _RequiredDescribeContributorInsightsInputRequestTypeDef,
    _OptionalDescribeContributorInsightsInputRequestTypeDef,
):
    pass

DescribeContributorInsightsOutputTypeDef = TypedDict(
    "DescribeContributorInsightsOutputTypeDef",
    {
        "TableName": str,
        "IndexName": str,
        "ContributorInsightsRuleList": List[str],
        "ContributorInsightsStatus": ContributorInsightsStatusType,
        "LastUpdateDateTime": datetime,
        "FailureException": "FailureExceptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointsResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseTypeDef",
    {
        "Endpoints": List["EndpointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportInputRequestTypeDef = TypedDict(
    "DescribeExportInputRequestTypeDef",
    {
        "ExportArn": str,
    },
)

DescribeExportOutputTypeDef = TypedDict(
    "DescribeExportOutputTypeDef",
    {
        "ExportDescription": "ExportDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGlobalTableInputRequestTypeDef = TypedDict(
    "DescribeGlobalTableInputRequestTypeDef",
    {
        "GlobalTableName": str,
    },
)

DescribeGlobalTableOutputTypeDef = TypedDict(
    "DescribeGlobalTableOutputTypeDef",
    {
        "GlobalTableDescription": "GlobalTableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGlobalTableSettingsInputRequestTypeDef = TypedDict(
    "DescribeGlobalTableSettingsInputRequestTypeDef",
    {
        "GlobalTableName": str,
    },
)

DescribeGlobalTableSettingsOutputTypeDef = TypedDict(
    "DescribeGlobalTableSettingsOutputTypeDef",
    {
        "GlobalTableName": str,
        "ReplicaSettings": List["ReplicaSettingsDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeKinesisStreamingDestinationInputRequestTypeDef = TypedDict(
    "DescribeKinesisStreamingDestinationInputRequestTypeDef",
    {
        "TableName": str,
    },
)

DescribeKinesisStreamingDestinationOutputTypeDef = TypedDict(
    "DescribeKinesisStreamingDestinationOutputTypeDef",
    {
        "TableName": str,
        "KinesisDataStreamDestinations": List["KinesisDataStreamDestinationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLimitsOutputTypeDef = TypedDict(
    "DescribeLimitsOutputTypeDef",
    {
        "AccountMaxReadCapacityUnits": int,
        "AccountMaxWriteCapacityUnits": int,
        "TableMaxReadCapacityUnits": int,
        "TableMaxWriteCapacityUnits": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTableInputRequestTypeDef = TypedDict(
    "DescribeTableInputRequestTypeDef",
    {
        "TableName": str,
    },
)

DescribeTableOutputTypeDef = TypedDict(
    "DescribeTableOutputTypeDef",
    {
        "Table": "TableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTableReplicaAutoScalingInputRequestTypeDef = TypedDict(
    "DescribeTableReplicaAutoScalingInputRequestTypeDef",
    {
        "TableName": str,
    },
)

DescribeTableReplicaAutoScalingOutputTypeDef = TypedDict(
    "DescribeTableReplicaAutoScalingOutputTypeDef",
    {
        "TableAutoScalingDescription": "TableAutoScalingDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTimeToLiveInputRequestTypeDef = TypedDict(
    "DescribeTimeToLiveInputRequestTypeDef",
    {
        "TableName": str,
    },
)

DescribeTimeToLiveOutputTypeDef = TypedDict(
    "DescribeTimeToLiveOutputTypeDef",
    {
        "TimeToLiveDescription": "TimeToLiveDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "CachePeriodInMinutes": int,
    },
)

_RequiredExecuteStatementInputRequestTypeDef = TypedDict(
    "_RequiredExecuteStatementInputRequestTypeDef",
    {
        "Statement": str,
    },
)
_OptionalExecuteStatementInputRequestTypeDef = TypedDict(
    "_OptionalExecuteStatementInputRequestTypeDef",
    {
        "Parameters": List[
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ]
        ],
        "ConsistentRead": bool,
        "NextToken": str,
    },
    total=False,
)

class ExecuteStatementInputRequestTypeDef(
    _RequiredExecuteStatementInputRequestTypeDef, _OptionalExecuteStatementInputRequestTypeDef
):
    pass

ExecuteStatementOutputTypeDef = TypedDict(
    "ExecuteStatementOutputTypeDef",
    {
        "Items": List[
            Dict[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    List[Any],
                    Dict[str, Any],
                    None,
                ],
            ]
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExecuteTransactionInputRequestTypeDef = TypedDict(
    "_RequiredExecuteTransactionInputRequestTypeDef",
    {
        "TransactStatements": List["ParameterizedStatementTypeDef"],
    },
)
_OptionalExecuteTransactionInputRequestTypeDef = TypedDict(
    "_OptionalExecuteTransactionInputRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class ExecuteTransactionInputRequestTypeDef(
    _RequiredExecuteTransactionInputRequestTypeDef, _OptionalExecuteTransactionInputRequestTypeDef
):
    pass

ExecuteTransactionOutputTypeDef = TypedDict(
    "ExecuteTransactionOutputTypeDef",
    {
        "Responses": List["ItemResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExpectedAttributeValueTypeDef = TypedDict(
    "ExpectedAttributeValueTypeDef",
    {
        "Value": Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
        "Exists": bool,
        "ComparisonOperator": ComparisonOperatorType,
        "AttributeValueList": List[
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ]
        ],
    },
    total=False,
)

ExportDescriptionTypeDef = TypedDict(
    "ExportDescriptionTypeDef",
    {
        "ExportArn": str,
        "ExportStatus": ExportStatusType,
        "StartTime": datetime,
        "EndTime": datetime,
        "ExportManifest": str,
        "TableArn": str,
        "TableId": str,
        "ExportTime": datetime,
        "ClientToken": str,
        "S3Bucket": str,
        "S3BucketOwner": str,
        "S3Prefix": str,
        "S3SseAlgorithm": S3SseAlgorithmType,
        "S3SseKmsKeyId": str,
        "FailureCode": str,
        "FailureMessage": str,
        "ExportFormat": ExportFormatType,
        "BilledSizeBytes": int,
        "ItemCount": int,
    },
    total=False,
)

ExportSummaryTypeDef = TypedDict(
    "ExportSummaryTypeDef",
    {
        "ExportArn": str,
        "ExportStatus": ExportStatusType,
    },
    total=False,
)

_RequiredExportTableToPointInTimeInputRequestTypeDef = TypedDict(
    "_RequiredExportTableToPointInTimeInputRequestTypeDef",
    {
        "TableArn": str,
        "S3Bucket": str,
    },
)
_OptionalExportTableToPointInTimeInputRequestTypeDef = TypedDict(
    "_OptionalExportTableToPointInTimeInputRequestTypeDef",
    {
        "ExportTime": Union[datetime, str],
        "ClientToken": str,
        "S3BucketOwner": str,
        "S3Prefix": str,
        "S3SseAlgorithm": S3SseAlgorithmType,
        "S3SseKmsKeyId": str,
        "ExportFormat": ExportFormatType,
    },
    total=False,
)

class ExportTableToPointInTimeInputRequestTypeDef(
    _RequiredExportTableToPointInTimeInputRequestTypeDef,
    _OptionalExportTableToPointInTimeInputRequestTypeDef,
):
    pass

ExportTableToPointInTimeOutputTypeDef = TypedDict(
    "ExportTableToPointInTimeOutputTypeDef",
    {
        "ExportDescription": "ExportDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailureExceptionTypeDef = TypedDict(
    "FailureExceptionTypeDef",
    {
        "ExceptionName": str,
        "ExceptionDescription": str,
    },
    total=False,
)

_RequiredGetItemInputRequestTypeDef = TypedDict(
    "_RequiredGetItemInputRequestTypeDef",
    {
        "TableName": str,
        "Key": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
)
_OptionalGetItemInputRequestTypeDef = TypedDict(
    "_OptionalGetItemInputRequestTypeDef",
    {
        "AttributesToGet": List[str],
        "ConsistentRead": bool,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
    },
    total=False,
)

class GetItemInputRequestTypeDef(
    _RequiredGetItemInputRequestTypeDef, _OptionalGetItemInputRequestTypeDef
):
    pass

_RequiredGetItemInputTableTypeDef = TypedDict(
    "_RequiredGetItemInputTableTypeDef",
    {
        "Key": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
)
_OptionalGetItemInputTableTypeDef = TypedDict(
    "_OptionalGetItemInputTableTypeDef",
    {
        "AttributesToGet": List[str],
        "ConsistentRead": bool,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
    },
    total=False,
)

class GetItemInputTableTypeDef(
    _RequiredGetItemInputTableTypeDef, _OptionalGetItemInputTableTypeDef
):
    pass

GetItemOutputTypeDef = TypedDict(
    "GetItemOutputTypeDef",
    {
        "Item": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTypeDef = TypedDict(
    "_RequiredGetTypeDef",
    {
        "Key": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "TableName": str,
    },
)
_OptionalGetTypeDef = TypedDict(
    "_OptionalGetTypeDef",
    {
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
    },
    total=False,
)

class GetTypeDef(_RequiredGetTypeDef, _OptionalGetTypeDef):
    pass

GlobalSecondaryIndexAutoScalingUpdateTypeDef = TypedDict(
    "GlobalSecondaryIndexAutoScalingUpdateTypeDef",
    {
        "IndexName": str,
        "ProvisionedWriteCapacityAutoScalingUpdate": "AutoScalingSettingsUpdateTypeDef",
    },
    total=False,
)

GlobalSecondaryIndexDescriptionTypeDef = TypedDict(
    "GlobalSecondaryIndexDescriptionTypeDef",
    {
        "IndexName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
        "IndexStatus": IndexStatusType,
        "Backfilling": bool,
        "ProvisionedThroughput": "ProvisionedThroughputDescriptionTypeDef",
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

GlobalSecondaryIndexInfoTypeDef = TypedDict(
    "GlobalSecondaryIndexInfoTypeDef",
    {
        "IndexName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
    },
    total=False,
)

_RequiredGlobalSecondaryIndexTypeDef = TypedDict(
    "_RequiredGlobalSecondaryIndexTypeDef",
    {
        "IndexName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
    },
)
_OptionalGlobalSecondaryIndexTypeDef = TypedDict(
    "_OptionalGlobalSecondaryIndexTypeDef",
    {
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
    },
    total=False,
)

class GlobalSecondaryIndexTypeDef(
    _RequiredGlobalSecondaryIndexTypeDef, _OptionalGlobalSecondaryIndexTypeDef
):
    pass

GlobalSecondaryIndexUpdateTypeDef = TypedDict(
    "GlobalSecondaryIndexUpdateTypeDef",
    {
        "Update": "UpdateGlobalSecondaryIndexActionTypeDef",
        "Create": "CreateGlobalSecondaryIndexActionTypeDef",
        "Delete": "DeleteGlobalSecondaryIndexActionTypeDef",
    },
    total=False,
)

GlobalTableDescriptionTypeDef = TypedDict(
    "GlobalTableDescriptionTypeDef",
    {
        "ReplicationGroup": List["ReplicaDescriptionTypeDef"],
        "GlobalTableArn": str,
        "CreationDateTime": datetime,
        "GlobalTableStatus": GlobalTableStatusType,
        "GlobalTableName": str,
    },
    total=False,
)

_RequiredGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "_RequiredGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "IndexName": str,
    },
)
_OptionalGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "_OptionalGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "ProvisionedWriteCapacityUnits": int,
        "ProvisionedWriteCapacityAutoScalingSettingsUpdate": "AutoScalingSettingsUpdateTypeDef",
    },
    total=False,
)

class GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef(
    _RequiredGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef,
    _OptionalGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef,
):
    pass

GlobalTableTypeDef = TypedDict(
    "GlobalTableTypeDef",
    {
        "GlobalTableName": str,
        "ReplicationGroup": List["ReplicaTypeDef"],
    },
    total=False,
)

ItemCollectionMetricsTypeDef = TypedDict(
    "ItemCollectionMetricsTypeDef",
    {
        "ItemCollectionKey": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "SizeEstimateRangeGB": List[float],
    },
    total=False,
)

ItemResponseTypeDef = TypedDict(
    "ItemResponseTypeDef",
    {
        "Item": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
    total=False,
)

KeySchemaElementTypeDef = TypedDict(
    "KeySchemaElementTypeDef",
    {
        "AttributeName": str,
        "KeyType": KeyTypeType,
    },
)

_RequiredKeysAndAttributesTypeDef = TypedDict(
    "_RequiredKeysAndAttributesTypeDef",
    {
        "Keys": List[
            Dict[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    List[Any],
                    Dict[str, Any],
                    None,
                ],
            ]
        ],
    },
)
_OptionalKeysAndAttributesTypeDef = TypedDict(
    "_OptionalKeysAndAttributesTypeDef",
    {
        "AttributesToGet": List[str],
        "ConsistentRead": bool,
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
    },
    total=False,
)

class KeysAndAttributesTypeDef(
    _RequiredKeysAndAttributesTypeDef, _OptionalKeysAndAttributesTypeDef
):
    pass

KinesisDataStreamDestinationTypeDef = TypedDict(
    "KinesisDataStreamDestinationTypeDef",
    {
        "StreamArn": str,
        "DestinationStatus": DestinationStatusType,
        "DestinationStatusDescription": str,
    },
    total=False,
)

KinesisStreamingDestinationInputRequestTypeDef = TypedDict(
    "KinesisStreamingDestinationInputRequestTypeDef",
    {
        "TableName": str,
        "StreamArn": str,
    },
)

KinesisStreamingDestinationOutputTypeDef = TypedDict(
    "KinesisStreamingDestinationOutputTypeDef",
    {
        "TableName": str,
        "StreamArn": str,
        "DestinationStatus": DestinationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBackupsInputRequestTypeDef = TypedDict(
    "ListBackupsInputRequestTypeDef",
    {
        "TableName": str,
        "Limit": int,
        "TimeRangeLowerBound": Union[datetime, str],
        "TimeRangeUpperBound": Union[datetime, str],
        "ExclusiveStartBackupArn": str,
        "BackupType": BackupTypeFilterType,
    },
    total=False,
)

ListBackupsOutputTypeDef = TypedDict(
    "ListBackupsOutputTypeDef",
    {
        "BackupSummaries": List["BackupSummaryTypeDef"],
        "LastEvaluatedBackupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContributorInsightsInputRequestTypeDef = TypedDict(
    "ListContributorInsightsInputRequestTypeDef",
    {
        "TableName": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListContributorInsightsOutputTypeDef = TypedDict(
    "ListContributorInsightsOutputTypeDef",
    {
        "ContributorInsightsSummaries": List["ContributorInsightsSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExportsInputRequestTypeDef = TypedDict(
    "ListExportsInputRequestTypeDef",
    {
        "TableArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListExportsOutputTypeDef = TypedDict(
    "ListExportsOutputTypeDef",
    {
        "ExportSummaries": List["ExportSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGlobalTablesInputRequestTypeDef = TypedDict(
    "ListGlobalTablesInputRequestTypeDef",
    {
        "ExclusiveStartGlobalTableName": str,
        "Limit": int,
        "RegionName": str,
    },
    total=False,
)

ListGlobalTablesOutputTypeDef = TypedDict(
    "ListGlobalTablesOutputTypeDef",
    {
        "GlobalTables": List["GlobalTableTypeDef"],
        "LastEvaluatedGlobalTableName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTablesInputRequestTypeDef = TypedDict(
    "ListTablesInputRequestTypeDef",
    {
        "ExclusiveStartTableName": str,
        "Limit": int,
    },
    total=False,
)

ListTablesOutputTypeDef = TypedDict(
    "ListTablesOutputTypeDef",
    {
        "TableNames": List[str],
        "LastEvaluatedTableName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsOfResourceInputRequestTypeDef = TypedDict(
    "_RequiredListTagsOfResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsOfResourceInputRequestTypeDef = TypedDict(
    "_OptionalListTagsOfResourceInputRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListTagsOfResourceInputRequestTypeDef(
    _RequiredListTagsOfResourceInputRequestTypeDef, _OptionalListTagsOfResourceInputRequestTypeDef
):
    pass

ListTagsOfResourceOutputTypeDef = TypedDict(
    "ListTagsOfResourceOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocalSecondaryIndexDescriptionTypeDef = TypedDict(
    "LocalSecondaryIndexDescriptionTypeDef",
    {
        "IndexName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

LocalSecondaryIndexInfoTypeDef = TypedDict(
    "LocalSecondaryIndexInfoTypeDef",
    {
        "IndexName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
    },
    total=False,
)

LocalSecondaryIndexTypeDef = TypedDict(
    "LocalSecondaryIndexTypeDef",
    {
        "IndexName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
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

_RequiredParameterizedStatementTypeDef = TypedDict(
    "_RequiredParameterizedStatementTypeDef",
    {
        "Statement": str,
    },
)
_OptionalParameterizedStatementTypeDef = TypedDict(
    "_OptionalParameterizedStatementTypeDef",
    {
        "Parameters": List[
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ]
        ],
    },
    total=False,
)

class ParameterizedStatementTypeDef(
    _RequiredParameterizedStatementTypeDef, _OptionalParameterizedStatementTypeDef
):
    pass

PointInTimeRecoveryDescriptionTypeDef = TypedDict(
    "PointInTimeRecoveryDescriptionTypeDef",
    {
        "PointInTimeRecoveryStatus": PointInTimeRecoveryStatusType,
        "EarliestRestorableDateTime": datetime,
        "LatestRestorableDateTime": datetime,
    },
    total=False,
)

PointInTimeRecoverySpecificationTypeDef = TypedDict(
    "PointInTimeRecoverySpecificationTypeDef",
    {
        "PointInTimeRecoveryEnabled": bool,
    },
)

ProjectionTypeDef = TypedDict(
    "ProjectionTypeDef",
    {
        "ProjectionType": ProjectionTypeType,
        "NonKeyAttributes": List[str],
    },
    total=False,
)

ProvisionedThroughputDescriptionTypeDef = TypedDict(
    "ProvisionedThroughputDescriptionTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
    total=False,
)

ProvisionedThroughputOverrideTypeDef = TypedDict(
    "ProvisionedThroughputOverrideTypeDef",
    {
        "ReadCapacityUnits": int,
    },
    total=False,
)

ProvisionedThroughputTypeDef = TypedDict(
    "ProvisionedThroughputTypeDef",
    {
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
)

_RequiredPutItemInputRequestTypeDef = TypedDict(
    "_RequiredPutItemInputRequestTypeDef",
    {
        "TableName": str,
        "Item": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
)
_OptionalPutItemInputRequestTypeDef = TypedDict(
    "_OptionalPutItemInputRequestTypeDef",
    {
        "Expected": Dict[str, "ExpectedAttributeValueTypeDef"],
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "ConditionalOperator": ConditionalOperatorType,
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
    total=False,
)

class PutItemInputRequestTypeDef(
    _RequiredPutItemInputRequestTypeDef, _OptionalPutItemInputRequestTypeDef
):
    pass

_RequiredPutItemInputTableTypeDef = TypedDict(
    "_RequiredPutItemInputTableTypeDef",
    {
        "Item": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
)
_OptionalPutItemInputTableTypeDef = TypedDict(
    "_OptionalPutItemInputTableTypeDef",
    {
        "Expected": Dict[str, "ExpectedAttributeValueTypeDef"],
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "ConditionalOperator": ConditionalOperatorType,
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
    total=False,
)

class PutItemInputTableTypeDef(
    _RequiredPutItemInputTableTypeDef, _OptionalPutItemInputTableTypeDef
):
    pass

PutItemOutputTypeDef = TypedDict(
    "PutItemOutputTypeDef",
    {
        "Attributes": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ItemCollectionMetrics": "ItemCollectionMetricsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRequestTypeDef = TypedDict(
    "PutRequestTypeDef",
    {
        "Item": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
)

_RequiredPutTypeDef = TypedDict(
    "_RequiredPutTypeDef",
    {
        "Item": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "TableName": str,
    },
)
_OptionalPutTypeDef = TypedDict(
    "_OptionalPutTypeDef",
    {
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)

class PutTypeDef(_RequiredPutTypeDef, _OptionalPutTypeDef):
    pass

_RequiredQueryInputRequestTypeDef = TypedDict(
    "_RequiredQueryInputRequestTypeDef",
    {
        "TableName": str,
    },
)
_OptionalQueryInputRequestTypeDef = TypedDict(
    "_OptionalQueryInputRequestTypeDef",
    {
        "IndexName": str,
        "Select": SelectType,
        "AttributesToGet": List[str],
        "Limit": int,
        "ConsistentRead": bool,
        "KeyConditions": Dict[str, "ConditionTypeDef"],
        "QueryFilter": Dict[str, "ConditionTypeDef"],
        "ConditionalOperator": ConditionalOperatorType,
        "ScanIndexForward": bool,
        "ExclusiveStartKey": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ProjectionExpression": str,
        "FilterExpression": str,
        "KeyConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
    total=False,
)

class QueryInputRequestTypeDef(
    _RequiredQueryInputRequestTypeDef, _OptionalQueryInputRequestTypeDef
):
    pass

QueryInputTableTypeDef = TypedDict(
    "QueryInputTableTypeDef",
    {
        "IndexName": str,
        "Select": SelectType,
        "AttributesToGet": List[str],
        "Limit": int,
        "ConsistentRead": bool,
        "KeyConditions": Dict[str, "ConditionTypeDef"],
        "QueryFilter": Dict[str, "ConditionTypeDef"],
        "ConditionalOperator": ConditionalOperatorType,
        "ScanIndexForward": bool,
        "ExclusiveStartKey": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ProjectionExpression": str,
        "FilterExpression": Union[str, ConditionBase],
        "KeyConditionExpression": Union[str, ConditionBase],
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
    total=False,
)

QueryOutputTypeDef = TypedDict(
    "QueryOutputTypeDef",
    {
        "Items": List[
            Dict[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    List[Any],
                    Dict[str, Any],
                    None,
                ],
            ]
        ],
        "Count": int,
        "ScannedCount": int,
        "LastEvaluatedKey": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReplicaAutoScalingDescriptionTypeDef = TypedDict(
    "ReplicaAutoScalingDescriptionTypeDef",
    {
        "RegionName": str,
        "GlobalSecondaryIndexes": List["ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef"],
        "ReplicaProvisionedReadCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
        "ReplicaProvisionedWriteCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
        "ReplicaStatus": ReplicaStatusType,
    },
    total=False,
)

_RequiredReplicaAutoScalingUpdateTypeDef = TypedDict(
    "_RequiredReplicaAutoScalingUpdateTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalReplicaAutoScalingUpdateTypeDef = TypedDict(
    "_OptionalReplicaAutoScalingUpdateTypeDef",
    {
        "ReplicaGlobalSecondaryIndexUpdates": List[
            "ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef"
        ],
        "ReplicaProvisionedReadCapacityAutoScalingUpdate": "AutoScalingSettingsUpdateTypeDef",
    },
    total=False,
)

class ReplicaAutoScalingUpdateTypeDef(
    _RequiredReplicaAutoScalingUpdateTypeDef, _OptionalReplicaAutoScalingUpdateTypeDef
):
    pass

ReplicaDescriptionTypeDef = TypedDict(
    "ReplicaDescriptionTypeDef",
    {
        "RegionName": str,
        "ReplicaStatus": ReplicaStatusType,
        "ReplicaStatusDescription": str,
        "ReplicaStatusPercentProgress": str,
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": "ProvisionedThroughputOverrideTypeDef",
        "GlobalSecondaryIndexes": List["ReplicaGlobalSecondaryIndexDescriptionTypeDef"],
        "ReplicaInaccessibleDateTime": datetime,
    },
    total=False,
)

ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef",
    {
        "IndexName": str,
        "IndexStatus": IndexStatusType,
        "ProvisionedReadCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
        "ProvisionedWriteCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
    },
    total=False,
)

ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef",
    {
        "IndexName": str,
        "ProvisionedReadCapacityAutoScalingUpdate": "AutoScalingSettingsUpdateTypeDef",
    },
    total=False,
)

ReplicaGlobalSecondaryIndexDescriptionTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexDescriptionTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughputOverride": "ProvisionedThroughputOverrideTypeDef",
    },
    total=False,
)

_RequiredReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef = TypedDict(
    "_RequiredReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef",
    {
        "IndexName": str,
    },
)
_OptionalReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef = TypedDict(
    "_OptionalReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef",
    {
        "IndexStatus": IndexStatusType,
        "ProvisionedReadCapacityUnits": int,
        "ProvisionedReadCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
        "ProvisionedWriteCapacityUnits": int,
        "ProvisionedWriteCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
    },
    total=False,
)

class ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef(
    _RequiredReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef,
    _OptionalReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef,
):
    pass

_RequiredReplicaGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "_RequiredReplicaGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "IndexName": str,
    },
)
_OptionalReplicaGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "_OptionalReplicaGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "ProvisionedReadCapacityUnits": int,
        "ProvisionedReadCapacityAutoScalingSettingsUpdate": "AutoScalingSettingsUpdateTypeDef",
    },
    total=False,
)

class ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef(
    _RequiredReplicaGlobalSecondaryIndexSettingsUpdateTypeDef,
    _OptionalReplicaGlobalSecondaryIndexSettingsUpdateTypeDef,
):
    pass

_RequiredReplicaGlobalSecondaryIndexTypeDef = TypedDict(
    "_RequiredReplicaGlobalSecondaryIndexTypeDef",
    {
        "IndexName": str,
    },
)
_OptionalReplicaGlobalSecondaryIndexTypeDef = TypedDict(
    "_OptionalReplicaGlobalSecondaryIndexTypeDef",
    {
        "ProvisionedThroughputOverride": "ProvisionedThroughputOverrideTypeDef",
    },
    total=False,
)

class ReplicaGlobalSecondaryIndexTypeDef(
    _RequiredReplicaGlobalSecondaryIndexTypeDef, _OptionalReplicaGlobalSecondaryIndexTypeDef
):
    pass

_RequiredReplicaSettingsDescriptionTypeDef = TypedDict(
    "_RequiredReplicaSettingsDescriptionTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalReplicaSettingsDescriptionTypeDef = TypedDict(
    "_OptionalReplicaSettingsDescriptionTypeDef",
    {
        "ReplicaStatus": ReplicaStatusType,
        "ReplicaBillingModeSummary": "BillingModeSummaryTypeDef",
        "ReplicaProvisionedReadCapacityUnits": int,
        "ReplicaProvisionedReadCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
        "ReplicaProvisionedWriteCapacityUnits": int,
        "ReplicaProvisionedWriteCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
        "ReplicaGlobalSecondaryIndexSettings": List[
            "ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef"
        ],
    },
    total=False,
)

class ReplicaSettingsDescriptionTypeDef(
    _RequiredReplicaSettingsDescriptionTypeDef, _OptionalReplicaSettingsDescriptionTypeDef
):
    pass

_RequiredReplicaSettingsUpdateTypeDef = TypedDict(
    "_RequiredReplicaSettingsUpdateTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalReplicaSettingsUpdateTypeDef = TypedDict(
    "_OptionalReplicaSettingsUpdateTypeDef",
    {
        "ReplicaProvisionedReadCapacityUnits": int,
        "ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate": "AutoScalingSettingsUpdateTypeDef",
        "ReplicaGlobalSecondaryIndexSettingsUpdate": List[
            "ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef"
        ],
    },
    total=False,
)

class ReplicaSettingsUpdateTypeDef(
    _RequiredReplicaSettingsUpdateTypeDef, _OptionalReplicaSettingsUpdateTypeDef
):
    pass

ReplicaTypeDef = TypedDict(
    "ReplicaTypeDef",
    {
        "RegionName": str,
    },
    total=False,
)

ReplicaUpdateTypeDef = TypedDict(
    "ReplicaUpdateTypeDef",
    {
        "Create": "CreateReplicaActionTypeDef",
        "Delete": "DeleteReplicaActionTypeDef",
    },
    total=False,
)

ReplicationGroupUpdateTypeDef = TypedDict(
    "ReplicationGroupUpdateTypeDef",
    {
        "Create": "CreateReplicationGroupMemberActionTypeDef",
        "Update": "UpdateReplicationGroupMemberActionTypeDef",
        "Delete": "DeleteReplicationGroupMemberActionTypeDef",
    },
    total=False,
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

_RequiredRestoreSummaryTypeDef = TypedDict(
    "_RequiredRestoreSummaryTypeDef",
    {
        "RestoreDateTime": datetime,
        "RestoreInProgress": bool,
    },
)
_OptionalRestoreSummaryTypeDef = TypedDict(
    "_OptionalRestoreSummaryTypeDef",
    {
        "SourceBackupArn": str,
        "SourceTableArn": str,
    },
    total=False,
)

class RestoreSummaryTypeDef(_RequiredRestoreSummaryTypeDef, _OptionalRestoreSummaryTypeDef):
    pass

_RequiredRestoreTableFromBackupInputRequestTypeDef = TypedDict(
    "_RequiredRestoreTableFromBackupInputRequestTypeDef",
    {
        "TargetTableName": str,
        "BackupArn": str,
    },
)
_OptionalRestoreTableFromBackupInputRequestTypeDef = TypedDict(
    "_OptionalRestoreTableFromBackupInputRequestTypeDef",
    {
        "BillingModeOverride": BillingModeType,
        "GlobalSecondaryIndexOverride": List["GlobalSecondaryIndexTypeDef"],
        "LocalSecondaryIndexOverride": List["LocalSecondaryIndexTypeDef"],
        "ProvisionedThroughputOverride": "ProvisionedThroughputTypeDef",
        "SSESpecificationOverride": "SSESpecificationTypeDef",
    },
    total=False,
)

class RestoreTableFromBackupInputRequestTypeDef(
    _RequiredRestoreTableFromBackupInputRequestTypeDef,
    _OptionalRestoreTableFromBackupInputRequestTypeDef,
):
    pass

RestoreTableFromBackupOutputTypeDef = TypedDict(
    "RestoreTableFromBackupOutputTypeDef",
    {
        "TableDescription": "TableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRestoreTableToPointInTimeInputRequestTypeDef = TypedDict(
    "_RequiredRestoreTableToPointInTimeInputRequestTypeDef",
    {
        "TargetTableName": str,
    },
)
_OptionalRestoreTableToPointInTimeInputRequestTypeDef = TypedDict(
    "_OptionalRestoreTableToPointInTimeInputRequestTypeDef",
    {
        "SourceTableArn": str,
        "SourceTableName": str,
        "UseLatestRestorableTime": bool,
        "RestoreDateTime": Union[datetime, str],
        "BillingModeOverride": BillingModeType,
        "GlobalSecondaryIndexOverride": List["GlobalSecondaryIndexTypeDef"],
        "LocalSecondaryIndexOverride": List["LocalSecondaryIndexTypeDef"],
        "ProvisionedThroughputOverride": "ProvisionedThroughputTypeDef",
        "SSESpecificationOverride": "SSESpecificationTypeDef",
    },
    total=False,
)

class RestoreTableToPointInTimeInputRequestTypeDef(
    _RequiredRestoreTableToPointInTimeInputRequestTypeDef,
    _OptionalRestoreTableToPointInTimeInputRequestTypeDef,
):
    pass

RestoreTableToPointInTimeOutputTypeDef = TypedDict(
    "RestoreTableToPointInTimeOutputTypeDef",
    {
        "TableDescription": "TableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SSEDescriptionTypeDef = TypedDict(
    "SSEDescriptionTypeDef",
    {
        "Status": SSEStatusType,
        "SSEType": SSETypeType,
        "KMSMasterKeyArn": str,
        "InaccessibleEncryptionDateTime": datetime,
    },
    total=False,
)

SSESpecificationTypeDef = TypedDict(
    "SSESpecificationTypeDef",
    {
        "Enabled": bool,
        "SSEType": SSETypeType,
        "KMSMasterKeyId": str,
    },
    total=False,
)

_RequiredScanInputRequestTypeDef = TypedDict(
    "_RequiredScanInputRequestTypeDef",
    {
        "TableName": str,
    },
)
_OptionalScanInputRequestTypeDef = TypedDict(
    "_OptionalScanInputRequestTypeDef",
    {
        "IndexName": str,
        "AttributesToGet": List[str],
        "Limit": int,
        "Select": SelectType,
        "ScanFilter": Dict[str, "ConditionTypeDef"],
        "ConditionalOperator": ConditionalOperatorType,
        "ExclusiveStartKey": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "TotalSegments": int,
        "Segment": int,
        "ProjectionExpression": str,
        "FilterExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ConsistentRead": bool,
    },
    total=False,
)

class ScanInputRequestTypeDef(_RequiredScanInputRequestTypeDef, _OptionalScanInputRequestTypeDef):
    pass

ScanInputTableTypeDef = TypedDict(
    "ScanInputTableTypeDef",
    {
        "IndexName": str,
        "AttributesToGet": List[str],
        "Limit": int,
        "Select": SelectType,
        "ScanFilter": Dict[str, "ConditionTypeDef"],
        "ConditionalOperator": ConditionalOperatorType,
        "ExclusiveStartKey": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "TotalSegments": int,
        "Segment": int,
        "ProjectionExpression": str,
        "FilterExpression": Union[str, ConditionBase],
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ConsistentRead": bool,
    },
    total=False,
)

ScanOutputTypeDef = TypedDict(
    "ScanOutputTypeDef",
    {
        "Items": List[
            Dict[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    List[Any],
                    Dict[str, Any],
                    None,
                ],
            ]
        ],
        "Count": int,
        "ScannedCount": int,
        "LastEvaluatedKey": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceResourceTableRequestTypeDef = TypedDict(
    "ServiceResourceTableRequestTypeDef",
    {
        "name": str,
    },
)

_RequiredSourceTableDetailsTypeDef = TypedDict(
    "_RequiredSourceTableDetailsTypeDef",
    {
        "TableName": str,
        "TableId": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "TableCreationDateTime": datetime,
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
    },
)
_OptionalSourceTableDetailsTypeDef = TypedDict(
    "_OptionalSourceTableDetailsTypeDef",
    {
        "TableArn": str,
        "TableSizeBytes": int,
        "ItemCount": int,
        "BillingMode": BillingModeType,
    },
    total=False,
)

class SourceTableDetailsTypeDef(
    _RequiredSourceTableDetailsTypeDef, _OptionalSourceTableDetailsTypeDef
):
    pass

SourceTableFeatureDetailsTypeDef = TypedDict(
    "SourceTableFeatureDetailsTypeDef",
    {
        "LocalSecondaryIndexes": List["LocalSecondaryIndexInfoTypeDef"],
        "GlobalSecondaryIndexes": List["GlobalSecondaryIndexInfoTypeDef"],
        "StreamDescription": "StreamSpecificationTypeDef",
        "TimeToLiveDescription": "TimeToLiveDescriptionTypeDef",
        "SSEDescription": "SSEDescriptionTypeDef",
    },
    total=False,
)

_RequiredStreamSpecificationTypeDef = TypedDict(
    "_RequiredStreamSpecificationTypeDef",
    {
        "StreamEnabled": bool,
    },
)
_OptionalStreamSpecificationTypeDef = TypedDict(
    "_OptionalStreamSpecificationTypeDef",
    {
        "StreamViewType": StreamViewTypeType,
    },
    total=False,
)

class StreamSpecificationTypeDef(
    _RequiredStreamSpecificationTypeDef, _OptionalStreamSpecificationTypeDef
):
    pass

TableAutoScalingDescriptionTypeDef = TypedDict(
    "TableAutoScalingDescriptionTypeDef",
    {
        "TableName": str,
        "TableStatus": TableStatusType,
        "Replicas": List["ReplicaAutoScalingDescriptionTypeDef"],
    },
    total=False,
)

TableBatchWriterRequestTypeDef = TypedDict(
    "TableBatchWriterRequestTypeDef",
    {
        "overwrite_by_pkeys": List[str],
    },
    total=False,
)

TableDescriptionTypeDef = TypedDict(
    "TableDescriptionTypeDef",
    {
        "AttributeDefinitions": List["AttributeDefinitionTypeDef"],
        "TableName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "TableStatus": TableStatusType,
        "CreationDateTime": datetime,
        "ProvisionedThroughput": "ProvisionedThroughputDescriptionTypeDef",
        "TableSizeBytes": int,
        "ItemCount": int,
        "TableArn": str,
        "TableId": str,
        "BillingModeSummary": "BillingModeSummaryTypeDef",
        "LocalSecondaryIndexes": List["LocalSecondaryIndexDescriptionTypeDef"],
        "GlobalSecondaryIndexes": List["GlobalSecondaryIndexDescriptionTypeDef"],
        "StreamSpecification": "StreamSpecificationTypeDef",
        "LatestStreamLabel": str,
        "LatestStreamArn": str,
        "GlobalTableVersion": str,
        "Replicas": List["ReplicaDescriptionTypeDef"],
        "RestoreSummary": "RestoreSummaryTypeDef",
        "SSEDescription": "SSEDescriptionTypeDef",
        "ArchivalSummary": "ArchivalSummaryTypeDef",
    },
    total=False,
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TimeToLiveDescriptionTypeDef = TypedDict(
    "TimeToLiveDescriptionTypeDef",
    {
        "TimeToLiveStatus": TimeToLiveStatusType,
        "AttributeName": str,
    },
    total=False,
)

TimeToLiveSpecificationTypeDef = TypedDict(
    "TimeToLiveSpecificationTypeDef",
    {
        "Enabled": bool,
        "AttributeName": str,
    },
)

TransactGetItemTypeDef = TypedDict(
    "TransactGetItemTypeDef",
    {
        "Get": "GetTypeDef",
    },
)

_RequiredTransactGetItemsInputRequestTypeDef = TypedDict(
    "_RequiredTransactGetItemsInputRequestTypeDef",
    {
        "TransactItems": List["TransactGetItemTypeDef"],
    },
)
_OptionalTransactGetItemsInputRequestTypeDef = TypedDict(
    "_OptionalTransactGetItemsInputRequestTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
    },
    total=False,
)

class TransactGetItemsInputRequestTypeDef(
    _RequiredTransactGetItemsInputRequestTypeDef, _OptionalTransactGetItemsInputRequestTypeDef
):
    pass

TransactGetItemsOutputTypeDef = TypedDict(
    "TransactGetItemsOutputTypeDef",
    {
        "ConsumedCapacity": List["ConsumedCapacityTypeDef"],
        "Responses": List["ItemResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TransactWriteItemTypeDef = TypedDict(
    "TransactWriteItemTypeDef",
    {
        "ConditionCheck": "ConditionCheckTypeDef",
        "Put": "PutTypeDef",
        "Delete": "DeleteTypeDef",
        "Update": "UpdateTypeDef",
    },
    total=False,
)

_RequiredTransactWriteItemsInputRequestTypeDef = TypedDict(
    "_RequiredTransactWriteItemsInputRequestTypeDef",
    {
        "TransactItems": List["TransactWriteItemTypeDef"],
    },
)
_OptionalTransactWriteItemsInputRequestTypeDef = TypedDict(
    "_OptionalTransactWriteItemsInputRequestTypeDef",
    {
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "ClientRequestToken": str,
    },
    total=False,
)

class TransactWriteItemsInputRequestTypeDef(
    _RequiredTransactWriteItemsInputRequestTypeDef, _OptionalTransactWriteItemsInputRequestTypeDef
):
    pass

TransactWriteItemsOutputTypeDef = TypedDict(
    "TransactWriteItemsOutputTypeDef",
    {
        "ConsumedCapacity": List["ConsumedCapacityTypeDef"],
        "ItemCollectionMetrics": Dict[str, List["ItemCollectionMetricsTypeDef"]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateContinuousBackupsInputRequestTypeDef = TypedDict(
    "UpdateContinuousBackupsInputRequestTypeDef",
    {
        "TableName": str,
        "PointInTimeRecoverySpecification": "PointInTimeRecoverySpecificationTypeDef",
    },
)

UpdateContinuousBackupsOutputTypeDef = TypedDict(
    "UpdateContinuousBackupsOutputTypeDef",
    {
        "ContinuousBackupsDescription": "ContinuousBackupsDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateContributorInsightsInputRequestTypeDef = TypedDict(
    "_RequiredUpdateContributorInsightsInputRequestTypeDef",
    {
        "TableName": str,
        "ContributorInsightsAction": ContributorInsightsActionType,
    },
)
_OptionalUpdateContributorInsightsInputRequestTypeDef = TypedDict(
    "_OptionalUpdateContributorInsightsInputRequestTypeDef",
    {
        "IndexName": str,
    },
    total=False,
)

class UpdateContributorInsightsInputRequestTypeDef(
    _RequiredUpdateContributorInsightsInputRequestTypeDef,
    _OptionalUpdateContributorInsightsInputRequestTypeDef,
):
    pass

UpdateContributorInsightsOutputTypeDef = TypedDict(
    "UpdateContributorInsightsOutputTypeDef",
    {
        "TableName": str,
        "IndexName": str,
        "ContributorInsightsStatus": ContributorInsightsStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGlobalSecondaryIndexActionTypeDef = TypedDict(
    "UpdateGlobalSecondaryIndexActionTypeDef",
    {
        "IndexName": str,
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
    },
)

UpdateGlobalTableInputRequestTypeDef = TypedDict(
    "UpdateGlobalTableInputRequestTypeDef",
    {
        "GlobalTableName": str,
        "ReplicaUpdates": List["ReplicaUpdateTypeDef"],
    },
)

UpdateGlobalTableOutputTypeDef = TypedDict(
    "UpdateGlobalTableOutputTypeDef",
    {
        "GlobalTableDescription": "GlobalTableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGlobalTableSettingsInputRequestTypeDef = TypedDict(
    "_RequiredUpdateGlobalTableSettingsInputRequestTypeDef",
    {
        "GlobalTableName": str,
    },
)
_OptionalUpdateGlobalTableSettingsInputRequestTypeDef = TypedDict(
    "_OptionalUpdateGlobalTableSettingsInputRequestTypeDef",
    {
        "GlobalTableBillingMode": BillingModeType,
        "GlobalTableProvisionedWriteCapacityUnits": int,
        "GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate": "AutoScalingSettingsUpdateTypeDef",
        "GlobalTableGlobalSecondaryIndexSettingsUpdate": List[
            "GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef"
        ],
        "ReplicaSettingsUpdate": List["ReplicaSettingsUpdateTypeDef"],
    },
    total=False,
)

class UpdateGlobalTableSettingsInputRequestTypeDef(
    _RequiredUpdateGlobalTableSettingsInputRequestTypeDef,
    _OptionalUpdateGlobalTableSettingsInputRequestTypeDef,
):
    pass

UpdateGlobalTableSettingsOutputTypeDef = TypedDict(
    "UpdateGlobalTableSettingsOutputTypeDef",
    {
        "GlobalTableName": str,
        "ReplicaSettings": List["ReplicaSettingsDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateItemInputRequestTypeDef = TypedDict(
    "_RequiredUpdateItemInputRequestTypeDef",
    {
        "TableName": str,
        "Key": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
)
_OptionalUpdateItemInputRequestTypeDef = TypedDict(
    "_OptionalUpdateItemInputRequestTypeDef",
    {
        "AttributeUpdates": Dict[str, "AttributeValueUpdateTypeDef"],
        "Expected": Dict[str, "ExpectedAttributeValueTypeDef"],
        "ConditionalOperator": ConditionalOperatorType,
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "UpdateExpression": str,
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
    total=False,
)

class UpdateItemInputRequestTypeDef(
    _RequiredUpdateItemInputRequestTypeDef, _OptionalUpdateItemInputRequestTypeDef
):
    pass

_RequiredUpdateItemInputTableTypeDef = TypedDict(
    "_RequiredUpdateItemInputTableTypeDef",
    {
        "Key": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
)
_OptionalUpdateItemInputTableTypeDef = TypedDict(
    "_OptionalUpdateItemInputTableTypeDef",
    {
        "AttributeUpdates": Dict[str, "AttributeValueUpdateTypeDef"],
        "Expected": Dict[str, "ExpectedAttributeValueTypeDef"],
        "ConditionalOperator": ConditionalOperatorType,
        "ReturnValues": ReturnValueType,
        "ReturnConsumedCapacity": ReturnConsumedCapacityType,
        "ReturnItemCollectionMetrics": ReturnItemCollectionMetricsType,
        "UpdateExpression": str,
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
    },
    total=False,
)

class UpdateItemInputTableTypeDef(
    _RequiredUpdateItemInputTableTypeDef, _OptionalUpdateItemInputTableTypeDef
):
    pass

UpdateItemOutputTypeDef = TypedDict(
    "UpdateItemOutputTypeDef",
    {
        "Attributes": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ItemCollectionMetrics": "ItemCollectionMetricsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateReplicationGroupMemberActionTypeDef = TypedDict(
    "_RequiredUpdateReplicationGroupMemberActionTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalUpdateReplicationGroupMemberActionTypeDef = TypedDict(
    "_OptionalUpdateReplicationGroupMemberActionTypeDef",
    {
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": "ProvisionedThroughputOverrideTypeDef",
        "GlobalSecondaryIndexes": List["ReplicaGlobalSecondaryIndexTypeDef"],
    },
    total=False,
)

class UpdateReplicationGroupMemberActionTypeDef(
    _RequiredUpdateReplicationGroupMemberActionTypeDef,
    _OptionalUpdateReplicationGroupMemberActionTypeDef,
):
    pass

_RequiredUpdateTableInputRequestTypeDef = TypedDict(
    "_RequiredUpdateTableInputRequestTypeDef",
    {
        "TableName": str,
    },
)
_OptionalUpdateTableInputRequestTypeDef = TypedDict(
    "_OptionalUpdateTableInputRequestTypeDef",
    {
        "AttributeDefinitions": List["AttributeDefinitionTypeDef"],
        "BillingMode": BillingModeType,
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
        "GlobalSecondaryIndexUpdates": List["GlobalSecondaryIndexUpdateTypeDef"],
        "StreamSpecification": "StreamSpecificationTypeDef",
        "SSESpecification": "SSESpecificationTypeDef",
        "ReplicaUpdates": List["ReplicationGroupUpdateTypeDef"],
    },
    total=False,
)

class UpdateTableInputRequestTypeDef(
    _RequiredUpdateTableInputRequestTypeDef, _OptionalUpdateTableInputRequestTypeDef
):
    pass

UpdateTableInputTableTypeDef = TypedDict(
    "UpdateTableInputTableTypeDef",
    {
        "AttributeDefinitions": List["AttributeDefinitionTypeDef"],
        "BillingMode": BillingModeType,
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
        "GlobalSecondaryIndexUpdates": List["GlobalSecondaryIndexUpdateTypeDef"],
        "StreamSpecification": "StreamSpecificationTypeDef",
        "SSESpecification": "SSESpecificationTypeDef",
        "ReplicaUpdates": List["ReplicationGroupUpdateTypeDef"],
    },
    total=False,
)

UpdateTableOutputTypeDef = TypedDict(
    "UpdateTableOutputTypeDef",
    {
        "TableDescription": "TableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTableReplicaAutoScalingInputRequestTypeDef = TypedDict(
    "_RequiredUpdateTableReplicaAutoScalingInputRequestTypeDef",
    {
        "TableName": str,
    },
)
_OptionalUpdateTableReplicaAutoScalingInputRequestTypeDef = TypedDict(
    "_OptionalUpdateTableReplicaAutoScalingInputRequestTypeDef",
    {
        "GlobalSecondaryIndexUpdates": List["GlobalSecondaryIndexAutoScalingUpdateTypeDef"],
        "ProvisionedWriteCapacityAutoScalingUpdate": "AutoScalingSettingsUpdateTypeDef",
        "ReplicaUpdates": List["ReplicaAutoScalingUpdateTypeDef"],
    },
    total=False,
)

class UpdateTableReplicaAutoScalingInputRequestTypeDef(
    _RequiredUpdateTableReplicaAutoScalingInputRequestTypeDef,
    _OptionalUpdateTableReplicaAutoScalingInputRequestTypeDef,
):
    pass

UpdateTableReplicaAutoScalingOutputTypeDef = TypedDict(
    "UpdateTableReplicaAutoScalingOutputTypeDef",
    {
        "TableAutoScalingDescription": "TableAutoScalingDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTimeToLiveInputRequestTypeDef = TypedDict(
    "UpdateTimeToLiveInputRequestTypeDef",
    {
        "TableName": str,
        "TimeToLiveSpecification": "TimeToLiveSpecificationTypeDef",
    },
)

UpdateTimeToLiveOutputTypeDef = TypedDict(
    "UpdateTimeToLiveOutputTypeDef",
    {
        "TimeToLiveSpecification": "TimeToLiveSpecificationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTypeDef = TypedDict(
    "_RequiredUpdateTypeDef",
    {
        "Key": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "UpdateExpression": str,
        "TableName": str,
    },
)
_OptionalUpdateTypeDef = TypedDict(
    "_OptionalUpdateTypeDef",
    {
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailureType,
    },
    total=False,
)

class UpdateTypeDef(_RequiredUpdateTypeDef, _OptionalUpdateTypeDef):
    pass

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

WriteRequestTypeDef = TypedDict(
    "WriteRequestTypeDef",
    {
        "PutRequest": "PutRequestTypeDef",
        "DeleteRequest": "DeleteRequestTypeDef",
    },
    total=False,
)
