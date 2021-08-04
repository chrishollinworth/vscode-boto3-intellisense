"""
Type annotations for health service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/type_defs.html)

Usage::

    ```python
    from mypy_boto3_health.type_defs import AffectedEntityTypeDef

    data: AffectedEntityTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    entityStatusCodeType,
    eventScopeCodeType,
    eventStatusCodeType,
    eventTypeCategoryType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AffectedEntityTypeDef",
    "DateTimeRangeTypeDef",
    "DescribeAffectedAccountsForOrganizationRequestRequestTypeDef",
    "DescribeAffectedAccountsForOrganizationResponseTypeDef",
    "DescribeAffectedEntitiesForOrganizationRequestRequestTypeDef",
    "DescribeAffectedEntitiesForOrganizationResponseTypeDef",
    "DescribeAffectedEntitiesRequestRequestTypeDef",
    "DescribeAffectedEntitiesResponseTypeDef",
    "DescribeEntityAggregatesRequestRequestTypeDef",
    "DescribeEntityAggregatesResponseTypeDef",
    "DescribeEventAggregatesRequestRequestTypeDef",
    "DescribeEventAggregatesResponseTypeDef",
    "DescribeEventDetailsForOrganizationRequestRequestTypeDef",
    "DescribeEventDetailsForOrganizationResponseTypeDef",
    "DescribeEventDetailsRequestRequestTypeDef",
    "DescribeEventDetailsResponseTypeDef",
    "DescribeEventTypesRequestRequestTypeDef",
    "DescribeEventTypesResponseTypeDef",
    "DescribeEventsForOrganizationRequestRequestTypeDef",
    "DescribeEventsForOrganizationResponseTypeDef",
    "DescribeEventsRequestRequestTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeHealthServiceStatusForOrganizationResponseTypeDef",
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
    "OrganizationEventDetailsErrorItemTypeDef",
    "OrganizationEventDetailsTypeDef",
    "OrganizationEventFilterTypeDef",
    "OrganizationEventTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
)

AffectedEntityTypeDef = TypedDict(
    "AffectedEntityTypeDef",
    {
        "entityArn": str,
        "eventArn": str,
        "entityValue": str,
        "entityUrl": str,
        "awsAccountId": str,
        "lastUpdatedTime": datetime,
        "statusCode": entityStatusCodeType,
        "tags": Dict[str, str],
    },
    total=False,
)

DateTimeRangeTypeDef = TypedDict(
    "DateTimeRangeTypeDef",
    {
        "from": Union[datetime, str],
        "to": Union[datetime, str],
    },
    total=False,
)

_RequiredDescribeAffectedAccountsForOrganizationRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAffectedAccountsForOrganizationRequestRequestTypeDef",
    {
        "eventArn": str,
    },
)
_OptionalDescribeAffectedAccountsForOrganizationRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAffectedAccountsForOrganizationRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class DescribeAffectedAccountsForOrganizationRequestRequestTypeDef(
    _RequiredDescribeAffectedAccountsForOrganizationRequestRequestTypeDef,
    _OptionalDescribeAffectedAccountsForOrganizationRequestRequestTypeDef,
):
    pass

DescribeAffectedAccountsForOrganizationResponseTypeDef = TypedDict(
    "DescribeAffectedAccountsForOrganizationResponseTypeDef",
    {
        "affectedAccounts": List[str],
        "eventScopeCode": eventScopeCodeType,
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAffectedEntitiesForOrganizationRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAffectedEntitiesForOrganizationRequestRequestTypeDef",
    {
        "organizationEntityFilters": List["EventAccountFilterTypeDef"],
    },
)
_OptionalDescribeAffectedEntitiesForOrganizationRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAffectedEntitiesForOrganizationRequestRequestTypeDef",
    {
        "locale": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class DescribeAffectedEntitiesForOrganizationRequestRequestTypeDef(
    _RequiredDescribeAffectedEntitiesForOrganizationRequestRequestTypeDef,
    _OptionalDescribeAffectedEntitiesForOrganizationRequestRequestTypeDef,
):
    pass

DescribeAffectedEntitiesForOrganizationResponseTypeDef = TypedDict(
    "DescribeAffectedEntitiesForOrganizationResponseTypeDef",
    {
        "entities": List["AffectedEntityTypeDef"],
        "failedSet": List["OrganizationAffectedEntitiesErrorItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAffectedEntitiesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAffectedEntitiesRequestRequestTypeDef",
    {
        "filter": "EntityFilterTypeDef",
    },
)
_OptionalDescribeAffectedEntitiesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAffectedEntitiesRequestRequestTypeDef",
    {
        "locale": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class DescribeAffectedEntitiesRequestRequestTypeDef(
    _RequiredDescribeAffectedEntitiesRequestRequestTypeDef,
    _OptionalDescribeAffectedEntitiesRequestRequestTypeDef,
):
    pass

DescribeAffectedEntitiesResponseTypeDef = TypedDict(
    "DescribeAffectedEntitiesResponseTypeDef",
    {
        "entities": List["AffectedEntityTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEntityAggregatesRequestRequestTypeDef = TypedDict(
    "DescribeEntityAggregatesRequestRequestTypeDef",
    {
        "eventArns": List[str],
    },
    total=False,
)

DescribeEntityAggregatesResponseTypeDef = TypedDict(
    "DescribeEntityAggregatesResponseTypeDef",
    {
        "entityAggregates": List["EntityAggregateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeEventAggregatesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeEventAggregatesRequestRequestTypeDef",
    {
        "aggregateField": Literal["eventTypeCategory"],
    },
)
_OptionalDescribeEventAggregatesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeEventAggregatesRequestRequestTypeDef",
    {
        "filter": "EventFilterTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class DescribeEventAggregatesRequestRequestTypeDef(
    _RequiredDescribeEventAggregatesRequestRequestTypeDef,
    _OptionalDescribeEventAggregatesRequestRequestTypeDef,
):
    pass

DescribeEventAggregatesResponseTypeDef = TypedDict(
    "DescribeEventAggregatesResponseTypeDef",
    {
        "eventAggregates": List["EventAggregateTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeEventDetailsForOrganizationRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeEventDetailsForOrganizationRequestRequestTypeDef",
    {
        "organizationEventDetailFilters": List["EventAccountFilterTypeDef"],
    },
)
_OptionalDescribeEventDetailsForOrganizationRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeEventDetailsForOrganizationRequestRequestTypeDef",
    {
        "locale": str,
    },
    total=False,
)

class DescribeEventDetailsForOrganizationRequestRequestTypeDef(
    _RequiredDescribeEventDetailsForOrganizationRequestRequestTypeDef,
    _OptionalDescribeEventDetailsForOrganizationRequestRequestTypeDef,
):
    pass

DescribeEventDetailsForOrganizationResponseTypeDef = TypedDict(
    "DescribeEventDetailsForOrganizationResponseTypeDef",
    {
        "successfulSet": List["OrganizationEventDetailsTypeDef"],
        "failedSet": List["OrganizationEventDetailsErrorItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeEventDetailsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeEventDetailsRequestRequestTypeDef",
    {
        "eventArns": List[str],
    },
)
_OptionalDescribeEventDetailsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeEventDetailsRequestRequestTypeDef",
    {
        "locale": str,
    },
    total=False,
)

class DescribeEventDetailsRequestRequestTypeDef(
    _RequiredDescribeEventDetailsRequestRequestTypeDef,
    _OptionalDescribeEventDetailsRequestRequestTypeDef,
):
    pass

DescribeEventDetailsResponseTypeDef = TypedDict(
    "DescribeEventDetailsResponseTypeDef",
    {
        "successfulSet": List["EventDetailsTypeDef"],
        "failedSet": List["EventDetailsErrorItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventTypesRequestRequestTypeDef = TypedDict(
    "DescribeEventTypesRequestRequestTypeDef",
    {
        "filter": "EventTypeFilterTypeDef",
        "locale": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

DescribeEventTypesResponseTypeDef = TypedDict(
    "DescribeEventTypesResponseTypeDef",
    {
        "eventTypes": List["EventTypeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventsForOrganizationRequestRequestTypeDef = TypedDict(
    "DescribeEventsForOrganizationRequestRequestTypeDef",
    {
        "filter": "OrganizationEventFilterTypeDef",
        "nextToken": str,
        "maxResults": int,
        "locale": str,
    },
    total=False,
)

DescribeEventsForOrganizationResponseTypeDef = TypedDict(
    "DescribeEventsForOrganizationResponseTypeDef",
    {
        "events": List["OrganizationEventTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventsRequestRequestTypeDef = TypedDict(
    "DescribeEventsRequestRequestTypeDef",
    {
        "filter": "EventFilterTypeDef",
        "nextToken": str,
        "maxResults": int,
        "locale": str,
    },
    total=False,
)

DescribeEventsResponseTypeDef = TypedDict(
    "DescribeEventsResponseTypeDef",
    {
        "events": List["EventTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHealthServiceStatusForOrganizationResponseTypeDef = TypedDict(
    "DescribeHealthServiceStatusForOrganizationResponseTypeDef",
    {
        "healthServiceAccessStatusForOrganization": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EntityAggregateTypeDef = TypedDict(
    "EntityAggregateTypeDef",
    {
        "eventArn": str,
        "count": int,
    },
    total=False,
)

_RequiredEntityFilterTypeDef = TypedDict(
    "_RequiredEntityFilterTypeDef",
    {
        "eventArns": List[str],
    },
)
_OptionalEntityFilterTypeDef = TypedDict(
    "_OptionalEntityFilterTypeDef",
    {
        "entityArns": List[str],
        "entityValues": List[str],
        "lastUpdatedTimes": List["DateTimeRangeTypeDef"],
        "tags": List[Dict[str, str]],
        "statusCodes": List[entityStatusCodeType],
    },
    total=False,
)

class EntityFilterTypeDef(_RequiredEntityFilterTypeDef, _OptionalEntityFilterTypeDef):
    pass

_RequiredEventAccountFilterTypeDef = TypedDict(
    "_RequiredEventAccountFilterTypeDef",
    {
        "eventArn": str,
    },
)
_OptionalEventAccountFilterTypeDef = TypedDict(
    "_OptionalEventAccountFilterTypeDef",
    {
        "awsAccountId": str,
    },
    total=False,
)

class EventAccountFilterTypeDef(
    _RequiredEventAccountFilterTypeDef, _OptionalEventAccountFilterTypeDef
):
    pass

EventAggregateTypeDef = TypedDict(
    "EventAggregateTypeDef",
    {
        "aggregateValue": str,
        "count": int,
    },
    total=False,
)

EventDescriptionTypeDef = TypedDict(
    "EventDescriptionTypeDef",
    {
        "latestDescription": str,
    },
    total=False,
)

EventDetailsErrorItemTypeDef = TypedDict(
    "EventDetailsErrorItemTypeDef",
    {
        "eventArn": str,
        "errorName": str,
        "errorMessage": str,
    },
    total=False,
)

EventDetailsTypeDef = TypedDict(
    "EventDetailsTypeDef",
    {
        "event": "EventTypeDef",
        "eventDescription": "EventDescriptionTypeDef",
        "eventMetadata": Dict[str, str],
    },
    total=False,
)

EventFilterTypeDef = TypedDict(
    "EventFilterTypeDef",
    {
        "eventArns": List[str],
        "eventTypeCodes": List[str],
        "services": List[str],
        "regions": List[str],
        "availabilityZones": List[str],
        "startTimes": List["DateTimeRangeTypeDef"],
        "endTimes": List["DateTimeRangeTypeDef"],
        "lastUpdatedTimes": List["DateTimeRangeTypeDef"],
        "entityArns": List[str],
        "entityValues": List[str],
        "eventTypeCategories": List[eventTypeCategoryType],
        "tags": List[Dict[str, str]],
        "eventStatusCodes": List[eventStatusCodeType],
    },
    total=False,
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "arn": str,
        "service": str,
        "eventTypeCode": str,
        "eventTypeCategory": eventTypeCategoryType,
        "region": str,
        "availabilityZone": str,
        "startTime": datetime,
        "endTime": datetime,
        "lastUpdatedTime": datetime,
        "statusCode": eventStatusCodeType,
        "eventScopeCode": eventScopeCodeType,
    },
    total=False,
)

EventTypeFilterTypeDef = TypedDict(
    "EventTypeFilterTypeDef",
    {
        "eventTypeCodes": List[str],
        "services": List[str],
        "eventTypeCategories": List[eventTypeCategoryType],
    },
    total=False,
)

EventTypeTypeDef = TypedDict(
    "EventTypeTypeDef",
    {
        "service": str,
        "code": str,
        "category": eventTypeCategoryType,
    },
    total=False,
)

OrganizationAffectedEntitiesErrorItemTypeDef = TypedDict(
    "OrganizationAffectedEntitiesErrorItemTypeDef",
    {
        "awsAccountId": str,
        "eventArn": str,
        "errorName": str,
        "errorMessage": str,
    },
    total=False,
)

OrganizationEventDetailsErrorItemTypeDef = TypedDict(
    "OrganizationEventDetailsErrorItemTypeDef",
    {
        "awsAccountId": str,
        "eventArn": str,
        "errorName": str,
        "errorMessage": str,
    },
    total=False,
)

OrganizationEventDetailsTypeDef = TypedDict(
    "OrganizationEventDetailsTypeDef",
    {
        "awsAccountId": str,
        "event": "EventTypeDef",
        "eventDescription": "EventDescriptionTypeDef",
        "eventMetadata": Dict[str, str],
    },
    total=False,
)

OrganizationEventFilterTypeDef = TypedDict(
    "OrganizationEventFilterTypeDef",
    {
        "eventTypeCodes": List[str],
        "awsAccountIds": List[str],
        "services": List[str],
        "regions": List[str],
        "startTime": "DateTimeRangeTypeDef",
        "endTime": "DateTimeRangeTypeDef",
        "lastUpdatedTime": "DateTimeRangeTypeDef",
        "entityArns": List[str],
        "entityValues": List[str],
        "eventTypeCategories": List[eventTypeCategoryType],
        "eventStatusCodes": List[eventStatusCodeType],
    },
    total=False,
)

OrganizationEventTypeDef = TypedDict(
    "OrganizationEventTypeDef",
    {
        "arn": str,
        "service": str,
        "eventTypeCode": str,
        "eventTypeCategory": eventTypeCategoryType,
        "eventScopeCode": eventScopeCodeType,
        "region": str,
        "startTime": datetime,
        "endTime": datetime,
        "lastUpdatedTime": datetime,
        "statusCode": eventStatusCodeType,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)
