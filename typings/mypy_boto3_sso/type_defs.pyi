"""
Type annotations for sso service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_sso.type_defs import AccountInfoTypeDef

    data: AccountInfoTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
else:
    from typing import Dict, List
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AccountInfoTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetRoleCredentialsRequestTypeDef",
    "GetRoleCredentialsResponseTypeDef",
    "ListAccountRolesRequestPaginateTypeDef",
    "ListAccountRolesRequestTypeDef",
    "ListAccountRolesResponseTypeDef",
    "ListAccountsRequestPaginateTypeDef",
    "ListAccountsRequestTypeDef",
    "ListAccountsResponseTypeDef",
    "LogoutRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RoleCredentialsTypeDef",
    "RoleInfoTypeDef",
)

class AccountInfoTypeDef(TypedDict):
    accountId: NotRequired[str]
    accountName: NotRequired[str]
    emailAddress: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class GetRoleCredentialsRequestTypeDef(TypedDict):
    roleName: str
    accountId: str
    accessToken: str

class RoleCredentialsTypeDef(TypedDict):
    accessKeyId: NotRequired[str]
    secretAccessKey: NotRequired[str]
    sessionToken: NotRequired[str]
    expiration: NotRequired[int]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAccountRolesRequestTypeDef(TypedDict):
    accessToken: str
    accountId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class RoleInfoTypeDef(TypedDict):
    roleName: NotRequired[str]
    accountId: NotRequired[str]

class ListAccountsRequestTypeDef(TypedDict):
    accessToken: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class LogoutRequestTypeDef(TypedDict):
    accessToken: str

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountsResponseTypeDef(TypedDict):
    accountList: List[AccountInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetRoleCredentialsResponseTypeDef(TypedDict):
    roleCredentials: RoleCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountRolesRequestPaginateTypeDef(TypedDict):
    accessToken: str
    accountId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAccountsRequestPaginateTypeDef(TypedDict):
    accessToken: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAccountRolesResponseTypeDef(TypedDict):
    roleList: List[RoleInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
