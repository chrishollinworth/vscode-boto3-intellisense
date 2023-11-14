"""
Type annotations for finspace-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_finspace_data.type_defs import AssociateUserToPermissionGroupRequestRequestTypeDef

    data: AssociateUserToPermissionGroupRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    ApiAccessType,
    ApplicationPermissionType,
    ChangeTypeType,
    ColumnDataTypeType,
    DatasetKindType,
    DatasetStatusType,
    DataViewStatusType,
    ErrorCategoryType,
    ExportFileFormatType,
    IngestionStatusType,
    PermissionGroupMembershipStatusType,
    UserStatusType,
    UserTypeType,
    locationTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AssociateUserToPermissionGroupRequestRequestTypeDef",
    "AssociateUserToPermissionGroupResponseTypeDef",
    "AwsCredentialsTypeDef",
    "ChangesetErrorInfoTypeDef",
    "ChangesetSummaryTypeDef",
    "ColumnDefinitionTypeDef",
    "CreateChangesetRequestRequestTypeDef",
    "CreateChangesetResponseTypeDef",
    "CreateDataViewRequestRequestTypeDef",
    "CreateDataViewResponseTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreatePermissionGroupRequestRequestTypeDef",
    "CreatePermissionGroupResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CreateUserResponseTypeDef",
    "CredentialsTypeDef",
    "DataViewDestinationTypeParamsTypeDef",
    "DataViewErrorInfoTypeDef",
    "DataViewSummaryTypeDef",
    "DatasetOwnerInfoTypeDef",
    "DatasetTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteDatasetResponseTypeDef",
    "DeletePermissionGroupRequestRequestTypeDef",
    "DeletePermissionGroupResponseTypeDef",
    "DisableUserRequestRequestTypeDef",
    "DisableUserResponseTypeDef",
    "DisassociateUserFromPermissionGroupRequestRequestTypeDef",
    "DisassociateUserFromPermissionGroupResponseTypeDef",
    "EnableUserRequestRequestTypeDef",
    "EnableUserResponseTypeDef",
    "GetChangesetRequestRequestTypeDef",
    "GetChangesetResponseTypeDef",
    "GetDataViewRequestRequestTypeDef",
    "GetDataViewResponseTypeDef",
    "GetDatasetRequestRequestTypeDef",
    "GetDatasetResponseTypeDef",
    "GetExternalDataViewAccessDetailsRequestRequestTypeDef",
    "GetExternalDataViewAccessDetailsResponseTypeDef",
    "GetPermissionGroupRequestRequestTypeDef",
    "GetPermissionGroupResponseTypeDef",
    "GetProgrammaticAccessCredentialsRequestRequestTypeDef",
    "GetProgrammaticAccessCredentialsResponseTypeDef",
    "GetUserRequestRequestTypeDef",
    "GetUserResponseTypeDef",
    "GetWorkingLocationRequestRequestTypeDef",
    "GetWorkingLocationResponseTypeDef",
    "ListChangesetsRequestRequestTypeDef",
    "ListChangesetsResponseTypeDef",
    "ListDataViewsRequestRequestTypeDef",
    "ListDataViewsResponseTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListPermissionGroupsByUserRequestRequestTypeDef",
    "ListPermissionGroupsByUserResponseTypeDef",
    "ListPermissionGroupsRequestRequestTypeDef",
    "ListPermissionGroupsResponseTypeDef",
    "ListUsersByPermissionGroupRequestRequestTypeDef",
    "ListUsersByPermissionGroupResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionGroupByUserTypeDef",
    "PermissionGroupParamsTypeDef",
    "PermissionGroupTypeDef",
    "ResetUserPasswordRequestRequestTypeDef",
    "ResetUserPasswordResponseTypeDef",
    "ResourcePermissionTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "SchemaDefinitionTypeDef",
    "SchemaUnionTypeDef",
    "UpdateChangesetRequestRequestTypeDef",
    "UpdateChangesetResponseTypeDef",
    "UpdateDatasetRequestRequestTypeDef",
    "UpdateDatasetResponseTypeDef",
    "UpdatePermissionGroupRequestRequestTypeDef",
    "UpdatePermissionGroupResponseTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UpdateUserResponseTypeDef",
    "UserByPermissionGroupTypeDef",
    "UserTypeDef",
)

_RequiredAssociateUserToPermissionGroupRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateUserToPermissionGroupRequestRequestTypeDef",
    {
        "permissionGroupId": str,
        "userId": str,
    },
)
_OptionalAssociateUserToPermissionGroupRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateUserToPermissionGroupRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class AssociateUserToPermissionGroupRequestRequestTypeDef(
    _RequiredAssociateUserToPermissionGroupRequestRequestTypeDef,
    _OptionalAssociateUserToPermissionGroupRequestRequestTypeDef,
):
    pass

AssociateUserToPermissionGroupResponseTypeDef = TypedDict(
    "AssociateUserToPermissionGroupResponseTypeDef",
    {
        "statusCode": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AwsCredentialsTypeDef = TypedDict(
    "AwsCredentialsTypeDef",
    {
        "accessKeyId": str,
        "secretAccessKey": str,
        "sessionToken": str,
        "expiration": int,
    },
    total=False,
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
        "activeFromTimestamp": int,
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
        "permissionGroupParams": "PermissionGroupParamsTypeDef",
    },
)
_OptionalCreateDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetRequestRequestTypeDef",
    {
        "clientToken": str,
        "datasetDescription": str,
        "ownerInfo": "DatasetOwnerInfoTypeDef",
        "alias": str,
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

_RequiredCreatePermissionGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePermissionGroupRequestRequestTypeDef",
    {
        "name": str,
        "applicationPermissions": List[ApplicationPermissionType],
    },
)
_OptionalCreatePermissionGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePermissionGroupRequestRequestTypeDef",
    {
        "description": str,
        "clientToken": str,
    },
    total=False,
)

class CreatePermissionGroupRequestRequestTypeDef(
    _RequiredCreatePermissionGroupRequestRequestTypeDef,
    _OptionalCreatePermissionGroupRequestRequestTypeDef,
):
    pass

CreatePermissionGroupResponseTypeDef = TypedDict(
    "CreatePermissionGroupResponseTypeDef",
    {
        "permissionGroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestRequestTypeDef",
    {
        "emailAddress": str,
        "type": UserTypeType,
    },
)
_OptionalCreateUserRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestRequestTypeDef",
    {
        "firstName": str,
        "lastName": str,
        "apiAccess": ApiAccessType,
        "apiAccessPrincipalArn": str,
        "clientToken": str,
    },
    total=False,
)

class CreateUserRequestRequestTypeDef(
    _RequiredCreateUserRequestRequestTypeDef, _OptionalCreateUserRequestRequestTypeDef
):
    pass

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "userId": str,
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

_RequiredDataViewDestinationTypeParamsTypeDef = TypedDict(
    "_RequiredDataViewDestinationTypeParamsTypeDef",
    {
        "destinationType": str,
    },
)
_OptionalDataViewDestinationTypeParamsTypeDef = TypedDict(
    "_OptionalDataViewDestinationTypeParamsTypeDef",
    {
        "s3DestinationExportFileFormat": ExportFileFormatType,
        "s3DestinationExportFileFormatOptions": Dict[str, str],
    },
    total=False,
)

class DataViewDestinationTypeParamsTypeDef(
    _RequiredDataViewDestinationTypeParamsTypeDef, _OptionalDataViewDestinationTypeParamsTypeDef
):
    pass

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

_RequiredDeletePermissionGroupRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePermissionGroupRequestRequestTypeDef",
    {
        "permissionGroupId": str,
    },
)
_OptionalDeletePermissionGroupRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePermissionGroupRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeletePermissionGroupRequestRequestTypeDef(
    _RequiredDeletePermissionGroupRequestRequestTypeDef,
    _OptionalDeletePermissionGroupRequestRequestTypeDef,
):
    pass

DeletePermissionGroupResponseTypeDef = TypedDict(
    "DeletePermissionGroupResponseTypeDef",
    {
        "permissionGroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisableUserRequestRequestTypeDef = TypedDict(
    "_RequiredDisableUserRequestRequestTypeDef",
    {
        "userId": str,
    },
)
_OptionalDisableUserRequestRequestTypeDef = TypedDict(
    "_OptionalDisableUserRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DisableUserRequestRequestTypeDef(
    _RequiredDisableUserRequestRequestTypeDef, _OptionalDisableUserRequestRequestTypeDef
):
    pass

DisableUserResponseTypeDef = TypedDict(
    "DisableUserResponseTypeDef",
    {
        "userId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateUserFromPermissionGroupRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateUserFromPermissionGroupRequestRequestTypeDef",
    {
        "permissionGroupId": str,
        "userId": str,
    },
)
_OptionalDisassociateUserFromPermissionGroupRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateUserFromPermissionGroupRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DisassociateUserFromPermissionGroupRequestRequestTypeDef(
    _RequiredDisassociateUserFromPermissionGroupRequestRequestTypeDef,
    _OptionalDisassociateUserFromPermissionGroupRequestRequestTypeDef,
):
    pass

DisassociateUserFromPermissionGroupResponseTypeDef = TypedDict(
    "DisassociateUserFromPermissionGroupResponseTypeDef",
    {
        "statusCode": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEnableUserRequestRequestTypeDef = TypedDict(
    "_RequiredEnableUserRequestRequestTypeDef",
    {
        "userId": str,
    },
)
_OptionalEnableUserRequestRequestTypeDef = TypedDict(
    "_OptionalEnableUserRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class EnableUserRequestRequestTypeDef(
    _RequiredEnableUserRequestRequestTypeDef, _OptionalEnableUserRequestRequestTypeDef
):
    pass

EnableUserResponseTypeDef = TypedDict(
    "EnableUserResponseTypeDef",
    {
        "userId": str,
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
        "activeFromTimestamp": int,
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

GetExternalDataViewAccessDetailsRequestRequestTypeDef = TypedDict(
    "GetExternalDataViewAccessDetailsRequestRequestTypeDef",
    {
        "dataViewId": str,
        "datasetId": str,
    },
)

GetExternalDataViewAccessDetailsResponseTypeDef = TypedDict(
    "GetExternalDataViewAccessDetailsResponseTypeDef",
    {
        "credentials": "AwsCredentialsTypeDef",
        "s3Location": "S3LocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPermissionGroupRequestRequestTypeDef = TypedDict(
    "GetPermissionGroupRequestRequestTypeDef",
    {
        "permissionGroupId": str,
    },
)

GetPermissionGroupResponseTypeDef = TypedDict(
    "GetPermissionGroupResponseTypeDef",
    {
        "permissionGroup": "PermissionGroupTypeDef",
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

GetUserRequestRequestTypeDef = TypedDict(
    "GetUserRequestRequestTypeDef",
    {
        "userId": str,
    },
)

GetUserResponseTypeDef = TypedDict(
    "GetUserResponseTypeDef",
    {
        "userId": str,
        "status": UserStatusType,
        "firstName": str,
        "lastName": str,
        "emailAddress": str,
        "type": UserTypeType,
        "apiAccess": ApiAccessType,
        "apiAccessPrincipalArn": str,
        "createTime": int,
        "lastEnabledTime": int,
        "lastDisabledTime": int,
        "lastModifiedTime": int,
        "lastLoginTime": int,
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

_RequiredListPermissionGroupsByUserRequestRequestTypeDef = TypedDict(
    "_RequiredListPermissionGroupsByUserRequestRequestTypeDef",
    {
        "userId": str,
        "maxResults": int,
    },
)
_OptionalListPermissionGroupsByUserRequestRequestTypeDef = TypedDict(
    "_OptionalListPermissionGroupsByUserRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListPermissionGroupsByUserRequestRequestTypeDef(
    _RequiredListPermissionGroupsByUserRequestRequestTypeDef,
    _OptionalListPermissionGroupsByUserRequestRequestTypeDef,
):
    pass

ListPermissionGroupsByUserResponseTypeDef = TypedDict(
    "ListPermissionGroupsByUserResponseTypeDef",
    {
        "permissionGroups": List["PermissionGroupByUserTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPermissionGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListPermissionGroupsRequestRequestTypeDef",
    {
        "maxResults": int,
    },
)
_OptionalListPermissionGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListPermissionGroupsRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListPermissionGroupsRequestRequestTypeDef(
    _RequiredListPermissionGroupsRequestRequestTypeDef,
    _OptionalListPermissionGroupsRequestRequestTypeDef,
):
    pass

ListPermissionGroupsResponseTypeDef = TypedDict(
    "ListPermissionGroupsResponseTypeDef",
    {
        "permissionGroups": List["PermissionGroupTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersByPermissionGroupRequestRequestTypeDef = TypedDict(
    "_RequiredListUsersByPermissionGroupRequestRequestTypeDef",
    {
        "permissionGroupId": str,
        "maxResults": int,
    },
)
_OptionalListUsersByPermissionGroupRequestRequestTypeDef = TypedDict(
    "_OptionalListUsersByPermissionGroupRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListUsersByPermissionGroupRequestRequestTypeDef(
    _RequiredListUsersByPermissionGroupRequestRequestTypeDef,
    _OptionalListUsersByPermissionGroupRequestRequestTypeDef,
):
    pass

ListUsersByPermissionGroupResponseTypeDef = TypedDict(
    "ListUsersByPermissionGroupResponseTypeDef",
    {
        "users": List["UserByPermissionGroupTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersRequestRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestRequestTypeDef",
    {
        "maxResults": int,
    },
)
_OptionalListUsersRequestRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListUsersRequestRequestTypeDef(
    _RequiredListUsersRequestRequestTypeDef, _OptionalListUsersRequestRequestTypeDef
):
    pass

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "users": List["UserTypeDef"],
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

PermissionGroupByUserTypeDef = TypedDict(
    "PermissionGroupByUserTypeDef",
    {
        "permissionGroupId": str,
        "name": str,
        "membershipStatus": PermissionGroupMembershipStatusType,
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

PermissionGroupTypeDef = TypedDict(
    "PermissionGroupTypeDef",
    {
        "permissionGroupId": str,
        "name": str,
        "description": str,
        "applicationPermissions": List[ApplicationPermissionType],
        "createTime": int,
        "lastModifiedTime": int,
        "membershipStatus": PermissionGroupMembershipStatusType,
    },
    total=False,
)

_RequiredResetUserPasswordRequestRequestTypeDef = TypedDict(
    "_RequiredResetUserPasswordRequestRequestTypeDef",
    {
        "userId": str,
    },
)
_OptionalResetUserPasswordRequestRequestTypeDef = TypedDict(
    "_OptionalResetUserPasswordRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class ResetUserPasswordRequestRequestTypeDef(
    _RequiredResetUserPasswordRequestRequestTypeDef, _OptionalResetUserPasswordRequestRequestTypeDef
):
    pass

ResetUserPasswordResponseTypeDef = TypedDict(
    "ResetUserPasswordResponseTypeDef",
    {
        "userId": str,
        "temporaryPassword": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
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
    },
)
_OptionalUpdateDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDatasetRequestRequestTypeDef",
    {
        "clientToken": str,
        "datasetDescription": str,
        "alias": str,
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

_RequiredUpdatePermissionGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePermissionGroupRequestRequestTypeDef",
    {
        "permissionGroupId": str,
    },
)
_OptionalUpdatePermissionGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePermissionGroupRequestRequestTypeDef",
    {
        "name": str,
        "description": str,
        "applicationPermissions": List[ApplicationPermissionType],
        "clientToken": str,
    },
    total=False,
)

class UpdatePermissionGroupRequestRequestTypeDef(
    _RequiredUpdatePermissionGroupRequestRequestTypeDef,
    _OptionalUpdatePermissionGroupRequestRequestTypeDef,
):
    pass

UpdatePermissionGroupResponseTypeDef = TypedDict(
    "UpdatePermissionGroupResponseTypeDef",
    {
        "permissionGroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserRequestRequestTypeDef",
    {
        "userId": str,
    },
)
_OptionalUpdateUserRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserRequestRequestTypeDef",
    {
        "type": UserTypeType,
        "firstName": str,
        "lastName": str,
        "apiAccess": ApiAccessType,
        "apiAccessPrincipalArn": str,
        "clientToken": str,
    },
    total=False,
)

class UpdateUserRequestRequestTypeDef(
    _RequiredUpdateUserRequestRequestTypeDef, _OptionalUpdateUserRequestRequestTypeDef
):
    pass

UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {
        "userId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserByPermissionGroupTypeDef = TypedDict(
    "UserByPermissionGroupTypeDef",
    {
        "userId": str,
        "status": UserStatusType,
        "firstName": str,
        "lastName": str,
        "emailAddress": str,
        "type": UserTypeType,
        "apiAccess": ApiAccessType,
        "apiAccessPrincipalArn": str,
        "membershipStatus": PermissionGroupMembershipStatusType,
    },
    total=False,
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "userId": str,
        "status": UserStatusType,
        "firstName": str,
        "lastName": str,
        "emailAddress": str,
        "type": UserTypeType,
        "apiAccess": ApiAccessType,
        "apiAccessPrincipalArn": str,
        "createTime": int,
        "lastEnabledTime": int,
        "lastDisabledTime": int,
        "lastModifiedTime": int,
        "lastLoginTime": int,
    },
    total=False,
)
