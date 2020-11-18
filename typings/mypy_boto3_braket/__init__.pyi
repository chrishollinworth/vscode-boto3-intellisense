"""
Main interface for braket service.

Usage::

    ```python
    import boto3
    from mypy_boto3_braket import (
        BraketClient,
        Client,
        SearchDevicesPaginator,
        SearchQuantumTasksPaginator,
    )

    session = boto3.Session()

    client: BraketClient = boto3.client("braket")
    session_client: BraketClient = session.client("braket")

    search_devices_paginator: SearchDevicesPaginator = client.get_paginator("search_devices")
    search_quantum_tasks_paginator: SearchQuantumTasksPaginator = client.get_paginator("search_quantum_tasks")
    ```
"""
from mypy_boto3_braket.client import BraketClient
from mypy_boto3_braket.paginator import SearchDevicesPaginator, SearchQuantumTasksPaginator

Client = BraketClient


__all__ = ("BraketClient", "Client", "SearchDevicesPaginator", "SearchQuantumTasksPaginator")
