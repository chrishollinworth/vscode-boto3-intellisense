# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for sso service client

Usage::

    ```python
    import boto3
    from mypy_boto3_sso import SSOClient

    client: SSOClient = boto3.client("sso")
    ```
"""
import sys
from typing import Any, Dict, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_sso.paginator import ListAccountRolesPaginator, ListAccountsPaginator
from mypy_boto3_sso.type_defs import (
    GetRoleCredentialsResponseTypeDef,
    ListAccountRolesResponseTypeDef,
    ListAccountsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SSOClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]


class SSOClient:
    """
    [SSO.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso.html#SSO.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso.html#SSO.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso.html#SSO.Client.generate_presigned_url)
        """

    def get_role_credentials(
        self, roleName: str, accountId: str, accessToken: str
    ) -> GetRoleCredentialsResponseTypeDef:
        """
        [Client.get_role_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso.html#SSO.Client.get_role_credentials)
        """

    def list_account_roles(
        self, accessToken: str, accountId: str, nextToken: str = None, maxResults: int = None
    ) -> ListAccountRolesResponseTypeDef:
        """
        [Client.list_account_roles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso.html#SSO.Client.list_account_roles)
        """

    def list_accounts(
        self, accessToken: str, nextToken: str = None, maxResults: int = None
    ) -> ListAccountsResponseTypeDef:
        """
        [Client.list_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso.html#SSO.Client.list_accounts)
        """

    def logout(self, accessToken: str) -> None:
        """
        [Client.logout documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso.html#SSO.Client.logout)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_roles"]
    ) -> ListAccountRolesPaginator:
        """
        [Paginator.ListAccountRoles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso.html#SSO.Paginator.ListAccountRoles)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_accounts"]) -> ListAccountsPaginator:
        """
        [Paginator.ListAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso.html#SSO.Paginator.ListAccounts)
        """
