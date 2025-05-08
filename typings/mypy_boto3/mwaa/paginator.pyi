"""
Type annotations for mwaa service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_mwaa.client import MWAAClient
    from mypy_boto3_mwaa.paginator import (
        ListEnvironmentsPaginator,
    )

    session = Session()
    client: MWAAClient = session.client("mwaa")

    list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListEnvironmentsInputPaginateTypeDef, ListEnvironmentsOutputTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListEnvironmentsPaginator",)

if TYPE_CHECKING:
    _ListEnvironmentsPaginatorBase = Paginator[ListEnvironmentsOutputTypeDef]
else:
    _ListEnvironmentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnvironmentsPaginator(_ListEnvironmentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa/paginator/ListEnvironments.html#MWAA.Paginator.ListEnvironments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/paginators/#listenvironmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnvironmentsInputPaginateTypeDef]
    ) -> PageIterator[ListEnvironmentsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa/paginator/ListEnvironments.html#MWAA.Paginator.ListEnvironments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa/paginators/#listenvironmentspaginator)
        """
