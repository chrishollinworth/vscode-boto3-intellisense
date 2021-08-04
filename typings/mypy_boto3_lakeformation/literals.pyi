"""
Type annotations for lakeformation service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/literals.html)

Usage::

    ```python
    from mypy_boto3_lakeformation.literals import ComparisonOperatorType

    data: ComparisonOperatorType = "BEGINS_WITH"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ComparisonOperatorType",
    "DataLakeResourceTypeType",
    "FieldNameStringType",
    "PermissionType",
    "ResourceShareTypeType",
    "ResourceTypeType",
)

ComparisonOperatorType = Literal[
    "BEGINS_WITH", "BETWEEN", "CONTAINS", "EQ", "GE", "GT", "IN", "LE", "LT", "NE", "NOT_CONTAINS"
]
DataLakeResourceTypeType = Literal[
    "CATALOG",
    "DATABASE",
    "DATA_LOCATION",
    "LF_TAG",
    "LF_TAG_POLICY",
    "LF_TAG_POLICY_DATABASE",
    "LF_TAG_POLICY_TABLE",
    "TABLE",
]
FieldNameStringType = Literal["LAST_MODIFIED", "RESOURCE_ARN", "ROLE_ARN"]
PermissionType = Literal[
    "ALL",
    "ALTER",
    "ALTER_TAG",
    "ASSOCIATE_TAG",
    "CREATE_DATABASE",
    "CREATE_TABLE",
    "CREATE_TAG",
    "DATA_LOCATION_ACCESS",
    "DELETE",
    "DELETE_TAG",
    "DESCRIBE",
    "DESCRIBE_TAG",
    "DROP",
    "INSERT",
    "SELECT",
]
ResourceShareTypeType = Literal["ALL", "FOREIGN"]
ResourceTypeType = Literal["DATABASE", "TABLE"]
