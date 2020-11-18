"""
Main interface for redshift-data service.

Usage::

    ```python
    import boto3
    from mypy_boto3_redshift_data import (
        Client,
        DescribeTablePaginator,
        GetStatementResultPaginator,
        ListDatabasesPaginator,
        ListSchemasPaginator,
        ListStatementsPaginator,
        ListTablesPaginator,
        RedshiftDataAPIServiceClient,
    )

    session = boto3.Session()

    client: RedshiftDataAPIServiceClient = boto3.client("redshift-data")
    session_client: RedshiftDataAPIServiceClient = session.client("redshift-data")

    describe_table_paginator: DescribeTablePaginator = client.get_paginator("describe_table")
    get_statement_result_paginator: GetStatementResultPaginator = client.get_paginator("get_statement_result")
    list_databases_paginator: ListDatabasesPaginator = client.get_paginator("list_databases")
    list_schemas_paginator: ListSchemasPaginator = client.get_paginator("list_schemas")
    list_statements_paginator: ListStatementsPaginator = client.get_paginator("list_statements")
    list_tables_paginator: ListTablesPaginator = client.get_paginator("list_tables")
    ```
"""
from mypy_boto3_redshift_data.client import RedshiftDataAPIServiceClient
from mypy_boto3_redshift_data.paginator import (
    DescribeTablePaginator,
    GetStatementResultPaginator,
    ListDatabasesPaginator,
    ListSchemasPaginator,
    ListStatementsPaginator,
    ListTablesPaginator,
)

Client = RedshiftDataAPIServiceClient


__all__ = (
    "Client",
    "DescribeTablePaginator",
    "GetStatementResultPaginator",
    "ListDatabasesPaginator",
    "ListSchemasPaginator",
    "ListStatementsPaginator",
    "ListTablesPaginator",
    "RedshiftDataAPIServiceClient",
)
