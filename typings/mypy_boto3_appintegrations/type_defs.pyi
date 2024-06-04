"""
Type annotations for appintegrations service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appintegrations.type_defs import ApplicationAssociationSummaryTypeDef

    data: ApplicationAssociationSummaryTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ApplicationAssociationSummaryTypeDef",
    "ApplicationSourceConfigTypeDef",
    "ApplicationSummaryTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateDataIntegrationRequestRequestTypeDef",
    "CreateDataIntegrationResponseTypeDef",
    "CreateEventIntegrationRequestRequestTypeDef",
    "CreateEventIntegrationResponseTypeDef",
    "DataIntegrationAssociationSummaryTypeDef",
    "DataIntegrationSummaryTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteDataIntegrationRequestRequestTypeDef",
    "DeleteEventIntegrationRequestRequestTypeDef",
    "EventFilterTypeDef",
    "EventIntegrationAssociationTypeDef",
    "EventIntegrationTypeDef",
    "ExternalUrlConfigTypeDef",
    "FileConfigurationTypeDef",
    "GetApplicationRequestRequestTypeDef",
    "GetApplicationResponseTypeDef",
    "GetDataIntegrationRequestRequestTypeDef",
    "GetDataIntegrationResponseTypeDef",
    "GetEventIntegrationRequestRequestTypeDef",
    "GetEventIntegrationResponseTypeDef",
    "ListApplicationAssociationsRequestRequestTypeDef",
    "ListApplicationAssociationsResponseTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListDataIntegrationAssociationsRequestRequestTypeDef",
    "ListDataIntegrationAssociationsResponseTypeDef",
    "ListDataIntegrationsRequestRequestTypeDef",
    "ListDataIntegrationsResponseTypeDef",
    "ListEventIntegrationAssociationsRequestRequestTypeDef",
    "ListEventIntegrationAssociationsResponseTypeDef",
    "ListEventIntegrationsRequestRequestTypeDef",
    "ListEventIntegrationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PublicationTypeDef",
    "ResponseMetadataTypeDef",
    "ScheduleConfigurationTypeDef",
    "SubscriptionTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "UpdateDataIntegrationRequestRequestTypeDef",
    "UpdateEventIntegrationRequestRequestTypeDef",
)

ApplicationAssociationSummaryTypeDef = TypedDict(
    "ApplicationAssociationSummaryTypeDef",
    {
        "ApplicationAssociationArn": str,
        "ApplicationArn": str,
        "ClientId": str,
    },
    total=False,
)

ApplicationSourceConfigTypeDef = TypedDict(
    "ApplicationSourceConfigTypeDef",
    {
        "ExternalUrlConfig": "ExternalUrlConfigTypeDef",
    },
    total=False,
)

ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Namespace": str,
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

_RequiredCreateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestRequestTypeDef",
    {
        "Name": str,
        "Namespace": str,
        "ApplicationSourceConfig": "ApplicationSourceConfigTypeDef",
    },
)
_OptionalCreateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestRequestTypeDef",
    {
        "Description": str,
        "Subscriptions": List["SubscriptionTypeDef"],
        "Publications": List["PublicationTypeDef"],
        "ClientToken": str,
        "Tags": Dict[str, str],
        "Permissions": List[str],
    },
    total=False,
)

class CreateApplicationRequestRequestTypeDef(
    _RequiredCreateApplicationRequestRequestTypeDef, _OptionalCreateApplicationRequestRequestTypeDef
):
    pass

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataIntegrationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataIntegrationRequestRequestTypeDef",
    {
        "Name": str,
        "KmsKey": str,
        "SourceURI": str,
    },
)
_OptionalCreateDataIntegrationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataIntegrationRequestRequestTypeDef",
    {
        "Description": str,
        "ScheduleConfig": "ScheduleConfigurationTypeDef",
        "Tags": Dict[str, str],
        "ClientToken": str,
        "FileConfiguration": "FileConfigurationTypeDef",
        "ObjectConfiguration": Dict[str, Dict[str, List[str]]],
    },
    total=False,
)

class CreateDataIntegrationRequestRequestTypeDef(
    _RequiredCreateDataIntegrationRequestRequestTypeDef,
    _OptionalCreateDataIntegrationRequestRequestTypeDef,
):
    pass

CreateDataIntegrationResponseTypeDef = TypedDict(
    "CreateDataIntegrationResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "KmsKey": str,
        "SourceURI": str,
        "ScheduleConfiguration": "ScheduleConfigurationTypeDef",
        "Tags": Dict[str, str],
        "ClientToken": str,
        "FileConfiguration": "FileConfigurationTypeDef",
        "ObjectConfiguration": Dict[str, Dict[str, List[str]]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEventIntegrationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
        "EventFilter": "EventFilterTypeDef",
        "EventBridgeBus": str,
    },
)
_OptionalCreateEventIntegrationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEventIntegrationRequestRequestTypeDef",
    {
        "Description": str,
        "ClientToken": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateEventIntegrationRequestRequestTypeDef(
    _RequiredCreateEventIntegrationRequestRequestTypeDef,
    _OptionalCreateEventIntegrationRequestRequestTypeDef,
):
    pass

CreateEventIntegrationResponseTypeDef = TypedDict(
    "CreateEventIntegrationResponseTypeDef",
    {
        "EventIntegrationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataIntegrationAssociationSummaryTypeDef = TypedDict(
    "DataIntegrationAssociationSummaryTypeDef",
    {
        "DataIntegrationAssociationArn": str,
        "DataIntegrationArn": str,
        "ClientId": str,
    },
    total=False,
)

DataIntegrationSummaryTypeDef = TypedDict(
    "DataIntegrationSummaryTypeDef",
    {
        "Arn": str,
        "Name": str,
        "SourceURI": str,
    },
    total=False,
)

DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

DeleteDataIntegrationRequestRequestTypeDef = TypedDict(
    "DeleteDataIntegrationRequestRequestTypeDef",
    {
        "DataIntegrationIdentifier": str,
    },
)

DeleteEventIntegrationRequestRequestTypeDef = TypedDict(
    "DeleteEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

EventFilterTypeDef = TypedDict(
    "EventFilterTypeDef",
    {
        "Source": str,
    },
)

EventIntegrationAssociationTypeDef = TypedDict(
    "EventIntegrationAssociationTypeDef",
    {
        "EventIntegrationAssociationArn": str,
        "EventIntegrationAssociationId": str,
        "EventIntegrationName": str,
        "ClientId": str,
        "EventBridgeRuleName": str,
        "ClientAssociationMetadata": Dict[str, str],
    },
    total=False,
)

EventIntegrationTypeDef = TypedDict(
    "EventIntegrationTypeDef",
    {
        "EventIntegrationArn": str,
        "Name": str,
        "Description": str,
        "EventFilter": "EventFilterTypeDef",
        "EventBridgeBus": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredExternalUrlConfigTypeDef = TypedDict(
    "_RequiredExternalUrlConfigTypeDef",
    {
        "AccessUrl": str,
    },
)
_OptionalExternalUrlConfigTypeDef = TypedDict(
    "_OptionalExternalUrlConfigTypeDef",
    {
        "ApprovedOrigins": List[str],
    },
    total=False,
)

class ExternalUrlConfigTypeDef(
    _RequiredExternalUrlConfigTypeDef, _OptionalExternalUrlConfigTypeDef
):
    pass

_RequiredFileConfigurationTypeDef = TypedDict(
    "_RequiredFileConfigurationTypeDef",
    {
        "Folders": List[str],
    },
)
_OptionalFileConfigurationTypeDef = TypedDict(
    "_OptionalFileConfigurationTypeDef",
    {
        "Filters": Dict[str, List[str]],
    },
    total=False,
)

class FileConfigurationTypeDef(
    _RequiredFileConfigurationTypeDef, _OptionalFileConfigurationTypeDef
):
    pass

GetApplicationRequestRequestTypeDef = TypedDict(
    "GetApplicationRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

GetApplicationResponseTypeDef = TypedDict(
    "GetApplicationResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Namespace": str,
        "Description": str,
        "ApplicationSourceConfig": "ApplicationSourceConfigTypeDef",
        "Subscriptions": List["SubscriptionTypeDef"],
        "Publications": List["PublicationTypeDef"],
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
        "Tags": Dict[str, str],
        "Permissions": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataIntegrationRequestRequestTypeDef = TypedDict(
    "GetDataIntegrationRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

GetDataIntegrationResponseTypeDef = TypedDict(
    "GetDataIntegrationResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "KmsKey": str,
        "SourceURI": str,
        "ScheduleConfiguration": "ScheduleConfigurationTypeDef",
        "Tags": Dict[str, str],
        "FileConfiguration": "FileConfigurationTypeDef",
        "ObjectConfiguration": Dict[str, Dict[str, List[str]]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventIntegrationRequestRequestTypeDef = TypedDict(
    "GetEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetEventIntegrationResponseTypeDef = TypedDict(
    "GetEventIntegrationResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "EventIntegrationArn": str,
        "EventBridgeBus": str,
        "EventFilter": "EventFilterTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListApplicationAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredListApplicationAssociationsRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalListApplicationAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalListApplicationAssociationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListApplicationAssociationsRequestRequestTypeDef(
    _RequiredListApplicationAssociationsRequestRequestTypeDef,
    _OptionalListApplicationAssociationsRequestRequestTypeDef,
):
    pass

ListApplicationAssociationsResponseTypeDef = TypedDict(
    "ListApplicationAssociationsResponseTypeDef",
    {
        "ApplicationAssociations": List["ApplicationAssociationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "Applications": List["ApplicationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDataIntegrationAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredListDataIntegrationAssociationsRequestRequestTypeDef",
    {
        "DataIntegrationIdentifier": str,
    },
)
_OptionalListDataIntegrationAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalListDataIntegrationAssociationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListDataIntegrationAssociationsRequestRequestTypeDef(
    _RequiredListDataIntegrationAssociationsRequestRequestTypeDef,
    _OptionalListDataIntegrationAssociationsRequestRequestTypeDef,
):
    pass

ListDataIntegrationAssociationsResponseTypeDef = TypedDict(
    "ListDataIntegrationAssociationsResponseTypeDef",
    {
        "DataIntegrationAssociations": List["DataIntegrationAssociationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataIntegrationsRequestRequestTypeDef = TypedDict(
    "ListDataIntegrationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDataIntegrationsResponseTypeDef = TypedDict(
    "ListDataIntegrationsResponseTypeDef",
    {
        "DataIntegrations": List["DataIntegrationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEventIntegrationAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredListEventIntegrationAssociationsRequestRequestTypeDef",
    {
        "EventIntegrationName": str,
    },
)
_OptionalListEventIntegrationAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalListEventIntegrationAssociationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListEventIntegrationAssociationsRequestRequestTypeDef(
    _RequiredListEventIntegrationAssociationsRequestRequestTypeDef,
    _OptionalListEventIntegrationAssociationsRequestRequestTypeDef,
):
    pass

ListEventIntegrationAssociationsResponseTypeDef = TypedDict(
    "ListEventIntegrationAssociationsResponseTypeDef",
    {
        "EventIntegrationAssociations": List["EventIntegrationAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventIntegrationsRequestRequestTypeDef = TypedDict(
    "ListEventIntegrationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEventIntegrationsResponseTypeDef = TypedDict(
    "ListEventIntegrationsResponseTypeDef",
    {
        "EventIntegrations": List["EventIntegrationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredPublicationTypeDef = TypedDict(
    "_RequiredPublicationTypeDef",
    {
        "Event": str,
        "Schema": str,
    },
)
_OptionalPublicationTypeDef = TypedDict(
    "_OptionalPublicationTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class PublicationTypeDef(_RequiredPublicationTypeDef, _OptionalPublicationTypeDef):
    pass

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

_RequiredScheduleConfigurationTypeDef = TypedDict(
    "_RequiredScheduleConfigurationTypeDef",
    {
        "ScheduleExpression": str,
    },
)
_OptionalScheduleConfigurationTypeDef = TypedDict(
    "_OptionalScheduleConfigurationTypeDef",
    {
        "FirstExecutionFrom": str,
        "Object": str,
    },
    total=False,
)

class ScheduleConfigurationTypeDef(
    _RequiredScheduleConfigurationTypeDef, _OptionalScheduleConfigurationTypeDef
):
    pass

_RequiredSubscriptionTypeDef = TypedDict(
    "_RequiredSubscriptionTypeDef",
    {
        "Event": str,
    },
)
_OptionalSubscriptionTypeDef = TypedDict(
    "_OptionalSubscriptionTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class SubscriptionTypeDef(_RequiredSubscriptionTypeDef, _OptionalSubscriptionTypeDef):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationRequestRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "ApplicationSourceConfig": "ApplicationSourceConfigTypeDef",
        "Subscriptions": List["SubscriptionTypeDef"],
        "Publications": List["PublicationTypeDef"],
        "Permissions": List[str],
    },
    total=False,
)

class UpdateApplicationRequestRequestTypeDef(
    _RequiredUpdateApplicationRequestRequestTypeDef, _OptionalUpdateApplicationRequestRequestTypeDef
):
    pass

_RequiredUpdateDataIntegrationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDataIntegrationRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
_OptionalUpdateDataIntegrationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDataIntegrationRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)

class UpdateDataIntegrationRequestRequestTypeDef(
    _RequiredUpdateDataIntegrationRequestRequestTypeDef,
    _OptionalUpdateDataIntegrationRequestRequestTypeDef,
):
    pass

_RequiredUpdateEventIntegrationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateEventIntegrationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEventIntegrationRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateEventIntegrationRequestRequestTypeDef(
    _RequiredUpdateEventIntegrationRequestRequestTypeDef,
    _OptionalUpdateEventIntegrationRequestRequestTypeDef,
):
    pass
