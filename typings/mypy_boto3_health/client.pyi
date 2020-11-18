# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for health service client

Usage::

    ```python
    import boto3
    from mypy_boto3_health import HealthClient

    client: HealthClient = boto3.client("health")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_health.paginator import (
    DescribeAffectedAccountsForOrganizationPaginator,
    DescribeAffectedEntitiesForOrganizationPaginator,
    DescribeAffectedEntitiesPaginator,
    DescribeEventAggregatesPaginator,
    DescribeEventsForOrganizationPaginator,
    DescribeEventsPaginator,
    DescribeEventTypesPaginator,
)
from mypy_boto3_health.type_defs import (
    DescribeAffectedAccountsForOrganizationResponseTypeDef,
    DescribeAffectedEntitiesForOrganizationResponseTypeDef,
    DescribeAffectedEntitiesResponseTypeDef,
    DescribeEntityAggregatesResponseTypeDef,
    DescribeEventAggregatesResponseTypeDef,
    DescribeEventDetailsForOrganizationResponseTypeDef,
    DescribeEventDetailsResponseTypeDef,
    DescribeEventsForOrganizationResponseTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeEventTypesResponseTypeDef,
    DescribeHealthServiceStatusForOrganizationResponseTypeDef,
    EntityFilterTypeDef,
    EventAccountFilterTypeDef,
    EventFilterTypeDef,
    EventTypeFilterTypeDef,
    OrganizationEventFilterTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("HealthClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    InvalidPaginationToken: Type[BotocoreClientError]
    UnsupportedLocale: Type[BotocoreClientError]


class HealthClient:
    """
    [Health.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/health.html#Health.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/health.html#Health.Client.can_paginate)
        """

    def describe_affected_accounts_for_organization(
        self, eventArn: str, nextToken: str = None, maxResults: int = None
    ) -> DescribeAffectedAccountsForOrganizationResponseTypeDef:
        """
        [Client.describe_affected_accounts_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/health.html#Health.Client.describe_affected_accounts_for_organization)
        """

    def describe_affected_entities(
        self,
        filter: EntityFilterTypeDef,
        locale: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeAffectedEntitiesResponseTypeDef:
        """
        [Client.describe_affected_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/health.html#Health.Client.describe_affected_entities)
        """

    def describe_affected_entities_for_organization(
        self,
        organizationEntityFilters: List[EventAccountFilterTypeDef],
        locale: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeAffectedEntitiesForOrganizationResponseTypeDef:
        """
        [Client.describe_affected_entities_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/health.html#Health.Client.describe_affected_entities_for_organization)
        """

    def describe_entity_aggregates(
        self, eventArns: List[str] = None
    ) -> DescribeEntityAggregatesResponseTypeDef:
        """
        [Client.describe_entity_aggregates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/health.html#Health.Client.describe_entity_aggregates)
        """

    def describe_event_aggregates(
        self,
        aggregateField: Literal["eventTypeCategory"],
        filter: EventFilterTypeDef = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> DescribeEventAggregatesResponseTypeDef:
        """
        [Client.describe_event_aggregates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/health.html#Health.Client.describe_event_aggregates)
        """

    def describe_event_details(
        self, eventArns: List[str], locale: str = None
    ) -> DescribeEventDetailsResponseTypeDef:
        """
        [Client.describe_event_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/health.html#Health.Client.describe_event_details)
        """

    def describe_event_details_for_organization(
        self, organizationEventDetailFilters: List[EventAccountFilterTypeDef], locale: str = None
    ) -> DescribeEventDetailsForOrganizationResponseTypeDef:
        """
        [Client.describe_event_details_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/health.html#Health.Client.describe_event_details_for_organization)
        """

    def describe_event_types(
        self,
        filter: EventTypeFilterTypeDef = None,
        locale: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeEventTypesResponseTypeDef:
        """
        [Client.describe_event_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/health.html#Health.Client.describe_event_types)
        """

    def describe_events(
        self,
        filter: EventFilterTypeDef = None,
        nextToken: str = None,
        maxResults: int = None,
        locale: str = None,
    ) -> DescribeEventsResponseTypeDef:
        """
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/health.html#Health.Client.describe_events)
        """

    def describe_events_for_organization(
        self,
        filter: OrganizationEventFilterTypeDef = None,
        nextToken: str = None,
        maxResults: int = None,
        locale: str = None,
    ) -> DescribeEventsForOrganizationResponseTypeDef:
        """
        [Client.describe_events_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/health.html#Health.Client.describe_events_for_organization)
        """

    def describe_health_service_status_for_organization(
        self,
    ) -> DescribeHealthServiceStatusForOrganizationResponseTypeDef:
        """
        [Client.describe_health_service_status_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/health.html#Health.Client.describe_health_service_status_for_organization)
        """

    def disable_health_service_access_for_organization(self) -> None:
        """
        [Client.disable_health_service_access_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/health.html#Health.Client.disable_health_service_access_for_organization)
        """

    def enable_health_service_access_for_organization(self) -> None:
        """
        [Client.enable_health_service_access_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/health.html#Health.Client.enable_health_service_access_for_organization)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/health.html#Health.Client.generate_presigned_url)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_affected_accounts_for_organization"]
    ) -> DescribeAffectedAccountsForOrganizationPaginator:
        """
        [Paginator.DescribeAffectedAccountsForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/health.html#Health.Paginator.DescribeAffectedAccountsForOrganization)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_affected_entities"]
    ) -> DescribeAffectedEntitiesPaginator:
        """
        [Paginator.DescribeAffectedEntities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/health.html#Health.Paginator.DescribeAffectedEntities)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_affected_entities_for_organization"]
    ) -> DescribeAffectedEntitiesForOrganizationPaginator:
        """
        [Paginator.DescribeAffectedEntitiesForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/health.html#Health.Paginator.DescribeAffectedEntitiesForOrganization)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_event_aggregates"]
    ) -> DescribeEventAggregatesPaginator:
        """
        [Paginator.DescribeEventAggregates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/health.html#Health.Paginator.DescribeEventAggregates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_event_types"]
    ) -> DescribeEventTypesPaginator:
        """
        [Paginator.DescribeEventTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/health.html#Health.Paginator.DescribeEventTypes)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/health.html#Health.Paginator.DescribeEvents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_events_for_organization"]
    ) -> DescribeEventsForOrganizationPaginator:
        """
        [Paginator.DescribeEventsForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/health.html#Health.Paginator.DescribeEventsForOrganization)
        """
