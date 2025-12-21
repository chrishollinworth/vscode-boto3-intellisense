"""
Main interface for controlcatalog service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_controlcatalog import (
        Client,
        ControlCatalogClient,
        ListCommonControlsPaginator,
        ListControlMappingsPaginator,
        ListControlsPaginator,
        ListDomainsPaginator,
        ListObjectivesPaginator,
    )

    session = Session()
    client: ControlCatalogClient = session.client("controlcatalog")

    list_common_controls_paginator: ListCommonControlsPaginator = client.get_paginator("list_common_controls")
    list_control_mappings_paginator: ListControlMappingsPaginator = client.get_paginator("list_control_mappings")
    list_controls_paginator: ListControlsPaginator = client.get_paginator("list_controls")
    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_objectives_paginator: ListObjectivesPaginator = client.get_paginator("list_objectives")
    ```
"""

from .client import ControlCatalogClient
from .paginator import (
    ListCommonControlsPaginator,
    ListControlMappingsPaginator,
    ListControlsPaginator,
    ListDomainsPaginator,
    ListObjectivesPaginator,
)

Client = ControlCatalogClient

__all__ = (
    "Client",
    "ControlCatalogClient",
    "ListCommonControlsPaginator",
    "ListControlMappingsPaginator",
    "ListControlsPaginator",
    "ListDomainsPaginator",
    "ListObjectivesPaginator",
)
