# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for dynamodb service client

Usage::

    ```python
    import boto3
    from mypy_boto3_dynamodb import DynamoDBClient

    client: DynamoDBClient = boto3.client("dynamodb")
    ```
"""
import sys
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, List, Set, Type, Union, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_dynamodb.paginator import (
    ListBackupsPaginator,
    ListTablesPaginator,
    ListTagsOfResourcePaginator,
    QueryPaginator,
    ScanPaginator,
)
from mypy_boto3_dynamodb.type_defs import (
    AttributeDefinitionTypeDef,
    AttributeValueUpdateTypeDef,
    AutoScalingSettingsUpdateTypeDef,
    BatchGetItemOutputTypeDef,
    BatchWriteItemOutputTypeDef,
    ConditionTypeDef,
    CreateBackupOutputTypeDef,
    CreateGlobalTableOutputTypeDef,
    CreateTableOutputTypeDef,
    DeleteBackupOutputTypeDef,
    DeleteItemOutputTypeDef,
    DeleteTableOutputTypeDef,
    DescribeBackupOutputTypeDef,
    DescribeContinuousBackupsOutputTypeDef,
    DescribeContributorInsightsOutputTypeDef,
    DescribeEndpointsResponseTypeDef,
    DescribeGlobalTableOutputTypeDef,
    DescribeGlobalTableSettingsOutputTypeDef,
    DescribeLimitsOutputTypeDef,
    DescribeTableOutputTypeDef,
    DescribeTableReplicaAutoScalingOutputTypeDef,
    DescribeTimeToLiveOutputTypeDef,
    ExpectedAttributeValueTypeDef,
    GetItemOutputTypeDef,
    GlobalSecondaryIndexAutoScalingUpdateTypeDef,
    GlobalSecondaryIndexTypeDef,
    GlobalSecondaryIndexUpdateTypeDef,
    GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef,
    KeysAndAttributesTypeDef,
    KeySchemaElementTypeDef,
    ListBackupsOutputTypeDef,
    ListContributorInsightsOutputTypeDef,
    ListGlobalTablesOutputTypeDef,
    ListTablesOutputTypeDef,
    ListTagsOfResourceOutputTypeDef,
    LocalSecondaryIndexTypeDef,
    PointInTimeRecoverySpecificationTypeDef,
    ProvisionedThroughputTypeDef,
    PutItemOutputTypeDef,
    QueryOutputTypeDef,
    ReplicaAutoScalingUpdateTypeDef,
    ReplicaSettingsUpdateTypeDef,
    ReplicationGroupUpdateTypeDef,
    ReplicaTypeDef,
    ReplicaUpdateTypeDef,
    RestoreTableFromBackupOutputTypeDef,
    RestoreTableToPointInTimeOutputTypeDef,
    ScanOutputTypeDef,
    SSESpecificationTypeDef,
    StreamSpecificationTypeDef,
    TagTypeDef,
    TimeToLiveSpecificationTypeDef,
    TransactGetItemsOutputTypeDef,
    TransactGetItemTypeDef,
    TransactWriteItemsOutputTypeDef,
    TransactWriteItemTypeDef,
    UpdateContinuousBackupsOutputTypeDef,
    UpdateContributorInsightsOutputTypeDef,
    UpdateGlobalTableOutputTypeDef,
    UpdateGlobalTableSettingsOutputTypeDef,
    UpdateItemOutputTypeDef,
    UpdateTableOutputTypeDef,
    UpdateTableReplicaAutoScalingOutputTypeDef,
    UpdateTimeToLiveOutputTypeDef,
    WriteRequestTypeDef,
)
from mypy_boto3_dynamodb.waiter import TableExistsWaiter, TableNotExistsWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DynamoDBClient",)


class Exceptions:
    BackupInUseException: Type[Boto3ClientError]
    BackupNotFoundException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    ConditionalCheckFailedException: Type[Boto3ClientError]
    ContinuousBackupsUnavailableException: Type[Boto3ClientError]
    GlobalTableAlreadyExistsException: Type[Boto3ClientError]
    GlobalTableNotFoundException: Type[Boto3ClientError]
    IdempotentParameterMismatchException: Type[Boto3ClientError]
    IndexNotFoundException: Type[Boto3ClientError]
    InternalServerError: Type[Boto3ClientError]
    InvalidRestoreTimeException: Type[Boto3ClientError]
    ItemCollectionSizeLimitExceededException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    PointInTimeRecoveryUnavailableException: Type[Boto3ClientError]
    ProvisionedThroughputExceededException: Type[Boto3ClientError]
    ReplicaAlreadyExistsException: Type[Boto3ClientError]
    ReplicaNotFoundException: Type[Boto3ClientError]
    RequestLimitExceeded: Type[Boto3ClientError]
    ResourceInUseException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    TableAlreadyExistsException: Type[Boto3ClientError]
    TableInUseException: Type[Boto3ClientError]
    TableNotFoundException: Type[Boto3ClientError]
    TransactionCanceledException: Type[Boto3ClientError]
    TransactionConflictException: Type[Boto3ClientError]
    TransactionInProgressException: Type[Boto3ClientError]


class DynamoDBClient:
    """
    [DynamoDB.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client)
    """

    exceptions: Exceptions

    def batch_get_item(
        self,
        RequestItems: Dict[str, "KeysAndAttributesTypeDef"],
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
    ) -> BatchGetItemOutputTypeDef:
        """
        [Client.batch_get_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.batch_get_item)
        """

    def batch_write_item(
        self,
        RequestItems: Dict[str, List["WriteRequestTypeDef"]],
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ReturnItemCollectionMetrics: Literal["SIZE", "NONE"] = None,
    ) -> BatchWriteItemOutputTypeDef:
        """
        [Client.batch_write_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.batch_write_item)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.can_paginate)
        """

    def create_backup(self, TableName: str, BackupName: str) -> CreateBackupOutputTypeDef:
        """
        [Client.create_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.create_backup)
        """

    def create_global_table(
        self, GlobalTableName: str, ReplicationGroup: List["ReplicaTypeDef"]
    ) -> CreateGlobalTableOutputTypeDef:
        """
        [Client.create_global_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.create_global_table)
        """

    def create_table(
        self,
        AttributeDefinitions: List["AttributeDefinitionTypeDef"],
        TableName: str,
        KeySchema: List["KeySchemaElementTypeDef"],
        LocalSecondaryIndexes: List[LocalSecondaryIndexTypeDef] = None,
        GlobalSecondaryIndexes: List[GlobalSecondaryIndexTypeDef] = None,
        BillingMode: Literal["PROVISIONED", "PAY_PER_REQUEST"] = None,
        ProvisionedThroughput: "ProvisionedThroughputTypeDef" = None,
        StreamSpecification: "StreamSpecificationTypeDef" = None,
        SSESpecification: SSESpecificationTypeDef = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateTableOutputTypeDef:
        """
        [Client.create_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.create_table)
        """

    def delete_backup(self, BackupArn: str) -> DeleteBackupOutputTypeDef:
        """
        [Client.delete_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.delete_backup)
        """

    def delete_item(
        self,
        TableName: str,
        Key: Dict[
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
        Expected: Dict[str, ExpectedAttributeValueTypeDef] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ReturnValues: Literal["NONE", "ALL_OLD", "UPDATED_OLD", "ALL_NEW", "UPDATED_NEW"] = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ReturnItemCollectionMetrics: Literal["SIZE", "NONE"] = None,
        ConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[
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
        ] = None,
    ) -> DeleteItemOutputTypeDef:
        """
        [Client.delete_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.delete_item)
        """

    def delete_table(self, TableName: str) -> DeleteTableOutputTypeDef:
        """
        [Client.delete_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.delete_table)
        """

    def describe_backup(self, BackupArn: str) -> DescribeBackupOutputTypeDef:
        """
        [Client.describe_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.describe_backup)
        """

    def describe_continuous_backups(self, TableName: str) -> DescribeContinuousBackupsOutputTypeDef:
        """
        [Client.describe_continuous_backups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.describe_continuous_backups)
        """

    def describe_contributor_insights(
        self, TableName: str, IndexName: str = None
    ) -> DescribeContributorInsightsOutputTypeDef:
        """
        [Client.describe_contributor_insights documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.describe_contributor_insights)
        """

    def describe_endpoints(self) -> DescribeEndpointsResponseTypeDef:
        """
        [Client.describe_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.describe_endpoints)
        """

    def describe_global_table(self, GlobalTableName: str) -> DescribeGlobalTableOutputTypeDef:
        """
        [Client.describe_global_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.describe_global_table)
        """

    def describe_global_table_settings(
        self, GlobalTableName: str
    ) -> DescribeGlobalTableSettingsOutputTypeDef:
        """
        [Client.describe_global_table_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.describe_global_table_settings)
        """

    def describe_limits(self) -> DescribeLimitsOutputTypeDef:
        """
        [Client.describe_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.describe_limits)
        """

    def describe_table(self, TableName: str) -> DescribeTableOutputTypeDef:
        """
        [Client.describe_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.describe_table)
        """

    def describe_table_replica_auto_scaling(
        self, TableName: str
    ) -> DescribeTableReplicaAutoScalingOutputTypeDef:
        """
        [Client.describe_table_replica_auto_scaling documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.describe_table_replica_auto_scaling)
        """

    def describe_time_to_live(self, TableName: str) -> DescribeTimeToLiveOutputTypeDef:
        """
        [Client.describe_time_to_live documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.describe_time_to_live)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.generate_presigned_url)
        """

    def get_item(
        self,
        TableName: str,
        Key: Dict[
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
        AttributesToGet: List[str] = None,
        ConsistentRead: bool = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ProjectionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
    ) -> GetItemOutputTypeDef:
        """
        [Client.get_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.get_item)
        """

    def list_backups(
        self,
        TableName: str = None,
        Limit: int = None,
        TimeRangeLowerBound: datetime = None,
        TimeRangeUpperBound: datetime = None,
        ExclusiveStartBackupArn: str = None,
        BackupType: Literal["USER", "SYSTEM", "AWS_BACKUP", "ALL"] = None,
    ) -> ListBackupsOutputTypeDef:
        """
        [Client.list_backups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.list_backups)
        """

    def list_contributor_insights(
        self, TableName: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListContributorInsightsOutputTypeDef:
        """
        [Client.list_contributor_insights documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.list_contributor_insights)
        """

    def list_global_tables(
        self, ExclusiveStartGlobalTableName: str = None, Limit: int = None, RegionName: str = None
    ) -> ListGlobalTablesOutputTypeDef:
        """
        [Client.list_global_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.list_global_tables)
        """

    def list_tables(
        self, ExclusiveStartTableName: str = None, Limit: int = None
    ) -> ListTablesOutputTypeDef:
        """
        [Client.list_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.list_tables)
        """

    def list_tags_of_resource(
        self, ResourceArn: str, NextToken: str = None
    ) -> ListTagsOfResourceOutputTypeDef:
        """
        [Client.list_tags_of_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.list_tags_of_resource)
        """

    def put_item(
        self,
        TableName: str,
        Item: Dict[
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
        Expected: Dict[str, ExpectedAttributeValueTypeDef] = None,
        ReturnValues: Literal["NONE", "ALL_OLD", "UPDATED_OLD", "ALL_NEW", "UPDATED_NEW"] = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ReturnItemCollectionMetrics: Literal["SIZE", "NONE"] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[
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
        ] = None,
    ) -> PutItemOutputTypeDef:
        """
        [Client.put_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.put_item)
        """

    def query(
        self,
        TableName: str,
        IndexName: str = None,
        Select: Literal[
            "ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "SPECIFIC_ATTRIBUTES", "COUNT"
        ] = None,
        AttributesToGet: List[str] = None,
        Limit: int = None,
        ConsistentRead: bool = None,
        KeyConditions: Dict[str, ConditionTypeDef] = None,
        QueryFilter: Dict[str, ConditionTypeDef] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ScanIndexForward: bool = None,
        ExclusiveStartKey: Dict[
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
        ] = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ProjectionExpression: str = None,
        FilterExpression: str = None,
        KeyConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[
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
        ] = None,
    ) -> QueryOutputTypeDef:
        """
        [Client.query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.query)
        """

    def restore_table_from_backup(
        self,
        TargetTableName: str,
        BackupArn: str,
        BillingModeOverride: Literal["PROVISIONED", "PAY_PER_REQUEST"] = None,
        GlobalSecondaryIndexOverride: List[GlobalSecondaryIndexTypeDef] = None,
        LocalSecondaryIndexOverride: List[LocalSecondaryIndexTypeDef] = None,
        ProvisionedThroughputOverride: "ProvisionedThroughputTypeDef" = None,
        SSESpecificationOverride: SSESpecificationTypeDef = None,
    ) -> RestoreTableFromBackupOutputTypeDef:
        """
        [Client.restore_table_from_backup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.restore_table_from_backup)
        """

    def restore_table_to_point_in_time(
        self,
        TargetTableName: str,
        SourceTableArn: str = None,
        SourceTableName: str = None,
        UseLatestRestorableTime: bool = None,
        RestoreDateTime: datetime = None,
        BillingModeOverride: Literal["PROVISIONED", "PAY_PER_REQUEST"] = None,
        GlobalSecondaryIndexOverride: List[GlobalSecondaryIndexTypeDef] = None,
        LocalSecondaryIndexOverride: List[LocalSecondaryIndexTypeDef] = None,
        ProvisionedThroughputOverride: "ProvisionedThroughputTypeDef" = None,
        SSESpecificationOverride: SSESpecificationTypeDef = None,
    ) -> RestoreTableToPointInTimeOutputTypeDef:
        """
        [Client.restore_table_to_point_in_time documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.restore_table_to_point_in_time)
        """

    def scan(
        self,
        TableName: str,
        IndexName: str = None,
        AttributesToGet: List[str] = None,
        Limit: int = None,
        Select: Literal[
            "ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "SPECIFIC_ATTRIBUTES", "COUNT"
        ] = None,
        ScanFilter: Dict[str, ConditionTypeDef] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ExclusiveStartKey: Dict[
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
        ] = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        TotalSegments: int = None,
        Segment: int = None,
        ProjectionExpression: str = None,
        FilterExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[
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
        ] = None,
        ConsistentRead: bool = None,
    ) -> ScanOutputTypeDef:
        """
        [Client.scan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.scan)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.tag_resource)
        """

    def transact_get_items(
        self,
        TransactItems: List[TransactGetItemTypeDef],
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
    ) -> TransactGetItemsOutputTypeDef:
        """
        [Client.transact_get_items documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.transact_get_items)
        """

    def transact_write_items(
        self,
        TransactItems: List[TransactWriteItemTypeDef],
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ReturnItemCollectionMetrics: Literal["SIZE", "NONE"] = None,
        ClientRequestToken: str = None,
    ) -> TransactWriteItemsOutputTypeDef:
        """
        [Client.transact_write_items documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.transact_write_items)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.untag_resource)
        """

    def update_continuous_backups(
        self,
        TableName: str,
        PointInTimeRecoverySpecification: PointInTimeRecoverySpecificationTypeDef,
    ) -> UpdateContinuousBackupsOutputTypeDef:
        """
        [Client.update_continuous_backups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.update_continuous_backups)
        """

    def update_contributor_insights(
        self,
        TableName: str,
        ContributorInsightsAction: Literal["ENABLE", "DISABLE"],
        IndexName: str = None,
    ) -> UpdateContributorInsightsOutputTypeDef:
        """
        [Client.update_contributor_insights documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.update_contributor_insights)
        """

    def update_global_table(
        self, GlobalTableName: str, ReplicaUpdates: List[ReplicaUpdateTypeDef]
    ) -> UpdateGlobalTableOutputTypeDef:
        """
        [Client.update_global_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.update_global_table)
        """

    def update_global_table_settings(
        self,
        GlobalTableName: str,
        GlobalTableBillingMode: Literal["PROVISIONED", "PAY_PER_REQUEST"] = None,
        GlobalTableProvisionedWriteCapacityUnits: int = None,
        GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate: "AutoScalingSettingsUpdateTypeDef" = None,
        GlobalTableGlobalSecondaryIndexSettingsUpdate: List[
            GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef
        ] = None,
        ReplicaSettingsUpdate: List[ReplicaSettingsUpdateTypeDef] = None,
    ) -> UpdateGlobalTableSettingsOutputTypeDef:
        """
        [Client.update_global_table_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.update_global_table_settings)
        """

    def update_item(
        self,
        TableName: str,
        Key: Dict[
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
        AttributeUpdates: Dict[str, AttributeValueUpdateTypeDef] = None,
        Expected: Dict[str, ExpectedAttributeValueTypeDef] = None,
        ConditionalOperator: Literal["AND", "OR"] = None,
        ReturnValues: Literal["NONE", "ALL_OLD", "UPDATED_OLD", "ALL_NEW", "UPDATED_NEW"] = None,
        ReturnConsumedCapacity: Literal["INDEXES", "TOTAL", "NONE"] = None,
        ReturnItemCollectionMetrics: Literal["SIZE", "NONE"] = None,
        UpdateExpression: str = None,
        ConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[
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
        ] = None,
    ) -> UpdateItemOutputTypeDef:
        """
        [Client.update_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.update_item)
        """

    def update_table(
        self,
        TableName: str,
        AttributeDefinitions: List["AttributeDefinitionTypeDef"] = None,
        BillingMode: Literal["PROVISIONED", "PAY_PER_REQUEST"] = None,
        ProvisionedThroughput: "ProvisionedThroughputTypeDef" = None,
        GlobalSecondaryIndexUpdates: List[GlobalSecondaryIndexUpdateTypeDef] = None,
        StreamSpecification: "StreamSpecificationTypeDef" = None,
        SSESpecification: SSESpecificationTypeDef = None,
        ReplicaUpdates: List[ReplicationGroupUpdateTypeDef] = None,
    ) -> UpdateTableOutputTypeDef:
        """
        [Client.update_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.update_table)
        """

    def update_table_replica_auto_scaling(
        self,
        TableName: str,
        GlobalSecondaryIndexUpdates: List[GlobalSecondaryIndexAutoScalingUpdateTypeDef] = None,
        ProvisionedWriteCapacityAutoScalingUpdate: "AutoScalingSettingsUpdateTypeDef" = None,
        ReplicaUpdates: List[ReplicaAutoScalingUpdateTypeDef] = None,
    ) -> UpdateTableReplicaAutoScalingOutputTypeDef:
        """
        [Client.update_table_replica_auto_scaling documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.update_table_replica_auto_scaling)
        """

    def update_time_to_live(
        self, TableName: str, TimeToLiveSpecification: "TimeToLiveSpecificationTypeDef"
    ) -> UpdateTimeToLiveOutputTypeDef:
        """
        [Client.update_time_to_live documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Client.update_time_to_live)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_backups"]) -> ListBackupsPaginator:
        """
        [Paginator.ListBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Paginator.ListBackups)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tables"]) -> ListTablesPaginator:
        """
        [Paginator.ListTables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Paginator.ListTables)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_of_resource"]
    ) -> ListTagsOfResourcePaginator:
        """
        [Paginator.ListTagsOfResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Paginator.ListTagsOfResource)
        """

    @overload
    def get_paginator(self, operation_name: Literal["query"]) -> QueryPaginator:
        """
        [Paginator.Query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Paginator.Query)
        """

    @overload
    def get_paginator(self, operation_name: Literal["scan"]) -> ScanPaginator:
        """
        [Paginator.Scan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Paginator.Scan)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass

    @overload
    def get_waiter(self, waiter_name: Literal["table_exists"]) -> TableExistsWaiter:
        """
        [Waiter.TableExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Waiter.TableExists)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["table_not_exists"]) -> TableNotExistsWaiter:
        """
        [Waiter.TableNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodb.html#DynamoDB.Waiter.TableNotExists)
        """

    def get_waiter(self, waiter_name: str) -> Boto3Waiter:
        pass
