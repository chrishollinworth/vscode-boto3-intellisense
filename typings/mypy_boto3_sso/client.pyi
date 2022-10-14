"""
Type annotations for sso service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_sso import SSOClient

    client: SSOClient = boto3.client("sso")
    ```
"""
import sys
from typing import Any, Dict, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import ListAccountRolesPaginator, ListAccountsPaginator
from .type_defs import (
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

class SSOClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sso.html#SSO.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SSOClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sso.html#SSO.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sso.html#SSO.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso/client.html#close)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sso.html#SSO.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso/client.html#generate_presigned_url)
        """
    def get_role_credentials(
        self, *, roleName: str, accountId: str, accessToken: str
    ) -> GetRoleCredentialsResponseTypeDef:
        """
        Returns the STS short-term credentials for a given role name that is assigned to
        the user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sso.html#SSO.Client.get_role_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso/client.html#get_role_credentials)
        """
    def list_account_roles(
        self, *, accessToken: str, accountId: str, nextToken: str = None, maxResults: int = None
    ) -> ListAccountRolesResponseTypeDef:
        """
        Lists all roles that are assigned to the user for a given AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sso.html#SSO.Client.list_account_roles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso/client.html#list_account_roles)
        """
    def list_accounts(
        self, *, accessToken: str, nextToken: str = None, maxResults: int = None
    ) -> ListAccountsResponseTypeDef:
        """
        Lists all AWS accounts assigned to the user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sso.html#SSO.Client.list_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso/client.html#list_accounts)
        """
    def logout(self, *, accessToken: str) -> None:
        """
        Removes the locally stored SSO tokens from the client-side cache and sends an
        API call to the IAM Identity Center service to invalidate the corresponding
        server-side IAM Identity Center sign in session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sso.html#SSO.Client.logout)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso/client.html#logout)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_roles"]
    ) -> ListAccountRolesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sso.html#SSO.Paginator.ListAccountRoles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso/paginators.html#listaccountrolespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_accounts"]) -> ListAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/sso.html#SSO.Paginator.ListAccounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso/paginators.html#listaccountspaginator)
        """
