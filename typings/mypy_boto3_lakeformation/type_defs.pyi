"""
Type annotations for lakeformation service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lakeformation.type_defs import AddLFTagsToResourceRequestRequestTypeDef

    data: AddLFTagsToResourceRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ComparisonOperatorType,
    DataLakeResourceTypeType,
    FieldNameStringType,
    OptimizerTypeType,
    PermissionType,
    PermissionTypeType,
    QueryStateStringType,
    ResourceShareTypeType,
    ResourceTypeType,
    TransactionStatusFilterType,
    TransactionStatusType,
    TransactionTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AddLFTagsToResourceRequestRequestTypeDef",
    "AddLFTagsToResourceResponseTypeDef",
    "AddObjectInputTypeDef",
    "AssumeDecoratedRoleWithSAMLRequestRequestTypeDef",
    "AssumeDecoratedRoleWithSAMLResponseTypeDef",
    "AuditContextTypeDef",
    "BatchGrantPermissionsRequestRequestTypeDef",
    "BatchGrantPermissionsResponseTypeDef",
    "BatchPermissionsFailureEntryTypeDef",
    "BatchPermissionsRequestEntryTypeDef",
    "BatchRevokePermissionsRequestRequestTypeDef",
    "BatchRevokePermissionsResponseTypeDef",
    "CancelTransactionRequestRequestTypeDef",
    "ColumnLFTagTypeDef",
    "ColumnWildcardTypeDef",
    "CommitTransactionRequestRequestTypeDef",
    "CommitTransactionResponseTypeDef",
    "CreateDataCellsFilterRequestRequestTypeDef",
    "CreateLFTagRequestRequestTypeDef",
    "DataCellsFilterResourceTypeDef",
    "DataCellsFilterTypeDef",
    "DataLakePrincipalTypeDef",
    "DataLakeSettingsTypeDef",
    "DataLocationResourceTypeDef",
    "DatabaseResourceTypeDef",
    "DeleteDataCellsFilterRequestRequestTypeDef",
    "DeleteLFTagRequestRequestTypeDef",
    "DeleteObjectInputTypeDef",
    "DeleteObjectsOnCancelRequestRequestTypeDef",
    "DeregisterResourceRequestRequestTypeDef",
    "DescribeResourceRequestRequestTypeDef",
    "DescribeResourceResponseTypeDef",
    "DescribeTransactionRequestRequestTypeDef",
    "DescribeTransactionResponseTypeDef",
    "DetailsMapTypeDef",
    "ErrorDetailTypeDef",
    "ExecutionStatisticsTypeDef",
    "ExtendTransactionRequestRequestTypeDef",
    "FilterConditionTypeDef",
    "GetDataCellsFilterRequestRequestTypeDef",
    "GetDataCellsFilterResponseTypeDef",
    "GetDataLakeSettingsRequestRequestTypeDef",
    "GetDataLakeSettingsResponseTypeDef",
    "GetEffectivePermissionsForPathRequestRequestTypeDef",
    "GetEffectivePermissionsForPathResponseTypeDef",
    "GetLFTagRequestRequestTypeDef",
    "GetLFTagResponseTypeDef",
    "GetQueryStateRequestRequestTypeDef",
    "GetQueryStateResponseTypeDef",
    "GetQueryStatisticsRequestRequestTypeDef",
    "GetQueryStatisticsResponseTypeDef",
    "GetResourceLFTagsRequestRequestTypeDef",
    "GetResourceLFTagsResponseTypeDef",
    "GetTableObjectsRequestRequestTypeDef",
    "GetTableObjectsResponseTypeDef",
    "GetTemporaryGluePartitionCredentialsRequestRequestTypeDef",
    "GetTemporaryGluePartitionCredentialsResponseTypeDef",
    "GetTemporaryGlueTableCredentialsRequestRequestTypeDef",
    "GetTemporaryGlueTableCredentialsResponseTypeDef",
    "GetWorkUnitResultsRequestRequestTypeDef",
    "GetWorkUnitResultsResponseTypeDef",
    "GetWorkUnitsRequestRequestTypeDef",
    "GetWorkUnitsResponseTypeDef",
    "GrantPermissionsRequestRequestTypeDef",
    "LFTagErrorTypeDef",
    "LFTagKeyResourceTypeDef",
    "LFTagPairTypeDef",
    "LFTagPolicyResourceTypeDef",
    "LFTagTypeDef",
    "ListDataCellsFilterRequestRequestTypeDef",
    "ListDataCellsFilterResponseTypeDef",
    "ListLFTagsRequestRequestTypeDef",
    "ListLFTagsResponseTypeDef",
    "ListPermissionsRequestRequestTypeDef",
    "ListPermissionsResponseTypeDef",
    "ListResourcesRequestRequestTypeDef",
    "ListResourcesResponseTypeDef",
    "ListTableStorageOptimizersRequestRequestTypeDef",
    "ListTableStorageOptimizersResponseTypeDef",
    "ListTransactionsRequestRequestTypeDef",
    "ListTransactionsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PartitionObjectsTypeDef",
    "PartitionValueListTypeDef",
    "PlanningStatisticsTypeDef",
    "PrincipalPermissionsTypeDef",
    "PrincipalResourcePermissionsTypeDef",
    "PutDataLakeSettingsRequestRequestTypeDef",
    "QueryPlanningContextTypeDef",
    "RegisterResourceRequestRequestTypeDef",
    "RemoveLFTagsFromResourceRequestRequestTypeDef",
    "RemoveLFTagsFromResourceResponseTypeDef",
    "ResourceInfoTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RevokePermissionsRequestRequestTypeDef",
    "RowFilterTypeDef",
    "SearchDatabasesByLFTagsRequestRequestTypeDef",
    "SearchDatabasesByLFTagsResponseTypeDef",
    "SearchTablesByLFTagsRequestRequestTypeDef",
    "SearchTablesByLFTagsResponseTypeDef",
    "StartQueryPlanningRequestRequestTypeDef",
    "StartQueryPlanningResponseTypeDef",
    "StartTransactionRequestRequestTypeDef",
    "StartTransactionResponseTypeDef",
    "StorageOptimizerTypeDef",
    "TableObjectTypeDef",
    "TableResourceTypeDef",
    "TableWithColumnsResourceTypeDef",
    "TaggedDatabaseTypeDef",
    "TaggedTableTypeDef",
    "TransactionDescriptionTypeDef",
    "UpdateDataCellsFilterRequestRequestTypeDef",
    "UpdateLFTagRequestRequestTypeDef",
    "UpdateResourceRequestRequestTypeDef",
    "UpdateTableObjectsRequestRequestTypeDef",
    "UpdateTableStorageOptimizerRequestRequestTypeDef",
    "UpdateTableStorageOptimizerResponseTypeDef",
    "VirtualObjectTypeDef",
    "WorkUnitRangeTypeDef",
    "WriteOperationTypeDef",
)

_RequiredAddLFTagsToResourceRequestRequestTypeDef = TypedDict(
    "_RequiredAddLFTagsToResourceRequestRequestTypeDef",
    {
        "Resource": "ResourceTypeDef",
        "LFTags": List["LFTagPairTypeDef"],
    },
)
_OptionalAddLFTagsToResourceRequestRequestTypeDef = TypedDict(
    "_OptionalAddLFTagsToResourceRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class AddLFTagsToResourceRequestRequestTypeDef(
    _RequiredAddLFTagsToResourceRequestRequestTypeDef,
    _OptionalAddLFTagsToResourceRequestRequestTypeDef,
):
    pass

AddLFTagsToResourceResponseTypeDef = TypedDict(
    "AddLFTagsToResourceResponseTypeDef",
    {
        "Failures": List["LFTagErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAddObjectInputTypeDef = TypedDict(
    "_RequiredAddObjectInputTypeDef",
    {
        "Uri": str,
        "ETag": str,
        "Size": int,
    },
)
_OptionalAddObjectInputTypeDef = TypedDict(
    "_OptionalAddObjectInputTypeDef",
    {
        "PartitionValues": List[str],
    },
    total=False,
)

class AddObjectInputTypeDef(_RequiredAddObjectInputTypeDef, _OptionalAddObjectInputTypeDef):
    pass

_RequiredAssumeDecoratedRoleWithSAMLRequestRequestTypeDef = TypedDict(
    "_RequiredAssumeDecoratedRoleWithSAMLRequestRequestTypeDef",
    {
        "SAMLAssertion": str,
        "RoleArn": str,
        "PrincipalArn": str,
    },
)
_OptionalAssumeDecoratedRoleWithSAMLRequestRequestTypeDef = TypedDict(
    "_OptionalAssumeDecoratedRoleWithSAMLRequestRequestTypeDef",
    {
        "DurationSeconds": int,
    },
    total=False,
)

class AssumeDecoratedRoleWithSAMLRequestRequestTypeDef(
    _RequiredAssumeDecoratedRoleWithSAMLRequestRequestTypeDef,
    _OptionalAssumeDecoratedRoleWithSAMLRequestRequestTypeDef,
):
    pass

AssumeDecoratedRoleWithSAMLResponseTypeDef = TypedDict(
    "AssumeDecoratedRoleWithSAMLResponseTypeDef",
    {
        "AccessKeyId": str,
        "SecretAccessKey": str,
        "SessionToken": str,
        "Expiration": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AuditContextTypeDef = TypedDict(
    "AuditContextTypeDef",
    {
        "AdditionalAuditContext": str,
    },
    total=False,
)

_RequiredBatchGrantPermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredBatchGrantPermissionsRequestRequestTypeDef",
    {
        "Entries": List["BatchPermissionsRequestEntryTypeDef"],
    },
)
_OptionalBatchGrantPermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalBatchGrantPermissionsRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class BatchGrantPermissionsRequestRequestTypeDef(
    _RequiredBatchGrantPermissionsRequestRequestTypeDef,
    _OptionalBatchGrantPermissionsRequestRequestTypeDef,
):
    pass

BatchGrantPermissionsResponseTypeDef = TypedDict(
    "BatchGrantPermissionsResponseTypeDef",
    {
        "Failures": List["BatchPermissionsFailureEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPermissionsFailureEntryTypeDef = TypedDict(
    "BatchPermissionsFailureEntryTypeDef",
    {
        "RequestEntry": "BatchPermissionsRequestEntryTypeDef",
        "Error": "ErrorDetailTypeDef",
    },
    total=False,
)

_RequiredBatchPermissionsRequestEntryTypeDef = TypedDict(
    "_RequiredBatchPermissionsRequestEntryTypeDef",
    {
        "Id": str,
    },
)
_OptionalBatchPermissionsRequestEntryTypeDef = TypedDict(
    "_OptionalBatchPermissionsRequestEntryTypeDef",
    {
        "Principal": "DataLakePrincipalTypeDef",
        "Resource": "ResourceTypeDef",
        "Permissions": List[PermissionType],
        "PermissionsWithGrantOption": List[PermissionType],
    },
    total=False,
)

class BatchPermissionsRequestEntryTypeDef(
    _RequiredBatchPermissionsRequestEntryTypeDef, _OptionalBatchPermissionsRequestEntryTypeDef
):
    pass

_RequiredBatchRevokePermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredBatchRevokePermissionsRequestRequestTypeDef",
    {
        "Entries": List["BatchPermissionsRequestEntryTypeDef"],
    },
)
_OptionalBatchRevokePermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalBatchRevokePermissionsRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class BatchRevokePermissionsRequestRequestTypeDef(
    _RequiredBatchRevokePermissionsRequestRequestTypeDef,
    _OptionalBatchRevokePermissionsRequestRequestTypeDef,
):
    pass

BatchRevokePermissionsResponseTypeDef = TypedDict(
    "BatchRevokePermissionsResponseTypeDef",
    {
        "Failures": List["BatchPermissionsFailureEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelTransactionRequestRequestTypeDef = TypedDict(
    "CancelTransactionRequestRequestTypeDef",
    {
        "TransactionId": str,
    },
)

ColumnLFTagTypeDef = TypedDict(
    "ColumnLFTagTypeDef",
    {
        "Name": str,
        "LFTags": List["LFTagPairTypeDef"],
    },
    total=False,
)

ColumnWildcardTypeDef = TypedDict(
    "ColumnWildcardTypeDef",
    {
        "ExcludedColumnNames": List[str],
    },
    total=False,
)

CommitTransactionRequestRequestTypeDef = TypedDict(
    "CommitTransactionRequestRequestTypeDef",
    {
        "TransactionId": str,
    },
)

CommitTransactionResponseTypeDef = TypedDict(
    "CommitTransactionResponseTypeDef",
    {
        "TransactionStatus": TransactionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDataCellsFilterRequestRequestTypeDef = TypedDict(
    "CreateDataCellsFilterRequestRequestTypeDef",
    {
        "TableData": "DataCellsFilterTypeDef",
    },
)

_RequiredCreateLFTagRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLFTagRequestRequestTypeDef",
    {
        "TagKey": str,
        "TagValues": List[str],
    },
)
_OptionalCreateLFTagRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLFTagRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class CreateLFTagRequestRequestTypeDef(
    _RequiredCreateLFTagRequestRequestTypeDef, _OptionalCreateLFTagRequestRequestTypeDef
):
    pass

DataCellsFilterResourceTypeDef = TypedDict(
    "DataCellsFilterResourceTypeDef",
    {
        "TableCatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Name": str,
    },
    total=False,
)

_RequiredDataCellsFilterTypeDef = TypedDict(
    "_RequiredDataCellsFilterTypeDef",
    {
        "TableCatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Name": str,
    },
)
_OptionalDataCellsFilterTypeDef = TypedDict(
    "_OptionalDataCellsFilterTypeDef",
    {
        "RowFilter": "RowFilterTypeDef",
        "ColumnNames": List[str],
        "ColumnWildcard": "ColumnWildcardTypeDef",
        "VersionId": str,
    },
    total=False,
)

class DataCellsFilterTypeDef(_RequiredDataCellsFilterTypeDef, _OptionalDataCellsFilterTypeDef):
    pass

DataLakePrincipalTypeDef = TypedDict(
    "DataLakePrincipalTypeDef",
    {
        "DataLakePrincipalIdentifier": str,
    },
    total=False,
)

DataLakeSettingsTypeDef = TypedDict(
    "DataLakeSettingsTypeDef",
    {
        "DataLakeAdmins": List["DataLakePrincipalTypeDef"],
        "CreateDatabaseDefaultPermissions": List["PrincipalPermissionsTypeDef"],
        "CreateTableDefaultPermissions": List["PrincipalPermissionsTypeDef"],
        "Parameters": Dict[str, str],
        "TrustedResourceOwners": List[str],
        "AllowExternalDataFiltering": bool,
        "ExternalDataFilteringAllowList": List["DataLakePrincipalTypeDef"],
        "AuthorizedSessionTagValueList": List[str],
    },
    total=False,
)

_RequiredDataLocationResourceTypeDef = TypedDict(
    "_RequiredDataLocationResourceTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalDataLocationResourceTypeDef = TypedDict(
    "_OptionalDataLocationResourceTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class DataLocationResourceTypeDef(
    _RequiredDataLocationResourceTypeDef, _OptionalDataLocationResourceTypeDef
):
    pass

_RequiredDatabaseResourceTypeDef = TypedDict(
    "_RequiredDatabaseResourceTypeDef",
    {
        "Name": str,
    },
)
_OptionalDatabaseResourceTypeDef = TypedDict(
    "_OptionalDatabaseResourceTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class DatabaseResourceTypeDef(_RequiredDatabaseResourceTypeDef, _OptionalDatabaseResourceTypeDef):
    pass

DeleteDataCellsFilterRequestRequestTypeDef = TypedDict(
    "DeleteDataCellsFilterRequestRequestTypeDef",
    {
        "TableCatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Name": str,
    },
    total=False,
)

_RequiredDeleteLFTagRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteLFTagRequestRequestTypeDef",
    {
        "TagKey": str,
    },
)
_OptionalDeleteLFTagRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteLFTagRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class DeleteLFTagRequestRequestTypeDef(
    _RequiredDeleteLFTagRequestRequestTypeDef, _OptionalDeleteLFTagRequestRequestTypeDef
):
    pass

_RequiredDeleteObjectInputTypeDef = TypedDict(
    "_RequiredDeleteObjectInputTypeDef",
    {
        "Uri": str,
    },
)
_OptionalDeleteObjectInputTypeDef = TypedDict(
    "_OptionalDeleteObjectInputTypeDef",
    {
        "ETag": str,
        "PartitionValues": List[str],
    },
    total=False,
)

class DeleteObjectInputTypeDef(
    _RequiredDeleteObjectInputTypeDef, _OptionalDeleteObjectInputTypeDef
):
    pass

_RequiredDeleteObjectsOnCancelRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteObjectsOnCancelRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "TransactionId": str,
        "Objects": List["VirtualObjectTypeDef"],
    },
)
_OptionalDeleteObjectsOnCancelRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteObjectsOnCancelRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class DeleteObjectsOnCancelRequestRequestTypeDef(
    _RequiredDeleteObjectsOnCancelRequestRequestTypeDef,
    _OptionalDeleteObjectsOnCancelRequestRequestTypeDef,
):
    pass

DeregisterResourceRequestRequestTypeDef = TypedDict(
    "DeregisterResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DescribeResourceRequestRequestTypeDef = TypedDict(
    "DescribeResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DescribeResourceResponseTypeDef = TypedDict(
    "DescribeResourceResponseTypeDef",
    {
        "ResourceInfo": "ResourceInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransactionRequestRequestTypeDef = TypedDict(
    "DescribeTransactionRequestRequestTypeDef",
    {
        "TransactionId": str,
    },
)

DescribeTransactionResponseTypeDef = TypedDict(
    "DescribeTransactionResponseTypeDef",
    {
        "TransactionDescription": "TransactionDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetailsMapTypeDef = TypedDict(
    "DetailsMapTypeDef",
    {
        "ResourceShare": List[str],
    },
    total=False,
)

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

ExecutionStatisticsTypeDef = TypedDict(
    "ExecutionStatisticsTypeDef",
    {
        "AverageExecutionTimeMillis": int,
        "DataScannedBytes": int,
        "WorkUnitsExecutedCount": int,
    },
    total=False,
)

ExtendTransactionRequestRequestTypeDef = TypedDict(
    "ExtendTransactionRequestRequestTypeDef",
    {
        "TransactionId": str,
    },
    total=False,
)

FilterConditionTypeDef = TypedDict(
    "FilterConditionTypeDef",
    {
        "Field": FieldNameStringType,
        "ComparisonOperator": ComparisonOperatorType,
        "StringValueList": List[str],
    },
    total=False,
)

GetDataCellsFilterRequestRequestTypeDef = TypedDict(
    "GetDataCellsFilterRequestRequestTypeDef",
    {
        "TableCatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Name": str,
    },
)

GetDataCellsFilterResponseTypeDef = TypedDict(
    "GetDataCellsFilterResponseTypeDef",
    {
        "DataCellsFilter": "DataCellsFilterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataLakeSettingsRequestRequestTypeDef = TypedDict(
    "GetDataLakeSettingsRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

GetDataLakeSettingsResponseTypeDef = TypedDict(
    "GetDataLakeSettingsResponseTypeDef",
    {
        "DataLakeSettings": "DataLakeSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetEffectivePermissionsForPathRequestRequestTypeDef = TypedDict(
    "_RequiredGetEffectivePermissionsForPathRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalGetEffectivePermissionsForPathRequestRequestTypeDef = TypedDict(
    "_OptionalGetEffectivePermissionsForPathRequestRequestTypeDef",
    {
        "CatalogId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetEffectivePermissionsForPathRequestRequestTypeDef(
    _RequiredGetEffectivePermissionsForPathRequestRequestTypeDef,
    _OptionalGetEffectivePermissionsForPathRequestRequestTypeDef,
):
    pass

GetEffectivePermissionsForPathResponseTypeDef = TypedDict(
    "GetEffectivePermissionsForPathResponseTypeDef",
    {
        "Permissions": List["PrincipalResourcePermissionsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLFTagRequestRequestTypeDef = TypedDict(
    "_RequiredGetLFTagRequestRequestTypeDef",
    {
        "TagKey": str,
    },
)
_OptionalGetLFTagRequestRequestTypeDef = TypedDict(
    "_OptionalGetLFTagRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class GetLFTagRequestRequestTypeDef(
    _RequiredGetLFTagRequestRequestTypeDef, _OptionalGetLFTagRequestRequestTypeDef
):
    pass

GetLFTagResponseTypeDef = TypedDict(
    "GetLFTagResponseTypeDef",
    {
        "CatalogId": str,
        "TagKey": str,
        "TagValues": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueryStateRequestRequestTypeDef = TypedDict(
    "GetQueryStateRequestRequestTypeDef",
    {
        "QueryId": str,
    },
)

GetQueryStateResponseTypeDef = TypedDict(
    "GetQueryStateResponseTypeDef",
    {
        "Error": str,
        "State": QueryStateStringType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueryStatisticsRequestRequestTypeDef = TypedDict(
    "GetQueryStatisticsRequestRequestTypeDef",
    {
        "QueryId": str,
    },
)

GetQueryStatisticsResponseTypeDef = TypedDict(
    "GetQueryStatisticsResponseTypeDef",
    {
        "ExecutionStatistics": "ExecutionStatisticsTypeDef",
        "PlanningStatistics": "PlanningStatisticsTypeDef",
        "QuerySubmissionTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetResourceLFTagsRequestRequestTypeDef = TypedDict(
    "_RequiredGetResourceLFTagsRequestRequestTypeDef",
    {
        "Resource": "ResourceTypeDef",
    },
)
_OptionalGetResourceLFTagsRequestRequestTypeDef = TypedDict(
    "_OptionalGetResourceLFTagsRequestRequestTypeDef",
    {
        "CatalogId": str,
        "ShowAssignedLFTags": bool,
    },
    total=False,
)

class GetResourceLFTagsRequestRequestTypeDef(
    _RequiredGetResourceLFTagsRequestRequestTypeDef, _OptionalGetResourceLFTagsRequestRequestTypeDef
):
    pass

GetResourceLFTagsResponseTypeDef = TypedDict(
    "GetResourceLFTagsResponseTypeDef",
    {
        "LFTagOnDatabase": List["LFTagPairTypeDef"],
        "LFTagsOnTable": List["LFTagPairTypeDef"],
        "LFTagsOnColumns": List["ColumnLFTagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTableObjectsRequestRequestTypeDef = TypedDict(
    "_RequiredGetTableObjectsRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
_OptionalGetTableObjectsRequestRequestTypeDef = TypedDict(
    "_OptionalGetTableObjectsRequestRequestTypeDef",
    {
        "CatalogId": str,
        "TransactionId": str,
        "QueryAsOfTime": Union[datetime, str],
        "PartitionPredicate": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetTableObjectsRequestRequestTypeDef(
    _RequiredGetTableObjectsRequestRequestTypeDef, _OptionalGetTableObjectsRequestRequestTypeDef
):
    pass

GetTableObjectsResponseTypeDef = TypedDict(
    "GetTableObjectsResponseTypeDef",
    {
        "Objects": List["PartitionObjectsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTemporaryGluePartitionCredentialsRequestRequestTypeDef = TypedDict(
    "_RequiredGetTemporaryGluePartitionCredentialsRequestRequestTypeDef",
    {
        "TableArn": str,
        "Partition": "PartitionValueListTypeDef",
        "SupportedPermissionTypes": List[PermissionTypeType],
    },
)
_OptionalGetTemporaryGluePartitionCredentialsRequestRequestTypeDef = TypedDict(
    "_OptionalGetTemporaryGluePartitionCredentialsRequestRequestTypeDef",
    {
        "Permissions": List[PermissionType],
        "DurationSeconds": int,
        "AuditContext": "AuditContextTypeDef",
    },
    total=False,
)

class GetTemporaryGluePartitionCredentialsRequestRequestTypeDef(
    _RequiredGetTemporaryGluePartitionCredentialsRequestRequestTypeDef,
    _OptionalGetTemporaryGluePartitionCredentialsRequestRequestTypeDef,
):
    pass

GetTemporaryGluePartitionCredentialsResponseTypeDef = TypedDict(
    "GetTemporaryGluePartitionCredentialsResponseTypeDef",
    {
        "AccessKeyId": str,
        "SecretAccessKey": str,
        "SessionToken": str,
        "Expiration": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTemporaryGlueTableCredentialsRequestRequestTypeDef = TypedDict(
    "_RequiredGetTemporaryGlueTableCredentialsRequestRequestTypeDef",
    {
        "TableArn": str,
        "SupportedPermissionTypes": List[PermissionTypeType],
    },
)
_OptionalGetTemporaryGlueTableCredentialsRequestRequestTypeDef = TypedDict(
    "_OptionalGetTemporaryGlueTableCredentialsRequestRequestTypeDef",
    {
        "Permissions": List[PermissionType],
        "DurationSeconds": int,
        "AuditContext": "AuditContextTypeDef",
    },
    total=False,
)

class GetTemporaryGlueTableCredentialsRequestRequestTypeDef(
    _RequiredGetTemporaryGlueTableCredentialsRequestRequestTypeDef,
    _OptionalGetTemporaryGlueTableCredentialsRequestRequestTypeDef,
):
    pass

GetTemporaryGlueTableCredentialsResponseTypeDef = TypedDict(
    "GetTemporaryGlueTableCredentialsResponseTypeDef",
    {
        "AccessKeyId": str,
        "SecretAccessKey": str,
        "SessionToken": str,
        "Expiration": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkUnitResultsRequestRequestTypeDef = TypedDict(
    "GetWorkUnitResultsRequestRequestTypeDef",
    {
        "QueryId": str,
        "WorkUnitId": int,
        "WorkUnitToken": str,
    },
)

GetWorkUnitResultsResponseTypeDef = TypedDict(
    "GetWorkUnitResultsResponseTypeDef",
    {
        "ResultStream": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetWorkUnitsRequestRequestTypeDef = TypedDict(
    "_RequiredGetWorkUnitsRequestRequestTypeDef",
    {
        "QueryId": str,
    },
)
_OptionalGetWorkUnitsRequestRequestTypeDef = TypedDict(
    "_OptionalGetWorkUnitsRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

class GetWorkUnitsRequestRequestTypeDef(
    _RequiredGetWorkUnitsRequestRequestTypeDef, _OptionalGetWorkUnitsRequestRequestTypeDef
):
    pass

GetWorkUnitsResponseTypeDef = TypedDict(
    "GetWorkUnitsResponseTypeDef",
    {
        "NextToken": str,
        "QueryId": str,
        "WorkUnitRanges": List["WorkUnitRangeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGrantPermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredGrantPermissionsRequestRequestTypeDef",
    {
        "Principal": "DataLakePrincipalTypeDef",
        "Resource": "ResourceTypeDef",
        "Permissions": List[PermissionType],
    },
)
_OptionalGrantPermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalGrantPermissionsRequestRequestTypeDef",
    {
        "CatalogId": str,
        "PermissionsWithGrantOption": List[PermissionType],
    },
    total=False,
)

class GrantPermissionsRequestRequestTypeDef(
    _RequiredGrantPermissionsRequestRequestTypeDef, _OptionalGrantPermissionsRequestRequestTypeDef
):
    pass

LFTagErrorTypeDef = TypedDict(
    "LFTagErrorTypeDef",
    {
        "LFTag": "LFTagPairTypeDef",
        "Error": "ErrorDetailTypeDef",
    },
    total=False,
)

_RequiredLFTagKeyResourceTypeDef = TypedDict(
    "_RequiredLFTagKeyResourceTypeDef",
    {
        "TagKey": str,
        "TagValues": List[str],
    },
)
_OptionalLFTagKeyResourceTypeDef = TypedDict(
    "_OptionalLFTagKeyResourceTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class LFTagKeyResourceTypeDef(_RequiredLFTagKeyResourceTypeDef, _OptionalLFTagKeyResourceTypeDef):
    pass

_RequiredLFTagPairTypeDef = TypedDict(
    "_RequiredLFTagPairTypeDef",
    {
        "TagKey": str,
        "TagValues": List[str],
    },
)
_OptionalLFTagPairTypeDef = TypedDict(
    "_OptionalLFTagPairTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class LFTagPairTypeDef(_RequiredLFTagPairTypeDef, _OptionalLFTagPairTypeDef):
    pass

_RequiredLFTagPolicyResourceTypeDef = TypedDict(
    "_RequiredLFTagPolicyResourceTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "Expression": List["LFTagTypeDef"],
    },
)
_OptionalLFTagPolicyResourceTypeDef = TypedDict(
    "_OptionalLFTagPolicyResourceTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class LFTagPolicyResourceTypeDef(
    _RequiredLFTagPolicyResourceTypeDef, _OptionalLFTagPolicyResourceTypeDef
):
    pass

LFTagTypeDef = TypedDict(
    "LFTagTypeDef",
    {
        "TagKey": str,
        "TagValues": List[str],
    },
)

ListDataCellsFilterRequestRequestTypeDef = TypedDict(
    "ListDataCellsFilterRequestRequestTypeDef",
    {
        "Table": "TableResourceTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDataCellsFilterResponseTypeDef = TypedDict(
    "ListDataCellsFilterResponseTypeDef",
    {
        "DataCellsFilters": List["DataCellsFilterTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLFTagsRequestRequestTypeDef = TypedDict(
    "ListLFTagsRequestRequestTypeDef",
    {
        "CatalogId": str,
        "ResourceShareType": ResourceShareTypeType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListLFTagsResponseTypeDef = TypedDict(
    "ListLFTagsResponseTypeDef",
    {
        "LFTags": List["LFTagPairTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPermissionsRequestRequestTypeDef = TypedDict(
    "ListPermissionsRequestRequestTypeDef",
    {
        "CatalogId": str,
        "Principal": "DataLakePrincipalTypeDef",
        "ResourceType": DataLakeResourceTypeType,
        "Resource": "ResourceTypeDef",
        "NextToken": str,
        "MaxResults": int,
        "IncludeRelated": str,
    },
    total=False,
)

ListPermissionsResponseTypeDef = TypedDict(
    "ListPermissionsResponseTypeDef",
    {
        "PrincipalResourcePermissions": List["PrincipalResourcePermissionsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourcesRequestRequestTypeDef = TypedDict(
    "ListResourcesRequestRequestTypeDef",
    {
        "FilterConditionList": List["FilterConditionTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListResourcesResponseTypeDef = TypedDict(
    "ListResourcesResponseTypeDef",
    {
        "ResourceInfoList": List["ResourceInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTableStorageOptimizersRequestRequestTypeDef = TypedDict(
    "_RequiredListTableStorageOptimizersRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
_OptionalListTableStorageOptimizersRequestRequestTypeDef = TypedDict(
    "_OptionalListTableStorageOptimizersRequestRequestTypeDef",
    {
        "CatalogId": str,
        "StorageOptimizerType": OptimizerTypeType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListTableStorageOptimizersRequestRequestTypeDef(
    _RequiredListTableStorageOptimizersRequestRequestTypeDef,
    _OptionalListTableStorageOptimizersRequestRequestTypeDef,
):
    pass

ListTableStorageOptimizersResponseTypeDef = TypedDict(
    "ListTableStorageOptimizersResponseTypeDef",
    {
        "StorageOptimizerList": List["StorageOptimizerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTransactionsRequestRequestTypeDef = TypedDict(
    "ListTransactionsRequestRequestTypeDef",
    {
        "CatalogId": str,
        "StatusFilter": TransactionStatusFilterType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListTransactionsResponseTypeDef = TypedDict(
    "ListTransactionsResponseTypeDef",
    {
        "Transactions": List["TransactionDescriptionTypeDef"],
        "NextToken": str,
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

PartitionObjectsTypeDef = TypedDict(
    "PartitionObjectsTypeDef",
    {
        "PartitionValues": List[str],
        "Objects": List["TableObjectTypeDef"],
    },
    total=False,
)

PartitionValueListTypeDef = TypedDict(
    "PartitionValueListTypeDef",
    {
        "Values": List[str],
    },
)

PlanningStatisticsTypeDef = TypedDict(
    "PlanningStatisticsTypeDef",
    {
        "EstimatedDataToScanBytes": int,
        "PlanningTimeMillis": int,
        "QueueTimeMillis": int,
        "WorkUnitsGeneratedCount": int,
    },
    total=False,
)

PrincipalPermissionsTypeDef = TypedDict(
    "PrincipalPermissionsTypeDef",
    {
        "Principal": "DataLakePrincipalTypeDef",
        "Permissions": List[PermissionType],
    },
    total=False,
)

PrincipalResourcePermissionsTypeDef = TypedDict(
    "PrincipalResourcePermissionsTypeDef",
    {
        "Principal": "DataLakePrincipalTypeDef",
        "Resource": "ResourceTypeDef",
        "Permissions": List[PermissionType],
        "PermissionsWithGrantOption": List[PermissionType],
        "AdditionalDetails": "DetailsMapTypeDef",
    },
    total=False,
)

_RequiredPutDataLakeSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredPutDataLakeSettingsRequestRequestTypeDef",
    {
        "DataLakeSettings": "DataLakeSettingsTypeDef",
    },
)
_OptionalPutDataLakeSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalPutDataLakeSettingsRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class PutDataLakeSettingsRequestRequestTypeDef(
    _RequiredPutDataLakeSettingsRequestRequestTypeDef,
    _OptionalPutDataLakeSettingsRequestRequestTypeDef,
):
    pass

_RequiredQueryPlanningContextTypeDef = TypedDict(
    "_RequiredQueryPlanningContextTypeDef",
    {
        "DatabaseName": str,
    },
)
_OptionalQueryPlanningContextTypeDef = TypedDict(
    "_OptionalQueryPlanningContextTypeDef",
    {
        "CatalogId": str,
        "QueryAsOfTime": Union[datetime, str],
        "QueryParameters": Dict[str, str],
        "TransactionId": str,
    },
    total=False,
)

class QueryPlanningContextTypeDef(
    _RequiredQueryPlanningContextTypeDef, _OptionalQueryPlanningContextTypeDef
):
    pass

_RequiredRegisterResourceRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalRegisterResourceRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterResourceRequestRequestTypeDef",
    {
        "UseServiceLinkedRole": bool,
        "RoleArn": str,
        "WithFederation": bool,
    },
    total=False,
)

class RegisterResourceRequestRequestTypeDef(
    _RequiredRegisterResourceRequestRequestTypeDef, _OptionalRegisterResourceRequestRequestTypeDef
):
    pass

_RequiredRemoveLFTagsFromResourceRequestRequestTypeDef = TypedDict(
    "_RequiredRemoveLFTagsFromResourceRequestRequestTypeDef",
    {
        "Resource": "ResourceTypeDef",
        "LFTags": List["LFTagPairTypeDef"],
    },
)
_OptionalRemoveLFTagsFromResourceRequestRequestTypeDef = TypedDict(
    "_OptionalRemoveLFTagsFromResourceRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class RemoveLFTagsFromResourceRequestRequestTypeDef(
    _RequiredRemoveLFTagsFromResourceRequestRequestTypeDef,
    _OptionalRemoveLFTagsFromResourceRequestRequestTypeDef,
):
    pass

RemoveLFTagsFromResourceResponseTypeDef = TypedDict(
    "RemoveLFTagsFromResourceResponseTypeDef",
    {
        "Failures": List["LFTagErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceInfoTypeDef = TypedDict(
    "ResourceInfoTypeDef",
    {
        "ResourceArn": str,
        "RoleArn": str,
        "LastModified": datetime,
        "WithFederation": bool,
    },
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "Catalog": Dict[str, Any],
        "Database": "DatabaseResourceTypeDef",
        "Table": "TableResourceTypeDef",
        "TableWithColumns": "TableWithColumnsResourceTypeDef",
        "DataLocation": "DataLocationResourceTypeDef",
        "DataCellsFilter": "DataCellsFilterResourceTypeDef",
        "LFTag": "LFTagKeyResourceTypeDef",
        "LFTagPolicy": "LFTagPolicyResourceTypeDef",
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

_RequiredRevokePermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredRevokePermissionsRequestRequestTypeDef",
    {
        "Principal": "DataLakePrincipalTypeDef",
        "Resource": "ResourceTypeDef",
        "Permissions": List[PermissionType],
    },
)
_OptionalRevokePermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalRevokePermissionsRequestRequestTypeDef",
    {
        "CatalogId": str,
        "PermissionsWithGrantOption": List[PermissionType],
    },
    total=False,
)

class RevokePermissionsRequestRequestTypeDef(
    _RequiredRevokePermissionsRequestRequestTypeDef, _OptionalRevokePermissionsRequestRequestTypeDef
):
    pass

RowFilterTypeDef = TypedDict(
    "RowFilterTypeDef",
    {
        "FilterExpression": str,
        "AllRowsWildcard": Dict[str, Any],
    },
    total=False,
)

_RequiredSearchDatabasesByLFTagsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchDatabasesByLFTagsRequestRequestTypeDef",
    {
        "Expression": List["LFTagTypeDef"],
    },
)
_OptionalSearchDatabasesByLFTagsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchDatabasesByLFTagsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "CatalogId": str,
    },
    total=False,
)

class SearchDatabasesByLFTagsRequestRequestTypeDef(
    _RequiredSearchDatabasesByLFTagsRequestRequestTypeDef,
    _OptionalSearchDatabasesByLFTagsRequestRequestTypeDef,
):
    pass

SearchDatabasesByLFTagsResponseTypeDef = TypedDict(
    "SearchDatabasesByLFTagsResponseTypeDef",
    {
        "NextToken": str,
        "DatabaseList": List["TaggedDatabaseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchTablesByLFTagsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchTablesByLFTagsRequestRequestTypeDef",
    {
        "Expression": List["LFTagTypeDef"],
    },
)
_OptionalSearchTablesByLFTagsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchTablesByLFTagsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "CatalogId": str,
    },
    total=False,
)

class SearchTablesByLFTagsRequestRequestTypeDef(
    _RequiredSearchTablesByLFTagsRequestRequestTypeDef,
    _OptionalSearchTablesByLFTagsRequestRequestTypeDef,
):
    pass

SearchTablesByLFTagsResponseTypeDef = TypedDict(
    "SearchTablesByLFTagsResponseTypeDef",
    {
        "NextToken": str,
        "TableList": List["TaggedTableTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartQueryPlanningRequestRequestTypeDef = TypedDict(
    "StartQueryPlanningRequestRequestTypeDef",
    {
        "QueryPlanningContext": "QueryPlanningContextTypeDef",
        "QueryString": str,
    },
)

StartQueryPlanningResponseTypeDef = TypedDict(
    "StartQueryPlanningResponseTypeDef",
    {
        "QueryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartTransactionRequestRequestTypeDef = TypedDict(
    "StartTransactionRequestRequestTypeDef",
    {
        "TransactionType": TransactionTypeType,
    },
    total=False,
)

StartTransactionResponseTypeDef = TypedDict(
    "StartTransactionResponseTypeDef",
    {
        "TransactionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StorageOptimizerTypeDef = TypedDict(
    "StorageOptimizerTypeDef",
    {
        "StorageOptimizerType": OptimizerTypeType,
        "Config": Dict[str, str],
        "ErrorMessage": str,
        "Warnings": str,
        "LastRunDetails": str,
    },
    total=False,
)

TableObjectTypeDef = TypedDict(
    "TableObjectTypeDef",
    {
        "Uri": str,
        "ETag": str,
        "Size": int,
    },
    total=False,
)

_RequiredTableResourceTypeDef = TypedDict(
    "_RequiredTableResourceTypeDef",
    {
        "DatabaseName": str,
    },
)
_OptionalTableResourceTypeDef = TypedDict(
    "_OptionalTableResourceTypeDef",
    {
        "CatalogId": str,
        "Name": str,
        "TableWildcard": Dict[str, Any],
    },
    total=False,
)

class TableResourceTypeDef(_RequiredTableResourceTypeDef, _OptionalTableResourceTypeDef):
    pass

_RequiredTableWithColumnsResourceTypeDef = TypedDict(
    "_RequiredTableWithColumnsResourceTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
    },
)
_OptionalTableWithColumnsResourceTypeDef = TypedDict(
    "_OptionalTableWithColumnsResourceTypeDef",
    {
        "CatalogId": str,
        "ColumnNames": List[str],
        "ColumnWildcard": "ColumnWildcardTypeDef",
    },
    total=False,
)

class TableWithColumnsResourceTypeDef(
    _RequiredTableWithColumnsResourceTypeDef, _OptionalTableWithColumnsResourceTypeDef
):
    pass

TaggedDatabaseTypeDef = TypedDict(
    "TaggedDatabaseTypeDef",
    {
        "Database": "DatabaseResourceTypeDef",
        "LFTags": List["LFTagPairTypeDef"],
    },
    total=False,
)

TaggedTableTypeDef = TypedDict(
    "TaggedTableTypeDef",
    {
        "Table": "TableResourceTypeDef",
        "LFTagOnDatabase": List["LFTagPairTypeDef"],
        "LFTagsOnTable": List["LFTagPairTypeDef"],
        "LFTagsOnColumns": List["ColumnLFTagTypeDef"],
    },
    total=False,
)

TransactionDescriptionTypeDef = TypedDict(
    "TransactionDescriptionTypeDef",
    {
        "TransactionId": str,
        "TransactionStatus": TransactionStatusType,
        "TransactionStartTime": datetime,
        "TransactionEndTime": datetime,
    },
    total=False,
)

UpdateDataCellsFilterRequestRequestTypeDef = TypedDict(
    "UpdateDataCellsFilterRequestRequestTypeDef",
    {
        "TableData": "DataCellsFilterTypeDef",
    },
)

_RequiredUpdateLFTagRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLFTagRequestRequestTypeDef",
    {
        "TagKey": str,
    },
)
_OptionalUpdateLFTagRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLFTagRequestRequestTypeDef",
    {
        "CatalogId": str,
        "TagValuesToDelete": List[str],
        "TagValuesToAdd": List[str],
    },
    total=False,
)

class UpdateLFTagRequestRequestTypeDef(
    _RequiredUpdateLFTagRequestRequestTypeDef, _OptionalUpdateLFTagRequestRequestTypeDef
):
    pass

_RequiredUpdateResourceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateResourceRequestRequestTypeDef",
    {
        "RoleArn": str,
        "ResourceArn": str,
    },
)
_OptionalUpdateResourceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateResourceRequestRequestTypeDef",
    {
        "WithFederation": bool,
    },
    total=False,
)

class UpdateResourceRequestRequestTypeDef(
    _RequiredUpdateResourceRequestRequestTypeDef, _OptionalUpdateResourceRequestRequestTypeDef
):
    pass

_RequiredUpdateTableObjectsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTableObjectsRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "WriteOperations": List["WriteOperationTypeDef"],
    },
)
_OptionalUpdateTableObjectsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTableObjectsRequestRequestTypeDef",
    {
        "CatalogId": str,
        "TransactionId": str,
    },
    total=False,
)

class UpdateTableObjectsRequestRequestTypeDef(
    _RequiredUpdateTableObjectsRequestRequestTypeDef,
    _OptionalUpdateTableObjectsRequestRequestTypeDef,
):
    pass

_RequiredUpdateTableStorageOptimizerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTableStorageOptimizerRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "StorageOptimizerConfig": Dict[OptimizerTypeType, Dict[str, str]],
    },
)
_OptionalUpdateTableStorageOptimizerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTableStorageOptimizerRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class UpdateTableStorageOptimizerRequestRequestTypeDef(
    _RequiredUpdateTableStorageOptimizerRequestRequestTypeDef,
    _OptionalUpdateTableStorageOptimizerRequestRequestTypeDef,
):
    pass

UpdateTableStorageOptimizerResponseTypeDef = TypedDict(
    "UpdateTableStorageOptimizerResponseTypeDef",
    {
        "Result": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredVirtualObjectTypeDef = TypedDict(
    "_RequiredVirtualObjectTypeDef",
    {
        "Uri": str,
    },
)
_OptionalVirtualObjectTypeDef = TypedDict(
    "_OptionalVirtualObjectTypeDef",
    {
        "ETag": str,
    },
    total=False,
)

class VirtualObjectTypeDef(_RequiredVirtualObjectTypeDef, _OptionalVirtualObjectTypeDef):
    pass

WorkUnitRangeTypeDef = TypedDict(
    "WorkUnitRangeTypeDef",
    {
        "WorkUnitIdMax": int,
        "WorkUnitIdMin": int,
        "WorkUnitToken": str,
    },
)

WriteOperationTypeDef = TypedDict(
    "WriteOperationTypeDef",
    {
        "AddObject": "AddObjectInputTypeDef",
        "DeleteObject": "DeleteObjectInputTypeDef",
    },
    total=False,
)
