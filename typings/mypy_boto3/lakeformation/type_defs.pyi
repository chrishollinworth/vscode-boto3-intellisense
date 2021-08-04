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
from typing import Any, Dict, List

from .literals import (
    ComparisonOperatorType,
    DataLakeResourceTypeType,
    FieldNameStringType,
    PermissionType,
    ResourceShareTypeType,
    ResourceTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AddLFTagsToResourceRequestRequestTypeDef",
    "AddLFTagsToResourceResponseTypeDef",
    "BatchGrantPermissionsRequestRequestTypeDef",
    "BatchGrantPermissionsResponseTypeDef",
    "BatchPermissionsFailureEntryTypeDef",
    "BatchPermissionsRequestEntryTypeDef",
    "BatchRevokePermissionsRequestRequestTypeDef",
    "BatchRevokePermissionsResponseTypeDef",
    "ColumnLFTagTypeDef",
    "ColumnWildcardTypeDef",
    "CreateLFTagRequestRequestTypeDef",
    "DataLakePrincipalTypeDef",
    "DataLakeSettingsTypeDef",
    "DataLocationResourceTypeDef",
    "DatabaseResourceTypeDef",
    "DeleteLFTagRequestRequestTypeDef",
    "DeregisterResourceRequestRequestTypeDef",
    "DescribeResourceRequestRequestTypeDef",
    "DescribeResourceResponseTypeDef",
    "DetailsMapTypeDef",
    "ErrorDetailTypeDef",
    "FilterConditionTypeDef",
    "GetDataLakeSettingsRequestRequestTypeDef",
    "GetDataLakeSettingsResponseTypeDef",
    "GetEffectivePermissionsForPathRequestRequestTypeDef",
    "GetEffectivePermissionsForPathResponseTypeDef",
    "GetLFTagRequestRequestTypeDef",
    "GetLFTagResponseTypeDef",
    "GetResourceLFTagsRequestRequestTypeDef",
    "GetResourceLFTagsResponseTypeDef",
    "GrantPermissionsRequestRequestTypeDef",
    "LFTagErrorTypeDef",
    "LFTagKeyResourceTypeDef",
    "LFTagPairTypeDef",
    "LFTagPolicyResourceTypeDef",
    "LFTagTypeDef",
    "ListLFTagsRequestRequestTypeDef",
    "ListLFTagsResponseTypeDef",
    "ListPermissionsRequestRequestTypeDef",
    "ListPermissionsResponseTypeDef",
    "ListResourcesRequestRequestTypeDef",
    "ListResourcesResponseTypeDef",
    "PrincipalPermissionsTypeDef",
    "PrincipalResourcePermissionsTypeDef",
    "PutDataLakeSettingsRequestRequestTypeDef",
    "RegisterResourceRequestRequestTypeDef",
    "RemoveLFTagsFromResourceRequestRequestTypeDef",
    "RemoveLFTagsFromResourceResponseTypeDef",
    "ResourceInfoTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RevokePermissionsRequestRequestTypeDef",
    "SearchDatabasesByLFTagsRequestRequestTypeDef",
    "SearchDatabasesByLFTagsResponseTypeDef",
    "SearchTablesByLFTagsRequestRequestTypeDef",
    "SearchTablesByLFTagsResponseTypeDef",
    "TableResourceTypeDef",
    "TableWithColumnsResourceTypeDef",
    "TaggedDatabaseTypeDef",
    "TaggedTableTypeDef",
    "UpdateLFTagRequestRequestTypeDef",
    "UpdateResourceRequestRequestTypeDef",
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
        "TrustedResourceOwners": List[str],
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

FilterConditionTypeDef = TypedDict(
    "FilterConditionTypeDef",
    {
        "Field": FieldNameStringType,
        "ComparisonOperator": ComparisonOperatorType,
        "StringValueList": List[str],
    },
    total=False,
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

UpdateResourceRequestRequestTypeDef = TypedDict(
    "UpdateResourceRequestRequestTypeDef",
    {
        "RoleArn": str,
        "ResourceArn": str,
    },
)
