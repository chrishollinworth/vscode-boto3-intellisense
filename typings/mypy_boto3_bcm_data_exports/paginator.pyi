"""
Type annotations for bcm-data-exports service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_bcm_data_exports.client import BillingandCostManagementDataExportsClient
    from mypy_boto3_bcm_data_exports.paginator import (
        ListExecutionsPaginator,
        ListExportsPaginator,
        ListTablesPaginator,
    )

    session = Session()
    client: BillingandCostManagementDataExportsClient = session.client("bcm-data-exports")

    list_executions_paginator: ListExecutionsPaginator = client.get_paginator("list_executions")
    list_exports_paginator: ListExportsPaginator = client.get_paginator("list_exports")
    list_tables_paginator: ListTablesPaginator = client.get_paginator("list_tables")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListExecutionsRequestPaginateTypeDef,
    ListExecutionsResponseTypeDef,
    ListExportsRequestPaginateTypeDef,
    ListExportsResponseTypeDef,
    ListTablesRequestPaginateTypeDef,
    ListTablesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListExecutionsPaginator", "ListExportsPaginator", "ListTablesPaginator")

if TYPE_CHECKING:
    _ListExecutionsPaginatorBase = Paginator[ListExecutionsResponseTypeDef]
else:
    _ListExecutionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListExecutionsPaginator(_ListExecutionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports/paginator/ListExecutions.html#BillingandCostManagementDataExports.Paginator.ListExecutions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/paginators/#listexecutionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListExecutionsRequestPaginateTypeDef]
    ) -> PageIterator[ListExecutionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports/paginator/ListExecutions.html#BillingandCostManagementDataExports.Paginator.ListExecutions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/paginators/#listexecutionspaginator)
        """

if TYPE_CHECKING:
    _ListExportsPaginatorBase = Paginator[ListExportsResponseTypeDef]
else:
    _ListExportsPaginatorBase = Paginator  # type: ignore[assignment]

class ListExportsPaginator(_ListExportsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports/paginator/ListExports.html#BillingandCostManagementDataExports.Paginator.ListExports)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/paginators/#listexportspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListExportsRequestPaginateTypeDef]
    ) -> PageIterator[ListExportsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports/paginator/ListExports.html#BillingandCostManagementDataExports.Paginator.ListExports.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/paginators/#listexportspaginator)
        """

if TYPE_CHECKING:
    _ListTablesPaginatorBase = Paginator[ListTablesResponseTypeDef]
else:
    _ListTablesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTablesPaginator(_ListTablesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports/paginator/ListTables.html#BillingandCostManagementDataExports.Paginator.ListTables)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/paginators/#listtablespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTablesRequestPaginateTypeDef]
    ) -> PageIterator[ListTablesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-data-exports/paginator/ListTables.html#BillingandCostManagementDataExports.Paginator.ListTables.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/paginators/#listtablespaginator)
        """
