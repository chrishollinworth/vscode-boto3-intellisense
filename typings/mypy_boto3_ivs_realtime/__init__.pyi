"""
Main interface for ivs-realtime service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ivs_realtime import (
        Client,
        IvsrealtimeClient,
        ListIngestConfigurationsPaginator,
        ListPublicKeysPaginator,
    )

    session = Session()
    client: IvsrealtimeClient = session.client("ivs-realtime")

    list_ingest_configurations_paginator: ListIngestConfigurationsPaginator = client.get_paginator("list_ingest_configurations")
    list_public_keys_paginator: ListPublicKeysPaginator = client.get_paginator("list_public_keys")
    ```
"""

from .client import IvsrealtimeClient
from .paginator import ListIngestConfigurationsPaginator, ListPublicKeysPaginator

Client = IvsrealtimeClient

__all__ = (
    "Client",
    "IvsrealtimeClient",
    "ListIngestConfigurationsPaginator",
    "ListPublicKeysPaginator",
)
