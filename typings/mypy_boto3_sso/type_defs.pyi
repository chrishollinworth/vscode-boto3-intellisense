"""
Main interface for sso service type definitions.

Usage::

    ```python
    from mypy_boto3_sso.type_defs import AccountInfoTypeDef

    data: AccountInfoTypeDef = {...}
    ```
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountInfoTypeDef",
    "RoleCredentialsTypeDef",
    "RoleInfoTypeDef",
    "GetRoleCredentialsResponseTypeDef",
    "ListAccountRolesResponseTypeDef",
    "ListAccountsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

AccountInfoTypeDef = TypedDict(
    "AccountInfoTypeDef", {"accountId": str, "accountName": str, "emailAddress": str}, total=False
)

RoleCredentialsTypeDef = TypedDict(
    "RoleCredentialsTypeDef",
    {"accessKeyId": str, "secretAccessKey": str, "sessionToken": str, "expiration": int},
    total=False,
)

RoleInfoTypeDef = TypedDict("RoleInfoTypeDef", {"roleName": str, "accountId": str}, total=False)

GetRoleCredentialsResponseTypeDef = TypedDict(
    "GetRoleCredentialsResponseTypeDef", {"roleCredentials": "RoleCredentialsTypeDef"}, total=False
)

ListAccountRolesResponseTypeDef = TypedDict(
    "ListAccountRolesResponseTypeDef",
    {"nextToken": str, "roleList": List["RoleInfoTypeDef"]},
    total=False,
)

ListAccountsResponseTypeDef = TypedDict(
    "ListAccountsResponseTypeDef",
    {"nextToken": str, "accountList": List["AccountInfoTypeDef"]},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
