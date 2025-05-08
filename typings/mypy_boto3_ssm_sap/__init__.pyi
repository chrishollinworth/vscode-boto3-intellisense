"""
Main interface for ssm-sap service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ssm_sap import (
        Client,
        ListApplicationsPaginator,
        ListComponentsPaginator,
        ListDatabasesPaginator,
        ListOperationEventsPaginator,
        ListOperationsPaginator,
        SsmSapClient,
    )

    session = Session()
    client: SsmSapClient = session.client("ssm-sap")

    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_components_paginator: ListComponentsPaginator = client.get_paginator("list_components")
    list_databases_paginator: ListDatabasesPaginator = client.get_paginator("list_databases")
    list_operation_events_paginator: ListOperationEventsPaginator = client.get_paginator("list_operation_events")
    list_operations_paginator: ListOperationsPaginator = client.get_paginator("list_operations")
    ```
"""

from .client import SsmSapClient
from .paginator import (
    ListApplicationsPaginator,
    ListComponentsPaginator,
    ListDatabasesPaginator,
    ListOperationEventsPaginator,
    ListOperationsPaginator,
)

Client = SsmSapClient

__all__ = (
    "Client",
    "ListApplicationsPaginator",
    "ListComponentsPaginator",
    "ListDatabasesPaginator",
    "ListOperationEventsPaginator",
    "ListOperationsPaginator",
    "SsmSapClient",
)
