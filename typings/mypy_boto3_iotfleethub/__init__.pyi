"""
Main interface for iotfleethub service.

Usage::

    ```python
    import boto3
    from mypy_boto3_iotfleethub import (
        Client,
        IoTFleetHubClient,
        ListApplicationsPaginator,
    )

    session = boto3.Session()

    client: IoTFleetHubClient = boto3.client("iotfleethub")
    session_client: IoTFleetHubClient = session.client("iotfleethub")

    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    ```
"""
from mypy_boto3_iotfleethub.client import IoTFleetHubClient
from mypy_boto3_iotfleethub.paginator import ListApplicationsPaginator

Client = IoTFleetHubClient


__all__ = ("Client", "IoTFleetHubClient", "ListApplicationsPaginator")
