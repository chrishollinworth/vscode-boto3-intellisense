"""
Main interface for dataexchange service.

Usage::

    ```python
    import boto3
    from mypy_boto3_dataexchange import (
        Client,
        DataExchangeClient,
        ListDataSetRevisionsPaginator,
        ListDataSetsPaginator,
        ListJobsPaginator,
        ListRevisionAssetsPaginator,
    )

    session = boto3.Session()

    client: DataExchangeClient = boto3.client("dataexchange")
    session_client: DataExchangeClient = session.client("dataexchange")

    list_data_set_revisions_paginator: ListDataSetRevisionsPaginator = client.get_paginator("list_data_set_revisions")
    list_data_sets_paginator: ListDataSetsPaginator = client.get_paginator("list_data_sets")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    list_revision_assets_paginator: ListRevisionAssetsPaginator = client.get_paginator("list_revision_assets")
    ```
"""
from mypy_boto3_dataexchange.client import DataExchangeClient
from mypy_boto3_dataexchange.paginator import (
    ListDataSetRevisionsPaginator,
    ListDataSetsPaginator,
    ListJobsPaginator,
    ListRevisionAssetsPaginator,
)

Client = DataExchangeClient


__all__ = (
    "Client",
    "DataExchangeClient",
    "ListDataSetRevisionsPaginator",
    "ListDataSetsPaginator",
    "ListJobsPaginator",
    "ListRevisionAssetsPaginator",
)
