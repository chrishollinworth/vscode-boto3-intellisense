"""
Type annotations for notifications service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notifications/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_notifications.client import UserNotificationsClient
    from mypy_boto3_notifications.paginator import (
        ListChannelsPaginator,
        ListEventRulesPaginator,
        ListManagedNotificationChannelAssociationsPaginator,
        ListManagedNotificationChildEventsPaginator,
        ListManagedNotificationConfigurationsPaginator,
        ListManagedNotificationEventsPaginator,
        ListNotificationConfigurationsPaginator,
        ListNotificationEventsPaginator,
        ListNotificationHubsPaginator,
    )

    session = Session()
    client: UserNotificationsClient = session.client("notifications")

    list_channels_paginator: ListChannelsPaginator = client.get_paginator("list_channels")
    list_event_rules_paginator: ListEventRulesPaginator = client.get_paginator("list_event_rules")
    list_managed_notification_channel_associations_paginator: ListManagedNotificationChannelAssociationsPaginator = client.get_paginator("list_managed_notification_channel_associations")
    list_managed_notification_child_events_paginator: ListManagedNotificationChildEventsPaginator = client.get_paginator("list_managed_notification_child_events")
    list_managed_notification_configurations_paginator: ListManagedNotificationConfigurationsPaginator = client.get_paginator("list_managed_notification_configurations")
    list_managed_notification_events_paginator: ListManagedNotificationEventsPaginator = client.get_paginator("list_managed_notification_events")
    list_notification_configurations_paginator: ListNotificationConfigurationsPaginator = client.get_paginator("list_notification_configurations")
    list_notification_events_paginator: ListNotificationEventsPaginator = client.get_paginator("list_notification_events")
    list_notification_hubs_paginator: ListNotificationHubsPaginator = client.get_paginator("list_notification_hubs")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListChannelsRequestPaginateTypeDef,
    ListChannelsResponseTypeDef,
    ListEventRulesRequestPaginateTypeDef,
    ListEventRulesResponseTypeDef,
    ListManagedNotificationChannelAssociationsRequestPaginateTypeDef,
    ListManagedNotificationChannelAssociationsResponseTypeDef,
    ListManagedNotificationChildEventsRequestPaginateTypeDef,
    ListManagedNotificationChildEventsResponseTypeDef,
    ListManagedNotificationConfigurationsRequestPaginateTypeDef,
    ListManagedNotificationConfigurationsResponseTypeDef,
    ListManagedNotificationEventsRequestPaginateTypeDef,
    ListManagedNotificationEventsResponseTypeDef,
    ListNotificationConfigurationsRequestPaginateTypeDef,
    ListNotificationConfigurationsResponseTypeDef,
    ListNotificationEventsRequestPaginateTypeDef,
    ListNotificationEventsResponseTypeDef,
    ListNotificationHubsRequestPaginateTypeDef,
    ListNotificationHubsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListChannelsPaginator",
    "ListEventRulesPaginator",
    "ListManagedNotificationChannelAssociationsPaginator",
    "ListManagedNotificationChildEventsPaginator",
    "ListManagedNotificationConfigurationsPaginator",
    "ListManagedNotificationEventsPaginator",
    "ListNotificationConfigurationsPaginator",
    "ListNotificationEventsPaginator",
    "ListNotificationHubsPaginator",
)

if TYPE_CHECKING:
    _ListChannelsPaginatorBase = Paginator[ListChannelsResponseTypeDef]
else:
    _ListChannelsPaginatorBase = Paginator  # type: ignore[assignment]

class ListChannelsPaginator(_ListChannelsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notifications/paginator/ListChannels.html#UserNotifications.Paginator.ListChannels)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notifications/paginators/#listchannelspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListChannelsRequestPaginateTypeDef]
    ) -> PageIterator[ListChannelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notifications/paginator/ListChannels.html#UserNotifications.Paginator.ListChannels.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notifications/paginators/#listchannelspaginator)
        """

if TYPE_CHECKING:
    _ListEventRulesPaginatorBase = Paginator[ListEventRulesResponseTypeDef]
else:
    _ListEventRulesPaginatorBase = Paginator  # type: ignore[assignment]

