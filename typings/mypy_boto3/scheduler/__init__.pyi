"""
Main interface for scheduler service.

Usage::

    ```python
    import boto3
    from mypy_boto3_scheduler import (
        Client,
        EventBridgeSchedulerClient,
        ListScheduleGroupsPaginator,
        ListSchedulesPaginator,
    )

    session = boto3.Session()

    client: EventBridgeSchedulerClient = boto3.client("scheduler")
    session_client: EventBridgeSchedulerClient = session.client("scheduler")

    list_schedule_groups_paginator: ListScheduleGroupsPaginator = client.get_paginator("list_schedule_groups")
    list_schedules_paginator: ListSchedulesPaginator = client.get_paginator("list_schedules")
    ```
"""

from .client import EventBridgeSchedulerClient
from .paginator import ListScheduleGroupsPaginator, ListSchedulesPaginator

Client = EventBridgeSchedulerClient

__all__ = (
    "Client",
    "EventBridgeSchedulerClient",
    "ListScheduleGroupsPaginator",
    "ListSchedulesPaginator",
)
