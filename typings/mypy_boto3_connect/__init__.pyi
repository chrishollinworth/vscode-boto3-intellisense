"""
Main interface for connect service.

Usage::

    ```python
    import boto3
    from mypy_boto3_connect import (
        Client,
        ConnectClient,
        GetMetricDataPaginator,
        ListContactFlowsPaginator,
        ListHoursOfOperationsPaginator,
        ListPhoneNumbersPaginator,
        ListQueuesPaginator,
        ListRoutingProfilesPaginator,
        ListSecurityProfilesPaginator,
        ListUserHierarchyGroupsPaginator,
        ListUsersPaginator,
    )

    session = boto3.Session()

    client: ConnectClient = boto3.client("connect")
    session_client: ConnectClient = session.client("connect")

    get_metric_data_paginator: GetMetricDataPaginator = client.get_paginator("get_metric_data")
    list_contact_flows_paginator: ListContactFlowsPaginator = client.get_paginator("list_contact_flows")
    list_hours_of_operations_paginator: ListHoursOfOperationsPaginator = client.get_paginator("list_hours_of_operations")
    list_phone_numbers_paginator: ListPhoneNumbersPaginator = client.get_paginator("list_phone_numbers")
    list_queues_paginator: ListQueuesPaginator = client.get_paginator("list_queues")
    list_routing_profiles_paginator: ListRoutingProfilesPaginator = client.get_paginator("list_routing_profiles")
    list_security_profiles_paginator: ListSecurityProfilesPaginator = client.get_paginator("list_security_profiles")
    list_user_hierarchy_groups_paginator: ListUserHierarchyGroupsPaginator = client.get_paginator("list_user_hierarchy_groups")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    ```
"""
from mypy_boto3_connect.client import ConnectClient
from mypy_boto3_connect.paginator import (
    GetMetricDataPaginator,
    ListContactFlowsPaginator,
    ListHoursOfOperationsPaginator,
    ListPhoneNumbersPaginator,
    ListQueuesPaginator,
    ListRoutingProfilesPaginator,
    ListSecurityProfilesPaginator,
    ListUserHierarchyGroupsPaginator,
    ListUsersPaginator,
)

Client = ConnectClient


__all__ = (
    "Client",
    "ConnectClient",
    "GetMetricDataPaginator",
    "ListContactFlowsPaginator",
    "ListHoursOfOperationsPaginator",
    "ListPhoneNumbersPaginator",
    "ListQueuesPaginator",
    "ListRoutingProfilesPaginator",
    "ListSecurityProfilesPaginator",
    "ListUserHierarchyGroupsPaginator",
    "ListUsersPaginator",
)
