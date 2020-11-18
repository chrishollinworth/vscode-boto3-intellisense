"""
Main interface for lakeformation service type definitions.

Usage::

    ```python
    from mypy_boto3_lakeformation.type_defs import BatchPermissionsFailureEntryTypeDef

    data: BatchPermissionsFailureEntryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchPermissionsFailureEntryTypeDef",
    "BatchPermissionsRequestEntryTypeDef",
    "ColumnWildcardTypeDef",
    "DataLakePrincipalTypeDef",
    "DataLakeSettingsTypeDef",
    "DataLocationResourceTypeDef",
    "DatabaseResourceTypeDef",
    "DetailsMapTypeDef",
    "ErrorDetailTypeDef",
    "PrincipalPermissionsTypeDef",
    "PrincipalResourcePermissionsTypeDef",
    "ResourceInfoTypeDef",
    "ResourceTypeDef",
    "TableResourceTypeDef",
    "TableWithColumnsResourceTypeDef",
    "BatchGrantPermissionsResponseTypeDef",
    "BatchRevokePermissionsResponseTypeDef",
    "DescribeResourceResponseTypeDef",
    "FilterConditionTypeDef",
    "GetDataLakeSettingsResponseTypeDef",
    "GetEffectivePermissionsForPathResponseTypeDef",
    "ListPermissionsResponseTypeDef",
    "ListResourcesResponseTypeDef",
)

BatchPermissionsFailureEntryTypeDef = TypedDict(
    "BatchPermissionsFailureEntryTypeDef",
    {"RequestEntry": "BatchPermissionsRequestEntryTypeDef", "Error": "ErrorDetailTypeDef"},
    total=False,
)

_RequiredBatchPermissionsRequestEntryTypeDef = TypedDict(
    "_RequiredBatchPermissionsRequestEntryTypeDef", {"Id": str}
)
_OptionalBatchPermissionsRequestEntryTypeDef = TypedDict(
    "_OptionalBatchPermissionsRequestEntryTypeDef",
    {
        "Principal": "DataLakePrincipalTypeDef",
        "Resource": "ResourceTypeDef",
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "DESCRIBE",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
        "PermissionsWithGrantOption": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "DESCRIBE",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)


class BatchPermissionsRequestEntryTypeDef(
    _RequiredBatchPermissionsRequestEntryTypeDef, _OptionalBatchPermissionsRequestEntryTypeDef
):
    pass


ColumnWildcardTypeDef = TypedDict(
    "ColumnWildcardTypeDef", {"ExcludedColumnNames": List[str]}, total=False
)

DataLakePrincipalTypeDef = TypedDict(
    "DataLakePrincipalTypeDef", {"DataLakePrincipalIdentifier": str}, total=False
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
    "_RequiredDataLocationResourceTypeDef", {"ResourceArn": str}
)
_OptionalDataLocationResourceTypeDef = TypedDict(
    "_OptionalDataLocationResourceTypeDef", {"CatalogId": str}, total=False
)


class DataLocationResourceTypeDef(
    _RequiredDataLocationResourceTypeDef, _OptionalDataLocationResourceTypeDef
):
    pass


_RequiredDatabaseResourceTypeDef = TypedDict("_RequiredDatabaseResourceTypeDef", {"Name": str})
_OptionalDatabaseResourceTypeDef = TypedDict(
    "_OptionalDatabaseResourceTypeDef", {"CatalogId": str}, total=False
)


class DatabaseResourceTypeDef(_RequiredDatabaseResourceTypeDef, _OptionalDatabaseResourceTypeDef):
    pass


DetailsMapTypeDef = TypedDict("DetailsMapTypeDef", {"ResourceShare": List[str]}, total=False)

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef", {"ErrorCode": str, "ErrorMessage": str}, total=False
)

PrincipalPermissionsTypeDef = TypedDict(
    "PrincipalPermissionsTypeDef",
    {
        "Principal": "DataLakePrincipalTypeDef",
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "DESCRIBE",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)

PrincipalResourcePermissionsTypeDef = TypedDict(
    "PrincipalResourcePermissionsTypeDef",
    {
        "Principal": "DataLakePrincipalTypeDef",
        "Resource": "ResourceTypeDef",
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "DESCRIBE",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
        "PermissionsWithGrantOption": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "DESCRIBE",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
        "AdditionalDetails": "DetailsMapTypeDef",
    },
    total=False,
)

ResourceInfoTypeDef = TypedDict(
    "ResourceInfoTypeDef",
    {"ResourceArn": str, "RoleArn": str, "LastModified": datetime},
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
    },
    total=False,
)

_RequiredTableResourceTypeDef = TypedDict("_RequiredTableResourceTypeDef", {"DatabaseName": str})
_OptionalTableResourceTypeDef = TypedDict(
    "_OptionalTableResourceTypeDef",
    {"CatalogId": str, "Name": str, "TableWildcard": Dict[str, Any]},
    total=False,
)


class TableResourceTypeDef(_RequiredTableResourceTypeDef, _OptionalTableResourceTypeDef):
    pass


_RequiredTableWithColumnsResourceTypeDef = TypedDict(
    "_RequiredTableWithColumnsResourceTypeDef", {"DatabaseName": str, "Name": str}
)
_OptionalTableWithColumnsResourceTypeDef = TypedDict(
    "_OptionalTableWithColumnsResourceTypeDef",
    {"CatalogId": str, "ColumnNames": List[str], "ColumnWildcard": "ColumnWildcardTypeDef"},
    total=False,
)


class TableWithColumnsResourceTypeDef(
    _RequiredTableWithColumnsResourceTypeDef, _OptionalTableWithColumnsResourceTypeDef
):
    pass


BatchGrantPermissionsResponseTypeDef = TypedDict(
    "BatchGrantPermissionsResponseTypeDef",
    {"Failures": List["BatchPermissionsFailureEntryTypeDef"]},
    total=False,
)

BatchRevokePermissionsResponseTypeDef = TypedDict(
    "BatchRevokePermissionsResponseTypeDef",
    {"Failures": List["BatchPermissionsFailureEntryTypeDef"]},
    total=False,
)

DescribeResourceResponseTypeDef = TypedDict(
    "DescribeResourceResponseTypeDef", {"ResourceInfo": "ResourceInfoTypeDef"}, total=False
)

FilterConditionTypeDef = TypedDict(
    "FilterConditionTypeDef",
    {
        "Field": Literal["RESOURCE_ARN", "ROLE_ARN", "LAST_MODIFIED"],
        "ComparisonOperator": Literal[
            "EQ",
            "NE",
            "LE",
            "LT",
            "GE",
            "GT",
            "CONTAINS",
            "NOT_CONTAINS",
            "BEGINS_WITH",
            "IN",
            "BETWEEN",
        ],
        "StringValueList": List[str],
    },
    total=False,
)

GetDataLakeSettingsResponseTypeDef = TypedDict(
    "GetDataLakeSettingsResponseTypeDef",
    {"DataLakeSettings": "DataLakeSettingsTypeDef"},
    total=False,
)

GetEffectivePermissionsForPathResponseTypeDef = TypedDict(
    "GetEffectivePermissionsForPathResponseTypeDef",
    {"Permissions": List["PrincipalResourcePermissionsTypeDef"], "NextToken": str},
    total=False,
)

ListPermissionsResponseTypeDef = TypedDict(
    "ListPermissionsResponseTypeDef",
    {"PrincipalResourcePermissions": List["PrincipalResourcePermissionsTypeDef"], "NextToken": str},
    total=False,
)

ListResourcesResponseTypeDef = TypedDict(
    "ListResourcesResponseTypeDef",
    {"ResourceInfoList": List["ResourceInfoTypeDef"], "NextToken": str},
    total=False,
)
