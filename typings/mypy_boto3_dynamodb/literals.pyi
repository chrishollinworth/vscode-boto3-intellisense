"""
Type annotations for dynamodb service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/literals.html)

Usage::

    ```python
    from mypy_boto3_dynamodb.literals import AttributeActionType

    data: AttributeActionType = "ADD"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AttributeActionType",
    "BackupStatusType",
    "BackupTypeFilterType",
    "BackupTypeType",
    "BatchStatementErrorCodeEnumType",
    "BillingModeType",
    "ComparisonOperatorType",
    "ConditionalOperatorType",
    "ContinuousBackupsStatusType",
    "ContributorInsightsActionType",
    "ContributorInsightsStatusType",
    "DestinationStatusType",
    "ExportFormatType",
    "ExportStatusType",
    "GlobalTableStatusType",
    "IndexStatusType",
    "KeyTypeType",
    "ListBackupsPaginatorName",
    "ListTablesPaginatorName",
    "ListTagsOfResourcePaginatorName",
    "PointInTimeRecoveryStatusType",
    "ProjectionTypeType",
    "QueryPaginatorName",
    "ReplicaStatusType",
    "ReturnConsumedCapacityType",
    "ReturnItemCollectionMetricsType",
    "ReturnValueType",
    "ReturnValuesOnConditionCheckFailureType",
    "S3SseAlgorithmType",
    "SSEStatusType",
    "SSETypeType",
    "ScalarAttributeTypeType",
    "ScanPaginatorName",
    "SelectType",
    "StreamViewTypeType",
    "TableExistsWaiterName",
    "TableNotExistsWaiterName",
    "TableStatusType",
    "TimeToLiveStatusType",
)

AttributeActionType = Literal["ADD", "DELETE", "PUT"]
BackupStatusType = Literal["AVAILABLE", "CREATING", "DELETED"]
BackupTypeFilterType = Literal["ALL", "AWS_BACKUP", "SYSTEM", "USER"]
BackupTypeType = Literal["AWS_BACKUP", "SYSTEM", "USER"]
BatchStatementErrorCodeEnumType = Literal[
    "AccessDenied",
    "ConditionalCheckFailed",
    "DuplicateItem",
    "InternalServerError",
    "ItemCollectionSizeLimitExceeded",
    "ProvisionedThroughputExceeded",
    "RequestLimitExceeded",
    "ResourceNotFound",
    "ThrottlingError",
    "TransactionConflict",
    "ValidationError",
]
BillingModeType = Literal["PAY_PER_REQUEST", "PROVISIONED"]
ComparisonOperatorType = Literal[
    "BEGINS_WITH",
    "BETWEEN",
    "CONTAINS",
    "EQ",
    "GE",
    "GT",
    "IN",
    "LE",
    "LT",
    "NE",
    "NOT_CONTAINS",
    "NOT_NULL",
    "NULL",
]
ConditionalOperatorType = Literal["AND", "OR"]
ContinuousBackupsStatusType = Literal["DISABLED", "ENABLED"]
ContributorInsightsActionType = Literal["DISABLE", "ENABLE"]
ContributorInsightsStatusType = Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING", "FAILED"]
DestinationStatusType = Literal["ACTIVE", "DISABLED", "DISABLING", "ENABLE_FAILED", "ENABLING"]
ExportFormatType = Literal["DYNAMODB_JSON", "ION"]
ExportStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS"]
GlobalTableStatusType = Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"]
IndexStatusType = Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"]
KeyTypeType = Literal["HASH", "RANGE"]
ListBackupsPaginatorName = Literal["list_backups"]
ListTablesPaginatorName = Literal["list_tables"]
ListTagsOfResourcePaginatorName = Literal["list_tags_of_resource"]
PointInTimeRecoveryStatusType = Literal["DISABLED", "ENABLED"]
ProjectionTypeType = Literal["ALL", "INCLUDE", "KEYS_ONLY"]
QueryPaginatorName = Literal["query"]
ReplicaStatusType = Literal[
    "ACTIVE",
    "CREATING",
    "CREATION_FAILED",
    "DELETING",
    "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
    "REGION_DISABLED",
    "UPDATING",
]
ReturnConsumedCapacityType = Literal["INDEXES", "NONE", "TOTAL"]
ReturnItemCollectionMetricsType = Literal["NONE", "SIZE"]
ReturnValueType = Literal["ALL_NEW", "ALL_OLD", "NONE", "UPDATED_NEW", "UPDATED_OLD"]
ReturnValuesOnConditionCheckFailureType = Literal["ALL_OLD", "NONE"]
S3SseAlgorithmType = Literal["AES256", "KMS"]
SSEStatusType = Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING", "UPDATING"]
SSETypeType = Literal["AES256", "KMS"]
ScalarAttributeTypeType = Literal["B", "N", "S"]
ScanPaginatorName = Literal["scan"]
SelectType = Literal["ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "COUNT", "SPECIFIC_ATTRIBUTES"]
StreamViewTypeType = Literal["KEYS_ONLY", "NEW_AND_OLD_IMAGES", "NEW_IMAGE", "OLD_IMAGE"]
TableExistsWaiterName = Literal["table_exists"]
TableNotExistsWaiterName = Literal["table_not_exists"]
TableStatusType = Literal[
    "ACTIVE",
    "ARCHIVED",
    "ARCHIVING",
    "CREATING",
    "DELETING",
    "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
    "UPDATING",
]
TimeToLiveStatusType = Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING"]
