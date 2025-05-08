"""
Type annotations for codestar-notifications service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_codestar_notifications.client import CodeStarNotificationsClient
    from mypy_boto3_codestar_notifications.paginator import (
        ListEventTypesPaginator,
        ListNotificationRulesPaginator,
        ListTargetsPaginator,
    )

    session = Session()
    client: CodeStarNotificationsClient = session.client("codestar-notifications")

    list_event_types_paginator: ListEventTypesPaginator = client.get_paginator("list_event_types")
    list_notification_rules_paginator: ListNotificationRulesPaginator = client.get_paginator("list_notification_rules")
    list_targets_paginator: ListTargetsPaginator = client.get_paginator("list_targets")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListEventTypesRequestPaginateTypeDef,
    ListEventTypesResultTypeDef,
    ListNotificationRulesRequestPaginateTypeDef,
    ListNotificationRulesResultTypeDef,
    ListTargetsRequestPaginateTypeDef,
    ListTargetsResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListEventTypesPaginator", "ListNotificationRulesPaginator", "ListTargetsPaginator")

if TYPE_CHECKING:
    _ListEventTypesPaginatorBase = Paginator[ListEventTypesResultTypeDef]
else:
    _ListEventTypesPaginatorBase = Paginator  # type: ignore[assignment]

class ListEventTypesPaginator(_ListEventTypesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/paginator/ListEventTypes.html#CodeStarNotifications.Paginator.ListEventTypes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/paginators/#listeventtypespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEventTypesRequestPaginateTypeDef]
    ) -> PageIterator[ListEventTypesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/paginator/ListEventTypes.html#CodeStarNotifications.Paginator.ListEventTypes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/paginators/#listeventtypespaginator)
        """

if TYPE_CHECKING:
    _ListNotificationRulesPaginatorBase = Paginator[ListNotificationRulesResultTypeDef]
else:
    _ListNotificationRulesPaginatorBase = Paginator  # type: ignore[assignment]

class ListNotificationRulesPaginator(_ListNotificationRulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/paginator/ListNotificationRules.html#CodeStarNotifications.Paginator.ListNotificationRules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/paginators/#listnotificationrulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListNotificationRulesRequestPaginateTypeDef]
    ) -> PageIterator[ListNotificationRulesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/paginator/ListNotificationRules.html#CodeStarNotifications.Paginator.ListNotificationRules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/paginators/#listnotificationrulespaginator)
        """

if TYPE_CHECKING:
    _ListTargetsPaginatorBase = Paginator[ListTargetsResultTypeDef]
else:
    _ListTargetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTargetsPaginator(_ListTargetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/paginator/ListTargets.html#CodeStarNotifications.Paginator.ListTargets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/paginators/#listtargetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTargetsRequestPaginateTypeDef]
    ) -> PageIterator[ListTargetsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications/paginator/ListTargets.html#CodeStarNotifications.Paginator.ListTargets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/paginators/#listtargetspaginator)
        """
