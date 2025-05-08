"""
Type annotations for config service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_config/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_config.type_defs import AccountAggregationSourceOutputTypeDef

    data: AccountAggregationSourceOutputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AggregateConformancePackComplianceSummaryGroupKeyType,
    AggregatedSourceStatusTypeType,
    AggregatedSourceTypeType,
    ChronologicalOrderType,
    ComplianceTypeType,
    ConfigRuleComplianceSummaryGroupKeyType,
    ConfigRuleStateType,
    ConfigurationItemStatusType,
    ConformancePackComplianceTypeType,
    ConformancePackStateType,
    DeliveryStatusType,
    EvaluationModeType,
    MaximumExecutionFrequencyType,
    MemberAccountRuleStatusType,
    MessageTypeType,
    OrganizationConfigRuleTriggerTypeNoSNType,
    OrganizationConfigRuleTriggerTypeType,
    OrganizationResourceDetailedStatusType,
    OrganizationResourceStatusType,
    OrganizationRuleStatusType,
    OwnerType,
    RecorderStatusType,
    RecordingFrequencyType,
    RecordingScopeType,
    RecordingStrategyTypeType,
    RemediationExecutionStateType,
    RemediationExecutionStepStateType,
    ResourceCountGroupKeyType,
    ResourceEvaluationStatusType,
    ResourceTypeType,
    SortOrderType,
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
    "AccountAggregationSourceOutputTypeDef",
    "AccountAggregationSourceTypeDef",
    "AccountAggregationSourceUnionTypeDef",
    "AggregateComplianceByConfigRuleTypeDef",
    "AggregateComplianceByConformancePackTypeDef",
    "AggregateComplianceCountTypeDef",
    "AggregateConformancePackComplianceCountTypeDef",
    "AggregateConformancePackComplianceFiltersTypeDef",
    "AggregateConformancePackComplianceSummaryFiltersTypeDef",
    "AggregateConformancePackComplianceSummaryTypeDef",
    "AggregateConformancePackComplianceTypeDef",
    "AggregateEvaluationResultTypeDef",
    "AggregateResourceIdentifierTypeDef",
    "AggregatedSourceStatusTypeDef",
    "AggregationAuthorizationTypeDef",
    "AggregatorFilterResourceTypeOutputTypeDef",
    "AggregatorFilterResourceTypeTypeDef",
    "AggregatorFilterServicePrincipalOutputTypeDef",
    "AggregatorFilterServicePrincipalTypeDef",
    "AggregatorFiltersOutputTypeDef",
    "AggregatorFiltersTypeDef",
    "AggregatorFiltersUnionTypeDef",
    "AssociateResourceTypesRequestTypeDef",
    "AssociateResourceTypesResponseTypeDef",
    "BaseConfigurationItemTypeDef",
    "BatchGetAggregateResourceConfigRequestTypeDef",
    "BatchGetAggregateResourceConfigResponseTypeDef",
    "BatchGetResourceConfigRequestTypeDef",
    "BatchGetResourceConfigResponseTypeDef",
    "ComplianceByConfigRuleTypeDef",
    "ComplianceByResourceTypeDef",
    "ComplianceContributorCountTypeDef",
    "ComplianceSummaryByResourceTypeTypeDef",
    "ComplianceSummaryTypeDef",
    "ComplianceTypeDef",
    "ConfigExportDeliveryInfoTypeDef",
    "ConfigRuleComplianceFiltersTypeDef",
    "ConfigRuleComplianceSummaryFiltersTypeDef",
    "ConfigRuleEvaluationStatusTypeDef",
    "ConfigRuleOutputTypeDef",
    "ConfigRuleTypeDef",
    "ConfigRuleUnionTypeDef",
    "ConfigSnapshotDeliveryPropertiesTypeDef",
    "ConfigStreamDeliveryInfoTypeDef",
    "ConfigurationAggregatorTypeDef",
    "ConfigurationItemTypeDef",
    "ConfigurationRecorderFilterTypeDef",
    "ConfigurationRecorderOutputTypeDef",
    "ConfigurationRecorderStatusTypeDef",
    "ConfigurationRecorderSummaryTypeDef",
    "ConfigurationRecorderTypeDef",
    "ConfigurationRecorderUnionTypeDef",
    "ConformancePackComplianceFiltersTypeDef",
    "ConformancePackComplianceScoreTypeDef",
    "ConformancePackComplianceScoresFiltersTypeDef",
    "ConformancePackComplianceSummaryTypeDef",
    "ConformancePackDetailTypeDef",
    "ConformancePackEvaluationFiltersTypeDef",
    "ConformancePackEvaluationResultTypeDef",
    "ConformancePackInputParameterTypeDef",
    "ConformancePackRuleComplianceTypeDef",
    "ConformancePackStatusDetailTypeDef",
    "CustomPolicyDetailsTypeDef",
    "DeleteAggregationAuthorizationRequestTypeDef",
    "DeleteConfigRuleRequestTypeDef",
    "DeleteConfigurationAggregatorRequestTypeDef",
    "DeleteConfigurationRecorderRequestTypeDef",
    "DeleteConformancePackRequestTypeDef",
    "DeleteDeliveryChannelRequestTypeDef",
    "DeleteEvaluationResultsRequestTypeDef",
    "DeleteOrganizationConfigRuleRequestTypeDef",
    "DeleteOrganizationConformancePackRequestTypeDef",
    "DeletePendingAggregationRequestRequestTypeDef",
    "DeleteRemediationConfigurationRequestTypeDef",
    "DeleteRemediationExceptionsRequestTypeDef",
    "DeleteRemediationExceptionsResponseTypeDef",
    "DeleteResourceConfigRequestTypeDef",
    "DeleteRetentionConfigurationRequestTypeDef",
    "DeleteServiceLinkedConfigurationRecorderRequestTypeDef",
    "DeleteServiceLinkedConfigurationRecorderResponseTypeDef",
    "DeleteStoredQueryRequestTypeDef",
    "DeliverConfigSnapshotRequestTypeDef",
    "DeliverConfigSnapshotResponseTypeDef",
    "DeliveryChannelStatusTypeDef",
    "DeliveryChannelTypeDef",
    "DescribeAggregateComplianceByConfigRulesRequestPaginateTypeDef",
    "DescribeAggregateComplianceByConfigRulesRequestTypeDef",
    "DescribeAggregateComplianceByConfigRulesResponseTypeDef",
    "DescribeAggregateComplianceByConformancePacksRequestPaginateTypeDef",
    "DescribeAggregateComplianceByConformancePacksRequestTypeDef",
    "DescribeAggregateComplianceByConformancePacksResponseTypeDef",
    "DescribeAggregationAuthorizationsRequestPaginateTypeDef",
    "DescribeAggregationAuthorizationsRequestTypeDef",
    "DescribeAggregationAuthorizationsResponseTypeDef",
    "DescribeComplianceByConfigRuleRequestPaginateTypeDef",
    "DescribeComplianceByConfigRuleRequestTypeDef",
    "DescribeComplianceByConfigRuleResponseTypeDef",
    "DescribeComplianceByResourceRequestPaginateTypeDef",
    "DescribeComplianceByResourceRequestTypeDef",
    "DescribeComplianceByResourceResponseTypeDef",
    "DescribeConfigRuleEvaluationStatusRequestPaginateTypeDef",
    "DescribeConfigRuleEvaluationStatusRequestTypeDef",
    "DescribeConfigRuleEvaluationStatusResponseTypeDef",
    "DescribeConfigRulesFiltersTypeDef",
    "DescribeConfigRulesRequestPaginateTypeDef",
    "DescribeConfigRulesRequestTypeDef",
    "DescribeConfigRulesResponseTypeDef",
    "DescribeConfigurationAggregatorSourcesStatusRequestPaginateTypeDef",
    "DescribeConfigurationAggregatorSourcesStatusRequestTypeDef",
    "DescribeConfigurationAggregatorSourcesStatusResponseTypeDef",
    "DescribeConfigurationAggregatorsRequestPaginateTypeDef",
    "DescribeConfigurationAggregatorsRequestTypeDef",
    "DescribeConfigurationAggregatorsResponseTypeDef",
    "DescribeConfigurationRecorderStatusRequestTypeDef",
    "DescribeConfigurationRecorderStatusResponseTypeDef",
    "DescribeConfigurationRecordersRequestTypeDef",
    "DescribeConfigurationRecordersResponseTypeDef",
    "DescribeConformancePackComplianceRequestTypeDef",
    "DescribeConformancePackComplianceResponseTypeDef",
    "DescribeConformancePackStatusRequestPaginateTypeDef",
    "DescribeConformancePackStatusRequestTypeDef",
    "DescribeConformancePackStatusResponseTypeDef",
    "DescribeConformancePacksRequestPaginateTypeDef",
    "DescribeConformancePacksRequestTypeDef",
    "DescribeConformancePacksResponseTypeDef",
    "DescribeDeliveryChannelStatusRequestTypeDef",
    "DescribeDeliveryChannelStatusResponseTypeDef",
    "DescribeDeliveryChannelsRequestTypeDef",
    "DescribeDeliveryChannelsResponseTypeDef",
    "DescribeOrganizationConfigRuleStatusesRequestPaginateTypeDef",
    "DescribeOrganizationConfigRuleStatusesRequestTypeDef",
    "DescribeOrganizationConfigRuleStatusesResponseTypeDef",
    "DescribeOrganizationConfigRulesRequestPaginateTypeDef",
    "DescribeOrganizationConfigRulesRequestTypeDef",
    "DescribeOrganizationConfigRulesResponseTypeDef",
    "DescribeOrganizationConformancePackStatusesRequestPaginateTypeDef",
    "DescribeOrganizationConformancePackStatusesRequestTypeDef",
    "DescribeOrganizationConformancePackStatusesResponseTypeDef",
    "DescribeOrganizationConformancePacksRequestPaginateTypeDef",
    "DescribeOrganizationConformancePacksRequestTypeDef",
    "DescribeOrganizationConformancePacksResponseTypeDef",
    "DescribePendingAggregationRequestsRequestPaginateTypeDef",
    "DescribePendingAggregationRequestsRequestTypeDef",
    "DescribePendingAggregationRequestsResponseTypeDef",
    "DescribeRemediationConfigurationsRequestTypeDef",
    "DescribeRemediationConfigurationsResponseTypeDef",
    "DescribeRemediationExceptionsRequestTypeDef",
    "DescribeRemediationExceptionsResponseTypeDef",
    "DescribeRemediationExecutionStatusRequestPaginateTypeDef",
    "DescribeRemediationExecutionStatusRequestTypeDef",
    "DescribeRemediationExecutionStatusResponseTypeDef",
    "DescribeRetentionConfigurationsRequestPaginateTypeDef",
    "DescribeRetentionConfigurationsRequestTypeDef",
    "DescribeRetentionConfigurationsResponseTypeDef",
    "DisassociateResourceTypesRequestTypeDef",
    "DisassociateResourceTypesResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EvaluationContextTypeDef",
    "EvaluationModeConfigurationTypeDef",
    "EvaluationOutputTypeDef",
    "EvaluationResultIdentifierTypeDef",
    "EvaluationResultQualifierTypeDef",
    "EvaluationResultTypeDef",
    "EvaluationStatusTypeDef",
    "EvaluationTypeDef",
    "EvaluationUnionTypeDef",
    "ExclusionByResourceTypesOutputTypeDef",
    "ExclusionByResourceTypesTypeDef",
    "ExecutionControlsTypeDef",
    "ExternalEvaluationTypeDef",
    "FailedDeleteRemediationExceptionsBatchTypeDef",
    "FailedRemediationBatchTypeDef",
    "FailedRemediationExceptionBatchTypeDef",
    "FieldInfoTypeDef",
    "GetAggregateComplianceDetailsByConfigRuleRequestPaginateTypeDef",
    "GetAggregateComplianceDetailsByConfigRuleRequestTypeDef",
    "GetAggregateComplianceDetailsByConfigRuleResponseTypeDef",
    "GetAggregateConfigRuleComplianceSummaryRequestTypeDef",
    "GetAggregateConfigRuleComplianceSummaryResponseTypeDef",
    "GetAggregateConformancePackComplianceSummaryRequestTypeDef",
    "GetAggregateConformancePackComplianceSummaryResponseTypeDef",
    "GetAggregateDiscoveredResourceCountsRequestTypeDef",
    "GetAggregateDiscoveredResourceCountsResponseTypeDef",
    "GetAggregateResourceConfigRequestTypeDef",
    "GetAggregateResourceConfigResponseTypeDef",
    "GetComplianceDetailsByConfigRuleRequestPaginateTypeDef",
    "GetComplianceDetailsByConfigRuleRequestTypeDef",
    "GetComplianceDetailsByConfigRuleResponseTypeDef",
    "GetComplianceDetailsByResourceRequestPaginateTypeDef",
    "GetComplianceDetailsByResourceRequestTypeDef",
    "GetComplianceDetailsByResourceResponseTypeDef",
    "GetComplianceSummaryByConfigRuleResponseTypeDef",
    "GetComplianceSummaryByResourceTypeRequestTypeDef",
    "GetComplianceSummaryByResourceTypeResponseTypeDef",
    "GetConformancePackComplianceDetailsRequestTypeDef",
    "GetConformancePackComplianceDetailsResponseTypeDef",
    "GetConformancePackComplianceSummaryRequestPaginateTypeDef",
    "GetConformancePackComplianceSummaryRequestTypeDef",
    "GetConformancePackComplianceSummaryResponseTypeDef",
    "GetCustomRulePolicyRequestTypeDef",
    "GetCustomRulePolicyResponseTypeDef",
    "GetDiscoveredResourceCountsRequestTypeDef",
    "GetDiscoveredResourceCountsResponseTypeDef",
    "GetOrganizationConfigRuleDetailedStatusRequestPaginateTypeDef",
    "GetOrganizationConfigRuleDetailedStatusRequestTypeDef",
    "GetOrganizationConfigRuleDetailedStatusResponseTypeDef",
    "GetOrganizationConformancePackDetailedStatusRequestPaginateTypeDef",
    "GetOrganizationConformancePackDetailedStatusRequestTypeDef",
    "GetOrganizationConformancePackDetailedStatusResponseTypeDef",
    "GetOrganizationCustomRulePolicyRequestTypeDef",
    "GetOrganizationCustomRulePolicyResponseTypeDef",
    "GetResourceConfigHistoryRequestPaginateTypeDef",
    "GetResourceConfigHistoryRequestTypeDef",
    "GetResourceConfigHistoryResponseTypeDef",
    "GetResourceEvaluationSummaryRequestTypeDef",
    "GetResourceEvaluationSummaryResponseTypeDef",
    "GetStoredQueryRequestTypeDef",
    "GetStoredQueryResponseTypeDef",
    "GroupedResourceCountTypeDef",
    "ListAggregateDiscoveredResourcesRequestPaginateTypeDef",
    "ListAggregateDiscoveredResourcesRequestTypeDef",
    "ListAggregateDiscoveredResourcesResponseTypeDef",
    "ListConfigurationRecordersRequestPaginateTypeDef",
    "ListConfigurationRecordersRequestTypeDef",
    "ListConfigurationRecordersResponseTypeDef",
    "ListConformancePackComplianceScoresRequestTypeDef",
    "ListConformancePackComplianceScoresResponseTypeDef",
    "ListDiscoveredResourcesRequestPaginateTypeDef",
    "ListDiscoveredResourcesRequestTypeDef",
    "ListDiscoveredResourcesResponseTypeDef",
    "ListResourceEvaluationsRequestPaginateTypeDef",
    "ListResourceEvaluationsRequestTypeDef",
    "ListResourceEvaluationsResponseTypeDef",
    "ListStoredQueriesRequestTypeDef",
    "ListStoredQueriesResponseTypeDef",
    "ListTagsForResourceRequestPaginateTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MemberAccountStatusTypeDef",
    "OrganizationAggregationSourceOutputTypeDef",
    "OrganizationAggregationSourceTypeDef",
    "OrganizationAggregationSourceUnionTypeDef",
    "OrganizationConfigRuleStatusTypeDef",
    "OrganizationConfigRuleTypeDef",
    "OrganizationConformancePackDetailedStatusTypeDef",
    "OrganizationConformancePackStatusTypeDef",
    "OrganizationConformancePackTypeDef",
    "OrganizationCustomPolicyRuleMetadataNoPolicyTypeDef",
    "OrganizationCustomPolicyRuleMetadataTypeDef",
    "OrganizationCustomRuleMetadataOutputTypeDef",
    "OrganizationCustomRuleMetadataTypeDef",
    "OrganizationCustomRuleMetadataUnionTypeDef",
    "OrganizationManagedRuleMetadataOutputTypeDef",
    "OrganizationManagedRuleMetadataTypeDef",
    "OrganizationManagedRuleMetadataUnionTypeDef",
    "OrganizationResourceDetailedStatusFiltersTypeDef",
    "PaginatorConfigTypeDef",
    "PendingAggregationRequestTypeDef",
    "PutAggregationAuthorizationRequestTypeDef",
    "PutAggregationAuthorizationResponseTypeDef",
    "PutConfigRuleRequestTypeDef",
    "PutConfigurationAggregatorRequestTypeDef",
    "PutConfigurationAggregatorResponseTypeDef",
    "PutConfigurationRecorderRequestTypeDef",
    "PutConformancePackRequestTypeDef",
    "PutConformancePackResponseTypeDef",
    "PutDeliveryChannelRequestTypeDef",
    "PutEvaluationsRequestTypeDef",
    "PutEvaluationsResponseTypeDef",
    "PutExternalEvaluationRequestTypeDef",
    "PutOrganizationConfigRuleRequestTypeDef",
    "PutOrganizationConfigRuleResponseTypeDef",
    "PutOrganizationConformancePackRequestTypeDef",
    "PutOrganizationConformancePackResponseTypeDef",
    "PutRemediationConfigurationsRequestTypeDef",
    "PutRemediationConfigurationsResponseTypeDef",
    "PutRemediationExceptionsRequestTypeDef",
    "PutRemediationExceptionsResponseTypeDef",
    "PutResourceConfigRequestTypeDef",
    "PutRetentionConfigurationRequestTypeDef",
    "PutRetentionConfigurationResponseTypeDef",
    "PutServiceLinkedConfigurationRecorderRequestTypeDef",
    "PutServiceLinkedConfigurationRecorderResponseTypeDef",
    "PutStoredQueryRequestTypeDef",
    "PutStoredQueryResponseTypeDef",
    "QueryInfoTypeDef",
    "RecordingGroupOutputTypeDef",
    "RecordingGroupTypeDef",
    "RecordingModeOutputTypeDef",
    "RecordingModeOverrideOutputTypeDef",
    "RecordingModeOverrideTypeDef",
    "RecordingModeTypeDef",
    "RecordingStrategyTypeDef",
    "RelationshipTypeDef",
    "RemediationConfigurationOutputTypeDef",
    "RemediationConfigurationTypeDef",
    "RemediationConfigurationUnionTypeDef",
    "RemediationExceptionResourceKeyTypeDef",
    "RemediationExceptionTypeDef",
    "RemediationExecutionStatusTypeDef",
    "RemediationExecutionStepTypeDef",
    "RemediationParameterValueOutputTypeDef",
    "RemediationParameterValueTypeDef",
    "RemediationParameterValueUnionTypeDef",
    "ResourceCountFiltersTypeDef",
    "ResourceCountTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceEvaluationFiltersTypeDef",
    "ResourceEvaluationTypeDef",
    "ResourceFiltersTypeDef",
    "ResourceIdentifierTypeDef",
    "ResourceKeyTypeDef",
    "ResourceValueTypeDef",
    "ResponseMetadataTypeDef",
    "RetentionConfigurationTypeDef",
    "ScopeOutputTypeDef",
    "ScopeTypeDef",
    "SelectAggregateResourceConfigRequestPaginateTypeDef",
    "SelectAggregateResourceConfigRequestTypeDef",
    "SelectAggregateResourceConfigResponseTypeDef",
    "SelectResourceConfigRequestPaginateTypeDef",
    "SelectResourceConfigRequestTypeDef",
    "SelectResourceConfigResponseTypeDef",
    "SourceDetailTypeDef",
    "SourceOutputTypeDef",
    "SourceTypeDef",
    "SsmControlsTypeDef",
    "StartConfigRulesEvaluationRequestTypeDef",
    "StartConfigurationRecorderRequestTypeDef",
    "StartRemediationExecutionRequestTypeDef",
    "StartRemediationExecutionResponseTypeDef",
    "StartResourceEvaluationRequestTypeDef",
    "StartResourceEvaluationResponseTypeDef",
    "StaticValueOutputTypeDef",
    "StaticValueTypeDef",
    "StaticValueUnionTypeDef",
    "StatusDetailFiltersTypeDef",
    "StopConfigurationRecorderRequestTypeDef",
    "StoredQueryMetadataTypeDef",
    "StoredQueryTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TemplateSSMDocumentDetailsTypeDef",
    "TimeWindowTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
)

class AccountAggregationSourceOutputTypeDef(TypedDict):
    AccountIds: List[str]
    AllAwsRegions: NotRequired[bool]
    AwsRegions: NotRequired[List[str]]

class AccountAggregationSourceTypeDef(TypedDict):
    AccountIds: Sequence[str]
    AllAwsRegions: NotRequired[bool]
    AwsRegions: NotRequired[Sequence[str]]

class AggregateConformancePackComplianceTypeDef(TypedDict):
    ComplianceType: NotRequired[ConformancePackComplianceTypeType]
    CompliantRuleCount: NotRequired[int]
    NonCompliantRuleCount: NotRequired[int]
    TotalRuleCount: NotRequired[int]

class AggregateConformancePackComplianceCountTypeDef(TypedDict):
    CompliantConformancePackCount: NotRequired[int]
    NonCompliantConformancePackCount: NotRequired[int]

class AggregateConformancePackComplianceFiltersTypeDef(TypedDict):
    ConformancePackName: NotRequired[str]
    ComplianceType: NotRequired[ConformancePackComplianceTypeType]
    AccountId: NotRequired[str]
    AwsRegion: NotRequired[str]

class AggregateConformancePackComplianceSummaryFiltersTypeDef(TypedDict):
    AccountId: NotRequired[str]
    AwsRegion: NotRequired[str]

class AggregateResourceIdentifierTypeDef(TypedDict):
    SourceAccountId: str
    SourceRegion: str
    ResourceId: str
    ResourceType: ResourceTypeType
    ResourceName: NotRequired[str]

class AggregatedSourceStatusTypeDef(TypedDict):
    SourceId: NotRequired[str]
    SourceType: NotRequired[AggregatedSourceTypeType]
    AwsRegion: NotRequired[str]
    LastUpdateStatus: NotRequired[AggregatedSourceStatusTypeType]
    LastUpdateTime: NotRequired[datetime]
    LastErrorCode: NotRequired[str]
    LastErrorMessage: NotRequired[str]

class AggregationAuthorizationTypeDef(TypedDict):
    AggregationAuthorizationArn: NotRequired[str]
    AuthorizedAccountId: NotRequired[str]
    AuthorizedAwsRegion: NotRequired[str]
    CreationTime: NotRequired[datetime]

AggregatorFilterResourceTypeOutputTypeDef = TypedDict(
    "AggregatorFilterResourceTypeOutputTypeDef",
    {
        "Type": NotRequired[Literal["INCLUDE"]],
        "Value": NotRequired[List[str]],
    },
)
AggregatorFilterResourceTypeTypeDef = TypedDict(
    "AggregatorFilterResourceTypeTypeDef",
    {
        "Type": NotRequired[Literal["INCLUDE"]],
        "Value": NotRequired[Sequence[str]],
    },
)
AggregatorFilterServicePrincipalOutputTypeDef = TypedDict(
    "AggregatorFilterServicePrincipalOutputTypeDef",
    {
        "Type": NotRequired[Literal["INCLUDE"]],
        "Value": NotRequired[List[str]],
    },
)
AggregatorFilterServicePrincipalTypeDef = TypedDict(
    "AggregatorFilterServicePrincipalTypeDef",
    {
        "Type": NotRequired[Literal["INCLUDE"]],
        "Value": NotRequired[Sequence[str]],
    },
)

class AssociateResourceTypesRequestTypeDef(TypedDict):
    ConfigurationRecorderArn: str
    ResourceTypes: Sequence[ResourceTypeType]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class BaseConfigurationItemTypeDef(TypedDict):
    version: NotRequired[str]
    accountId: NotRequired[str]
    configurationItemCaptureTime: NotRequired[datetime]
    configurationItemStatus: NotRequired[ConfigurationItemStatusType]
    configurationStateId: NotRequired[str]
    arn: NotRequired[str]
    resourceType: NotRequired[ResourceTypeType]
    resourceId: NotRequired[str]
    resourceName: NotRequired[str]
    awsRegion: NotRequired[str]
    availabilityZone: NotRequired[str]
    resourceCreationTime: NotRequired[datetime]
    configuration: NotRequired[str]
    supplementaryConfiguration: NotRequired[Dict[str, str]]
    recordingFrequency: NotRequired[RecordingFrequencyType]
    configurationItemDeliveryTime: NotRequired[datetime]

class ResourceKeyTypeDef(TypedDict):
    resourceType: ResourceTypeType
    resourceId: str

class ComplianceContributorCountTypeDef(TypedDict):
    CappedCount: NotRequired[int]
    CapExceeded: NotRequired[bool]

class ConfigExportDeliveryInfoTypeDef(TypedDict):
    lastStatus: NotRequired[DeliveryStatusType]
    lastErrorCode: NotRequired[str]
    lastErrorMessage: NotRequired[str]
    lastAttemptTime: NotRequired[datetime]
    lastSuccessfulTime: NotRequired[datetime]
    nextDeliveryTime: NotRequired[datetime]

class ConfigRuleComplianceFiltersTypeDef(TypedDict):
    ConfigRuleName: NotRequired[str]
    ComplianceType: NotRequired[ComplianceTypeType]
    AccountId: NotRequired[str]
    AwsRegion: NotRequired[str]

class ConfigRuleComplianceSummaryFiltersTypeDef(TypedDict):
    AccountId: NotRequired[str]
    AwsRegion: NotRequired[str]

class ConfigRuleEvaluationStatusTypeDef(TypedDict):
    ConfigRuleName: NotRequired[str]
    ConfigRuleArn: NotRequired[str]
    ConfigRuleId: NotRequired[str]
    LastSuccessfulInvocationTime: NotRequired[datetime]
    LastFailedInvocationTime: NotRequired[datetime]
    LastSuccessfulEvaluationTime: NotRequired[datetime]
    LastFailedEvaluationTime: NotRequired[datetime]
    FirstActivatedTime: NotRequired[datetime]
    LastDeactivatedTime: NotRequired[datetime]
    LastErrorCode: NotRequired[str]
    LastErrorMessage: NotRequired[str]
    FirstEvaluationStarted: NotRequired[bool]
    LastDebugLogDeliveryStatus: NotRequired[str]
    LastDebugLogDeliveryStatusReason: NotRequired[str]
    LastDebugLogDeliveryTime: NotRequired[datetime]

class EvaluationModeConfigurationTypeDef(TypedDict):
    Mode: NotRequired[EvaluationModeType]

class ScopeOutputTypeDef(TypedDict):
    ComplianceResourceTypes: NotRequired[List[str]]
    TagKey: NotRequired[str]
    TagValue: NotRequired[str]
    ComplianceResourceId: NotRequired[str]

class ScopeTypeDef(TypedDict):
    ComplianceResourceTypes: NotRequired[Sequence[str]]
    TagKey: NotRequired[str]
    TagValue: NotRequired[str]
    ComplianceResourceId: NotRequired[str]

class ConfigSnapshotDeliveryPropertiesTypeDef(TypedDict):
    deliveryFrequency: NotRequired[MaximumExecutionFrequencyType]

class ConfigStreamDeliveryInfoTypeDef(TypedDict):
    lastStatus: NotRequired[DeliveryStatusType]
    lastErrorCode: NotRequired[str]
    lastErrorMessage: NotRequired[str]
    lastStatusChangeTime: NotRequired[datetime]

class OrganizationAggregationSourceOutputTypeDef(TypedDict):
    RoleArn: str
    AwsRegions: NotRequired[List[str]]
    AllAwsRegions: NotRequired[bool]

class RelationshipTypeDef(TypedDict):
    resourceType: NotRequired[ResourceTypeType]
    resourceId: NotRequired[str]
    resourceName: NotRequired[str]
    relationshipName: NotRequired[str]

class ConfigurationRecorderFilterTypeDef(TypedDict):
    filterName: NotRequired[Literal["recordingScope"]]
    filterValue: NotRequired[Sequence[str]]

class ConfigurationRecorderStatusTypeDef(TypedDict):
    arn: NotRequired[str]
    name: NotRequired[str]
    lastStartTime: NotRequired[datetime]
    lastStopTime: NotRequired[datetime]
    recording: NotRequired[bool]
    lastStatus: NotRequired[RecorderStatusType]
    lastErrorCode: NotRequired[str]
    lastErrorMessage: NotRequired[str]
    lastStatusChangeTime: NotRequired[datetime]
    servicePrincipal: NotRequired[str]

class ConfigurationRecorderSummaryTypeDef(TypedDict):
    arn: str
    name: str
    recordingScope: RecordingScopeType
    servicePrincipal: NotRequired[str]

class ConformancePackComplianceFiltersTypeDef(TypedDict):
    ConfigRuleNames: NotRequired[Sequence[str]]
    ComplianceType: NotRequired[ConformancePackComplianceTypeType]

class ConformancePackComplianceScoreTypeDef(TypedDict):
    Score: NotRequired[str]
    ConformancePackName: NotRequired[str]
    LastUpdatedTime: NotRequired[datetime]

class ConformancePackComplianceScoresFiltersTypeDef(TypedDict):
    ConformancePackNames: Sequence[str]

class ConformancePackComplianceSummaryTypeDef(TypedDict):
    ConformancePackName: str
    ConformancePackComplianceStatus: ConformancePackComplianceTypeType

class ConformancePackInputParameterTypeDef(TypedDict):
    ParameterName: str
    ParameterValue: str

class TemplateSSMDocumentDetailsTypeDef(TypedDict):
    DocumentName: str
    DocumentVersion: NotRequired[str]

class ConformancePackEvaluationFiltersTypeDef(TypedDict):
    ConfigRuleNames: NotRequired[Sequence[str]]
    ComplianceType: NotRequired[ConformancePackComplianceTypeType]
    ResourceType: NotRequired[str]
    ResourceIds: NotRequired[Sequence[str]]

class ConformancePackRuleComplianceTypeDef(TypedDict):
    ConfigRuleName: NotRequired[str]
    ComplianceType: NotRequired[ConformancePackComplianceTypeType]
    Controls: NotRequired[List[str]]

class ConformancePackStatusDetailTypeDef(TypedDict):
    ConformancePackName: str
    ConformancePackId: str
    ConformancePackArn: str
    ConformancePackState: ConformancePackStateType
    StackArn: str
    LastUpdateRequestedTime: datetime
    ConformancePackStatusReason: NotRequired[str]
    LastUpdateCompletedTime: NotRequired[datetime]

class CustomPolicyDetailsTypeDef(TypedDict):
    PolicyRuntime: str
    PolicyText: str
    EnableDebugLogDelivery: NotRequired[bool]

class DeleteAggregationAuthorizationRequestTypeDef(TypedDict):
    AuthorizedAccountId: str
    AuthorizedAwsRegion: str

class DeleteConfigRuleRequestTypeDef(TypedDict):
    ConfigRuleName: str

class DeleteConfigurationAggregatorRequestTypeDef(TypedDict):
    ConfigurationAggregatorName: str

class DeleteConfigurationRecorderRequestTypeDef(TypedDict):
    ConfigurationRecorderName: str

class DeleteConformancePackRequestTypeDef(TypedDict):
    ConformancePackName: str

class DeleteDeliveryChannelRequestTypeDef(TypedDict):
    DeliveryChannelName: str

class DeleteEvaluationResultsRequestTypeDef(TypedDict):
    ConfigRuleName: str

class DeleteOrganizationConfigRuleRequestTypeDef(TypedDict):
    OrganizationConfigRuleName: str

class DeleteOrganizationConformancePackRequestTypeDef(TypedDict):
    OrganizationConformancePackName: str

class DeletePendingAggregationRequestRequestTypeDef(TypedDict):
    RequesterAccountId: str
    RequesterAwsRegion: str

class DeleteRemediationConfigurationRequestTypeDef(TypedDict):
    ConfigRuleName: str
    ResourceType: NotRequired[str]

class RemediationExceptionResourceKeyTypeDef(TypedDict):
    ResourceType: NotRequired[str]
    ResourceId: NotRequired[str]

class DeleteResourceConfigRequestTypeDef(TypedDict):
    ResourceType: str
    ResourceId: str

class DeleteRetentionConfigurationRequestTypeDef(TypedDict):
    RetentionConfigurationName: str

class DeleteServiceLinkedConfigurationRecorderRequestTypeDef(TypedDict):
    ServicePrincipal: str

class DeleteStoredQueryRequestTypeDef(TypedDict):
    QueryName: str

class DeliverConfigSnapshotRequestTypeDef(TypedDict):
    deliveryChannelName: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeAggregationAuthorizationsRequestTypeDef(TypedDict):
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeComplianceByConfigRuleRequestTypeDef(TypedDict):
    ConfigRuleNames: NotRequired[Sequence[str]]
    ComplianceTypes: NotRequired[Sequence[ComplianceTypeType]]
    NextToken: NotRequired[str]

class DescribeComplianceByResourceRequestTypeDef(TypedDict):
    ResourceType: NotRequired[str]
    ResourceId: NotRequired[str]
    ComplianceTypes: NotRequired[Sequence[ComplianceTypeType]]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeConfigRuleEvaluationStatusRequestTypeDef(TypedDict):
    ConfigRuleNames: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    Limit: NotRequired[int]

class DescribeConfigRulesFiltersTypeDef(TypedDict):
    EvaluationMode: NotRequired[EvaluationModeType]

class DescribeConfigurationAggregatorSourcesStatusRequestTypeDef(TypedDict):
    ConfigurationAggregatorName: str
    UpdateStatus: NotRequired[Sequence[AggregatedSourceStatusTypeType]]
    NextToken: NotRequired[str]
    Limit: NotRequired[int]

class DescribeConfigurationAggregatorsRequestTypeDef(TypedDict):
    ConfigurationAggregatorNames: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    Limit: NotRequired[int]

class DescribeConfigurationRecorderStatusRequestTypeDef(TypedDict):
    ConfigurationRecorderNames: NotRequired[Sequence[str]]
    ServicePrincipal: NotRequired[str]
    Arn: NotRequired[str]

class DescribeConfigurationRecordersRequestTypeDef(TypedDict):
    ConfigurationRecorderNames: NotRequired[Sequence[str]]
    ServicePrincipal: NotRequired[str]
    Arn: NotRequired[str]

class DescribeConformancePackStatusRequestTypeDef(TypedDict):
    ConformancePackNames: NotRequired[Sequence[str]]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeConformancePacksRequestTypeDef(TypedDict):
    ConformancePackNames: NotRequired[Sequence[str]]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeDeliveryChannelStatusRequestTypeDef(TypedDict):
    DeliveryChannelNames: NotRequired[Sequence[str]]

class DescribeDeliveryChannelsRequestTypeDef(TypedDict):
    DeliveryChannelNames: NotRequired[Sequence[str]]

class DescribeOrganizationConfigRuleStatusesRequestTypeDef(TypedDict):
    OrganizationConfigRuleNames: NotRequired[Sequence[str]]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class OrganizationConfigRuleStatusTypeDef(TypedDict):
    OrganizationConfigRuleName: str
    OrganizationRuleStatus: OrganizationRuleStatusType
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]
    LastUpdateTime: NotRequired[datetime]

class DescribeOrganizationConfigRulesRequestTypeDef(TypedDict):
    OrganizationConfigRuleNames: NotRequired[Sequence[str]]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeOrganizationConformancePackStatusesRequestTypeDef(TypedDict):
    OrganizationConformancePackNames: NotRequired[Sequence[str]]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class OrganizationConformancePackStatusTypeDef(TypedDict):
    OrganizationConformancePackName: str
    Status: OrganizationResourceStatusType
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]
    LastUpdateTime: NotRequired[datetime]

class DescribeOrganizationConformancePacksRequestTypeDef(TypedDict):
    OrganizationConformancePackNames: NotRequired[Sequence[str]]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class DescribePendingAggregationRequestsRequestTypeDef(TypedDict):
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class PendingAggregationRequestTypeDef(TypedDict):
    RequesterAccountId: NotRequired[str]
    RequesterAwsRegion: NotRequired[str]

class DescribeRemediationConfigurationsRequestTypeDef(TypedDict):
    ConfigRuleNames: Sequence[str]

class RemediationExceptionTypeDef(TypedDict):
    ConfigRuleName: str
    ResourceType: str
    ResourceId: str
    Message: NotRequired[str]
    ExpirationTime: NotRequired[datetime]

class DescribeRetentionConfigurationsRequestTypeDef(TypedDict):
    RetentionConfigurationNames: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]

class RetentionConfigurationTypeDef(TypedDict):
    Name: str
    RetentionPeriodInDays: int

class DisassociateResourceTypesRequestTypeDef(TypedDict):
    ConfigurationRecorderArn: str
    ResourceTypes: Sequence[ResourceTypeType]

class EvaluationContextTypeDef(TypedDict):
    EvaluationContextIdentifier: NotRequired[str]

class EvaluationOutputTypeDef(TypedDict):
    ComplianceResourceType: str
    ComplianceResourceId: str
    ComplianceType: ComplianceTypeType
    OrderingTimestamp: datetime
    Annotation: NotRequired[str]

class EvaluationResultQualifierTypeDef(TypedDict):
    ConfigRuleName: NotRequired[str]
    ResourceType: NotRequired[str]
    ResourceId: NotRequired[str]
    EvaluationMode: NotRequired[EvaluationModeType]

class EvaluationStatusTypeDef(TypedDict):
    Status: ResourceEvaluationStatusType
    FailureReason: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class ExclusionByResourceTypesOutputTypeDef(TypedDict):
    resourceTypes: NotRequired[List[ResourceTypeType]]

class ExclusionByResourceTypesTypeDef(TypedDict):
    resourceTypes: NotRequired[Sequence[ResourceTypeType]]

class SsmControlsTypeDef(TypedDict):
    ConcurrentExecutionRatePercentage: NotRequired[int]
    ErrorPercentage: NotRequired[int]

class FieldInfoTypeDef(TypedDict):
    Name: NotRequired[str]

class GetAggregateComplianceDetailsByConfigRuleRequestTypeDef(TypedDict):
    ConfigurationAggregatorName: str
    ConfigRuleName: str
    AccountId: str
    AwsRegion: str
    ComplianceType: NotRequired[ComplianceTypeType]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class ResourceCountFiltersTypeDef(TypedDict):
    ResourceType: NotRequired[ResourceTypeType]
    AccountId: NotRequired[str]
    Region: NotRequired[str]

class GroupedResourceCountTypeDef(TypedDict):
    GroupName: str
    ResourceCount: int

class GetComplianceDetailsByConfigRuleRequestTypeDef(TypedDict):
    ConfigRuleName: str
    ComplianceTypes: NotRequired[Sequence[ComplianceTypeType]]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class GetComplianceDetailsByResourceRequestTypeDef(TypedDict):
    ResourceType: NotRequired[str]
    ResourceId: NotRequired[str]
    ComplianceTypes: NotRequired[Sequence[ComplianceTypeType]]
    NextToken: NotRequired[str]
    ResourceEvaluationId: NotRequired[str]

class GetComplianceSummaryByResourceTypeRequestTypeDef(TypedDict):
    ResourceTypes: NotRequired[Sequence[str]]

class GetConformancePackComplianceSummaryRequestTypeDef(TypedDict):
    ConformancePackNames: Sequence[str]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class GetCustomRulePolicyRequestTypeDef(TypedDict):
    ConfigRuleName: NotRequired[str]

class GetDiscoveredResourceCountsRequestTypeDef(TypedDict):
    resourceTypes: NotRequired[Sequence[str]]
    limit: NotRequired[int]
    nextToken: NotRequired[str]

class ResourceCountTypeDef(TypedDict):
    resourceType: NotRequired[ResourceTypeType]
    count: NotRequired[int]

class StatusDetailFiltersTypeDef(TypedDict):
    AccountId: NotRequired[str]
    MemberAccountRuleStatus: NotRequired[MemberAccountRuleStatusType]

class MemberAccountStatusTypeDef(TypedDict):
    AccountId: str
    ConfigRuleName: str
    MemberAccountRuleStatus: MemberAccountRuleStatusType
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]
    LastUpdateTime: NotRequired[datetime]

class OrganizationResourceDetailedStatusFiltersTypeDef(TypedDict):
    AccountId: NotRequired[str]
    Status: NotRequired[OrganizationResourceDetailedStatusType]

class OrganizationConformancePackDetailedStatusTypeDef(TypedDict):
    AccountId: str
    ConformancePackName: str
    Status: OrganizationResourceDetailedStatusType
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]
    LastUpdateTime: NotRequired[datetime]

class GetOrganizationCustomRulePolicyRequestTypeDef(TypedDict):
    OrganizationConfigRuleName: str

class GetResourceEvaluationSummaryRequestTypeDef(TypedDict):
    ResourceEvaluationId: str

class ResourceDetailsTypeDef(TypedDict):
    ResourceId: str
    ResourceType: str
    ResourceConfiguration: str
    ResourceConfigurationSchemaType: NotRequired[Literal["CFN_RESOURCE_SCHEMA"]]

class GetStoredQueryRequestTypeDef(TypedDict):
    QueryName: str

class StoredQueryTypeDef(TypedDict):
    QueryName: str
    QueryId: NotRequired[str]
    QueryArn: NotRequired[str]
    Description: NotRequired[str]
    Expression: NotRequired[str]

class ResourceFiltersTypeDef(TypedDict):
    AccountId: NotRequired[str]
    ResourceId: NotRequired[str]
    ResourceName: NotRequired[str]
    Region: NotRequired[str]

class ListDiscoveredResourcesRequestTypeDef(TypedDict):
    resourceType: ResourceTypeType
    resourceIds: NotRequired[Sequence[str]]
    resourceName: NotRequired[str]
    limit: NotRequired[int]
    includeDeletedResources: NotRequired[bool]
    nextToken: NotRequired[str]

class ResourceIdentifierTypeDef(TypedDict):
    resourceType: NotRequired[ResourceTypeType]
    resourceId: NotRequired[str]
    resourceName: NotRequired[str]
    resourceDeletionTime: NotRequired[datetime]

class ResourceEvaluationTypeDef(TypedDict):
    ResourceEvaluationId: NotRequired[str]
    EvaluationMode: NotRequired[EvaluationModeType]
    EvaluationStartTimestamp: NotRequired[datetime]

class ListStoredQueriesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class StoredQueryMetadataTypeDef(TypedDict):
    QueryId: str
    QueryArn: str
    QueryName: str
    Description: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class OrganizationAggregationSourceTypeDef(TypedDict):
    RoleArn: str
    AwsRegions: NotRequired[Sequence[str]]
    AllAwsRegions: NotRequired[bool]

class OrganizationCustomPolicyRuleMetadataNoPolicyTypeDef(TypedDict):
    Description: NotRequired[str]
    OrganizationConfigRuleTriggerTypes: NotRequired[List[OrganizationConfigRuleTriggerTypeNoSNType]]
    InputParameters: NotRequired[str]
    MaximumExecutionFrequency: NotRequired[MaximumExecutionFrequencyType]
    ResourceTypesScope: NotRequired[List[str]]
    ResourceIdScope: NotRequired[str]
    TagKeyScope: NotRequired[str]
    TagValueScope: NotRequired[str]
    PolicyRuntime: NotRequired[str]
    DebugLogDeliveryAccounts: NotRequired[List[str]]

class OrganizationCustomRuleMetadataOutputTypeDef(TypedDict):
    LambdaFunctionArn: str
    OrganizationConfigRuleTriggerTypes: List[OrganizationConfigRuleTriggerTypeType]
    Description: NotRequired[str]
    InputParameters: NotRequired[str]
    MaximumExecutionFrequency: NotRequired[MaximumExecutionFrequencyType]
    ResourceTypesScope: NotRequired[List[str]]
    ResourceIdScope: NotRequired[str]
    TagKeyScope: NotRequired[str]
    TagValueScope: NotRequired[str]

class OrganizationManagedRuleMetadataOutputTypeDef(TypedDict):
    RuleIdentifier: str
    Description: NotRequired[str]
    InputParameters: NotRequired[str]
    MaximumExecutionFrequency: NotRequired[MaximumExecutionFrequencyType]
    ResourceTypesScope: NotRequired[List[str]]
    ResourceIdScope: NotRequired[str]
    TagKeyScope: NotRequired[str]
    TagValueScope: NotRequired[str]

class OrganizationCustomPolicyRuleMetadataTypeDef(TypedDict):
    PolicyRuntime: str
    PolicyText: str
    Description: NotRequired[str]
    OrganizationConfigRuleTriggerTypes: NotRequired[
        Sequence[OrganizationConfigRuleTriggerTypeNoSNType]
    ]
    InputParameters: NotRequired[str]
    MaximumExecutionFrequency: NotRequired[MaximumExecutionFrequencyType]
    ResourceTypesScope: NotRequired[Sequence[str]]
    ResourceIdScope: NotRequired[str]
    TagKeyScope: NotRequired[str]
    TagValueScope: NotRequired[str]
    DebugLogDeliveryAccounts: NotRequired[Sequence[str]]

class OrganizationCustomRuleMetadataTypeDef(TypedDict):
    LambdaFunctionArn: str
    OrganizationConfigRuleTriggerTypes: Sequence[OrganizationConfigRuleTriggerTypeType]
    Description: NotRequired[str]
    InputParameters: NotRequired[str]
    MaximumExecutionFrequency: NotRequired[MaximumExecutionFrequencyType]
    ResourceTypesScope: NotRequired[Sequence[str]]
    ResourceIdScope: NotRequired[str]
    TagKeyScope: NotRequired[str]
    TagValueScope: NotRequired[str]

class OrganizationManagedRuleMetadataTypeDef(TypedDict):
    RuleIdentifier: str
    Description: NotRequired[str]
    InputParameters: NotRequired[str]
    MaximumExecutionFrequency: NotRequired[MaximumExecutionFrequencyType]
    ResourceTypesScope: NotRequired[Sequence[str]]
    ResourceIdScope: NotRequired[str]
    TagKeyScope: NotRequired[str]
    TagValueScope: NotRequired[str]

class PutResourceConfigRequestTypeDef(TypedDict):
    ResourceType: str
    SchemaVersionId: str
    ResourceId: str
    Configuration: str
    ResourceName: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class PutRetentionConfigurationRequestTypeDef(TypedDict):
    RetentionPeriodInDays: int

class RecordingStrategyTypeDef(TypedDict):
    useOnly: NotRequired[RecordingStrategyTypeType]

class RecordingModeOverrideOutputTypeDef(TypedDict):
    resourceTypes: List[ResourceTypeType]
    recordingFrequency: RecordingFrequencyType
    description: NotRequired[str]

class RecordingModeOverrideTypeDef(TypedDict):
    resourceTypes: Sequence[ResourceTypeType]
    recordingFrequency: RecordingFrequencyType
    description: NotRequired[str]

class RemediationExecutionStepTypeDef(TypedDict):
    Name: NotRequired[str]
    State: NotRequired[RemediationExecutionStepStateType]
    ErrorMessage: NotRequired[str]
    StartTime: NotRequired[datetime]
    StopTime: NotRequired[datetime]

class ResourceValueTypeDef(TypedDict):
    Value: Literal["RESOURCE_ID"]

class StaticValueOutputTypeDef(TypedDict):
    Values: List[str]

class SelectAggregateResourceConfigRequestTypeDef(TypedDict):
    Expression: str
    ConfigurationAggregatorName: str
    Limit: NotRequired[int]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class SelectResourceConfigRequestTypeDef(TypedDict):
    Expression: str
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class SourceDetailTypeDef(TypedDict):
    EventSource: NotRequired[Literal["aws.config"]]
    MessageType: NotRequired[MessageTypeType]
    MaximumExecutionFrequency: NotRequired[MaximumExecutionFrequencyType]

class StartConfigRulesEvaluationRequestTypeDef(TypedDict):
    ConfigRuleNames: NotRequired[Sequence[str]]

class StartConfigurationRecorderRequestTypeDef(TypedDict):
    ConfigurationRecorderName: str

class StaticValueTypeDef(TypedDict):
    Values: Sequence[str]

class StopConfigurationRecorderRequestTypeDef(TypedDict):
    ConfigurationRecorderName: str

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

AccountAggregationSourceUnionTypeDef = Union[
    AccountAggregationSourceTypeDef, AccountAggregationSourceOutputTypeDef
]

class AggregateComplianceByConformancePackTypeDef(TypedDict):
    ConformancePackName: NotRequired[str]
    Compliance: NotRequired[AggregateConformancePackComplianceTypeDef]
    AccountId: NotRequired[str]
    AwsRegion: NotRequired[str]

class AggregateConformancePackComplianceSummaryTypeDef(TypedDict):
    ComplianceSummary: NotRequired[AggregateConformancePackComplianceCountTypeDef]
    GroupName: NotRequired[str]

class DescribeAggregateComplianceByConformancePacksRequestTypeDef(TypedDict):
    ConfigurationAggregatorName: str
    Filters: NotRequired[AggregateConformancePackComplianceFiltersTypeDef]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class GetAggregateConformancePackComplianceSummaryRequestTypeDef(TypedDict):
    ConfigurationAggregatorName: str
    Filters: NotRequired[AggregateConformancePackComplianceSummaryFiltersTypeDef]
    GroupByKey: NotRequired[AggregateConformancePackComplianceSummaryGroupKeyType]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class BatchGetAggregateResourceConfigRequestTypeDef(TypedDict):
    ConfigurationAggregatorName: str
    ResourceIdentifiers: Sequence[AggregateResourceIdentifierTypeDef]

class GetAggregateResourceConfigRequestTypeDef(TypedDict):
    ConfigurationAggregatorName: str
    ResourceIdentifier: AggregateResourceIdentifierTypeDef

class AggregatorFiltersOutputTypeDef(TypedDict):
    ResourceType: NotRequired[AggregatorFilterResourceTypeOutputTypeDef]
    ServicePrincipal: NotRequired[AggregatorFilterServicePrincipalOutputTypeDef]

class AggregatorFiltersTypeDef(TypedDict):
    ResourceType: NotRequired[AggregatorFilterResourceTypeTypeDef]
    ServicePrincipal: NotRequired[AggregatorFilterServicePrincipalTypeDef]

class DeleteServiceLinkedConfigurationRecorderResponseTypeDef(TypedDict):
    Arn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeliverConfigSnapshotResponseTypeDef(TypedDict):
    configSnapshotId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAggregationAuthorizationsResponseTypeDef(TypedDict):
    AggregationAuthorizations: List[AggregationAuthorizationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeConfigurationAggregatorSourcesStatusResponseTypeDef(TypedDict):
    AggregatedSourceStatusList: List[AggregatedSourceStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetCustomRulePolicyResponseTypeDef(TypedDict):
    PolicyText: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetOrganizationCustomRulePolicyResponseTypeDef(TypedDict):
    PolicyText: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAggregateDiscoveredResourcesResponseTypeDef(TypedDict):
    ResourceIdentifiers: List[AggregateResourceIdentifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PutAggregationAuthorizationResponseTypeDef(TypedDict):
    AggregationAuthorization: AggregationAuthorizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutConformancePackResponseTypeDef(TypedDict):
    ConformancePackArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutOrganizationConfigRuleResponseTypeDef(TypedDict):
    OrganizationConfigRuleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutOrganizationConformancePackResponseTypeDef(TypedDict):
    OrganizationConformancePackArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutServiceLinkedConfigurationRecorderResponseTypeDef(TypedDict):
    Arn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutStoredQueryResponseTypeDef(TypedDict):
    QueryArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartResourceEvaluationResponseTypeDef(TypedDict):
    ResourceEvaluationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetAggregateResourceConfigResponseTypeDef(TypedDict):
    BaseConfigurationItems: List[BaseConfigurationItemTypeDef]
    UnprocessedResourceIdentifiers: List[AggregateResourceIdentifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetResourceConfigRequestTypeDef(TypedDict):
    resourceKeys: Sequence[ResourceKeyTypeDef]

class BatchGetResourceConfigResponseTypeDef(TypedDict):
    baseConfigurationItems: List[BaseConfigurationItemTypeDef]
    unprocessedResourceKeys: List[ResourceKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRemediationExecutionStatusRequestTypeDef(TypedDict):
    ConfigRuleName: str
    ResourceKeys: NotRequired[Sequence[ResourceKeyTypeDef]]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class StartRemediationExecutionRequestTypeDef(TypedDict):
    ConfigRuleName: str
    ResourceKeys: Sequence[ResourceKeyTypeDef]

class StartRemediationExecutionResponseTypeDef(TypedDict):
    FailureMessage: str
    FailedItems: List[ResourceKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ComplianceSummaryTypeDef(TypedDict):
    CompliantResourceCount: NotRequired[ComplianceContributorCountTypeDef]
    NonCompliantResourceCount: NotRequired[ComplianceContributorCountTypeDef]
    ComplianceSummaryTimestamp: NotRequired[datetime]

class ComplianceTypeDef(TypedDict):
    ComplianceType: NotRequired[ComplianceTypeType]
    ComplianceContributorCount: NotRequired[ComplianceContributorCountTypeDef]

class DescribeAggregateComplianceByConfigRulesRequestTypeDef(TypedDict):
    ConfigurationAggregatorName: str
    Filters: NotRequired[ConfigRuleComplianceFiltersTypeDef]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class GetAggregateConfigRuleComplianceSummaryRequestTypeDef(TypedDict):
    ConfigurationAggregatorName: str
    Filters: NotRequired[ConfigRuleComplianceSummaryFiltersTypeDef]
    GroupByKey: NotRequired[ConfigRuleComplianceSummaryGroupKeyType]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeConfigRuleEvaluationStatusResponseTypeDef(TypedDict):
    ConfigRulesEvaluationStatus: List[ConfigRuleEvaluationStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DeliveryChannelTypeDef(TypedDict):
    name: NotRequired[str]
    s3BucketName: NotRequired[str]
    s3KeyPrefix: NotRequired[str]
    s3KmsKeyArn: NotRequired[str]
    snsTopicARN: NotRequired[str]
    configSnapshotDeliveryProperties: NotRequired[ConfigSnapshotDeliveryPropertiesTypeDef]

class DeliveryChannelStatusTypeDef(TypedDict):
    name: NotRequired[str]
    configSnapshotDeliveryInfo: NotRequired[ConfigExportDeliveryInfoTypeDef]
    configHistoryDeliveryInfo: NotRequired[ConfigExportDeliveryInfoTypeDef]
    configStreamDeliveryInfo: NotRequired[ConfigStreamDeliveryInfoTypeDef]

class ConfigurationItemTypeDef(TypedDict):
    version: NotRequired[str]
    accountId: NotRequired[str]
    configurationItemCaptureTime: NotRequired[datetime]
    configurationItemStatus: NotRequired[ConfigurationItemStatusType]
    configurationStateId: NotRequired[str]
    configurationItemMD5Hash: NotRequired[str]
    arn: NotRequired[str]
    resourceType: NotRequired[ResourceTypeType]
    resourceId: NotRequired[str]
    resourceName: NotRequired[str]
    awsRegion: NotRequired[str]
    availabilityZone: NotRequired[str]
    resourceCreationTime: NotRequired[datetime]
    tags: NotRequired[Dict[str, str]]
    relatedEvents: NotRequired[List[str]]
    relationships: NotRequired[List[RelationshipTypeDef]]
    configuration: NotRequired[str]
    supplementaryConfiguration: NotRequired[Dict[str, str]]
    recordingFrequency: NotRequired[RecordingFrequencyType]
    configurationItemDeliveryTime: NotRequired[datetime]

class ListConfigurationRecordersRequestTypeDef(TypedDict):
    Filters: NotRequired[Sequence[ConfigurationRecorderFilterTypeDef]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeConfigurationRecorderStatusResponseTypeDef(TypedDict):
    ConfigurationRecordersStatus: List[ConfigurationRecorderStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfigurationRecordersResponseTypeDef(TypedDict):
    ConfigurationRecorderSummaries: List[ConfigurationRecorderSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeConformancePackComplianceRequestTypeDef(TypedDict):
    ConformancePackName: str
    Filters: NotRequired[ConformancePackComplianceFiltersTypeDef]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class ListConformancePackComplianceScoresResponseTypeDef(TypedDict):
    ConformancePackComplianceScores: List[ConformancePackComplianceScoreTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListConformancePackComplianceScoresRequestTypeDef(TypedDict):
    Filters: NotRequired[ConformancePackComplianceScoresFiltersTypeDef]
    SortOrder: NotRequired[SortOrderType]
    SortBy: NotRequired[Literal["SCORE"]]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class GetConformancePackComplianceSummaryResponseTypeDef(TypedDict):
    ConformancePackComplianceSummaryList: List[ConformancePackComplianceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class OrganizationConformancePackTypeDef(TypedDict):
    OrganizationConformancePackName: str
    OrganizationConformancePackArn: str
    LastUpdateTime: datetime
    DeliveryS3Bucket: NotRequired[str]
    DeliveryS3KeyPrefix: NotRequired[str]
    ConformancePackInputParameters: NotRequired[List[ConformancePackInputParameterTypeDef]]
    ExcludedAccounts: NotRequired[List[str]]

class PutOrganizationConformancePackRequestTypeDef(TypedDict):
    OrganizationConformancePackName: str
    TemplateS3Uri: NotRequired[str]
    TemplateBody: NotRequired[str]
    DeliveryS3Bucket: NotRequired[str]
    DeliveryS3KeyPrefix: NotRequired[str]
    ConformancePackInputParameters: NotRequired[Sequence[ConformancePackInputParameterTypeDef]]
    ExcludedAccounts: NotRequired[Sequence[str]]

class ConformancePackDetailTypeDef(TypedDict):
    ConformancePackName: str
    ConformancePackArn: str
    ConformancePackId: str
    DeliveryS3Bucket: NotRequired[str]
    DeliveryS3KeyPrefix: NotRequired[str]
    ConformancePackInputParameters: NotRequired[List[ConformancePackInputParameterTypeDef]]
    LastUpdateRequestedTime: NotRequired[datetime]
    CreatedBy: NotRequired[str]
    TemplateSSMDocumentDetails: NotRequired[TemplateSSMDocumentDetailsTypeDef]

class PutConformancePackRequestTypeDef(TypedDict):
    ConformancePackName: str
    TemplateS3Uri: NotRequired[str]
    TemplateBody: NotRequired[str]
    DeliveryS3Bucket: NotRequired[str]
    DeliveryS3KeyPrefix: NotRequired[str]
    ConformancePackInputParameters: NotRequired[Sequence[ConformancePackInputParameterTypeDef]]
    TemplateSSMDocumentDetails: NotRequired[TemplateSSMDocumentDetailsTypeDef]

class GetConformancePackComplianceDetailsRequestTypeDef(TypedDict):
    ConformancePackName: str
    Filters: NotRequired[ConformancePackEvaluationFiltersTypeDef]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeConformancePackComplianceResponseTypeDef(TypedDict):
    ConformancePackName: str
    ConformancePackRuleComplianceList: List[ConformancePackRuleComplianceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeConformancePackStatusResponseTypeDef(TypedDict):
    ConformancePackStatusDetails: List[ConformancePackStatusDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DeleteRemediationExceptionsRequestTypeDef(TypedDict):
    ConfigRuleName: str
    ResourceKeys: Sequence[RemediationExceptionResourceKeyTypeDef]

class DescribeRemediationExceptionsRequestTypeDef(TypedDict):
    ConfigRuleName: str
    ResourceKeys: NotRequired[Sequence[RemediationExceptionResourceKeyTypeDef]]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class FailedDeleteRemediationExceptionsBatchTypeDef(TypedDict):
    FailureMessage: NotRequired[str]
    FailedItems: NotRequired[List[RemediationExceptionResourceKeyTypeDef]]

class DescribeAggregateComplianceByConfigRulesRequestPaginateTypeDef(TypedDict):
    ConfigurationAggregatorName: str
    Filters: NotRequired[ConfigRuleComplianceFiltersTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeAggregateComplianceByConformancePacksRequestPaginateTypeDef(TypedDict):
    ConfigurationAggregatorName: str
    Filters: NotRequired[AggregateConformancePackComplianceFiltersTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeAggregationAuthorizationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeComplianceByConfigRuleRequestPaginateTypeDef(TypedDict):
    ConfigRuleNames: NotRequired[Sequence[str]]
    ComplianceTypes: NotRequired[Sequence[ComplianceTypeType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeComplianceByResourceRequestPaginateTypeDef(TypedDict):
    ResourceType: NotRequired[str]
    ResourceId: NotRequired[str]
    ComplianceTypes: NotRequired[Sequence[ComplianceTypeType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeConfigRuleEvaluationStatusRequestPaginateTypeDef(TypedDict):
    ConfigRuleNames: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeConfigurationAggregatorSourcesStatusRequestPaginateTypeDef(TypedDict):
    ConfigurationAggregatorName: str
    UpdateStatus: NotRequired[Sequence[AggregatedSourceStatusTypeType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeConfigurationAggregatorsRequestPaginateTypeDef(TypedDict):
    ConfigurationAggregatorNames: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeConformancePackStatusRequestPaginateTypeDef(TypedDict):
    ConformancePackNames: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeConformancePacksRequestPaginateTypeDef(TypedDict):
    ConformancePackNames: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeOrganizationConfigRuleStatusesRequestPaginateTypeDef(TypedDict):
    OrganizationConfigRuleNames: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeOrganizationConfigRulesRequestPaginateTypeDef(TypedDict):
    OrganizationConfigRuleNames: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeOrganizationConformancePackStatusesRequestPaginateTypeDef(TypedDict):
    OrganizationConformancePackNames: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeOrganizationConformancePacksRequestPaginateTypeDef(TypedDict):
    OrganizationConformancePackNames: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribePendingAggregationRequestsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeRemediationExecutionStatusRequestPaginateTypeDef(TypedDict):
    ConfigRuleName: str
    ResourceKeys: NotRequired[Sequence[ResourceKeyTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeRetentionConfigurationsRequestPaginateTypeDef(TypedDict):
    RetentionConfigurationNames: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetAggregateComplianceDetailsByConfigRuleRequestPaginateTypeDef(TypedDict):
    ConfigurationAggregatorName: str
    ConfigRuleName: str
    AccountId: str
    AwsRegion: str
    ComplianceType: NotRequired[ComplianceTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetComplianceDetailsByConfigRuleRequestPaginateTypeDef(TypedDict):
    ConfigRuleName: str
    ComplianceTypes: NotRequired[Sequence[ComplianceTypeType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetComplianceDetailsByResourceRequestPaginateTypeDef(TypedDict):
    ResourceType: NotRequired[str]
    ResourceId: NotRequired[str]
    ComplianceTypes: NotRequired[Sequence[ComplianceTypeType]]
    ResourceEvaluationId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetConformancePackComplianceSummaryRequestPaginateTypeDef(TypedDict):
    ConformancePackNames: Sequence[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListConfigurationRecordersRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[ConfigurationRecorderFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDiscoveredResourcesRequestPaginateTypeDef(TypedDict):
    resourceType: ResourceTypeType
    resourceIds: NotRequired[Sequence[str]]
    resourceName: NotRequired[str]
    includeDeletedResources: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsForResourceRequestPaginateTypeDef(TypedDict):
    ResourceArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SelectAggregateResourceConfigRequestPaginateTypeDef(TypedDict):
    Expression: str
    ConfigurationAggregatorName: str
    MaxResults: NotRequired[int]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SelectResourceConfigRequestPaginateTypeDef(TypedDict):
    Expression: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeConfigRulesRequestPaginateTypeDef(TypedDict):
    ConfigRuleNames: NotRequired[Sequence[str]]
    Filters: NotRequired[DescribeConfigRulesFiltersTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeConfigRulesRequestTypeDef(TypedDict):
    ConfigRuleNames: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    Filters: NotRequired[DescribeConfigRulesFiltersTypeDef]

class DescribeOrganizationConfigRuleStatusesResponseTypeDef(TypedDict):
    OrganizationConfigRuleStatuses: List[OrganizationConfigRuleStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeOrganizationConformancePackStatusesResponseTypeDef(TypedDict):
    OrganizationConformancePackStatuses: List[OrganizationConformancePackStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribePendingAggregationRequestsResponseTypeDef(TypedDict):
    PendingAggregationRequests: List[PendingAggregationRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeRemediationExceptionsResponseTypeDef(TypedDict):
    RemediationExceptions: List[RemediationExceptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class FailedRemediationExceptionBatchTypeDef(TypedDict):
    FailureMessage: NotRequired[str]
    FailedItems: NotRequired[List[RemediationExceptionTypeDef]]

class DescribeRetentionConfigurationsResponseTypeDef(TypedDict):
    RetentionConfigurations: List[RetentionConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PutRetentionConfigurationResponseTypeDef(TypedDict):
    RetentionConfiguration: RetentionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutEvaluationsResponseTypeDef(TypedDict):
    FailedEvaluations: List[EvaluationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EvaluationResultIdentifierTypeDef(TypedDict):
    EvaluationResultQualifier: NotRequired[EvaluationResultQualifierTypeDef]
    OrderingTimestamp: NotRequired[datetime]
    ResourceEvaluationId: NotRequired[str]

class EvaluationTypeDef(TypedDict):
    ComplianceResourceType: str
    ComplianceResourceId: str
    ComplianceType: ComplianceTypeType
    OrderingTimestamp: TimestampTypeDef
    Annotation: NotRequired[str]

class ExternalEvaluationTypeDef(TypedDict):
    ComplianceResourceType: str
    ComplianceResourceId: str
    ComplianceType: ComplianceTypeType
    OrderingTimestamp: TimestampTypeDef
    Annotation: NotRequired[str]

class GetResourceConfigHistoryRequestPaginateTypeDef(TypedDict):
    resourceType: ResourceTypeType
    resourceId: str
    laterTime: NotRequired[TimestampTypeDef]
    earlierTime: NotRequired[TimestampTypeDef]
    chronologicalOrder: NotRequired[ChronologicalOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetResourceConfigHistoryRequestTypeDef(TypedDict):
    resourceType: ResourceTypeType
    resourceId: str
    laterTime: NotRequired[TimestampTypeDef]
    earlierTime: NotRequired[TimestampTypeDef]
    chronologicalOrder: NotRequired[ChronologicalOrderType]
    limit: NotRequired[int]
    nextToken: NotRequired[str]

class PutRemediationExceptionsRequestTypeDef(TypedDict):
    ConfigRuleName: str
    ResourceKeys: Sequence[RemediationExceptionResourceKeyTypeDef]
    Message: NotRequired[str]
    ExpirationTime: NotRequired[TimestampTypeDef]

class TimeWindowTypeDef(TypedDict):
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]

class ExecutionControlsTypeDef(TypedDict):
    SsmControls: NotRequired[SsmControlsTypeDef]

class QueryInfoTypeDef(TypedDict):
    SelectFields: NotRequired[List[FieldInfoTypeDef]]

class GetAggregateDiscoveredResourceCountsRequestTypeDef(TypedDict):
    ConfigurationAggregatorName: str
    Filters: NotRequired[ResourceCountFiltersTypeDef]
    GroupByKey: NotRequired[ResourceCountGroupKeyType]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class GetAggregateDiscoveredResourceCountsResponseTypeDef(TypedDict):
    TotalDiscoveredResources: int
    GroupByKey: str
    GroupedResourceCounts: List[GroupedResourceCountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetDiscoveredResourceCountsResponseTypeDef(TypedDict):
    totalDiscoveredResources: int
    resourceCounts: List[ResourceCountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetOrganizationConfigRuleDetailedStatusRequestPaginateTypeDef(TypedDict):
    OrganizationConfigRuleName: str
    Filters: NotRequired[StatusDetailFiltersTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetOrganizationConfigRuleDetailedStatusRequestTypeDef(TypedDict):
    OrganizationConfigRuleName: str
    Filters: NotRequired[StatusDetailFiltersTypeDef]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class GetOrganizationConfigRuleDetailedStatusResponseTypeDef(TypedDict):
    OrganizationConfigRuleDetailedStatus: List[MemberAccountStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetOrganizationConformancePackDetailedStatusRequestPaginateTypeDef(TypedDict):
    OrganizationConformancePackName: str
    Filters: NotRequired[OrganizationResourceDetailedStatusFiltersTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetOrganizationConformancePackDetailedStatusRequestTypeDef(TypedDict):
    OrganizationConformancePackName: str
    Filters: NotRequired[OrganizationResourceDetailedStatusFiltersTypeDef]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class GetOrganizationConformancePackDetailedStatusResponseTypeDef(TypedDict):
    OrganizationConformancePackDetailedStatuses: List[
        OrganizationConformancePackDetailedStatusTypeDef
    ]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetResourceEvaluationSummaryResponseTypeDef(TypedDict):
    ResourceEvaluationId: str
    EvaluationMode: EvaluationModeType
    EvaluationStatus: EvaluationStatusTypeDef
    EvaluationStartTimestamp: datetime
    Compliance: ComplianceTypeType
    EvaluationContext: EvaluationContextTypeDef
    ResourceDetails: ResourceDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartResourceEvaluationRequestTypeDef(TypedDict):
    ResourceDetails: ResourceDetailsTypeDef
    EvaluationMode: EvaluationModeType
    EvaluationContext: NotRequired[EvaluationContextTypeDef]
    EvaluationTimeout: NotRequired[int]
    ClientToken: NotRequired[str]

class GetStoredQueryResponseTypeDef(TypedDict):
    StoredQuery: StoredQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAggregateDiscoveredResourcesRequestPaginateTypeDef(TypedDict):
    ConfigurationAggregatorName: str
    ResourceType: ResourceTypeType
    Filters: NotRequired[ResourceFiltersTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAggregateDiscoveredResourcesRequestTypeDef(TypedDict):
    ConfigurationAggregatorName: str
    ResourceType: ResourceTypeType
    Filters: NotRequired[ResourceFiltersTypeDef]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class ListDiscoveredResourcesResponseTypeDef(TypedDict):
    resourceIdentifiers: List[ResourceIdentifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListResourceEvaluationsResponseTypeDef(TypedDict):
    ResourceEvaluations: List[ResourceEvaluationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListStoredQueriesResponseTypeDef(TypedDict):
    StoredQueryMetadata: List[StoredQueryMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PutAggregationAuthorizationRequestTypeDef(TypedDict):
    AuthorizedAccountId: str
    AuthorizedAwsRegion: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class PutServiceLinkedConfigurationRecorderRequestTypeDef(TypedDict):
    ServicePrincipal: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class PutStoredQueryRequestTypeDef(TypedDict):
    StoredQuery: StoredQueryTypeDef
    Tags: NotRequired[Sequence[TagTypeDef]]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

OrganizationAggregationSourceUnionTypeDef = Union[
    OrganizationAggregationSourceTypeDef, OrganizationAggregationSourceOutputTypeDef
]

class OrganizationConfigRuleTypeDef(TypedDict):
    OrganizationConfigRuleName: str
    OrganizationConfigRuleArn: str
    OrganizationManagedRuleMetadata: NotRequired[OrganizationManagedRuleMetadataOutputTypeDef]
    OrganizationCustomRuleMetadata: NotRequired[OrganizationCustomRuleMetadataOutputTypeDef]
    ExcludedAccounts: NotRequired[List[str]]
    LastUpdateTime: NotRequired[datetime]
    OrganizationCustomPolicyRuleMetadata: NotRequired[
        OrganizationCustomPolicyRuleMetadataNoPolicyTypeDef
    ]

OrganizationCustomRuleMetadataUnionTypeDef = Union[
    OrganizationCustomRuleMetadataTypeDef, OrganizationCustomRuleMetadataOutputTypeDef
]
OrganizationManagedRuleMetadataUnionTypeDef = Union[
    OrganizationManagedRuleMetadataTypeDef, OrganizationManagedRuleMetadataOutputTypeDef
]

class RecordingGroupOutputTypeDef(TypedDict):
    allSupported: NotRequired[bool]
    includeGlobalResourceTypes: NotRequired[bool]
    resourceTypes: NotRequired[List[ResourceTypeType]]
    exclusionByResourceTypes: NotRequired[ExclusionByResourceTypesOutputTypeDef]
    recordingStrategy: NotRequired[RecordingStrategyTypeDef]

class RecordingGroupTypeDef(TypedDict):
    allSupported: NotRequired[bool]
    includeGlobalResourceTypes: NotRequired[bool]
    resourceTypes: NotRequired[Sequence[ResourceTypeType]]
    exclusionByResourceTypes: NotRequired[ExclusionByResourceTypesTypeDef]
    recordingStrategy: NotRequired[RecordingStrategyTypeDef]

class RecordingModeOutputTypeDef(TypedDict):
    recordingFrequency: RecordingFrequencyType
    recordingModeOverrides: NotRequired[List[RecordingModeOverrideOutputTypeDef]]

class RecordingModeTypeDef(TypedDict):
    recordingFrequency: RecordingFrequencyType
    recordingModeOverrides: NotRequired[Sequence[RecordingModeOverrideTypeDef]]

class RemediationExecutionStatusTypeDef(TypedDict):
    ResourceKey: NotRequired[ResourceKeyTypeDef]
    State: NotRequired[RemediationExecutionStateType]
    StepDetails: NotRequired[List[RemediationExecutionStepTypeDef]]
    InvocationTime: NotRequired[datetime]
    LastUpdatedTime: NotRequired[datetime]

class RemediationParameterValueOutputTypeDef(TypedDict):
    ResourceValue: NotRequired[ResourceValueTypeDef]
    StaticValue: NotRequired[StaticValueOutputTypeDef]

class SourceOutputTypeDef(TypedDict):
    Owner: OwnerType
    SourceIdentifier: NotRequired[str]
    SourceDetails: NotRequired[List[SourceDetailTypeDef]]
    CustomPolicyDetails: NotRequired[CustomPolicyDetailsTypeDef]

class SourceTypeDef(TypedDict):
    Owner: OwnerType
    SourceIdentifier: NotRequired[str]
    SourceDetails: NotRequired[Sequence[SourceDetailTypeDef]]
    CustomPolicyDetails: NotRequired[CustomPolicyDetailsTypeDef]

StaticValueUnionTypeDef = Union[StaticValueTypeDef, StaticValueOutputTypeDef]

class DescribeAggregateComplianceByConformancePacksResponseTypeDef(TypedDict):
    AggregateComplianceByConformancePacks: List[AggregateComplianceByConformancePackTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetAggregateConformancePackComplianceSummaryResponseTypeDef(TypedDict):
    AggregateConformancePackComplianceSummaries: List[
        AggregateConformancePackComplianceSummaryTypeDef
    ]
    GroupByKey: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ConfigurationAggregatorTypeDef(TypedDict):
    ConfigurationAggregatorName: NotRequired[str]
    ConfigurationAggregatorArn: NotRequired[str]
    AccountAggregationSources: NotRequired[List[AccountAggregationSourceOutputTypeDef]]
    OrganizationAggregationSource: NotRequired[OrganizationAggregationSourceOutputTypeDef]
    CreationTime: NotRequired[datetime]
    LastUpdatedTime: NotRequired[datetime]
    CreatedBy: NotRequired[str]
    AggregatorFilters: NotRequired[AggregatorFiltersOutputTypeDef]

AggregatorFiltersUnionTypeDef = Union[AggregatorFiltersTypeDef, AggregatorFiltersOutputTypeDef]

class AggregateComplianceCountTypeDef(TypedDict):
    GroupName: NotRequired[str]
    ComplianceSummary: NotRequired[ComplianceSummaryTypeDef]

class ComplianceSummaryByResourceTypeTypeDef(TypedDict):
    ResourceType: NotRequired[str]
    ComplianceSummary: NotRequired[ComplianceSummaryTypeDef]

class GetComplianceSummaryByConfigRuleResponseTypeDef(TypedDict):
    ComplianceSummary: ComplianceSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AggregateComplianceByConfigRuleTypeDef(TypedDict):
    ConfigRuleName: NotRequired[str]
    Compliance: NotRequired[ComplianceTypeDef]
    AccountId: NotRequired[str]
    AwsRegion: NotRequired[str]

class ComplianceByConfigRuleTypeDef(TypedDict):
    ConfigRuleName: NotRequired[str]
    Compliance: NotRequired[ComplianceTypeDef]

class ComplianceByResourceTypeDef(TypedDict):
    ResourceType: NotRequired[str]
    ResourceId: NotRequired[str]
    Compliance: NotRequired[ComplianceTypeDef]

class DescribeDeliveryChannelsResponseTypeDef(TypedDict):
    DeliveryChannels: List[DeliveryChannelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutDeliveryChannelRequestTypeDef(TypedDict):
    DeliveryChannel: DeliveryChannelTypeDef

class DescribeDeliveryChannelStatusResponseTypeDef(TypedDict):
    DeliveryChannelsStatus: List[DeliveryChannelStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetAggregateResourceConfigResponseTypeDef(TypedDict):
    ConfigurationItem: ConfigurationItemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceConfigHistoryResponseTypeDef(TypedDict):
    configurationItems: List[ConfigurationItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeOrganizationConformancePacksResponseTypeDef(TypedDict):
    OrganizationConformancePacks: List[OrganizationConformancePackTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeConformancePacksResponseTypeDef(TypedDict):
    ConformancePackDetails: List[ConformancePackDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DeleteRemediationExceptionsResponseTypeDef(TypedDict):
    FailedBatches: List[FailedDeleteRemediationExceptionsBatchTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutRemediationExceptionsResponseTypeDef(TypedDict):
    FailedBatches: List[FailedRemediationExceptionBatchTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AggregateEvaluationResultTypeDef(TypedDict):
    EvaluationResultIdentifier: NotRequired[EvaluationResultIdentifierTypeDef]
    ComplianceType: NotRequired[ComplianceTypeType]
    ResultRecordedTime: NotRequired[datetime]
    ConfigRuleInvokedTime: NotRequired[datetime]
    Annotation: NotRequired[str]
    AccountId: NotRequired[str]
    AwsRegion: NotRequired[str]

class ConformancePackEvaluationResultTypeDef(TypedDict):
    ComplianceType: ConformancePackComplianceTypeType
    EvaluationResultIdentifier: EvaluationResultIdentifierTypeDef
    ConfigRuleInvokedTime: datetime
    ResultRecordedTime: datetime
    Annotation: NotRequired[str]

class EvaluationResultTypeDef(TypedDict):
    EvaluationResultIdentifier: NotRequired[EvaluationResultIdentifierTypeDef]
    ComplianceType: NotRequired[ComplianceTypeType]
    ResultRecordedTime: NotRequired[datetime]
    ConfigRuleInvokedTime: NotRequired[datetime]
    Annotation: NotRequired[str]
    ResultToken: NotRequired[str]

EvaluationUnionTypeDef = Union[EvaluationTypeDef, EvaluationOutputTypeDef]

class PutExternalEvaluationRequestTypeDef(TypedDict):
    ConfigRuleName: str
    ExternalEvaluation: ExternalEvaluationTypeDef

class ResourceEvaluationFiltersTypeDef(TypedDict):
    EvaluationMode: NotRequired[EvaluationModeType]
    TimeWindow: NotRequired[TimeWindowTypeDef]
    EvaluationContextIdentifier: NotRequired[str]

class SelectAggregateResourceConfigResponseTypeDef(TypedDict):
    Results: List[str]
    QueryInfo: QueryInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SelectResourceConfigResponseTypeDef(TypedDict):
    Results: List[str]
    QueryInfo: QueryInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeOrganizationConfigRulesResponseTypeDef(TypedDict):
    OrganizationConfigRules: List[OrganizationConfigRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PutOrganizationConfigRuleRequestTypeDef(TypedDict):
    OrganizationConfigRuleName: str
    OrganizationManagedRuleMetadata: NotRequired[OrganizationManagedRuleMetadataUnionTypeDef]
    OrganizationCustomRuleMetadata: NotRequired[OrganizationCustomRuleMetadataUnionTypeDef]
    ExcludedAccounts: NotRequired[Sequence[str]]
    OrganizationCustomPolicyRuleMetadata: NotRequired[OrganizationCustomPolicyRuleMetadataTypeDef]

class ConfigurationRecorderOutputTypeDef(TypedDict):
    arn: NotRequired[str]
    name: NotRequired[str]
    roleARN: NotRequired[str]
    recordingGroup: NotRequired[RecordingGroupOutputTypeDef]
    recordingMode: NotRequired[RecordingModeOutputTypeDef]
    recordingScope: NotRequired[RecordingScopeType]
    servicePrincipal: NotRequired[str]

class ConfigurationRecorderTypeDef(TypedDict):
    arn: NotRequired[str]
    name: NotRequired[str]
    roleARN: NotRequired[str]
    recordingGroup: NotRequired[RecordingGroupTypeDef]
    recordingMode: NotRequired[RecordingModeTypeDef]
    recordingScope: NotRequired[RecordingScopeType]
    servicePrincipal: NotRequired[str]

class DescribeRemediationExecutionStatusResponseTypeDef(TypedDict):
    RemediationExecutionStatuses: List[RemediationExecutionStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class RemediationConfigurationOutputTypeDef(TypedDict):
    ConfigRuleName: str
    TargetType: Literal["SSM_DOCUMENT"]
    TargetId: str
    TargetVersion: NotRequired[str]
    Parameters: NotRequired[Dict[str, RemediationParameterValueOutputTypeDef]]
    ResourceType: NotRequired[str]
    Automatic: NotRequired[bool]
    ExecutionControls: NotRequired[ExecutionControlsTypeDef]
    MaximumAutomaticAttempts: NotRequired[int]
    RetryAttemptSeconds: NotRequired[int]
    Arn: NotRequired[str]
    CreatedByService: NotRequired[str]

class ConfigRuleOutputTypeDef(TypedDict):
    Source: SourceOutputTypeDef
    ConfigRuleName: NotRequired[str]
    ConfigRuleArn: NotRequired[str]
    ConfigRuleId: NotRequired[str]
    Description: NotRequired[str]
    Scope: NotRequired[ScopeOutputTypeDef]
    InputParameters: NotRequired[str]
    MaximumExecutionFrequency: NotRequired[MaximumExecutionFrequencyType]
    ConfigRuleState: NotRequired[ConfigRuleStateType]
    CreatedBy: NotRequired[str]
    EvaluationModes: NotRequired[List[EvaluationModeConfigurationTypeDef]]

class ConfigRuleTypeDef(TypedDict):
    Source: SourceTypeDef
    ConfigRuleName: NotRequired[str]
    ConfigRuleArn: NotRequired[str]
    ConfigRuleId: NotRequired[str]
    Description: NotRequired[str]
    Scope: NotRequired[ScopeTypeDef]
    InputParameters: NotRequired[str]
    MaximumExecutionFrequency: NotRequired[MaximumExecutionFrequencyType]
    ConfigRuleState: NotRequired[ConfigRuleStateType]
    CreatedBy: NotRequired[str]
    EvaluationModes: NotRequired[Sequence[EvaluationModeConfigurationTypeDef]]

class RemediationParameterValueTypeDef(TypedDict):
    ResourceValue: NotRequired[ResourceValueTypeDef]
    StaticValue: NotRequired[StaticValueUnionTypeDef]

class DescribeConfigurationAggregatorsResponseTypeDef(TypedDict):
    ConfigurationAggregators: List[ConfigurationAggregatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PutConfigurationAggregatorResponseTypeDef(TypedDict):
    ConfigurationAggregator: ConfigurationAggregatorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutConfigurationAggregatorRequestTypeDef(TypedDict):
    ConfigurationAggregatorName: str
    AccountAggregationSources: NotRequired[Sequence[AccountAggregationSourceUnionTypeDef]]
    OrganizationAggregationSource: NotRequired[OrganizationAggregationSourceUnionTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]
    AggregatorFilters: NotRequired[AggregatorFiltersUnionTypeDef]

class GetAggregateConfigRuleComplianceSummaryResponseTypeDef(TypedDict):
    GroupByKey: str
    AggregateComplianceCounts: List[AggregateComplianceCountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetComplianceSummaryByResourceTypeResponseTypeDef(TypedDict):
    ComplianceSummariesByResourceType: List[ComplianceSummaryByResourceTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAggregateComplianceByConfigRulesResponseTypeDef(TypedDict):
    AggregateComplianceByConfigRules: List[AggregateComplianceByConfigRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeComplianceByConfigRuleResponseTypeDef(TypedDict):
    ComplianceByConfigRules: List[ComplianceByConfigRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeComplianceByResourceResponseTypeDef(TypedDict):
    ComplianceByResources: List[ComplianceByResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetAggregateComplianceDetailsByConfigRuleResponseTypeDef(TypedDict):
    AggregateEvaluationResults: List[AggregateEvaluationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetConformancePackComplianceDetailsResponseTypeDef(TypedDict):
    ConformancePackName: str
    ConformancePackRuleEvaluationResults: List[ConformancePackEvaluationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetComplianceDetailsByConfigRuleResponseTypeDef(TypedDict):
    EvaluationResults: List[EvaluationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetComplianceDetailsByResourceResponseTypeDef(TypedDict):
    EvaluationResults: List[EvaluationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PutEvaluationsRequestTypeDef(TypedDict):
    ResultToken: str
    Evaluations: NotRequired[Sequence[EvaluationUnionTypeDef]]
    TestMode: NotRequired[bool]

class ListResourceEvaluationsRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[ResourceEvaluationFiltersTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceEvaluationsRequestTypeDef(TypedDict):
    Filters: NotRequired[ResourceEvaluationFiltersTypeDef]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class AssociateResourceTypesResponseTypeDef(TypedDict):
    ConfigurationRecorder: ConfigurationRecorderOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConfigurationRecordersResponseTypeDef(TypedDict):
    ConfigurationRecorders: List[ConfigurationRecorderOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateResourceTypesResponseTypeDef(TypedDict):
    ConfigurationRecorder: ConfigurationRecorderOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

ConfigurationRecorderUnionTypeDef = Union[
    ConfigurationRecorderTypeDef, ConfigurationRecorderOutputTypeDef
]

class DescribeRemediationConfigurationsResponseTypeDef(TypedDict):
    RemediationConfigurations: List[RemediationConfigurationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FailedRemediationBatchTypeDef(TypedDict):
    FailureMessage: NotRequired[str]
    FailedItems: NotRequired[List[RemediationConfigurationOutputTypeDef]]

class DescribeConfigRulesResponseTypeDef(TypedDict):
    ConfigRules: List[ConfigRuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

ConfigRuleUnionTypeDef = Union[ConfigRuleTypeDef, ConfigRuleOutputTypeDef]
RemediationParameterValueUnionTypeDef = Union[
    RemediationParameterValueTypeDef, RemediationParameterValueOutputTypeDef
]

class PutConfigurationRecorderRequestTypeDef(TypedDict):
    ConfigurationRecorder: ConfigurationRecorderUnionTypeDef
    Tags: NotRequired[Sequence[TagTypeDef]]

class PutRemediationConfigurationsResponseTypeDef(TypedDict):
    FailedBatches: List[FailedRemediationBatchTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutConfigRuleRequestTypeDef(TypedDict):
    ConfigRule: ConfigRuleUnionTypeDef
    Tags: NotRequired[Sequence[TagTypeDef]]

class RemediationConfigurationTypeDef(TypedDict):
    ConfigRuleName: str
    TargetType: Literal["SSM_DOCUMENT"]
    TargetId: str
    TargetVersion: NotRequired[str]
    Parameters: NotRequired[Mapping[str, RemediationParameterValueUnionTypeDef]]
    ResourceType: NotRequired[str]
    Automatic: NotRequired[bool]
    ExecutionControls: NotRequired[ExecutionControlsTypeDef]
    MaximumAutomaticAttempts: NotRequired[int]
    RetryAttemptSeconds: NotRequired[int]
    Arn: NotRequired[str]
    CreatedByService: NotRequired[str]

RemediationConfigurationUnionTypeDef = Union[
    RemediationConfigurationTypeDef, RemediationConfigurationOutputTypeDef
]

class PutRemediationConfigurationsRequestTypeDef(TypedDict):
    RemediationConfigurations: Sequence[RemediationConfigurationUnionTypeDef]
