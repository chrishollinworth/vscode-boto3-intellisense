"""
Type annotations for cognito-identity service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_cognito_identity.client import CognitoIdentityClient
    from mypy_boto3_cognito_identity.paginator import (
        ListIdentityPoolsPaginator,
    )

    session = Session()
    client: CognitoIdentityClient = session.client("cognito-identity")

    list_identity_pools_paginator: ListIdentityPoolsPaginator = client.get_paginator("list_identity_pools")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListIdentityPoolsInputPaginateTypeDef, ListIdentityPoolsResponseTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListIdentityPoolsPaginator",)

if TYPE_CHECKING:
    _ListIdentityPoolsPaginatorBase = Paginator[ListIdentityPoolsResponseTypeDef]
else:
    _ListIdentityPoolsPaginatorBase = Paginator  # type: ignore[assignment]

class ListIdentityPoolsPaginator(_ListIdentityPoolsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/paginator/ListIdentityPools.html#CognitoIdentity.Paginator.ListIdentityPools)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/paginators/#listidentitypoolspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIdentityPoolsInputPaginateTypeDef]
    ) -> PageIterator[ListIdentityPoolsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/paginator/ListIdentityPools.html#CognitoIdentity.Paginator.ListIdentityPools.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/paginators/#listidentitypoolspaginator)
        """
