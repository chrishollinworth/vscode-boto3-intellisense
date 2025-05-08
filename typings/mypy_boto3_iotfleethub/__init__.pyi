"""
Main interface for iotfleethub service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleethub/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_iotfleethub import (
        Client,
        IoTFleetHubClient,
        ListApplicationsPaginator,
    )

    session = Session()
    client: IoTFleetHubClient = session.client("iotfleethub")

    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    ```
"""

from .client import IoTFleetHubClient
from .paginator import ListApplicationsPaginator

Client = IoTFleetHubClient

__all__ = ("Client", "IoTFleetHubClient", "ListApplicationsPaginator")
