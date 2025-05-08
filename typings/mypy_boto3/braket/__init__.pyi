"""
Main interface for braket service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_braket import (
        BraketClient,
        Client,
        SearchDevicesPaginator,
        SearchJobsPaginator,
        SearchQuantumTasksPaginator,
    )

    session = Session()
    client: BraketClient = session.client("braket")

    search_devices_paginator: SearchDevicesPaginator = client.get_paginator("search_devices")
    search_jobs_paginator: SearchJobsPaginator = client.get_paginator("search_jobs")
    search_quantum_tasks_paginator: SearchQuantumTasksPaginator = client.get_paginator("search_quantum_tasks")
    ```
"""

from .client import BraketClient
from .paginator import SearchDevicesPaginator, SearchJobsPaginator, SearchQuantumTasksPaginator

Client = BraketClient

__all__ = (
    "BraketClient",
    "Client",
    "SearchDevicesPaginator",
    "SearchJobsPaginator",
    "SearchQuantumTasksPaginator",
)
