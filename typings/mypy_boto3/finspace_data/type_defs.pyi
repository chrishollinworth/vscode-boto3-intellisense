"""
Type annotations for finspace-data service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_finspace_data.type_defs import AssociateUserToPermissionGroupRequestTypeDef

    data: AssociateUserToPermissionGroupRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import Union

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
    LocationTypeType,
    PermissionGroupMembershipStatusType,
    UserStatusType,
    UserTypeType,
)

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
    "AssociateUserToPermissionGroupRequestTypeDef",
    "AssociateUserToPermissionGroupResponseTypeDef",
    "AwsCredentialsTypeDef",
    "ChangesetErrorInfoTypeDef",
    "ChangesetSummaryTypeDef",
    "ColumnDefinitionTypeDef",
    "CreateChangesetRequestTypeDef",
    "CreateChangesetResponseTypeDef",
    "CreateDataViewRequestTypeDef",
    "CreateDataViewResponseTypeDef",
    "CreateDatasetRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreatePermissionGroupRequestTypeDef",
    "CreatePermissionGroupResponseTypeDef",
    "CreateUserRequestTypeDef",
    "CreateUserResponseTypeDef",
    "CredentialsTypeDef",
    "DataViewDestinationTypeParamsOutputTypeDef",
    "DataViewDestinationTypeParamsTypeDef",
    "DataViewDestinationTypeParamsUnionTypeDef",
    "DataViewErrorInfoTypeDef",
    "DataViewSummaryTypeDef",
    "DatasetOwnerInfoTypeDef",
    "DatasetTypeDef",
    "DeleteDatasetRequestTypeDef",
    "DeleteDatasetResponseTypeDef",
    "DeletePermissionGroupRequestTypeDef",
    "DeletePermissionGroupResponseTypeDef",
    "DisableUserRequestTypeDef",
    "DisableUserResponseTypeDef",
    "DisassociateUserFromPermissionGroupRequestTypeDef",
    "DisassociateUserFromPermissionGroupResponseTypeDef",
    "EnableUserRequestTypeDef",
    "EnableUserResponseTypeDef",
    "GetChangesetRequestTypeDef",
    "GetChangesetResponseTypeDef",
    "GetDataViewRequestTypeDef",
    "GetDataViewResponseTypeDef",
    "GetDatasetRequestTypeDef",
    "GetDatasetResponseTypeDef",
    "GetExternalDataViewAccessDetailsRequestTypeDef",
    "GetExternalDataViewAccessDetailsResponseTypeDef",
    "GetPermissionGroupRequestTypeDef",
    "GetPermissionGroupResponseTypeDef",
    "GetProgrammaticAccessCredentialsRequestTypeDef",
    "GetProgrammaticAccessCredentialsResponseTypeDef",
    "GetUserRequestTypeDef",
    "GetUserResponseTypeDef",
    "GetWorkingLocationRequestTypeDef",
    "GetWorkingLocationResponseTypeDef",
    "ListChangesetsRequestPaginateTypeDef",
    "ListChangesetsRequestTypeDef",
    "ListChangesetsResponseTypeDef",
    "ListDataViewsRequestPaginateTypeDef",
    "ListDataViewsRequestTypeDef",
    "ListDataViewsResponseTypeDef",
    "ListDatasetsRequestPaginateTypeDef",
    "ListDatasetsRequestTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListPermissionGroupsByUserRequestTypeDef",
    "ListPermissionGroupsByUserResponseTypeDef",
    "ListPermissionGroupsRequestPaginateTypeDef",
    "ListPermissionGroupsRequestTypeDef",
    "ListPermissionGroupsResponseTypeDef",
    "ListUsersByPermissionGroupRequestTypeDef",
    "ListUsersByPermissionGroupResponseTypeDef",
    "ListUsersRequestPaginateTypeDef",
    "ListUsersRequestTypeDef",
    "ListUsersResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionGroupByUserTypeDef",
    "PermissionGroupParamsTypeDef",
    "PermissionGroupTypeDef",
    "ResetUserPasswordRequestTypeDef",
    "ResetUserPasswordResponseTypeDef",
    "ResourcePermissionTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "SchemaDefinitionOutputTypeDef",
    "SchemaDefinitionTypeDef",
    "SchemaUnionOutputTypeDef",
    "SchemaUnionTypeDef",
    "SchemaUnionUnionTypeDef",
    "UpdateChangesetRequestTypeDef",
    "UpdateChangesetResponseTypeDef",
    "UpdateDatasetRequestTypeDef",
    "UpdateDatasetResponseTypeDef",
    "UpdatePermissionGroupRequestTypeDef",
    "UpdatePermissionGroupResponseTypeDef",
    "UpdateUserRequestTypeDef",
    "UpdateUserResponseTypeDef",
    "UserByPermissionGroupTypeDef",
    "UserTypeDef",
)

class AssociateUserToPermissionGroupRequestTypeDef(TypedDict):
    permissionGroupId: str
    userId: str
    clientToken: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AwsCredentialsTypeDef(TypedDict):
    accessKeyId: NotRequired[str]
    secretAccessKey: NotRequired[str]
    sessionToken: NotRequired[str]
    expiration: NotRequired[int]

class ChangesetErrorInfoTypeDef(TypedDict):
    errorMessage: NotRequired[str]
    errorCategory: NotRequired[ErrorCategoryType]

class ColumnDefinitionTypeDef(TypedDict):
    dataType: NotRequired[ColumnDataTypeType]
    columnName: NotRequired[str]
    columnDescription: NotRequired[str]

class CreateChangesetRequestTypeDef(TypedDict):
    datasetId: str
    changeType: ChangeTypeType
    sourceParams: Mapping[str, str]
    formatParams: Mapping[str, str]
    clientToken: NotRequired[str]

class DatasetOwnerInfoTypeDef(TypedDict):
    name: NotRequired[str]
    phoneNumber: NotRequired[str]
    email: NotRequired[str]

class CreatePermissionGroupRequestTypeDef(TypedDict):
    name: str
    applicationPermissions: Sequence[ApplicationPermissionType]
    description: NotRequired[str]
    clientToken: NotRequired[str]

CreateUserRequestTypeDef = TypedDict(
    "CreateUserRequestTypeDef",
    {
        "emailAddress": str,
        "type": UserTypeType,
        "firstName": NotRequired[str],
        "lastName": NotRequired[str],
        "apiAccess": NotRequired[ApiAccessType],
        "apiAccessPrincipalArn": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)

class CredentialsTypeDef(TypedDict):
    accessKeyId: NotRequired[str]
    secretAccessKey: NotRequired[str]
    sessionToken: NotRequired[str]

class DataViewDestinationTypeParamsOutputTypeDef(TypedDict):
    destinationType: str
    s3DestinationExportFileFormat: NotRequired[ExportFileFormatType]
    s3DestinationExportFileFormatOptions: NotRequired[Dict[str, str]]

class DataViewDestinationTypeParamsTypeDef(TypedDict):
    destinationType: str
    s3DestinationExportFileFormat: NotRequired[ExportFileFormatType]
    s3DestinationExportFileFormatOptions: NotRequired[Mapping[str, str]]

class DataViewErrorInfoTypeDef(TypedDict):
    errorMessage: NotRequired[str]
    errorCategory: NotRequired[ErrorCategoryType]

class DeleteDatasetRequestTypeDef(TypedDict):
    datasetId: str
    clientToken: NotRequired[str]

class DeletePermissionGroupRequestTypeDef(TypedDict):
    permissionGroupId: str
    clientToken: NotRequired[str]

class DisableUserRequestTypeDef(TypedDict):
    userId: str
    clientToken: NotRequired[str]

class DisassociateUserFromPermissionGroupRequestTypeDef(TypedDict):
    permissionGroupId: str
    userId: str
    clientToken: NotRequired[str]

class EnableUserRequestTypeDef(TypedDict):
    userId: str
    clientToken: NotRequired[str]

class GetChangesetRequestTypeDef(TypedDict):
    datasetId: str
    changesetId: str

class GetDataViewRequestTypeDef(TypedDict):
    dataViewId: str
    datasetId: str

class GetDatasetRequestTypeDef(TypedDict):
    datasetId: str

class GetExternalDataViewAccessDetailsRequestTypeDef(TypedDict):
    dataViewId: str
    datasetId: str

class S3LocationTypeDef(TypedDict):
    bucket: str
    key: str

class GetPermissionGroupRequestTypeDef(TypedDict):
    permissionGroupId: str

class PermissionGroupTypeDef(TypedDict):
    permissionGroupId: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str]
    applicationPermissions: NotRequired[List[ApplicationPermissionType]]
    createTime: NotRequired[int]
    lastModifiedTime: NotRequired[int]
    membershipStatus: NotRequired[PermissionGroupMembershipStatusType]

class GetProgrammaticAccessCredentialsRequestTypeDef(TypedDict):
    environmentId: str
    durationInMinutes: NotRequired[int]

class GetUserRequestTypeDef(TypedDict):
    userId: str

class GetWorkingLocationRequestTypeDef(TypedDict):
    locationType: NotRequired[LocationTypeType]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListChangesetsRequestTypeDef(TypedDict):
    datasetId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListDataViewsRequestTypeDef(TypedDict):
    datasetId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListDatasetsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListPermissionGroupsByUserRequestTypeDef(TypedDict):
    userId: str
    maxResults: int
    nextToken: NotRequired[str]

class PermissionGroupByUserTypeDef(TypedDict):
    permissionGroupId: NotRequired[str]
    name: NotRequired[str]
    membershipStatus: NotRequired[PermissionGroupMembershipStatusType]

class ListPermissionGroupsRequestTypeDef(TypedDict):
    maxResults: int
    nextToken: NotRequired[str]

class ListUsersByPermissionGroupRequestTypeDef(TypedDict):
    permissionGroupId: str
    maxResults: int
    nextToken: NotRequired[str]

UserByPermissionGroupTypeDef = TypedDict(
    "UserByPermissionGroupTypeDef",
    {
        "userId": NotRequired[str],
        "status": NotRequired[UserStatusType],
        "firstName": NotRequired[str],
        "lastName": NotRequired[str],
        "emailAddress": NotRequired[str],
        "type": NotRequired[UserTypeType],
        "apiAccess": NotRequired[ApiAccessType],
        "apiAccessPrincipalArn": NotRequired[str],
        "membershipStatus": NotRequired[PermissionGroupMembershipStatusType],
    },
)

class ListUsersRequestTypeDef(TypedDict):
    maxResults: int
    nextToken: NotRequired[str]

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "userId": NotRequired[str],
        "status": NotRequired[UserStatusType],
        "firstName": NotRequired[str],
        "lastName": NotRequired[str],
        "emailAddress": NotRequired[str],
        "type": NotRequired[UserTypeType],
        "apiAccess": NotRequired[ApiAccessType],
        "apiAccessPrincipalArn": NotRequired[str],
        "createTime": NotRequired[int],
        "lastEnabledTime": NotRequired[int],
        "lastDisabledTime": NotRequired[int],
        "lastModifiedTime": NotRequired[int],
        "lastLoginTime": NotRequired[int],
    },
)

class ResourcePermissionTypeDef(TypedDict):
    permission: NotRequired[str]

class ResetUserPasswordRequestTypeDef(TypedDict):
    userId: str
    clientToken: NotRequired[str]

class UpdateChangesetRequestTypeDef(TypedDict):
    datasetId: str
    changesetId: str
    sourceParams: Mapping[str, str]
    formatParams: Mapping[str, str]
    clientToken: NotRequired[str]

class UpdatePermissionGroupRequestTypeDef(TypedDict):
    permissionGroupId: str
    name: NotRequired[str]
    description: NotRequired[str]
    applicationPermissions: NotRequired[Sequence[ApplicationPermissionType]]
    clientToken: NotRequired[str]

UpdateUserRequestTypeDef = TypedDict(
    "UpdateUserRequestTypeDef",
    {
        "userId": str,
        "type": NotRequired[UserTypeType],
        "firstName": NotRequired[str],
        "lastName": NotRequired[str],
        "apiAccess": NotRequired[ApiAccessType],
        "apiAccessPrincipalArn": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)

class AssociateUserToPermissionGroupResponseTypeDef(TypedDict):
    statusCode: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChangesetResponseTypeDef(TypedDict):
    datasetId: str
    changesetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataViewResponseTypeDef(TypedDict):
    datasetId: str
    dataViewId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetResponseTypeDef(TypedDict):
    datasetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePermissionGroupResponseTypeDef(TypedDict):
    permissionGroupId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserResponseTypeDef(TypedDict):
    userId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDatasetResponseTypeDef(TypedDict):
    datasetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePermissionGroupResponseTypeDef(TypedDict):
    permissionGroupId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisableUserResponseTypeDef(TypedDict):
    userId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateUserFromPermissionGroupResponseTypeDef(TypedDict):
    statusCode: int
    ResponseMetadata: ResponseMetadataTypeDef

class EnableUserResponseTypeDef(TypedDict):
    userId: str
    ResponseMetadata: ResponseMetadataTypeDef

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
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetWorkingLocationResponseTypeDef(TypedDict):
    s3Uri: str
    s3Path: str
    s3Bucket: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResetUserPasswordResponseTypeDef(TypedDict):
    userId: str
    temporaryPassword: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChangesetResponseTypeDef(TypedDict):
    changesetId: str
    datasetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDatasetResponseTypeDef(TypedDict):
    datasetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePermissionGroupResponseTypeDef(TypedDict):
    permissionGroupId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserResponseTypeDef(TypedDict):
    userId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChangesetSummaryTypeDef(TypedDict):
    changesetId: NotRequired[str]
    changesetArn: NotRequired[str]
    datasetId: NotRequired[str]
    changeType: NotRequired[ChangeTypeType]
    sourceParams: NotRequired[Dict[str, str]]
    formatParams: NotRequired[Dict[str, str]]
    createTime: NotRequired[int]
    status: NotRequired[IngestionStatusType]
    errorInfo: NotRequired[ChangesetErrorInfoTypeDef]
    activeUntilTimestamp: NotRequired[int]
    activeFromTimestamp: NotRequired[int]
    updatesChangesetId: NotRequired[str]
    updatedByChangesetId: NotRequired[str]

class GetChangesetResponseTypeDef(TypedDict):
    changesetId: str
    changesetArn: str
    datasetId: str
    changeType: ChangeTypeType
    sourceParams: Dict[str, str]
    formatParams: Dict[str, str]
    createTime: int
    status: IngestionStatusType
    errorInfo: ChangesetErrorInfoTypeDef
    activeUntilTimestamp: int
    activeFromTimestamp: int
    updatesChangesetId: str
    updatedByChangesetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SchemaDefinitionOutputTypeDef(TypedDict):
    columns: NotRequired[List[ColumnDefinitionTypeDef]]
    primaryKeyColumns: NotRequired[List[str]]

class SchemaDefinitionTypeDef(TypedDict):
    columns: NotRequired[Sequence[ColumnDefinitionTypeDef]]
    primaryKeyColumns: NotRequired[Sequence[str]]

class GetProgrammaticAccessCredentialsResponseTypeDef(TypedDict):
    credentials: CredentialsTypeDef
    durationInMinutes: int
    ResponseMetadata: ResponseMetadataTypeDef

DataViewDestinationTypeParamsUnionTypeDef = Union[
    DataViewDestinationTypeParamsTypeDef, DataViewDestinationTypeParamsOutputTypeDef
]

class DataViewSummaryTypeDef(TypedDict):
    dataViewId: NotRequired[str]
    dataViewArn: NotRequired[str]
    datasetId: NotRequired[str]
    asOfTimestamp: NotRequired[int]
    partitionColumns: NotRequired[List[str]]
    sortColumns: NotRequired[List[str]]
    status: NotRequired[DataViewStatusType]
    errorInfo: NotRequired[DataViewErrorInfoTypeDef]
    destinationTypeProperties: NotRequired[DataViewDestinationTypeParamsOutputTypeDef]
    autoUpdate: NotRequired[bool]
    createTime: NotRequired[int]
    lastModifiedTime: NotRequired[int]

class GetDataViewResponseTypeDef(TypedDict):
    autoUpdate: bool
    partitionColumns: List[str]
    datasetId: str
    asOfTimestamp: int
    errorInfo: DataViewErrorInfoTypeDef
    lastModifiedTime: int
    createTime: int
    sortColumns: List[str]
    dataViewId: str
    dataViewArn: str
    destinationTypeParams: DataViewDestinationTypeParamsOutputTypeDef
    status: DataViewStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetExternalDataViewAccessDetailsResponseTypeDef(TypedDict):
    credentials: AwsCredentialsTypeDef
    s3Location: S3LocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPermissionGroupResponseTypeDef(TypedDict):
    permissionGroup: PermissionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPermissionGroupsResponseTypeDef(TypedDict):
    permissionGroups: List[PermissionGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListChangesetsRequestPaginateTypeDef(TypedDict):
    datasetId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDataViewsRequestPaginateTypeDef(TypedDict):
    datasetId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDatasetsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPermissionGroupsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListUsersRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPermissionGroupsByUserResponseTypeDef(TypedDict):
    permissionGroups: List[PermissionGroupByUserTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListUsersByPermissionGroupResponseTypeDef(TypedDict):
    users: List[UserByPermissionGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListUsersResponseTypeDef(TypedDict):
    users: List[UserTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class PermissionGroupParamsTypeDef(TypedDict):
    permissionGroupId: NotRequired[str]
    datasetPermissions: NotRequired[Sequence[ResourcePermissionTypeDef]]

class ListChangesetsResponseTypeDef(TypedDict):
    changesets: List[ChangesetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SchemaUnionOutputTypeDef(TypedDict):
    tabularSchemaConfig: NotRequired[SchemaDefinitionOutputTypeDef]

class SchemaUnionTypeDef(TypedDict):
    tabularSchemaConfig: NotRequired[SchemaDefinitionTypeDef]

class CreateDataViewRequestTypeDef(TypedDict):
    datasetId: str
    destinationTypeParams: DataViewDestinationTypeParamsUnionTypeDef
    clientToken: NotRequired[str]
    autoUpdate: NotRequired[bool]
    sortColumns: NotRequired[Sequence[str]]
    partitionColumns: NotRequired[Sequence[str]]
    asOfTimestamp: NotRequired[int]

class ListDataViewsResponseTypeDef(TypedDict):
    dataViews: List[DataViewSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DatasetTypeDef(TypedDict):
    datasetId: NotRequired[str]
    datasetArn: NotRequired[str]
    datasetTitle: NotRequired[str]
    kind: NotRequired[DatasetKindType]
    datasetDescription: NotRequired[str]
    ownerInfo: NotRequired[DatasetOwnerInfoTypeDef]
    createTime: NotRequired[int]
    lastModifiedTime: NotRequired[int]
    schemaDefinition: NotRequired[SchemaUnionOutputTypeDef]
    alias: NotRequired[str]

class GetDatasetResponseTypeDef(TypedDict):
    datasetId: str
    datasetArn: str
    datasetTitle: str
    kind: DatasetKindType
    datasetDescription: str
    createTime: int
    lastModifiedTime: int
    schemaDefinition: SchemaUnionOutputTypeDef
    alias: str
    status: DatasetStatusType
    ResponseMetadata: ResponseMetadataTypeDef

SchemaUnionUnionTypeDef = Union[SchemaUnionTypeDef, SchemaUnionOutputTypeDef]

class ListDatasetsResponseTypeDef(TypedDict):
    datasets: List[DatasetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateDatasetRequestTypeDef(TypedDict):
    datasetTitle: str
    kind: DatasetKindType
    permissionGroupParams: PermissionGroupParamsTypeDef
    clientToken: NotRequired[str]
    datasetDescription: NotRequired[str]
    ownerInfo: NotRequired[DatasetOwnerInfoTypeDef]
    alias: NotRequired[str]
    schemaDefinition: NotRequired[SchemaUnionUnionTypeDef]

class UpdateDatasetRequestTypeDef(TypedDict):
    datasetId: str
    datasetTitle: str
    kind: DatasetKindType
    clientToken: NotRequired[str]
    datasetDescription: NotRequired[str]
    alias: NotRequired[str]
    schemaDefinition: NotRequired[SchemaUnionUnionTypeDef]
