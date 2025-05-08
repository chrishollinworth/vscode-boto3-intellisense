"""
Main interface for dataexchange service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_dataexchange import (
        Client,
        DataExchangeClient,
        ListDataGrantsPaginator,
        ListDataSetRevisionsPaginator,
        ListDataSetsPaginator,
        ListEventActionsPaginator,
        ListJobsPaginator,
        ListReceivedDataGrantsPaginator,
        ListRevisionAssetsPaginator,
    )

    session = Session()
    client: DataExchangeClient = session.client("dataexchange")

    list_data_grants_paginator: ListDataGrantsPaginator = client.get_paginator("list_data_grants")
    list_data_set_revisions_paginator: ListDataSetRevisionsPaginator = client.get_paginator("list_data_set_revisions")
    list_data_sets_paginator: ListDataSetsPaginator = client.get_paginator("list_data_sets")
    list_event_actions_paginator: ListEventActionsPaginator = client.get_paginator("list_event_actions")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    list_received_data_grants_paginator: ListReceivedDataGrantsPaginator = client.get_paginator("list_received_data_grants")
    list_revision_assets_paginator: ListRevisionAssetsPaginator = client.get_paginator("list_revision_assets")
    ```
"""

from .client import DataExchangeClient
from .paginator import (
    ListDataGrantsPaginator,
    ListDataSetRevisionsPaginator,
    ListDataSetsPaginator,
    ListEventActionsPaginator,
    ListJobsPaginator,
    ListReceivedDataGrantsPaginator,
    ListRevisionAssetsPaginator,
)

Client = DataExchangeClient

__all__ = (
    "Client",
    "DataExchangeClient",
    "ListDataGrantsPaginator",
    "ListDataSetRevisionsPaginator",
    "ListDataSetsPaginator",
    "ListEventActionsPaginator",
    "ListJobsPaginator",
    "ListReceivedDataGrantsPaginator",
    "ListRevisionAssetsPaginator",
)
