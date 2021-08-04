"""
Type annotations for health service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/literals.html)

Usage::

    ```python
    from mypy_boto3_health.literals import DescribeAffectedAccountsForOrganizationPaginatorName

    data: DescribeAffectedAccountsForOrganizationPaginatorName = "describe_affected_accounts_for_organization"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DescribeAffectedAccountsForOrganizationPaginatorName",
    "DescribeAffectedEntitiesForOrganizationPaginatorName",
    "DescribeAffectedEntitiesPaginatorName",
    "DescribeEventAggregatesPaginatorName",
    "DescribeEventTypesPaginatorName",
    "DescribeEventsForOrganizationPaginatorName",
    "DescribeEventsPaginatorName",
    "entityStatusCodeType",
    "eventAggregateFieldType",
    "eventScopeCodeType",
    "eventStatusCodeType",
    "eventTypeCategoryType",
)

DescribeAffectedAccountsForOrganizationPaginatorName = Literal[
    "describe_affected_accounts_for_organization"
]
DescribeAffectedEntitiesForOrganizationPaginatorName = Literal[
    "describe_affected_entities_for_organization"
]
DescribeAffectedEntitiesPaginatorName = Literal["describe_affected_entities"]
DescribeEventAggregatesPaginatorName = Literal["describe_event_aggregates"]
DescribeEventTypesPaginatorName = Literal["describe_event_types"]
DescribeEventsForOrganizationPaginatorName = Literal["describe_events_for_organization"]
DescribeEventsPaginatorName = Literal["describe_events"]
entityStatusCodeType = Literal["IMPAIRED", "UNIMPAIRED", "UNKNOWN"]
eventAggregateFieldType = Literal["eventTypeCategory"]
eventScopeCodeType = Literal["ACCOUNT_SPECIFIC", "NONE", "PUBLIC"]
eventStatusCodeType = Literal["closed", "open", "upcoming"]
eventTypeCategoryType = Literal["accountNotification", "investigation", "issue", "scheduledChange"]
