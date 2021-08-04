"""
Type annotations for config service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/type_defs.html)

Usage::

    ```python
    from mypy_boto3_config.type_defs import AccountAggregationSourceTypeDef

    data: AccountAggregationSourceTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

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
    MaximumExecutionFrequencyType,
    MemberAccountRuleStatusType,
    MessageTypeType,
    OrganizationConfigRuleTriggerTypeType,
    OrganizationResourceDetailedStatusType,
    OrganizationResourceStatusType,
    OrganizationRuleStatusType,
    OwnerType,
    RecorderStatusType,
    RemediationExecutionStateType,
    RemediationExecutionStepStateType,
    ResourceCountGroupKeyType,
    ResourceTypeType,
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
    "AccountAggregationSourceTypeDef",
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
    "BaseConfigurationItemTypeDef",
    "BatchGetAggregateResourceConfigRequestRequestTypeDef",
    "BatchGetAggregateResourceConfigResponseTypeDef",
    "BatchGetResourceConfigRequestRequestTypeDef",
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
    "ConfigRuleTypeDef",
    "ConfigSnapshotDeliveryPropertiesTypeDef",
    "ConfigStreamDeliveryInfoTypeDef",
    "ConfigurationAggregatorTypeDef",
    "ConfigurationItemTypeDef",
    "ConfigurationRecorderStatusTypeDef",
    "ConfigurationRecorderTypeDef",
    "ConformancePackComplianceFiltersTypeDef",
    "ConformancePackComplianceSummaryTypeDef",
    "ConformancePackDetailTypeDef",
    "ConformancePackEvaluationFiltersTypeDef",
    "ConformancePackEvaluationResultTypeDef",
    "ConformancePackInputParameterTypeDef",
    "ConformancePackRuleComplianceTypeDef",
    "ConformancePackStatusDetailTypeDef",
    "DeleteAggregationAuthorizationRequestRequestTypeDef",
    "DeleteConfigRuleRequestRequestTypeDef",
    "DeleteConfigurationAggregatorRequestRequestTypeDef",
    "DeleteConfigurationRecorderRequestRequestTypeDef",
    "DeleteConformancePackRequestRequestTypeDef",
    "DeleteDeliveryChannelRequestRequestTypeDef",
    "DeleteEvaluationResultsRequestRequestTypeDef",
    "DeleteOrganizationConfigRuleRequestRequestTypeDef",
    "DeleteOrganizationConformancePackRequestRequestTypeDef",
    "DeletePendingAggregationRequestRequestRequestTypeDef",
    "DeleteRemediationConfigurationRequestRequestTypeDef",
    "DeleteRemediationExceptionsRequestRequestTypeDef",
    "DeleteRemediationExceptionsResponseTypeDef",
    "DeleteResourceConfigRequestRequestTypeDef",
    "DeleteRetentionConfigurationRequestRequestTypeDef",
    "DeleteStoredQueryRequestRequestTypeDef",
    "DeliverConfigSnapshotRequestRequestTypeDef",
    "DeliverConfigSnapshotResponseTypeDef",
    "DeliveryChannelStatusTypeDef",
    "DeliveryChannelTypeDef",
    "DescribeAggregateComplianceByConfigRulesRequestRequestTypeDef",
    "DescribeAggregateComplianceByConfigRulesResponseTypeDef",
    "DescribeAggregateComplianceByConformancePacksRequestRequestTypeDef",
    "DescribeAggregateComplianceByConformancePacksResponseTypeDef",
    "DescribeAggregationAuthorizationsRequestRequestTypeDef",
    "DescribeAggregationAuthorizationsResponseTypeDef",
    "DescribeComplianceByConfigRuleRequestRequestTypeDef",
    "DescribeComplianceByConfigRuleResponseTypeDef",
    "DescribeComplianceByResourceRequestRequestTypeDef",
    "DescribeComplianceByResourceResponseTypeDef",
    "DescribeConfigRuleEvaluationStatusRequestRequestTypeDef",
    "DescribeConfigRuleEvaluationStatusResponseTypeDef",
    "DescribeConfigRulesRequestRequestTypeDef",
    "DescribeConfigRulesResponseTypeDef",
    "DescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef",
    "DescribeConfigurationAggregatorSourcesStatusResponseTypeDef",
    "DescribeConfigurationAggregatorsRequestRequestTypeDef",
    "DescribeConfigurationAggregatorsResponseTypeDef",
    "DescribeConfigurationRecorderStatusRequestRequestTypeDef",
    "DescribeConfigurationRecorderStatusResponseTypeDef",
    "DescribeConfigurationRecordersRequestRequestTypeDef",
    "DescribeConfigurationRecordersResponseTypeDef",
    "DescribeConformancePackComplianceRequestRequestTypeDef",
    "DescribeConformancePackComplianceResponseTypeDef",
    "DescribeConformancePackStatusRequestRequestTypeDef",
    "DescribeConformancePackStatusResponseTypeDef",
    "DescribeConformancePacksRequestRequestTypeDef",
    "DescribeConformancePacksResponseTypeDef",
    "DescribeDeliveryChannelStatusRequestRequestTypeDef",
    "DescribeDeliveryChannelStatusResponseTypeDef",
    "DescribeDeliveryChannelsRequestRequestTypeDef",
    "DescribeDeliveryChannelsResponseTypeDef",
    "DescribeOrganizationConfigRuleStatusesRequestRequestTypeDef",
    "DescribeOrganizationConfigRuleStatusesResponseTypeDef",
    "DescribeOrganizationConfigRulesRequestRequestTypeDef",
    "DescribeOrganizationConfigRulesResponseTypeDef",
    "DescribeOrganizationConformancePackStatusesRequestRequestTypeDef",
    "DescribeOrganizationConformancePackStatusesResponseTypeDef",
    "DescribeOrganizationConformancePacksRequestRequestTypeDef",
    "DescribeOrganizationConformancePacksResponseTypeDef",
    "DescribePendingAggregationRequestsRequestRequestTypeDef",
    "DescribePendingAggregationRequestsResponseTypeDef",
    "DescribeRemediationConfigurationsRequestRequestTypeDef",
    "DescribeRemediationConfigurationsResponseTypeDef",
    "DescribeRemediationExceptionsRequestRequestTypeDef",
    "DescribeRemediationExceptionsResponseTypeDef",
    "DescribeRemediationExecutionStatusRequestRequestTypeDef",
    "DescribeRemediationExecutionStatusResponseTypeDef",
    "DescribeRetentionConfigurationsRequestRequestTypeDef",
    "DescribeRetentionConfigurationsResponseTypeDef",
    "EvaluationResultIdentifierTypeDef",
    "EvaluationResultQualifierTypeDef",
    "EvaluationResultTypeDef",
    "EvaluationTypeDef",
    "ExecutionControlsTypeDef",
    "ExternalEvaluationTypeDef",
    "FailedDeleteRemediationExceptionsBatchTypeDef",
    "FailedRemediationBatchTypeDef",
    "FailedRemediationExceptionBatchTypeDef",
    "FieldInfoTypeDef",
    "GetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef",
    "GetAggregateComplianceDetailsByConfigRuleResponseTypeDef",
    "GetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef",
    "GetAggregateConfigRuleComplianceSummaryResponseTypeDef",
    "GetAggregateConformancePackComplianceSummaryRequestRequestTypeDef",
    "GetAggregateConformancePackComplianceSummaryResponseTypeDef",
    "GetAggregateDiscoveredResourceCountsRequestRequestTypeDef",
    "GetAggregateDiscoveredResourceCountsResponseTypeDef",
    "GetAggregateResourceConfigRequestRequestTypeDef",
    "GetAggregateResourceConfigResponseTypeDef",
    "GetComplianceDetailsByConfigRuleRequestRequestTypeDef",
    "GetComplianceDetailsByConfigRuleResponseTypeDef",
    "GetComplianceDetailsByResourceRequestRequestTypeDef",
    "GetComplianceDetailsByResourceResponseTypeDef",
    "GetComplianceSummaryByConfigRuleResponseTypeDef",
    "GetComplianceSummaryByResourceTypeRequestRequestTypeDef",
    "GetComplianceSummaryByResourceTypeResponseTypeDef",
    "GetConformancePackComplianceDetailsRequestRequestTypeDef",
    "GetConformancePackComplianceDetailsResponseTypeDef",
    "GetConformancePackComplianceSummaryRequestRequestTypeDef",
    "GetConformancePackComplianceSummaryResponseTypeDef",
    "GetDiscoveredResourceCountsRequestRequestTypeDef",
    "GetDiscoveredResourceCountsResponseTypeDef",
    "GetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef",
    "GetOrganizationConfigRuleDetailedStatusResponseTypeDef",
    "GetOrganizationConformancePackDetailedStatusRequestRequestTypeDef",
    "GetOrganizationConformancePackDetailedStatusResponseTypeDef",
    "GetResourceConfigHistoryRequestRequestTypeDef",
    "GetResourceConfigHistoryResponseTypeDef",
    "GetStoredQueryRequestRequestTypeDef",
    "GetStoredQueryResponseTypeDef",
    "GroupedResourceCountTypeDef",
    "ListAggregateDiscoveredResourcesRequestRequestTypeDef",
    "ListAggregateDiscoveredResourcesResponseTypeDef",
    "ListDiscoveredResourcesRequestRequestTypeDef",
    "ListDiscoveredResourcesResponseTypeDef",
    "ListStoredQueriesRequestRequestTypeDef",
    "ListStoredQueriesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MemberAccountStatusTypeDef",
    "OrganizationAggregationSourceTypeDef",
    "OrganizationConfigRuleStatusTypeDef",
    "OrganizationConfigRuleTypeDef",
    "OrganizationConformancePackDetailedStatusTypeDef",
    "OrganizationConformancePackStatusTypeDef",
    "OrganizationConformancePackTypeDef",
    "OrganizationCustomRuleMetadataTypeDef",
    "OrganizationManagedRuleMetadataTypeDef",
    "OrganizationResourceDetailedStatusFiltersTypeDef",
    "PaginatorConfigTypeDef",
    "PendingAggregationRequestTypeDef",
    "PutAggregationAuthorizationRequestRequestTypeDef",
    "PutAggregationAuthorizationResponseTypeDef",
    "PutConfigRuleRequestRequestTypeDef",
    "PutConfigurationAggregatorRequestRequestTypeDef",
    "PutConfigurationAggregatorResponseTypeDef",
    "PutConfigurationRecorderRequestRequestTypeDef",
    "PutConformancePackRequestRequestTypeDef",
    "PutConformancePackResponseTypeDef",
    "PutDeliveryChannelRequestRequestTypeDef",
    "PutEvaluationsRequestRequestTypeDef",
    "PutEvaluationsResponseTypeDef",
    "PutExternalEvaluationRequestRequestTypeDef",
    "PutOrganizationConfigRuleRequestRequestTypeDef",
    "PutOrganizationConfigRuleResponseTypeDef",
    "PutOrganizationConformancePackRequestRequestTypeDef",
    "PutOrganizationConformancePackResponseTypeDef",
    "PutRemediationConfigurationsRequestRequestTypeDef",
    "PutRemediationConfigurationsResponseTypeDef",
    "PutRemediationExceptionsRequestRequestTypeDef",
    "PutRemediationExceptionsResponseTypeDef",
    "PutResourceConfigRequestRequestTypeDef",
    "PutRetentionConfigurationRequestRequestTypeDef",
    "PutRetentionConfigurationResponseTypeDef",
    "PutStoredQueryRequestRequestTypeDef",
    "PutStoredQueryResponseTypeDef",
    "QueryInfoTypeDef",
    "RecordingGroupTypeDef",
    "RelationshipTypeDef",
    "RemediationConfigurationTypeDef",
    "RemediationExceptionResourceKeyTypeDef",
    "RemediationExceptionTypeDef",
    "RemediationExecutionStatusTypeDef",
    "RemediationExecutionStepTypeDef",
    "RemediationParameterValueTypeDef",
    "ResourceCountFiltersTypeDef",
    "ResourceCountTypeDef",
    "ResourceFiltersTypeDef",
    "ResourceIdentifierTypeDef",
    "ResourceKeyTypeDef",
    "ResourceValueTypeDef",
    "ResponseMetadataTypeDef",
    "RetentionConfigurationTypeDef",
    "ScopeTypeDef",
    "SelectAggregateResourceConfigRequestRequestTypeDef",
    "SelectAggregateResourceConfigResponseTypeDef",
    "SelectResourceConfigRequestRequestTypeDef",
    "SelectResourceConfigResponseTypeDef",
    "SourceDetailTypeDef",
    "SourceTypeDef",
    "SsmControlsTypeDef",
    "StartConfigRulesEvaluationRequestRequestTypeDef",
    "StartConfigurationRecorderRequestRequestTypeDef",
    "StartRemediationExecutionRequestRequestTypeDef",
    "StartRemediationExecutionResponseTypeDef",
    "StaticValueTypeDef",
    "StatusDetailFiltersTypeDef",
    "StopConfigurationRecorderRequestRequestTypeDef",
    "StoredQueryMetadataTypeDef",
    "StoredQueryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
)

_RequiredAccountAggregationSourceTypeDef = TypedDict(
    "_RequiredAccountAggregationSourceTypeDef",
    {
        "AccountIds": List[str],
    },
)
_OptionalAccountAggregationSourceTypeDef = TypedDict(
    "_OptionalAccountAggregationSourceTypeDef",
    {
        "AllAwsRegions": bool,
        "AwsRegions": List[str],
    },
    total=False,
)

class AccountAggregationSourceTypeDef(
    _RequiredAccountAggregationSourceTypeDef, _OptionalAccountAggregationSourceTypeDef
):
    pass

AggregateComplianceByConfigRuleTypeDef = TypedDict(
    "AggregateComplianceByConfigRuleTypeDef",
    {
        "ConfigRuleName": str,
        "Compliance": "ComplianceTypeDef",
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

AggregateComplianceByConformancePackTypeDef = TypedDict(
    "AggregateComplianceByConformancePackTypeDef",
    {
        "ConformancePackName": str,
        "Compliance": "AggregateConformancePackComplianceTypeDef",
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

AggregateComplianceCountTypeDef = TypedDict(
    "AggregateComplianceCountTypeDef",
    {
        "GroupName": str,
        "ComplianceSummary": "ComplianceSummaryTypeDef",
    },
    total=False,
)

AggregateConformancePackComplianceCountTypeDef = TypedDict(
    "AggregateConformancePackComplianceCountTypeDef",
    {
        "CompliantConformancePackCount": int,
        "NonCompliantConformancePackCount": int,
    },
    total=False,
)

AggregateConformancePackComplianceFiltersTypeDef = TypedDict(
    "AggregateConformancePackComplianceFiltersTypeDef",
    {
        "ConformancePackName": str,
        "ComplianceType": ConformancePackComplianceTypeType,
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

AggregateConformancePackComplianceSummaryFiltersTypeDef = TypedDict(
    "AggregateConformancePackComplianceSummaryFiltersTypeDef",
    {
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

AggregateConformancePackComplianceSummaryTypeDef = TypedDict(
    "AggregateConformancePackComplianceSummaryTypeDef",
    {
        "ComplianceSummary": "AggregateConformancePackComplianceCountTypeDef",
        "GroupName": str,
    },
    total=False,
)

AggregateConformancePackComplianceTypeDef = TypedDict(
    "AggregateConformancePackComplianceTypeDef",
    {
        "ComplianceType": ConformancePackComplianceTypeType,
        "CompliantRuleCount": int,
        "NonCompliantRuleCount": int,
        "TotalRuleCount": int,
    },
    total=False,
)

AggregateEvaluationResultTypeDef = TypedDict(
    "AggregateEvaluationResultTypeDef",
    {
        "EvaluationResultIdentifier": "EvaluationResultIdentifierTypeDef",
        "ComplianceType": ComplianceTypeType,
        "ResultRecordedTime": datetime,
        "ConfigRuleInvokedTime": datetime,
        "Annotation": str,
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

_RequiredAggregateResourceIdentifierTypeDef = TypedDict(
    "_RequiredAggregateResourceIdentifierTypeDef",
    {
        "SourceAccountId": str,
        "SourceRegion": str,
        "ResourceId": str,
        "ResourceType": ResourceTypeType,
    },
)
_OptionalAggregateResourceIdentifierTypeDef = TypedDict(
    "_OptionalAggregateResourceIdentifierTypeDef",
    {
        "ResourceName": str,
    },
    total=False,
)

class AggregateResourceIdentifierTypeDef(
    _RequiredAggregateResourceIdentifierTypeDef, _OptionalAggregateResourceIdentifierTypeDef
):
    pass

AggregatedSourceStatusTypeDef = TypedDict(
    "AggregatedSourceStatusTypeDef",
    {
        "SourceId": str,
        "SourceType": AggregatedSourceTypeType,
        "AwsRegion": str,
        "LastUpdateStatus": AggregatedSourceStatusTypeType,
        "LastUpdateTime": datetime,
        "LastErrorCode": str,
        "LastErrorMessage": str,
    },
    total=False,
)

AggregationAuthorizationTypeDef = TypedDict(
    "AggregationAuthorizationTypeDef",
    {
        "AggregationAuthorizationArn": str,
        "AuthorizedAccountId": str,
        "AuthorizedAwsRegion": str,
        "CreationTime": datetime,
    },
    total=False,
)

BaseConfigurationItemTypeDef = TypedDict(
    "BaseConfigurationItemTypeDef",
    {
        "version": str,
        "accountId": str,
        "configurationItemCaptureTime": datetime,
        "configurationItemStatus": ConfigurationItemStatusType,
        "configurationStateId": str,
        "arn": str,
        "resourceType": ResourceTypeType,
        "resourceId": str,
        "resourceName": str,
        "awsRegion": str,
        "availabilityZone": str,
        "resourceCreationTime": datetime,
        "configuration": str,
        "supplementaryConfiguration": Dict[str, str],
    },
    total=False,
)

BatchGetAggregateResourceConfigRequestRequestTypeDef = TypedDict(
    "BatchGetAggregateResourceConfigRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ResourceIdentifiers": List["AggregateResourceIdentifierTypeDef"],
    },
)

BatchGetAggregateResourceConfigResponseTypeDef = TypedDict(
    "BatchGetAggregateResourceConfigResponseTypeDef",
    {
        "BaseConfigurationItems": List["BaseConfigurationItemTypeDef"],
        "UnprocessedResourceIdentifiers": List["AggregateResourceIdentifierTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetResourceConfigRequestRequestTypeDef = TypedDict(
    "BatchGetResourceConfigRequestRequestTypeDef",
    {
        "resourceKeys": List["ResourceKeyTypeDef"],
    },
)

BatchGetResourceConfigResponseTypeDef = TypedDict(
    "BatchGetResourceConfigResponseTypeDef",
    {
        "baseConfigurationItems": List["BaseConfigurationItemTypeDef"],
        "unprocessedResourceKeys": List["ResourceKeyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ComplianceByConfigRuleTypeDef = TypedDict(
    "ComplianceByConfigRuleTypeDef",
    {
        "ConfigRuleName": str,
        "Compliance": "ComplianceTypeDef",
    },
    total=False,
)

ComplianceByResourceTypeDef = TypedDict(
    "ComplianceByResourceTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
        "Compliance": "ComplianceTypeDef",
    },
    total=False,
)

ComplianceContributorCountTypeDef = TypedDict(
    "ComplianceContributorCountTypeDef",
    {
        "CappedCount": int,
        "CapExceeded": bool,
    },
    total=False,
)

ComplianceSummaryByResourceTypeTypeDef = TypedDict(
    "ComplianceSummaryByResourceTypeTypeDef",
    {
        "ResourceType": str,
        "ComplianceSummary": "ComplianceSummaryTypeDef",
    },
    total=False,
)

ComplianceSummaryTypeDef = TypedDict(
    "ComplianceSummaryTypeDef",
    {
        "CompliantResourceCount": "ComplianceContributorCountTypeDef",
        "NonCompliantResourceCount": "ComplianceContributorCountTypeDef",
        "ComplianceSummaryTimestamp": datetime,
    },
    total=False,
)

ComplianceTypeDef = TypedDict(
    "ComplianceTypeDef",
    {
        "ComplianceType": ComplianceTypeType,
        "ComplianceContributorCount": "ComplianceContributorCountTypeDef",
    },
    total=False,
)

ConfigExportDeliveryInfoTypeDef = TypedDict(
    "ConfigExportDeliveryInfoTypeDef",
    {
        "lastStatus": DeliveryStatusType,
        "lastErrorCode": str,
        "lastErrorMessage": str,
        "lastAttemptTime": datetime,
        "lastSuccessfulTime": datetime,
        "nextDeliveryTime": datetime,
    },
    total=False,
)

ConfigRuleComplianceFiltersTypeDef = TypedDict(
    "ConfigRuleComplianceFiltersTypeDef",
    {
        "ConfigRuleName": str,
        "ComplianceType": ComplianceTypeType,
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

ConfigRuleComplianceSummaryFiltersTypeDef = TypedDict(
    "ConfigRuleComplianceSummaryFiltersTypeDef",
    {
        "AccountId": str,
        "AwsRegion": str,
    },
    total=False,
)

ConfigRuleEvaluationStatusTypeDef = TypedDict(
    "ConfigRuleEvaluationStatusTypeDef",
    {
        "ConfigRuleName": str,
        "ConfigRuleArn": str,
        "ConfigRuleId": str,
        "LastSuccessfulInvocationTime": datetime,
        "LastFailedInvocationTime": datetime,
        "LastSuccessfulEvaluationTime": datetime,
        "LastFailedEvaluationTime": datetime,
        "FirstActivatedTime": datetime,
        "LastDeactivatedTime": datetime,
        "LastErrorCode": str,
        "LastErrorMessage": str,
        "FirstEvaluationStarted": bool,
    },
    total=False,
)

_RequiredConfigRuleTypeDef = TypedDict(
    "_RequiredConfigRuleTypeDef",
    {
        "Source": "SourceTypeDef",
    },
)
_OptionalConfigRuleTypeDef = TypedDict(
    "_OptionalConfigRuleTypeDef",
    {
        "ConfigRuleName": str,
        "ConfigRuleArn": str,
        "ConfigRuleId": str,
        "Description": str,
        "Scope": "ScopeTypeDef",
        "InputParameters": str,
        "MaximumExecutionFrequency": MaximumExecutionFrequencyType,
        "ConfigRuleState": ConfigRuleStateType,
        "CreatedBy": str,
    },
    total=False,
)

class ConfigRuleTypeDef(_RequiredConfigRuleTypeDef, _OptionalConfigRuleTypeDef):
    pass

ConfigSnapshotDeliveryPropertiesTypeDef = TypedDict(
    "ConfigSnapshotDeliveryPropertiesTypeDef",
    {
        "deliveryFrequency": MaximumExecutionFrequencyType,
    },
    total=False,
)

ConfigStreamDeliveryInfoTypeDef = TypedDict(
    "ConfigStreamDeliveryInfoTypeDef",
    {
        "lastStatus": DeliveryStatusType,
        "lastErrorCode": str,
        "lastErrorMessage": str,
        "lastStatusChangeTime": datetime,
    },
    total=False,
)

ConfigurationAggregatorTypeDef = TypedDict(
    "ConfigurationAggregatorTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ConfigurationAggregatorArn": str,
        "AccountAggregationSources": List["AccountAggregationSourceTypeDef"],
        "OrganizationAggregationSource": "OrganizationAggregationSourceTypeDef",
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "CreatedBy": str,
    },
    total=False,
)

ConfigurationItemTypeDef = TypedDict(
    "ConfigurationItemTypeDef",
    {
        "version": str,
        "accountId": str,
        "configurationItemCaptureTime": datetime,
        "configurationItemStatus": ConfigurationItemStatusType,
        "configurationStateId": str,
        "configurationItemMD5Hash": str,
        "arn": str,
        "resourceType": ResourceTypeType,
        "resourceId": str,
        "resourceName": str,
        "awsRegion": str,
        "availabilityZone": str,
        "resourceCreationTime": datetime,
        "tags": Dict[str, str],
        "relatedEvents": List[str],
        "relationships": List["RelationshipTypeDef"],
        "configuration": str,
        "supplementaryConfiguration": Dict[str, str],
    },
    total=False,
)

ConfigurationRecorderStatusTypeDef = TypedDict(
    "ConfigurationRecorderStatusTypeDef",
    {
        "name": str,
        "lastStartTime": datetime,
        "lastStopTime": datetime,
        "recording": bool,
        "lastStatus": RecorderStatusType,
        "lastErrorCode": str,
        "lastErrorMessage": str,
        "lastStatusChangeTime": datetime,
    },
    total=False,
)

ConfigurationRecorderTypeDef = TypedDict(
    "ConfigurationRecorderTypeDef",
    {
        "name": str,
        "roleARN": str,
        "recordingGroup": "RecordingGroupTypeDef",
    },
    total=False,
)

ConformancePackComplianceFiltersTypeDef = TypedDict(
    "ConformancePackComplianceFiltersTypeDef",
    {
        "ConfigRuleNames": List[str],
        "ComplianceType": ConformancePackComplianceTypeType,
    },
    total=False,
)

ConformancePackComplianceSummaryTypeDef = TypedDict(
    "ConformancePackComplianceSummaryTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackComplianceStatus": ConformancePackComplianceTypeType,
    },
)

_RequiredConformancePackDetailTypeDef = TypedDict(
    "_RequiredConformancePackDetailTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackArn": str,
        "ConformancePackId": str,
    },
)
_OptionalConformancePackDetailTypeDef = TypedDict(
    "_OptionalConformancePackDetailTypeDef",
    {
        "DeliveryS3Bucket": str,
        "DeliveryS3KeyPrefix": str,
        "ConformancePackInputParameters": List["ConformancePackInputParameterTypeDef"],
        "LastUpdateRequestedTime": datetime,
        "CreatedBy": str,
    },
    total=False,
)

class ConformancePackDetailTypeDef(
    _RequiredConformancePackDetailTypeDef, _OptionalConformancePackDetailTypeDef
):
    pass

ConformancePackEvaluationFiltersTypeDef = TypedDict(
    "ConformancePackEvaluationFiltersTypeDef",
    {
        "ConfigRuleNames": List[str],
        "ComplianceType": ConformancePackComplianceTypeType,
        "ResourceType": str,
        "ResourceIds": List[str],
    },
    total=False,
)

_RequiredConformancePackEvaluationResultTypeDef = TypedDict(
    "_RequiredConformancePackEvaluationResultTypeDef",
    {
        "ComplianceType": ConformancePackComplianceTypeType,
        "EvaluationResultIdentifier": "EvaluationResultIdentifierTypeDef",
        "ConfigRuleInvokedTime": datetime,
        "ResultRecordedTime": datetime,
    },
)
_OptionalConformancePackEvaluationResultTypeDef = TypedDict(
    "_OptionalConformancePackEvaluationResultTypeDef",
    {
        "Annotation": str,
    },
    total=False,
)

class ConformancePackEvaluationResultTypeDef(
    _RequiredConformancePackEvaluationResultTypeDef, _OptionalConformancePackEvaluationResultTypeDef
):
    pass

ConformancePackInputParameterTypeDef = TypedDict(
    "ConformancePackInputParameterTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
    },
)

ConformancePackRuleComplianceTypeDef = TypedDict(
    "ConformancePackRuleComplianceTypeDef",
    {
        "ConfigRuleName": str,
        "ComplianceType": ConformancePackComplianceTypeType,
        "Controls": List[str],
    },
    total=False,
)

_RequiredConformancePackStatusDetailTypeDef = TypedDict(
    "_RequiredConformancePackStatusDetailTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackId": str,
        "ConformancePackArn": str,
        "ConformancePackState": ConformancePackStateType,
        "StackArn": str,
        "LastUpdateRequestedTime": datetime,
    },
)
_OptionalConformancePackStatusDetailTypeDef = TypedDict(
    "_OptionalConformancePackStatusDetailTypeDef",
    {
        "ConformancePackStatusReason": str,
        "LastUpdateCompletedTime": datetime,
    },
    total=False,
)

class ConformancePackStatusDetailTypeDef(
    _RequiredConformancePackStatusDetailTypeDef, _OptionalConformancePackStatusDetailTypeDef
):
    pass

DeleteAggregationAuthorizationRequestRequestTypeDef = TypedDict(
    "DeleteAggregationAuthorizationRequestRequestTypeDef",
    {
        "AuthorizedAccountId": str,
        "AuthorizedAwsRegion": str,
    },
)

DeleteConfigRuleRequestRequestTypeDef = TypedDict(
    "DeleteConfigRuleRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
    },
)

DeleteConfigurationAggregatorRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationAggregatorRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)

DeleteConfigurationRecorderRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationRecorderRequestRequestTypeDef",
    {
        "ConfigurationRecorderName": str,
    },
)

DeleteConformancePackRequestRequestTypeDef = TypedDict(
    "DeleteConformancePackRequestRequestTypeDef",
    {
        "ConformancePackName": str,
    },
)

DeleteDeliveryChannelRequestRequestTypeDef = TypedDict(
    "DeleteDeliveryChannelRequestRequestTypeDef",
    {
        "DeliveryChannelName": str,
    },
)

DeleteEvaluationResultsRequestRequestTypeDef = TypedDict(
    "DeleteEvaluationResultsRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
    },
)

DeleteOrganizationConfigRuleRequestRequestTypeDef = TypedDict(
    "DeleteOrganizationConfigRuleRequestRequestTypeDef",
    {
        "OrganizationConfigRuleName": str,
    },
)

DeleteOrganizationConformancePackRequestRequestTypeDef = TypedDict(
    "DeleteOrganizationConformancePackRequestRequestTypeDef",
    {
        "OrganizationConformancePackName": str,
    },
)

DeletePendingAggregationRequestRequestRequestTypeDef = TypedDict(
    "DeletePendingAggregationRequestRequestRequestTypeDef",
    {
        "RequesterAccountId": str,
        "RequesterAwsRegion": str,
    },
)

_RequiredDeleteRemediationConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRemediationConfigurationRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
    },
)
_OptionalDeleteRemediationConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteRemediationConfigurationRequestRequestTypeDef",
    {
        "ResourceType": str,
    },
    total=False,
)

class DeleteRemediationConfigurationRequestRequestTypeDef(
    _RequiredDeleteRemediationConfigurationRequestRequestTypeDef,
    _OptionalDeleteRemediationConfigurationRequestRequestTypeDef,
):
    pass

DeleteRemediationExceptionsRequestRequestTypeDef = TypedDict(
    "DeleteRemediationExceptionsRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceKeys": List["RemediationExceptionResourceKeyTypeDef"],
    },
)

DeleteRemediationExceptionsResponseTypeDef = TypedDict(
    "DeleteRemediationExceptionsResponseTypeDef",
    {
        "FailedBatches": List["FailedDeleteRemediationExceptionsBatchTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourceConfigRequestRequestTypeDef = TypedDict(
    "DeleteResourceConfigRequestRequestTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
    },
)

DeleteRetentionConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteRetentionConfigurationRequestRequestTypeDef",
    {
        "RetentionConfigurationName": str,
    },
)

DeleteStoredQueryRequestRequestTypeDef = TypedDict(
    "DeleteStoredQueryRequestRequestTypeDef",
    {
        "QueryName": str,
    },
)

DeliverConfigSnapshotRequestRequestTypeDef = TypedDict(
    "DeliverConfigSnapshotRequestRequestTypeDef",
    {
        "deliveryChannelName": str,
    },
)

DeliverConfigSnapshotResponseTypeDef = TypedDict(
    "DeliverConfigSnapshotResponseTypeDef",
    {
        "configSnapshotId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeliveryChannelStatusTypeDef = TypedDict(
    "DeliveryChannelStatusTypeDef",
    {
        "name": str,
        "configSnapshotDeliveryInfo": "ConfigExportDeliveryInfoTypeDef",
        "configHistoryDeliveryInfo": "ConfigExportDeliveryInfoTypeDef",
        "configStreamDeliveryInfo": "ConfigStreamDeliveryInfoTypeDef",
    },
    total=False,
)

DeliveryChannelTypeDef = TypedDict(
    "DeliveryChannelTypeDef",
    {
        "name": str,
        "s3BucketName": str,
        "s3KeyPrefix": str,
        "s3KmsKeyArn": str,
        "snsTopicARN": str,
        "configSnapshotDeliveryProperties": "ConfigSnapshotDeliveryPropertiesTypeDef",
    },
    total=False,
)

_RequiredDescribeAggregateComplianceByConfigRulesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAggregateComplianceByConfigRulesRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalDescribeAggregateComplianceByConfigRulesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAggregateComplianceByConfigRulesRequestRequestTypeDef",
    {
        "Filters": "ConfigRuleComplianceFiltersTypeDef",
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeAggregateComplianceByConfigRulesRequestRequestTypeDef(
    _RequiredDescribeAggregateComplianceByConfigRulesRequestRequestTypeDef,
    _OptionalDescribeAggregateComplianceByConfigRulesRequestRequestTypeDef,
):
    pass

DescribeAggregateComplianceByConfigRulesResponseTypeDef = TypedDict(
    "DescribeAggregateComplianceByConfigRulesResponseTypeDef",
    {
        "AggregateComplianceByConfigRules": List["AggregateComplianceByConfigRuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAggregateComplianceByConformancePacksRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAggregateComplianceByConformancePacksRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalDescribeAggregateComplianceByConformancePacksRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAggregateComplianceByConformancePacksRequestRequestTypeDef",
    {
        "Filters": "AggregateConformancePackComplianceFiltersTypeDef",
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeAggregateComplianceByConformancePacksRequestRequestTypeDef(
    _RequiredDescribeAggregateComplianceByConformancePacksRequestRequestTypeDef,
    _OptionalDescribeAggregateComplianceByConformancePacksRequestRequestTypeDef,
):
    pass

DescribeAggregateComplianceByConformancePacksResponseTypeDef = TypedDict(
    "DescribeAggregateComplianceByConformancePacksResponseTypeDef",
    {
        "AggregateComplianceByConformancePacks": List[
            "AggregateComplianceByConformancePackTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAggregationAuthorizationsRequestRequestTypeDef = TypedDict(
    "DescribeAggregationAuthorizationsRequestRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeAggregationAuthorizationsResponseTypeDef = TypedDict(
    "DescribeAggregationAuthorizationsResponseTypeDef",
    {
        "AggregationAuthorizations": List["AggregationAuthorizationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeComplianceByConfigRuleRequestRequestTypeDef = TypedDict(
    "DescribeComplianceByConfigRuleRequestRequestTypeDef",
    {
        "ConfigRuleNames": List[str],
        "ComplianceTypes": List[ComplianceTypeType],
        "NextToken": str,
    },
    total=False,
)

DescribeComplianceByConfigRuleResponseTypeDef = TypedDict(
    "DescribeComplianceByConfigRuleResponseTypeDef",
    {
        "ComplianceByConfigRules": List["ComplianceByConfigRuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeComplianceByResourceRequestRequestTypeDef = TypedDict(
    "DescribeComplianceByResourceRequestRequestTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
        "ComplianceTypes": List[ComplianceTypeType],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeComplianceByResourceResponseTypeDef = TypedDict(
    "DescribeComplianceByResourceResponseTypeDef",
    {
        "ComplianceByResources": List["ComplianceByResourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigRuleEvaluationStatusRequestRequestTypeDef = TypedDict(
    "DescribeConfigRuleEvaluationStatusRequestRequestTypeDef",
    {
        "ConfigRuleNames": List[str],
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

DescribeConfigRuleEvaluationStatusResponseTypeDef = TypedDict(
    "DescribeConfigRuleEvaluationStatusResponseTypeDef",
    {
        "ConfigRulesEvaluationStatus": List["ConfigRuleEvaluationStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigRulesRequestRequestTypeDef = TypedDict(
    "DescribeConfigRulesRequestRequestTypeDef",
    {
        "ConfigRuleNames": List[str],
        "NextToken": str,
    },
    total=False,
)

DescribeConfigRulesResponseTypeDef = TypedDict(
    "DescribeConfigRulesResponseTypeDef",
    {
        "ConfigRules": List["ConfigRuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalDescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef",
    {
        "UpdateStatus": List[AggregatedSourceStatusTypeType],
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

class DescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef(
    _RequiredDescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef,
    _OptionalDescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef,
):
    pass

DescribeConfigurationAggregatorSourcesStatusResponseTypeDef = TypedDict(
    "DescribeConfigurationAggregatorSourcesStatusResponseTypeDef",
    {
        "AggregatedSourceStatusList": List["AggregatedSourceStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationAggregatorsRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationAggregatorsRequestRequestTypeDef",
    {
        "ConfigurationAggregatorNames": List[str],
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

DescribeConfigurationAggregatorsResponseTypeDef = TypedDict(
    "DescribeConfigurationAggregatorsResponseTypeDef",
    {
        "ConfigurationAggregators": List["ConfigurationAggregatorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationRecorderStatusRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationRecorderStatusRequestRequestTypeDef",
    {
        "ConfigurationRecorderNames": List[str],
    },
    total=False,
)

DescribeConfigurationRecorderStatusResponseTypeDef = TypedDict(
    "DescribeConfigurationRecorderStatusResponseTypeDef",
    {
        "ConfigurationRecordersStatus": List["ConfigurationRecorderStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationRecordersRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationRecordersRequestRequestTypeDef",
    {
        "ConfigurationRecorderNames": List[str],
    },
    total=False,
)

DescribeConfigurationRecordersResponseTypeDef = TypedDict(
    "DescribeConfigurationRecordersResponseTypeDef",
    {
        "ConfigurationRecorders": List["ConfigurationRecorderTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeConformancePackComplianceRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeConformancePackComplianceRequestRequestTypeDef",
    {
        "ConformancePackName": str,
    },
)
_OptionalDescribeConformancePackComplianceRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeConformancePackComplianceRequestRequestTypeDef",
    {
        "Filters": "ConformancePackComplianceFiltersTypeDef",
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeConformancePackComplianceRequestRequestTypeDef(
    _RequiredDescribeConformancePackComplianceRequestRequestTypeDef,
    _OptionalDescribeConformancePackComplianceRequestRequestTypeDef,
):
    pass

DescribeConformancePackComplianceResponseTypeDef = TypedDict(
    "DescribeConformancePackComplianceResponseTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackRuleComplianceList": List["ConformancePackRuleComplianceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConformancePackStatusRequestRequestTypeDef = TypedDict(
    "DescribeConformancePackStatusRequestRequestTypeDef",
    {
        "ConformancePackNames": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeConformancePackStatusResponseTypeDef = TypedDict(
    "DescribeConformancePackStatusResponseTypeDef",
    {
        "ConformancePackStatusDetails": List["ConformancePackStatusDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConformancePacksRequestRequestTypeDef = TypedDict(
    "DescribeConformancePacksRequestRequestTypeDef",
    {
        "ConformancePackNames": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeConformancePacksResponseTypeDef = TypedDict(
    "DescribeConformancePacksResponseTypeDef",
    {
        "ConformancePackDetails": List["ConformancePackDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeliveryChannelStatusRequestRequestTypeDef = TypedDict(
    "DescribeDeliveryChannelStatusRequestRequestTypeDef",
    {
        "DeliveryChannelNames": List[str],
    },
    total=False,
)

DescribeDeliveryChannelStatusResponseTypeDef = TypedDict(
    "DescribeDeliveryChannelStatusResponseTypeDef",
    {
        "DeliveryChannelsStatus": List["DeliveryChannelStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeliveryChannelsRequestRequestTypeDef = TypedDict(
    "DescribeDeliveryChannelsRequestRequestTypeDef",
    {
        "DeliveryChannelNames": List[str],
    },
    total=False,
)

DescribeDeliveryChannelsResponseTypeDef = TypedDict(
    "DescribeDeliveryChannelsResponseTypeDef",
    {
        "DeliveryChannels": List["DeliveryChannelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationConfigRuleStatusesRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationConfigRuleStatusesRequestRequestTypeDef",
    {
        "OrganizationConfigRuleNames": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeOrganizationConfigRuleStatusesResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigRuleStatusesResponseTypeDef",
    {
        "OrganizationConfigRuleStatuses": List["OrganizationConfigRuleStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationConfigRulesRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationConfigRulesRequestRequestTypeDef",
    {
        "OrganizationConfigRuleNames": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeOrganizationConfigRulesResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigRulesResponseTypeDef",
    {
        "OrganizationConfigRules": List["OrganizationConfigRuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationConformancePackStatusesRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationConformancePackStatusesRequestRequestTypeDef",
    {
        "OrganizationConformancePackNames": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeOrganizationConformancePackStatusesResponseTypeDef = TypedDict(
    "DescribeOrganizationConformancePackStatusesResponseTypeDef",
    {
        "OrganizationConformancePackStatuses": List["OrganizationConformancePackStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationConformancePacksRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationConformancePacksRequestRequestTypeDef",
    {
        "OrganizationConformancePackNames": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeOrganizationConformancePacksResponseTypeDef = TypedDict(
    "DescribeOrganizationConformancePacksResponseTypeDef",
    {
        "OrganizationConformancePacks": List["OrganizationConformancePackTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePendingAggregationRequestsRequestRequestTypeDef = TypedDict(
    "DescribePendingAggregationRequestsRequestRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribePendingAggregationRequestsResponseTypeDef = TypedDict(
    "DescribePendingAggregationRequestsResponseTypeDef",
    {
        "PendingAggregationRequests": List["PendingAggregationRequestTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRemediationConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeRemediationConfigurationsRequestRequestTypeDef",
    {
        "ConfigRuleNames": List[str],
    },
)

DescribeRemediationConfigurationsResponseTypeDef = TypedDict(
    "DescribeRemediationConfigurationsResponseTypeDef",
    {
        "RemediationConfigurations": List["RemediationConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRemediationExceptionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeRemediationExceptionsRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
    },
)
_OptionalDescribeRemediationExceptionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeRemediationExceptionsRequestRequestTypeDef",
    {
        "ResourceKeys": List["RemediationExceptionResourceKeyTypeDef"],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeRemediationExceptionsRequestRequestTypeDef(
    _RequiredDescribeRemediationExceptionsRequestRequestTypeDef,
    _OptionalDescribeRemediationExceptionsRequestRequestTypeDef,
):
    pass

DescribeRemediationExceptionsResponseTypeDef = TypedDict(
    "DescribeRemediationExceptionsResponseTypeDef",
    {
        "RemediationExceptions": List["RemediationExceptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRemediationExecutionStatusRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeRemediationExecutionStatusRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
    },
)
_OptionalDescribeRemediationExecutionStatusRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeRemediationExecutionStatusRequestRequestTypeDef",
    {
        "ResourceKeys": List["ResourceKeyTypeDef"],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeRemediationExecutionStatusRequestRequestTypeDef(
    _RequiredDescribeRemediationExecutionStatusRequestRequestTypeDef,
    _OptionalDescribeRemediationExecutionStatusRequestRequestTypeDef,
):
    pass

DescribeRemediationExecutionStatusResponseTypeDef = TypedDict(
    "DescribeRemediationExecutionStatusResponseTypeDef",
    {
        "RemediationExecutionStatuses": List["RemediationExecutionStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRetentionConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeRetentionConfigurationsRequestRequestTypeDef",
    {
        "RetentionConfigurationNames": List[str],
        "NextToken": str,
    },
    total=False,
)

DescribeRetentionConfigurationsResponseTypeDef = TypedDict(
    "DescribeRetentionConfigurationsResponseTypeDef",
    {
        "RetentionConfigurations": List["RetentionConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EvaluationResultIdentifierTypeDef = TypedDict(
    "EvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": "EvaluationResultQualifierTypeDef",
        "OrderingTimestamp": datetime,
    },
    total=False,
)

EvaluationResultQualifierTypeDef = TypedDict(
    "EvaluationResultQualifierTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceType": str,
        "ResourceId": str,
    },
    total=False,
)

EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "EvaluationResultIdentifier": "EvaluationResultIdentifierTypeDef",
        "ComplianceType": ComplianceTypeType,
        "ResultRecordedTime": datetime,
        "ConfigRuleInvokedTime": datetime,
        "Annotation": str,
        "ResultToken": str,
    },
    total=False,
)

_RequiredEvaluationTypeDef = TypedDict(
    "_RequiredEvaluationTypeDef",
    {
        "ComplianceResourceType": str,
        "ComplianceResourceId": str,
        "ComplianceType": ComplianceTypeType,
        "OrderingTimestamp": Union[datetime, str],
    },
)
_OptionalEvaluationTypeDef = TypedDict(
    "_OptionalEvaluationTypeDef",
    {
        "Annotation": str,
    },
    total=False,
)

class EvaluationTypeDef(_RequiredEvaluationTypeDef, _OptionalEvaluationTypeDef):
    pass

ExecutionControlsTypeDef = TypedDict(
    "ExecutionControlsTypeDef",
    {
        "SsmControls": "SsmControlsTypeDef",
    },
    total=False,
)

_RequiredExternalEvaluationTypeDef = TypedDict(
    "_RequiredExternalEvaluationTypeDef",
    {
        "ComplianceResourceType": str,
        "ComplianceResourceId": str,
        "ComplianceType": ComplianceTypeType,
        "OrderingTimestamp": Union[datetime, str],
    },
)
_OptionalExternalEvaluationTypeDef = TypedDict(
    "_OptionalExternalEvaluationTypeDef",
    {
        "Annotation": str,
    },
    total=False,
)

class ExternalEvaluationTypeDef(
    _RequiredExternalEvaluationTypeDef, _OptionalExternalEvaluationTypeDef
):
    pass

FailedDeleteRemediationExceptionsBatchTypeDef = TypedDict(
    "FailedDeleteRemediationExceptionsBatchTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List["RemediationExceptionResourceKeyTypeDef"],
    },
    total=False,
)

FailedRemediationBatchTypeDef = TypedDict(
    "FailedRemediationBatchTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List["RemediationConfigurationTypeDef"],
    },
    total=False,
)

FailedRemediationExceptionBatchTypeDef = TypedDict(
    "FailedRemediationExceptionBatchTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List["RemediationExceptionTypeDef"],
    },
    total=False,
)

FieldInfoTypeDef = TypedDict(
    "FieldInfoTypeDef",
    {
        "Name": str,
    },
    total=False,
)

_RequiredGetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef = TypedDict(
    "_RequiredGetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ConfigRuleName": str,
        "AccountId": str,
        "AwsRegion": str,
    },
)
_OptionalGetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef = TypedDict(
    "_OptionalGetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef",
    {
        "ComplianceType": ComplianceTypeType,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class GetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef(
    _RequiredGetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef,
    _OptionalGetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef,
):
    pass

GetAggregateComplianceDetailsByConfigRuleResponseTypeDef = TypedDict(
    "GetAggregateComplianceDetailsByConfigRuleResponseTypeDef",
    {
        "AggregateEvaluationResults": List["AggregateEvaluationResultTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef = TypedDict(
    "_RequiredGetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalGetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef = TypedDict(
    "_OptionalGetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef",
    {
        "Filters": "ConfigRuleComplianceSummaryFiltersTypeDef",
        "GroupByKey": ConfigRuleComplianceSummaryGroupKeyType,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class GetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef(
    _RequiredGetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef,
    _OptionalGetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef,
):
    pass

GetAggregateConfigRuleComplianceSummaryResponseTypeDef = TypedDict(
    "GetAggregateConfigRuleComplianceSummaryResponseTypeDef",
    {
        "GroupByKey": str,
        "AggregateComplianceCounts": List["AggregateComplianceCountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetAggregateConformancePackComplianceSummaryRequestRequestTypeDef = TypedDict(
    "_RequiredGetAggregateConformancePackComplianceSummaryRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalGetAggregateConformancePackComplianceSummaryRequestRequestTypeDef = TypedDict(
    "_OptionalGetAggregateConformancePackComplianceSummaryRequestRequestTypeDef",
    {
        "Filters": "AggregateConformancePackComplianceSummaryFiltersTypeDef",
        "GroupByKey": AggregateConformancePackComplianceSummaryGroupKeyType,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class GetAggregateConformancePackComplianceSummaryRequestRequestTypeDef(
    _RequiredGetAggregateConformancePackComplianceSummaryRequestRequestTypeDef,
    _OptionalGetAggregateConformancePackComplianceSummaryRequestRequestTypeDef,
):
    pass

GetAggregateConformancePackComplianceSummaryResponseTypeDef = TypedDict(
    "GetAggregateConformancePackComplianceSummaryResponseTypeDef",
    {
        "AggregateConformancePackComplianceSummaries": List[
            "AggregateConformancePackComplianceSummaryTypeDef"
        ],
        "GroupByKey": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetAggregateDiscoveredResourceCountsRequestRequestTypeDef = TypedDict(
    "_RequiredGetAggregateDiscoveredResourceCountsRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalGetAggregateDiscoveredResourceCountsRequestRequestTypeDef = TypedDict(
    "_OptionalGetAggregateDiscoveredResourceCountsRequestRequestTypeDef",
    {
        "Filters": "ResourceCountFiltersTypeDef",
        "GroupByKey": ResourceCountGroupKeyType,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class GetAggregateDiscoveredResourceCountsRequestRequestTypeDef(
    _RequiredGetAggregateDiscoveredResourceCountsRequestRequestTypeDef,
    _OptionalGetAggregateDiscoveredResourceCountsRequestRequestTypeDef,
):
    pass

GetAggregateDiscoveredResourceCountsResponseTypeDef = TypedDict(
    "GetAggregateDiscoveredResourceCountsResponseTypeDef",
    {
        "TotalDiscoveredResources": int,
        "GroupByKey": str,
        "GroupedResourceCounts": List["GroupedResourceCountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAggregateResourceConfigRequestRequestTypeDef = TypedDict(
    "GetAggregateResourceConfigRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ResourceIdentifier": "AggregateResourceIdentifierTypeDef",
    },
)

GetAggregateResourceConfigResponseTypeDef = TypedDict(
    "GetAggregateResourceConfigResponseTypeDef",
    {
        "ConfigurationItem": "ConfigurationItemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetComplianceDetailsByConfigRuleRequestRequestTypeDef = TypedDict(
    "_RequiredGetComplianceDetailsByConfigRuleRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
    },
)
_OptionalGetComplianceDetailsByConfigRuleRequestRequestTypeDef = TypedDict(
    "_OptionalGetComplianceDetailsByConfigRuleRequestRequestTypeDef",
    {
        "ComplianceTypes": List[ComplianceTypeType],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class GetComplianceDetailsByConfigRuleRequestRequestTypeDef(
    _RequiredGetComplianceDetailsByConfigRuleRequestRequestTypeDef,
    _OptionalGetComplianceDetailsByConfigRuleRequestRequestTypeDef,
):
    pass

GetComplianceDetailsByConfigRuleResponseTypeDef = TypedDict(
    "GetComplianceDetailsByConfigRuleResponseTypeDef",
    {
        "EvaluationResults": List["EvaluationResultTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetComplianceDetailsByResourceRequestRequestTypeDef = TypedDict(
    "_RequiredGetComplianceDetailsByResourceRequestRequestTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
    },
)
_OptionalGetComplianceDetailsByResourceRequestRequestTypeDef = TypedDict(
    "_OptionalGetComplianceDetailsByResourceRequestRequestTypeDef",
    {
        "ComplianceTypes": List[ComplianceTypeType],
        "NextToken": str,
    },
    total=False,
)

class GetComplianceDetailsByResourceRequestRequestTypeDef(
    _RequiredGetComplianceDetailsByResourceRequestRequestTypeDef,
    _OptionalGetComplianceDetailsByResourceRequestRequestTypeDef,
):
    pass

GetComplianceDetailsByResourceResponseTypeDef = TypedDict(
    "GetComplianceDetailsByResourceResponseTypeDef",
    {
        "EvaluationResults": List["EvaluationResultTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComplianceSummaryByConfigRuleResponseTypeDef = TypedDict(
    "GetComplianceSummaryByConfigRuleResponseTypeDef",
    {
        "ComplianceSummary": "ComplianceSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComplianceSummaryByResourceTypeRequestRequestTypeDef = TypedDict(
    "GetComplianceSummaryByResourceTypeRequestRequestTypeDef",
    {
        "ResourceTypes": List[str],
    },
    total=False,
)

GetComplianceSummaryByResourceTypeResponseTypeDef = TypedDict(
    "GetComplianceSummaryByResourceTypeResponseTypeDef",
    {
        "ComplianceSummariesByResourceType": List["ComplianceSummaryByResourceTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetConformancePackComplianceDetailsRequestRequestTypeDef = TypedDict(
    "_RequiredGetConformancePackComplianceDetailsRequestRequestTypeDef",
    {
        "ConformancePackName": str,
    },
)
_OptionalGetConformancePackComplianceDetailsRequestRequestTypeDef = TypedDict(
    "_OptionalGetConformancePackComplianceDetailsRequestRequestTypeDef",
    {
        "Filters": "ConformancePackEvaluationFiltersTypeDef",
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class GetConformancePackComplianceDetailsRequestRequestTypeDef(
    _RequiredGetConformancePackComplianceDetailsRequestRequestTypeDef,
    _OptionalGetConformancePackComplianceDetailsRequestRequestTypeDef,
):
    pass

GetConformancePackComplianceDetailsResponseTypeDef = TypedDict(
    "GetConformancePackComplianceDetailsResponseTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackRuleEvaluationResults": List["ConformancePackEvaluationResultTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetConformancePackComplianceSummaryRequestRequestTypeDef = TypedDict(
    "_RequiredGetConformancePackComplianceSummaryRequestRequestTypeDef",
    {
        "ConformancePackNames": List[str],
    },
)
_OptionalGetConformancePackComplianceSummaryRequestRequestTypeDef = TypedDict(
    "_OptionalGetConformancePackComplianceSummaryRequestRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class GetConformancePackComplianceSummaryRequestRequestTypeDef(
    _RequiredGetConformancePackComplianceSummaryRequestRequestTypeDef,
    _OptionalGetConformancePackComplianceSummaryRequestRequestTypeDef,
):
    pass

GetConformancePackComplianceSummaryResponseTypeDef = TypedDict(
    "GetConformancePackComplianceSummaryResponseTypeDef",
    {
        "ConformancePackComplianceSummaryList": List["ConformancePackComplianceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDiscoveredResourceCountsRequestRequestTypeDef = TypedDict(
    "GetDiscoveredResourceCountsRequestRequestTypeDef",
    {
        "resourceTypes": List[str],
        "limit": int,
        "nextToken": str,
    },
    total=False,
)

GetDiscoveredResourceCountsResponseTypeDef = TypedDict(
    "GetDiscoveredResourceCountsResponseTypeDef",
    {
        "totalDiscoveredResources": int,
        "resourceCounts": List["ResourceCountTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef = TypedDict(
    "_RequiredGetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef",
    {
        "OrganizationConfigRuleName": str,
    },
)
_OptionalGetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef = TypedDict(
    "_OptionalGetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef",
    {
        "Filters": "StatusDetailFiltersTypeDef",
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class GetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef(
    _RequiredGetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef,
    _OptionalGetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef,
):
    pass

GetOrganizationConfigRuleDetailedStatusResponseTypeDef = TypedDict(
    "GetOrganizationConfigRuleDetailedStatusResponseTypeDef",
    {
        "OrganizationConfigRuleDetailedStatus": List["MemberAccountStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetOrganizationConformancePackDetailedStatusRequestRequestTypeDef = TypedDict(
    "_RequiredGetOrganizationConformancePackDetailedStatusRequestRequestTypeDef",
    {
        "OrganizationConformancePackName": str,
    },
)
_OptionalGetOrganizationConformancePackDetailedStatusRequestRequestTypeDef = TypedDict(
    "_OptionalGetOrganizationConformancePackDetailedStatusRequestRequestTypeDef",
    {
        "Filters": "OrganizationResourceDetailedStatusFiltersTypeDef",
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class GetOrganizationConformancePackDetailedStatusRequestRequestTypeDef(
    _RequiredGetOrganizationConformancePackDetailedStatusRequestRequestTypeDef,
    _OptionalGetOrganizationConformancePackDetailedStatusRequestRequestTypeDef,
):
    pass

GetOrganizationConformancePackDetailedStatusResponseTypeDef = TypedDict(
    "GetOrganizationConformancePackDetailedStatusResponseTypeDef",
    {
        "OrganizationConformancePackDetailedStatuses": List[
            "OrganizationConformancePackDetailedStatusTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetResourceConfigHistoryRequestRequestTypeDef = TypedDict(
    "_RequiredGetResourceConfigHistoryRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceId": str,
    },
)
_OptionalGetResourceConfigHistoryRequestRequestTypeDef = TypedDict(
    "_OptionalGetResourceConfigHistoryRequestRequestTypeDef",
    {
        "laterTime": Union[datetime, str],
        "earlierTime": Union[datetime, str],
        "chronologicalOrder": ChronologicalOrderType,
        "limit": int,
        "nextToken": str,
    },
    total=False,
)

class GetResourceConfigHistoryRequestRequestTypeDef(
    _RequiredGetResourceConfigHistoryRequestRequestTypeDef,
    _OptionalGetResourceConfigHistoryRequestRequestTypeDef,
):
    pass

GetResourceConfigHistoryResponseTypeDef = TypedDict(
    "GetResourceConfigHistoryResponseTypeDef",
    {
        "configurationItems": List["ConfigurationItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStoredQueryRequestRequestTypeDef = TypedDict(
    "GetStoredQueryRequestRequestTypeDef",
    {
        "QueryName": str,
    },
)

GetStoredQueryResponseTypeDef = TypedDict(
    "GetStoredQueryResponseTypeDef",
    {
        "StoredQuery": "StoredQueryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupedResourceCountTypeDef = TypedDict(
    "GroupedResourceCountTypeDef",
    {
        "GroupName": str,
        "ResourceCount": int,
    },
)

_RequiredListAggregateDiscoveredResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListAggregateDiscoveredResourcesRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ResourceType": ResourceTypeType,
    },
)
_OptionalListAggregateDiscoveredResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListAggregateDiscoveredResourcesRequestRequestTypeDef",
    {
        "Filters": "ResourceFiltersTypeDef",
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class ListAggregateDiscoveredResourcesRequestRequestTypeDef(
    _RequiredListAggregateDiscoveredResourcesRequestRequestTypeDef,
    _OptionalListAggregateDiscoveredResourcesRequestRequestTypeDef,
):
    pass

ListAggregateDiscoveredResourcesResponseTypeDef = TypedDict(
    "ListAggregateDiscoveredResourcesResponseTypeDef",
    {
        "ResourceIdentifiers": List["AggregateResourceIdentifierTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDiscoveredResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListDiscoveredResourcesRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
    },
)
_OptionalListDiscoveredResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListDiscoveredResourcesRequestRequestTypeDef",
    {
        "resourceIds": List[str],
        "resourceName": str,
        "limit": int,
        "includeDeletedResources": bool,
        "nextToken": str,
    },
    total=False,
)

class ListDiscoveredResourcesRequestRequestTypeDef(
    _RequiredListDiscoveredResourcesRequestRequestTypeDef,
    _OptionalListDiscoveredResourcesRequestRequestTypeDef,
):
    pass

ListDiscoveredResourcesResponseTypeDef = TypedDict(
    "ListDiscoveredResourcesResponseTypeDef",
    {
        "resourceIdentifiers": List["ResourceIdentifierTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStoredQueriesRequestRequestTypeDef = TypedDict(
    "ListStoredQueriesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListStoredQueriesResponseTypeDef = TypedDict(
    "ListStoredQueriesResponseTypeDef",
    {
        "StoredQueryMetadata": List["StoredQueryMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class ListTagsForResourceRequestRequestTypeDef(
    _RequiredListTagsForResourceRequestRequestTypeDef,
    _OptionalListTagsForResourceRequestRequestTypeDef,
):
    pass

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMemberAccountStatusTypeDef = TypedDict(
    "_RequiredMemberAccountStatusTypeDef",
    {
        "AccountId": str,
        "ConfigRuleName": str,
        "MemberAccountRuleStatus": MemberAccountRuleStatusType,
    },
)
_OptionalMemberAccountStatusTypeDef = TypedDict(
    "_OptionalMemberAccountStatusTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "LastUpdateTime": datetime,
    },
    total=False,
)

class MemberAccountStatusTypeDef(
    _RequiredMemberAccountStatusTypeDef, _OptionalMemberAccountStatusTypeDef
):
    pass

_RequiredOrganizationAggregationSourceTypeDef = TypedDict(
    "_RequiredOrganizationAggregationSourceTypeDef",
    {
        "RoleArn": str,
    },
)
_OptionalOrganizationAggregationSourceTypeDef = TypedDict(
    "_OptionalOrganizationAggregationSourceTypeDef",
    {
        "AwsRegions": List[str],
        "AllAwsRegions": bool,
    },
    total=False,
)

class OrganizationAggregationSourceTypeDef(
    _RequiredOrganizationAggregationSourceTypeDef, _OptionalOrganizationAggregationSourceTypeDef
):
    pass

_RequiredOrganizationConfigRuleStatusTypeDef = TypedDict(
    "_RequiredOrganizationConfigRuleStatusTypeDef",
    {
        "OrganizationConfigRuleName": str,
        "OrganizationRuleStatus": OrganizationRuleStatusType,
    },
)
_OptionalOrganizationConfigRuleStatusTypeDef = TypedDict(
    "_OptionalOrganizationConfigRuleStatusTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "LastUpdateTime": datetime,
    },
    total=False,
)

class OrganizationConfigRuleStatusTypeDef(
    _RequiredOrganizationConfigRuleStatusTypeDef, _OptionalOrganizationConfigRuleStatusTypeDef
):
    pass

_RequiredOrganizationConfigRuleTypeDef = TypedDict(
    "_RequiredOrganizationConfigRuleTypeDef",
    {
        "OrganizationConfigRuleName": str,
        "OrganizationConfigRuleArn": str,
    },
)
_OptionalOrganizationConfigRuleTypeDef = TypedDict(
    "_OptionalOrganizationConfigRuleTypeDef",
    {
        "OrganizationManagedRuleMetadata": "OrganizationManagedRuleMetadataTypeDef",
        "OrganizationCustomRuleMetadata": "OrganizationCustomRuleMetadataTypeDef",
        "ExcludedAccounts": List[str],
        "LastUpdateTime": datetime,
    },
    total=False,
)

class OrganizationConfigRuleTypeDef(
    _RequiredOrganizationConfigRuleTypeDef, _OptionalOrganizationConfigRuleTypeDef
):
    pass

_RequiredOrganizationConformancePackDetailedStatusTypeDef = TypedDict(
    "_RequiredOrganizationConformancePackDetailedStatusTypeDef",
    {
        "AccountId": str,
        "ConformancePackName": str,
        "Status": OrganizationResourceDetailedStatusType,
    },
)
_OptionalOrganizationConformancePackDetailedStatusTypeDef = TypedDict(
    "_OptionalOrganizationConformancePackDetailedStatusTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "LastUpdateTime": datetime,
    },
    total=False,
)

class OrganizationConformancePackDetailedStatusTypeDef(
    _RequiredOrganizationConformancePackDetailedStatusTypeDef,
    _OptionalOrganizationConformancePackDetailedStatusTypeDef,
):
    pass

_RequiredOrganizationConformancePackStatusTypeDef = TypedDict(
    "_RequiredOrganizationConformancePackStatusTypeDef",
    {
        "OrganizationConformancePackName": str,
        "Status": OrganizationResourceStatusType,
    },
)
_OptionalOrganizationConformancePackStatusTypeDef = TypedDict(
    "_OptionalOrganizationConformancePackStatusTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "LastUpdateTime": datetime,
    },
    total=False,
)

class OrganizationConformancePackStatusTypeDef(
    _RequiredOrganizationConformancePackStatusTypeDef,
    _OptionalOrganizationConformancePackStatusTypeDef,
):
    pass

_RequiredOrganizationConformancePackTypeDef = TypedDict(
    "_RequiredOrganizationConformancePackTypeDef",
    {
        "OrganizationConformancePackName": str,
        "OrganizationConformancePackArn": str,
        "LastUpdateTime": datetime,
    },
)
_OptionalOrganizationConformancePackTypeDef = TypedDict(
    "_OptionalOrganizationConformancePackTypeDef",
    {
        "DeliveryS3Bucket": str,
        "DeliveryS3KeyPrefix": str,
        "ConformancePackInputParameters": List["ConformancePackInputParameterTypeDef"],
        "ExcludedAccounts": List[str],
    },
    total=False,
)

class OrganizationConformancePackTypeDef(
    _RequiredOrganizationConformancePackTypeDef, _OptionalOrganizationConformancePackTypeDef
):
    pass

_RequiredOrganizationCustomRuleMetadataTypeDef = TypedDict(
    "_RequiredOrganizationCustomRuleMetadataTypeDef",
    {
        "LambdaFunctionArn": str,
        "OrganizationConfigRuleTriggerTypes": List[OrganizationConfigRuleTriggerTypeType],
    },
)
_OptionalOrganizationCustomRuleMetadataTypeDef = TypedDict(
    "_OptionalOrganizationCustomRuleMetadataTypeDef",
    {
        "Description": str,
        "InputParameters": str,
        "MaximumExecutionFrequency": MaximumExecutionFrequencyType,
        "ResourceTypesScope": List[str],
        "ResourceIdScope": str,
        "TagKeyScope": str,
        "TagValueScope": str,
    },
    total=False,
)

class OrganizationCustomRuleMetadataTypeDef(
    _RequiredOrganizationCustomRuleMetadataTypeDef, _OptionalOrganizationCustomRuleMetadataTypeDef
):
    pass

_RequiredOrganizationManagedRuleMetadataTypeDef = TypedDict(
    "_RequiredOrganizationManagedRuleMetadataTypeDef",
    {
        "RuleIdentifier": str,
    },
)
_OptionalOrganizationManagedRuleMetadataTypeDef = TypedDict(
    "_OptionalOrganizationManagedRuleMetadataTypeDef",
    {
        "Description": str,
        "InputParameters": str,
        "MaximumExecutionFrequency": MaximumExecutionFrequencyType,
        "ResourceTypesScope": List[str],
        "ResourceIdScope": str,
        "TagKeyScope": str,
        "TagValueScope": str,
    },
    total=False,
)

class OrganizationManagedRuleMetadataTypeDef(
    _RequiredOrganizationManagedRuleMetadataTypeDef, _OptionalOrganizationManagedRuleMetadataTypeDef
):
    pass

OrganizationResourceDetailedStatusFiltersTypeDef = TypedDict(
    "OrganizationResourceDetailedStatusFiltersTypeDef",
    {
        "AccountId": str,
        "Status": OrganizationResourceDetailedStatusType,
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

PendingAggregationRequestTypeDef = TypedDict(
    "PendingAggregationRequestTypeDef",
    {
        "RequesterAccountId": str,
        "RequesterAwsRegion": str,
    },
    total=False,
)

_RequiredPutAggregationAuthorizationRequestRequestTypeDef = TypedDict(
    "_RequiredPutAggregationAuthorizationRequestRequestTypeDef",
    {
        "AuthorizedAccountId": str,
        "AuthorizedAwsRegion": str,
    },
)
_OptionalPutAggregationAuthorizationRequestRequestTypeDef = TypedDict(
    "_OptionalPutAggregationAuthorizationRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class PutAggregationAuthorizationRequestRequestTypeDef(
    _RequiredPutAggregationAuthorizationRequestRequestTypeDef,
    _OptionalPutAggregationAuthorizationRequestRequestTypeDef,
):
    pass

PutAggregationAuthorizationResponseTypeDef = TypedDict(
    "PutAggregationAuthorizationResponseTypeDef",
    {
        "AggregationAuthorization": "AggregationAuthorizationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutConfigRuleRequestRequestTypeDef = TypedDict(
    "_RequiredPutConfigRuleRequestRequestTypeDef",
    {
        "ConfigRule": "ConfigRuleTypeDef",
    },
)
_OptionalPutConfigRuleRequestRequestTypeDef = TypedDict(
    "_OptionalPutConfigRuleRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class PutConfigRuleRequestRequestTypeDef(
    _RequiredPutConfigRuleRequestRequestTypeDef, _OptionalPutConfigRuleRequestRequestTypeDef
):
    pass

_RequiredPutConfigurationAggregatorRequestRequestTypeDef = TypedDict(
    "_RequiredPutConfigurationAggregatorRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
_OptionalPutConfigurationAggregatorRequestRequestTypeDef = TypedDict(
    "_OptionalPutConfigurationAggregatorRequestRequestTypeDef",
    {
        "AccountAggregationSources": List["AccountAggregationSourceTypeDef"],
        "OrganizationAggregationSource": "OrganizationAggregationSourceTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class PutConfigurationAggregatorRequestRequestTypeDef(
    _RequiredPutConfigurationAggregatorRequestRequestTypeDef,
    _OptionalPutConfigurationAggregatorRequestRequestTypeDef,
):
    pass

PutConfigurationAggregatorResponseTypeDef = TypedDict(
    "PutConfigurationAggregatorResponseTypeDef",
    {
        "ConfigurationAggregator": "ConfigurationAggregatorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutConfigurationRecorderRequestRequestTypeDef = TypedDict(
    "PutConfigurationRecorderRequestRequestTypeDef",
    {
        "ConfigurationRecorder": "ConfigurationRecorderTypeDef",
    },
)

_RequiredPutConformancePackRequestRequestTypeDef = TypedDict(
    "_RequiredPutConformancePackRequestRequestTypeDef",
    {
        "ConformancePackName": str,
    },
)
_OptionalPutConformancePackRequestRequestTypeDef = TypedDict(
    "_OptionalPutConformancePackRequestRequestTypeDef",
    {
        "TemplateS3Uri": str,
        "TemplateBody": str,
        "DeliveryS3Bucket": str,
        "DeliveryS3KeyPrefix": str,
        "ConformancePackInputParameters": List["ConformancePackInputParameterTypeDef"],
    },
    total=False,
)

class PutConformancePackRequestRequestTypeDef(
    _RequiredPutConformancePackRequestRequestTypeDef,
    _OptionalPutConformancePackRequestRequestTypeDef,
):
    pass

PutConformancePackResponseTypeDef = TypedDict(
    "PutConformancePackResponseTypeDef",
    {
        "ConformancePackArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutDeliveryChannelRequestRequestTypeDef = TypedDict(
    "PutDeliveryChannelRequestRequestTypeDef",
    {
        "DeliveryChannel": "DeliveryChannelTypeDef",
    },
)

_RequiredPutEvaluationsRequestRequestTypeDef = TypedDict(
    "_RequiredPutEvaluationsRequestRequestTypeDef",
    {
        "ResultToken": str,
    },
)
_OptionalPutEvaluationsRequestRequestTypeDef = TypedDict(
    "_OptionalPutEvaluationsRequestRequestTypeDef",
    {
        "Evaluations": List["EvaluationTypeDef"],
        "TestMode": bool,
    },
    total=False,
)

class PutEvaluationsRequestRequestTypeDef(
    _RequiredPutEvaluationsRequestRequestTypeDef, _OptionalPutEvaluationsRequestRequestTypeDef
):
    pass

PutEvaluationsResponseTypeDef = TypedDict(
    "PutEvaluationsResponseTypeDef",
    {
        "FailedEvaluations": List["EvaluationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutExternalEvaluationRequestRequestTypeDef = TypedDict(
    "PutExternalEvaluationRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ExternalEvaluation": "ExternalEvaluationTypeDef",
    },
)

_RequiredPutOrganizationConfigRuleRequestRequestTypeDef = TypedDict(
    "_RequiredPutOrganizationConfigRuleRequestRequestTypeDef",
    {
        "OrganizationConfigRuleName": str,
    },
)
_OptionalPutOrganizationConfigRuleRequestRequestTypeDef = TypedDict(
    "_OptionalPutOrganizationConfigRuleRequestRequestTypeDef",
    {
        "OrganizationManagedRuleMetadata": "OrganizationManagedRuleMetadataTypeDef",
        "OrganizationCustomRuleMetadata": "OrganizationCustomRuleMetadataTypeDef",
        "ExcludedAccounts": List[str],
    },
    total=False,
)

class PutOrganizationConfigRuleRequestRequestTypeDef(
    _RequiredPutOrganizationConfigRuleRequestRequestTypeDef,
    _OptionalPutOrganizationConfigRuleRequestRequestTypeDef,
):
    pass

PutOrganizationConfigRuleResponseTypeDef = TypedDict(
    "PutOrganizationConfigRuleResponseTypeDef",
    {
        "OrganizationConfigRuleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutOrganizationConformancePackRequestRequestTypeDef = TypedDict(
    "_RequiredPutOrganizationConformancePackRequestRequestTypeDef",
    {
        "OrganizationConformancePackName": str,
    },
)
_OptionalPutOrganizationConformancePackRequestRequestTypeDef = TypedDict(
    "_OptionalPutOrganizationConformancePackRequestRequestTypeDef",
    {
        "TemplateS3Uri": str,
        "TemplateBody": str,
        "DeliveryS3Bucket": str,
        "DeliveryS3KeyPrefix": str,
        "ConformancePackInputParameters": List["ConformancePackInputParameterTypeDef"],
        "ExcludedAccounts": List[str],
    },
    total=False,
)

class PutOrganizationConformancePackRequestRequestTypeDef(
    _RequiredPutOrganizationConformancePackRequestRequestTypeDef,
    _OptionalPutOrganizationConformancePackRequestRequestTypeDef,
):
    pass

PutOrganizationConformancePackResponseTypeDef = TypedDict(
    "PutOrganizationConformancePackResponseTypeDef",
    {
        "OrganizationConformancePackArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRemediationConfigurationsRequestRequestTypeDef = TypedDict(
    "PutRemediationConfigurationsRequestRequestTypeDef",
    {
        "RemediationConfigurations": List["RemediationConfigurationTypeDef"],
    },
)

PutRemediationConfigurationsResponseTypeDef = TypedDict(
    "PutRemediationConfigurationsResponseTypeDef",
    {
        "FailedBatches": List["FailedRemediationBatchTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutRemediationExceptionsRequestRequestTypeDef = TypedDict(
    "_RequiredPutRemediationExceptionsRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceKeys": List["RemediationExceptionResourceKeyTypeDef"],
    },
)
_OptionalPutRemediationExceptionsRequestRequestTypeDef = TypedDict(
    "_OptionalPutRemediationExceptionsRequestRequestTypeDef",
    {
        "Message": str,
        "ExpirationTime": Union[datetime, str],
    },
    total=False,
)

class PutRemediationExceptionsRequestRequestTypeDef(
    _RequiredPutRemediationExceptionsRequestRequestTypeDef,
    _OptionalPutRemediationExceptionsRequestRequestTypeDef,
):
    pass

PutRemediationExceptionsResponseTypeDef = TypedDict(
    "PutRemediationExceptionsResponseTypeDef",
    {
        "FailedBatches": List["FailedRemediationExceptionBatchTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutResourceConfigRequestRequestTypeDef = TypedDict(
    "_RequiredPutResourceConfigRequestRequestTypeDef",
    {
        "ResourceType": str,
        "SchemaVersionId": str,
        "ResourceId": str,
        "Configuration": str,
    },
)
_OptionalPutResourceConfigRequestRequestTypeDef = TypedDict(
    "_OptionalPutResourceConfigRequestRequestTypeDef",
    {
        "ResourceName": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class PutResourceConfigRequestRequestTypeDef(
    _RequiredPutResourceConfigRequestRequestTypeDef, _OptionalPutResourceConfigRequestRequestTypeDef
):
    pass

PutRetentionConfigurationRequestRequestTypeDef = TypedDict(
    "PutRetentionConfigurationRequestRequestTypeDef",
    {
        "RetentionPeriodInDays": int,
    },
)

PutRetentionConfigurationResponseTypeDef = TypedDict(
    "PutRetentionConfigurationResponseTypeDef",
    {
        "RetentionConfiguration": "RetentionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutStoredQueryRequestRequestTypeDef = TypedDict(
    "_RequiredPutStoredQueryRequestRequestTypeDef",
    {
        "StoredQuery": "StoredQueryTypeDef",
    },
)
_OptionalPutStoredQueryRequestRequestTypeDef = TypedDict(
    "_OptionalPutStoredQueryRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class PutStoredQueryRequestRequestTypeDef(
    _RequiredPutStoredQueryRequestRequestTypeDef, _OptionalPutStoredQueryRequestRequestTypeDef
):
    pass

PutStoredQueryResponseTypeDef = TypedDict(
    "PutStoredQueryResponseTypeDef",
    {
        "QueryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QueryInfoTypeDef = TypedDict(
    "QueryInfoTypeDef",
    {
        "SelectFields": List["FieldInfoTypeDef"],
    },
    total=False,
)

RecordingGroupTypeDef = TypedDict(
    "RecordingGroupTypeDef",
    {
        "allSupported": bool,
        "includeGlobalResourceTypes": bool,
        "resourceTypes": List[ResourceTypeType],
    },
    total=False,
)

RelationshipTypeDef = TypedDict(
    "RelationshipTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceId": str,
        "resourceName": str,
        "relationshipName": str,
    },
    total=False,
)

_RequiredRemediationConfigurationTypeDef = TypedDict(
    "_RequiredRemediationConfigurationTypeDef",
    {
        "ConfigRuleName": str,
        "TargetType": Literal["SSM_DOCUMENT"],
        "TargetId": str,
    },
)
_OptionalRemediationConfigurationTypeDef = TypedDict(
    "_OptionalRemediationConfigurationTypeDef",
    {
        "TargetVersion": str,
        "Parameters": Dict[str, "RemediationParameterValueTypeDef"],
        "ResourceType": str,
        "Automatic": bool,
        "ExecutionControls": "ExecutionControlsTypeDef",
        "MaximumAutomaticAttempts": int,
        "RetryAttemptSeconds": int,
        "Arn": str,
        "CreatedByService": str,
    },
    total=False,
)

class RemediationConfigurationTypeDef(
    _RequiredRemediationConfigurationTypeDef, _OptionalRemediationConfigurationTypeDef
):
    pass

RemediationExceptionResourceKeyTypeDef = TypedDict(
    "RemediationExceptionResourceKeyTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
    },
    total=False,
)

_RequiredRemediationExceptionTypeDef = TypedDict(
    "_RequiredRemediationExceptionTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceType": str,
        "ResourceId": str,
    },
)
_OptionalRemediationExceptionTypeDef = TypedDict(
    "_OptionalRemediationExceptionTypeDef",
    {
        "Message": str,
        "ExpirationTime": datetime,
    },
    total=False,
)

class RemediationExceptionTypeDef(
    _RequiredRemediationExceptionTypeDef, _OptionalRemediationExceptionTypeDef
):
    pass

RemediationExecutionStatusTypeDef = TypedDict(
    "RemediationExecutionStatusTypeDef",
    {
        "ResourceKey": "ResourceKeyTypeDef",
        "State": RemediationExecutionStateType,
        "StepDetails": List["RemediationExecutionStepTypeDef"],
        "InvocationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

RemediationExecutionStepTypeDef = TypedDict(
    "RemediationExecutionStepTypeDef",
    {
        "Name": str,
        "State": RemediationExecutionStepStateType,
        "ErrorMessage": str,
        "StartTime": datetime,
        "StopTime": datetime,
    },
    total=False,
)

RemediationParameterValueTypeDef = TypedDict(
    "RemediationParameterValueTypeDef",
    {
        "ResourceValue": "ResourceValueTypeDef",
        "StaticValue": "StaticValueTypeDef",
    },
    total=False,
)

ResourceCountFiltersTypeDef = TypedDict(
    "ResourceCountFiltersTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "AccountId": str,
        "Region": str,
    },
    total=False,
)

ResourceCountTypeDef = TypedDict(
    "ResourceCountTypeDef",
    {
        "resourceType": ResourceTypeType,
        "count": int,
    },
    total=False,
)

ResourceFiltersTypeDef = TypedDict(
    "ResourceFiltersTypeDef",
    {
        "AccountId": str,
        "ResourceId": str,
        "ResourceName": str,
        "Region": str,
    },
    total=False,
)

ResourceIdentifierTypeDef = TypedDict(
    "ResourceIdentifierTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceId": str,
        "resourceName": str,
        "resourceDeletionTime": datetime,
    },
    total=False,
)

ResourceKeyTypeDef = TypedDict(
    "ResourceKeyTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceId": str,
    },
)

ResourceValueTypeDef = TypedDict(
    "ResourceValueTypeDef",
    {
        "Value": Literal["RESOURCE_ID"],
    },
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

RetentionConfigurationTypeDef = TypedDict(
    "RetentionConfigurationTypeDef",
    {
        "Name": str,
        "RetentionPeriodInDays": int,
    },
)

ScopeTypeDef = TypedDict(
    "ScopeTypeDef",
    {
        "ComplianceResourceTypes": List[str],
        "TagKey": str,
        "TagValue": str,
        "ComplianceResourceId": str,
    },
    total=False,
)

_RequiredSelectAggregateResourceConfigRequestRequestTypeDef = TypedDict(
    "_RequiredSelectAggregateResourceConfigRequestRequestTypeDef",
    {
        "Expression": str,
        "ConfigurationAggregatorName": str,
    },
)
_OptionalSelectAggregateResourceConfigRequestRequestTypeDef = TypedDict(
    "_OptionalSelectAggregateResourceConfigRequestRequestTypeDef",
    {
        "Limit": int,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class SelectAggregateResourceConfigRequestRequestTypeDef(
    _RequiredSelectAggregateResourceConfigRequestRequestTypeDef,
    _OptionalSelectAggregateResourceConfigRequestRequestTypeDef,
):
    pass

SelectAggregateResourceConfigResponseTypeDef = TypedDict(
    "SelectAggregateResourceConfigResponseTypeDef",
    {
        "Results": List[str],
        "QueryInfo": "QueryInfoTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSelectResourceConfigRequestRequestTypeDef = TypedDict(
    "_RequiredSelectResourceConfigRequestRequestTypeDef",
    {
        "Expression": str,
    },
)
_OptionalSelectResourceConfigRequestRequestTypeDef = TypedDict(
    "_OptionalSelectResourceConfigRequestRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class SelectResourceConfigRequestRequestTypeDef(
    _RequiredSelectResourceConfigRequestRequestTypeDef,
    _OptionalSelectResourceConfigRequestRequestTypeDef,
):
    pass

SelectResourceConfigResponseTypeDef = TypedDict(
    "SelectResourceConfigResponseTypeDef",
    {
        "Results": List[str],
        "QueryInfo": "QueryInfoTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SourceDetailTypeDef = TypedDict(
    "SourceDetailTypeDef",
    {
        "EventSource": Literal["aws.config"],
        "MessageType": MessageTypeType,
        "MaximumExecutionFrequency": MaximumExecutionFrequencyType,
    },
    total=False,
)

_RequiredSourceTypeDef = TypedDict(
    "_RequiredSourceTypeDef",
    {
        "Owner": OwnerType,
        "SourceIdentifier": str,
    },
)
_OptionalSourceTypeDef = TypedDict(
    "_OptionalSourceTypeDef",
    {
        "SourceDetails": List["SourceDetailTypeDef"],
    },
    total=False,
)

class SourceTypeDef(_RequiredSourceTypeDef, _OptionalSourceTypeDef):
    pass

SsmControlsTypeDef = TypedDict(
    "SsmControlsTypeDef",
    {
        "ConcurrentExecutionRatePercentage": int,
        "ErrorPercentage": int,
    },
    total=False,
)

StartConfigRulesEvaluationRequestRequestTypeDef = TypedDict(
    "StartConfigRulesEvaluationRequestRequestTypeDef",
    {
        "ConfigRuleNames": List[str],
    },
    total=False,
)

StartConfigurationRecorderRequestRequestTypeDef = TypedDict(
    "StartConfigurationRecorderRequestRequestTypeDef",
    {
        "ConfigurationRecorderName": str,
    },
)

StartRemediationExecutionRequestRequestTypeDef = TypedDict(
    "StartRemediationExecutionRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceKeys": List["ResourceKeyTypeDef"],
    },
)

StartRemediationExecutionResponseTypeDef = TypedDict(
    "StartRemediationExecutionResponseTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List["ResourceKeyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StaticValueTypeDef = TypedDict(
    "StaticValueTypeDef",
    {
        "Values": List[str],
    },
)

StatusDetailFiltersTypeDef = TypedDict(
    "StatusDetailFiltersTypeDef",
    {
        "AccountId": str,
        "MemberAccountRuleStatus": MemberAccountRuleStatusType,
    },
    total=False,
)

StopConfigurationRecorderRequestRequestTypeDef = TypedDict(
    "StopConfigurationRecorderRequestRequestTypeDef",
    {
        "ConfigurationRecorderName": str,
    },
)

_RequiredStoredQueryMetadataTypeDef = TypedDict(
    "_RequiredStoredQueryMetadataTypeDef",
    {
        "QueryId": str,
        "QueryArn": str,
        "QueryName": str,
    },
)
_OptionalStoredQueryMetadataTypeDef = TypedDict(
    "_OptionalStoredQueryMetadataTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class StoredQueryMetadataTypeDef(
    _RequiredStoredQueryMetadataTypeDef, _OptionalStoredQueryMetadataTypeDef
):
    pass

_RequiredStoredQueryTypeDef = TypedDict(
    "_RequiredStoredQueryTypeDef",
    {
        "QueryName": str,
    },
)
_OptionalStoredQueryTypeDef = TypedDict(
    "_OptionalStoredQueryTypeDef",
    {
        "QueryId": str,
        "QueryArn": str,
        "Description": str,
        "Expression": str,
    },
    total=False,
)

class StoredQueryTypeDef(_RequiredStoredQueryTypeDef, _OptionalStoredQueryTypeDef):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)
