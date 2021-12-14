"""
Main interface for braket service.

Usage::

    ```python
    import boto3
    from mypy_boto3_braket import (
        BraketClient,
        Client,
        SearchDevicesPaginator,
        SearchJobsPaginator,
        SearchQuantumTasksPaginator,
    )

    session = boto3.Session()

    client: BraketClient = boto3.client("braket")
    session_client: BraketClient = session.client("braket")

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
