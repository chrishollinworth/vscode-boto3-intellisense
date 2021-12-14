"""
Type annotations for finspace-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_finspace_data.type_defs import ChangesetErrorInfoTypeDef

    data: ChangesetErrorInfoTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    ChangeTypeType,
    ColumnDataTypeType,
    DatasetKindType,
    DatasetStatusType,
    DataViewStatusType,
    ErrorCategoryType,
    IngestionStatusType,
    locationTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ChangesetErrorInfoTypeDef",
    "ChangesetSummaryTypeDef",
    "ColumnDefinitionTypeDef",
    "CreateChangesetRequestRequestTypeDef",
    "CreateChangesetResponseTypeDef",
    "CreateDataViewRequestRequestTypeDef",
    "CreateDataViewResponseTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CredentialsTypeDef",
    "DataViewDestinationTypeParamsTypeDef",
    "DataViewErrorInfoTypeDef",
    "DataViewSummaryTypeDef",
    "DatasetOwnerInfoTypeDef",
    "DatasetTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteDatasetResponseTypeDef",
    "GetChangesetRequestRequestTypeDef",
    "GetChangesetResponseTypeDef",
    "GetDataViewRequestRequestTypeDef",
    "GetDataViewResponseTypeDef",
    "GetDatasetRequestRequestTypeDef",
    "GetDatasetResponseTypeDef",
    "GetProgrammaticAccessCredentialsRequestRequestTypeDef",
    "GetProgrammaticAccessCredentialsResponseTypeDef",
    "GetWorkingLocationRequestRequestTypeDef",
    "GetWorkingLocationResponseTypeDef",
    "ListChangesetsRequestRequestTypeDef",
    "ListChangesetsResponseTypeDef",
    "ListDataViewsRequestRequestTypeDef",
    "ListDataViewsResponseTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListDatasetsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionGroupParamsTypeDef",
    "ResourcePermissionTypeDef",
    "ResponseMetadataTypeDef",
    "SchemaDefinitionTypeDef",
    "SchemaUnionTypeDef",
    "UpdateChangesetRequestRequestTypeDef",
    "UpdateChangesetResponseTypeDef",
    "UpdateDatasetRequestRequestTypeDef",
    "UpdateDatasetResponseTypeDef",
)

ChangesetErrorInfoTypeDef = TypedDict(
    "ChangesetErrorInfoTypeDef",
    {
        "errorMessage": str,
        "errorCategory": ErrorCategoryType,
    },
    total=False,
)

ChangesetSummaryTypeDef = TypedDict(
    "ChangesetSummaryTypeDef",
    {
        "changesetId": str,
        "changesetArn": str,
        "datasetId": str,
        "changeType": ChangeTypeType,
        "sourceParams": Dict[str, str],
        "formatParams": Dict[str, str],
        "createTime": int,
        "status": IngestionStatusType,
        "errorInfo": "ChangesetErrorInfoTypeDef",
        "activeUntilTimestamp": int,
        "updatesChangesetId": str,
        "updatedByChangesetId": str,
    },
    total=False,
)

ColumnDefinitionTypeDef = TypedDict(
    "ColumnDefinitionTypeDef",
    {
        "dataType": ColumnDataTypeType,
        "columnName": str,
        "columnDescription": str,
    },
    total=False,
)

_RequiredCreateChangesetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateChangesetRequestRequestTypeDef",
    {
        "datasetId": str,
        "changeType": ChangeTypeType,
        "sourceParams": Dict[str, str],
        "formatParams": Dict[str, str],
    },
)
_OptionalCreateChangesetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateChangesetRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateChangesetRequestRequestTypeDef(
    _RequiredCreateChangesetRequestRequestTypeDef, _OptionalCreateChangesetRequestRequestTypeDef
):
    pass

CreateChangesetResponseTypeDef = TypedDict(
    "CreateChangesetResponseTypeDef",
    {
        "datasetId": str,
        "changesetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataViewRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataViewRequestRequestTypeDef",
    {
        "datasetId": str,
        "destinationTypeParams": "DataViewDestinationTypeParamsTypeDef",
    },
)
_OptionalCreateDataViewRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataViewRequestRequestTypeDef",
    {
        "clientToken": str,
        "autoUpdate": bool,
        "sortColumns": List[str],
        "partitionColumns": List[str],
        "asOfTimestamp": int,
    },
    total=False,
)

class CreateDataViewRequestRequestTypeDef(
    _RequiredCreateDataViewRequestRequestTypeDef, _OptionalCreateDataViewRequestRequestTypeDef
):
    pass

CreateDataViewResponseTypeDef = TypedDict(
    "CreateDataViewResponseTypeDef",
    {
        "datasetId": str,
        "dataViewId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDatasetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetRequestRequestTypeDef",
    {
        "datasetTitle": str,
        "kind": DatasetKindType,
        "datasetDescription": str,
        "permissionGroupParams": "PermissionGroupParamsTypeDef",
        "alias": str,
    },
)
_OptionalCreateDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetRequestRequestTypeDef",
    {
        "clientToken": str,
        "ownerInfo": "DatasetOwnerInfoTypeDef",
        "schemaDefinition": "SchemaUnionTypeDef",
    },
    total=False,
)

class CreateDatasetRequestRequestTypeDef(
    _RequiredCreateDatasetRequestRequestTypeDef, _OptionalCreateDatasetRequestRequestTypeDef
):
    pass

CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "datasetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "accessKeyId": str,
        "secretAccessKey": str,
        "sessionToken": str,
    },
    total=False,
)

DataViewDestinationTypeParamsTypeDef = TypedDict(
    "DataViewDestinationTypeParamsTypeDef",
    {
        "destinationType": str,
    },
)

DataViewErrorInfoTypeDef = TypedDict(
    "DataViewErrorInfoTypeDef",
    {
        "errorMessage": str,
        "errorCategory": ErrorCategoryType,
    },
    total=False,
)

DataViewSummaryTypeDef = TypedDict(
    "DataViewSummaryTypeDef",
    {
        "dataViewId": str,
        "dataViewArn": str,
        "datasetId": str,
        "asOfTimestamp": int,
        "partitionColumns": List[str],
        "sortColumns": List[str],
        "status": DataViewStatusType,
        "errorInfo": "DataViewErrorInfoTypeDef",
        "destinationTypeProperties": "DataViewDestinationTypeParamsTypeDef",
        "autoUpdate": bool,
        "createTime": int,
        "lastModifiedTime": int,
    },
    total=False,
)

DatasetOwnerInfoTypeDef = TypedDict(
    "DatasetOwnerInfoTypeDef",
    {
        "name": str,
        "phoneNumber": str,
        "email": str,
    },
    total=False,
)

DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "datasetId": str,
        "datasetArn": str,
        "datasetTitle": str,
        "kind": DatasetKindType,
        "datasetDescription": str,
        "ownerInfo": "DatasetOwnerInfoTypeDef",
        "createTime": int,
        "lastModifiedTime": int,
        "schemaDefinition": "SchemaUnionTypeDef",
        "alias": str,
    },
    total=False,
)

_RequiredDeleteDatasetRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteDatasetRequestRequestTypeDef",
    {
        "datasetId": str,
    },
)
_OptionalDeleteDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteDatasetRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteDatasetRequestRequestTypeDef(
    _RequiredDeleteDatasetRequestRequestTypeDef, _OptionalDeleteDatasetRequestRequestTypeDef
):
    pass

DeleteDatasetResponseTypeDef = TypedDict(
    "DeleteDatasetResponseTypeDef",
    {
        "datasetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChangesetRequestRequestTypeDef = TypedDict(
    "GetChangesetRequestRequestTypeDef",
    {
        "datasetId": str,
        "changesetId": str,
    },
)

GetChangesetResponseTypeDef = TypedDict(
    "GetChangesetResponseTypeDef",
    {
        "changesetId": str,
        "changesetArn": str,
        "datasetId": str,
        "changeType": ChangeTypeType,
        "sourceParams": Dict[str, str],
        "formatParams": Dict[str, str],
        "createTime": int,
        "status": IngestionStatusType,
        "errorInfo": "ChangesetErrorInfoTypeDef",
        "activeUntilTimestamp": int,
        "updatesChangesetId": str,
        "updatedByChangesetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataViewRequestRequestTypeDef = TypedDict(
    "GetDataViewRequestRequestTypeDef",
    {
        "dataViewId": str,
        "datasetId": str,
    },
)

GetDataViewResponseTypeDef = TypedDict(
    "GetDataViewResponseTypeDef",
    {
        "autoUpdate": bool,
        "partitionColumns": List[str],
        "datasetId": str,
        "asOfTimestamp": int,
        "errorInfo": "DataViewErrorInfoTypeDef",
        "lastModifiedTime": int,
        "createTime": int,
        "sortColumns": List[str],
        "dataViewId": str,
        "dataViewArn": str,
        "destinationTypeParams": "DataViewDestinationTypeParamsTypeDef",
        "status": DataViewStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDatasetRequestRequestTypeDef = TypedDict(
    "GetDatasetRequestRequestTypeDef",
    {
        "datasetId": str,
    },
)

GetDatasetResponseTypeDef = TypedDict(
    "GetDatasetResponseTypeDef",
    {
        "datasetId": str,
        "datasetArn": str,
        "datasetTitle": str,
        "kind": DatasetKindType,
        "datasetDescription": str,
        "createTime": int,
        "lastModifiedTime": int,
        "schemaDefinition": "SchemaUnionTypeDef",
        "alias": str,
        "status": DatasetStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetProgrammaticAccessCredentialsRequestRequestTypeDef = TypedDict(
    "_RequiredGetProgrammaticAccessCredentialsRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)
_OptionalGetProgrammaticAccessCredentialsRequestRequestTypeDef = TypedDict(
    "_OptionalGetProgrammaticAccessCredentialsRequestRequestTypeDef",
    {
        "durationInMinutes": int,
    },
    total=False,
)

class GetProgrammaticAccessCredentialsRequestRequestTypeDef(
    _RequiredGetProgrammaticAccessCredentialsRequestRequestTypeDef,
    _OptionalGetProgrammaticAccessCredentialsRequestRequestTypeDef,
):
    pass

GetProgrammaticAccessCredentialsResponseTypeDef = TypedDict(
    "GetProgrammaticAccessCredentialsResponseTypeDef",
    {
        "credentials": "CredentialsTypeDef",
        "durationInMinutes": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkingLocationRequestRequestTypeDef = TypedDict(
    "GetWorkingLocationRequestRequestTypeDef",
    {
        "locationType": locationTypeType,
    },
    total=False,
)

GetWorkingLocationResponseTypeDef = TypedDict(
    "GetWorkingLocationResponseTypeDef",
    {
        "s3Uri": str,
        "s3Path": str,
        "s3Bucket": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChangesetsRequestRequestTypeDef = TypedDict(
    "_RequiredListChangesetsRequestRequestTypeDef",
    {
        "datasetId": str,
    },
)
_OptionalListChangesetsRequestRequestTypeDef = TypedDict(
    "_OptionalListChangesetsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListChangesetsRequestRequestTypeDef(
    _RequiredListChangesetsRequestRequestTypeDef, _OptionalListChangesetsRequestRequestTypeDef
):
    pass

ListChangesetsResponseTypeDef = TypedDict(
    "ListChangesetsResponseTypeDef",
    {
        "changesets": List["ChangesetSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDataViewsRequestRequestTypeDef = TypedDict(
    "_RequiredListDataViewsRequestRequestTypeDef",
    {
        "datasetId": str,
    },
)
_OptionalListDataViewsRequestRequestTypeDef = TypedDict(
    "_OptionalListDataViewsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListDataViewsRequestRequestTypeDef(
    _RequiredListDataViewsRequestRequestTypeDef, _OptionalListDataViewsRequestRequestTypeDef
):
    pass

ListDataViewsResponseTypeDef = TypedDict(
    "ListDataViewsResponseTypeDef",
    {
        "nextToken": str,
        "dataViews": List["DataViewSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetsRequestRequestTypeDef = TypedDict(
    "ListDatasetsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "datasets": List["DatasetTypeDef"],
        "nextToken": str,
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

PermissionGroupParamsTypeDef = TypedDict(
    "PermissionGroupParamsTypeDef",
    {
        "permissionGroupId": str,
        "datasetPermissions": List["ResourcePermissionTypeDef"],
    },
    total=False,
)

ResourcePermissionTypeDef = TypedDict(
    "ResourcePermissionTypeDef",
    {
        "permission": str,
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

SchemaDefinitionTypeDef = TypedDict(
    "SchemaDefinitionTypeDef",
    {
        "columns": List["ColumnDefinitionTypeDef"],
        "primaryKeyColumns": List[str],
    },
    total=False,
)

SchemaUnionTypeDef = TypedDict(
    "SchemaUnionTypeDef",
    {
        "tabularSchemaConfig": "SchemaDefinitionTypeDef",
    },
    total=False,
)

_RequiredUpdateChangesetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateChangesetRequestRequestTypeDef",
    {
        "datasetId": str,
        "changesetId": str,
        "sourceParams": Dict[str, str],
        "formatParams": Dict[str, str],
    },
)
_OptionalUpdateChangesetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateChangesetRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateChangesetRequestRequestTypeDef(
    _RequiredUpdateChangesetRequestRequestTypeDef, _OptionalUpdateChangesetRequestRequestTypeDef
):
    pass

UpdateChangesetResponseTypeDef = TypedDict(
    "UpdateChangesetResponseTypeDef",
    {
        "changesetId": str,
        "datasetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDatasetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDatasetRequestRequestTypeDef",
    {
        "datasetId": str,
        "datasetTitle": str,
        "kind": DatasetKindType,
        "alias": str,
    },
)
_OptionalUpdateDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDatasetRequestRequestTypeDef",
    {
        "clientToken": str,
        "datasetDescription": str,
        "schemaDefinition": "SchemaUnionTypeDef",
    },
    total=False,
)

class UpdateDatasetRequestRequestTypeDef(
    _RequiredUpdateDatasetRequestRequestTypeDef, _OptionalUpdateDatasetRequestRequestTypeDef
):
    pass

UpdateDatasetResponseTypeDef = TypedDict(
    "UpdateDatasetResponseTypeDef",
    {
        "datasetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
