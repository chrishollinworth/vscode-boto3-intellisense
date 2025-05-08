"""
Type annotations for health service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_health/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_health.type_defs import AccountEntityAggregateTypeDef

    data: AccountEntityAggregateTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    EntityStatusCodeType,
    EventScopeCodeType,
    EventStatusCodeType,
    EventTypeCategoryType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccountEntityAggregateTypeDef",
    "AffectedEntityTypeDef",
    "DateTimeRangeTypeDef",
    "DescribeAffectedAccountsForOrganizationRequestPaginateTypeDef",
    "DescribeAffectedAccountsForOrganizationRequestTypeDef",
    "DescribeAffectedAccountsForOrganizationResponseTypeDef",
    "DescribeAffectedEntitiesForOrganizationRequestPaginateTypeDef",
    "DescribeAffectedEntitiesForOrganizationRequestTypeDef",
    "DescribeAffectedEntitiesForOrganizationResponseTypeDef",
    "DescribeAffectedEntitiesRequestPaginateTypeDef",
    "DescribeAffectedEntitiesRequestTypeDef",
    "DescribeAffectedEntitiesResponseTypeDef",
    "DescribeEntityAggregatesForOrganizationRequestTypeDef",
    "DescribeEntityAggregatesForOrganizationResponseTypeDef",
    "DescribeEntityAggregatesRequestTypeDef",
    "DescribeEntityAggregatesResponseTypeDef",
    "DescribeEventAggregatesRequestPaginateTypeDef",
    "DescribeEventAggregatesRequestTypeDef",
    "DescribeEventAggregatesResponseTypeDef",
    "DescribeEventDetailsForOrganizationRequestTypeDef",
    "DescribeEventDetailsForOrganizationResponseTypeDef",
    "DescribeEventDetailsRequestTypeDef",
    "DescribeEventDetailsResponseTypeDef",
    "DescribeEventTypesRequestPaginateTypeDef",
    "DescribeEventTypesRequestTypeDef",
    "DescribeEventTypesResponseTypeDef",
    "DescribeEventsForOrganizationRequestPaginateTypeDef",
    "DescribeEventsForOrganizationRequestTypeDef",
    "DescribeEventsForOrganizationResponseTypeDef",
    "DescribeEventsRequestPaginateTypeDef",
    "DescribeEventsRequestTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeHealthServiceStatusForOrganizationResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EntityAccountFilterTypeDef",
    "EntityAggregateTypeDef",
    "EntityFilterTypeDef",
    "EventAccountFilterTypeDef",
    "EventAggregateTypeDef",
    "EventDescriptionTypeDef",
    "EventDetailsErrorItemTypeDef",
    "EventDetailsTypeDef",
    "EventFilterTypeDef",
    "EventTypeDef",
    "EventTypeFilterTypeDef",
    "EventTypeTypeDef",
    "OrganizationAffectedEntitiesErrorItemTypeDef",
    "OrganizationEntityAggregateTypeDef",
    "OrganizationEventDetailsErrorItemTypeDef",
    "OrganizationEventDetailsTypeDef",
    "OrganizationEventFilterTypeDef",
    "OrganizationEventTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TimestampTypeDef",
)

class AccountEntityAggregateTypeDef(TypedDict):
    accountId: NotRequired[str]
    count: NotRequired[int]
    statuses: NotRequired[Dict[EntityStatusCodeType, int]]

class AffectedEntityTypeDef(TypedDict):
    entityArn: NotRequired[str]
    eventArn: NotRequired[str]
    entityValue: NotRequired[str]
    entityUrl: NotRequired[str]
    awsAccountId: NotRequired[str]
    lastUpdatedTime: NotRequired[datetime]
    statusCode: NotRequired[EntityStatusCodeType]
    tags: NotRequired[Dict[str, str]]
    entityMetadata: NotRequired[Dict[str, str]]

TimestampTypeDef = Union[datetime, str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeAffectedAccountsForOrganizationRequestTypeDef(TypedDict):
    eventArn: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class EntityAccountFilterTypeDef(TypedDict):
    eventArn: str
    awsAccountId: NotRequired[str]
    statusCodes: NotRequired[Sequence[EntityStatusCodeType]]

class EventAccountFilterTypeDef(TypedDict):
    eventArn: str
    awsAccountId: NotRequired[str]

class OrganizationAffectedEntitiesErrorItemTypeDef(TypedDict):
    awsAccountId: NotRequired[str]
    eventArn: NotRequired[str]
    errorName: NotRequired[str]
    errorMessage: NotRequired[str]

class DescribeEntityAggregatesForOrganizationRequestTypeDef(TypedDict):
    eventArns: Sequence[str]
    awsAccountIds: NotRequired[Sequence[str]]

class DescribeEntityAggregatesRequestTypeDef(TypedDict):
    eventArns: NotRequired[Sequence[str]]

class EntityAggregateTypeDef(TypedDict):
    eventArn: NotRequired[str]
    count: NotRequired[int]
    statuses: NotRequired[Dict[EntityStatusCodeType, int]]

class EventAggregateTypeDef(TypedDict):
    aggregateValue: NotRequired[str]
    count: NotRequired[int]

class OrganizationEventDetailsErrorItemTypeDef(TypedDict):
    awsAccountId: NotRequired[str]
    eventArn: NotRequired[str]
    errorName: NotRequired[str]
    errorMessage: NotRequired[str]

class DescribeEventDetailsRequestTypeDef(TypedDict):
    eventArns: Sequence[str]
    locale: NotRequired[str]

class EventDetailsErrorItemTypeDef(TypedDict):
    eventArn: NotRequired[str]
    errorName: NotRequired[str]
    errorMessage: NotRequired[str]

class EventTypeFilterTypeDef(TypedDict):
    eventTypeCodes: NotRequired[Sequence[str]]
    services: NotRequired[Sequence[str]]
    eventTypeCategories: NotRequired[Sequence[EventTypeCategoryType]]

class EventTypeTypeDef(TypedDict):
    service: NotRequired[str]
    code: NotRequired[str]
    category: NotRequired[EventTypeCategoryType]

class OrganizationEventTypeDef(TypedDict):
    arn: NotRequired[str]
    service: NotRequired[str]
    eventTypeCode: NotRequired[str]
    eventTypeCategory: NotRequired[EventTypeCategoryType]
    eventScopeCode: NotRequired[EventScopeCodeType]
    region: NotRequired[str]
    startTime: NotRequired[datetime]
    endTime: NotRequired[datetime]
    lastUpdatedTime: NotRequired[datetime]
    statusCode: NotRequired[EventStatusCodeType]

class EventTypeDef(TypedDict):
    arn: NotRequired[str]
    service: NotRequired[str]
    eventTypeCode: NotRequired[str]
    eventTypeCategory: NotRequired[EventTypeCategoryType]
    region: NotRequired[str]
    availabilityZone: NotRequired[str]
    startTime: NotRequired[datetime]
    endTime: NotRequired[datetime]
    lastUpdatedTime: NotRequired[datetime]
    statusCode: NotRequired[EventStatusCodeType]
    eventScopeCode: NotRequired[EventScopeCodeType]

class EventDescriptionTypeDef(TypedDict):
    latestDescription: NotRequired[str]

class OrganizationEntityAggregateTypeDef(TypedDict):
    eventArn: NotRequired[str]
    count: NotRequired[int]
    statuses: NotRequired[Dict[EntityStatusCodeType, int]]
    accounts: NotRequired[List[AccountEntityAggregateTypeDef]]

DateTimeRangeTypeDef = TypedDict(
    "DateTimeRangeTypeDef",
    {
        "from": NotRequired[TimestampTypeDef],
        "to": NotRequired[TimestampTypeDef],
    },
)

class DescribeAffectedAccountsForOrganizationRequestPaginateTypeDef(TypedDict):
    eventArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeAffectedAccountsForOrganizationResponseTypeDef(TypedDict):
    affectedAccounts: List[str]
    eventScopeCode: EventScopeCodeType
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeAffectedEntitiesResponseTypeDef(TypedDict):
    entities: List[AffectedEntityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeHealthServiceStatusForOrganizationResponseTypeDef(TypedDict):
    healthServiceAccessStatusForOrganization: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAffectedEntitiesForOrganizationRequestPaginateTypeDef(TypedDict):
    organizationEntityFilters: NotRequired[Sequence[EventAccountFilterTypeDef]]
    locale: NotRequired[str]
    organizationEntityAccountFilters: NotRequired[Sequence[EntityAccountFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeAffectedEntitiesForOrganizationRequestTypeDef(TypedDict):
    organizationEntityFilters: NotRequired[Sequence[EventAccountFilterTypeDef]]
    locale: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    organizationEntityAccountFilters: NotRequired[Sequence[EntityAccountFilterTypeDef]]

class DescribeEventDetailsForOrganizationRequestTypeDef(TypedDict):
    organizationEventDetailFilters: Sequence[EventAccountFilterTypeDef]
    locale: NotRequired[str]

class DescribeAffectedEntitiesForOrganizationResponseTypeDef(TypedDict):
    entities: List[AffectedEntityTypeDef]
    failedSet: List[OrganizationAffectedEntitiesErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeEntityAggregatesResponseTypeDef(TypedDict):
    entityAggregates: List[EntityAggregateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventAggregatesResponseTypeDef(TypedDict):
    eventAggregates: List[EventAggregateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

DescribeEventTypesRequestPaginateTypeDef = TypedDict(
    "DescribeEventTypesRequestPaginateTypeDef",
    {
        "filter": NotRequired[EventTypeFilterTypeDef],
        "locale": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEventTypesRequestTypeDef = TypedDict(
    "DescribeEventTypesRequestTypeDef",
    {
        "filter": NotRequired[EventTypeFilterTypeDef],
        "locale": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

class DescribeEventTypesResponseTypeDef(TypedDict):
    eventTypes: List[EventTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeEventsForOrganizationResponseTypeDef(TypedDict):
    events: List[OrganizationEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeEventsResponseTypeDef(TypedDict):
    events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class EventDetailsTypeDef(TypedDict):
    event: NotRequired[EventTypeDef]
    eventDescription: NotRequired[EventDescriptionTypeDef]
    eventMetadata: NotRequired[Dict[str, str]]

class OrganizationEventDetailsTypeDef(TypedDict):
    awsAccountId: NotRequired[str]
    event: NotRequired[EventTypeDef]
    eventDescription: NotRequired[EventDescriptionTypeDef]
    eventMetadata: NotRequired[Dict[str, str]]

class DescribeEntityAggregatesForOrganizationResponseTypeDef(TypedDict):
    organizationEntityAggregates: List[OrganizationEntityAggregateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EntityFilterTypeDef(TypedDict):
    eventArns: Sequence[str]
    entityArns: NotRequired[Sequence[str]]
    entityValues: NotRequired[Sequence[str]]
    lastUpdatedTimes: NotRequired[Sequence[DateTimeRangeTypeDef]]
    tags: NotRequired[Sequence[Mapping[str, str]]]
    statusCodes: NotRequired[Sequence[EntityStatusCodeType]]

class EventFilterTypeDef(TypedDict):
    eventArns: NotRequired[Sequence[str]]
    eventTypeCodes: NotRequired[Sequence[str]]
    services: NotRequired[Sequence[str]]
    regions: NotRequired[Sequence[str]]
    availabilityZones: NotRequired[Sequence[str]]
    startTimes: NotRequired[Sequence[DateTimeRangeTypeDef]]
    endTimes: NotRequired[Sequence[DateTimeRangeTypeDef]]
    lastUpdatedTimes: NotRequired[Sequence[DateTimeRangeTypeDef]]
    entityArns: NotRequired[Sequence[str]]
    entityValues: NotRequired[Sequence[str]]
    eventTypeCategories: NotRequired[Sequence[EventTypeCategoryType]]
    tags: NotRequired[Sequence[Mapping[str, str]]]
    eventStatusCodes: NotRequired[Sequence[EventStatusCodeType]]

class OrganizationEventFilterTypeDef(TypedDict):
    eventTypeCodes: NotRequired[Sequence[str]]
    awsAccountIds: NotRequired[Sequence[str]]
    services: NotRequired[Sequence[str]]
    regions: NotRequired[Sequence[str]]
    startTime: NotRequired[DateTimeRangeTypeDef]
    endTime: NotRequired[DateTimeRangeTypeDef]
    lastUpdatedTime: NotRequired[DateTimeRangeTypeDef]
    entityArns: NotRequired[Sequence[str]]
    entityValues: NotRequired[Sequence[str]]
    eventTypeCategories: NotRequired[Sequence[EventTypeCategoryType]]
    eventStatusCodes: NotRequired[Sequence[EventStatusCodeType]]

class DescribeEventDetailsResponseTypeDef(TypedDict):
    successfulSet: List[EventDetailsTypeDef]
    failedSet: List[EventDetailsErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventDetailsForOrganizationResponseTypeDef(TypedDict):
    successfulSet: List[OrganizationEventDetailsTypeDef]
    failedSet: List[OrganizationEventDetailsErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

DescribeAffectedEntitiesRequestPaginateTypeDef = TypedDict(
    "DescribeAffectedEntitiesRequestPaginateTypeDef",
    {
        "filter": EntityFilterTypeDef,
        "locale": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeAffectedEntitiesRequestTypeDef = TypedDict(
    "DescribeAffectedEntitiesRequestTypeDef",
    {
        "filter": EntityFilterTypeDef,
        "locale": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
DescribeEventAggregatesRequestPaginateTypeDef = TypedDict(
    "DescribeEventAggregatesRequestPaginateTypeDef",
    {
        "aggregateField": Literal["eventTypeCategory"],
        "filter": NotRequired[EventFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEventAggregatesRequestTypeDef = TypedDict(
    "DescribeEventAggregatesRequestTypeDef",
    {
        "aggregateField": Literal["eventTypeCategory"],
        "filter": NotRequired[EventFilterTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
DescribeEventsRequestPaginateTypeDef = TypedDict(
    "DescribeEventsRequestPaginateTypeDef",
    {
        "filter": NotRequired[EventFilterTypeDef],
        "locale": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEventsRequestTypeDef = TypedDict(
    "DescribeEventsRequestTypeDef",
    {
        "filter": NotRequired[EventFilterTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "locale": NotRequired[str],
    },
)
DescribeEventsForOrganizationRequestPaginateTypeDef = TypedDict(
    "DescribeEventsForOrganizationRequestPaginateTypeDef",
    {
        "filter": NotRequired[OrganizationEventFilterTypeDef],
        "locale": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEventsForOrganizationRequestTypeDef = TypedDict(
    "DescribeEventsForOrganizationRequestTypeDef",
    {
        "filter": NotRequired[OrganizationEventFilterTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "locale": NotRequired[str],
    },
)
