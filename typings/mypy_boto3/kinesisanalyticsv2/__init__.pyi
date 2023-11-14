"""
Main interface for kinesisanalyticsv2 service.

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesisanalyticsv2 import (
        Client,
        KinesisAnalyticsV2Client,
        ListApplicationSnapshotsPaginator,
        ListApplicationsPaginator,
    )

    session = boto3.Session()

    client: KinesisAnalyticsV2Client = boto3.client("kinesisanalyticsv2")
    session_client: KinesisAnalyticsV2Client = session.client("kinesisanalyticsv2")

    list_application_snapshots_paginator: ListApplicationSnapshotsPaginator = client.get_paginator("list_application_snapshots")
    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    ```
"""
from .client import KinesisAnalyticsV2Client
from .paginator import ListApplicationSnapshotsPaginator, ListApplicationsPaginator

Client = KinesisAnalyticsV2Client

__all__ = (
    "Client",
    "KinesisAnalyticsV2Client",
    "ListApplicationSnapshotsPaginator",
    "ListApplicationsPaginator",
)
