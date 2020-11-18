# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for secretsmanager service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_secretsmanager import SecretsManagerClient
    from mypy_boto3_secretsmanager.paginator import (
        ListSecretsPaginator,
    )

    client: SecretsManagerClient = boto3.client("secretsmanager")

    list_secrets_paginator: ListSecretsPaginator = client.get_paginator("list_secrets")
    ```
"""
import sys
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_secretsmanager.type_defs import (
    FilterTypeDef,
    ListSecretsResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ListSecretsPaginator",)


class ListSecretsPaginator(Boto3Paginator):
    """
    [Paginator.ListSecrets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/secretsmanager.html#SecretsManager.Paginator.ListSecrets)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        SortOrder: Literal["asc", "desc"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListSecretsResponseTypeDef]:
        """
        [ListSecrets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/secretsmanager.html#SecretsManager.Paginator.ListSecrets.paginate)
        """
