"""
Type annotations for appintegrations service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_appintegrations.type_defs import ApplicationAssociationSummaryTypeDef

    data: ApplicationAssociationSummaryTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import ExecutionModeType, ExecutionStatusType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ApplicationAssociationSummaryTypeDef",
    "ApplicationSourceConfigOutputTypeDef",
    "ApplicationSourceConfigTypeDef",
    "ApplicationSourceConfigUnionTypeDef",
    "ApplicationSummaryTypeDef",
    "CreateApplicationRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateDataIntegrationAssociationRequestTypeDef",
    "CreateDataIntegrationAssociationResponseTypeDef",
    "CreateDataIntegrationRequestTypeDef",
    "CreateDataIntegrationResponseTypeDef",
    "CreateEventIntegrationRequestTypeDef",
    "CreateEventIntegrationResponseTypeDef",
    "DataIntegrationAssociationSummaryTypeDef",
    "DataIntegrationSummaryTypeDef",
    "DeleteApplicationRequestTypeDef",
    "DeleteDataIntegrationRequestTypeDef",
    "DeleteEventIntegrationRequestTypeDef",
    "EventFilterTypeDef",
    "EventIntegrationAssociationTypeDef",
    "EventIntegrationTypeDef",
    "ExecutionConfigurationTypeDef",
    "ExternalUrlConfigOutputTypeDef",
    "ExternalUrlConfigTypeDef",
    "FileConfigurationOutputTypeDef",
    "FileConfigurationTypeDef",
    "FileConfigurationUnionTypeDef",
    "GetApplicationRequestTypeDef",
    "GetApplicationResponseTypeDef",
    "GetDataIntegrationRequestTypeDef",
    "GetDataIntegrationResponseTypeDef",
    "GetEventIntegrationRequestTypeDef",
    "GetEventIntegrationResponseTypeDef",
    "LastExecutionStatusTypeDef",
    "ListApplicationAssociationsRequestPaginateTypeDef",
    "ListApplicationAssociationsRequestTypeDef",
    "ListApplicationAssociationsResponseTypeDef",
    "ListApplicationsRequestPaginateTypeDef",
    "ListApplicationsRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListDataIntegrationAssociationsRequestPaginateTypeDef",
    "ListDataIntegrationAssociationsRequestTypeDef",
    "ListDataIntegrationAssociationsResponseTypeDef",
    "ListDataIntegrationsRequestPaginateTypeDef",
    "ListDataIntegrationsRequestTypeDef",
    "ListDataIntegrationsResponseTypeDef",
    "ListEventIntegrationAssociationsRequestPaginateTypeDef",
    "ListEventIntegrationAssociationsRequestTypeDef",
    "ListEventIntegrationAssociationsResponseTypeDef",
    "ListEventIntegrationsRequestPaginateTypeDef",
    "ListEventIntegrationsRequestTypeDef",
    "ListEventIntegrationsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OnDemandConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PublicationTypeDef",
    "ResponseMetadataTypeDef",
    "ScheduleConfigurationTypeDef",
    "SubscriptionTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateApplicationRequestTypeDef",
    "UpdateDataIntegrationAssociationRequestTypeDef",
    "UpdateDataIntegrationRequestTypeDef",
    "UpdateEventIntegrationRequestTypeDef",
)

class ApplicationAssociationSummaryTypeDef(TypedDict):
    ApplicationAssociationArn: NotRequired[str]
    ApplicationArn: NotRequired[str]
    ClientId: NotRequired[str]

class ExternalUrlConfigOutputTypeDef(TypedDict):
    AccessUrl: str
    ApprovedOrigins: NotRequired[List[str]]

class ExternalUrlConfigTypeDef(TypedDict):
    AccessUrl: str
    ApprovedOrigins: NotRequired[Sequence[str]]

class ApplicationSummaryTypeDef(TypedDict):
    Arn: NotRequired[str]
    Id: NotRequired[str]
    Name: NotRequired[str]
    Namespace: NotRequired[str]
    CreatedTime: NotRequired[datetime]
    LastModifiedTime: NotRequired[datetime]

class PublicationTypeDef(TypedDict):
    Event: str
    Schema: str
    Description: NotRequired[str]

class SubscriptionTypeDef(TypedDict):
    Event: str
    Description: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ScheduleConfigurationTypeDef(TypedDict):
    ScheduleExpression: str
    FirstExecutionFrom: NotRequired[str]
    Object: NotRequired[str]

class FileConfigurationOutputTypeDef(TypedDict):
    Folders: List[str]
    Filters: NotRequired[Dict[str, List[str]]]

class EventFilterTypeDef(TypedDict):
    Source: str

class LastExecutionStatusTypeDef(TypedDict):
    ExecutionStatus: NotRequired[ExecutionStatusType]
    StatusMessage: NotRequired[str]

class DataIntegrationSummaryTypeDef(TypedDict):
    Arn: NotRequired[str]
    Name: NotRequired[str]
    SourceURI: NotRequired[str]

class DeleteApplicationRequestTypeDef(TypedDict):
    Arn: str

class DeleteDataIntegrationRequestTypeDef(TypedDict):
    DataIntegrationIdentifier: str

class DeleteEventIntegrationRequestTypeDef(TypedDict):
    Name: str

class EventIntegrationAssociationTypeDef(TypedDict):
    EventIntegrationAssociationArn: NotRequired[str]
    EventIntegrationAssociationId: NotRequired[str]
    EventIntegrationName: NotRequired[str]
    ClientId: NotRequired[str]
    EventBridgeRuleName: NotRequired[str]
    ClientAssociationMetadata: NotRequired[Dict[str, str]]

class OnDemandConfigurationTypeDef(TypedDict):
    StartTime: str
    EndTime: NotRequired[str]

class FileConfigurationTypeDef(TypedDict):
    Folders: Sequence[str]
    Filters: NotRequired[Mapping[str, Sequence[str]]]

class GetApplicationRequestTypeDef(TypedDict):
    Arn: str

class GetDataIntegrationRequestTypeDef(TypedDict):
    Identifier: str

class GetEventIntegrationRequestTypeDef(TypedDict):
    Name: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListApplicationAssociationsRequestTypeDef(TypedDict):
    ApplicationId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListApplicationsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListDataIntegrationAssociationsRequestTypeDef(TypedDict):
    DataIntegrationIdentifier: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListDataIntegrationsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListEventIntegrationAssociationsRequestTypeDef(TypedDict):
    EventIntegrationName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListEventIntegrationsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateDataIntegrationRequestTypeDef(TypedDict):
    Identifier: str
    Name: NotRequired[str]
    Description: NotRequired[str]

class UpdateEventIntegrationRequestTypeDef(TypedDict):
    Name: str
    Description: NotRequired[str]

class ApplicationSourceConfigOutputTypeDef(TypedDict):
    ExternalUrlConfig: NotRequired[ExternalUrlConfigOutputTypeDef]

class ApplicationSourceConfigTypeDef(TypedDict):
    ExternalUrlConfig: NotRequired[ExternalUrlConfigTypeDef]

class CreateApplicationResponseTypeDef(TypedDict):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataIntegrationAssociationResponseTypeDef(TypedDict):
    DataIntegrationAssociationId: str
    DataIntegrationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventIntegrationResponseTypeDef(TypedDict):
    EventIntegrationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationAssociationsResponseTypeDef(TypedDict):
    ApplicationAssociations: List[ApplicationAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListApplicationsResponseTypeDef(TypedDict):
    Applications: List[ApplicationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataIntegrationResponseTypeDef(TypedDict):
    Arn: str
    Id: str
    Name: str
    Description: str
    KmsKey: str
    SourceURI: str
    ScheduleConfiguration: ScheduleConfigurationTypeDef
    Tags: Dict[str, str]
    ClientToken: str
    FileConfiguration: FileConfigurationOutputTypeDef
    ObjectConfiguration: Dict[str, Dict[str, List[str]]]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataIntegrationResponseTypeDef(TypedDict):
    Arn: str
    Id: str
    Name: str
    Description: str
    KmsKey: str
    SourceURI: str
    ScheduleConfiguration: ScheduleConfigurationTypeDef
    Tags: Dict[str, str]
    FileConfiguration: FileConfigurationOutputTypeDef
    ObjectConfiguration: Dict[str, Dict[str, List[str]]]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventIntegrationRequestTypeDef(TypedDict):
    Name: str
    EventFilter: EventFilterTypeDef
    EventBridgeBus: str
    Description: NotRequired[str]
    ClientToken: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class EventIntegrationTypeDef(TypedDict):
    EventIntegrationArn: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    EventFilter: NotRequired[EventFilterTypeDef]
    EventBridgeBus: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]

class GetEventIntegrationResponseTypeDef(TypedDict):
    Name: str
    Description: str
    EventIntegrationArn: str
    EventBridgeBus: str
    EventFilter: EventFilterTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataIntegrationsResponseTypeDef(TypedDict):
    DataIntegrations: List[DataIntegrationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListEventIntegrationAssociationsResponseTypeDef(TypedDict):
    EventIntegrationAssociations: List[EventIntegrationAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ExecutionConfigurationTypeDef(TypedDict):
    ExecutionMode: ExecutionModeType
    OnDemandConfiguration: NotRequired[OnDemandConfigurationTypeDef]
    ScheduleConfiguration: NotRequired[ScheduleConfigurationTypeDef]

FileConfigurationUnionTypeDef = Union[FileConfigurationTypeDef, FileConfigurationOutputTypeDef]

class ListApplicationAssociationsRequestPaginateTypeDef(TypedDict):
    ApplicationId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListApplicationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDataIntegrationAssociationsRequestPaginateTypeDef(TypedDict):
    DataIntegrationIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDataIntegrationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEventIntegrationAssociationsRequestPaginateTypeDef(TypedDict):
    EventIntegrationName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEventIntegrationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetApplicationResponseTypeDef(TypedDict):
    Arn: str
    Id: str
    Name: str
    Namespace: str
    Description: str
    ApplicationSourceConfig: ApplicationSourceConfigOutputTypeDef
    Subscriptions: List[SubscriptionTypeDef]
    Publications: List[PublicationTypeDef]
    CreatedTime: datetime
    LastModifiedTime: datetime
    Tags: Dict[str, str]
    Permissions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

ApplicationSourceConfigUnionTypeDef = Union[
    ApplicationSourceConfigTypeDef, ApplicationSourceConfigOutputTypeDef
]

class ListEventIntegrationsResponseTypeDef(TypedDict):
    EventIntegrations: List[EventIntegrationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateDataIntegrationAssociationRequestTypeDef(TypedDict):
    DataIntegrationIdentifier: str
    ClientId: NotRequired[str]
    ObjectConfiguration: NotRequired[Mapping[str, Mapping[str, Sequence[str]]]]
    DestinationURI: NotRequired[str]
    ClientAssociationMetadata: NotRequired[Mapping[str, str]]
    ClientToken: NotRequired[str]
    ExecutionConfiguration: NotRequired[ExecutionConfigurationTypeDef]

class DataIntegrationAssociationSummaryTypeDef(TypedDict):
    DataIntegrationAssociationArn: NotRequired[str]
    DataIntegrationArn: NotRequired[str]
    ClientId: NotRequired[str]
    DestinationURI: NotRequired[str]
    LastExecutionStatus: NotRequired[LastExecutionStatusTypeDef]
    ExecutionConfiguration: NotRequired[ExecutionConfigurationTypeDef]

class UpdateDataIntegrationAssociationRequestTypeDef(TypedDict):
    DataIntegrationIdentifier: str
    DataIntegrationAssociationIdentifier: str
    ExecutionConfiguration: ExecutionConfigurationTypeDef

class CreateDataIntegrationRequestTypeDef(TypedDict):
    Name: str
    KmsKey: str
    Description: NotRequired[str]
    SourceURI: NotRequired[str]
    ScheduleConfig: NotRequired[ScheduleConfigurationTypeDef]
    Tags: NotRequired[Mapping[str, str]]
    ClientToken: NotRequired[str]
    FileConfiguration: NotRequired[FileConfigurationUnionTypeDef]
    ObjectConfiguration: NotRequired[Mapping[str, Mapping[str, Sequence[str]]]]

class CreateApplicationRequestTypeDef(TypedDict):
    Name: str
    Namespace: str
    ApplicationSourceConfig: ApplicationSourceConfigUnionTypeDef
    Description: NotRequired[str]
    Subscriptions: NotRequired[Sequence[SubscriptionTypeDef]]
    Publications: NotRequired[Sequence[PublicationTypeDef]]
    ClientToken: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    Permissions: NotRequired[Sequence[str]]

class UpdateApplicationRequestTypeDef(TypedDict):
    Arn: str
    Name: NotRequired[str]
    Description: NotRequired[str]
    ApplicationSourceConfig: NotRequired[ApplicationSourceConfigUnionTypeDef]
    Subscriptions: NotRequired[Sequence[SubscriptionTypeDef]]
    Publications: NotRequired[Sequence[PublicationTypeDef]]
    Permissions: NotRequired[Sequence[str]]

class ListDataIntegrationAssociationsResponseTypeDef(TypedDict):
    DataIntegrationAssociations: List[DataIntegrationAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
