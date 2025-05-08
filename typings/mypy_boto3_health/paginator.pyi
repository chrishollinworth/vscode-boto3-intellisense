"""
Type annotations for health service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_health/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_health.client import HealthClient
    from mypy_boto3_health.paginator import (
        DescribeAffectedAccountsForOrganizationPaginator,
        DescribeAffectedEntitiesForOrganizationPaginator,
        DescribeAffectedEntitiesPaginator,
        DescribeEventAggregatesPaginator,
        DescribeEventTypesPaginator,
        DescribeEventsForOrganizationPaginator,
        DescribeEventsPaginator,
    )

    session = Session()
    client: HealthClient = session.client("health")

    describe_affected_accounts_for_organization_paginator: DescribeAffectedAccountsForOrganizationPaginator = client.get_paginator("describe_affected_accounts_for_organization")
    describe_affected_entities_for_organization_paginator: DescribeAffectedEntitiesForOrganizationPaginator = client.get_paginator("describe_affected_entities_for_organization")
    describe_affected_entities_paginator: DescribeAffectedEntitiesPaginator = client.get_paginator("describe_affected_entities")
    describe_event_aggregates_paginator: DescribeEventAggregatesPaginator = client.get_paginator("describe_event_aggregates")
    describe_event_types_paginator: DescribeEventTypesPaginator = client.get_paginator("describe_event_types")
    describe_events_for_organization_paginator: DescribeEventsForOrganizationPaginator = client.get_paginator("describe_events_for_organization")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeAffectedAccountsForOrganizationRequestPaginateTypeDef,
    DescribeAffectedAccountsForOrganizationResponseTypeDef,
    DescribeAffectedEntitiesForOrganizationRequestPaginateTypeDef,
    DescribeAffectedEntitiesForOrganizationResponseTypeDef,
    DescribeAffectedEntitiesRequestPaginateTypeDef,
    DescribeAffectedEntitiesResponseTypeDef,
    DescribeEventAggregatesRequestPaginateTypeDef,
    DescribeEventAggregatesResponseTypeDef,
    DescribeEventsForOrganizationRequestPaginateTypeDef,
    DescribeEventsForOrganizationResponseTypeDef,
    DescribeEventsRequestPaginateTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeEventTypesRequestPaginateTypeDef,
    DescribeEventTypesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeAffectedAccountsForOrganizationPaginator",
    "DescribeAffectedEntitiesForOrganizationPaginator",
    "DescribeAffectedEntitiesPaginator",
    "DescribeEventAggregatesPaginator",
    "DescribeEventTypesPaginator",
    "DescribeEventsForOrganizationPaginator",
    "DescribeEventsPaginator",
)

if TYPE_CHECKING:
    _DescribeAffectedAccountsForOrganizationPaginatorBase = Paginator[
        DescribeAffectedAccountsForOrganizationResponseTypeDef
    ]
else:
    _DescribeAffectedAccountsForOrganizationPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeAffectedAccountsForOrganizationPaginator(
    _DescribeAffectedAccountsForOrganizationPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health/paginator/DescribeAffectedAccountsForOrganization.html#Health.Paginator.DescribeAffectedAccountsForOrganization)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_health/paginators/#describeaffectedaccountsfororganizationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAffectedAccountsForOrganizationRequestPaginateTypeDef]
    ) -> PageIterator[DescribeAffectedAccountsForOrganizationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health/paginator/DescribeAffectedAccountsForOrganization.html#Health.Paginator.DescribeAffectedAccountsForOrganization.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_health/paginators/#describeaffectedaccountsfororganizationpaginator)
        """

if TYPE_CHECKING:
    _DescribeAffectedEntitiesForOrganizationPaginatorBase = Paginator[
        DescribeAffectedEntitiesForOrganizationResponseTypeDef
    ]
else:
    _DescribeAffectedEntitiesForOrganizationPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeAffectedEntitiesForOrganizationPaginator(
    _DescribeAffectedEntitiesForOrganizationPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health/paginator/DescribeAffectedEntitiesForOrganization.html#Health.Paginator.DescribeAffectedEntitiesForOrganization)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_health/paginators/#describeaffectedentitiesfororganizationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAffectedEntitiesForOrganizationRequestPaginateTypeDef]
    ) -> PageIterator[DescribeAffectedEntitiesForOrganizationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health/paginator/DescribeAffectedEntitiesForOrganization.html#Health.Paginator.DescribeAffectedEntitiesForOrganization.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_health/paginators/#describeaffectedentitiesfororganizationpaginator)
        """

if TYPE_CHECKING:
    _DescribeAffectedEntitiesPaginatorBase = Paginator[DescribeAffectedEntitiesResponseTypeDef]
else:
    _DescribeAffectedEntitiesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeAffectedEntitiesPaginator(_DescribeAffectedEntitiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health/paginator/DescribeAffectedEntities.html#Health.Paginator.DescribeAffectedEntities)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_health/paginators/#describeaffectedentitiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAffectedEntitiesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeAffectedEntitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health/paginator/DescribeAffectedEntities.html#Health.Paginator.DescribeAffectedEntities.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_health/paginators/#describeaffectedentitiespaginator)
        """

if TYPE_CHECKING:
    _DescribeEventAggregatesPaginatorBase = Paginator[DescribeEventAggregatesResponseTypeDef]
else:
    _DescribeEventAggregatesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEventAggregatesPaginator(_DescribeEventAggregatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health/paginator/DescribeEventAggregates.html#Health.Paginator.DescribeEventAggregates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_health/paginators/#describeeventaggregatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEventAggregatesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeEventAggregatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health/paginator/DescribeEventAggregates.html#Health.Paginator.DescribeEventAggregates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_health/paginators/#describeeventaggregatespaginator)
        """

if TYPE_CHECKING:
    _DescribeEventTypesPaginatorBase = Paginator[DescribeEventTypesResponseTypeDef]
else:
    _DescribeEventTypesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEventTypesPaginator(_DescribeEventTypesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health/paginator/DescribeEventTypes.html#Health.Paginator.DescribeEventTypes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_health/paginators/#describeeventtypespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEventTypesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeEventTypesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health/paginator/DescribeEventTypes.html#Health.Paginator.DescribeEventTypes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_health/paginators/#describeeventtypespaginator)
        """

if TYPE_CHECKING:
    _DescribeEventsForOrganizationPaginatorBase = Paginator[
        DescribeEventsForOrganizationResponseTypeDef
    ]
else:
    _DescribeEventsForOrganizationPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEventsForOrganizationPaginator(_DescribeEventsForOrganizationPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health/paginator/DescribeEventsForOrganization.html#Health.Paginator.DescribeEventsForOrganization)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_health/paginators/#describeeventsfororganizationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEventsForOrganizationRequestPaginateTypeDef]
    ) -> PageIterator[DescribeEventsForOrganizationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health/paginator/DescribeEventsForOrganization.html#Health.Paginator.DescribeEventsForOrganization.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_health/paginators/#describeeventsfororganizationpaginator)
        """

if TYPE_CHECKING:
    _DescribeEventsPaginatorBase = Paginator[DescribeEventsResponseTypeDef]
else:
    _DescribeEventsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEventsPaginator(_DescribeEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health/paginator/DescribeEvents.html#Health.Paginator.DescribeEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_health/paginators/#describeeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEventsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health/paginator/DescribeEvents.html#Health.Paginator.DescribeEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_health/paginators/#describeeventspaginator)
        """
