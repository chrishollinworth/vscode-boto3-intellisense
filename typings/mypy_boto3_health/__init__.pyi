"""
Main interface for health service.

Usage::

    ```python
    import boto3
    from mypy_boto3_health import (
        Client,
        DescribeAffectedAccountsForOrganizationPaginator,
        DescribeAffectedEntitiesForOrganizationPaginator,
        DescribeAffectedEntitiesPaginator,
        DescribeEventAggregatesPaginator,
        DescribeEventTypesPaginator,
        DescribeEventsForOrganizationPaginator,
        DescribeEventsPaginator,
        HealthClient,
    )

    session = boto3.Session()

    client: HealthClient = boto3.client("health")
    session_client: HealthClient = session.client("health")

    describe_affected_accounts_for_organization_paginator: DescribeAffectedAccountsForOrganizationPaginator = client.get_paginator("describe_affected_accounts_for_organization")
    describe_affected_entities_paginator: DescribeAffectedEntitiesPaginator = client.get_paginator("describe_affected_entities")
    describe_affected_entities_for_organization_paginator: DescribeAffectedEntitiesForOrganizationPaginator = client.get_paginator("describe_affected_entities_for_organization")
    describe_event_aggregates_paginator: DescribeEventAggregatesPaginator = client.get_paginator("describe_event_aggregates")
    describe_event_types_paginator: DescribeEventTypesPaginator = client.get_paginator("describe_event_types")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_events_for_organization_paginator: DescribeEventsForOrganizationPaginator = client.get_paginator("describe_events_for_organization")
    ```
"""
from mypy_boto3_health.client import HealthClient
from mypy_boto3_health.paginator import (
    DescribeAffectedAccountsForOrganizationPaginator,
    DescribeAffectedEntitiesForOrganizationPaginator,
    DescribeAffectedEntitiesPaginator,
    DescribeEventAggregatesPaginator,
    DescribeEventsForOrganizationPaginator,
    DescribeEventsPaginator,
    DescribeEventTypesPaginator,
)

Client = HealthClient


__all__ = (
    "Client",
    "DescribeAffectedAccountsForOrganizationPaginator",
    "DescribeAffectedEntitiesForOrganizationPaginator",
    "DescribeAffectedEntitiesPaginator",
    "DescribeEventAggregatesPaginator",
    "DescribeEventTypesPaginator",
    "DescribeEventsForOrganizationPaginator",
    "DescribeEventsPaginator",
    "HealthClient",
)
