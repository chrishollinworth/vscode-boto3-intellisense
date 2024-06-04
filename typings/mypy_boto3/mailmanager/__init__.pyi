"""
Main interface for mailmanager service.

Usage::

    ```python
    import boto3
    from mypy_boto3_mailmanager import (
        Client,
        ListAddonInstancesPaginator,
        ListAddonSubscriptionsPaginator,
        ListArchiveExportsPaginator,
        ListArchiveSearchesPaginator,
        ListArchivesPaginator,
        ListIngressPointsPaginator,
        ListRelaysPaginator,
        ListRuleSetsPaginator,
        ListTrafficPoliciesPaginator,
        MailManagerClient,
    )

    session = boto3.Session()

    client: MailManagerClient = boto3.client("mailmanager")
    session_client: MailManagerClient = session.client("mailmanager")

    list_addon_instances_paginator: ListAddonInstancesPaginator = client.get_paginator("list_addon_instances")
    list_addon_subscriptions_paginator: ListAddonSubscriptionsPaginator = client.get_paginator("list_addon_subscriptions")
    list_archive_exports_paginator: ListArchiveExportsPaginator = client.get_paginator("list_archive_exports")
    list_archive_searches_paginator: ListArchiveSearchesPaginator = client.get_paginator("list_archive_searches")
    list_archives_paginator: ListArchivesPaginator = client.get_paginator("list_archives")
    list_ingress_points_paginator: ListIngressPointsPaginator = client.get_paginator("list_ingress_points")
    list_relays_paginator: ListRelaysPaginator = client.get_paginator("list_relays")
    list_rule_sets_paginator: ListRuleSetsPaginator = client.get_paginator("list_rule_sets")
    list_traffic_policies_paginator: ListTrafficPoliciesPaginator = client.get_paginator("list_traffic_policies")
    ```
"""

from .client import MailManagerClient
from .paginator import (
    ListAddonInstancesPaginator,
    ListAddonSubscriptionsPaginator,
    ListArchiveExportsPaginator,
    ListArchiveSearchesPaginator,
    ListArchivesPaginator,
    ListIngressPointsPaginator,
    ListRelaysPaginator,
    ListRuleSetsPaginator,
    ListTrafficPoliciesPaginator,
)

Client = MailManagerClient

__all__ = (
    "Client",
    "ListAddonInstancesPaginator",
    "ListAddonSubscriptionsPaginator",
    "ListArchiveExportsPaginator",
    "ListArchiveSearchesPaginator",
    "ListArchivesPaginator",
    "ListIngressPointsPaginator",
    "ListRelaysPaginator",
    "ListRuleSetsPaginator",
    "ListTrafficPoliciesPaginator",
    "MailManagerClient",
)
