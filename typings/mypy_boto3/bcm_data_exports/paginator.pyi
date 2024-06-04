"""
Type annotations for bcm-data-exports service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_bcm_data_exports import BillingandCostManagementDataExportsClient
    from mypy_boto3_bcm_data_exports.paginator import (
        ListExecutionsPaginator,
        ListExportsPaginator,
        ListTablesPaginator,
    )

    client: BillingandCostManagementDataExportsClient = boto3.client("bcm-data-exports")

    list_executions_paginator: ListExecutionsPaginator = client.get_paginator("list_executions")
    list_exports_paginator: ListExportsPaginator = client.get_paginator("list_exports")
    list_tables_paginator: ListTablesPaginator = client.get_paginator("list_tables")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListExecutionsResponseTypeDef,
    ListExportsResponseTypeDef,
    ListTablesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListExecutionsPaginator", "ListExportsPaginator", "ListTablesPaginator")

class ListExecutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Paginator.ListExecutions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/paginators.html#listexecutionspaginator)
    """

    def paginate(
        self, *, ExportArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListExecutionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Paginator.ListExecutions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/paginators.html#listexecutionspaginator)
        """

class ListExportsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Paginator.ListExports)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/paginators.html#listexportspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListExportsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Paginator.ListExports.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/paginators.html#listexportspaginator)
        """

class ListTablesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Paginator.ListTables)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/paginators.html#listtablespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTablesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bcm-data-exports.html#BillingandCostManagementDataExports.Paginator.ListTables.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/paginators.html#listtablespaginator)
        """
