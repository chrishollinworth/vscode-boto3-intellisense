# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for cognito-identity service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_cognito_identity import CognitoIdentityClient
    from mypy_boto3_cognito_identity.paginator import (
        ListIdentityPoolsPaginator,
    )

    client: CognitoIdentityClient = boto3.client("cognito-identity")

    list_identity_pools_paginator: ListIdentityPoolsPaginator = client.get_paginator("list_identity_pools")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_cognito_identity.type_defs import (
    ListIdentityPoolsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListIdentityPoolsPaginator",)


class ListIdentityPoolsPaginator(Boto3Paginator):
    """
    [Paginator.ListIdentityPools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-identity.html#CognitoIdentity.Paginator.ListIdentityPools)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIdentityPoolsResponseTypeDef]:
        """
        [ListIdentityPools.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-identity.html#CognitoIdentity.Paginator.ListIdentityPools.paginate)
        """
