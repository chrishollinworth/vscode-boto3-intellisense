"""
Main interface for ssm-incidents service.

Usage::

    ```python
    import boto3
    from mypy_boto3_ssm_incidents import (
        Client,
        GetResourcePoliciesPaginator,
        ListIncidentRecordsPaginator,
        ListRelatedItemsPaginator,
        ListReplicationSetsPaginator,
        ListResponsePlansPaginator,
        ListTimelineEventsPaginator,
        SSMIncidentsClient,
        WaitForReplicationSetActiveWaiter,
        WaitForReplicationSetDeletedWaiter,
    )

    session = boto3.Session()

    client: SSMIncidentsClient = boto3.client("ssm-incidents")
    session_client: SSMIncidentsClient = session.client("ssm-incidents")

    wait_for_replication_set_active_waiter: WaitForReplicationSetActiveWaiter = client.get_waiter("wait_for_replication_set_active")
    wait_for_replication_set_deleted_waiter: WaitForReplicationSetDeletedWaiter = client.get_waiter("wait_for_replication_set_deleted")

    get_resource_policies_paginator: GetResourcePoliciesPaginator = client.get_paginator("get_resource_policies")
    list_incident_records_paginator: ListIncidentRecordsPaginator = client.get_paginator("list_incident_records")
    list_related_items_paginator: ListRelatedItemsPaginator = client.get_paginator("list_related_items")
    list_replication_sets_paginator: ListReplicationSetsPaginator = client.get_paginator("list_replication_sets")
    list_response_plans_paginator: ListResponsePlansPaginator = client.get_paginator("list_response_plans")
    list_timeline_events_paginator: ListTimelineEventsPaginator = client.get_paginator("list_timeline_events")
    ```
"""
from .client import SSMIncidentsClient
from .paginator import (
    GetResourcePoliciesPaginator,
    ListIncidentRecordsPaginator,
    ListRelatedItemsPaginator,
    ListReplicationSetsPaginator,
    ListResponsePlansPaginator,
    ListTimelineEventsPaginator,
)
from .waiter import WaitForReplicationSetActiveWaiter, WaitForReplicationSetDeletedWaiter

Client = SSMIncidentsClient

__all__ = (
    "Client",
    "GetResourcePoliciesPaginator",
    "ListIncidentRecordsPaginator",
    "ListRelatedItemsPaginator",
    "ListReplicationSetsPaginator",
    "ListResponsePlansPaginator",
    "ListTimelineEventsPaginator",
    "SSMIncidentsClient",
    "WaitForReplicationSetActiveWaiter",
    "WaitForReplicationSetDeletedWaiter",
)
