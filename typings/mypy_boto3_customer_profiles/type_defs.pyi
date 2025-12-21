"""
Type annotations for customer-profiles service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_customer_profiles.type_defs import AddProfileKeyRequestTypeDef

    data: AddProfileKeyRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ActionTypeType,
    AttributeDimensionTypeType,
    AttributeMatchingModelType,
    ComparisonOperatorType,
    ConflictResolvingModelType,
    ContactTypeType,
    ContentTypeType,
    DataFormatType,
    DataPullModeType,
    DateDimensionTypeType,
    EstimateStatusType,
    EventStreamDestinationStatusType,
    EventStreamStateType,
    EventTriggerLogicalOperatorType,
    FeatureTypeType,
    FieldContentTypeType,
    FilterDimensionTypeType,
    GenderType,
    IdentityResolutionJobStatusType,
    IncludeOptionsType,
    IncludeType,
    JobScheduleDayOfTheWeekType,
    LogicalOperatorType,
    MarketoConnectorOperatorType,
    MatchTypeType,
    OperatorPropertiesKeysType,
    OperatorType,
    PartyTypeType,
    PeriodUnitType,
    ProfileTypeDimensionTypeType,
    ProfileTypeType,
    QueryResultType,
    ReadinessStatusType,
    RecommenderRecipeNameType,
    RecommenderStatusType,
    RuleBasedMatchingStatusType,
    S3ConnectorOperatorType,
    SalesforceConnectorOperatorType,
    ScopeType,
    SegmentSnapshotStatusType,
    SegmentTypeType,
    ServiceNowConnectorOperatorType,
    SourceConnectorTypeType,
    StandardIdentifierType,
    StatisticType,
    StatusReasonType,
    StatusType,
    StringDimensionTypeType,
    TaskTypeType,
    TrainingMetricNameType,
    TriggerTypeType,
    TypeType,
    UploadJobStatusType,
    ZendeskConnectorOperatorType,
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
    "AddProfileKeyRequestTypeDef",
    "AddProfileKeyResponseTypeDef",
    "AdditionalSearchKeyTypeDef",
    "AddressDimensionOutputTypeDef",
    "AddressDimensionTypeDef",
    "AddressDimensionUnionTypeDef",
    "AddressTypeDef",
    "AppflowIntegrationTypeDef",
    "AppflowIntegrationWorkflowAttributesTypeDef",
    "AppflowIntegrationWorkflowMetricsTypeDef",
    "AppflowIntegrationWorkflowStepTypeDef",
    "AttributeDetailsOutputTypeDef",
    "AttributeDetailsTypeDef",
    "AttributeDetailsUnionTypeDef",
    "AttributeDimensionOutputTypeDef",
    "AttributeDimensionTypeDef",
    "AttributeDimensionUnionTypeDef",
    "AttributeItemTypeDef",
    "AttributeTypesSelectorOutputTypeDef",
    "AttributeTypesSelectorTypeDef",
    "AttributeTypesSelectorUnionTypeDef",
    "AttributeValueItemTypeDef",
    "AutoMergingOutputTypeDef",
    "AutoMergingTypeDef",
    "AutoMergingUnionTypeDef",
    "BatchGetCalculatedAttributeForProfileErrorTypeDef",
    "BatchGetCalculatedAttributeForProfileRequestTypeDef",
    "BatchGetCalculatedAttributeForProfileResponseTypeDef",
    "BatchGetProfileErrorTypeDef",
    "BatchGetProfileRequestTypeDef",
    "BatchGetProfileResponseTypeDef",
    "BatchTypeDef",
    "CalculatedAttributeDimensionOutputTypeDef",
    "CalculatedAttributeDimensionTypeDef",
    "CalculatedAttributeDimensionUnionTypeDef",
    "CalculatedAttributeValueTypeDef",
    "CatalogItemTypeDef",
    "ConditionOverridesTypeDef",
    "ConditionsTypeDef",
    "ConflictResolutionTypeDef",
    "ConnectorOperatorTypeDef",
    "ConsolidationOutputTypeDef",
    "ConsolidationTypeDef",
    "ConsolidationUnionTypeDef",
    "ContactPreferenceTypeDef",
    "CreateCalculatedAttributeDefinitionRequestTypeDef",
    "CreateCalculatedAttributeDefinitionResponseTypeDef",
    "CreateDomainLayoutRequestTypeDef",
    "CreateDomainLayoutResponseTypeDef",
    "CreateDomainRequestTypeDef",
    "CreateDomainResponseTypeDef",
    "CreateEventStreamRequestTypeDef",
    "CreateEventStreamResponseTypeDef",
    "CreateEventTriggerRequestTypeDef",
    "CreateEventTriggerResponseTypeDef",
    "CreateIntegrationWorkflowRequestTypeDef",
    "CreateIntegrationWorkflowResponseTypeDef",
    "CreateProfileRequestTypeDef",
    "CreateProfileResponseTypeDef",
    "CreateRecommenderRequestTypeDef",
    "CreateRecommenderResponseTypeDef",
    "CreateSegmentDefinitionRequestTypeDef",
    "CreateSegmentDefinitionResponseTypeDef",
    "CreateSegmentEstimateRequestTypeDef",
    "CreateSegmentEstimateResponseTypeDef",
    "CreateSegmentSnapshotRequestTypeDef",
    "CreateSegmentSnapshotResponseTypeDef",
    "CreateUploadJobRequestTypeDef",
    "CreateUploadJobResponseTypeDef",
    "DataStoreRequestTypeDef",
    "DataStoreResponseTypeDef",
    "DateDimensionOutputTypeDef",
    "DateDimensionTypeDef",
    "DateDimensionUnionTypeDef",
    "DeleteCalculatedAttributeDefinitionRequestTypeDef",
    "DeleteDomainLayoutRequestTypeDef",
    "DeleteDomainLayoutResponseTypeDef",
    "DeleteDomainObjectTypeRequestTypeDef",
    "DeleteDomainRequestTypeDef",
    "DeleteDomainResponseTypeDef",
    "DeleteEventStreamRequestTypeDef",
    "DeleteEventTriggerRequestTypeDef",
    "DeleteEventTriggerResponseTypeDef",
    "DeleteIntegrationRequestTypeDef",
    "DeleteIntegrationResponseTypeDef",
    "DeleteProfileKeyRequestTypeDef",
    "DeleteProfileKeyResponseTypeDef",
    "DeleteProfileObjectRequestTypeDef",
    "DeleteProfileObjectResponseTypeDef",
    "DeleteProfileObjectTypeRequestTypeDef",
    "DeleteProfileObjectTypeResponseTypeDef",
    "DeleteProfileRequestTypeDef",
    "DeleteProfileResponseTypeDef",
    "DeleteRecommenderRequestTypeDef",
    "DeleteSegmentDefinitionRequestTypeDef",
    "DeleteSegmentDefinitionResponseTypeDef",
    "DeleteWorkflowRequestTypeDef",
    "DestinationSummaryTypeDef",
    "DetectProfileObjectTypeRequestTypeDef",
    "DetectProfileObjectTypeResponseTypeDef",
    "DetectedProfileObjectTypeTypeDef",
    "DimensionOutputTypeDef",
    "DimensionTypeDef",
    "DimensionUnionTypeDef",
    "DomainObjectTypeFieldTypeDef",
    "DomainObjectTypesListItemTypeDef",
    "DomainStatsTypeDef",
    "EngagementPreferencesOutputTypeDef",
    "EngagementPreferencesTypeDef",
    "EngagementPreferencesUnionTypeDef",
    "EventParametersTypeDef",
    "EventStreamDestinationDetailsTypeDef",
    "EventStreamSummaryTypeDef",
    "EventTriggerConditionOutputTypeDef",
    "EventTriggerConditionTypeDef",
    "EventTriggerConditionUnionTypeDef",
    "EventTriggerDimensionOutputTypeDef",
    "EventTriggerDimensionTypeDef",
    "EventTriggerDimensionUnionTypeDef",
    "EventTriggerLimitsOutputTypeDef",
    "EventTriggerLimitsTypeDef",
    "EventTriggerLimitsUnionTypeDef",
    "EventTriggerSummaryItemTypeDef",
    "EventsConfigOutputTypeDef",
    "EventsConfigTypeDef",
    "ExportingConfigTypeDef",
    "ExportingLocationTypeDef",
    "ExtraLengthValueProfileDimensionOutputTypeDef",
    "ExtraLengthValueProfileDimensionTypeDef",
    "ExtraLengthValueProfileDimensionUnionTypeDef",
    "FieldSourceProfileIdsTypeDef",
    "FilterAttributeDimensionOutputTypeDef",
    "FilterAttributeDimensionTypeDef",
    "FilterDimensionOutputTypeDef",
    "FilterDimensionTypeDef",
    "FilterGroupOutputTypeDef",
    "FilterGroupTypeDef",
    "FilterOutputTypeDef",
    "FilterTypeDef",
    "FilterUnionTypeDef",
    "FlowDefinitionTypeDef",
    "FoundByKeyValueTypeDef",
    "GetAutoMergingPreviewRequestTypeDef",
    "GetAutoMergingPreviewResponseTypeDef",
    "GetCalculatedAttributeDefinitionRequestTypeDef",
    "GetCalculatedAttributeDefinitionResponseTypeDef",
    "GetCalculatedAttributeForProfileRequestTypeDef",
    "GetCalculatedAttributeForProfileResponseTypeDef",
    "GetDomainLayoutRequestTypeDef",
    "GetDomainLayoutResponseTypeDef",
    "GetDomainObjectTypeRequestTypeDef",
    "GetDomainObjectTypeResponseTypeDef",
    "GetDomainRequestTypeDef",
    "GetDomainResponseTypeDef",
    "GetEventStreamRequestTypeDef",
    "GetEventStreamResponseTypeDef",
    "GetEventTriggerRequestTypeDef",
    "GetEventTriggerResponseTypeDef",
    "GetIdentityResolutionJobRequestTypeDef",
    "GetIdentityResolutionJobResponseTypeDef",
    "GetIntegrationRequestTypeDef",
    "GetIntegrationResponseTypeDef",
    "GetMatchesRequestTypeDef",
    "GetMatchesResponseTypeDef",
    "GetObjectTypeAttributeStatisticsPercentilesTypeDef",
    "GetObjectTypeAttributeStatisticsRequestTypeDef",
    "GetObjectTypeAttributeStatisticsResponseTypeDef",
    "GetObjectTypeAttributeStatisticsStatsTypeDef",
    "GetProfileHistoryRecordRequestTypeDef",
    "GetProfileHistoryRecordResponseTypeDef",
    "GetProfileObjectTypeRequestTypeDef",
    "GetProfileObjectTypeResponseTypeDef",
    "GetProfileObjectTypeTemplateRequestTypeDef",
    "GetProfileObjectTypeTemplateResponseTypeDef",
    "GetProfileRecommendationsRequestTypeDef",
    "GetProfileRecommendationsResponseTypeDef",
    "GetRecommenderRequestTypeDef",
    "GetRecommenderResponseTypeDef",
    "GetSegmentDefinitionRequestTypeDef",
    "GetSegmentDefinitionResponseTypeDef",
    "GetSegmentEstimateRequestTypeDef",
    "GetSegmentEstimateResponseTypeDef",
    "GetSegmentMembershipRequestTypeDef",
    "GetSegmentMembershipResponseTypeDef",
    "GetSegmentSnapshotRequestTypeDef",
    "GetSegmentSnapshotResponseTypeDef",
    "GetSimilarProfilesRequestPaginateTypeDef",
    "GetSimilarProfilesRequestTypeDef",
    "GetSimilarProfilesResponseTypeDef",
    "GetUploadJobPathRequestTypeDef",
    "GetUploadJobPathResponseTypeDef",
    "GetUploadJobRequestTypeDef",
    "GetUploadJobResponseTypeDef",
    "GetWorkflowRequestTypeDef",
    "GetWorkflowResponseTypeDef",
    "GetWorkflowStepsRequestTypeDef",
    "GetWorkflowStepsResponseTypeDef",
    "GroupOutputTypeDef",
    "GroupTypeDef",
    "GroupUnionTypeDef",
    "IdentityResolutionJobTypeDef",
    "IncrementalPullConfigTypeDef",
    "IntegrationConfigTypeDef",
    "JobScheduleTypeDef",
    "JobStatsTypeDef",
    "LayoutItemTypeDef",
    "ListAccountIntegrationsRequestTypeDef",
    "ListAccountIntegrationsResponseTypeDef",
    "ListCalculatedAttributeDefinitionItemTypeDef",
    "ListCalculatedAttributeDefinitionsRequestTypeDef",
    "ListCalculatedAttributeDefinitionsResponseTypeDef",
    "ListCalculatedAttributeForProfileItemTypeDef",
    "ListCalculatedAttributesForProfileRequestTypeDef",
    "ListCalculatedAttributesForProfileResponseTypeDef",
    "ListDomainItemTypeDef",
    "ListDomainLayoutsRequestPaginateTypeDef",
    "ListDomainLayoutsRequestTypeDef",
    "ListDomainLayoutsResponseTypeDef",
    "ListDomainObjectTypesRequestPaginateTypeDef",
    "ListDomainObjectTypesRequestTypeDef",
    "ListDomainObjectTypesResponseTypeDef",
    "ListDomainsRequestTypeDef",
    "ListDomainsResponseTypeDef",
    "ListEventStreamsRequestPaginateTypeDef",
    "ListEventStreamsRequestTypeDef",
    "ListEventStreamsResponseTypeDef",
    "ListEventTriggersRequestPaginateTypeDef",
    "ListEventTriggersRequestTypeDef",
    "ListEventTriggersResponseTypeDef",
    "ListIdentityResolutionJobsRequestTypeDef",
    "ListIdentityResolutionJobsResponseTypeDef",
    "ListIntegrationItemTypeDef",
    "ListIntegrationsRequestTypeDef",
    "ListIntegrationsResponseTypeDef",
    "ListObjectTypeAttributeItemTypeDef",
    "ListObjectTypeAttributeValuesItemTypeDef",
    "ListObjectTypeAttributeValuesRequestTypeDef",
    "ListObjectTypeAttributeValuesResponseTypeDef",
    "ListObjectTypeAttributesRequestPaginateTypeDef",
    "ListObjectTypeAttributesRequestTypeDef",
    "ListObjectTypeAttributesResponseTypeDef",
    "ListProfileHistoryRecordsRequestTypeDef",
    "ListProfileHistoryRecordsResponseTypeDef",
    "ListProfileObjectTypeItemTypeDef",
    "ListProfileObjectTypeTemplateItemTypeDef",
    "ListProfileObjectTypeTemplatesRequestTypeDef",
    "ListProfileObjectTypeTemplatesResponseTypeDef",
    "ListProfileObjectTypesRequestTypeDef",
    "ListProfileObjectTypesResponseTypeDef",
    "ListProfileObjectsItemTypeDef",
    "ListProfileObjectsRequestTypeDef",
    "ListProfileObjectsResponseTypeDef",
    "ListRecommenderRecipesRequestPaginateTypeDef",
    "ListRecommenderRecipesRequestTypeDef",
    "ListRecommenderRecipesResponseTypeDef",
    "ListRecommendersRequestPaginateTypeDef",
    "ListRecommendersRequestTypeDef",
    "ListRecommendersResponseTypeDef",
    "ListRuleBasedMatchesRequestPaginateTypeDef",
    "ListRuleBasedMatchesRequestTypeDef",
    "ListRuleBasedMatchesResponseTypeDef",
    "ListSegmentDefinitionsRequestPaginateTypeDef",
    "ListSegmentDefinitionsRequestTypeDef",
    "ListSegmentDefinitionsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUploadJobsRequestPaginateTypeDef",
    "ListUploadJobsRequestTypeDef",
    "ListUploadJobsResponseTypeDef",
    "ListWorkflowsItemTypeDef",
    "ListWorkflowsRequestTypeDef",
    "ListWorkflowsResponseTypeDef",
    "MarketoSourcePropertiesTypeDef",
    "MatchItemTypeDef",
    "MatchingRequestTypeDef",
    "MatchingResponseTypeDef",
    "MatchingRuleOutputTypeDef",
    "MatchingRuleTypeDef",
    "MatchingRuleUnionTypeDef",
    "MergeProfilesRequestTypeDef",
    "MergeProfilesResponseTypeDef",
    "ObjectAttributeOutputTypeDef",
    "ObjectAttributeTypeDef",
    "ObjectAttributeUnionTypeDef",
    "ObjectFilterTypeDef",
    "ObjectTypeFieldTypeDef",
    "ObjectTypeKeyOutputTypeDef",
    "ObjectTypeKeyTypeDef",
    "ObjectTypeKeyUnionTypeDef",
    "PaginatorConfigTypeDef",
    "PeriodTypeDef",
    "ProfileAttributeValuesRequestTypeDef",
    "ProfileAttributeValuesResponseTypeDef",
    "ProfileAttributesOutputTypeDef",
    "ProfileAttributesTypeDef",
    "ProfileAttributesUnionTypeDef",
    "ProfileDimensionOutputTypeDef",
    "ProfileDimensionTypeDef",
    "ProfileDimensionUnionTypeDef",
    "ProfileHistoryRecordTypeDef",
    "ProfileQueryFailuresTypeDef",
    "ProfileQueryResultTypeDef",
    "ProfileTypeDef",
    "ProfileTypeDimensionOutputTypeDef",
    "ProfileTypeDimensionTypeDef",
    "ProfileTypeDimensionUnionTypeDef",
    "PutDomainObjectTypeRequestTypeDef",
    "PutDomainObjectTypeResponseTypeDef",
    "PutIntegrationRequestTypeDef",
    "PutIntegrationResponseTypeDef",
    "PutProfileObjectRequestTypeDef",
    "PutProfileObjectResponseTypeDef",
    "PutProfileObjectTypeRequestTypeDef",
    "PutProfileObjectTypeResponseTypeDef",
    "RangeOverrideTypeDef",
    "RangeTypeDef",
    "ReadinessTypeDef",
    "RecommendationTypeDef",
    "RecommenderConfigOutputTypeDef",
    "RecommenderConfigTypeDef",
    "RecommenderConfigUnionTypeDef",
    "RecommenderRecipeTypeDef",
    "RecommenderSummaryTypeDef",
    "RecommenderUpdateTypeDef",
    "ResponseMetadataTypeDef",
    "ResultsSummaryTypeDef",
    "RuleBasedMatchingRequestTypeDef",
    "RuleBasedMatchingResponseTypeDef",
    "S3ExportingConfigTypeDef",
    "S3ExportingLocationTypeDef",
    "S3SourcePropertiesTypeDef",
    "SalesforceSourcePropertiesTypeDef",
    "ScheduledTriggerPropertiesTypeDef",
    "SearchProfilesRequestTypeDef",
    "SearchProfilesResponseTypeDef",
    "SegmentDefinitionItemTypeDef",
    "SegmentGroupOutputTypeDef",
    "SegmentGroupStructureTypeDef",
    "SegmentGroupTypeDef",
    "SegmentGroupUnionTypeDef",
    "ServiceNowSourcePropertiesTypeDef",
    "SourceConnectorPropertiesTypeDef",
    "SourceFlowConfigTypeDef",
    "SourceSegmentTypeDef",
    "StartRecommenderRequestTypeDef",
    "StartUploadJobRequestTypeDef",
    "StopRecommenderRequestTypeDef",
    "StopUploadJobRequestTypeDef",
    "TagResourceRequestTypeDef",
    "TaskTypeDef",
    "ThresholdTypeDef",
    "TimestampTypeDef",
    "TrainingMetricsTypeDef",
    "TriggerConfigTypeDef",
    "TriggerPropertiesTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAddressTypeDef",
    "UpdateCalculatedAttributeDefinitionRequestTypeDef",
    "UpdateCalculatedAttributeDefinitionResponseTypeDef",
    "UpdateDomainLayoutRequestTypeDef",
    "UpdateDomainLayoutResponseTypeDef",
    "UpdateDomainRequestTypeDef",
    "UpdateDomainResponseTypeDef",
    "UpdateEventTriggerRequestTypeDef",
    "UpdateEventTriggerResponseTypeDef",
    "UpdateProfileRequestTypeDef",
    "UpdateProfileResponseTypeDef",
    "UpdateRecommenderRequestTypeDef",
    "UpdateRecommenderResponseTypeDef",
    "UploadJobItemTypeDef",
    "ValueRangeTypeDef",
    "WorkflowAttributesTypeDef",
    "WorkflowMetricsTypeDef",
    "WorkflowStepItemTypeDef",
    "ZendeskSourcePropertiesTypeDef",
)

class AddProfileKeyRequestTypeDef(TypedDict):
    ProfileId: str
    KeyName: str
    Values: Sequence[str]
    DomainName: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AdditionalSearchKeyTypeDef(TypedDict):
    KeyName: str
    Values: Sequence[str]

class ProfileDimensionOutputTypeDef(TypedDict):
    DimensionType: StringDimensionTypeType
    Values: List[str]

class AddressTypeDef(TypedDict):
    Address1: NotRequired[str]
    Address2: NotRequired[str]
    Address3: NotRequired[str]
    Address4: NotRequired[str]
    City: NotRequired[str]
    County: NotRequired[str]
    State: NotRequired[str]
    Province: NotRequired[str]
    Country: NotRequired[str]
    PostalCode: NotRequired[str]

class AppflowIntegrationWorkflowAttributesTypeDef(TypedDict):
    SourceConnectorType: SourceConnectorTypeType
    ConnectorProfileName: str
    RoleArn: NotRequired[str]

class AppflowIntegrationWorkflowMetricsTypeDef(TypedDict):
    RecordsProcessed: int
    StepsCompleted: int
    TotalSteps: int

class AppflowIntegrationWorkflowStepTypeDef(TypedDict):
    FlowName: str
    Status: StatusType
    ExecutionMessage: str
    RecordsProcessed: int
    BatchRecordsStartTime: str
    BatchRecordsEndTime: str
    CreatedAt: datetime
    LastUpdatedAt: datetime

class AttributeItemTypeDef(TypedDict):
    Name: str

class AttributeDimensionOutputTypeDef(TypedDict):
    DimensionType: AttributeDimensionTypeType
    Values: List[str]

class AttributeDimensionTypeDef(TypedDict):
    DimensionType: AttributeDimensionTypeType
    Values: Sequence[str]

class AttributeTypesSelectorOutputTypeDef(TypedDict):
    AttributeMatchingModel: AttributeMatchingModelType
    Address: NotRequired[List[str]]
    PhoneNumber: NotRequired[List[str]]
    EmailAddress: NotRequired[List[str]]

class AttributeTypesSelectorTypeDef(TypedDict):
    AttributeMatchingModel: AttributeMatchingModelType
    Address: NotRequired[Sequence[str]]
    PhoneNumber: NotRequired[Sequence[str]]
    EmailAddress: NotRequired[Sequence[str]]

class AttributeValueItemTypeDef(TypedDict):
    Value: NotRequired[str]

class ConflictResolutionTypeDef(TypedDict):
    ConflictResolvingModel: ConflictResolvingModelType
    SourceName: NotRequired[str]

class ConsolidationOutputTypeDef(TypedDict):
    MatchingAttributesList: List[List[str]]

class BatchGetCalculatedAttributeForProfileErrorTypeDef(TypedDict):
    Code: str
    Message: str
    ProfileId: str

class CalculatedAttributeValueTypeDef(TypedDict):
    CalculatedAttributeName: NotRequired[str]
    DisplayName: NotRequired[str]
    IsDataPartial: NotRequired[str]
    ProfileId: NotRequired[str]
    Value: NotRequired[str]
    LastObjectTimestamp: NotRequired[datetime]

class BatchGetProfileErrorTypeDef(TypedDict):
    Code: str
    Message: str
    ProfileId: str

class BatchGetProfileRequestTypeDef(TypedDict):
    DomainName: str
    ProfileIds: Sequence[str]

TimestampTypeDef = Union[datetime, str]
CatalogItemTypeDef = TypedDict(
    "CatalogItemTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Code": NotRequired[str],
        "Type": NotRequired[str],
        "Category": NotRequired[str],
        "Description": NotRequired[str],
        "AdditionalInformation": NotRequired[str],
        "ImageLink": NotRequired[str],
        "Link": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
        "Price": NotRequired[str],
        "Attributes": NotRequired[Dict[str, str]],
    },
)

class RangeOverrideTypeDef(TypedDict):
    Start: int
    Unit: Literal["DAYS"]
    End: NotRequired[int]

class ThresholdTypeDef(TypedDict):
    Value: str
    Operator: OperatorType

class ConnectorOperatorTypeDef(TypedDict):
    Marketo: NotRequired[MarketoConnectorOperatorType]
    S3: NotRequired[S3ConnectorOperatorType]
    Salesforce: NotRequired[SalesforceConnectorOperatorType]
    ServiceNow: NotRequired[ServiceNowConnectorOperatorType]
    Zendesk: NotRequired[ZendeskConnectorOperatorType]

class ConsolidationTypeDef(TypedDict):
    MatchingAttributesList: Sequence[Sequence[str]]

class ContactPreferenceTypeDef(TypedDict):
    KeyName: NotRequired[str]
    KeyValue: NotRequired[str]
    ProfileId: NotRequired[str]
    ContactType: NotRequired[ContactTypeType]

class ReadinessTypeDef(TypedDict):
    ProgressPercentage: NotRequired[int]
    Message: NotRequired[str]

class CreateDomainLayoutRequestTypeDef(TypedDict):
    DomainName: str
    LayoutDefinitionName: str
    Description: str
    DisplayName: str
    LayoutType: Literal["PROFILE_EXPLORER"]
    Layout: str
    IsDefault: NotRequired[bool]
    Tags: NotRequired[Mapping[str, str]]

class DataStoreRequestTypeDef(TypedDict):
    Enabled: NotRequired[bool]

class CreateEventStreamRequestTypeDef(TypedDict):
    DomainName: str
    Uri: str
    EventStreamName: str
    Tags: NotRequired[Mapping[str, str]]

class CreateSegmentSnapshotRequestTypeDef(TypedDict):
    DomainName: str
    SegmentDefinitionName: str
    DataFormat: DataFormatType
    EncryptionKey: NotRequired[str]
    RoleArn: NotRequired[str]
    DestinationUri: NotRequired[str]

class ObjectTypeFieldTypeDef(TypedDict):
    Source: NotRequired[str]
    Target: NotRequired[str]
    ContentType: NotRequired[FieldContentTypeType]

class DateDimensionOutputTypeDef(TypedDict):
    DimensionType: DateDimensionTypeType
    Values: List[str]

class DateDimensionTypeDef(TypedDict):
    DimensionType: DateDimensionTypeType
    Values: Sequence[str]

class DeleteCalculatedAttributeDefinitionRequestTypeDef(TypedDict):
    DomainName: str
    CalculatedAttributeName: str

class DeleteDomainLayoutRequestTypeDef(TypedDict):
    DomainName: str
    LayoutDefinitionName: str

class DeleteDomainObjectTypeRequestTypeDef(TypedDict):
    DomainName: str
    ObjectTypeName: str

class DeleteDomainRequestTypeDef(TypedDict):
    DomainName: str

class DeleteEventStreamRequestTypeDef(TypedDict):
    DomainName: str
    EventStreamName: str

class DeleteEventTriggerRequestTypeDef(TypedDict):
    DomainName: str
    EventTriggerName: str

class DeleteIntegrationRequestTypeDef(TypedDict):
    DomainName: str
    Uri: str

class DeleteProfileKeyRequestTypeDef(TypedDict):
    ProfileId: str
    KeyName: str
    Values: Sequence[str]
    DomainName: str

class DeleteProfileObjectRequestTypeDef(TypedDict):
    ProfileId: str
    ProfileObjectUniqueKey: str
    ObjectTypeName: str
    DomainName: str

class DeleteProfileObjectTypeRequestTypeDef(TypedDict):
    DomainName: str
    ObjectTypeName: str

class DeleteProfileRequestTypeDef(TypedDict):
    ProfileId: str
    DomainName: str

class DeleteRecommenderRequestTypeDef(TypedDict):
    DomainName: str
    RecommenderName: str

class DeleteSegmentDefinitionRequestTypeDef(TypedDict):
    DomainName: str
    SegmentDefinitionName: str

class DeleteWorkflowRequestTypeDef(TypedDict):
    DomainName: str
    WorkflowId: str

class DestinationSummaryTypeDef(TypedDict):
    Uri: str
    Status: EventStreamDestinationStatusType
    UnhealthySince: NotRequired[datetime]

class DetectProfileObjectTypeRequestTypeDef(TypedDict):
    Objects: Sequence[str]
    DomainName: str

class ObjectTypeKeyOutputTypeDef(TypedDict):
    StandardIdentifiers: NotRequired[List[StandardIdentifierType]]
    FieldNames: NotRequired[List[str]]

class DomainObjectTypeFieldTypeDef(TypedDict):
    Source: str
    Target: str
    ContentType: NotRequired[ContentTypeType]
    FeatureType: NotRequired[FeatureTypeType]

class DomainObjectTypesListItemTypeDef(TypedDict):
    ObjectTypeName: str
    Description: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    LastUpdatedAt: NotRequired[datetime]
    Tags: NotRequired[Dict[str, str]]

class DomainStatsTypeDef(TypedDict):
    ProfileCount: NotRequired[int]
    MeteringProfileCount: NotRequired[int]
    ObjectCount: NotRequired[int]
    TotalSize: NotRequired[int]

class EventParametersTypeDef(TypedDict):
    EventType: str
    EventValueThreshold: NotRequired[float]

class EventStreamDestinationDetailsTypeDef(TypedDict):
    Uri: str
    Status: EventStreamDestinationStatusType
    UnhealthySince: NotRequired[datetime]
    Message: NotRequired[str]

class ObjectAttributeOutputTypeDef(TypedDict):
    ComparisonOperator: ComparisonOperatorType
    Values: List[str]
    Source: NotRequired[str]
    FieldName: NotRequired[str]

class PeriodTypeDef(TypedDict):
    Unit: PeriodUnitType
    Value: int
    MaxInvocationsPerProfile: NotRequired[int]
    Unlimited: NotRequired[bool]

class EventTriggerSummaryItemTypeDef(TypedDict):
    ObjectTypeName: NotRequired[str]
    EventTriggerName: NotRequired[str]
    Description: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    LastUpdatedAt: NotRequired[datetime]
    Tags: NotRequired[Dict[str, str]]

class S3ExportingConfigTypeDef(TypedDict):
    S3BucketName: str
    S3KeyName: NotRequired[str]

class S3ExportingLocationTypeDef(TypedDict):
    S3BucketName: NotRequired[str]
    S3KeyName: NotRequired[str]

class ExtraLengthValueProfileDimensionOutputTypeDef(TypedDict):
    DimensionType: StringDimensionTypeType
    Values: List[str]

class ExtraLengthValueProfileDimensionTypeDef(TypedDict):
    DimensionType: StringDimensionTypeType
    Values: Sequence[str]

class FieldSourceProfileIdsTypeDef(TypedDict):
    AccountNumber: NotRequired[str]
    AdditionalInformation: NotRequired[str]
    PartyType: NotRequired[str]
    BusinessName: NotRequired[str]
    FirstName: NotRequired[str]
    MiddleName: NotRequired[str]
    LastName: NotRequired[str]
    BirthDate: NotRequired[str]
    Gender: NotRequired[str]
    PhoneNumber: NotRequired[str]
    MobilePhoneNumber: NotRequired[str]
    HomePhoneNumber: NotRequired[str]
    BusinessPhoneNumber: NotRequired[str]
    EmailAddress: NotRequired[str]
    PersonalEmailAddress: NotRequired[str]
    BusinessEmailAddress: NotRequired[str]
    Address: NotRequired[str]
    ShippingAddress: NotRequired[str]
    MailingAddress: NotRequired[str]
    BillingAddress: NotRequired[str]
    Attributes: NotRequired[Mapping[str, str]]
    ProfileType: NotRequired[str]
    EngagementPreferences: NotRequired[str]

class FilterAttributeDimensionOutputTypeDef(TypedDict):
    DimensionType: FilterDimensionTypeType
    Values: List[str]

class FilterAttributeDimensionTypeDef(TypedDict):
    DimensionType: FilterDimensionTypeType
    Values: Sequence[str]

class FoundByKeyValueTypeDef(TypedDict):
    KeyName: NotRequired[str]
    Values: NotRequired[List[str]]

class GetCalculatedAttributeDefinitionRequestTypeDef(TypedDict):
    DomainName: str
    CalculatedAttributeName: str

class GetCalculatedAttributeForProfileRequestTypeDef(TypedDict):
    DomainName: str
    ProfileId: str
    CalculatedAttributeName: str

class GetDomainLayoutRequestTypeDef(TypedDict):
    DomainName: str
    LayoutDefinitionName: str

class GetDomainObjectTypeRequestTypeDef(TypedDict):
    DomainName: str
    ObjectTypeName: str

class GetDomainRequestTypeDef(TypedDict):
    DomainName: str

class GetEventStreamRequestTypeDef(TypedDict):
    DomainName: str
    EventStreamName: str

class GetEventTriggerRequestTypeDef(TypedDict):
    DomainName: str
    EventTriggerName: str

class GetIdentityResolutionJobRequestTypeDef(TypedDict):
    DomainName: str
    JobId: str

class JobStatsTypeDef(TypedDict):
    NumberOfProfilesReviewed: NotRequired[int]
    NumberOfMatchesFound: NotRequired[int]
    NumberOfMergesDone: NotRequired[int]

class GetIntegrationRequestTypeDef(TypedDict):
    DomainName: str
    Uri: str

class GetMatchesRequestTypeDef(TypedDict):
    DomainName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class MatchItemTypeDef(TypedDict):
    MatchId: NotRequired[str]
    ProfileIds: NotRequired[List[str]]
    ConfidenceScore: NotRequired[float]

class GetObjectTypeAttributeStatisticsPercentilesTypeDef(TypedDict):
    P5: float
    P25: float
    P50: float
    P75: float
    P95: float

class GetObjectTypeAttributeStatisticsRequestTypeDef(TypedDict):
    DomainName: str
    ObjectTypeName: str
    AttributeName: str

class GetProfileHistoryRecordRequestTypeDef(TypedDict):
    DomainName: str
    ProfileId: str
    Id: str

class GetProfileObjectTypeRequestTypeDef(TypedDict):
    DomainName: str
    ObjectTypeName: str

class GetProfileObjectTypeTemplateRequestTypeDef(TypedDict):
    TemplateId: str

class GetProfileRecommendationsRequestTypeDef(TypedDict):
    DomainName: str
    ProfileId: str
    RecommenderName: str
    Context: NotRequired[Mapping[str, str]]
    MaxResults: NotRequired[int]

class GetRecommenderRequestTypeDef(TypedDict):
    DomainName: str
    RecommenderName: str
    TrainingMetricsCount: NotRequired[int]

class TrainingMetricsTypeDef(TypedDict):
    Time: NotRequired[datetime]
    Metrics: NotRequired[Dict[TrainingMetricNameType, float]]

class GetSegmentDefinitionRequestTypeDef(TypedDict):
    DomainName: str
    SegmentDefinitionName: str

class GetSegmentEstimateRequestTypeDef(TypedDict):
    DomainName: str
    EstimateId: str

class GetSegmentMembershipRequestTypeDef(TypedDict):
    DomainName: str
    SegmentDefinitionName: str
    ProfileIds: Sequence[str]

class ProfileQueryFailuresTypeDef(TypedDict):
    ProfileId: str
    Message: str
    Status: NotRequired[int]

class GetSegmentSnapshotRequestTypeDef(TypedDict):
    DomainName: str
    SegmentDefinitionName: str
    SnapshotId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetSimilarProfilesRequestTypeDef(TypedDict):
    DomainName: str
    MatchType: MatchTypeType
    SearchKey: str
    SearchValue: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class GetUploadJobPathRequestTypeDef(TypedDict):
    DomainName: str
    JobId: str

class GetUploadJobRequestTypeDef(TypedDict):
    DomainName: str
    JobId: str

class ResultsSummaryTypeDef(TypedDict):
    UpdatedRecords: NotRequired[int]
    CreatedRecords: NotRequired[int]
    FailedRecords: NotRequired[int]

class GetWorkflowRequestTypeDef(TypedDict):
    DomainName: str
    WorkflowId: str

class GetWorkflowStepsRequestTypeDef(TypedDict):
    DomainName: str
    WorkflowId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class SourceSegmentTypeDef(TypedDict):
    SegmentDefinitionName: NotRequired[str]

class IncrementalPullConfigTypeDef(TypedDict):
    DatetimeTypeFieldName: NotRequired[str]

class JobScheduleTypeDef(TypedDict):
    DayOfTheWeek: JobScheduleDayOfTheWeekType
    Time: str

class LayoutItemTypeDef(TypedDict):
    LayoutDefinitionName: str
    Description: str
    DisplayName: str
    LayoutType: Literal["PROFILE_EXPLORER"]
    CreatedAt: datetime
    LastUpdatedAt: datetime
    IsDefault: NotRequired[bool]
    Tags: NotRequired[Dict[str, str]]

class ListAccountIntegrationsRequestTypeDef(TypedDict):
    Uri: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    IncludeHidden: NotRequired[bool]

class ListIntegrationItemTypeDef(TypedDict):
    DomainName: str
    Uri: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    ObjectTypeName: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]
    ObjectTypeNames: NotRequired[Dict[str, str]]
    WorkflowId: NotRequired[str]
    IsUnstructured: NotRequired[bool]
    RoleArn: NotRequired[str]
    EventTriggerNames: NotRequired[List[str]]
    Scope: NotRequired[ScopeType]

class ListCalculatedAttributeDefinitionItemTypeDef(TypedDict):
    CalculatedAttributeName: NotRequired[str]
    DisplayName: NotRequired[str]
    Description: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    LastUpdatedAt: NotRequired[datetime]
    UseHistoricalData: NotRequired[bool]
    Status: NotRequired[ReadinessStatusType]
    Tags: NotRequired[Dict[str, str]]

class ListCalculatedAttributeDefinitionsRequestTypeDef(TypedDict):
    DomainName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListCalculatedAttributeForProfileItemTypeDef(TypedDict):
    CalculatedAttributeName: NotRequired[str]
    DisplayName: NotRequired[str]
    IsDataPartial: NotRequired[str]
    Value: NotRequired[str]
    LastObjectTimestamp: NotRequired[datetime]

class ListCalculatedAttributesForProfileRequestTypeDef(TypedDict):
    DomainName: str
    ProfileId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListDomainItemTypeDef(TypedDict):
    DomainName: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: NotRequired[Dict[str, str]]

class ListDomainLayoutsRequestTypeDef(TypedDict):
    DomainName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListDomainObjectTypesRequestTypeDef(TypedDict):
    DomainName: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListDomainsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListEventStreamsRequestTypeDef(TypedDict):
    DomainName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListEventTriggersRequestTypeDef(TypedDict):
    DomainName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListIdentityResolutionJobsRequestTypeDef(TypedDict):
    DomainName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListIntegrationsRequestTypeDef(TypedDict):
    DomainName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    IncludeHidden: NotRequired[bool]

class ListObjectTypeAttributeItemTypeDef(TypedDict):
    AttributeName: str
    LastUpdatedAt: datetime

class ListObjectTypeAttributeValuesItemTypeDef(TypedDict):
    Value: str
    LastUpdatedAt: datetime

class ListObjectTypeAttributeValuesRequestTypeDef(TypedDict):
    DomainName: str
    ObjectTypeName: str
    AttributeName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListObjectTypeAttributesRequestTypeDef(TypedDict):
    DomainName: str
    ObjectTypeName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListProfileHistoryRecordsRequestTypeDef(TypedDict):
    DomainName: str
    ProfileId: str
    ObjectTypeName: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ActionType: NotRequired[ActionTypeType]
    PerformedBy: NotRequired[str]

class ProfileHistoryRecordTypeDef(TypedDict):
    Id: str
    ObjectTypeName: str
    CreatedAt: datetime
    ActionType: ActionTypeType
    LastUpdatedAt: NotRequired[datetime]
    ProfileObjectUniqueKey: NotRequired[str]
    PerformedBy: NotRequired[str]

class ListProfileObjectTypeItemTypeDef(TypedDict):
    ObjectTypeName: str
    Description: str
    CreatedAt: NotRequired[datetime]
    LastUpdatedAt: NotRequired[datetime]
    MaxProfileObjectCount: NotRequired[int]
    MaxAvailableProfileObjectCount: NotRequired[int]
    Tags: NotRequired[Dict[str, str]]

class ListProfileObjectTypeTemplateItemTypeDef(TypedDict):
    TemplateId: NotRequired[str]
    SourceName: NotRequired[str]
    SourceObject: NotRequired[str]

class ListProfileObjectTypeTemplatesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListProfileObjectTypesRequestTypeDef(TypedDict):
    DomainName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListProfileObjectsItemTypeDef(TypedDict):
    ObjectTypeName: NotRequired[str]
    ProfileObjectUniqueKey: NotRequired[str]
    Object: NotRequired[str]

class ObjectFilterTypeDef(TypedDict):
    KeyName: str
    Values: Sequence[str]

class ListRecommenderRecipesRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class RecommenderRecipeTypeDef(TypedDict):
    name: NotRequired[RecommenderRecipeNameType]
    description: NotRequired[str]

class ListRecommendersRequestTypeDef(TypedDict):
    DomainName: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListRuleBasedMatchesRequestTypeDef(TypedDict):
    DomainName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListSegmentDefinitionsRequestTypeDef(TypedDict):
    DomainName: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class SegmentDefinitionItemTypeDef(TypedDict):
    SegmentDefinitionName: NotRequired[str]
    DisplayName: NotRequired[str]
    Description: NotRequired[str]
    SegmentDefinitionArn: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    Tags: NotRequired[Dict[str, str]]
    SegmentType: NotRequired[SegmentTypeType]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ListUploadJobsRequestTypeDef(TypedDict):
    DomainName: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class UploadJobItemTypeDef(TypedDict):
    JobId: NotRequired[str]
    DisplayName: NotRequired[str]
    Status: NotRequired[UploadJobStatusType]
    StatusReason: NotRequired[StatusReasonType]
    CreatedAt: NotRequired[datetime]
    CompletedAt: NotRequired[datetime]
    DataExpiry: NotRequired[int]

class ListWorkflowsItemTypeDef(TypedDict):
    WorkflowType: Literal["APPFLOW_INTEGRATION"]
    WorkflowId: str
    Status: StatusType
    StatusDescription: str
    CreatedAt: datetime
    LastUpdatedAt: datetime

class MarketoSourcePropertiesTypeDef(TypedDict):
    Object: str

class MatchingRuleOutputTypeDef(TypedDict):
    Rule: List[str]

class MatchingRuleTypeDef(TypedDict):
    Rule: Sequence[str]

class ObjectAttributeTypeDef(TypedDict):
    ComparisonOperator: ComparisonOperatorType
    Values: Sequence[str]
    Source: NotRequired[str]
    FieldName: NotRequired[str]

class ObjectTypeKeyTypeDef(TypedDict):
    StandardIdentifiers: NotRequired[Sequence[StandardIdentifierType]]
    FieldNames: NotRequired[Sequence[str]]

class ProfileAttributeValuesRequestTypeDef(TypedDict):
    DomainName: str
    AttributeName: str

class ProfileTypeDimensionOutputTypeDef(TypedDict):
    DimensionType: ProfileTypeDimensionTypeType
    Values: List[ProfileTypeType]

class ProfileDimensionTypeDef(TypedDict):
    DimensionType: StringDimensionTypeType
    Values: Sequence[str]

class ProfileTypeDimensionTypeDef(TypedDict):
    DimensionType: ProfileTypeDimensionTypeType
    Values: Sequence[ProfileTypeType]

class PutProfileObjectRequestTypeDef(TypedDict):
    ObjectTypeName: str
    Object: str
    DomainName: str

class ValueRangeTypeDef(TypedDict):
    Start: int
    End: int

class S3SourcePropertiesTypeDef(TypedDict):
    BucketName: str
    BucketPrefix: NotRequired[str]

class SalesforceSourcePropertiesTypeDef(TypedDict):
    Object: str
    EnableDynamicFieldUpdate: NotRequired[bool]
    IncludeDeletedRecords: NotRequired[bool]

class ServiceNowSourcePropertiesTypeDef(TypedDict):
    Object: str

class ZendeskSourcePropertiesTypeDef(TypedDict):
    Object: str

class StartRecommenderRequestTypeDef(TypedDict):
    DomainName: str
    RecommenderName: str

class StartUploadJobRequestTypeDef(TypedDict):
    DomainName: str
    JobId: str

class StopRecommenderRequestTypeDef(TypedDict):
    DomainName: str
    RecommenderName: str

class StopUploadJobRequestTypeDef(TypedDict):
    DomainName: str
    JobId: str

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAddressTypeDef(TypedDict):
    Address1: NotRequired[str]
    Address2: NotRequired[str]
    Address3: NotRequired[str]
    Address4: NotRequired[str]
    City: NotRequired[str]
    County: NotRequired[str]
    State: NotRequired[str]
    Province: NotRequired[str]
    Country: NotRequired[str]
    PostalCode: NotRequired[str]

class UpdateDomainLayoutRequestTypeDef(TypedDict):
    DomainName: str
    LayoutDefinitionName: str
    Description: NotRequired[str]
    DisplayName: NotRequired[str]
    IsDefault: NotRequired[bool]
    LayoutType: NotRequired[Literal["PROFILE_EXPLORER"]]
    Layout: NotRequired[str]

class AddProfileKeyResponseTypeDef(TypedDict):
    KeyName: str
    Values: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainLayoutResponseTypeDef(TypedDict):
    LayoutDefinitionName: str
    Description: str
    DisplayName: str
    IsDefault: bool
    LayoutType: Literal["PROFILE_EXPLORER"]
    Layout: str
    Version: str
    Tags: Dict[str, str]
    CreatedAt: datetime
    LastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventStreamResponseTypeDef(TypedDict):
    EventStreamArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIntegrationWorkflowResponseTypeDef(TypedDict):
    WorkflowId: str
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProfileResponseTypeDef(TypedDict):
    ProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRecommenderResponseTypeDef(TypedDict):
    RecommenderArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSegmentDefinitionResponseTypeDef(TypedDict):
    SegmentDefinitionName: str
    DisplayName: str
    Description: str
    CreatedAt: datetime
    SegmentDefinitionArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSegmentEstimateResponseTypeDef(TypedDict):
    DomainName: str
    EstimateId: str
    StatusCode: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSegmentSnapshotResponseTypeDef(TypedDict):
    SnapshotId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUploadJobResponseTypeDef(TypedDict):
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDomainLayoutResponseTypeDef(TypedDict):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDomainResponseTypeDef(TypedDict):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEventTriggerResponseTypeDef(TypedDict):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIntegrationResponseTypeDef(TypedDict):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProfileKeyResponseTypeDef(TypedDict):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProfileObjectResponseTypeDef(TypedDict):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProfileObjectTypeResponseTypeDef(TypedDict):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProfileResponseTypeDef(TypedDict):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSegmentDefinitionResponseTypeDef(TypedDict):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAutoMergingPreviewResponseTypeDef(TypedDict):
    DomainName: str
    NumberOfMatchesInSample: int
    NumberOfProfilesInSample: int
    NumberOfProfilesWillBeMerged: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetCalculatedAttributeForProfileResponseTypeDef(TypedDict):
    CalculatedAttributeName: str
    DisplayName: str
    IsDataPartial: str
    Value: str
    LastObjectTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainLayoutResponseTypeDef(TypedDict):
    LayoutDefinitionName: str
    Description: str
    DisplayName: str
    IsDefault: bool
    LayoutType: Literal["PROFILE_EXPLORER"]
    Layout: str
    Version: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetIntegrationResponseTypeDef(TypedDict):
    DomainName: str
    Uri: str
    ObjectTypeName: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ObjectTypeNames: Dict[str, str]
    WorkflowId: str
    IsUnstructured: bool
    RoleArn: str
    EventTriggerNames: List[str]
    Scope: ScopeType
    ResponseMetadata: ResponseMetadataTypeDef

class GetProfileHistoryRecordResponseTypeDef(TypedDict):
    Id: str
    ObjectTypeName: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    ActionType: ActionTypeType
    ProfileObjectUniqueKey: str
    Content: str
    PerformedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSegmentEstimateResponseTypeDef(TypedDict):
    DomainName: str
    EstimateId: str
    Status: EstimateStatusType
    Estimate: str
    Message: str
    StatusCode: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetSegmentSnapshotResponseTypeDef(TypedDict):
    SnapshotId: str
    Status: SegmentSnapshotStatusType
    StatusMessage: str
    DataFormat: DataFormatType
    EncryptionKey: str
    RoleArn: str
    DestinationUri: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSimilarProfilesResponseTypeDef(TypedDict):
    ProfileIds: List[str]
    MatchId: str
    MatchType: MatchTypeType
    RuleLevel: int
    ConfidenceScore: float
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetUploadJobPathResponseTypeDef(TypedDict):
    Url: str
    ClientToken: str
    ValidUntil: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListRuleBasedMatchesResponseTypeDef(TypedDict):
    MatchIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class MergeProfilesResponseTypeDef(TypedDict):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutIntegrationResponseTypeDef(TypedDict):
    DomainName: str
    Uri: str
    ObjectTypeName: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ObjectTypeNames: Dict[str, str]
    WorkflowId: str
    IsUnstructured: bool
    RoleArn: str
    EventTriggerNames: List[str]
    Scope: ScopeType
    ResponseMetadata: ResponseMetadataTypeDef

class PutProfileObjectResponseTypeDef(TypedDict):
    ProfileObjectUniqueKey: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainLayoutResponseTypeDef(TypedDict):
    LayoutDefinitionName: str
    Description: str
    DisplayName: str
    IsDefault: bool
    LayoutType: Literal["PROFILE_EXPLORER"]
    Layout: str
    Version: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProfileResponseTypeDef(TypedDict):
    ProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRecommenderResponseTypeDef(TypedDict):
    RecommenderName: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchProfilesRequestTypeDef(TypedDict):
    DomainName: str
    KeyName: str
    Values: Sequence[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    AdditionalSearchKeys: NotRequired[Sequence[AdditionalSearchKeyTypeDef]]
    LogicalOperator: NotRequired[LogicalOperatorType]

class AddressDimensionOutputTypeDef(TypedDict):
    City: NotRequired[ProfileDimensionOutputTypeDef]
    Country: NotRequired[ProfileDimensionOutputTypeDef]
    County: NotRequired[ProfileDimensionOutputTypeDef]
    PostalCode: NotRequired[ProfileDimensionOutputTypeDef]
    Province: NotRequired[ProfileDimensionOutputTypeDef]
    State: NotRequired[ProfileDimensionOutputTypeDef]

class WorkflowAttributesTypeDef(TypedDict):
    AppflowIntegration: NotRequired[AppflowIntegrationWorkflowAttributesTypeDef]

class WorkflowMetricsTypeDef(TypedDict):
    AppflowIntegration: NotRequired[AppflowIntegrationWorkflowMetricsTypeDef]

class WorkflowStepItemTypeDef(TypedDict):
    AppflowIntegration: NotRequired[AppflowIntegrationWorkflowStepTypeDef]

class AttributeDetailsOutputTypeDef(TypedDict):
    Attributes: List[AttributeItemTypeDef]
    Expression: str

class AttributeDetailsTypeDef(TypedDict):
    Attributes: Sequence[AttributeItemTypeDef]
    Expression: str

AttributeDimensionUnionTypeDef = Union[AttributeDimensionTypeDef, AttributeDimensionOutputTypeDef]
AttributeTypesSelectorUnionTypeDef = Union[
    AttributeTypesSelectorTypeDef, AttributeTypesSelectorOutputTypeDef
]

class ProfileAttributeValuesResponseTypeDef(TypedDict):
    DomainName: str
    AttributeName: str
    Items: List[AttributeValueItemTypeDef]
    StatusCode: int
    ResponseMetadata: ResponseMetadataTypeDef

class AutoMergingOutputTypeDef(TypedDict):
    Enabled: bool
    Consolidation: NotRequired[ConsolidationOutputTypeDef]
    ConflictResolution: NotRequired[ConflictResolutionTypeDef]
    MinAllowedConfidenceScoreForMerging: NotRequired[float]

class BatchTypeDef(TypedDict):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef

class ListWorkflowsRequestTypeDef(TypedDict):
    DomainName: str
    WorkflowType: NotRequired[Literal["APPFLOW_INTEGRATION"]]
    Status: NotRequired[StatusType]
    QueryStartDate: NotRequired[TimestampTypeDef]
    QueryEndDate: NotRequired[TimestampTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ScheduledTriggerPropertiesTypeDef(TypedDict):
    ScheduleExpression: str
    DataPullMode: NotRequired[DataPullModeType]
    ScheduleStartTime: NotRequired[TimestampTypeDef]
    ScheduleEndTime: NotRequired[TimestampTypeDef]
    Timezone: NotRequired[str]
    ScheduleOffset: NotRequired[int]
    FirstExecutionFrom: NotRequired[TimestampTypeDef]

class RecommendationTypeDef(TypedDict):
    CatalogItem: NotRequired[CatalogItemTypeDef]
    Score: NotRequired[float]

class ConditionOverridesTypeDef(TypedDict):
    Range: NotRequired[RangeOverrideTypeDef]

class TaskTypeDef(TypedDict):
    SourceFields: Sequence[str]
    TaskType: TaskTypeType
    ConnectorOperator: NotRequired[ConnectorOperatorTypeDef]
    DestinationField: NotRequired[str]
    TaskProperties: NotRequired[Mapping[OperatorPropertiesKeysType, str]]

ConsolidationUnionTypeDef = Union[ConsolidationTypeDef, ConsolidationOutputTypeDef]

class EngagementPreferencesOutputTypeDef(TypedDict):
    Phone: NotRequired[List[ContactPreferenceTypeDef]]
    Email: NotRequired[List[ContactPreferenceTypeDef]]

class EngagementPreferencesTypeDef(TypedDict):
    Phone: NotRequired[Sequence[ContactPreferenceTypeDef]]
    Email: NotRequired[Sequence[ContactPreferenceTypeDef]]

class DataStoreResponseTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    Readiness: NotRequired[ReadinessTypeDef]

class CreateUploadJobRequestTypeDef(TypedDict):
    DomainName: str
    DisplayName: str
    Fields: Mapping[str, ObjectTypeFieldTypeDef]
    UniqueKey: str
    DataExpiry: NotRequired[int]

DateDimensionUnionTypeDef = Union[DateDimensionTypeDef, DateDimensionOutputTypeDef]

class EventStreamSummaryTypeDef(TypedDict):
    DomainName: str
    EventStreamName: str
    EventStreamArn: str
    State: EventStreamStateType
    StoppedSince: NotRequired[datetime]
    DestinationSummary: NotRequired[DestinationSummaryTypeDef]
    Tags: NotRequired[Dict[str, str]]

class DetectedProfileObjectTypeTypeDef(TypedDict):
    SourceLastUpdatedTimestampFormat: NotRequired[str]
    Fields: NotRequired[Dict[str, ObjectTypeFieldTypeDef]]
    Keys: NotRequired[Dict[str, List[ObjectTypeKeyOutputTypeDef]]]

class GetProfileObjectTypeResponseTypeDef(TypedDict):
    ObjectTypeName: str
    Description: str
    TemplateId: str
    ExpirationDays: int
    EncryptionKey: str
    AllowProfileCreation: bool
    SourceLastUpdatedTimestampFormat: str
    MaxAvailableProfileObjectCount: int
    MaxProfileObjectCount: int
    Fields: Dict[str, ObjectTypeFieldTypeDef]
    Keys: Dict[str, List[ObjectTypeKeyOutputTypeDef]]
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetProfileObjectTypeTemplateResponseTypeDef(TypedDict):
    TemplateId: str
    SourceName: str
    SourceObject: str
    AllowProfileCreation: bool
    SourceLastUpdatedTimestampFormat: str
    Fields: Dict[str, ObjectTypeFieldTypeDef]
    Keys: Dict[str, List[ObjectTypeKeyOutputTypeDef]]
    ResponseMetadata: ResponseMetadataTypeDef

class PutProfileObjectTypeResponseTypeDef(TypedDict):
    ObjectTypeName: str
    Description: str
    TemplateId: str
    ExpirationDays: int
    EncryptionKey: str
    AllowProfileCreation: bool
    SourceLastUpdatedTimestampFormat: str
    MaxProfileObjectCount: int
    MaxAvailableProfileObjectCount: int
    Fields: Dict[str, ObjectTypeFieldTypeDef]
    Keys: Dict[str, List[ObjectTypeKeyOutputTypeDef]]
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainObjectTypeResponseTypeDef(TypedDict):
    ObjectTypeName: str
    Description: str
    EncryptionKey: str
    Fields: Dict[str, DomainObjectTypeFieldTypeDef]
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutDomainObjectTypeRequestTypeDef(TypedDict):
    DomainName: str
    ObjectTypeName: str
    Fields: Mapping[str, DomainObjectTypeFieldTypeDef]
    Description: NotRequired[str]
    EncryptionKey: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class PutDomainObjectTypeResponseTypeDef(TypedDict):
    ObjectTypeName: str
    Description: str
    EncryptionKey: str
    Fields: Dict[str, DomainObjectTypeFieldTypeDef]
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainObjectTypesResponseTypeDef(TypedDict):
    Items: List[DomainObjectTypesListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class EventsConfigOutputTypeDef(TypedDict):
    EventParametersList: List[EventParametersTypeDef]

class EventsConfigTypeDef(TypedDict):
    EventParametersList: Sequence[EventParametersTypeDef]

class GetEventStreamResponseTypeDef(TypedDict):
    DomainName: str
    EventStreamArn: str
    CreatedAt: datetime
    State: EventStreamStateType
    StoppedSince: datetime
    DestinationDetails: EventStreamDestinationDetailsTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class EventTriggerDimensionOutputTypeDef(TypedDict):
    ObjectAttributes: List[ObjectAttributeOutputTypeDef]

class EventTriggerLimitsOutputTypeDef(TypedDict):
    EventExpiration: NotRequired[int]
    Periods: NotRequired[List[PeriodTypeDef]]

class EventTriggerLimitsTypeDef(TypedDict):
    EventExpiration: NotRequired[int]
    Periods: NotRequired[Sequence[PeriodTypeDef]]

class ListEventTriggersResponseTypeDef(TypedDict):
    Items: List[EventTriggerSummaryItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ExportingConfigTypeDef(TypedDict):
    S3Exporting: NotRequired[S3ExportingConfigTypeDef]

class ExportingLocationTypeDef(TypedDict):
    S3Exporting: NotRequired[S3ExportingLocationTypeDef]

ExtraLengthValueProfileDimensionUnionTypeDef = Union[
    ExtraLengthValueProfileDimensionTypeDef, ExtraLengthValueProfileDimensionOutputTypeDef
]

class MergeProfilesRequestTypeDef(TypedDict):
    DomainName: str
    MainProfileId: str
    ProfileIdsToBeMerged: Sequence[str]
    FieldSourceProfileIds: NotRequired[FieldSourceProfileIdsTypeDef]

class FilterDimensionOutputTypeDef(TypedDict):
    Attributes: Dict[str, FilterAttributeDimensionOutputTypeDef]

class FilterDimensionTypeDef(TypedDict):
    Attributes: Mapping[str, FilterAttributeDimensionTypeDef]

class GetMatchesResponseTypeDef(TypedDict):
    MatchGenerationDate: datetime
    PotentialMatches: int
    Matches: List[MatchItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetObjectTypeAttributeStatisticsStatsTypeDef(TypedDict):
    Maximum: float
    Minimum: float
    Average: float
    StandardDeviation: float
    Percentiles: GetObjectTypeAttributeStatisticsPercentilesTypeDef

class GetSimilarProfilesRequestPaginateTypeDef(TypedDict):
    DomainName: str
    MatchType: MatchTypeType
    SearchKey: str
    SearchValue: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDomainLayoutsRequestPaginateTypeDef(TypedDict):
    DomainName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDomainObjectTypesRequestPaginateTypeDef(TypedDict):
    DomainName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEventStreamsRequestPaginateTypeDef(TypedDict):
    DomainName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEventTriggersRequestPaginateTypeDef(TypedDict):
    DomainName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListObjectTypeAttributesRequestPaginateTypeDef(TypedDict):
    DomainName: str
    ObjectTypeName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRecommenderRecipesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRecommendersRequestPaginateTypeDef(TypedDict):
    DomainName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRuleBasedMatchesRequestPaginateTypeDef(TypedDict):
    DomainName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSegmentDefinitionsRequestPaginateTypeDef(TypedDict):
    DomainName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListUploadJobsRequestPaginateTypeDef(TypedDict):
    DomainName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetUploadJobResponseTypeDef(TypedDict):
    JobId: str
    DisplayName: str
    Status: UploadJobStatusType
    StatusReason: StatusReasonType
    CreatedAt: datetime
    CompletedAt: datetime
    Fields: Dict[str, ObjectTypeFieldTypeDef]
    UniqueKey: str
    ResultsSummary: ResultsSummaryTypeDef
    DataExpiry: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainLayoutsResponseTypeDef(TypedDict):
    Items: List[LayoutItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListAccountIntegrationsResponseTypeDef(TypedDict):
    Items: List[ListIntegrationItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListIntegrationsResponseTypeDef(TypedDict):
    Items: List[ListIntegrationItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListCalculatedAttributeDefinitionsResponseTypeDef(TypedDict):
    Items: List[ListCalculatedAttributeDefinitionItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListCalculatedAttributesForProfileResponseTypeDef(TypedDict):
    Items: List[ListCalculatedAttributeForProfileItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDomainsResponseTypeDef(TypedDict):
    Items: List[ListDomainItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListObjectTypeAttributesResponseTypeDef(TypedDict):
    Items: List[ListObjectTypeAttributeItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListObjectTypeAttributeValuesResponseTypeDef(TypedDict):
    Items: List[ListObjectTypeAttributeValuesItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListProfileHistoryRecordsResponseTypeDef(TypedDict):
    ProfileHistoryRecords: List[ProfileHistoryRecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListProfileObjectTypesResponseTypeDef(TypedDict):
    Items: List[ListProfileObjectTypeItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListProfileObjectTypeTemplatesResponseTypeDef(TypedDict):
    Items: List[ListProfileObjectTypeTemplateItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListProfileObjectsResponseTypeDef(TypedDict):
    Items: List[ListProfileObjectsItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListProfileObjectsRequestTypeDef(TypedDict):
    DomainName: str
    ObjectTypeName: str
    ProfileId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ObjectFilter: NotRequired[ObjectFilterTypeDef]

class ListRecommenderRecipesResponseTypeDef(TypedDict):
    RecommenderRecipes: List[RecommenderRecipeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSegmentDefinitionsResponseTypeDef(TypedDict):
    Items: List[SegmentDefinitionItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListUploadJobsResponseTypeDef(TypedDict):
    Items: List[UploadJobItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListWorkflowsResponseTypeDef(TypedDict):
    Items: List[ListWorkflowsItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

MatchingRuleUnionTypeDef = Union[MatchingRuleTypeDef, MatchingRuleOutputTypeDef]
ObjectAttributeUnionTypeDef = Union[ObjectAttributeTypeDef, ObjectAttributeOutputTypeDef]
ObjectTypeKeyUnionTypeDef = Union[ObjectTypeKeyTypeDef, ObjectTypeKeyOutputTypeDef]
ProfileDimensionUnionTypeDef = Union[ProfileDimensionTypeDef, ProfileDimensionOutputTypeDef]
ProfileTypeDimensionUnionTypeDef = Union[
    ProfileTypeDimensionTypeDef, ProfileTypeDimensionOutputTypeDef
]

class RangeTypeDef(TypedDict):
    Value: NotRequired[int]
    Unit: NotRequired[Literal["DAYS"]]
    ValueRange: NotRequired[ValueRangeTypeDef]
    TimestampSource: NotRequired[str]
    TimestampFormat: NotRequired[str]

class SourceConnectorPropertiesTypeDef(TypedDict):
    Marketo: NotRequired[MarketoSourcePropertiesTypeDef]
    S3: NotRequired[S3SourcePropertiesTypeDef]
    Salesforce: NotRequired[SalesforceSourcePropertiesTypeDef]
    ServiceNow: NotRequired[ServiceNowSourcePropertiesTypeDef]
    Zendesk: NotRequired[ZendeskSourcePropertiesTypeDef]

class ProfileAttributesOutputTypeDef(TypedDict):
    AccountNumber: NotRequired[ProfileDimensionOutputTypeDef]
    AdditionalInformation: NotRequired[ExtraLengthValueProfileDimensionOutputTypeDef]
    FirstName: NotRequired[ProfileDimensionOutputTypeDef]
    LastName: NotRequired[ProfileDimensionOutputTypeDef]
    MiddleName: NotRequired[ProfileDimensionOutputTypeDef]
    GenderString: NotRequired[ProfileDimensionOutputTypeDef]
    PartyTypeString: NotRequired[ProfileDimensionOutputTypeDef]
    BirthDate: NotRequired[DateDimensionOutputTypeDef]
    PhoneNumber: NotRequired[ProfileDimensionOutputTypeDef]
    BusinessName: NotRequired[ProfileDimensionOutputTypeDef]
    BusinessPhoneNumber: NotRequired[ProfileDimensionOutputTypeDef]
    HomePhoneNumber: NotRequired[ProfileDimensionOutputTypeDef]
    MobilePhoneNumber: NotRequired[ProfileDimensionOutputTypeDef]
    EmailAddress: NotRequired[ProfileDimensionOutputTypeDef]
    PersonalEmailAddress: NotRequired[ProfileDimensionOutputTypeDef]
    BusinessEmailAddress: NotRequired[ProfileDimensionOutputTypeDef]
    Address: NotRequired[AddressDimensionOutputTypeDef]
    ShippingAddress: NotRequired[AddressDimensionOutputTypeDef]
    MailingAddress: NotRequired[AddressDimensionOutputTypeDef]
    BillingAddress: NotRequired[AddressDimensionOutputTypeDef]
    Attributes: NotRequired[Dict[str, AttributeDimensionOutputTypeDef]]
    ProfileType: NotRequired[ProfileTypeDimensionOutputTypeDef]

class GetWorkflowResponseTypeDef(TypedDict):
    WorkflowId: str
    WorkflowType: Literal["APPFLOW_INTEGRATION"]
    Status: StatusType
    ErrorDescription: str
    StartDate: datetime
    LastUpdatedAt: datetime
    Attributes: WorkflowAttributesTypeDef
    Metrics: WorkflowMetricsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkflowStepsResponseTypeDef(TypedDict):
    WorkflowId: str
    WorkflowType: Literal["APPFLOW_INTEGRATION"]
    Items: List[WorkflowStepItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

AttributeDetailsUnionTypeDef = Union[AttributeDetailsTypeDef, AttributeDetailsOutputTypeDef]

class TriggerPropertiesTypeDef(TypedDict):
    Scheduled: NotRequired[ScheduledTriggerPropertiesTypeDef]

class GetProfileRecommendationsResponseTypeDef(TypedDict):
    Recommendations: List[RecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetCalculatedAttributeForProfileRequestTypeDef(TypedDict):
    CalculatedAttributeName: str
    DomainName: str
    ProfileIds: Sequence[str]
    ConditionOverrides: NotRequired[ConditionOverridesTypeDef]

class BatchGetCalculatedAttributeForProfileResponseTypeDef(TypedDict):
    Errors: List[BatchGetCalculatedAttributeForProfileErrorTypeDef]
    CalculatedAttributeValues: List[CalculatedAttributeValueTypeDef]
    ConditionOverrides: ConditionOverridesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CalculatedAttributeDimensionOutputTypeDef(TypedDict):
    DimensionType: AttributeDimensionTypeType
    Values: List[str]
    ConditionOverrides: NotRequired[ConditionOverridesTypeDef]

class CalculatedAttributeDimensionTypeDef(TypedDict):
    DimensionType: AttributeDimensionTypeType
    Values: Sequence[str]
    ConditionOverrides: NotRequired[ConditionOverridesTypeDef]

class AutoMergingTypeDef(TypedDict):
    Enabled: bool
    Consolidation: NotRequired[ConsolidationUnionTypeDef]
    ConflictResolution: NotRequired[ConflictResolutionTypeDef]
    MinAllowedConfidenceScoreForMerging: NotRequired[float]

class GetAutoMergingPreviewRequestTypeDef(TypedDict):
    DomainName: str
    Consolidation: ConsolidationUnionTypeDef
    ConflictResolution: ConflictResolutionTypeDef
    MinAllowedConfidenceScoreForMerging: NotRequired[float]

class ProfileTypeDef(TypedDict):
    ProfileId: NotRequired[str]
    AccountNumber: NotRequired[str]
    AdditionalInformation: NotRequired[str]
    PartyType: NotRequired[PartyTypeType]
    BusinessName: NotRequired[str]
    FirstName: NotRequired[str]
    MiddleName: NotRequired[str]
    LastName: NotRequired[str]
    BirthDate: NotRequired[str]
    Gender: NotRequired[GenderType]
    PhoneNumber: NotRequired[str]
    MobilePhoneNumber: NotRequired[str]
    HomePhoneNumber: NotRequired[str]
    BusinessPhoneNumber: NotRequired[str]
    EmailAddress: NotRequired[str]
    PersonalEmailAddress: NotRequired[str]
    BusinessEmailAddress: NotRequired[str]
    Address: NotRequired[AddressTypeDef]
    ShippingAddress: NotRequired[AddressTypeDef]
    MailingAddress: NotRequired[AddressTypeDef]
    BillingAddress: NotRequired[AddressTypeDef]
    Attributes: NotRequired[Dict[str, str]]
    FoundByItems: NotRequired[List[FoundByKeyValueTypeDef]]
    PartyTypeString: NotRequired[str]
    GenderString: NotRequired[str]
    ProfileType: NotRequired[ProfileTypeType]
    EngagementPreferences: NotRequired[EngagementPreferencesOutputTypeDef]

EngagementPreferencesUnionTypeDef = Union[
    EngagementPreferencesTypeDef, EngagementPreferencesOutputTypeDef
]

class ListEventStreamsResponseTypeDef(TypedDict):
    Items: List[EventStreamSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DetectProfileObjectTypeResponseTypeDef(TypedDict):
    DetectedProfileObjectTypes: List[DetectedProfileObjectTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RecommenderConfigOutputTypeDef(TypedDict):
    EventsConfig: EventsConfigOutputTypeDef
    TrainingFrequency: NotRequired[int]

class RecommenderConfigTypeDef(TypedDict):
    EventsConfig: EventsConfigTypeDef
    TrainingFrequency: NotRequired[int]

class EventTriggerConditionOutputTypeDef(TypedDict):
    EventTriggerDimensions: List[EventTriggerDimensionOutputTypeDef]
    LogicalOperator: EventTriggerLogicalOperatorType

EventTriggerLimitsUnionTypeDef = Union[EventTriggerLimitsTypeDef, EventTriggerLimitsOutputTypeDef]

class MatchingResponseTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    JobSchedule: NotRequired[JobScheduleTypeDef]
    AutoMerging: NotRequired[AutoMergingOutputTypeDef]
    ExportingConfig: NotRequired[ExportingConfigTypeDef]

class RuleBasedMatchingResponseTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    MatchingRules: NotRequired[List[MatchingRuleOutputTypeDef]]
    Status: NotRequired[RuleBasedMatchingStatusType]
    MaxAllowedRuleLevelForMerging: NotRequired[int]
    MaxAllowedRuleLevelForMatching: NotRequired[int]
    AttributeTypesSelector: NotRequired[AttributeTypesSelectorOutputTypeDef]
    ConflictResolution: NotRequired[ConflictResolutionTypeDef]
    ExportingConfig: NotRequired[ExportingConfigTypeDef]

class GetIdentityResolutionJobResponseTypeDef(TypedDict):
    DomainName: str
    JobId: str
    Status: IdentityResolutionJobStatusType
    Message: str
    JobStartTime: datetime
    JobEndTime: datetime
    LastUpdatedAt: datetime
    JobExpirationTime: datetime
    AutoMerging: AutoMergingOutputTypeDef
    ExportingLocation: ExportingLocationTypeDef
    JobStats: JobStatsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IdentityResolutionJobTypeDef(TypedDict):
    DomainName: NotRequired[str]
    JobId: NotRequired[str]
    Status: NotRequired[IdentityResolutionJobStatusType]
    JobStartTime: NotRequired[datetime]
    JobEndTime: NotRequired[datetime]
    JobStats: NotRequired[JobStatsTypeDef]
    ExportingLocation: NotRequired[ExportingLocationTypeDef]
    Message: NotRequired[str]

FilterGroupOutputTypeDef = TypedDict(
    "FilterGroupOutputTypeDef",
    {
        "Type": TypeType,
        "Dimensions": List[FilterDimensionOutputTypeDef],
    },
)
FilterGroupTypeDef = TypedDict(
    "FilterGroupTypeDef",
    {
        "Type": TypeType,
        "Dimensions": Sequence[FilterDimensionTypeDef],
    },
)

class GetObjectTypeAttributeStatisticsResponseTypeDef(TypedDict):
    Statistics: GetObjectTypeAttributeStatisticsStatsTypeDef
    CalculatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class RuleBasedMatchingRequestTypeDef(TypedDict):
    Enabled: bool
    MatchingRules: NotRequired[Sequence[MatchingRuleUnionTypeDef]]
    MaxAllowedRuleLevelForMerging: NotRequired[int]
    MaxAllowedRuleLevelForMatching: NotRequired[int]
    AttributeTypesSelector: NotRequired[AttributeTypesSelectorUnionTypeDef]
    ConflictResolution: NotRequired[ConflictResolutionTypeDef]
    ExportingConfig: NotRequired[ExportingConfigTypeDef]

class EventTriggerDimensionTypeDef(TypedDict):
    ObjectAttributes: Sequence[ObjectAttributeUnionTypeDef]

class PutProfileObjectTypeRequestTypeDef(TypedDict):
    DomainName: str
    ObjectTypeName: str
    Description: str
    TemplateId: NotRequired[str]
    ExpirationDays: NotRequired[int]
    EncryptionKey: NotRequired[str]
    AllowProfileCreation: NotRequired[bool]
    SourceLastUpdatedTimestampFormat: NotRequired[str]
    MaxProfileObjectCount: NotRequired[int]
    Fields: NotRequired[Mapping[str, ObjectTypeFieldTypeDef]]
    Keys: NotRequired[Mapping[str, Sequence[ObjectTypeKeyUnionTypeDef]]]
    Tags: NotRequired[Mapping[str, str]]

class AddressDimensionTypeDef(TypedDict):
    City: NotRequired[ProfileDimensionUnionTypeDef]
    Country: NotRequired[ProfileDimensionUnionTypeDef]
    County: NotRequired[ProfileDimensionUnionTypeDef]
    PostalCode: NotRequired[ProfileDimensionUnionTypeDef]
    Province: NotRequired[ProfileDimensionUnionTypeDef]
    State: NotRequired[ProfileDimensionUnionTypeDef]

class ConditionsTypeDef(TypedDict):
    Range: NotRequired[RangeTypeDef]
    ObjectCount: NotRequired[int]
    Threshold: NotRequired[ThresholdTypeDef]

class SourceFlowConfigTypeDef(TypedDict):
    ConnectorType: SourceConnectorTypeType
    SourceConnectorProperties: SourceConnectorPropertiesTypeDef
    ConnectorProfileName: NotRequired[str]
    IncrementalPullConfig: NotRequired[IncrementalPullConfigTypeDef]

class TriggerConfigTypeDef(TypedDict):
    TriggerType: TriggerTypeType
    TriggerProperties: NotRequired[TriggerPropertiesTypeDef]

class DimensionOutputTypeDef(TypedDict):
    ProfileAttributes: NotRequired[ProfileAttributesOutputTypeDef]
    CalculatedAttributes: NotRequired[Dict[str, CalculatedAttributeDimensionOutputTypeDef]]

CalculatedAttributeDimensionUnionTypeDef = Union[
    CalculatedAttributeDimensionTypeDef, CalculatedAttributeDimensionOutputTypeDef
]
AutoMergingUnionTypeDef = Union[AutoMergingTypeDef, AutoMergingOutputTypeDef]

class BatchGetProfileResponseTypeDef(TypedDict):
    Errors: List[BatchGetProfileErrorTypeDef]
    Profiles: List[ProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ProfileQueryResultTypeDef(TypedDict):
    ProfileId: str
    QueryResult: QueryResultType
    Profile: NotRequired[ProfileTypeDef]

class SearchProfilesResponseTypeDef(TypedDict):
    Items: List[ProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateProfileRequestTypeDef(TypedDict):
    DomainName: str
    AccountNumber: NotRequired[str]
    AdditionalInformation: NotRequired[str]
    PartyType: NotRequired[PartyTypeType]
    BusinessName: NotRequired[str]
    FirstName: NotRequired[str]
    MiddleName: NotRequired[str]
    LastName: NotRequired[str]
    BirthDate: NotRequired[str]
    Gender: NotRequired[GenderType]
    PhoneNumber: NotRequired[str]
    MobilePhoneNumber: NotRequired[str]
    HomePhoneNumber: NotRequired[str]
    BusinessPhoneNumber: NotRequired[str]
    EmailAddress: NotRequired[str]
    PersonalEmailAddress: NotRequired[str]
    BusinessEmailAddress: NotRequired[str]
    Address: NotRequired[AddressTypeDef]
    ShippingAddress: NotRequired[AddressTypeDef]
    MailingAddress: NotRequired[AddressTypeDef]
    BillingAddress: NotRequired[AddressTypeDef]
    Attributes: NotRequired[Mapping[str, str]]
    PartyTypeString: NotRequired[str]
    GenderString: NotRequired[str]
    ProfileType: NotRequired[ProfileTypeType]
    EngagementPreferences: NotRequired[EngagementPreferencesUnionTypeDef]

class UpdateProfileRequestTypeDef(TypedDict):
    DomainName: str
    ProfileId: str
    AdditionalInformation: NotRequired[str]
    AccountNumber: NotRequired[str]
    PartyType: NotRequired[PartyTypeType]
    BusinessName: NotRequired[str]
    FirstName: NotRequired[str]
    MiddleName: NotRequired[str]
    LastName: NotRequired[str]
    BirthDate: NotRequired[str]
    Gender: NotRequired[GenderType]
    PhoneNumber: NotRequired[str]
    MobilePhoneNumber: NotRequired[str]
    HomePhoneNumber: NotRequired[str]
    BusinessPhoneNumber: NotRequired[str]
    EmailAddress: NotRequired[str]
    PersonalEmailAddress: NotRequired[str]
    BusinessEmailAddress: NotRequired[str]
    Address: NotRequired[UpdateAddressTypeDef]
    ShippingAddress: NotRequired[UpdateAddressTypeDef]
    MailingAddress: NotRequired[UpdateAddressTypeDef]
    BillingAddress: NotRequired[UpdateAddressTypeDef]
    Attributes: NotRequired[Mapping[str, str]]
    PartyTypeString: NotRequired[str]
    GenderString: NotRequired[str]
    ProfileType: NotRequired[ProfileTypeType]
    EngagementPreferences: NotRequired[EngagementPreferencesUnionTypeDef]

class RecommenderUpdateTypeDef(TypedDict):
    RecommenderConfig: NotRequired[RecommenderConfigOutputTypeDef]
    Status: NotRequired[RecommenderStatusType]
    CreatedAt: NotRequired[datetime]
    LastUpdatedAt: NotRequired[datetime]
    FailureReason: NotRequired[str]

RecommenderConfigUnionTypeDef = Union[RecommenderConfigTypeDef, RecommenderConfigOutputTypeDef]

class CreateEventTriggerResponseTypeDef(TypedDict):
    EventTriggerName: str
    ObjectTypeName: str
    Description: str
    EventTriggerConditions: List[EventTriggerConditionOutputTypeDef]
    SegmentFilter: str
    EventTriggerLimits: EventTriggerLimitsOutputTypeDef
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetEventTriggerResponseTypeDef(TypedDict):
    EventTriggerName: str
    ObjectTypeName: str
    Description: str
    EventTriggerConditions: List[EventTriggerConditionOutputTypeDef]
    SegmentFilter: str
    EventTriggerLimits: EventTriggerLimitsOutputTypeDef
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEventTriggerResponseTypeDef(TypedDict):
    EventTriggerName: str
    ObjectTypeName: str
    Description: str
    EventTriggerConditions: List[EventTriggerConditionOutputTypeDef]
    SegmentFilter: str
    EventTriggerLimits: EventTriggerLimitsOutputTypeDef
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainResponseTypeDef(TypedDict):
    DomainName: str
    DefaultExpirationDays: int
    DefaultEncryptionKey: str
    DeadLetterQueueUrl: str
    Matching: MatchingResponseTypeDef
    RuleBasedMatching: RuleBasedMatchingResponseTypeDef
    DataStore: DataStoreResponseTypeDef
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainResponseTypeDef(TypedDict):
    DomainName: str
    DefaultExpirationDays: int
    DefaultEncryptionKey: str
    DeadLetterQueueUrl: str
    Stats: DomainStatsTypeDef
    Matching: MatchingResponseTypeDef
    RuleBasedMatching: RuleBasedMatchingResponseTypeDef
    DataStore: DataStoreResponseTypeDef
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainResponseTypeDef(TypedDict):
    DomainName: str
    DefaultExpirationDays: int
    DefaultEncryptionKey: str
    DeadLetterQueueUrl: str
    Matching: MatchingResponseTypeDef
    RuleBasedMatching: RuleBasedMatchingResponseTypeDef
    DataStore: DataStoreResponseTypeDef
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListIdentityResolutionJobsResponseTypeDef(TypedDict):
    IdentityResolutionJobsList: List[IdentityResolutionJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class FilterOutputTypeDef(TypedDict):
    Include: IncludeType
    Groups: List[FilterGroupOutputTypeDef]

class FilterTypeDef(TypedDict):
    Include: IncludeType
    Groups: Sequence[FilterGroupTypeDef]

EventTriggerDimensionUnionTypeDef = Union[
    EventTriggerDimensionTypeDef, EventTriggerDimensionOutputTypeDef
]
AddressDimensionUnionTypeDef = Union[AddressDimensionTypeDef, AddressDimensionOutputTypeDef]

class UpdateCalculatedAttributeDefinitionRequestTypeDef(TypedDict):
    DomainName: str
    CalculatedAttributeName: str
    DisplayName: NotRequired[str]
    Description: NotRequired[str]
    Conditions: NotRequired[ConditionsTypeDef]

class UpdateCalculatedAttributeDefinitionResponseTypeDef(TypedDict):
    CalculatedAttributeName: str
    DisplayName: str
    Description: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Statistic: StatisticType
    Conditions: ConditionsTypeDef
    AttributeDetails: AttributeDetailsOutputTypeDef
    UseHistoricalData: bool
    Status: ReadinessStatusType
    Readiness: ReadinessTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class FlowDefinitionTypeDef(TypedDict):
    FlowName: str
    KmsArn: str
    SourceFlowConfig: SourceFlowConfigTypeDef
    Tasks: Sequence[TaskTypeDef]
    TriggerConfig: TriggerConfigTypeDef
    Description: NotRequired[str]

GroupOutputTypeDef = TypedDict(
    "GroupOutputTypeDef",
    {
        "Dimensions": NotRequired[List[DimensionOutputTypeDef]],
        "SourceSegments": NotRequired[List[SourceSegmentTypeDef]],
        "SourceType": NotRequired[IncludeOptionsType],
        "Type": NotRequired[IncludeOptionsType],
    },
)

class MatchingRequestTypeDef(TypedDict):
    Enabled: bool
    JobSchedule: NotRequired[JobScheduleTypeDef]
    AutoMerging: NotRequired[AutoMergingUnionTypeDef]
    ExportingConfig: NotRequired[ExportingConfigTypeDef]

class GetSegmentMembershipResponseTypeDef(TypedDict):
    SegmentDefinitionName: str
    Profiles: List[ProfileQueryResultTypeDef]
    Failures: List[ProfileQueryFailuresTypeDef]
    LastComputedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecommenderResponseTypeDef(TypedDict):
    RecommenderName: str
    RecommenderRecipeName: RecommenderRecipeNameType
    RecommenderConfig: RecommenderConfigOutputTypeDef
    Description: str
    Status: RecommenderStatusType
    LastUpdatedAt: datetime
    CreatedAt: datetime
    FailureReason: str
    LatestRecommenderUpdate: RecommenderUpdateTypeDef
    TrainingMetrics: List[TrainingMetricsTypeDef]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RecommenderSummaryTypeDef(TypedDict):
    RecommenderName: NotRequired[str]
    RecipeName: NotRequired[RecommenderRecipeNameType]
    RecommenderConfig: NotRequired[RecommenderConfigOutputTypeDef]
    CreatedAt: NotRequired[datetime]
    Description: NotRequired[str]
    Status: NotRequired[RecommenderStatusType]
    LastUpdatedAt: NotRequired[datetime]
    Tags: NotRequired[Dict[str, str]]
    FailureReason: NotRequired[str]
    LatestRecommenderUpdate: NotRequired[RecommenderUpdateTypeDef]

class CreateRecommenderRequestTypeDef(TypedDict):
    DomainName: str
    RecommenderName: str
    RecommenderRecipeName: RecommenderRecipeNameType
    RecommenderConfig: NotRequired[RecommenderConfigUnionTypeDef]
    Description: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class UpdateRecommenderRequestTypeDef(TypedDict):
    DomainName: str
    RecommenderName: str
    Description: NotRequired[str]
    RecommenderConfig: NotRequired[RecommenderConfigUnionTypeDef]

class CreateCalculatedAttributeDefinitionResponseTypeDef(TypedDict):
    CalculatedAttributeName: str
    DisplayName: str
    Description: str
    AttributeDetails: AttributeDetailsOutputTypeDef
    Conditions: ConditionsTypeDef
    Filter: FilterOutputTypeDef
    Statistic: StatisticType
    CreatedAt: datetime
    LastUpdatedAt: datetime
    UseHistoricalData: bool
    Status: ReadinessStatusType
    Readiness: ReadinessTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCalculatedAttributeDefinitionResponseTypeDef(TypedDict):
    CalculatedAttributeName: str
    DisplayName: str
    Description: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Statistic: StatisticType
    Filter: FilterOutputTypeDef
    Conditions: ConditionsTypeDef
    AttributeDetails: AttributeDetailsOutputTypeDef
    UseHistoricalData: bool
    Status: ReadinessStatusType
    Readiness: ReadinessTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

FilterUnionTypeDef = Union[FilterTypeDef, FilterOutputTypeDef]

class EventTriggerConditionTypeDef(TypedDict):
    EventTriggerDimensions: Sequence[EventTriggerDimensionUnionTypeDef]
    LogicalOperator: EventTriggerLogicalOperatorType

class ProfileAttributesTypeDef(TypedDict):
    AccountNumber: NotRequired[ProfileDimensionUnionTypeDef]
    AdditionalInformation: NotRequired[ExtraLengthValueProfileDimensionUnionTypeDef]
    FirstName: NotRequired[ProfileDimensionUnionTypeDef]
    LastName: NotRequired[ProfileDimensionUnionTypeDef]
    MiddleName: NotRequired[ProfileDimensionUnionTypeDef]
    GenderString: NotRequired[ProfileDimensionUnionTypeDef]
    PartyTypeString: NotRequired[ProfileDimensionUnionTypeDef]
    BirthDate: NotRequired[DateDimensionUnionTypeDef]
    PhoneNumber: NotRequired[ProfileDimensionUnionTypeDef]
    BusinessName: NotRequired[ProfileDimensionUnionTypeDef]
    BusinessPhoneNumber: NotRequired[ProfileDimensionUnionTypeDef]
    HomePhoneNumber: NotRequired[ProfileDimensionUnionTypeDef]
    MobilePhoneNumber: NotRequired[ProfileDimensionUnionTypeDef]
    EmailAddress: NotRequired[ProfileDimensionUnionTypeDef]
    PersonalEmailAddress: NotRequired[ProfileDimensionUnionTypeDef]
    BusinessEmailAddress: NotRequired[ProfileDimensionUnionTypeDef]
    Address: NotRequired[AddressDimensionUnionTypeDef]
    ShippingAddress: NotRequired[AddressDimensionUnionTypeDef]
    MailingAddress: NotRequired[AddressDimensionUnionTypeDef]
    BillingAddress: NotRequired[AddressDimensionUnionTypeDef]
    Attributes: NotRequired[Mapping[str, AttributeDimensionUnionTypeDef]]
    ProfileType: NotRequired[ProfileTypeDimensionUnionTypeDef]

class AppflowIntegrationTypeDef(TypedDict):
    FlowDefinition: FlowDefinitionTypeDef
    Batches: NotRequired[Sequence[BatchTypeDef]]

class PutIntegrationRequestTypeDef(TypedDict):
    DomainName: str
    Uri: NotRequired[str]
    ObjectTypeName: NotRequired[str]
    ObjectTypeNames: NotRequired[Mapping[str, str]]
    Tags: NotRequired[Mapping[str, str]]
    FlowDefinition: NotRequired[FlowDefinitionTypeDef]
    RoleArn: NotRequired[str]
    EventTriggerNames: NotRequired[Sequence[str]]
    Scope: NotRequired[ScopeType]

class SegmentGroupOutputTypeDef(TypedDict):
    Groups: NotRequired[List[GroupOutputTypeDef]]
    Include: NotRequired[IncludeOptionsType]

class CreateDomainRequestTypeDef(TypedDict):
    DomainName: str
    DefaultExpirationDays: int
    DefaultEncryptionKey: NotRequired[str]
    DeadLetterQueueUrl: NotRequired[str]
    Matching: NotRequired[MatchingRequestTypeDef]
    RuleBasedMatching: NotRequired[RuleBasedMatchingRequestTypeDef]
    DataStore: NotRequired[DataStoreRequestTypeDef]
    Tags: NotRequired[Mapping[str, str]]

class UpdateDomainRequestTypeDef(TypedDict):
    DomainName: str
    DefaultExpirationDays: NotRequired[int]
    DefaultEncryptionKey: NotRequired[str]
    DeadLetterQueueUrl: NotRequired[str]
    Matching: NotRequired[MatchingRequestTypeDef]
    RuleBasedMatching: NotRequired[RuleBasedMatchingRequestTypeDef]
    DataStore: NotRequired[DataStoreRequestTypeDef]
    Tags: NotRequired[Mapping[str, str]]

class ListRecommendersResponseTypeDef(TypedDict):
    Recommenders: List[RecommenderSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateCalculatedAttributeDefinitionRequestTypeDef(TypedDict):
    DomainName: str
    CalculatedAttributeName: str
    AttributeDetails: AttributeDetailsUnionTypeDef
    Statistic: StatisticType
    DisplayName: NotRequired[str]
    Description: NotRequired[str]
    Conditions: NotRequired[ConditionsTypeDef]
    Filter: NotRequired[FilterUnionTypeDef]
    UseHistoricalData: NotRequired[bool]
    Tags: NotRequired[Mapping[str, str]]

EventTriggerConditionUnionTypeDef = Union[
    EventTriggerConditionTypeDef, EventTriggerConditionOutputTypeDef
]
ProfileAttributesUnionTypeDef = Union[ProfileAttributesTypeDef, ProfileAttributesOutputTypeDef]

class IntegrationConfigTypeDef(TypedDict):
    AppflowIntegration: NotRequired[AppflowIntegrationTypeDef]

class GetSegmentDefinitionResponseTypeDef(TypedDict):
    SegmentDefinitionName: str
    DisplayName: str
    Description: str
    SegmentGroups: SegmentGroupOutputTypeDef
    SegmentDefinitionArn: str
    CreatedAt: datetime
    Tags: Dict[str, str]
    SegmentSqlQuery: str
    SegmentType: SegmentTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventTriggerRequestTypeDef(TypedDict):
    DomainName: str
    EventTriggerName: str
    ObjectTypeName: str
    EventTriggerConditions: Sequence[EventTriggerConditionUnionTypeDef]
    Description: NotRequired[str]
    SegmentFilter: NotRequired[str]
    EventTriggerLimits: NotRequired[EventTriggerLimitsUnionTypeDef]
    Tags: NotRequired[Mapping[str, str]]

class UpdateEventTriggerRequestTypeDef(TypedDict):
    DomainName: str
    EventTriggerName: str
    ObjectTypeName: NotRequired[str]
    Description: NotRequired[str]
    EventTriggerConditions: NotRequired[Sequence[EventTriggerConditionUnionTypeDef]]
    SegmentFilter: NotRequired[str]
    EventTriggerLimits: NotRequired[EventTriggerLimitsUnionTypeDef]

class DimensionTypeDef(TypedDict):
    ProfileAttributes: NotRequired[ProfileAttributesUnionTypeDef]
    CalculatedAttributes: NotRequired[Mapping[str, CalculatedAttributeDimensionUnionTypeDef]]

class CreateIntegrationWorkflowRequestTypeDef(TypedDict):
    DomainName: str
    WorkflowType: Literal["APPFLOW_INTEGRATION"]
    IntegrationConfig: IntegrationConfigTypeDef
    ObjectTypeName: str
    RoleArn: str
    Tags: NotRequired[Mapping[str, str]]

DimensionUnionTypeDef = Union[DimensionTypeDef, DimensionOutputTypeDef]
GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "Dimensions": NotRequired[Sequence[DimensionUnionTypeDef]],
        "SourceSegments": NotRequired[Sequence[SourceSegmentTypeDef]],
        "SourceType": NotRequired[IncludeOptionsType],
        "Type": NotRequired[IncludeOptionsType],
    },
)
GroupUnionTypeDef = Union[GroupTypeDef, GroupOutputTypeDef]

class SegmentGroupTypeDef(TypedDict):
    Groups: NotRequired[Sequence[GroupTypeDef]]
    Include: NotRequired[IncludeOptionsType]

class SegmentGroupStructureTypeDef(TypedDict):
    Groups: NotRequired[Sequence[GroupUnionTypeDef]]
    Include: NotRequired[IncludeOptionsType]

SegmentGroupUnionTypeDef = Union[SegmentGroupTypeDef, SegmentGroupOutputTypeDef]

class CreateSegmentEstimateRequestTypeDef(TypedDict):
    DomainName: str
    SegmentQuery: NotRequired[SegmentGroupStructureTypeDef]
    SegmentSqlQuery: NotRequired[str]

class CreateSegmentDefinitionRequestTypeDef(TypedDict):
    DomainName: str
    SegmentDefinitionName: str
    DisplayName: str
    Description: NotRequired[str]
    SegmentGroups: NotRequired[SegmentGroupUnionTypeDef]
    SegmentSqlQuery: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