class ListEventRulesPaginator(_ListEventRulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notifications/paginator/ListEventRules.html#UserNotifications.Paginator.ListEventRules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notifications/paginators/#listeventrulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEventRulesRequestPaginateTypeDef]
    ) -> PageIterator[ListEventRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notifications/paginator/ListEventRules.html#UserNotifications.Paginator.ListEventRules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notifications/paginators/#listeventrulespaginator)
        """

if TYPE_CHECKING:
    _ListManagedNotificationChannelAssociationsPaginatorBase = Paginator[
        ListManagedNotificationChannelAssociationsResponseTypeDef
    ]
else:
    _ListManagedNotificationChannelAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListManagedNotificationChannelAssociationsPaginator(
    _ListManagedNotificationChannelAssociationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notifications/paginator/ListManagedNotificationChannelAssociations.html#UserNotifications.Paginator.ListManagedNotificationChannelAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notifications/paginators/#listmanagednotificationchannelassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListManagedNotificationChannelAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListManagedNotificationChannelAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notifications/paginator/ListManagedNotificationChannelAssociations.html#UserNotifications.Paginator.ListManagedNotificationChannelAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notifications/paginators/#listmanagednotificationchannelassociationspaginator)
        """

if TYPE_CHECKING:
    _ListManagedNotificationChildEventsPaginatorBase = Paginator[
        ListManagedNotificationChildEventsResponseTypeDef
    ]
else:
    _ListManagedNotificationChildEventsPaginatorBase = Paginator  # type: ignore[assignment]

class ListManagedNotificationChildEventsPaginator(_ListManagedNotificationChildEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notifications/paginator/ListManagedNotificationChildEvents.html#UserNotifications.Paginator.ListManagedNotificationChildEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notifications/paginators/#listmanagednotificationchildeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListManagedNotificationChildEventsRequestPaginateTypeDef]
    ) -> PageIterator[ListManagedNotificationChildEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notifications/paginator/ListManagedNotificationChildEvents.html#UserNotifications.Paginator.ListManagedNotificationChildEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notifications/paginators/#listmanagednotificationchildeventspaginator)
        """

if TYPE_CHECKING:
    _ListManagedNotificationConfigurationsPaginatorBase = Paginator[
        ListManagedNotificationConfigurationsResponseTypeDef
    ]
else:
    _ListManagedNotificationConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListManagedNotificationConfigurationsPaginator(
    _ListManagedNotificationConfigurationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notifications/paginator/ListManagedNotificationConfigurations.html#UserNotifications.Paginator.ListManagedNotificationConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notifications/paginators/#listmanagednotificationconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListManagedNotificationConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[ListManagedNotificationConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notifications/paginator/ListManagedNotificationConfigurations.html#UserNotifications.Paginator.ListManagedNotificationConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notifications/paginators/#listmanagednotificationconfigurationspaginator)
        """

if TYPE_CHECKING:
    _ListManagedNotificationEventsPaginatorBase = Paginator[
        ListManagedNotificationEventsResponseTypeDef
    ]
else:
    _ListManagedNotificationEventsPaginatorBase = Paginator  # type: ignore[assignment]

class ListManagedNotificationEventsPaginator(_ListManagedNotificationEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notifications/paginator/ListManagedNotificationEvents.html#UserNotifications.Paginator.ListManagedNotificationEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notifications/paginators/#listmanagednotificationeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListManagedNotificationEventsRequestPaginateTypeDef]
    ) -> PageIterator[ListManagedNotificationEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notifications/paginator/ListManagedNotificationEvents.html#UserNotifications.Paginator.ListManagedNotificationEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notifications/paginators/#listmanagednotificationeventspaginator)
        """

if TYPE_CHECKING:
    _ListNotificationConfigurationsPaginatorBase = Paginator[
        ListNotificationConfigurationsResponseTypeDef
    ]
else:
    _ListNotificationConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListNotificationConfigurationsPaginator(_ListNotificationConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notifications/paginator/ListNotificationConfigurations.html#UserNotifications.Paginator.ListNotificationConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notifications/paginators/#listnotificationconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListNotificationConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[ListNotificationConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notifications/paginator/ListNotificationConfigurations.html#UserNotifications.Paginator.ListNotificationConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notifications/paginators/#listnotificationconfigurationspaginator)
        """

if TYPE_CHECKING:
    _ListNotificationEventsPaginatorBase = Paginator[ListNotificationEventsResponseTypeDef]
else:
    _ListNotificationEventsPaginatorBase = Paginator  # type: ignore[assignment]

class ListNotificationEventsPaginator(_ListNotificationEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notifications/paginator/ListNotificationEvents.html#UserNotifications.Paginator.ListNotificationEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notifications/paginators/#listnotificationeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListNotificationEventsRequestPaginateTypeDef]
    ) -> PageIterator[ListNotificationEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notifications/paginator/ListNotificationEvents.html#UserNotifications.Paginator.ListNotificationEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notifications/paginators/#listnotificationeventspaginator)
        """

if TYPE_CHECKING:
    _ListNotificationHubsPaginatorBase = Paginator[ListNotificationHubsResponseTypeDef]
else:
    _ListNotificationHubsPaginatorBase = Paginator  # type: ignore[assignment]

class ListNotificationHubsPaginator(_ListNotificationHubsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notifications/paginator/ListNotificationHubs.html#UserNotifications.Paginator.ListNotificationHubs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notifications/paginators/#listnotificationhubspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListNotificationHubsRequestPaginateTypeDef]
    ) -> PageIterator[ListNotificationHubsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/notifications/paginator/ListNotificationHubs.html#UserNotifications.Paginator.ListNotificationHubs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_notifications/paginators/#listnotificationhubspaginator)
        """
