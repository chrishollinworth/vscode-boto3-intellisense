"""
Type annotations for sso service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sso.client import SSOClient

    session = Session()
    client: SSOClient = session.client("sso")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListAccountRolesPaginator, ListAccountsPaginator
from .type_defs import (
    EmptyResponseMetadataTypeDef,
    GetRoleCredentialsRequestTypeDef,
    GetRoleCredentialsResponseTypeDef,
    ListAccountRolesRequestTypeDef,
    ListAccountRolesResponseTypeDef,
    ListAccountsRequestTypeDef,
    ListAccountsResponseTypeDef,
    LogoutRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("SSOClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]

class SSOClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso.html#SSO.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SSOClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso.html#SSO.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso/client/#generate_presigned_url)
        """

    def get_role_credentials(
        self, **kwargs: Unpack[GetRoleCredentialsRequestTypeDef]
    ) -> GetRoleCredentialsResponseTypeDef:
        """
        Returns the STS short-term credentials for a given role name that is assigned
        to the user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso/client/get_role_credentials.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso/client/#get_role_credentials)
        """

    def list_account_roles(
        self, **kwargs: Unpack[ListAccountRolesRequestTypeDef]
    ) -> ListAccountRolesResponseTypeDef:
        """
        Lists all roles that are assigned to the user for a given AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso/client/list_account_roles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso/client/#list_account_roles)
        """

    def list_accounts(
        self, **kwargs: Unpack[ListAccountsRequestTypeDef]
    ) -> ListAccountsResponseTypeDef:
        """
        Lists all AWS accounts assigned to the user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso/client/list_accounts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso/client/#list_accounts)
        """

    def logout(self, **kwargs: Unpack[LogoutRequestTypeDef]) -> EmptyResponseMetadataTypeDef:
        """
        Removes the locally stored SSO tokens from the client-side cache and sends an
        API call to the IAM Identity Center service to invalidate the corresponding
        server-side IAM Identity Center sign in session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso/client/logout.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso/client/#logout)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_account_roles"]
    ) -> ListAccountRolesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_accounts"]
    ) -> ListAccountsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso/client/#get_paginator)
        """
