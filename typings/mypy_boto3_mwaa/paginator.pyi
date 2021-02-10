"""
Main interface for mwaa service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_mwaa import MWAAClient
    from mypy_boto3_mwaa.paginator import (
        ListEnvironmentsPaginator,
    )

    client: MWAAClient = boto3.client("mwaa")

    list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_mwaa.type_defs import ListEnvironmentsOutputTypeDef, PaginatorConfigTypeDef

__all__ = ("ListEnvironmentsPaginator",)


class ListEnvironmentsPaginator(Boto3Paginator):
    """
    [Paginator.ListEnvironments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/mwaa.html#MWAA.Paginator.ListEnvironments)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnvironmentsOutputTypeDef]:
        """
        [ListEnvironments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/mwaa.html#MWAA.Paginator.ListEnvironments.paginate)
        """
