"""
Main interface for ssm-sap service.

Usage::

    ```python
    import boto3
    from mypy_boto3_ssm_sap import (
        Client,
        ListApplicationsPaginator,
        ListComponentsPaginator,
        ListDatabasesPaginator,
        SsmSapClient,
    )

    session = boto3.Session()

    client: SsmSapClient = boto3.client("ssm-sap")
    session_client: SsmSapClient = session.client("ssm-sap")

    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_components_paginator: ListComponentsPaginator = client.get_paginator("list_components")
    list_databases_paginator: ListDatabasesPaginator = client.get_paginator("list_databases")
    ```
"""
from .client import SsmSapClient
from .paginator import ListApplicationsPaginator, ListComponentsPaginator, ListDatabasesPaginator

Client = SsmSapClient

__all__ = (
    "Client",
    "ListApplicationsPaginator",
    "ListComponentsPaginator",
    "ListDatabasesPaginator",
    "SsmSapClient",
)
