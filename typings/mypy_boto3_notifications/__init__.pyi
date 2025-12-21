"""
Main interface for notifications service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notifications/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_notifications import (
        Client,
        ListChannelsPaginator,
        ListEventRulesPaginator,
        ListManagedNotificationChannelAssociationsPaginator,
        ListManagedNotificationChildEventsPaginator,
        ListManagedNotificationConfigurationsPaginator,
        ListManagedNotificationEventsPaginator,
        ListMemberAccountsPaginator,
        ListNotificationConfigurationsPaginator,
        ListNotificationEventsPaginator,
        ListNotificationHubsPaginator,
        ListOrganizationalUnitsPaginator,
        UserNotificationsClient,
    )

    session = Session()
    client: UserNotificationsClient = session.client("notifications")

    list_channels_paginator: ListChannelsPaginator = client.get_paginator("list_channels")
    list_event_rules_paginator: ListEventRulesPaginator = client.get_paginator("list_event_rules")
    list_managed_notification_channel_associations_paginator: ListManagedNotificationChannelAssociationsPaginator = client.get_paginator("list_managed_notification_channel_associations")
    list_managed_notification_child_events_paginator: ListManagedNotificationChildEventsPaginator = client.get_paginator("list_managed_notification_child_events")
    list_managed_notification_configurations_paginator: ListManagedNotificationConfigurationsPaginator = client.get_paginator("list_managed_notification_configurations")
    list_managed_notification_events_paginator: ListManagedNotificationEventsPaginator = client.get_paginator("list_managed_notification_events")
    list_member_accounts_paginator: ListMemberAccountsPaginator = client.get_paginator("list_member_accounts")
    list_notification_configurations_paginator: ListNotificationConfigurationsPaginator = client.get_paginator("list_notification_configurations")
    list_notification_events_paginator: ListNotificationEventsPaginator = client.get_paginator("list_notification_events")
    list_notification_hubs_paginator: ListNotificationHubsPaginator = client.get_paginator("list_notification_hubs")
    list_organizational_units_paginator: ListOrganizationalUnitsPaginator = client.get_paginator("list_organizational_units")
    ```
"""

from .client import UserNotificationsClient
from .paginator import (
    ListChannelsPaginator,
    ListEventRulesPaginator,
    ListManagedNotificationChannelAssociationsPaginator,
    ListManagedNotificationChildEventsPaginator,
    ListManagedNotificationConfigurationsPaginator,
    ListManagedNotificationEventsPaginator,
    ListMemberAccountsPaginator,
    ListNotificationConfigurationsPaginator,
    ListNotificationEventsPaginator,
    ListNotificationHubsPaginator,
    ListOrganizationalUnitsPaginator,
)

Client = UserNotificationsClient

__all__ = (
    "Client",
    "ListChannelsPaginator",
    "ListEventRulesPaginator",
    "ListManagedNotificationChannelAssociationsPaginator",
    "ListManagedNotificationChildEventsPaginator",
    "ListManagedNotificationConfigurationsPaginator",
    "ListManagedNotificationEventsPaginator",
    "ListMemberAccountsPaginator",
    "ListNotificationConfigurationsPaginator",
    "ListNotificationEventsPaginator",
    "ListNotificationHubsPaginator",
    "ListOrganizationalUnitsPaginator",
    "UserNotificationsClient",
)
