"""
Type annotations for iot service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iot.type_defs import AbortConfigTypeDef

    data: AbortConfigTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ActionTypeType,
    AuditCheckRunStatusType,
    AuditFindingSeverityType,
    AuditFrequencyType,
    AuditMitigationActionsExecutionStatusType,
    AuditMitigationActionsTaskStatusType,
    AuditTaskStatusType,
    AuditTaskTypeType,
    AuthDecisionType,
    AuthorizerStatusType,
    AutoRegistrationStatusType,
    AwsJobAbortCriteriaFailureTypeType,
    BehaviorCriteriaTypeType,
    CACertificateStatusType,
    CannedAccessControlListType,
    CertificateModeType,
    CertificateStatusType,
    ComparisonOperatorType,
    ConfidenceLevelType,
    CustomMetricTypeType,
    DayOfWeekType,
    DetectMitigationActionExecutionStatusType,
    DetectMitigationActionsTaskStatusType,
    DimensionValueOperatorType,
    DomainConfigurationStatusType,
    DomainTypeType,
    DynamicGroupStatusType,
    DynamoKeyTypeType,
    EventTypeType,
    FieldTypeType,
    IndexStatusType,
    JobExecutionFailureTypeType,
    JobExecutionStatusType,
    JobStatusType,
    LogLevelType,
    LogTargetTypeType,
    MessageFormatType,
    MitigationActionTypeType,
    ModelStatusType,
    OTAUpdateStatusType,
    ProtocolType,
    ReportTypeType,
    ResourceTypeType,
    ServerCertificateStatusType,
    ServiceTypeType,
    StatusType,
    TargetSelectionType,
    ThingConnectivityIndexingModeType,
    ThingGroupIndexingModeType,
    ThingIndexingModeType,
    TopicRuleDestinationStatusType,
    ViolationEventTypeType,
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
    "AbortConfigTypeDef",
    "AbortCriteriaTypeDef",
    "AcceptCertificateTransferRequestRequestTypeDef",
    "ActionTypeDef",
    "ActiveViolationTypeDef",
    "AddThingToBillingGroupRequestRequestTypeDef",
    "AddThingToThingGroupRequestRequestTypeDef",
    "AddThingsToThingGroupParamsTypeDef",
    "AlertTargetTypeDef",
    "AllowedTypeDef",
    "AssetPropertyTimestampTypeDef",
    "AssetPropertyValueTypeDef",
    "AssetPropertyVariantTypeDef",
    "AssociateTargetsWithJobRequestRequestTypeDef",
    "AssociateTargetsWithJobResponseTypeDef",
    "AttachPolicyRequestRequestTypeDef",
    "AttachPrincipalPolicyRequestRequestTypeDef",
    "AttachSecurityProfileRequestRequestTypeDef",
    "AttachThingPrincipalRequestRequestTypeDef",
    "AttributePayloadTypeDef",
    "AuditCheckConfigurationTypeDef",
    "AuditCheckDetailsTypeDef",
    "AuditFindingTypeDef",
    "AuditMitigationActionExecutionMetadataTypeDef",
    "AuditMitigationActionsTaskMetadataTypeDef",
    "AuditMitigationActionsTaskTargetTypeDef",
    "AuditNotificationTargetTypeDef",
    "AuditSuppressionTypeDef",
    "AuditTaskMetadataTypeDef",
    "AuthInfoTypeDef",
    "AuthResultTypeDef",
    "AuthorizerConfigTypeDef",
    "AuthorizerDescriptionTypeDef",
    "AuthorizerSummaryTypeDef",
    "AwsJobAbortConfigTypeDef",
    "AwsJobAbortCriteriaTypeDef",
    "AwsJobExecutionsRolloutConfigTypeDef",
    "AwsJobExponentialRolloutRateTypeDef",
    "AwsJobPresignedUrlConfigTypeDef",
    "AwsJobRateIncreaseCriteriaTypeDef",
    "AwsJobTimeoutConfigTypeDef",
    "BehaviorCriteriaTypeDef",
    "BehaviorModelTrainingSummaryTypeDef",
    "BehaviorTypeDef",
    "BillingGroupMetadataTypeDef",
    "BillingGroupPropertiesTypeDef",
    "CACertificateDescriptionTypeDef",
    "CACertificateTypeDef",
    "CancelAuditMitigationActionsTaskRequestRequestTypeDef",
    "CancelAuditTaskRequestRequestTypeDef",
    "CancelCertificateTransferRequestRequestTypeDef",
    "CancelDetectMitigationActionsTaskRequestRequestTypeDef",
    "CancelJobExecutionRequestRequestTypeDef",
    "CancelJobRequestRequestTypeDef",
    "CancelJobResponseTypeDef",
    "CertificateDescriptionTypeDef",
    "CertificateTypeDef",
    "CertificateValidityTypeDef",
    "CloudwatchAlarmActionTypeDef",
    "CloudwatchLogsActionTypeDef",
    "CloudwatchMetricActionTypeDef",
    "CodeSigningCertificateChainTypeDef",
    "CodeSigningSignatureTypeDef",
    "CodeSigningTypeDef",
    "ConfigurationTypeDef",
    "ConfirmTopicRuleDestinationRequestRequestTypeDef",
    "CreateAuditSuppressionRequestRequestTypeDef",
    "CreateAuthorizerRequestRequestTypeDef",
    "CreateAuthorizerResponseTypeDef",
    "CreateBillingGroupRequestRequestTypeDef",
    "CreateBillingGroupResponseTypeDef",
    "CreateCertificateFromCsrRequestRequestTypeDef",
    "CreateCertificateFromCsrResponseTypeDef",
    "CreateCustomMetricRequestRequestTypeDef",
    "CreateCustomMetricResponseTypeDef",
    "CreateDimensionRequestRequestTypeDef",
    "CreateDimensionResponseTypeDef",
    "CreateDomainConfigurationRequestRequestTypeDef",
    "CreateDomainConfigurationResponseTypeDef",
    "CreateDynamicThingGroupRequestRequestTypeDef",
    "CreateDynamicThingGroupResponseTypeDef",
    "CreateJobRequestRequestTypeDef",
    "CreateJobResponseTypeDef",
    "CreateJobTemplateRequestRequestTypeDef",
    "CreateJobTemplateResponseTypeDef",
    "CreateKeysAndCertificateRequestRequestTypeDef",
    "CreateKeysAndCertificateResponseTypeDef",
    "CreateMitigationActionRequestRequestTypeDef",
    "CreateMitigationActionResponseTypeDef",
    "CreateOTAUpdateRequestRequestTypeDef",
    "CreateOTAUpdateResponseTypeDef",
    "CreatePolicyRequestRequestTypeDef",
    "CreatePolicyResponseTypeDef",
    "CreatePolicyVersionRequestRequestTypeDef",
    "CreatePolicyVersionResponseTypeDef",
    "CreateProvisioningClaimRequestRequestTypeDef",
    "CreateProvisioningClaimResponseTypeDef",
    "CreateProvisioningTemplateRequestRequestTypeDef",
    "CreateProvisioningTemplateResponseTypeDef",
    "CreateProvisioningTemplateVersionRequestRequestTypeDef",
    "CreateProvisioningTemplateVersionResponseTypeDef",
    "CreateRoleAliasRequestRequestTypeDef",
    "CreateRoleAliasResponseTypeDef",
    "CreateScheduledAuditRequestRequestTypeDef",
    "CreateScheduledAuditResponseTypeDef",
    "CreateSecurityProfileRequestRequestTypeDef",
    "CreateSecurityProfileResponseTypeDef",
    "CreateStreamRequestRequestTypeDef",
    "CreateStreamResponseTypeDef",
    "CreateThingGroupRequestRequestTypeDef",
    "CreateThingGroupResponseTypeDef",
    "CreateThingRequestRequestTypeDef",
    "CreateThingResponseTypeDef",
    "CreateThingTypeRequestRequestTypeDef",
    "CreateThingTypeResponseTypeDef",
    "CreateTopicRuleDestinationRequestRequestTypeDef",
    "CreateTopicRuleDestinationResponseTypeDef",
    "CreateTopicRuleRequestRequestTypeDef",
    "CustomCodeSigningTypeDef",
    "DeleteAccountAuditConfigurationRequestRequestTypeDef",
    "DeleteAuditSuppressionRequestRequestTypeDef",
    "DeleteAuthorizerRequestRequestTypeDef",
    "DeleteBillingGroupRequestRequestTypeDef",
    "DeleteCACertificateRequestRequestTypeDef",
    "DeleteCertificateRequestRequestTypeDef",
    "DeleteCustomMetricRequestRequestTypeDef",
    "DeleteDimensionRequestRequestTypeDef",
    "DeleteDomainConfigurationRequestRequestTypeDef",
    "DeleteDynamicThingGroupRequestRequestTypeDef",
    "DeleteJobExecutionRequestRequestTypeDef",
    "DeleteJobRequestRequestTypeDef",
    "DeleteJobTemplateRequestRequestTypeDef",
    "DeleteMitigationActionRequestRequestTypeDef",
    "DeleteOTAUpdateRequestRequestTypeDef",
    "DeletePolicyRequestRequestTypeDef",
    "DeletePolicyVersionRequestRequestTypeDef",
    "DeleteProvisioningTemplateRequestRequestTypeDef",
    "DeleteProvisioningTemplateVersionRequestRequestTypeDef",
    "DeleteRoleAliasRequestRequestTypeDef",
    "DeleteScheduledAuditRequestRequestTypeDef",
    "DeleteSecurityProfileRequestRequestTypeDef",
    "DeleteStreamRequestRequestTypeDef",
    "DeleteThingGroupRequestRequestTypeDef",
    "DeleteThingRequestRequestTypeDef",
    "DeleteThingTypeRequestRequestTypeDef",
    "DeleteTopicRuleDestinationRequestRequestTypeDef",
    "DeleteTopicRuleRequestRequestTypeDef",
    "DeleteV2LoggingLevelRequestRequestTypeDef",
    "DeniedTypeDef",
    "DeprecateThingTypeRequestRequestTypeDef",
    "DescribeAccountAuditConfigurationResponseTypeDef",
    "DescribeAuditFindingRequestRequestTypeDef",
    "DescribeAuditFindingResponseTypeDef",
    "DescribeAuditMitigationActionsTaskRequestRequestTypeDef",
    "DescribeAuditMitigationActionsTaskResponseTypeDef",
    "DescribeAuditSuppressionRequestRequestTypeDef",
    "DescribeAuditSuppressionResponseTypeDef",
    "DescribeAuditTaskRequestRequestTypeDef",
    "DescribeAuditTaskResponseTypeDef",
    "DescribeAuthorizerRequestRequestTypeDef",
    "DescribeAuthorizerResponseTypeDef",
    "DescribeBillingGroupRequestRequestTypeDef",
    "DescribeBillingGroupResponseTypeDef",
    "DescribeCACertificateRequestRequestTypeDef",
    "DescribeCACertificateResponseTypeDef",
    "DescribeCertificateRequestRequestTypeDef",
    "DescribeCertificateResponseTypeDef",
    "DescribeCustomMetricRequestRequestTypeDef",
    "DescribeCustomMetricResponseTypeDef",
    "DescribeDefaultAuthorizerResponseTypeDef",
    "DescribeDetectMitigationActionsTaskRequestRequestTypeDef",
    "DescribeDetectMitigationActionsTaskResponseTypeDef",
    "DescribeDimensionRequestRequestTypeDef",
    "DescribeDimensionResponseTypeDef",
    "DescribeDomainConfigurationRequestRequestTypeDef",
    "DescribeDomainConfigurationResponseTypeDef",
    "DescribeEndpointRequestRequestTypeDef",
    "DescribeEndpointResponseTypeDef",
    "DescribeEventConfigurationsResponseTypeDef",
    "DescribeIndexRequestRequestTypeDef",
    "DescribeIndexResponseTypeDef",
    "DescribeJobExecutionRequestRequestTypeDef",
    "DescribeJobExecutionResponseTypeDef",
    "DescribeJobRequestRequestTypeDef",
    "DescribeJobResponseTypeDef",
    "DescribeJobTemplateRequestRequestTypeDef",
    "DescribeJobTemplateResponseTypeDef",
    "DescribeMitigationActionRequestRequestTypeDef",
    "DescribeMitigationActionResponseTypeDef",
    "DescribeProvisioningTemplateRequestRequestTypeDef",
    "DescribeProvisioningTemplateResponseTypeDef",
    "DescribeProvisioningTemplateVersionRequestRequestTypeDef",
    "DescribeProvisioningTemplateVersionResponseTypeDef",
    "DescribeRoleAliasRequestRequestTypeDef",
    "DescribeRoleAliasResponseTypeDef",
    "DescribeScheduledAuditRequestRequestTypeDef",
    "DescribeScheduledAuditResponseTypeDef",
    "DescribeSecurityProfileRequestRequestTypeDef",
    "DescribeSecurityProfileResponseTypeDef",
    "DescribeStreamRequestRequestTypeDef",
    "DescribeStreamResponseTypeDef",
    "DescribeThingGroupRequestRequestTypeDef",
    "DescribeThingGroupResponseTypeDef",
    "DescribeThingRegistrationTaskRequestRequestTypeDef",
    "DescribeThingRegistrationTaskResponseTypeDef",
    "DescribeThingRequestRequestTypeDef",
    "DescribeThingResponseTypeDef",
    "DescribeThingTypeRequestRequestTypeDef",
    "DescribeThingTypeResponseTypeDef",
    "DestinationTypeDef",
    "DetachPolicyRequestRequestTypeDef",
    "DetachPrincipalPolicyRequestRequestTypeDef",
    "DetachSecurityProfileRequestRequestTypeDef",
    "DetachThingPrincipalRequestRequestTypeDef",
    "DetectMitigationActionExecutionTypeDef",
    "DetectMitigationActionsTaskStatisticsTypeDef",
    "DetectMitigationActionsTaskSummaryTypeDef",
    "DetectMitigationActionsTaskTargetTypeDef",
    "DisableTopicRuleRequestRequestTypeDef",
    "DomainConfigurationSummaryTypeDef",
    "DynamoDBActionTypeDef",
    "DynamoDBv2ActionTypeDef",
    "EffectivePolicyTypeDef",
    "ElasticsearchActionTypeDef",
    "EnableIoTLoggingParamsTypeDef",
    "EnableTopicRuleRequestRequestTypeDef",
    "ErrorInfoTypeDef",
    "ExplicitDenyTypeDef",
    "ExponentialRolloutRateTypeDef",
    "FieldTypeDef",
    "FileLocationTypeDef",
    "FirehoseActionTypeDef",
    "GetBehaviorModelTrainingSummariesRequestRequestTypeDef",
    "GetBehaviorModelTrainingSummariesResponseTypeDef",
    "GetCardinalityRequestRequestTypeDef",
    "GetCardinalityResponseTypeDef",
    "GetEffectivePoliciesRequestRequestTypeDef",
    "GetEffectivePoliciesResponseTypeDef",
    "GetIndexingConfigurationResponseTypeDef",
    "GetJobDocumentRequestRequestTypeDef",
    "GetJobDocumentResponseTypeDef",
    "GetLoggingOptionsResponseTypeDef",
    "GetOTAUpdateRequestRequestTypeDef",
    "GetOTAUpdateResponseTypeDef",
    "GetPercentilesRequestRequestTypeDef",
    "GetPercentilesResponseTypeDef",
    "GetPolicyRequestRequestTypeDef",
    "GetPolicyResponseTypeDef",
    "GetPolicyVersionRequestRequestTypeDef",
    "GetPolicyVersionResponseTypeDef",
    "GetRegistrationCodeResponseTypeDef",
    "GetStatisticsRequestRequestTypeDef",
    "GetStatisticsResponseTypeDef",
    "GetTopicRuleDestinationRequestRequestTypeDef",
    "GetTopicRuleDestinationResponseTypeDef",
    "GetTopicRuleRequestRequestTypeDef",
    "GetTopicRuleResponseTypeDef",
    "GetV2LoggingOptionsResponseTypeDef",
    "GroupNameAndArnTypeDef",
    "HttpActionHeaderTypeDef",
    "HttpActionTypeDef",
    "HttpAuthorizationTypeDef",
    "HttpContextTypeDef",
    "HttpUrlDestinationConfigurationTypeDef",
    "HttpUrlDestinationPropertiesTypeDef",
    "HttpUrlDestinationSummaryTypeDef",
    "ImplicitDenyTypeDef",
    "IotAnalyticsActionTypeDef",
    "IotEventsActionTypeDef",
    "IotSiteWiseActionTypeDef",
    "JobExecutionStatusDetailsTypeDef",
    "JobExecutionSummaryForJobTypeDef",
    "JobExecutionSummaryForThingTypeDef",
    "JobExecutionSummaryTypeDef",
    "JobExecutionTypeDef",
    "JobExecutionsRolloutConfigTypeDef",
    "JobProcessDetailsTypeDef",
    "JobSummaryTypeDef",
    "JobTemplateSummaryTypeDef",
    "JobTypeDef",
    "KafkaActionTypeDef",
    "KeyPairTypeDef",
    "KinesisActionTypeDef",
    "LambdaActionTypeDef",
    "ListActiveViolationsRequestRequestTypeDef",
    "ListActiveViolationsResponseTypeDef",
    "ListAttachedPoliciesRequestRequestTypeDef",
    "ListAttachedPoliciesResponseTypeDef",
    "ListAuditFindingsRequestRequestTypeDef",
    "ListAuditFindingsResponseTypeDef",
    "ListAuditMitigationActionsExecutionsRequestRequestTypeDef",
    "ListAuditMitigationActionsExecutionsResponseTypeDef",
    "ListAuditMitigationActionsTasksRequestRequestTypeDef",
    "ListAuditMitigationActionsTasksResponseTypeDef",
    "ListAuditSuppressionsRequestRequestTypeDef",
    "ListAuditSuppressionsResponseTypeDef",
    "ListAuditTasksRequestRequestTypeDef",
    "ListAuditTasksResponseTypeDef",
    "ListAuthorizersRequestRequestTypeDef",
    "ListAuthorizersResponseTypeDef",
    "ListBillingGroupsRequestRequestTypeDef",
    "ListBillingGroupsResponseTypeDef",
    "ListCACertificatesRequestRequestTypeDef",
    "ListCACertificatesResponseTypeDef",
    "ListCertificatesByCARequestRequestTypeDef",
    "ListCertificatesByCAResponseTypeDef",
    "ListCertificatesRequestRequestTypeDef",
    "ListCertificatesResponseTypeDef",
    "ListCustomMetricsRequestRequestTypeDef",
    "ListCustomMetricsResponseTypeDef",
    "ListDetectMitigationActionsExecutionsRequestRequestTypeDef",
    "ListDetectMitigationActionsExecutionsResponseTypeDef",
    "ListDetectMitigationActionsTasksRequestRequestTypeDef",
    "ListDetectMitigationActionsTasksResponseTypeDef",
    "ListDimensionsRequestRequestTypeDef",
    "ListDimensionsResponseTypeDef",
    "ListDomainConfigurationsRequestRequestTypeDef",
    "ListDomainConfigurationsResponseTypeDef",
    "ListIndicesRequestRequestTypeDef",
    "ListIndicesResponseTypeDef",
    "ListJobExecutionsForJobRequestRequestTypeDef",
    "ListJobExecutionsForJobResponseTypeDef",
    "ListJobExecutionsForThingRequestRequestTypeDef",
    "ListJobExecutionsForThingResponseTypeDef",
    "ListJobTemplatesRequestRequestTypeDef",
    "ListJobTemplatesResponseTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListJobsResponseTypeDef",
    "ListMitigationActionsRequestRequestTypeDef",
    "ListMitigationActionsResponseTypeDef",
    "ListOTAUpdatesRequestRequestTypeDef",
    "ListOTAUpdatesResponseTypeDef",
    "ListOutgoingCertificatesRequestRequestTypeDef",
    "ListOutgoingCertificatesResponseTypeDef",
    "ListPoliciesRequestRequestTypeDef",
    "ListPoliciesResponseTypeDef",
    "ListPolicyPrincipalsRequestRequestTypeDef",
    "ListPolicyPrincipalsResponseTypeDef",
    "ListPolicyVersionsRequestRequestTypeDef",
    "ListPolicyVersionsResponseTypeDef",
    "ListPrincipalPoliciesRequestRequestTypeDef",
    "ListPrincipalPoliciesResponseTypeDef",
    "ListPrincipalThingsRequestRequestTypeDef",
    "ListPrincipalThingsResponseTypeDef",
    "ListProvisioningTemplateVersionsRequestRequestTypeDef",
    "ListProvisioningTemplateVersionsResponseTypeDef",
    "ListProvisioningTemplatesRequestRequestTypeDef",
    "ListProvisioningTemplatesResponseTypeDef",
    "ListRoleAliasesRequestRequestTypeDef",
    "ListRoleAliasesResponseTypeDef",
    "ListScheduledAuditsRequestRequestTypeDef",
    "ListScheduledAuditsResponseTypeDef",
    "ListSecurityProfilesForTargetRequestRequestTypeDef",
    "ListSecurityProfilesForTargetResponseTypeDef",
    "ListSecurityProfilesRequestRequestTypeDef",
    "ListSecurityProfilesResponseTypeDef",
    "ListStreamsRequestRequestTypeDef",
    "ListStreamsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTargetsForPolicyRequestRequestTypeDef",
    "ListTargetsForPolicyResponseTypeDef",
    "ListTargetsForSecurityProfileRequestRequestTypeDef",
    "ListTargetsForSecurityProfileResponseTypeDef",
    "ListThingGroupsForThingRequestRequestTypeDef",
    "ListThingGroupsForThingResponseTypeDef",
    "ListThingGroupsRequestRequestTypeDef",
    "ListThingGroupsResponseTypeDef",
    "ListThingPrincipalsRequestRequestTypeDef",
    "ListThingPrincipalsResponseTypeDef",
    "ListThingRegistrationTaskReportsRequestRequestTypeDef",
    "ListThingRegistrationTaskReportsResponseTypeDef",
    "ListThingRegistrationTasksRequestRequestTypeDef",
    "ListThingRegistrationTasksResponseTypeDef",
    "ListThingTypesRequestRequestTypeDef",
    "ListThingTypesResponseTypeDef",
    "ListThingsInBillingGroupRequestRequestTypeDef",
    "ListThingsInBillingGroupResponseTypeDef",
    "ListThingsInThingGroupRequestRequestTypeDef",
    "ListThingsInThingGroupResponseTypeDef",
    "ListThingsRequestRequestTypeDef",
    "ListThingsResponseTypeDef",
    "ListTopicRuleDestinationsRequestRequestTypeDef",
    "ListTopicRuleDestinationsResponseTypeDef",
    "ListTopicRulesRequestRequestTypeDef",
    "ListTopicRulesResponseTypeDef",
    "ListV2LoggingLevelsRequestRequestTypeDef",
    "ListV2LoggingLevelsResponseTypeDef",
    "ListViolationEventsRequestRequestTypeDef",
    "ListViolationEventsResponseTypeDef",
    "LogTargetConfigurationTypeDef",
    "LogTargetTypeDef",
    "LoggingOptionsPayloadTypeDef",
    "MachineLearningDetectionConfigTypeDef",
    "MetricDimensionTypeDef",
    "MetricToRetainTypeDef",
    "MetricValueTypeDef",
    "MitigationActionIdentifierTypeDef",
    "MitigationActionParamsTypeDef",
    "MitigationActionTypeDef",
    "MqttContextTypeDef",
    "NonCompliantResourceTypeDef",
    "OTAUpdateFileTypeDef",
    "OTAUpdateInfoTypeDef",
    "OTAUpdateSummaryTypeDef",
    "OutgoingCertificateTypeDef",
    "PaginatorConfigTypeDef",
    "PercentPairTypeDef",
    "PolicyTypeDef",
    "PolicyVersionIdentifierTypeDef",
    "PolicyVersionTypeDef",
    "PresignedUrlConfigTypeDef",
    "ProvisioningHookTypeDef",
    "ProvisioningTemplateSummaryTypeDef",
    "ProvisioningTemplateVersionSummaryTypeDef",
    "PublishFindingToSnsParamsTypeDef",
    "PutAssetPropertyValueEntryTypeDef",
    "PutItemInputTypeDef",
    "RateIncreaseCriteriaTypeDef",
    "RegisterCACertificateRequestRequestTypeDef",
    "RegisterCACertificateResponseTypeDef",
    "RegisterCertificateRequestRequestTypeDef",
    "RegisterCertificateResponseTypeDef",
    "RegisterCertificateWithoutCARequestRequestTypeDef",
    "RegisterCertificateWithoutCAResponseTypeDef",
    "RegisterThingRequestRequestTypeDef",
    "RegisterThingResponseTypeDef",
    "RegistrationConfigTypeDef",
    "RejectCertificateTransferRequestRequestTypeDef",
    "RelatedResourceTypeDef",
    "RemoveThingFromBillingGroupRequestRequestTypeDef",
    "RemoveThingFromThingGroupRequestRequestTypeDef",
    "ReplaceDefaultPolicyVersionParamsTypeDef",
    "ReplaceTopicRuleRequestRequestTypeDef",
    "RepublishActionTypeDef",
    "ResourceIdentifierTypeDef",
    "ResponseMetadataTypeDef",
    "RoleAliasDescriptionTypeDef",
    "S3ActionTypeDef",
    "S3DestinationTypeDef",
    "S3LocationTypeDef",
    "SalesforceActionTypeDef",
    "ScheduledAuditMetadataTypeDef",
    "SearchIndexRequestRequestTypeDef",
    "SearchIndexResponseTypeDef",
    "SecurityProfileIdentifierTypeDef",
    "SecurityProfileTargetMappingTypeDef",
    "SecurityProfileTargetTypeDef",
    "ServerCertificateSummaryTypeDef",
    "SetDefaultAuthorizerRequestRequestTypeDef",
    "SetDefaultAuthorizerResponseTypeDef",
    "SetDefaultPolicyVersionRequestRequestTypeDef",
    "SetLoggingOptionsRequestRequestTypeDef",
    "SetV2LoggingLevelRequestRequestTypeDef",
    "SetV2LoggingOptionsRequestRequestTypeDef",
    "SigV4AuthorizationTypeDef",
    "SigningProfileParameterTypeDef",
    "SnsActionTypeDef",
    "SqsActionTypeDef",
    "StartAuditMitigationActionsTaskRequestRequestTypeDef",
    "StartAuditMitigationActionsTaskResponseTypeDef",
    "StartDetectMitigationActionsTaskRequestRequestTypeDef",
    "StartDetectMitigationActionsTaskResponseTypeDef",
    "StartOnDemandAuditTaskRequestRequestTypeDef",
    "StartOnDemandAuditTaskResponseTypeDef",
    "StartSigningJobParameterTypeDef",
    "StartThingRegistrationTaskRequestRequestTypeDef",
    "StartThingRegistrationTaskResponseTypeDef",
    "StatisticalThresholdTypeDef",
    "StatisticsTypeDef",
    "StepFunctionsActionTypeDef",
    "StopThingRegistrationTaskRequestRequestTypeDef",
    "StreamFileTypeDef",
    "StreamInfoTypeDef",
    "StreamSummaryTypeDef",
    "StreamTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TaskStatisticsForAuditCheckTypeDef",
    "TaskStatisticsTypeDef",
    "TestAuthorizationRequestRequestTypeDef",
    "TestAuthorizationResponseTypeDef",
    "TestInvokeAuthorizerRequestRequestTypeDef",
    "TestInvokeAuthorizerResponseTypeDef",
    "ThingAttributeTypeDef",
    "ThingConnectivityTypeDef",
    "ThingDocumentTypeDef",
    "ThingGroupDocumentTypeDef",
    "ThingGroupIndexingConfigurationTypeDef",
    "ThingGroupMetadataTypeDef",
    "ThingGroupPropertiesTypeDef",
    "ThingIndexingConfigurationTypeDef",
    "ThingTypeDefinitionTypeDef",
    "ThingTypeMetadataTypeDef",
    "ThingTypePropertiesTypeDef",
    "TimeoutConfigTypeDef",
    "TimestreamActionTypeDef",
    "TimestreamDimensionTypeDef",
    "TimestreamTimestampTypeDef",
    "TlsContextTypeDef",
    "TopicRuleDestinationConfigurationTypeDef",
    "TopicRuleDestinationSummaryTypeDef",
    "TopicRuleDestinationTypeDef",
    "TopicRuleListItemTypeDef",
    "TopicRulePayloadTypeDef",
    "TopicRuleTypeDef",
    "TransferCertificateRequestRequestTypeDef",
    "TransferCertificateResponseTypeDef",
    "TransferDataTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccountAuditConfigurationRequestRequestTypeDef",
    "UpdateAuditSuppressionRequestRequestTypeDef",
    "UpdateAuthorizerRequestRequestTypeDef",
    "UpdateAuthorizerResponseTypeDef",
    "UpdateBillingGroupRequestRequestTypeDef",
    "UpdateBillingGroupResponseTypeDef",
    "UpdateCACertificateParamsTypeDef",
    "UpdateCACertificateRequestRequestTypeDef",
    "UpdateCertificateRequestRequestTypeDef",
    "UpdateCustomMetricRequestRequestTypeDef",
    "UpdateCustomMetricResponseTypeDef",
    "UpdateDeviceCertificateParamsTypeDef",
    "UpdateDimensionRequestRequestTypeDef",
    "UpdateDimensionResponseTypeDef",
    "UpdateDomainConfigurationRequestRequestTypeDef",
    "UpdateDomainConfigurationResponseTypeDef",
    "UpdateDynamicThingGroupRequestRequestTypeDef",
    "UpdateDynamicThingGroupResponseTypeDef",
    "UpdateEventConfigurationsRequestRequestTypeDef",
    "UpdateIndexingConfigurationRequestRequestTypeDef",
    "UpdateJobRequestRequestTypeDef",
    "UpdateMitigationActionRequestRequestTypeDef",
    "UpdateMitigationActionResponseTypeDef",
    "UpdateProvisioningTemplateRequestRequestTypeDef",
    "UpdateRoleAliasRequestRequestTypeDef",
    "UpdateRoleAliasResponseTypeDef",
    "UpdateScheduledAuditRequestRequestTypeDef",
    "UpdateScheduledAuditResponseTypeDef",
    "UpdateSecurityProfileRequestRequestTypeDef",
    "UpdateSecurityProfileResponseTypeDef",
    "UpdateStreamRequestRequestTypeDef",
    "UpdateStreamResponseTypeDef",
    "UpdateThingGroupRequestRequestTypeDef",
    "UpdateThingGroupResponseTypeDef",
    "UpdateThingGroupsForThingRequestRequestTypeDef",
    "UpdateThingRequestRequestTypeDef",
    "UpdateTopicRuleDestinationRequestRequestTypeDef",
    "ValidateSecurityProfileBehaviorsRequestRequestTypeDef",
    "ValidateSecurityProfileBehaviorsResponseTypeDef",
    "ValidationErrorTypeDef",
    "ViolationEventAdditionalInfoTypeDef",
    "ViolationEventOccurrenceRangeTypeDef",
    "ViolationEventTypeDef",
    "VpcDestinationConfigurationTypeDef",
    "VpcDestinationPropertiesTypeDef",
    "VpcDestinationSummaryTypeDef",
)

AbortConfigTypeDef = TypedDict(
    "AbortConfigTypeDef",
    {
        "criteriaList": List["AbortCriteriaTypeDef"],
    },
)

AbortCriteriaTypeDef = TypedDict(
    "AbortCriteriaTypeDef",
    {
        "failureType": JobExecutionFailureTypeType,
        "action": Literal["CANCEL"],
        "thresholdPercentage": float,
        "minNumberOfExecutedThings": int,
    },
)

_RequiredAcceptCertificateTransferRequestRequestTypeDef = TypedDict(
    "_RequiredAcceptCertificateTransferRequestRequestTypeDef",
    {
        "certificateId": str,
    },
)
_OptionalAcceptCertificateTransferRequestRequestTypeDef = TypedDict(
    "_OptionalAcceptCertificateTransferRequestRequestTypeDef",
    {
        "setAsActive": bool,
    },
    total=False,
)

class AcceptCertificateTransferRequestRequestTypeDef(
    _RequiredAcceptCertificateTransferRequestRequestTypeDef,
    _OptionalAcceptCertificateTransferRequestRequestTypeDef,
):
    pass

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "dynamoDB": "DynamoDBActionTypeDef",
        "dynamoDBv2": "DynamoDBv2ActionTypeDef",
        "lambda": "LambdaActionTypeDef",
        "sns": "SnsActionTypeDef",
        "sqs": "SqsActionTypeDef",
        "kinesis": "KinesisActionTypeDef",
        "republish": "RepublishActionTypeDef",
        "s3": "S3ActionTypeDef",
        "firehose": "FirehoseActionTypeDef",
        "cloudwatchMetric": "CloudwatchMetricActionTypeDef",
        "cloudwatchAlarm": "CloudwatchAlarmActionTypeDef",
        "cloudwatchLogs": "CloudwatchLogsActionTypeDef",
        "elasticsearch": "ElasticsearchActionTypeDef",
        "salesforce": "SalesforceActionTypeDef",
        "iotAnalytics": "IotAnalyticsActionTypeDef",
        "iotEvents": "IotEventsActionTypeDef",
        "iotSiteWise": "IotSiteWiseActionTypeDef",
        "stepFunctions": "StepFunctionsActionTypeDef",
        "timestream": "TimestreamActionTypeDef",
        "http": "HttpActionTypeDef",
        "kafka": "KafkaActionTypeDef",
    },
    total=False,
)

ActiveViolationTypeDef = TypedDict(
    "ActiveViolationTypeDef",
    {
        "violationId": str,
        "thingName": str,
        "securityProfileName": str,
        "behavior": "BehaviorTypeDef",
        "lastViolationValue": "MetricValueTypeDef",
        "violationEventAdditionalInfo": "ViolationEventAdditionalInfoTypeDef",
        "lastViolationTime": datetime,
        "violationStartTime": datetime,
    },
    total=False,
)

AddThingToBillingGroupRequestRequestTypeDef = TypedDict(
    "AddThingToBillingGroupRequestRequestTypeDef",
    {
        "billingGroupName": str,
        "billingGroupArn": str,
        "thingName": str,
        "thingArn": str,
    },
    total=False,
)

AddThingToThingGroupRequestRequestTypeDef = TypedDict(
    "AddThingToThingGroupRequestRequestTypeDef",
    {
        "thingGroupName": str,
        "thingGroupArn": str,
        "thingName": str,
        "thingArn": str,
        "overrideDynamicGroups": bool,
    },
    total=False,
)

_RequiredAddThingsToThingGroupParamsTypeDef = TypedDict(
    "_RequiredAddThingsToThingGroupParamsTypeDef",
    {
        "thingGroupNames": List[str],
    },
)
_OptionalAddThingsToThingGroupParamsTypeDef = TypedDict(
    "_OptionalAddThingsToThingGroupParamsTypeDef",
    {
        "overrideDynamicGroups": bool,
    },
    total=False,
)

class AddThingsToThingGroupParamsTypeDef(
    _RequiredAddThingsToThingGroupParamsTypeDef, _OptionalAddThingsToThingGroupParamsTypeDef
):
    pass

AlertTargetTypeDef = TypedDict(
    "AlertTargetTypeDef",
    {
        "alertTargetArn": str,
        "roleArn": str,
    },
)

AllowedTypeDef = TypedDict(
    "AllowedTypeDef",
    {
        "policies": List["PolicyTypeDef"],
    },
    total=False,
)

_RequiredAssetPropertyTimestampTypeDef = TypedDict(
    "_RequiredAssetPropertyTimestampTypeDef",
    {
        "timeInSeconds": str,
    },
)
_OptionalAssetPropertyTimestampTypeDef = TypedDict(
    "_OptionalAssetPropertyTimestampTypeDef",
    {
        "offsetInNanos": str,
    },
    total=False,
)

class AssetPropertyTimestampTypeDef(
    _RequiredAssetPropertyTimestampTypeDef, _OptionalAssetPropertyTimestampTypeDef
):
    pass

_RequiredAssetPropertyValueTypeDef = TypedDict(
    "_RequiredAssetPropertyValueTypeDef",
    {
        "value": "AssetPropertyVariantTypeDef",
        "timestamp": "AssetPropertyTimestampTypeDef",
    },
)
_OptionalAssetPropertyValueTypeDef = TypedDict(
    "_OptionalAssetPropertyValueTypeDef",
    {
        "quality": str,
    },
    total=False,
)

class AssetPropertyValueTypeDef(
    _RequiredAssetPropertyValueTypeDef, _OptionalAssetPropertyValueTypeDef
):
    pass

AssetPropertyVariantTypeDef = TypedDict(
    "AssetPropertyVariantTypeDef",
    {
        "stringValue": str,
        "integerValue": str,
        "doubleValue": str,
        "booleanValue": str,
    },
    total=False,
)

_RequiredAssociateTargetsWithJobRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateTargetsWithJobRequestRequestTypeDef",
    {
        "targets": List[str],
        "jobId": str,
    },
)
_OptionalAssociateTargetsWithJobRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateTargetsWithJobRequestRequestTypeDef",
    {
        "comment": str,
        "namespaceId": str,
    },
    total=False,
)

class AssociateTargetsWithJobRequestRequestTypeDef(
    _RequiredAssociateTargetsWithJobRequestRequestTypeDef,
    _OptionalAssociateTargetsWithJobRequestRequestTypeDef,
):
    pass

AssociateTargetsWithJobResponseTypeDef = TypedDict(
    "AssociateTargetsWithJobResponseTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachPolicyRequestRequestTypeDef = TypedDict(
    "AttachPolicyRequestRequestTypeDef",
    {
        "policyName": str,
        "target": str,
    },
)

AttachPrincipalPolicyRequestRequestTypeDef = TypedDict(
    "AttachPrincipalPolicyRequestRequestTypeDef",
    {
        "policyName": str,
        "principal": str,
    },
)

AttachSecurityProfileRequestRequestTypeDef = TypedDict(
    "AttachSecurityProfileRequestRequestTypeDef",
    {
        "securityProfileName": str,
        "securityProfileTargetArn": str,
    },
)

AttachThingPrincipalRequestRequestTypeDef = TypedDict(
    "AttachThingPrincipalRequestRequestTypeDef",
    {
        "thingName": str,
        "principal": str,
    },
)

AttributePayloadTypeDef = TypedDict(
    "AttributePayloadTypeDef",
    {
        "attributes": Dict[str, str],
        "merge": bool,
    },
    total=False,
)

AuditCheckConfigurationTypeDef = TypedDict(
    "AuditCheckConfigurationTypeDef",
    {
        "enabled": bool,
    },
    total=False,
)

AuditCheckDetailsTypeDef = TypedDict(
    "AuditCheckDetailsTypeDef",
    {
        "checkRunStatus": AuditCheckRunStatusType,
        "checkCompliant": bool,
        "totalResourcesCount": int,
        "nonCompliantResourcesCount": int,
        "suppressedNonCompliantResourcesCount": int,
        "errorCode": str,
        "message": str,
    },
    total=False,
)

AuditFindingTypeDef = TypedDict(
    "AuditFindingTypeDef",
    {
        "findingId": str,
        "taskId": str,
        "checkName": str,
        "taskStartTime": datetime,
        "findingTime": datetime,
        "severity": AuditFindingSeverityType,
        "nonCompliantResource": "NonCompliantResourceTypeDef",
        "relatedResources": List["RelatedResourceTypeDef"],
        "reasonForNonCompliance": str,
        "reasonForNonComplianceCode": str,
        "isSuppressed": bool,
    },
    total=False,
)

AuditMitigationActionExecutionMetadataTypeDef = TypedDict(
    "AuditMitigationActionExecutionMetadataTypeDef",
    {
        "taskId": str,
        "findingId": str,
        "actionName": str,
        "actionId": str,
        "status": AuditMitigationActionsExecutionStatusType,
        "startTime": datetime,
        "endTime": datetime,
        "errorCode": str,
        "message": str,
    },
    total=False,
)

AuditMitigationActionsTaskMetadataTypeDef = TypedDict(
    "AuditMitigationActionsTaskMetadataTypeDef",
    {
        "taskId": str,
        "startTime": datetime,
        "taskStatus": AuditMitigationActionsTaskStatusType,
    },
    total=False,
)

AuditMitigationActionsTaskTargetTypeDef = TypedDict(
    "AuditMitigationActionsTaskTargetTypeDef",
    {
        "auditTaskId": str,
        "findingIds": List[str],
        "auditCheckToReasonCodeFilter": Dict[str, List[str]],
    },
    total=False,
)

AuditNotificationTargetTypeDef = TypedDict(
    "AuditNotificationTargetTypeDef",
    {
        "targetArn": str,
        "roleArn": str,
        "enabled": bool,
    },
    total=False,
)

_RequiredAuditSuppressionTypeDef = TypedDict(
    "_RequiredAuditSuppressionTypeDef",
    {
        "checkName": str,
        "resourceIdentifier": "ResourceIdentifierTypeDef",
    },
)
_OptionalAuditSuppressionTypeDef = TypedDict(
    "_OptionalAuditSuppressionTypeDef",
    {
        "expirationDate": datetime,
        "suppressIndefinitely": bool,
        "description": str,
    },
    total=False,
)

class AuditSuppressionTypeDef(_RequiredAuditSuppressionTypeDef, _OptionalAuditSuppressionTypeDef):
    pass

AuditTaskMetadataTypeDef = TypedDict(
    "AuditTaskMetadataTypeDef",
    {
        "taskId": str,
        "taskStatus": AuditTaskStatusType,
        "taskType": AuditTaskTypeType,
    },
    total=False,
)

_RequiredAuthInfoTypeDef = TypedDict(
    "_RequiredAuthInfoTypeDef",
    {
        "resources": List[str],
    },
)
_OptionalAuthInfoTypeDef = TypedDict(
    "_OptionalAuthInfoTypeDef",
    {
        "actionType": ActionTypeType,
    },
    total=False,
)

class AuthInfoTypeDef(_RequiredAuthInfoTypeDef, _OptionalAuthInfoTypeDef):
    pass

AuthResultTypeDef = TypedDict(
    "AuthResultTypeDef",
    {
        "authInfo": "AuthInfoTypeDef",
        "allowed": "AllowedTypeDef",
        "denied": "DeniedTypeDef",
        "authDecision": AuthDecisionType,
        "missingContextValues": List[str],
    },
    total=False,
)

AuthorizerConfigTypeDef = TypedDict(
    "AuthorizerConfigTypeDef",
    {
        "defaultAuthorizerName": str,
        "allowAuthorizerOverride": bool,
    },
    total=False,
)

AuthorizerDescriptionTypeDef = TypedDict(
    "AuthorizerDescriptionTypeDef",
    {
        "authorizerName": str,
        "authorizerArn": str,
        "authorizerFunctionArn": str,
        "tokenKeyName": str,
        "tokenSigningPublicKeys": Dict[str, str],
        "status": AuthorizerStatusType,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "signingDisabled": bool,
    },
    total=False,
)

AuthorizerSummaryTypeDef = TypedDict(
    "AuthorizerSummaryTypeDef",
    {
        "authorizerName": str,
        "authorizerArn": str,
    },
    total=False,
)

AwsJobAbortConfigTypeDef = TypedDict(
    "AwsJobAbortConfigTypeDef",
    {
        "abortCriteriaList": List["AwsJobAbortCriteriaTypeDef"],
    },
)

AwsJobAbortCriteriaTypeDef = TypedDict(
    "AwsJobAbortCriteriaTypeDef",
    {
        "failureType": AwsJobAbortCriteriaFailureTypeType,
        "action": Literal["CANCEL"],
        "thresholdPercentage": float,
        "minNumberOfExecutedThings": int,
    },
)

AwsJobExecutionsRolloutConfigTypeDef = TypedDict(
    "AwsJobExecutionsRolloutConfigTypeDef",
    {
        "maximumPerMinute": int,
        "exponentialRate": "AwsJobExponentialRolloutRateTypeDef",
    },
    total=False,
)

AwsJobExponentialRolloutRateTypeDef = TypedDict(
    "AwsJobExponentialRolloutRateTypeDef",
    {
        "baseRatePerMinute": int,
        "incrementFactor": float,
        "rateIncreaseCriteria": "AwsJobRateIncreaseCriteriaTypeDef",
    },
)

AwsJobPresignedUrlConfigTypeDef = TypedDict(
    "AwsJobPresignedUrlConfigTypeDef",
    {
        "expiresInSec": int,
    },
    total=False,
)

AwsJobRateIncreaseCriteriaTypeDef = TypedDict(
    "AwsJobRateIncreaseCriteriaTypeDef",
    {
        "numberOfNotifiedThings": int,
        "numberOfSucceededThings": int,
    },
    total=False,
)

AwsJobTimeoutConfigTypeDef = TypedDict(
    "AwsJobTimeoutConfigTypeDef",
    {
        "inProgressTimeoutInMinutes": int,
    },
    total=False,
)

BehaviorCriteriaTypeDef = TypedDict(
    "BehaviorCriteriaTypeDef",
    {
        "comparisonOperator": ComparisonOperatorType,
        "value": "MetricValueTypeDef",
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": "StatisticalThresholdTypeDef",
        "mlDetectionConfig": "MachineLearningDetectionConfigTypeDef",
    },
    total=False,
)

BehaviorModelTrainingSummaryTypeDef = TypedDict(
    "BehaviorModelTrainingSummaryTypeDef",
    {
        "securityProfileName": str,
        "behaviorName": str,
        "trainingDataCollectionStartDate": datetime,
        "modelStatus": ModelStatusType,
        "datapointsCollectionPercentage": float,
        "lastModelRefreshDate": datetime,
    },
    total=False,
)

_RequiredBehaviorTypeDef = TypedDict(
    "_RequiredBehaviorTypeDef",
    {
        "name": str,
    },
)
_OptionalBehaviorTypeDef = TypedDict(
    "_OptionalBehaviorTypeDef",
    {
        "metric": str,
        "metricDimension": "MetricDimensionTypeDef",
        "criteria": "BehaviorCriteriaTypeDef",
        "suppressAlerts": bool,
    },
    total=False,
)

class BehaviorTypeDef(_RequiredBehaviorTypeDef, _OptionalBehaviorTypeDef):
    pass

BillingGroupMetadataTypeDef = TypedDict(
    "BillingGroupMetadataTypeDef",
    {
        "creationDate": datetime,
    },
    total=False,
)

BillingGroupPropertiesTypeDef = TypedDict(
    "BillingGroupPropertiesTypeDef",
    {
        "billingGroupDescription": str,
    },
    total=False,
)

CACertificateDescriptionTypeDef = TypedDict(
    "CACertificateDescriptionTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": CACertificateStatusType,
        "certificatePem": str,
        "ownedBy": str,
        "creationDate": datetime,
        "autoRegistrationStatus": AutoRegistrationStatusType,
        "lastModifiedDate": datetime,
        "customerVersion": int,
        "generationId": str,
        "validity": "CertificateValidityTypeDef",
    },
    total=False,
)

CACertificateTypeDef = TypedDict(
    "CACertificateTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": CACertificateStatusType,
        "creationDate": datetime,
    },
    total=False,
)

CancelAuditMitigationActionsTaskRequestRequestTypeDef = TypedDict(
    "CancelAuditMitigationActionsTaskRequestRequestTypeDef",
    {
        "taskId": str,
    },
)

CancelAuditTaskRequestRequestTypeDef = TypedDict(
    "CancelAuditTaskRequestRequestTypeDef",
    {
        "taskId": str,
    },
)

CancelCertificateTransferRequestRequestTypeDef = TypedDict(
    "CancelCertificateTransferRequestRequestTypeDef",
    {
        "certificateId": str,
    },
)

CancelDetectMitigationActionsTaskRequestRequestTypeDef = TypedDict(
    "CancelDetectMitigationActionsTaskRequestRequestTypeDef",
    {
        "taskId": str,
    },
)

_RequiredCancelJobExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredCancelJobExecutionRequestRequestTypeDef",
    {
        "jobId": str,
        "thingName": str,
    },
)
_OptionalCancelJobExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalCancelJobExecutionRequestRequestTypeDef",
    {
        "force": bool,
        "expectedVersion": int,
        "statusDetails": Dict[str, str],
    },
    total=False,
)

class CancelJobExecutionRequestRequestTypeDef(
    _RequiredCancelJobExecutionRequestRequestTypeDef,
    _OptionalCancelJobExecutionRequestRequestTypeDef,
):
    pass

_RequiredCancelJobRequestRequestTypeDef = TypedDict(
    "_RequiredCancelJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)
_OptionalCancelJobRequestRequestTypeDef = TypedDict(
    "_OptionalCancelJobRequestRequestTypeDef",
    {
        "reasonCode": str,
        "comment": str,
        "force": bool,
    },
    total=False,
)

class CancelJobRequestRequestTypeDef(
    _RequiredCancelJobRequestRequestTypeDef, _OptionalCancelJobRequestRequestTypeDef
):
    pass

CancelJobResponseTypeDef = TypedDict(
    "CancelJobResponseTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CertificateDescriptionTypeDef = TypedDict(
    "CertificateDescriptionTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "caCertificateId": str,
        "status": CertificateStatusType,
        "certificatePem": str,
        "ownedBy": str,
        "previousOwnedBy": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "customerVersion": int,
        "transferData": "TransferDataTypeDef",
        "generationId": str,
        "validity": "CertificateValidityTypeDef",
        "certificateMode": CertificateModeType,
    },
    total=False,
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": CertificateStatusType,
        "certificateMode": CertificateModeType,
        "creationDate": datetime,
    },
    total=False,
)

CertificateValidityTypeDef = TypedDict(
    "CertificateValidityTypeDef",
    {
        "notBefore": datetime,
        "notAfter": datetime,
    },
    total=False,
)

CloudwatchAlarmActionTypeDef = TypedDict(
    "CloudwatchAlarmActionTypeDef",
    {
        "roleArn": str,
        "alarmName": str,
        "stateReason": str,
        "stateValue": str,
    },
)

CloudwatchLogsActionTypeDef = TypedDict(
    "CloudwatchLogsActionTypeDef",
    {
        "roleArn": str,
        "logGroupName": str,
    },
)

_RequiredCloudwatchMetricActionTypeDef = TypedDict(
    "_RequiredCloudwatchMetricActionTypeDef",
    {
        "roleArn": str,
        "metricNamespace": str,
        "metricName": str,
        "metricValue": str,
        "metricUnit": str,
    },
)
_OptionalCloudwatchMetricActionTypeDef = TypedDict(
    "_OptionalCloudwatchMetricActionTypeDef",
    {
        "metricTimestamp": str,
    },
    total=False,
)

class CloudwatchMetricActionTypeDef(
    _RequiredCloudwatchMetricActionTypeDef, _OptionalCloudwatchMetricActionTypeDef
):
    pass

CodeSigningCertificateChainTypeDef = TypedDict(
    "CodeSigningCertificateChainTypeDef",
    {
        "certificateName": str,
        "inlineDocument": str,
    },
    total=False,
)

CodeSigningSignatureTypeDef = TypedDict(
    "CodeSigningSignatureTypeDef",
    {
        "inlineDocument": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

CodeSigningTypeDef = TypedDict(
    "CodeSigningTypeDef",
    {
        "awsSignerJobId": str,
        "startSigningJobParameter": "StartSigningJobParameterTypeDef",
        "customCodeSigning": "CustomCodeSigningTypeDef",
    },
    total=False,
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

ConfirmTopicRuleDestinationRequestRequestTypeDef = TypedDict(
    "ConfirmTopicRuleDestinationRequestRequestTypeDef",
    {
        "confirmationToken": str,
    },
)

_RequiredCreateAuditSuppressionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAuditSuppressionRequestRequestTypeDef",
    {
        "checkName": str,
        "resourceIdentifier": "ResourceIdentifierTypeDef",
        "clientRequestToken": str,
    },
)
_OptionalCreateAuditSuppressionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAuditSuppressionRequestRequestTypeDef",
    {
        "expirationDate": Union[datetime, str],
        "suppressIndefinitely": bool,
        "description": str,
    },
    total=False,
)

class CreateAuditSuppressionRequestRequestTypeDef(
    _RequiredCreateAuditSuppressionRequestRequestTypeDef,
    _OptionalCreateAuditSuppressionRequestRequestTypeDef,
):
    pass

_RequiredCreateAuthorizerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAuthorizerRequestRequestTypeDef",
    {
        "authorizerName": str,
        "authorizerFunctionArn": str,
    },
)
_OptionalCreateAuthorizerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAuthorizerRequestRequestTypeDef",
    {
        "tokenKeyName": str,
        "tokenSigningPublicKeys": Dict[str, str],
        "status": AuthorizerStatusType,
        "tags": List["TagTypeDef"],
        "signingDisabled": bool,
    },
    total=False,
)

class CreateAuthorizerRequestRequestTypeDef(
    _RequiredCreateAuthorizerRequestRequestTypeDef, _OptionalCreateAuthorizerRequestRequestTypeDef
):
    pass

CreateAuthorizerResponseTypeDef = TypedDict(
    "CreateAuthorizerResponseTypeDef",
    {
        "authorizerName": str,
        "authorizerArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBillingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBillingGroupRequestRequestTypeDef",
    {
        "billingGroupName": str,
    },
)
_OptionalCreateBillingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBillingGroupRequestRequestTypeDef",
    {
        "billingGroupProperties": "BillingGroupPropertiesTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateBillingGroupRequestRequestTypeDef(
    _RequiredCreateBillingGroupRequestRequestTypeDef,
    _OptionalCreateBillingGroupRequestRequestTypeDef,
):
    pass

CreateBillingGroupResponseTypeDef = TypedDict(
    "CreateBillingGroupResponseTypeDef",
    {
        "billingGroupName": str,
        "billingGroupArn": str,
        "billingGroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCertificateFromCsrRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCertificateFromCsrRequestRequestTypeDef",
    {
        "certificateSigningRequest": str,
    },
)
_OptionalCreateCertificateFromCsrRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCertificateFromCsrRequestRequestTypeDef",
    {
        "setAsActive": bool,
    },
    total=False,
)

class CreateCertificateFromCsrRequestRequestTypeDef(
    _RequiredCreateCertificateFromCsrRequestRequestTypeDef,
    _OptionalCreateCertificateFromCsrRequestRequestTypeDef,
):
    pass

CreateCertificateFromCsrResponseTypeDef = TypedDict(
    "CreateCertificateFromCsrResponseTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "certificatePem": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCustomMetricRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCustomMetricRequestRequestTypeDef",
    {
        "metricName": str,
        "metricType": CustomMetricTypeType,
        "clientRequestToken": str,
    },
)
_OptionalCreateCustomMetricRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCustomMetricRequestRequestTypeDef",
    {
        "displayName": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateCustomMetricRequestRequestTypeDef(
    _RequiredCreateCustomMetricRequestRequestTypeDef,
    _OptionalCreateCustomMetricRequestRequestTypeDef,
):
    pass

CreateCustomMetricResponseTypeDef = TypedDict(
    "CreateCustomMetricResponseTypeDef",
    {
        "metricName": str,
        "metricArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDimensionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDimensionRequestRequestTypeDef",
    {
        "name": str,
        "type": Literal["TOPIC_FILTER"],
        "stringValues": List[str],
        "clientRequestToken": str,
    },
)
_OptionalCreateDimensionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDimensionRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDimensionRequestRequestTypeDef(
    _RequiredCreateDimensionRequestRequestTypeDef, _OptionalCreateDimensionRequestRequestTypeDef
):
    pass

CreateDimensionResponseTypeDef = TypedDict(
    "CreateDimensionResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDomainConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDomainConfigurationRequestRequestTypeDef",
    {
        "domainConfigurationName": str,
    },
)
_OptionalCreateDomainConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDomainConfigurationRequestRequestTypeDef",
    {
        "domainName": str,
        "serverCertificateArns": List[str],
        "validationCertificateArn": str,
        "authorizerConfig": "AuthorizerConfigTypeDef",
        "serviceType": ServiceTypeType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDomainConfigurationRequestRequestTypeDef(
    _RequiredCreateDomainConfigurationRequestRequestTypeDef,
    _OptionalCreateDomainConfigurationRequestRequestTypeDef,
):
    pass

CreateDomainConfigurationResponseTypeDef = TypedDict(
    "CreateDomainConfigurationResponseTypeDef",
    {
        "domainConfigurationName": str,
        "domainConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDynamicThingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDynamicThingGroupRequestRequestTypeDef",
    {
        "thingGroupName": str,
        "queryString": str,
    },
)
_OptionalCreateDynamicThingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDynamicThingGroupRequestRequestTypeDef",
    {
        "thingGroupProperties": "ThingGroupPropertiesTypeDef",
        "indexName": str,
        "queryVersion": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDynamicThingGroupRequestRequestTypeDef(
    _RequiredCreateDynamicThingGroupRequestRequestTypeDef,
    _OptionalCreateDynamicThingGroupRequestRequestTypeDef,
):
    pass

CreateDynamicThingGroupResponseTypeDef = TypedDict(
    "CreateDynamicThingGroupResponseTypeDef",
    {
        "thingGroupName": str,
        "thingGroupArn": str,
        "thingGroupId": str,
        "indexName": str,
        "queryString": str,
        "queryVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateJobRequestRequestTypeDef",
    {
        "jobId": str,
        "targets": List[str],
    },
)
_OptionalCreateJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateJobRequestRequestTypeDef",
    {
        "documentSource": str,
        "document": str,
        "description": str,
        "presignedUrlConfig": "PresignedUrlConfigTypeDef",
        "targetSelection": TargetSelectionType,
        "jobExecutionsRolloutConfig": "JobExecutionsRolloutConfigTypeDef",
        "abortConfig": "AbortConfigTypeDef",
        "timeoutConfig": "TimeoutConfigTypeDef",
        "tags": List["TagTypeDef"],
        "namespaceId": str,
        "jobTemplateArn": str,
    },
    total=False,
)

class CreateJobRequestRequestTypeDef(
    _RequiredCreateJobRequestRequestTypeDef, _OptionalCreateJobRequestRequestTypeDef
):
    pass

CreateJobResponseTypeDef = TypedDict(
    "CreateJobResponseTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateJobTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateJobTemplateRequestRequestTypeDef",
    {
        "jobTemplateId": str,
        "description": str,
    },
)
_OptionalCreateJobTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateJobTemplateRequestRequestTypeDef",
    {
        "jobArn": str,
        "documentSource": str,
        "document": str,
        "presignedUrlConfig": "PresignedUrlConfigTypeDef",
        "jobExecutionsRolloutConfig": "JobExecutionsRolloutConfigTypeDef",
        "abortConfig": "AbortConfigTypeDef",
        "timeoutConfig": "TimeoutConfigTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateJobTemplateRequestRequestTypeDef(
    _RequiredCreateJobTemplateRequestRequestTypeDef, _OptionalCreateJobTemplateRequestRequestTypeDef
):
    pass

CreateJobTemplateResponseTypeDef = TypedDict(
    "CreateJobTemplateResponseTypeDef",
    {
        "jobTemplateArn": str,
        "jobTemplateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateKeysAndCertificateRequestRequestTypeDef = TypedDict(
    "CreateKeysAndCertificateRequestRequestTypeDef",
    {
        "setAsActive": bool,
    },
    total=False,
)

CreateKeysAndCertificateResponseTypeDef = TypedDict(
    "CreateKeysAndCertificateResponseTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "certificatePem": str,
        "keyPair": "KeyPairTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMitigationActionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMitigationActionRequestRequestTypeDef",
    {
        "actionName": str,
        "roleArn": str,
        "actionParams": "MitigationActionParamsTypeDef",
    },
)
_OptionalCreateMitigationActionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMitigationActionRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateMitigationActionRequestRequestTypeDef(
    _RequiredCreateMitigationActionRequestRequestTypeDef,
    _OptionalCreateMitigationActionRequestRequestTypeDef,
):
    pass

CreateMitigationActionResponseTypeDef = TypedDict(
    "CreateMitigationActionResponseTypeDef",
    {
        "actionArn": str,
        "actionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateOTAUpdateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateOTAUpdateRequestRequestTypeDef",
    {
        "otaUpdateId": str,
        "targets": List[str],
        "files": List["OTAUpdateFileTypeDef"],
        "roleArn": str,
    },
)
_OptionalCreateOTAUpdateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateOTAUpdateRequestRequestTypeDef",
    {
        "description": str,
        "protocols": List[ProtocolType],
        "targetSelection": TargetSelectionType,
        "awsJobExecutionsRolloutConfig": "AwsJobExecutionsRolloutConfigTypeDef",
        "awsJobPresignedUrlConfig": "AwsJobPresignedUrlConfigTypeDef",
        "awsJobAbortConfig": "AwsJobAbortConfigTypeDef",
        "awsJobTimeoutConfig": "AwsJobTimeoutConfigTypeDef",
        "additionalParameters": Dict[str, str],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateOTAUpdateRequestRequestTypeDef(
    _RequiredCreateOTAUpdateRequestRequestTypeDef, _OptionalCreateOTAUpdateRequestRequestTypeDef
):
    pass

CreateOTAUpdateResponseTypeDef = TypedDict(
    "CreateOTAUpdateResponseTypeDef",
    {
        "otaUpdateId": str,
        "awsIotJobId": str,
        "otaUpdateArn": str,
        "awsIotJobArn": str,
        "otaUpdateStatus": OTAUpdateStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePolicyRequestRequestTypeDef",
    {
        "policyName": str,
        "policyDocument": str,
    },
)
_OptionalCreatePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePolicyRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreatePolicyRequestRequestTypeDef(
    _RequiredCreatePolicyRequestRequestTypeDef, _OptionalCreatePolicyRequestRequestTypeDef
):
    pass

CreatePolicyResponseTypeDef = TypedDict(
    "CreatePolicyResponseTypeDef",
    {
        "policyName": str,
        "policyArn": str,
        "policyDocument": str,
        "policyVersionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePolicyVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePolicyVersionRequestRequestTypeDef",
    {
        "policyName": str,
        "policyDocument": str,
    },
)
_OptionalCreatePolicyVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePolicyVersionRequestRequestTypeDef",
    {
        "setAsDefault": bool,
    },
    total=False,
)

class CreatePolicyVersionRequestRequestTypeDef(
    _RequiredCreatePolicyVersionRequestRequestTypeDef,
    _OptionalCreatePolicyVersionRequestRequestTypeDef,
):
    pass

CreatePolicyVersionResponseTypeDef = TypedDict(
    "CreatePolicyVersionResponseTypeDef",
    {
        "policyArn": str,
        "policyDocument": str,
        "policyVersionId": str,
        "isDefaultVersion": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProvisioningClaimRequestRequestTypeDef = TypedDict(
    "CreateProvisioningClaimRequestRequestTypeDef",
    {
        "templateName": str,
    },
)

CreateProvisioningClaimResponseTypeDef = TypedDict(
    "CreateProvisioningClaimResponseTypeDef",
    {
        "certificateId": str,
        "certificatePem": str,
        "keyPair": "KeyPairTypeDef",
        "expiration": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProvisioningTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProvisioningTemplateRequestRequestTypeDef",
    {
        "templateName": str,
        "templateBody": str,
        "provisioningRoleArn": str,
    },
)
_OptionalCreateProvisioningTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProvisioningTemplateRequestRequestTypeDef",
    {
        "description": str,
        "enabled": bool,
        "preProvisioningHook": "ProvisioningHookTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateProvisioningTemplateRequestRequestTypeDef(
    _RequiredCreateProvisioningTemplateRequestRequestTypeDef,
    _OptionalCreateProvisioningTemplateRequestRequestTypeDef,
):
    pass

CreateProvisioningTemplateResponseTypeDef = TypedDict(
    "CreateProvisioningTemplateResponseTypeDef",
    {
        "templateArn": str,
        "templateName": str,
        "defaultVersionId": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProvisioningTemplateVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProvisioningTemplateVersionRequestRequestTypeDef",
    {
        "templateName": str,
        "templateBody": str,
    },
)
_OptionalCreateProvisioningTemplateVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProvisioningTemplateVersionRequestRequestTypeDef",
    {
        "setAsDefault": bool,
    },
    total=False,
)

class CreateProvisioningTemplateVersionRequestRequestTypeDef(
    _RequiredCreateProvisioningTemplateVersionRequestRequestTypeDef,
    _OptionalCreateProvisioningTemplateVersionRequestRequestTypeDef,
):
    pass

CreateProvisioningTemplateVersionResponseTypeDef = TypedDict(
    "CreateProvisioningTemplateVersionResponseTypeDef",
    {
        "templateArn": str,
        "templateName": str,
        "versionId": int,
        "isDefaultVersion": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRoleAliasRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRoleAliasRequestRequestTypeDef",
    {
        "roleAlias": str,
        "roleArn": str,
    },
)
_OptionalCreateRoleAliasRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRoleAliasRequestRequestTypeDef",
    {
        "credentialDurationSeconds": int,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateRoleAliasRequestRequestTypeDef(
    _RequiredCreateRoleAliasRequestRequestTypeDef, _OptionalCreateRoleAliasRequestRequestTypeDef
):
    pass

CreateRoleAliasResponseTypeDef = TypedDict(
    "CreateRoleAliasResponseTypeDef",
    {
        "roleAlias": str,
        "roleAliasArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateScheduledAuditRequestRequestTypeDef = TypedDict(
    "_RequiredCreateScheduledAuditRequestRequestTypeDef",
    {
        "frequency": AuditFrequencyType,
        "targetCheckNames": List[str],
        "scheduledAuditName": str,
    },
)
_OptionalCreateScheduledAuditRequestRequestTypeDef = TypedDict(
    "_OptionalCreateScheduledAuditRequestRequestTypeDef",
    {
        "dayOfMonth": str,
        "dayOfWeek": DayOfWeekType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateScheduledAuditRequestRequestTypeDef(
    _RequiredCreateScheduledAuditRequestRequestTypeDef,
    _OptionalCreateScheduledAuditRequestRequestTypeDef,
):
    pass

CreateScheduledAuditResponseTypeDef = TypedDict(
    "CreateScheduledAuditResponseTypeDef",
    {
        "scheduledAuditArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSecurityProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSecurityProfileRequestRequestTypeDef",
    {
        "securityProfileName": str,
    },
)
_OptionalCreateSecurityProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSecurityProfileRequestRequestTypeDef",
    {
        "securityProfileDescription": str,
        "behaviors": List["BehaviorTypeDef"],
        "alertTargets": Dict[Literal["SNS"], "AlertTargetTypeDef"],
        "additionalMetricsToRetain": List[str],
        "additionalMetricsToRetainV2": List["MetricToRetainTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateSecurityProfileRequestRequestTypeDef(
    _RequiredCreateSecurityProfileRequestRequestTypeDef,
    _OptionalCreateSecurityProfileRequestRequestTypeDef,
):
    pass

CreateSecurityProfileResponseTypeDef = TypedDict(
    "CreateSecurityProfileResponseTypeDef",
    {
        "securityProfileName": str,
        "securityProfileArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStreamRequestRequestTypeDef = TypedDict(
    "_RequiredCreateStreamRequestRequestTypeDef",
    {
        "streamId": str,
        "files": List["StreamFileTypeDef"],
        "roleArn": str,
    },
)
_OptionalCreateStreamRequestRequestTypeDef = TypedDict(
    "_OptionalCreateStreamRequestRequestTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateStreamRequestRequestTypeDef(
    _RequiredCreateStreamRequestRequestTypeDef, _OptionalCreateStreamRequestRequestTypeDef
):
    pass

CreateStreamResponseTypeDef = TypedDict(
    "CreateStreamResponseTypeDef",
    {
        "streamId": str,
        "streamArn": str,
        "description": str,
        "streamVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateThingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateThingGroupRequestRequestTypeDef",
    {
        "thingGroupName": str,
    },
)
_OptionalCreateThingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateThingGroupRequestRequestTypeDef",
    {
        "parentGroupName": str,
        "thingGroupProperties": "ThingGroupPropertiesTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateThingGroupRequestRequestTypeDef(
    _RequiredCreateThingGroupRequestRequestTypeDef, _OptionalCreateThingGroupRequestRequestTypeDef
):
    pass

CreateThingGroupResponseTypeDef = TypedDict(
    "CreateThingGroupResponseTypeDef",
    {
        "thingGroupName": str,
        "thingGroupArn": str,
        "thingGroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateThingRequestRequestTypeDef = TypedDict(
    "_RequiredCreateThingRequestRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalCreateThingRequestRequestTypeDef = TypedDict(
    "_OptionalCreateThingRequestRequestTypeDef",
    {
        "thingTypeName": str,
        "attributePayload": "AttributePayloadTypeDef",
        "billingGroupName": str,
    },
    total=False,
)

class CreateThingRequestRequestTypeDef(
    _RequiredCreateThingRequestRequestTypeDef, _OptionalCreateThingRequestRequestTypeDef
):
    pass

CreateThingResponseTypeDef = TypedDict(
    "CreateThingResponseTypeDef",
    {
        "thingName": str,
        "thingArn": str,
        "thingId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateThingTypeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateThingTypeRequestRequestTypeDef",
    {
        "thingTypeName": str,
    },
)
_OptionalCreateThingTypeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateThingTypeRequestRequestTypeDef",
    {
        "thingTypeProperties": "ThingTypePropertiesTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateThingTypeRequestRequestTypeDef(
    _RequiredCreateThingTypeRequestRequestTypeDef, _OptionalCreateThingTypeRequestRequestTypeDef
):
    pass

CreateThingTypeResponseTypeDef = TypedDict(
    "CreateThingTypeResponseTypeDef",
    {
        "thingTypeName": str,
        "thingTypeArn": str,
        "thingTypeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTopicRuleDestinationRequestRequestTypeDef = TypedDict(
    "CreateTopicRuleDestinationRequestRequestTypeDef",
    {
        "destinationConfiguration": "TopicRuleDestinationConfigurationTypeDef",
    },
)

CreateTopicRuleDestinationResponseTypeDef = TypedDict(
    "CreateTopicRuleDestinationResponseTypeDef",
    {
        "topicRuleDestination": "TopicRuleDestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTopicRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTopicRuleRequestRequestTypeDef",
    {
        "ruleName": str,
        "topicRulePayload": "TopicRulePayloadTypeDef",
    },
)
_OptionalCreateTopicRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTopicRuleRequestRequestTypeDef",
    {
        "tags": str,
    },
    total=False,
)

class CreateTopicRuleRequestRequestTypeDef(
    _RequiredCreateTopicRuleRequestRequestTypeDef, _OptionalCreateTopicRuleRequestRequestTypeDef
):
    pass

CustomCodeSigningTypeDef = TypedDict(
    "CustomCodeSigningTypeDef",
    {
        "signature": "CodeSigningSignatureTypeDef",
        "certificateChain": "CodeSigningCertificateChainTypeDef",
        "hashAlgorithm": str,
        "signatureAlgorithm": str,
    },
    total=False,
)

DeleteAccountAuditConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteAccountAuditConfigurationRequestRequestTypeDef",
    {
        "deleteScheduledAudits": bool,
    },
    total=False,
)

DeleteAuditSuppressionRequestRequestTypeDef = TypedDict(
    "DeleteAuditSuppressionRequestRequestTypeDef",
    {
        "checkName": str,
        "resourceIdentifier": "ResourceIdentifierTypeDef",
    },
)

DeleteAuthorizerRequestRequestTypeDef = TypedDict(
    "DeleteAuthorizerRequestRequestTypeDef",
    {
        "authorizerName": str,
    },
)

_RequiredDeleteBillingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBillingGroupRequestRequestTypeDef",
    {
        "billingGroupName": str,
    },
)
_OptionalDeleteBillingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBillingGroupRequestRequestTypeDef",
    {
        "expectedVersion": int,
    },
    total=False,
)

class DeleteBillingGroupRequestRequestTypeDef(
    _RequiredDeleteBillingGroupRequestRequestTypeDef,
    _OptionalDeleteBillingGroupRequestRequestTypeDef,
):
    pass

DeleteCACertificateRequestRequestTypeDef = TypedDict(
    "DeleteCACertificateRequestRequestTypeDef",
    {
        "certificateId": str,
    },
)

_RequiredDeleteCertificateRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteCertificateRequestRequestTypeDef",
    {
        "certificateId": str,
    },
)
_OptionalDeleteCertificateRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteCertificateRequestRequestTypeDef",
    {
        "forceDelete": bool,
    },
    total=False,
)

class DeleteCertificateRequestRequestTypeDef(
    _RequiredDeleteCertificateRequestRequestTypeDef, _OptionalDeleteCertificateRequestRequestTypeDef
):
    pass

DeleteCustomMetricRequestRequestTypeDef = TypedDict(
    "DeleteCustomMetricRequestRequestTypeDef",
    {
        "metricName": str,
    },
)

DeleteDimensionRequestRequestTypeDef = TypedDict(
    "DeleteDimensionRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteDomainConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteDomainConfigurationRequestRequestTypeDef",
    {
        "domainConfigurationName": str,
    },
)

_RequiredDeleteDynamicThingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteDynamicThingGroupRequestRequestTypeDef",
    {
        "thingGroupName": str,
    },
)
_OptionalDeleteDynamicThingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteDynamicThingGroupRequestRequestTypeDef",
    {
        "expectedVersion": int,
    },
    total=False,
)

class DeleteDynamicThingGroupRequestRequestTypeDef(
    _RequiredDeleteDynamicThingGroupRequestRequestTypeDef,
    _OptionalDeleteDynamicThingGroupRequestRequestTypeDef,
):
    pass

_RequiredDeleteJobExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteJobExecutionRequestRequestTypeDef",
    {
        "jobId": str,
        "thingName": str,
        "executionNumber": int,
    },
)
_OptionalDeleteJobExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteJobExecutionRequestRequestTypeDef",
    {
        "force": bool,
        "namespaceId": str,
    },
    total=False,
)

class DeleteJobExecutionRequestRequestTypeDef(
    _RequiredDeleteJobExecutionRequestRequestTypeDef,
    _OptionalDeleteJobExecutionRequestRequestTypeDef,
):
    pass

_RequiredDeleteJobRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)
_OptionalDeleteJobRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteJobRequestRequestTypeDef",
    {
        "force": bool,
        "namespaceId": str,
    },
    total=False,
)

class DeleteJobRequestRequestTypeDef(
    _RequiredDeleteJobRequestRequestTypeDef, _OptionalDeleteJobRequestRequestTypeDef
):
    pass

DeleteJobTemplateRequestRequestTypeDef = TypedDict(
    "DeleteJobTemplateRequestRequestTypeDef",
    {
        "jobTemplateId": str,
    },
)

DeleteMitigationActionRequestRequestTypeDef = TypedDict(
    "DeleteMitigationActionRequestRequestTypeDef",
    {
        "actionName": str,
    },
)

_RequiredDeleteOTAUpdateRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteOTAUpdateRequestRequestTypeDef",
    {
        "otaUpdateId": str,
    },
)
_OptionalDeleteOTAUpdateRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteOTAUpdateRequestRequestTypeDef",
    {
        "deleteStream": bool,
        "forceDeleteAWSJob": bool,
    },
    total=False,
)

class DeleteOTAUpdateRequestRequestTypeDef(
    _RequiredDeleteOTAUpdateRequestRequestTypeDef, _OptionalDeleteOTAUpdateRequestRequestTypeDef
):
    pass

DeletePolicyRequestRequestTypeDef = TypedDict(
    "DeletePolicyRequestRequestTypeDef",
    {
        "policyName": str,
    },
)

DeletePolicyVersionRequestRequestTypeDef = TypedDict(
    "DeletePolicyVersionRequestRequestTypeDef",
    {
        "policyName": str,
        "policyVersionId": str,
    },
)

DeleteProvisioningTemplateRequestRequestTypeDef = TypedDict(
    "DeleteProvisioningTemplateRequestRequestTypeDef",
    {
        "templateName": str,
    },
)

DeleteProvisioningTemplateVersionRequestRequestTypeDef = TypedDict(
    "DeleteProvisioningTemplateVersionRequestRequestTypeDef",
    {
        "templateName": str,
        "versionId": int,
    },
)

DeleteRoleAliasRequestRequestTypeDef = TypedDict(
    "DeleteRoleAliasRequestRequestTypeDef",
    {
        "roleAlias": str,
    },
)

DeleteScheduledAuditRequestRequestTypeDef = TypedDict(
    "DeleteScheduledAuditRequestRequestTypeDef",
    {
        "scheduledAuditName": str,
    },
)

_RequiredDeleteSecurityProfileRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteSecurityProfileRequestRequestTypeDef",
    {
        "securityProfileName": str,
    },
)
_OptionalDeleteSecurityProfileRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteSecurityProfileRequestRequestTypeDef",
    {
        "expectedVersion": int,
    },
    total=False,
)

class DeleteSecurityProfileRequestRequestTypeDef(
    _RequiredDeleteSecurityProfileRequestRequestTypeDef,
    _OptionalDeleteSecurityProfileRequestRequestTypeDef,
):
    pass

DeleteStreamRequestRequestTypeDef = TypedDict(
    "DeleteStreamRequestRequestTypeDef",
    {
        "streamId": str,
    },
)

_RequiredDeleteThingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteThingGroupRequestRequestTypeDef",
    {
        "thingGroupName": str,
    },
)
_OptionalDeleteThingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteThingGroupRequestRequestTypeDef",
    {
        "expectedVersion": int,
    },
    total=False,
)

class DeleteThingGroupRequestRequestTypeDef(
    _RequiredDeleteThingGroupRequestRequestTypeDef, _OptionalDeleteThingGroupRequestRequestTypeDef
):
    pass

_RequiredDeleteThingRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteThingRequestRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalDeleteThingRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteThingRequestRequestTypeDef",
    {
        "expectedVersion": int,
    },
    total=False,
)

class DeleteThingRequestRequestTypeDef(
    _RequiredDeleteThingRequestRequestTypeDef, _OptionalDeleteThingRequestRequestTypeDef
):
    pass

DeleteThingTypeRequestRequestTypeDef = TypedDict(
    "DeleteThingTypeRequestRequestTypeDef",
    {
        "thingTypeName": str,
    },
)

DeleteTopicRuleDestinationRequestRequestTypeDef = TypedDict(
    "DeleteTopicRuleDestinationRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteTopicRuleRequestRequestTypeDef = TypedDict(
    "DeleteTopicRuleRequestRequestTypeDef",
    {
        "ruleName": str,
    },
)

DeleteV2LoggingLevelRequestRequestTypeDef = TypedDict(
    "DeleteV2LoggingLevelRequestRequestTypeDef",
    {
        "targetType": LogTargetTypeType,
        "targetName": str,
    },
)

DeniedTypeDef = TypedDict(
    "DeniedTypeDef",
    {
        "implicitDeny": "ImplicitDenyTypeDef",
        "explicitDeny": "ExplicitDenyTypeDef",
    },
    total=False,
)

_RequiredDeprecateThingTypeRequestRequestTypeDef = TypedDict(
    "_RequiredDeprecateThingTypeRequestRequestTypeDef",
    {
        "thingTypeName": str,
    },
)
_OptionalDeprecateThingTypeRequestRequestTypeDef = TypedDict(
    "_OptionalDeprecateThingTypeRequestRequestTypeDef",
    {
        "undoDeprecate": bool,
    },
    total=False,
)

class DeprecateThingTypeRequestRequestTypeDef(
    _RequiredDeprecateThingTypeRequestRequestTypeDef,
    _OptionalDeprecateThingTypeRequestRequestTypeDef,
):
    pass

DescribeAccountAuditConfigurationResponseTypeDef = TypedDict(
    "DescribeAccountAuditConfigurationResponseTypeDef",
    {
        "roleArn": str,
        "auditNotificationTargetConfigurations": Dict[
            Literal["SNS"], "AuditNotificationTargetTypeDef"
        ],
        "auditCheckConfigurations": Dict[str, "AuditCheckConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAuditFindingRequestRequestTypeDef = TypedDict(
    "DescribeAuditFindingRequestRequestTypeDef",
    {
        "findingId": str,
    },
)

DescribeAuditFindingResponseTypeDef = TypedDict(
    "DescribeAuditFindingResponseTypeDef",
    {
        "finding": "AuditFindingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAuditMitigationActionsTaskRequestRequestTypeDef = TypedDict(
    "DescribeAuditMitigationActionsTaskRequestRequestTypeDef",
    {
        "taskId": str,
    },
)

DescribeAuditMitigationActionsTaskResponseTypeDef = TypedDict(
    "DescribeAuditMitigationActionsTaskResponseTypeDef",
    {
        "taskStatus": AuditMitigationActionsTaskStatusType,
        "startTime": datetime,
        "endTime": datetime,
        "taskStatistics": Dict[str, "TaskStatisticsForAuditCheckTypeDef"],
        "target": "AuditMitigationActionsTaskTargetTypeDef",
        "auditCheckToActionsMapping": Dict[str, List[str]],
        "actionsDefinition": List["MitigationActionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAuditSuppressionRequestRequestTypeDef = TypedDict(
    "DescribeAuditSuppressionRequestRequestTypeDef",
    {
        "checkName": str,
        "resourceIdentifier": "ResourceIdentifierTypeDef",
    },
)

DescribeAuditSuppressionResponseTypeDef = TypedDict(
    "DescribeAuditSuppressionResponseTypeDef",
    {
        "checkName": str,
        "resourceIdentifier": "ResourceIdentifierTypeDef",
        "expirationDate": datetime,
        "suppressIndefinitely": bool,
        "description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAuditTaskRequestRequestTypeDef = TypedDict(
    "DescribeAuditTaskRequestRequestTypeDef",
    {
        "taskId": str,
    },
)

DescribeAuditTaskResponseTypeDef = TypedDict(
    "DescribeAuditTaskResponseTypeDef",
    {
        "taskStatus": AuditTaskStatusType,
        "taskType": AuditTaskTypeType,
        "taskStartTime": datetime,
        "taskStatistics": "TaskStatisticsTypeDef",
        "scheduledAuditName": str,
        "auditDetails": Dict[str, "AuditCheckDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAuthorizerRequestRequestTypeDef = TypedDict(
    "DescribeAuthorizerRequestRequestTypeDef",
    {
        "authorizerName": str,
    },
)

DescribeAuthorizerResponseTypeDef = TypedDict(
    "DescribeAuthorizerResponseTypeDef",
    {
        "authorizerDescription": "AuthorizerDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBillingGroupRequestRequestTypeDef = TypedDict(
    "DescribeBillingGroupRequestRequestTypeDef",
    {
        "billingGroupName": str,
    },
)

DescribeBillingGroupResponseTypeDef = TypedDict(
    "DescribeBillingGroupResponseTypeDef",
    {
        "billingGroupName": str,
        "billingGroupId": str,
        "billingGroupArn": str,
        "version": int,
        "billingGroupProperties": "BillingGroupPropertiesTypeDef",
        "billingGroupMetadata": "BillingGroupMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCACertificateRequestRequestTypeDef = TypedDict(
    "DescribeCACertificateRequestRequestTypeDef",
    {
        "certificateId": str,
    },
)

DescribeCACertificateResponseTypeDef = TypedDict(
    "DescribeCACertificateResponseTypeDef",
    {
        "certificateDescription": "CACertificateDescriptionTypeDef",
        "registrationConfig": "RegistrationConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCertificateRequestRequestTypeDef = TypedDict(
    "DescribeCertificateRequestRequestTypeDef",
    {
        "certificateId": str,
    },
)

DescribeCertificateResponseTypeDef = TypedDict(
    "DescribeCertificateResponseTypeDef",
    {
        "certificateDescription": "CertificateDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCustomMetricRequestRequestTypeDef = TypedDict(
    "DescribeCustomMetricRequestRequestTypeDef",
    {
        "metricName": str,
    },
)

DescribeCustomMetricResponseTypeDef = TypedDict(
    "DescribeCustomMetricResponseTypeDef",
    {
        "metricName": str,
        "metricArn": str,
        "metricType": CustomMetricTypeType,
        "displayName": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDefaultAuthorizerResponseTypeDef = TypedDict(
    "DescribeDefaultAuthorizerResponseTypeDef",
    {
        "authorizerDescription": "AuthorizerDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDetectMitigationActionsTaskRequestRequestTypeDef = TypedDict(
    "DescribeDetectMitigationActionsTaskRequestRequestTypeDef",
    {
        "taskId": str,
    },
)

DescribeDetectMitigationActionsTaskResponseTypeDef = TypedDict(
    "DescribeDetectMitigationActionsTaskResponseTypeDef",
    {
        "taskSummary": "DetectMitigationActionsTaskSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDimensionRequestRequestTypeDef = TypedDict(
    "DescribeDimensionRequestRequestTypeDef",
    {
        "name": str,
    },
)

DescribeDimensionResponseTypeDef = TypedDict(
    "DescribeDimensionResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "type": Literal["TOPIC_FILTER"],
        "stringValues": List[str],
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeDomainConfigurationRequestRequestTypeDef",
    {
        "domainConfigurationName": str,
    },
)

DescribeDomainConfigurationResponseTypeDef = TypedDict(
    "DescribeDomainConfigurationResponseTypeDef",
    {
        "domainConfigurationName": str,
        "domainConfigurationArn": str,
        "domainName": str,
        "serverCertificates": List["ServerCertificateSummaryTypeDef"],
        "authorizerConfig": "AuthorizerConfigTypeDef",
        "domainConfigurationStatus": DomainConfigurationStatusType,
        "serviceType": ServiceTypeType,
        "domainType": DomainTypeType,
        "lastStatusChangeDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointRequestRequestTypeDef = TypedDict(
    "DescribeEndpointRequestRequestTypeDef",
    {
        "endpointType": str,
    },
    total=False,
)

DescribeEndpointResponseTypeDef = TypedDict(
    "DescribeEndpointResponseTypeDef",
    {
        "endpointAddress": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventConfigurationsResponseTypeDef = TypedDict(
    "DescribeEventConfigurationsResponseTypeDef",
    {
        "eventConfigurations": Dict[EventTypeType, "ConfigurationTypeDef"],
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIndexRequestRequestTypeDef = TypedDict(
    "DescribeIndexRequestRequestTypeDef",
    {
        "indexName": str,
    },
)

DescribeIndexResponseTypeDef = TypedDict(
    "DescribeIndexResponseTypeDef",
    {
        "indexName": str,
        "indexStatus": IndexStatusType,
        "schema": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeJobExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeJobExecutionRequestRequestTypeDef",
    {
        "jobId": str,
        "thingName": str,
    },
)
_OptionalDescribeJobExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeJobExecutionRequestRequestTypeDef",
    {
        "executionNumber": int,
    },
    total=False,
)

class DescribeJobExecutionRequestRequestTypeDef(
    _RequiredDescribeJobExecutionRequestRequestTypeDef,
    _OptionalDescribeJobExecutionRequestRequestTypeDef,
):
    pass

DescribeJobExecutionResponseTypeDef = TypedDict(
    "DescribeJobExecutionResponseTypeDef",
    {
        "execution": "JobExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobRequestRequestTypeDef = TypedDict(
    "DescribeJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

DescribeJobResponseTypeDef = TypedDict(
    "DescribeJobResponseTypeDef",
    {
        "documentSource": str,
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobTemplateRequestRequestTypeDef = TypedDict(
    "DescribeJobTemplateRequestRequestTypeDef",
    {
        "jobTemplateId": str,
    },
)

DescribeJobTemplateResponseTypeDef = TypedDict(
    "DescribeJobTemplateResponseTypeDef",
    {
        "jobTemplateArn": str,
        "jobTemplateId": str,
        "description": str,
        "documentSource": str,
        "document": str,
        "createdAt": datetime,
        "presignedUrlConfig": "PresignedUrlConfigTypeDef",
        "jobExecutionsRolloutConfig": "JobExecutionsRolloutConfigTypeDef",
        "abortConfig": "AbortConfigTypeDef",
        "timeoutConfig": "TimeoutConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMitigationActionRequestRequestTypeDef = TypedDict(
    "DescribeMitigationActionRequestRequestTypeDef",
    {
        "actionName": str,
    },
)

DescribeMitigationActionResponseTypeDef = TypedDict(
    "DescribeMitigationActionResponseTypeDef",
    {
        "actionName": str,
        "actionType": MitigationActionTypeType,
        "actionArn": str,
        "actionId": str,
        "roleArn": str,
        "actionParams": "MitigationActionParamsTypeDef",
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProvisioningTemplateRequestRequestTypeDef = TypedDict(
    "DescribeProvisioningTemplateRequestRequestTypeDef",
    {
        "templateName": str,
    },
)

DescribeProvisioningTemplateResponseTypeDef = TypedDict(
    "DescribeProvisioningTemplateResponseTypeDef",
    {
        "templateArn": str,
        "templateName": str,
        "description": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "defaultVersionId": int,
        "templateBody": str,
        "enabled": bool,
        "provisioningRoleArn": str,
        "preProvisioningHook": "ProvisioningHookTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProvisioningTemplateVersionRequestRequestTypeDef = TypedDict(
    "DescribeProvisioningTemplateVersionRequestRequestTypeDef",
    {
        "templateName": str,
        "versionId": int,
    },
)

DescribeProvisioningTemplateVersionResponseTypeDef = TypedDict(
    "DescribeProvisioningTemplateVersionResponseTypeDef",
    {
        "versionId": int,
        "creationDate": datetime,
        "templateBody": str,
        "isDefaultVersion": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRoleAliasRequestRequestTypeDef = TypedDict(
    "DescribeRoleAliasRequestRequestTypeDef",
    {
        "roleAlias": str,
    },
)

DescribeRoleAliasResponseTypeDef = TypedDict(
    "DescribeRoleAliasResponseTypeDef",
    {
        "roleAliasDescription": "RoleAliasDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScheduledAuditRequestRequestTypeDef = TypedDict(
    "DescribeScheduledAuditRequestRequestTypeDef",
    {
        "scheduledAuditName": str,
    },
)

DescribeScheduledAuditResponseTypeDef = TypedDict(
    "DescribeScheduledAuditResponseTypeDef",
    {
        "frequency": AuditFrequencyType,
        "dayOfMonth": str,
        "dayOfWeek": DayOfWeekType,
        "targetCheckNames": List[str],
        "scheduledAuditName": str,
        "scheduledAuditArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSecurityProfileRequestRequestTypeDef = TypedDict(
    "DescribeSecurityProfileRequestRequestTypeDef",
    {
        "securityProfileName": str,
    },
)

DescribeSecurityProfileResponseTypeDef = TypedDict(
    "DescribeSecurityProfileResponseTypeDef",
    {
        "securityProfileName": str,
        "securityProfileArn": str,
        "securityProfileDescription": str,
        "behaviors": List["BehaviorTypeDef"],
        "alertTargets": Dict[Literal["SNS"], "AlertTargetTypeDef"],
        "additionalMetricsToRetain": List[str],
        "additionalMetricsToRetainV2": List["MetricToRetainTypeDef"],
        "version": int,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStreamRequestRequestTypeDef = TypedDict(
    "DescribeStreamRequestRequestTypeDef",
    {
        "streamId": str,
    },
)

DescribeStreamResponseTypeDef = TypedDict(
    "DescribeStreamResponseTypeDef",
    {
        "streamInfo": "StreamInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeThingGroupRequestRequestTypeDef = TypedDict(
    "DescribeThingGroupRequestRequestTypeDef",
    {
        "thingGroupName": str,
    },
)

DescribeThingGroupResponseTypeDef = TypedDict(
    "DescribeThingGroupResponseTypeDef",
    {
        "thingGroupName": str,
        "thingGroupId": str,
        "thingGroupArn": str,
        "version": int,
        "thingGroupProperties": "ThingGroupPropertiesTypeDef",
        "thingGroupMetadata": "ThingGroupMetadataTypeDef",
        "indexName": str,
        "queryString": str,
        "queryVersion": str,
        "status": DynamicGroupStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeThingRegistrationTaskRequestRequestTypeDef = TypedDict(
    "DescribeThingRegistrationTaskRequestRequestTypeDef",
    {
        "taskId": str,
    },
)

DescribeThingRegistrationTaskResponseTypeDef = TypedDict(
    "DescribeThingRegistrationTaskResponseTypeDef",
    {
        "taskId": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "templateBody": str,
        "inputFileBucket": str,
        "inputFileKey": str,
        "roleArn": str,
        "status": StatusType,
        "message": str,
        "successCount": int,
        "failureCount": int,
        "percentageProgress": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeThingRequestRequestTypeDef = TypedDict(
    "DescribeThingRequestRequestTypeDef",
    {
        "thingName": str,
    },
)

DescribeThingResponseTypeDef = TypedDict(
    "DescribeThingResponseTypeDef",
    {
        "defaultClientId": str,
        "thingName": str,
        "thingId": str,
        "thingArn": str,
        "thingTypeName": str,
        "attributes": Dict[str, str],
        "version": int,
        "billingGroupName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeThingTypeRequestRequestTypeDef = TypedDict(
    "DescribeThingTypeRequestRequestTypeDef",
    {
        "thingTypeName": str,
    },
)

DescribeThingTypeResponseTypeDef = TypedDict(
    "DescribeThingTypeResponseTypeDef",
    {
        "thingTypeName": str,
        "thingTypeId": str,
        "thingTypeArn": str,
        "thingTypeProperties": "ThingTypePropertiesTypeDef",
        "thingTypeMetadata": "ThingTypeMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "s3Destination": "S3DestinationTypeDef",
    },
    total=False,
)

DetachPolicyRequestRequestTypeDef = TypedDict(
    "DetachPolicyRequestRequestTypeDef",
    {
        "policyName": str,
        "target": str,
    },
)

DetachPrincipalPolicyRequestRequestTypeDef = TypedDict(
    "DetachPrincipalPolicyRequestRequestTypeDef",
    {
        "policyName": str,
        "principal": str,
    },
)

DetachSecurityProfileRequestRequestTypeDef = TypedDict(
    "DetachSecurityProfileRequestRequestTypeDef",
    {
        "securityProfileName": str,
        "securityProfileTargetArn": str,
    },
)

DetachThingPrincipalRequestRequestTypeDef = TypedDict(
    "DetachThingPrincipalRequestRequestTypeDef",
    {
        "thingName": str,
        "principal": str,
    },
)

DetectMitigationActionExecutionTypeDef = TypedDict(
    "DetectMitigationActionExecutionTypeDef",
    {
        "taskId": str,
        "violationId": str,
        "actionName": str,
        "thingName": str,
        "executionStartDate": datetime,
        "executionEndDate": datetime,
        "status": DetectMitigationActionExecutionStatusType,
        "errorCode": str,
        "message": str,
    },
    total=False,
)

DetectMitigationActionsTaskStatisticsTypeDef = TypedDict(
    "DetectMitigationActionsTaskStatisticsTypeDef",
    {
        "actionsExecuted": int,
        "actionsSkipped": int,
        "actionsFailed": int,
    },
    total=False,
)

DetectMitigationActionsTaskSummaryTypeDef = TypedDict(
    "DetectMitigationActionsTaskSummaryTypeDef",
    {
        "taskId": str,
        "taskStatus": DetectMitigationActionsTaskStatusType,
        "taskStartTime": datetime,
        "taskEndTime": datetime,
        "target": "DetectMitigationActionsTaskTargetTypeDef",
        "violationEventOccurrenceRange": "ViolationEventOccurrenceRangeTypeDef",
        "onlyActiveViolationsIncluded": bool,
        "suppressedAlertsIncluded": bool,
        "actionsDefinition": List["MitigationActionTypeDef"],
        "taskStatistics": "DetectMitigationActionsTaskStatisticsTypeDef",
    },
    total=False,
)

DetectMitigationActionsTaskTargetTypeDef = TypedDict(
    "DetectMitigationActionsTaskTargetTypeDef",
    {
        "violationIds": List[str],
        "securityProfileName": str,
        "behaviorName": str,
    },
    total=False,
)

DisableTopicRuleRequestRequestTypeDef = TypedDict(
    "DisableTopicRuleRequestRequestTypeDef",
    {
        "ruleName": str,
    },
)

DomainConfigurationSummaryTypeDef = TypedDict(
    "DomainConfigurationSummaryTypeDef",
    {
        "domainConfigurationName": str,
        "domainConfigurationArn": str,
        "serviceType": ServiceTypeType,
    },
    total=False,
)

_RequiredDynamoDBActionTypeDef = TypedDict(
    "_RequiredDynamoDBActionTypeDef",
    {
        "tableName": str,
        "roleArn": str,
        "hashKeyField": str,
        "hashKeyValue": str,
    },
)
_OptionalDynamoDBActionTypeDef = TypedDict(
    "_OptionalDynamoDBActionTypeDef",
    {
        "operation": str,
        "hashKeyType": DynamoKeyTypeType,
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "rangeKeyType": DynamoKeyTypeType,
        "payloadField": str,
    },
    total=False,
)

class DynamoDBActionTypeDef(_RequiredDynamoDBActionTypeDef, _OptionalDynamoDBActionTypeDef):
    pass

DynamoDBv2ActionTypeDef = TypedDict(
    "DynamoDBv2ActionTypeDef",
    {
        "roleArn": str,
        "putItem": "PutItemInputTypeDef",
    },
)

EffectivePolicyTypeDef = TypedDict(
    "EffectivePolicyTypeDef",
    {
        "policyName": str,
        "policyArn": str,
        "policyDocument": str,
    },
    total=False,
)

ElasticsearchActionTypeDef = TypedDict(
    "ElasticsearchActionTypeDef",
    {
        "roleArn": str,
        "endpoint": str,
        "index": str,
        "type": str,
        "id": str,
    },
)

EnableIoTLoggingParamsTypeDef = TypedDict(
    "EnableIoTLoggingParamsTypeDef",
    {
        "roleArnForLogging": str,
        "logLevel": LogLevelType,
    },
)

EnableTopicRuleRequestRequestTypeDef = TypedDict(
    "EnableTopicRuleRequestRequestTypeDef",
    {
        "ruleName": str,
    },
)

ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "code": str,
        "message": str,
    },
    total=False,
)

ExplicitDenyTypeDef = TypedDict(
    "ExplicitDenyTypeDef",
    {
        "policies": List["PolicyTypeDef"],
    },
    total=False,
)

ExponentialRolloutRateTypeDef = TypedDict(
    "ExponentialRolloutRateTypeDef",
    {
        "baseRatePerMinute": int,
        "incrementFactor": float,
        "rateIncreaseCriteria": "RateIncreaseCriteriaTypeDef",
    },
)

FieldTypeDef = TypedDict(
    "FieldTypeDef",
    {
        "name": str,
        "type": FieldTypeType,
    },
    total=False,
)

FileLocationTypeDef = TypedDict(
    "FileLocationTypeDef",
    {
        "stream": "StreamTypeDef",
        "s3Location": "S3LocationTypeDef",
    },
    total=False,
)

_RequiredFirehoseActionTypeDef = TypedDict(
    "_RequiredFirehoseActionTypeDef",
    {
        "roleArn": str,
        "deliveryStreamName": str,
    },
)
_OptionalFirehoseActionTypeDef = TypedDict(
    "_OptionalFirehoseActionTypeDef",
    {
        "separator": str,
        "batchMode": bool,
    },
    total=False,
)

class FirehoseActionTypeDef(_RequiredFirehoseActionTypeDef, _OptionalFirehoseActionTypeDef):
    pass

GetBehaviorModelTrainingSummariesRequestRequestTypeDef = TypedDict(
    "GetBehaviorModelTrainingSummariesRequestRequestTypeDef",
    {
        "securityProfileName": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

GetBehaviorModelTrainingSummariesResponseTypeDef = TypedDict(
    "GetBehaviorModelTrainingSummariesResponseTypeDef",
    {
        "summaries": List["BehaviorModelTrainingSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCardinalityRequestRequestTypeDef = TypedDict(
    "_RequiredGetCardinalityRequestRequestTypeDef",
    {
        "queryString": str,
    },
)
_OptionalGetCardinalityRequestRequestTypeDef = TypedDict(
    "_OptionalGetCardinalityRequestRequestTypeDef",
    {
        "indexName": str,
        "aggregationField": str,
        "queryVersion": str,
    },
    total=False,
)

class GetCardinalityRequestRequestTypeDef(
    _RequiredGetCardinalityRequestRequestTypeDef, _OptionalGetCardinalityRequestRequestTypeDef
):
    pass

GetCardinalityResponseTypeDef = TypedDict(
    "GetCardinalityResponseTypeDef",
    {
        "cardinality": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEffectivePoliciesRequestRequestTypeDef = TypedDict(
    "GetEffectivePoliciesRequestRequestTypeDef",
    {
        "principal": str,
        "cognitoIdentityPoolId": str,
        "thingName": str,
    },
    total=False,
)

GetEffectivePoliciesResponseTypeDef = TypedDict(
    "GetEffectivePoliciesResponseTypeDef",
    {
        "effectivePolicies": List["EffectivePolicyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIndexingConfigurationResponseTypeDef = TypedDict(
    "GetIndexingConfigurationResponseTypeDef",
    {
        "thingIndexingConfiguration": "ThingIndexingConfigurationTypeDef",
        "thingGroupIndexingConfiguration": "ThingGroupIndexingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobDocumentRequestRequestTypeDef = TypedDict(
    "GetJobDocumentRequestRequestTypeDef",
    {
        "jobId": str,
    },
)

GetJobDocumentResponseTypeDef = TypedDict(
    "GetJobDocumentResponseTypeDef",
    {
        "document": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoggingOptionsResponseTypeDef = TypedDict(
    "GetLoggingOptionsResponseTypeDef",
    {
        "roleArn": str,
        "logLevel": LogLevelType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOTAUpdateRequestRequestTypeDef = TypedDict(
    "GetOTAUpdateRequestRequestTypeDef",
    {
        "otaUpdateId": str,
    },
)

GetOTAUpdateResponseTypeDef = TypedDict(
    "GetOTAUpdateResponseTypeDef",
    {
        "otaUpdateInfo": "OTAUpdateInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPercentilesRequestRequestTypeDef = TypedDict(
    "_RequiredGetPercentilesRequestRequestTypeDef",
    {
        "queryString": str,
    },
)
_OptionalGetPercentilesRequestRequestTypeDef = TypedDict(
    "_OptionalGetPercentilesRequestRequestTypeDef",
    {
        "indexName": str,
        "aggregationField": str,
        "queryVersion": str,
        "percents": List[float],
    },
    total=False,
)

class GetPercentilesRequestRequestTypeDef(
    _RequiredGetPercentilesRequestRequestTypeDef, _OptionalGetPercentilesRequestRequestTypeDef
):
    pass

GetPercentilesResponseTypeDef = TypedDict(
    "GetPercentilesResponseTypeDef",
    {
        "percentiles": List["PercentPairTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyRequestRequestTypeDef = TypedDict(
    "GetPolicyRequestRequestTypeDef",
    {
        "policyName": str,
    },
)

GetPolicyResponseTypeDef = TypedDict(
    "GetPolicyResponseTypeDef",
    {
        "policyName": str,
        "policyArn": str,
        "policyDocument": str,
        "defaultVersionId": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "generationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyVersionRequestRequestTypeDef = TypedDict(
    "GetPolicyVersionRequestRequestTypeDef",
    {
        "policyName": str,
        "policyVersionId": str,
    },
)

GetPolicyVersionResponseTypeDef = TypedDict(
    "GetPolicyVersionResponseTypeDef",
    {
        "policyArn": str,
        "policyName": str,
        "policyDocument": str,
        "policyVersionId": str,
        "isDefaultVersion": bool,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "generationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegistrationCodeResponseTypeDef = TypedDict(
    "GetRegistrationCodeResponseTypeDef",
    {
        "registrationCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetStatisticsRequestRequestTypeDef = TypedDict(
    "_RequiredGetStatisticsRequestRequestTypeDef",
    {
        "queryString": str,
    },
)
_OptionalGetStatisticsRequestRequestTypeDef = TypedDict(
    "_OptionalGetStatisticsRequestRequestTypeDef",
    {
        "indexName": str,
        "aggregationField": str,
        "queryVersion": str,
    },
    total=False,
)

class GetStatisticsRequestRequestTypeDef(
    _RequiredGetStatisticsRequestRequestTypeDef, _OptionalGetStatisticsRequestRequestTypeDef
):
    pass

GetStatisticsResponseTypeDef = TypedDict(
    "GetStatisticsResponseTypeDef",
    {
        "statistics": "StatisticsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTopicRuleDestinationRequestRequestTypeDef = TypedDict(
    "GetTopicRuleDestinationRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetTopicRuleDestinationResponseTypeDef = TypedDict(
    "GetTopicRuleDestinationResponseTypeDef",
    {
        "topicRuleDestination": "TopicRuleDestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTopicRuleRequestRequestTypeDef = TypedDict(
    "GetTopicRuleRequestRequestTypeDef",
    {
        "ruleName": str,
    },
)

GetTopicRuleResponseTypeDef = TypedDict(
    "GetTopicRuleResponseTypeDef",
    {
        "ruleArn": str,
        "rule": "TopicRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetV2LoggingOptionsResponseTypeDef = TypedDict(
    "GetV2LoggingOptionsResponseTypeDef",
    {
        "roleArn": str,
        "defaultLogLevel": LogLevelType,
        "disableAllLogs": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupNameAndArnTypeDef = TypedDict(
    "GroupNameAndArnTypeDef",
    {
        "groupName": str,
        "groupArn": str,
    },
    total=False,
)

HttpActionHeaderTypeDef = TypedDict(
    "HttpActionHeaderTypeDef",
    {
        "key": str,
        "value": str,
    },
)

_RequiredHttpActionTypeDef = TypedDict(
    "_RequiredHttpActionTypeDef",
    {
        "url": str,
    },
)
_OptionalHttpActionTypeDef = TypedDict(
    "_OptionalHttpActionTypeDef",
    {
        "confirmationUrl": str,
        "headers": List["HttpActionHeaderTypeDef"],
        "auth": "HttpAuthorizationTypeDef",
    },
    total=False,
)

class HttpActionTypeDef(_RequiredHttpActionTypeDef, _OptionalHttpActionTypeDef):
    pass

HttpAuthorizationTypeDef = TypedDict(
    "HttpAuthorizationTypeDef",
    {
        "sigv4": "SigV4AuthorizationTypeDef",
    },
    total=False,
)

HttpContextTypeDef = TypedDict(
    "HttpContextTypeDef",
    {
        "headers": Dict[str, str],
        "queryString": str,
    },
    total=False,
)

HttpUrlDestinationConfigurationTypeDef = TypedDict(
    "HttpUrlDestinationConfigurationTypeDef",
    {
        "confirmationUrl": str,
    },
)

HttpUrlDestinationPropertiesTypeDef = TypedDict(
    "HttpUrlDestinationPropertiesTypeDef",
    {
        "confirmationUrl": str,
    },
    total=False,
)

HttpUrlDestinationSummaryTypeDef = TypedDict(
    "HttpUrlDestinationSummaryTypeDef",
    {
        "confirmationUrl": str,
    },
    total=False,
)

ImplicitDenyTypeDef = TypedDict(
    "ImplicitDenyTypeDef",
    {
        "policies": List["PolicyTypeDef"],
    },
    total=False,
)

IotAnalyticsActionTypeDef = TypedDict(
    "IotAnalyticsActionTypeDef",
    {
        "channelArn": str,
        "channelName": str,
        "batchMode": bool,
        "roleArn": str,
    },
    total=False,
)

_RequiredIotEventsActionTypeDef = TypedDict(
    "_RequiredIotEventsActionTypeDef",
    {
        "inputName": str,
        "roleArn": str,
    },
)
_OptionalIotEventsActionTypeDef = TypedDict(
    "_OptionalIotEventsActionTypeDef",
    {
        "messageId": str,
        "batchMode": bool,
    },
    total=False,
)

class IotEventsActionTypeDef(_RequiredIotEventsActionTypeDef, _OptionalIotEventsActionTypeDef):
    pass

IotSiteWiseActionTypeDef = TypedDict(
    "IotSiteWiseActionTypeDef",
    {
        "putAssetPropertyValueEntries": List["PutAssetPropertyValueEntryTypeDef"],
        "roleArn": str,
    },
)

JobExecutionStatusDetailsTypeDef = TypedDict(
    "JobExecutionStatusDetailsTypeDef",
    {
        "detailsMap": Dict[str, str],
    },
    total=False,
)

JobExecutionSummaryForJobTypeDef = TypedDict(
    "JobExecutionSummaryForJobTypeDef",
    {
        "thingArn": str,
        "jobExecutionSummary": "JobExecutionSummaryTypeDef",
    },
    total=False,
)

JobExecutionSummaryForThingTypeDef = TypedDict(
    "JobExecutionSummaryForThingTypeDef",
    {
        "jobId": str,
        "jobExecutionSummary": "JobExecutionSummaryTypeDef",
    },
    total=False,
)

JobExecutionSummaryTypeDef = TypedDict(
    "JobExecutionSummaryTypeDef",
    {
        "status": JobExecutionStatusType,
        "queuedAt": datetime,
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
        "executionNumber": int,
    },
    total=False,
)

JobExecutionTypeDef = TypedDict(
    "JobExecutionTypeDef",
    {
        "jobId": str,
        "status": JobExecutionStatusType,
        "forceCanceled": bool,
        "statusDetails": "JobExecutionStatusDetailsTypeDef",
        "thingArn": str,
        "queuedAt": datetime,
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
        "executionNumber": int,
        "versionNumber": int,
        "approximateSecondsBeforeTimedOut": int,
    },
    total=False,
)

JobExecutionsRolloutConfigTypeDef = TypedDict(
    "JobExecutionsRolloutConfigTypeDef",
    {
        "maximumPerMinute": int,
        "exponentialRate": "ExponentialRolloutRateTypeDef",
    },
    total=False,
)

JobProcessDetailsTypeDef = TypedDict(
    "JobProcessDetailsTypeDef",
    {
        "processingTargets": List[str],
        "numberOfCanceledThings": int,
        "numberOfSucceededThings": int,
        "numberOfFailedThings": int,
        "numberOfRejectedThings": int,
        "numberOfQueuedThings": int,
        "numberOfInProgressThings": int,
        "numberOfRemovedThings": int,
        "numberOfTimedOutThings": int,
    },
    total=False,
)

JobSummaryTypeDef = TypedDict(
    "JobSummaryTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "thingGroupId": str,
        "targetSelection": TargetSelectionType,
        "status": JobStatusType,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "completedAt": datetime,
    },
    total=False,
)

JobTemplateSummaryTypeDef = TypedDict(
    "JobTemplateSummaryTypeDef",
    {
        "jobTemplateArn": str,
        "jobTemplateId": str,
        "description": str,
        "createdAt": datetime,
    },
    total=False,
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "targetSelection": TargetSelectionType,
        "status": JobStatusType,
        "forceCanceled": bool,
        "reasonCode": str,
        "comment": str,
        "targets": List[str],
        "description": str,
        "presignedUrlConfig": "PresignedUrlConfigTypeDef",
        "jobExecutionsRolloutConfig": "JobExecutionsRolloutConfigTypeDef",
        "abortConfig": "AbortConfigTypeDef",
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "completedAt": datetime,
        "jobProcessDetails": "JobProcessDetailsTypeDef",
        "timeoutConfig": "TimeoutConfigTypeDef",
        "namespaceId": str,
        "jobTemplateArn": str,
    },
    total=False,
)

_RequiredKafkaActionTypeDef = TypedDict(
    "_RequiredKafkaActionTypeDef",
    {
        "destinationArn": str,
        "topic": str,
        "clientProperties": Dict[str, str],
    },
)
_OptionalKafkaActionTypeDef = TypedDict(
    "_OptionalKafkaActionTypeDef",
    {
        "key": str,
        "partition": str,
    },
    total=False,
)

class KafkaActionTypeDef(_RequiredKafkaActionTypeDef, _OptionalKafkaActionTypeDef):
    pass

KeyPairTypeDef = TypedDict(
    "KeyPairTypeDef",
    {
        "PublicKey": str,
        "PrivateKey": str,
    },
    total=False,
)

_RequiredKinesisActionTypeDef = TypedDict(
    "_RequiredKinesisActionTypeDef",
    {
        "roleArn": str,
        "streamName": str,
    },
)
_OptionalKinesisActionTypeDef = TypedDict(
    "_OptionalKinesisActionTypeDef",
    {
        "partitionKey": str,
    },
    total=False,
)

class KinesisActionTypeDef(_RequiredKinesisActionTypeDef, _OptionalKinesisActionTypeDef):
    pass

LambdaActionTypeDef = TypedDict(
    "LambdaActionTypeDef",
    {
        "functionArn": str,
    },
)

ListActiveViolationsRequestRequestTypeDef = TypedDict(
    "ListActiveViolationsRequestRequestTypeDef",
    {
        "thingName": str,
        "securityProfileName": str,
        "behaviorCriteriaType": BehaviorCriteriaTypeType,
        "listSuppressedAlerts": bool,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListActiveViolationsResponseTypeDef = TypedDict(
    "ListActiveViolationsResponseTypeDef",
    {
        "activeViolations": List["ActiveViolationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAttachedPoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredListAttachedPoliciesRequestRequestTypeDef",
    {
        "target": str,
    },
)
_OptionalListAttachedPoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalListAttachedPoliciesRequestRequestTypeDef",
    {
        "recursive": bool,
        "marker": str,
        "pageSize": int,
    },
    total=False,
)

class ListAttachedPoliciesRequestRequestTypeDef(
    _RequiredListAttachedPoliciesRequestRequestTypeDef,
    _OptionalListAttachedPoliciesRequestRequestTypeDef,
):
    pass

ListAttachedPoliciesResponseTypeDef = TypedDict(
    "ListAttachedPoliciesResponseTypeDef",
    {
        "policies": List["PolicyTypeDef"],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAuditFindingsRequestRequestTypeDef = TypedDict(
    "ListAuditFindingsRequestRequestTypeDef",
    {
        "taskId": str,
        "checkName": str,
        "resourceIdentifier": "ResourceIdentifierTypeDef",
        "maxResults": int,
        "nextToken": str,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "listSuppressedFindings": bool,
    },
    total=False,
)

ListAuditFindingsResponseTypeDef = TypedDict(
    "ListAuditFindingsResponseTypeDef",
    {
        "findings": List["AuditFindingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAuditMitigationActionsExecutionsRequestRequestTypeDef = TypedDict(
    "_RequiredListAuditMitigationActionsExecutionsRequestRequestTypeDef",
    {
        "taskId": str,
        "findingId": str,
    },
)
_OptionalListAuditMitigationActionsExecutionsRequestRequestTypeDef = TypedDict(
    "_OptionalListAuditMitigationActionsExecutionsRequestRequestTypeDef",
    {
        "actionStatus": AuditMitigationActionsExecutionStatusType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAuditMitigationActionsExecutionsRequestRequestTypeDef(
    _RequiredListAuditMitigationActionsExecutionsRequestRequestTypeDef,
    _OptionalListAuditMitigationActionsExecutionsRequestRequestTypeDef,
):
    pass

ListAuditMitigationActionsExecutionsResponseTypeDef = TypedDict(
    "ListAuditMitigationActionsExecutionsResponseTypeDef",
    {
        "actionsExecutions": List["AuditMitigationActionExecutionMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAuditMitigationActionsTasksRequestRequestTypeDef = TypedDict(
    "_RequiredListAuditMitigationActionsTasksRequestRequestTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)
_OptionalListAuditMitigationActionsTasksRequestRequestTypeDef = TypedDict(
    "_OptionalListAuditMitigationActionsTasksRequestRequestTypeDef",
    {
        "auditTaskId": str,
        "findingId": str,
        "taskStatus": AuditMitigationActionsTaskStatusType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAuditMitigationActionsTasksRequestRequestTypeDef(
    _RequiredListAuditMitigationActionsTasksRequestRequestTypeDef,
    _OptionalListAuditMitigationActionsTasksRequestRequestTypeDef,
):
    pass

ListAuditMitigationActionsTasksResponseTypeDef = TypedDict(
    "ListAuditMitigationActionsTasksResponseTypeDef",
    {
        "tasks": List["AuditMitigationActionsTaskMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAuditSuppressionsRequestRequestTypeDef = TypedDict(
    "ListAuditSuppressionsRequestRequestTypeDef",
    {
        "checkName": str,
        "resourceIdentifier": "ResourceIdentifierTypeDef",
        "ascendingOrder": bool,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListAuditSuppressionsResponseTypeDef = TypedDict(
    "ListAuditSuppressionsResponseTypeDef",
    {
        "suppressions": List["AuditSuppressionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAuditTasksRequestRequestTypeDef = TypedDict(
    "_RequiredListAuditTasksRequestRequestTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)
_OptionalListAuditTasksRequestRequestTypeDef = TypedDict(
    "_OptionalListAuditTasksRequestRequestTypeDef",
    {
        "taskType": AuditTaskTypeType,
        "taskStatus": AuditTaskStatusType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListAuditTasksRequestRequestTypeDef(
    _RequiredListAuditTasksRequestRequestTypeDef, _OptionalListAuditTasksRequestRequestTypeDef
):
    pass

ListAuditTasksResponseTypeDef = TypedDict(
    "ListAuditTasksResponseTypeDef",
    {
        "tasks": List["AuditTaskMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAuthorizersRequestRequestTypeDef = TypedDict(
    "ListAuthorizersRequestRequestTypeDef",
    {
        "pageSize": int,
        "marker": str,
        "ascendingOrder": bool,
        "status": AuthorizerStatusType,
    },
    total=False,
)

ListAuthorizersResponseTypeDef = TypedDict(
    "ListAuthorizersResponseTypeDef",
    {
        "authorizers": List["AuthorizerSummaryTypeDef"],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBillingGroupsRequestRequestTypeDef = TypedDict(
    "ListBillingGroupsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "namePrefixFilter": str,
    },
    total=False,
)

ListBillingGroupsResponseTypeDef = TypedDict(
    "ListBillingGroupsResponseTypeDef",
    {
        "billingGroups": List["GroupNameAndArnTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCACertificatesRequestRequestTypeDef = TypedDict(
    "ListCACertificatesRequestRequestTypeDef",
    {
        "pageSize": int,
        "marker": str,
        "ascendingOrder": bool,
    },
    total=False,
)

ListCACertificatesResponseTypeDef = TypedDict(
    "ListCACertificatesResponseTypeDef",
    {
        "certificates": List["CACertificateTypeDef"],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCertificatesByCARequestRequestTypeDef = TypedDict(
    "_RequiredListCertificatesByCARequestRequestTypeDef",
    {
        "caCertificateId": str,
    },
)
_OptionalListCertificatesByCARequestRequestTypeDef = TypedDict(
    "_OptionalListCertificatesByCARequestRequestTypeDef",
    {
        "pageSize": int,
        "marker": str,
        "ascendingOrder": bool,
    },
    total=False,
)

class ListCertificatesByCARequestRequestTypeDef(
    _RequiredListCertificatesByCARequestRequestTypeDef,
    _OptionalListCertificatesByCARequestRequestTypeDef,
):
    pass

ListCertificatesByCAResponseTypeDef = TypedDict(
    "ListCertificatesByCAResponseTypeDef",
    {
        "certificates": List["CertificateTypeDef"],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCertificatesRequestRequestTypeDef = TypedDict(
    "ListCertificatesRequestRequestTypeDef",
    {
        "pageSize": int,
        "marker": str,
        "ascendingOrder": bool,
    },
    total=False,
)

ListCertificatesResponseTypeDef = TypedDict(
    "ListCertificatesResponseTypeDef",
    {
        "certificates": List["CertificateTypeDef"],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomMetricsRequestRequestTypeDef = TypedDict(
    "ListCustomMetricsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListCustomMetricsResponseTypeDef = TypedDict(
    "ListCustomMetricsResponseTypeDef",
    {
        "metricNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDetectMitigationActionsExecutionsRequestRequestTypeDef = TypedDict(
    "ListDetectMitigationActionsExecutionsRequestRequestTypeDef",
    {
        "taskId": str,
        "violationId": str,
        "thingName": str,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListDetectMitigationActionsExecutionsResponseTypeDef = TypedDict(
    "ListDetectMitigationActionsExecutionsResponseTypeDef",
    {
        "actionsExecutions": List["DetectMitigationActionExecutionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDetectMitigationActionsTasksRequestRequestTypeDef = TypedDict(
    "_RequiredListDetectMitigationActionsTasksRequestRequestTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)
_OptionalListDetectMitigationActionsTasksRequestRequestTypeDef = TypedDict(
    "_OptionalListDetectMitigationActionsTasksRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListDetectMitigationActionsTasksRequestRequestTypeDef(
    _RequiredListDetectMitigationActionsTasksRequestRequestTypeDef,
    _OptionalListDetectMitigationActionsTasksRequestRequestTypeDef,
):
    pass

ListDetectMitigationActionsTasksResponseTypeDef = TypedDict(
    "ListDetectMitigationActionsTasksResponseTypeDef",
    {
        "tasks": List["DetectMitigationActionsTaskSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDimensionsRequestRequestTypeDef = TypedDict(
    "ListDimensionsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDimensionsResponseTypeDef = TypedDict(
    "ListDimensionsResponseTypeDef",
    {
        "dimensionNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDomainConfigurationsRequestRequestTypeDef = TypedDict(
    "ListDomainConfigurationsRequestRequestTypeDef",
    {
        "marker": str,
        "pageSize": int,
        "serviceType": ServiceTypeType,
    },
    total=False,
)

ListDomainConfigurationsResponseTypeDef = TypedDict(
    "ListDomainConfigurationsResponseTypeDef",
    {
        "domainConfigurations": List["DomainConfigurationSummaryTypeDef"],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIndicesRequestRequestTypeDef = TypedDict(
    "ListIndicesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListIndicesResponseTypeDef = TypedDict(
    "ListIndicesResponseTypeDef",
    {
        "indexNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListJobExecutionsForJobRequestRequestTypeDef = TypedDict(
    "_RequiredListJobExecutionsForJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)
_OptionalListJobExecutionsForJobRequestRequestTypeDef = TypedDict(
    "_OptionalListJobExecutionsForJobRequestRequestTypeDef",
    {
        "status": JobExecutionStatusType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListJobExecutionsForJobRequestRequestTypeDef(
    _RequiredListJobExecutionsForJobRequestRequestTypeDef,
    _OptionalListJobExecutionsForJobRequestRequestTypeDef,
):
    pass

ListJobExecutionsForJobResponseTypeDef = TypedDict(
    "ListJobExecutionsForJobResponseTypeDef",
    {
        "executionSummaries": List["JobExecutionSummaryForJobTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListJobExecutionsForThingRequestRequestTypeDef = TypedDict(
    "_RequiredListJobExecutionsForThingRequestRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalListJobExecutionsForThingRequestRequestTypeDef = TypedDict(
    "_OptionalListJobExecutionsForThingRequestRequestTypeDef",
    {
        "status": JobExecutionStatusType,
        "namespaceId": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListJobExecutionsForThingRequestRequestTypeDef(
    _RequiredListJobExecutionsForThingRequestRequestTypeDef,
    _OptionalListJobExecutionsForThingRequestRequestTypeDef,
):
    pass

ListJobExecutionsForThingResponseTypeDef = TypedDict(
    "ListJobExecutionsForThingResponseTypeDef",
    {
        "executionSummaries": List["JobExecutionSummaryForThingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobTemplatesRequestRequestTypeDef = TypedDict(
    "ListJobTemplatesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListJobTemplatesResponseTypeDef = TypedDict(
    "ListJobTemplatesResponseTypeDef",
    {
        "jobTemplates": List["JobTemplateSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "status": JobStatusType,
        "targetSelection": TargetSelectionType,
        "maxResults": int,
        "nextToken": str,
        "thingGroupName": str,
        "thingGroupId": str,
        "namespaceId": str,
    },
    total=False,
)

ListJobsResponseTypeDef = TypedDict(
    "ListJobsResponseTypeDef",
    {
        "jobs": List["JobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMitigationActionsRequestRequestTypeDef = TypedDict(
    "ListMitigationActionsRequestRequestTypeDef",
    {
        "actionType": MitigationActionTypeType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListMitigationActionsResponseTypeDef = TypedDict(
    "ListMitigationActionsResponseTypeDef",
    {
        "actionIdentifiers": List["MitigationActionIdentifierTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOTAUpdatesRequestRequestTypeDef = TypedDict(
    "ListOTAUpdatesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "otaUpdateStatus": OTAUpdateStatusType,
    },
    total=False,
)

ListOTAUpdatesResponseTypeDef = TypedDict(
    "ListOTAUpdatesResponseTypeDef",
    {
        "otaUpdates": List["OTAUpdateSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOutgoingCertificatesRequestRequestTypeDef = TypedDict(
    "ListOutgoingCertificatesRequestRequestTypeDef",
    {
        "pageSize": int,
        "marker": str,
        "ascendingOrder": bool,
    },
    total=False,
)

ListOutgoingCertificatesResponseTypeDef = TypedDict(
    "ListOutgoingCertificatesResponseTypeDef",
    {
        "outgoingCertificates": List["OutgoingCertificateTypeDef"],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPoliciesRequestRequestTypeDef = TypedDict(
    "ListPoliciesRequestRequestTypeDef",
    {
        "marker": str,
        "pageSize": int,
        "ascendingOrder": bool,
    },
    total=False,
)

ListPoliciesResponseTypeDef = TypedDict(
    "ListPoliciesResponseTypeDef",
    {
        "policies": List["PolicyTypeDef"],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPolicyPrincipalsRequestRequestTypeDef = TypedDict(
    "_RequiredListPolicyPrincipalsRequestRequestTypeDef",
    {
        "policyName": str,
    },
)
_OptionalListPolicyPrincipalsRequestRequestTypeDef = TypedDict(
    "_OptionalListPolicyPrincipalsRequestRequestTypeDef",
    {
        "marker": str,
        "pageSize": int,
        "ascendingOrder": bool,
    },
    total=False,
)

class ListPolicyPrincipalsRequestRequestTypeDef(
    _RequiredListPolicyPrincipalsRequestRequestTypeDef,
    _OptionalListPolicyPrincipalsRequestRequestTypeDef,
):
    pass

ListPolicyPrincipalsResponseTypeDef = TypedDict(
    "ListPolicyPrincipalsResponseTypeDef",
    {
        "principals": List[str],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPolicyVersionsRequestRequestTypeDef = TypedDict(
    "ListPolicyVersionsRequestRequestTypeDef",
    {
        "policyName": str,
    },
)

ListPolicyVersionsResponseTypeDef = TypedDict(
    "ListPolicyVersionsResponseTypeDef",
    {
        "policyVersions": List["PolicyVersionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPrincipalPoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredListPrincipalPoliciesRequestRequestTypeDef",
    {
        "principal": str,
    },
)
_OptionalListPrincipalPoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalListPrincipalPoliciesRequestRequestTypeDef",
    {
        "marker": str,
        "pageSize": int,
        "ascendingOrder": bool,
    },
    total=False,
)

class ListPrincipalPoliciesRequestRequestTypeDef(
    _RequiredListPrincipalPoliciesRequestRequestTypeDef,
    _OptionalListPrincipalPoliciesRequestRequestTypeDef,
):
    pass

ListPrincipalPoliciesResponseTypeDef = TypedDict(
    "ListPrincipalPoliciesResponseTypeDef",
    {
        "policies": List["PolicyTypeDef"],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPrincipalThingsRequestRequestTypeDef = TypedDict(
    "_RequiredListPrincipalThingsRequestRequestTypeDef",
    {
        "principal": str,
    },
)
_OptionalListPrincipalThingsRequestRequestTypeDef = TypedDict(
    "_OptionalListPrincipalThingsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListPrincipalThingsRequestRequestTypeDef(
    _RequiredListPrincipalThingsRequestRequestTypeDef,
    _OptionalListPrincipalThingsRequestRequestTypeDef,
):
    pass

ListPrincipalThingsResponseTypeDef = TypedDict(
    "ListPrincipalThingsResponseTypeDef",
    {
        "things": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProvisioningTemplateVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListProvisioningTemplateVersionsRequestRequestTypeDef",
    {
        "templateName": str,
    },
)
_OptionalListProvisioningTemplateVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListProvisioningTemplateVersionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListProvisioningTemplateVersionsRequestRequestTypeDef(
    _RequiredListProvisioningTemplateVersionsRequestRequestTypeDef,
    _OptionalListProvisioningTemplateVersionsRequestRequestTypeDef,
):
    pass

ListProvisioningTemplateVersionsResponseTypeDef = TypedDict(
    "ListProvisioningTemplateVersionsResponseTypeDef",
    {
        "versions": List["ProvisioningTemplateVersionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProvisioningTemplatesRequestRequestTypeDef = TypedDict(
    "ListProvisioningTemplatesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListProvisioningTemplatesResponseTypeDef = TypedDict(
    "ListProvisioningTemplatesResponseTypeDef",
    {
        "templates": List["ProvisioningTemplateSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRoleAliasesRequestRequestTypeDef = TypedDict(
    "ListRoleAliasesRequestRequestTypeDef",
    {
        "pageSize": int,
        "marker": str,
        "ascendingOrder": bool,
    },
    total=False,
)

ListRoleAliasesResponseTypeDef = TypedDict(
    "ListRoleAliasesResponseTypeDef",
    {
        "roleAliases": List[str],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListScheduledAuditsRequestRequestTypeDef = TypedDict(
    "ListScheduledAuditsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListScheduledAuditsResponseTypeDef = TypedDict(
    "ListScheduledAuditsResponseTypeDef",
    {
        "scheduledAudits": List["ScheduledAuditMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSecurityProfilesForTargetRequestRequestTypeDef = TypedDict(
    "_RequiredListSecurityProfilesForTargetRequestRequestTypeDef",
    {
        "securityProfileTargetArn": str,
    },
)
_OptionalListSecurityProfilesForTargetRequestRequestTypeDef = TypedDict(
    "_OptionalListSecurityProfilesForTargetRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "recursive": bool,
    },
    total=False,
)

class ListSecurityProfilesForTargetRequestRequestTypeDef(
    _RequiredListSecurityProfilesForTargetRequestRequestTypeDef,
    _OptionalListSecurityProfilesForTargetRequestRequestTypeDef,
):
    pass

ListSecurityProfilesForTargetResponseTypeDef = TypedDict(
    "ListSecurityProfilesForTargetResponseTypeDef",
    {
        "securityProfileTargetMappings": List["SecurityProfileTargetMappingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSecurityProfilesRequestRequestTypeDef = TypedDict(
    "ListSecurityProfilesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "dimensionName": str,
        "metricName": str,
    },
    total=False,
)

ListSecurityProfilesResponseTypeDef = TypedDict(
    "ListSecurityProfilesResponseTypeDef",
    {
        "securityProfileIdentifiers": List["SecurityProfileIdentifierTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamsRequestRequestTypeDef = TypedDict(
    "ListStreamsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "ascendingOrder": bool,
    },
    total=False,
)

ListStreamsResponseTypeDef = TypedDict(
    "ListStreamsResponseTypeDef",
    {
        "streams": List["StreamSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "nextToken": str,
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
        "tags": List["TagTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTargetsForPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredListTargetsForPolicyRequestRequestTypeDef",
    {
        "policyName": str,
    },
)
_OptionalListTargetsForPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalListTargetsForPolicyRequestRequestTypeDef",
    {
        "marker": str,
        "pageSize": int,
    },
    total=False,
)

class ListTargetsForPolicyRequestRequestTypeDef(
    _RequiredListTargetsForPolicyRequestRequestTypeDef,
    _OptionalListTargetsForPolicyRequestRequestTypeDef,
):
    pass

ListTargetsForPolicyResponseTypeDef = TypedDict(
    "ListTargetsForPolicyResponseTypeDef",
    {
        "targets": List[str],
        "nextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTargetsForSecurityProfileRequestRequestTypeDef = TypedDict(
    "_RequiredListTargetsForSecurityProfileRequestRequestTypeDef",
    {
        "securityProfileName": str,
    },
)
_OptionalListTargetsForSecurityProfileRequestRequestTypeDef = TypedDict(
    "_OptionalListTargetsForSecurityProfileRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListTargetsForSecurityProfileRequestRequestTypeDef(
    _RequiredListTargetsForSecurityProfileRequestRequestTypeDef,
    _OptionalListTargetsForSecurityProfileRequestRequestTypeDef,
):
    pass

ListTargetsForSecurityProfileResponseTypeDef = TypedDict(
    "ListTargetsForSecurityProfileResponseTypeDef",
    {
        "securityProfileTargets": List["SecurityProfileTargetTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThingGroupsForThingRequestRequestTypeDef = TypedDict(
    "_RequiredListThingGroupsForThingRequestRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalListThingGroupsForThingRequestRequestTypeDef = TypedDict(
    "_OptionalListThingGroupsForThingRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListThingGroupsForThingRequestRequestTypeDef(
    _RequiredListThingGroupsForThingRequestRequestTypeDef,
    _OptionalListThingGroupsForThingRequestRequestTypeDef,
):
    pass

ListThingGroupsForThingResponseTypeDef = TypedDict(
    "ListThingGroupsForThingResponseTypeDef",
    {
        "thingGroups": List["GroupNameAndArnTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListThingGroupsRequestRequestTypeDef = TypedDict(
    "ListThingGroupsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "parentGroup": str,
        "namePrefixFilter": str,
        "recursive": bool,
    },
    total=False,
)

ListThingGroupsResponseTypeDef = TypedDict(
    "ListThingGroupsResponseTypeDef",
    {
        "thingGroups": List["GroupNameAndArnTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThingPrincipalsRequestRequestTypeDef = TypedDict(
    "_RequiredListThingPrincipalsRequestRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalListThingPrincipalsRequestRequestTypeDef = TypedDict(
    "_OptionalListThingPrincipalsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListThingPrincipalsRequestRequestTypeDef(
    _RequiredListThingPrincipalsRequestRequestTypeDef,
    _OptionalListThingPrincipalsRequestRequestTypeDef,
):
    pass

ListThingPrincipalsResponseTypeDef = TypedDict(
    "ListThingPrincipalsResponseTypeDef",
    {
        "principals": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThingRegistrationTaskReportsRequestRequestTypeDef = TypedDict(
    "_RequiredListThingRegistrationTaskReportsRequestRequestTypeDef",
    {
        "taskId": str,
        "reportType": ReportTypeType,
    },
)
_OptionalListThingRegistrationTaskReportsRequestRequestTypeDef = TypedDict(
    "_OptionalListThingRegistrationTaskReportsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListThingRegistrationTaskReportsRequestRequestTypeDef(
    _RequiredListThingRegistrationTaskReportsRequestRequestTypeDef,
    _OptionalListThingRegistrationTaskReportsRequestRequestTypeDef,
):
    pass

ListThingRegistrationTaskReportsResponseTypeDef = TypedDict(
    "ListThingRegistrationTaskReportsResponseTypeDef",
    {
        "resourceLinks": List[str],
        "reportType": ReportTypeType,
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListThingRegistrationTasksRequestRequestTypeDef = TypedDict(
    "ListThingRegistrationTasksRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "status": StatusType,
    },
    total=False,
)

ListThingRegistrationTasksResponseTypeDef = TypedDict(
    "ListThingRegistrationTasksResponseTypeDef",
    {
        "taskIds": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListThingTypesRequestRequestTypeDef = TypedDict(
    "ListThingTypesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "thingTypeName": str,
    },
    total=False,
)

ListThingTypesResponseTypeDef = TypedDict(
    "ListThingTypesResponseTypeDef",
    {
        "thingTypes": List["ThingTypeDefinitionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThingsInBillingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredListThingsInBillingGroupRequestRequestTypeDef",
    {
        "billingGroupName": str,
    },
)
_OptionalListThingsInBillingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalListThingsInBillingGroupRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListThingsInBillingGroupRequestRequestTypeDef(
    _RequiredListThingsInBillingGroupRequestRequestTypeDef,
    _OptionalListThingsInBillingGroupRequestRequestTypeDef,
):
    pass

ListThingsInBillingGroupResponseTypeDef = TypedDict(
    "ListThingsInBillingGroupResponseTypeDef",
    {
        "things": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThingsInThingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredListThingsInThingGroupRequestRequestTypeDef",
    {
        "thingGroupName": str,
    },
)
_OptionalListThingsInThingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalListThingsInThingGroupRequestRequestTypeDef",
    {
        "recursive": bool,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListThingsInThingGroupRequestRequestTypeDef(
    _RequiredListThingsInThingGroupRequestRequestTypeDef,
    _OptionalListThingsInThingGroupRequestRequestTypeDef,
):
    pass

ListThingsInThingGroupResponseTypeDef = TypedDict(
    "ListThingsInThingGroupResponseTypeDef",
    {
        "things": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListThingsRequestRequestTypeDef = TypedDict(
    "ListThingsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "attributeName": str,
        "attributeValue": str,
        "thingTypeName": str,
        "usePrefixAttributeValue": bool,
    },
    total=False,
)

ListThingsResponseTypeDef = TypedDict(
    "ListThingsResponseTypeDef",
    {
        "things": List["ThingAttributeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTopicRuleDestinationsRequestRequestTypeDef = TypedDict(
    "ListTopicRuleDestinationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListTopicRuleDestinationsResponseTypeDef = TypedDict(
    "ListTopicRuleDestinationsResponseTypeDef",
    {
        "destinationSummaries": List["TopicRuleDestinationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTopicRulesRequestRequestTypeDef = TypedDict(
    "ListTopicRulesRequestRequestTypeDef",
    {
        "topic": str,
        "maxResults": int,
        "nextToken": str,
        "ruleDisabled": bool,
    },
    total=False,
)

ListTopicRulesResponseTypeDef = TypedDict(
    "ListTopicRulesResponseTypeDef",
    {
        "rules": List["TopicRuleListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListV2LoggingLevelsRequestRequestTypeDef = TypedDict(
    "ListV2LoggingLevelsRequestRequestTypeDef",
    {
        "targetType": LogTargetTypeType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListV2LoggingLevelsResponseTypeDef = TypedDict(
    "ListV2LoggingLevelsResponseTypeDef",
    {
        "logTargetConfigurations": List["LogTargetConfigurationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListViolationEventsRequestRequestTypeDef = TypedDict(
    "_RequiredListViolationEventsRequestRequestTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)
_OptionalListViolationEventsRequestRequestTypeDef = TypedDict(
    "_OptionalListViolationEventsRequestRequestTypeDef",
    {
        "thingName": str,
        "securityProfileName": str,
        "behaviorCriteriaType": BehaviorCriteriaTypeType,
        "listSuppressedAlerts": bool,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListViolationEventsRequestRequestTypeDef(
    _RequiredListViolationEventsRequestRequestTypeDef,
    _OptionalListViolationEventsRequestRequestTypeDef,
):
    pass

ListViolationEventsResponseTypeDef = TypedDict(
    "ListViolationEventsResponseTypeDef",
    {
        "violationEvents": List["ViolationEventTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogTargetConfigurationTypeDef = TypedDict(
    "LogTargetConfigurationTypeDef",
    {
        "logTarget": "LogTargetTypeDef",
        "logLevel": LogLevelType,
    },
    total=False,
)

_RequiredLogTargetTypeDef = TypedDict(
    "_RequiredLogTargetTypeDef",
    {
        "targetType": LogTargetTypeType,
    },
)
_OptionalLogTargetTypeDef = TypedDict(
    "_OptionalLogTargetTypeDef",
    {
        "targetName": str,
    },
    total=False,
)

class LogTargetTypeDef(_RequiredLogTargetTypeDef, _OptionalLogTargetTypeDef):
    pass

_RequiredLoggingOptionsPayloadTypeDef = TypedDict(
    "_RequiredLoggingOptionsPayloadTypeDef",
    {
        "roleArn": str,
    },
)
_OptionalLoggingOptionsPayloadTypeDef = TypedDict(
    "_OptionalLoggingOptionsPayloadTypeDef",
    {
        "logLevel": LogLevelType,
    },
    total=False,
)

class LoggingOptionsPayloadTypeDef(
    _RequiredLoggingOptionsPayloadTypeDef, _OptionalLoggingOptionsPayloadTypeDef
):
    pass

MachineLearningDetectionConfigTypeDef = TypedDict(
    "MachineLearningDetectionConfigTypeDef",
    {
        "confidenceLevel": ConfidenceLevelType,
    },
)

_RequiredMetricDimensionTypeDef = TypedDict(
    "_RequiredMetricDimensionTypeDef",
    {
        "dimensionName": str,
    },
)
_OptionalMetricDimensionTypeDef = TypedDict(
    "_OptionalMetricDimensionTypeDef",
    {
        "operator": DimensionValueOperatorType,
    },
    total=False,
)

class MetricDimensionTypeDef(_RequiredMetricDimensionTypeDef, _OptionalMetricDimensionTypeDef):
    pass

_RequiredMetricToRetainTypeDef = TypedDict(
    "_RequiredMetricToRetainTypeDef",
    {
        "metric": str,
    },
)
_OptionalMetricToRetainTypeDef = TypedDict(
    "_OptionalMetricToRetainTypeDef",
    {
        "metricDimension": "MetricDimensionTypeDef",
    },
    total=False,
)

class MetricToRetainTypeDef(_RequiredMetricToRetainTypeDef, _OptionalMetricToRetainTypeDef):
    pass

MetricValueTypeDef = TypedDict(
    "MetricValueTypeDef",
    {
        "count": int,
        "cidrs": List[str],
        "ports": List[int],
        "number": float,
        "numbers": List[float],
        "strings": List[str],
    },
    total=False,
)

MitigationActionIdentifierTypeDef = TypedDict(
    "MitigationActionIdentifierTypeDef",
    {
        "actionName": str,
        "actionArn": str,
        "creationDate": datetime,
    },
    total=False,
)

MitigationActionParamsTypeDef = TypedDict(
    "MitigationActionParamsTypeDef",
    {
        "updateDeviceCertificateParams": "UpdateDeviceCertificateParamsTypeDef",
        "updateCACertificateParams": "UpdateCACertificateParamsTypeDef",
        "addThingsToThingGroupParams": "AddThingsToThingGroupParamsTypeDef",
        "replaceDefaultPolicyVersionParams": "ReplaceDefaultPolicyVersionParamsTypeDef",
        "enableIoTLoggingParams": "EnableIoTLoggingParamsTypeDef",
        "publishFindingToSnsParams": "PublishFindingToSnsParamsTypeDef",
    },
    total=False,
)

MitigationActionTypeDef = TypedDict(
    "MitigationActionTypeDef",
    {
        "name": str,
        "id": str,
        "roleArn": str,
        "actionParams": "MitigationActionParamsTypeDef",
    },
    total=False,
)

MqttContextTypeDef = TypedDict(
    "MqttContextTypeDef",
    {
        "username": str,
        "password": Union[bytes, IO[bytes], StreamingBody],
        "clientId": str,
    },
    total=False,
)

NonCompliantResourceTypeDef = TypedDict(
    "NonCompliantResourceTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceIdentifier": "ResourceIdentifierTypeDef",
        "additionalInfo": Dict[str, str],
    },
    total=False,
)

OTAUpdateFileTypeDef = TypedDict(
    "OTAUpdateFileTypeDef",
    {
        "fileName": str,
        "fileType": int,
        "fileVersion": str,
        "fileLocation": "FileLocationTypeDef",
        "codeSigning": "CodeSigningTypeDef",
        "attributes": Dict[str, str],
    },
    total=False,
)

OTAUpdateInfoTypeDef = TypedDict(
    "OTAUpdateInfoTypeDef",
    {
        "otaUpdateId": str,
        "otaUpdateArn": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "description": str,
        "targets": List[str],
        "protocols": List[ProtocolType],
        "awsJobExecutionsRolloutConfig": "AwsJobExecutionsRolloutConfigTypeDef",
        "awsJobPresignedUrlConfig": "AwsJobPresignedUrlConfigTypeDef",
        "targetSelection": TargetSelectionType,
        "otaUpdateFiles": List["OTAUpdateFileTypeDef"],
        "otaUpdateStatus": OTAUpdateStatusType,
        "awsIotJobId": str,
        "awsIotJobArn": str,
        "errorInfo": "ErrorInfoTypeDef",
        "additionalParameters": Dict[str, str],
    },
    total=False,
)

OTAUpdateSummaryTypeDef = TypedDict(
    "OTAUpdateSummaryTypeDef",
    {
        "otaUpdateId": str,
        "otaUpdateArn": str,
        "creationDate": datetime,
    },
    total=False,
)

OutgoingCertificateTypeDef = TypedDict(
    "OutgoingCertificateTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "transferredTo": str,
        "transferDate": datetime,
        "transferMessage": str,
        "creationDate": datetime,
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

PercentPairTypeDef = TypedDict(
    "PercentPairTypeDef",
    {
        "percent": float,
        "value": float,
    },
    total=False,
)

PolicyTypeDef = TypedDict(
    "PolicyTypeDef",
    {
        "policyName": str,
        "policyArn": str,
    },
    total=False,
)

PolicyVersionIdentifierTypeDef = TypedDict(
    "PolicyVersionIdentifierTypeDef",
    {
        "policyName": str,
        "policyVersionId": str,
    },
    total=False,
)

PolicyVersionTypeDef = TypedDict(
    "PolicyVersionTypeDef",
    {
        "versionId": str,
        "isDefaultVersion": bool,
        "createDate": datetime,
    },
    total=False,
)

PresignedUrlConfigTypeDef = TypedDict(
    "PresignedUrlConfigTypeDef",
    {
        "roleArn": str,
        "expiresInSec": int,
    },
    total=False,
)

_RequiredProvisioningHookTypeDef = TypedDict(
    "_RequiredProvisioningHookTypeDef",
    {
        "targetArn": str,
    },
)
_OptionalProvisioningHookTypeDef = TypedDict(
    "_OptionalProvisioningHookTypeDef",
    {
        "payloadVersion": str,
    },
    total=False,
)

class ProvisioningHookTypeDef(_RequiredProvisioningHookTypeDef, _OptionalProvisioningHookTypeDef):
    pass

ProvisioningTemplateSummaryTypeDef = TypedDict(
    "ProvisioningTemplateSummaryTypeDef",
    {
        "templateArn": str,
        "templateName": str,
        "description": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "enabled": bool,
    },
    total=False,
)

ProvisioningTemplateVersionSummaryTypeDef = TypedDict(
    "ProvisioningTemplateVersionSummaryTypeDef",
    {
        "versionId": int,
        "creationDate": datetime,
        "isDefaultVersion": bool,
    },
    total=False,
)

PublishFindingToSnsParamsTypeDef = TypedDict(
    "PublishFindingToSnsParamsTypeDef",
    {
        "topicArn": str,
    },
)

_RequiredPutAssetPropertyValueEntryTypeDef = TypedDict(
    "_RequiredPutAssetPropertyValueEntryTypeDef",
    {
        "propertyValues": List["AssetPropertyValueTypeDef"],
    },
)
_OptionalPutAssetPropertyValueEntryTypeDef = TypedDict(
    "_OptionalPutAssetPropertyValueEntryTypeDef",
    {
        "entryId": str,
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
    },
    total=False,
)

class PutAssetPropertyValueEntryTypeDef(
    _RequiredPutAssetPropertyValueEntryTypeDef, _OptionalPutAssetPropertyValueEntryTypeDef
):
    pass

PutItemInputTypeDef = TypedDict(
    "PutItemInputTypeDef",
    {
        "tableName": str,
    },
)

RateIncreaseCriteriaTypeDef = TypedDict(
    "RateIncreaseCriteriaTypeDef",
    {
        "numberOfNotifiedThings": int,
        "numberOfSucceededThings": int,
    },
    total=False,
)

_RequiredRegisterCACertificateRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterCACertificateRequestRequestTypeDef",
    {
        "caCertificate": str,
        "verificationCertificate": str,
    },
)
_OptionalRegisterCACertificateRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterCACertificateRequestRequestTypeDef",
    {
        "setAsActive": bool,
        "allowAutoRegistration": bool,
        "registrationConfig": "RegistrationConfigTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class RegisterCACertificateRequestRequestTypeDef(
    _RequiredRegisterCACertificateRequestRequestTypeDef,
    _OptionalRegisterCACertificateRequestRequestTypeDef,
):
    pass

RegisterCACertificateResponseTypeDef = TypedDict(
    "RegisterCACertificateResponseTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterCertificateRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterCertificateRequestRequestTypeDef",
    {
        "certificatePem": str,
    },
)
_OptionalRegisterCertificateRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterCertificateRequestRequestTypeDef",
    {
        "caCertificatePem": str,
        "setAsActive": bool,
        "status": CertificateStatusType,
    },
    total=False,
)

class RegisterCertificateRequestRequestTypeDef(
    _RequiredRegisterCertificateRequestRequestTypeDef,
    _OptionalRegisterCertificateRequestRequestTypeDef,
):
    pass

RegisterCertificateResponseTypeDef = TypedDict(
    "RegisterCertificateResponseTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterCertificateWithoutCARequestRequestTypeDef = TypedDict(
    "_RequiredRegisterCertificateWithoutCARequestRequestTypeDef",
    {
        "certificatePem": str,
    },
)
_OptionalRegisterCertificateWithoutCARequestRequestTypeDef = TypedDict(
    "_OptionalRegisterCertificateWithoutCARequestRequestTypeDef",
    {
        "status": CertificateStatusType,
    },
    total=False,
)

class RegisterCertificateWithoutCARequestRequestTypeDef(
    _RequiredRegisterCertificateWithoutCARequestRequestTypeDef,
    _OptionalRegisterCertificateWithoutCARequestRequestTypeDef,
):
    pass

RegisterCertificateWithoutCAResponseTypeDef = TypedDict(
    "RegisterCertificateWithoutCAResponseTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterThingRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterThingRequestRequestTypeDef",
    {
        "templateBody": str,
    },
)
_OptionalRegisterThingRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterThingRequestRequestTypeDef",
    {
        "parameters": Dict[str, str],
    },
    total=False,
)

class RegisterThingRequestRequestTypeDef(
    _RequiredRegisterThingRequestRequestTypeDef, _OptionalRegisterThingRequestRequestTypeDef
):
    pass

RegisterThingResponseTypeDef = TypedDict(
    "RegisterThingResponseTypeDef",
    {
        "certificatePem": str,
        "resourceArns": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegistrationConfigTypeDef = TypedDict(
    "RegistrationConfigTypeDef",
    {
        "templateBody": str,
        "roleArn": str,
    },
    total=False,
)

_RequiredRejectCertificateTransferRequestRequestTypeDef = TypedDict(
    "_RequiredRejectCertificateTransferRequestRequestTypeDef",
    {
        "certificateId": str,
    },
)
_OptionalRejectCertificateTransferRequestRequestTypeDef = TypedDict(
    "_OptionalRejectCertificateTransferRequestRequestTypeDef",
    {
        "rejectReason": str,
    },
    total=False,
)

class RejectCertificateTransferRequestRequestTypeDef(
    _RequiredRejectCertificateTransferRequestRequestTypeDef,
    _OptionalRejectCertificateTransferRequestRequestTypeDef,
):
    pass

RelatedResourceTypeDef = TypedDict(
    "RelatedResourceTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceIdentifier": "ResourceIdentifierTypeDef",
        "additionalInfo": Dict[str, str],
    },
    total=False,
)

RemoveThingFromBillingGroupRequestRequestTypeDef = TypedDict(
    "RemoveThingFromBillingGroupRequestRequestTypeDef",
    {
        "billingGroupName": str,
        "billingGroupArn": str,
        "thingName": str,
        "thingArn": str,
    },
    total=False,
)

RemoveThingFromThingGroupRequestRequestTypeDef = TypedDict(
    "RemoveThingFromThingGroupRequestRequestTypeDef",
    {
        "thingGroupName": str,
        "thingGroupArn": str,
        "thingName": str,
        "thingArn": str,
    },
    total=False,
)

ReplaceDefaultPolicyVersionParamsTypeDef = TypedDict(
    "ReplaceDefaultPolicyVersionParamsTypeDef",
    {
        "templateName": Literal["BLANK_POLICY"],
    },
)

ReplaceTopicRuleRequestRequestTypeDef = TypedDict(
    "ReplaceTopicRuleRequestRequestTypeDef",
    {
        "ruleName": str,
        "topicRulePayload": "TopicRulePayloadTypeDef",
    },
)

_RequiredRepublishActionTypeDef = TypedDict(
    "_RequiredRepublishActionTypeDef",
    {
        "roleArn": str,
        "topic": str,
    },
)
_OptionalRepublishActionTypeDef = TypedDict(
    "_OptionalRepublishActionTypeDef",
    {
        "qos": int,
    },
    total=False,
)

class RepublishActionTypeDef(_RequiredRepublishActionTypeDef, _OptionalRepublishActionTypeDef):
    pass

ResourceIdentifierTypeDef = TypedDict(
    "ResourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": "PolicyVersionIdentifierTypeDef",
        "account": str,
        "iamRoleArn": str,
        "roleAliasArn": str,
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

RoleAliasDescriptionTypeDef = TypedDict(
    "RoleAliasDescriptionTypeDef",
    {
        "roleAlias": str,
        "roleAliasArn": str,
        "roleArn": str,
        "owner": str,
        "credentialDurationSeconds": int,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)

_RequiredS3ActionTypeDef = TypedDict(
    "_RequiredS3ActionTypeDef",
    {
        "roleArn": str,
        "bucketName": str,
        "key": str,
    },
)
_OptionalS3ActionTypeDef = TypedDict(
    "_OptionalS3ActionTypeDef",
    {
        "cannedAcl": CannedAccessControlListType,
    },
    total=False,
)

class S3ActionTypeDef(_RequiredS3ActionTypeDef, _OptionalS3ActionTypeDef):
    pass

S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "bucket": str,
        "prefix": str,
    },
    total=False,
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "version": str,
    },
    total=False,
)

SalesforceActionTypeDef = TypedDict(
    "SalesforceActionTypeDef",
    {
        "token": str,
        "url": str,
    },
)

ScheduledAuditMetadataTypeDef = TypedDict(
    "ScheduledAuditMetadataTypeDef",
    {
        "scheduledAuditName": str,
        "scheduledAuditArn": str,
        "frequency": AuditFrequencyType,
        "dayOfMonth": str,
        "dayOfWeek": DayOfWeekType,
    },
    total=False,
)

_RequiredSearchIndexRequestRequestTypeDef = TypedDict(
    "_RequiredSearchIndexRequestRequestTypeDef",
    {
        "queryString": str,
    },
)
_OptionalSearchIndexRequestRequestTypeDef = TypedDict(
    "_OptionalSearchIndexRequestRequestTypeDef",
    {
        "indexName": str,
        "nextToken": str,
        "maxResults": int,
        "queryVersion": str,
    },
    total=False,
)

class SearchIndexRequestRequestTypeDef(
    _RequiredSearchIndexRequestRequestTypeDef, _OptionalSearchIndexRequestRequestTypeDef
):
    pass

SearchIndexResponseTypeDef = TypedDict(
    "SearchIndexResponseTypeDef",
    {
        "nextToken": str,
        "things": List["ThingDocumentTypeDef"],
        "thingGroups": List["ThingGroupDocumentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SecurityProfileIdentifierTypeDef = TypedDict(
    "SecurityProfileIdentifierTypeDef",
    {
        "name": str,
        "arn": str,
    },
)

SecurityProfileTargetMappingTypeDef = TypedDict(
    "SecurityProfileTargetMappingTypeDef",
    {
        "securityProfileIdentifier": "SecurityProfileIdentifierTypeDef",
        "target": "SecurityProfileTargetTypeDef",
    },
    total=False,
)

SecurityProfileTargetTypeDef = TypedDict(
    "SecurityProfileTargetTypeDef",
    {
        "arn": str,
    },
)

ServerCertificateSummaryTypeDef = TypedDict(
    "ServerCertificateSummaryTypeDef",
    {
        "serverCertificateArn": str,
        "serverCertificateStatus": ServerCertificateStatusType,
        "serverCertificateStatusDetail": str,
    },
    total=False,
)

SetDefaultAuthorizerRequestRequestTypeDef = TypedDict(
    "SetDefaultAuthorizerRequestRequestTypeDef",
    {
        "authorizerName": str,
    },
)

SetDefaultAuthorizerResponseTypeDef = TypedDict(
    "SetDefaultAuthorizerResponseTypeDef",
    {
        "authorizerName": str,
        "authorizerArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetDefaultPolicyVersionRequestRequestTypeDef = TypedDict(
    "SetDefaultPolicyVersionRequestRequestTypeDef",
    {
        "policyName": str,
        "policyVersionId": str,
    },
)

SetLoggingOptionsRequestRequestTypeDef = TypedDict(
    "SetLoggingOptionsRequestRequestTypeDef",
    {
        "loggingOptionsPayload": "LoggingOptionsPayloadTypeDef",
    },
)

SetV2LoggingLevelRequestRequestTypeDef = TypedDict(
    "SetV2LoggingLevelRequestRequestTypeDef",
    {
        "logTarget": "LogTargetTypeDef",
        "logLevel": LogLevelType,
    },
)

SetV2LoggingOptionsRequestRequestTypeDef = TypedDict(
    "SetV2LoggingOptionsRequestRequestTypeDef",
    {
        "roleArn": str,
        "defaultLogLevel": LogLevelType,
        "disableAllLogs": bool,
    },
    total=False,
)

SigV4AuthorizationTypeDef = TypedDict(
    "SigV4AuthorizationTypeDef",
    {
        "signingRegion": str,
        "serviceName": str,
        "roleArn": str,
    },
)

SigningProfileParameterTypeDef = TypedDict(
    "SigningProfileParameterTypeDef",
    {
        "certificateArn": str,
        "platform": str,
        "certificatePathOnDevice": str,
    },
    total=False,
)

_RequiredSnsActionTypeDef = TypedDict(
    "_RequiredSnsActionTypeDef",
    {
        "targetArn": str,
        "roleArn": str,
    },
)
_OptionalSnsActionTypeDef = TypedDict(
    "_OptionalSnsActionTypeDef",
    {
        "messageFormat": MessageFormatType,
    },
    total=False,
)

class SnsActionTypeDef(_RequiredSnsActionTypeDef, _OptionalSnsActionTypeDef):
    pass

_RequiredSqsActionTypeDef = TypedDict(
    "_RequiredSqsActionTypeDef",
    {
        "roleArn": str,
        "queueUrl": str,
    },
)
_OptionalSqsActionTypeDef = TypedDict(
    "_OptionalSqsActionTypeDef",
    {
        "useBase64": bool,
    },
    total=False,
)

class SqsActionTypeDef(_RequiredSqsActionTypeDef, _OptionalSqsActionTypeDef):
    pass

StartAuditMitigationActionsTaskRequestRequestTypeDef = TypedDict(
    "StartAuditMitigationActionsTaskRequestRequestTypeDef",
    {
        "taskId": str,
        "target": "AuditMitigationActionsTaskTargetTypeDef",
        "auditCheckToActionsMapping": Dict[str, List[str]],
        "clientRequestToken": str,
    },
)

StartAuditMitigationActionsTaskResponseTypeDef = TypedDict(
    "StartAuditMitigationActionsTaskResponseTypeDef",
    {
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartDetectMitigationActionsTaskRequestRequestTypeDef = TypedDict(
    "_RequiredStartDetectMitigationActionsTaskRequestRequestTypeDef",
    {
        "taskId": str,
        "target": "DetectMitigationActionsTaskTargetTypeDef",
        "actions": List[str],
        "clientRequestToken": str,
    },
)
_OptionalStartDetectMitigationActionsTaskRequestRequestTypeDef = TypedDict(
    "_OptionalStartDetectMitigationActionsTaskRequestRequestTypeDef",
    {
        "violationEventOccurrenceRange": "ViolationEventOccurrenceRangeTypeDef",
        "includeOnlyActiveViolations": bool,
        "includeSuppressedAlerts": bool,
    },
    total=False,
)

class StartDetectMitigationActionsTaskRequestRequestTypeDef(
    _RequiredStartDetectMitigationActionsTaskRequestRequestTypeDef,
    _OptionalStartDetectMitigationActionsTaskRequestRequestTypeDef,
):
    pass

StartDetectMitigationActionsTaskResponseTypeDef = TypedDict(
    "StartDetectMitigationActionsTaskResponseTypeDef",
    {
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartOnDemandAuditTaskRequestRequestTypeDef = TypedDict(
    "StartOnDemandAuditTaskRequestRequestTypeDef",
    {
        "targetCheckNames": List[str],
    },
)

StartOnDemandAuditTaskResponseTypeDef = TypedDict(
    "StartOnDemandAuditTaskResponseTypeDef",
    {
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartSigningJobParameterTypeDef = TypedDict(
    "StartSigningJobParameterTypeDef",
    {
        "signingProfileParameter": "SigningProfileParameterTypeDef",
        "signingProfileName": str,
        "destination": "DestinationTypeDef",
    },
    total=False,
)

StartThingRegistrationTaskRequestRequestTypeDef = TypedDict(
    "StartThingRegistrationTaskRequestRequestTypeDef",
    {
        "templateBody": str,
        "inputFileBucket": str,
        "inputFileKey": str,
        "roleArn": str,
    },
)

StartThingRegistrationTaskResponseTypeDef = TypedDict(
    "StartThingRegistrationTaskResponseTypeDef",
    {
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StatisticalThresholdTypeDef = TypedDict(
    "StatisticalThresholdTypeDef",
    {
        "statistic": str,
    },
    total=False,
)

StatisticsTypeDef = TypedDict(
    "StatisticsTypeDef",
    {
        "count": int,
        "average": float,
        "sum": float,
        "minimum": float,
        "maximum": float,
        "sumOfSquares": float,
        "variance": float,
        "stdDeviation": float,
    },
    total=False,
)

_RequiredStepFunctionsActionTypeDef = TypedDict(
    "_RequiredStepFunctionsActionTypeDef",
    {
        "stateMachineName": str,
        "roleArn": str,
    },
)
_OptionalStepFunctionsActionTypeDef = TypedDict(
    "_OptionalStepFunctionsActionTypeDef",
    {
        "executionNamePrefix": str,
    },
    total=False,
)

class StepFunctionsActionTypeDef(
    _RequiredStepFunctionsActionTypeDef, _OptionalStepFunctionsActionTypeDef
):
    pass

StopThingRegistrationTaskRequestRequestTypeDef = TypedDict(
    "StopThingRegistrationTaskRequestRequestTypeDef",
    {
        "taskId": str,
    },
)

StreamFileTypeDef = TypedDict(
    "StreamFileTypeDef",
    {
        "fileId": int,
        "s3Location": "S3LocationTypeDef",
    },
    total=False,
)

StreamInfoTypeDef = TypedDict(
    "StreamInfoTypeDef",
    {
        "streamId": str,
        "streamArn": str,
        "streamVersion": int,
        "description": str,
        "files": List["StreamFileTypeDef"],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "roleArn": str,
    },
    total=False,
)

StreamSummaryTypeDef = TypedDict(
    "StreamSummaryTypeDef",
    {
        "streamId": str,
        "streamArn": str,
        "streamVersion": int,
        "description": str,
    },
    total=False,
)

StreamTypeDef = TypedDict(
    "StreamTypeDef",
    {
        "streamId": str,
        "fileId": int,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass

TaskStatisticsForAuditCheckTypeDef = TypedDict(
    "TaskStatisticsForAuditCheckTypeDef",
    {
        "totalFindingsCount": int,
        "failedFindingsCount": int,
        "succeededFindingsCount": int,
        "skippedFindingsCount": int,
        "canceledFindingsCount": int,
    },
    total=False,
)

TaskStatisticsTypeDef = TypedDict(
    "TaskStatisticsTypeDef",
    {
        "totalChecks": int,
        "inProgressChecks": int,
        "waitingForDataCollectionChecks": int,
        "compliantChecks": int,
        "nonCompliantChecks": int,
        "failedChecks": int,
        "canceledChecks": int,
    },
    total=False,
)

_RequiredTestAuthorizationRequestRequestTypeDef = TypedDict(
    "_RequiredTestAuthorizationRequestRequestTypeDef",
    {
        "authInfos": List["AuthInfoTypeDef"],
    },
)
_OptionalTestAuthorizationRequestRequestTypeDef = TypedDict(
    "_OptionalTestAuthorizationRequestRequestTypeDef",
    {
        "principal": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyNamesToAdd": List[str],
        "policyNamesToSkip": List[str],
    },
    total=False,
)

class TestAuthorizationRequestRequestTypeDef(
    _RequiredTestAuthorizationRequestRequestTypeDef, _OptionalTestAuthorizationRequestRequestTypeDef
):
    pass

TestAuthorizationResponseTypeDef = TypedDict(
    "TestAuthorizationResponseTypeDef",
    {
        "authResults": List["AuthResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredTestInvokeAuthorizerRequestRequestTypeDef = TypedDict(
    "_RequiredTestInvokeAuthorizerRequestRequestTypeDef",
    {
        "authorizerName": str,
    },
)
_OptionalTestInvokeAuthorizerRequestRequestTypeDef = TypedDict(
    "_OptionalTestInvokeAuthorizerRequestRequestTypeDef",
    {
        "token": str,
        "tokenSignature": str,
        "httpContext": "HttpContextTypeDef",
        "mqttContext": "MqttContextTypeDef",
        "tlsContext": "TlsContextTypeDef",
    },
    total=False,
)

class TestInvokeAuthorizerRequestRequestTypeDef(
    _RequiredTestInvokeAuthorizerRequestRequestTypeDef,
    _OptionalTestInvokeAuthorizerRequestRequestTypeDef,
):
    pass

TestInvokeAuthorizerResponseTypeDef = TypedDict(
    "TestInvokeAuthorizerResponseTypeDef",
    {
        "isAuthenticated": bool,
        "principalId": str,
        "policyDocuments": List[str],
        "refreshAfterInSeconds": int,
        "disconnectAfterInSeconds": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ThingAttributeTypeDef = TypedDict(
    "ThingAttributeTypeDef",
    {
        "thingName": str,
        "thingTypeName": str,
        "thingArn": str,
        "attributes": Dict[str, str],
        "version": int,
    },
    total=False,
)

ThingConnectivityTypeDef = TypedDict(
    "ThingConnectivityTypeDef",
    {
        "connected": bool,
        "timestamp": int,
    },
    total=False,
)

ThingDocumentTypeDef = TypedDict(
    "ThingDocumentTypeDef",
    {
        "thingName": str,
        "thingId": str,
        "thingTypeName": str,
        "thingGroupNames": List[str],
        "attributes": Dict[str, str],
        "shadow": str,
        "connectivity": "ThingConnectivityTypeDef",
    },
    total=False,
)

ThingGroupDocumentTypeDef = TypedDict(
    "ThingGroupDocumentTypeDef",
    {
        "thingGroupName": str,
        "thingGroupId": str,
        "thingGroupDescription": str,
        "attributes": Dict[str, str],
        "parentGroupNames": List[str],
    },
    total=False,
)

_RequiredThingGroupIndexingConfigurationTypeDef = TypedDict(
    "_RequiredThingGroupIndexingConfigurationTypeDef",
    {
        "thingGroupIndexingMode": ThingGroupIndexingModeType,
    },
)
_OptionalThingGroupIndexingConfigurationTypeDef = TypedDict(
    "_OptionalThingGroupIndexingConfigurationTypeDef",
    {
        "managedFields": List["FieldTypeDef"],
        "customFields": List["FieldTypeDef"],
    },
    total=False,
)

class ThingGroupIndexingConfigurationTypeDef(
    _RequiredThingGroupIndexingConfigurationTypeDef, _OptionalThingGroupIndexingConfigurationTypeDef
):
    pass

ThingGroupMetadataTypeDef = TypedDict(
    "ThingGroupMetadataTypeDef",
    {
        "parentGroupName": str,
        "rootToParentThingGroups": List["GroupNameAndArnTypeDef"],
        "creationDate": datetime,
    },
    total=False,
)

ThingGroupPropertiesTypeDef = TypedDict(
    "ThingGroupPropertiesTypeDef",
    {
        "thingGroupDescription": str,
        "attributePayload": "AttributePayloadTypeDef",
    },
    total=False,
)

_RequiredThingIndexingConfigurationTypeDef = TypedDict(
    "_RequiredThingIndexingConfigurationTypeDef",
    {
        "thingIndexingMode": ThingIndexingModeType,
    },
)
_OptionalThingIndexingConfigurationTypeDef = TypedDict(
    "_OptionalThingIndexingConfigurationTypeDef",
    {
        "thingConnectivityIndexingMode": ThingConnectivityIndexingModeType,
        "managedFields": List["FieldTypeDef"],
        "customFields": List["FieldTypeDef"],
    },
    total=False,
)

class ThingIndexingConfigurationTypeDef(
    _RequiredThingIndexingConfigurationTypeDef, _OptionalThingIndexingConfigurationTypeDef
):
    pass

ThingTypeDefinitionTypeDef = TypedDict(
    "ThingTypeDefinitionTypeDef",
    {
        "thingTypeName": str,
        "thingTypeArn": str,
        "thingTypeProperties": "ThingTypePropertiesTypeDef",
        "thingTypeMetadata": "ThingTypeMetadataTypeDef",
    },
    total=False,
)

ThingTypeMetadataTypeDef = TypedDict(
    "ThingTypeMetadataTypeDef",
    {
        "deprecated": bool,
        "deprecationDate": datetime,
        "creationDate": datetime,
    },
    total=False,
)

ThingTypePropertiesTypeDef = TypedDict(
    "ThingTypePropertiesTypeDef",
    {
        "thingTypeDescription": str,
        "searchableAttributes": List[str],
    },
    total=False,
)

TimeoutConfigTypeDef = TypedDict(
    "TimeoutConfigTypeDef",
    {
        "inProgressTimeoutInMinutes": int,
    },
    total=False,
)

_RequiredTimestreamActionTypeDef = TypedDict(
    "_RequiredTimestreamActionTypeDef",
    {
        "roleArn": str,
        "databaseName": str,
        "tableName": str,
        "dimensions": List["TimestreamDimensionTypeDef"],
    },
)
_OptionalTimestreamActionTypeDef = TypedDict(
    "_OptionalTimestreamActionTypeDef",
    {
        "timestamp": "TimestreamTimestampTypeDef",
    },
    total=False,
)

class TimestreamActionTypeDef(_RequiredTimestreamActionTypeDef, _OptionalTimestreamActionTypeDef):
    pass

TimestreamDimensionTypeDef = TypedDict(
    "TimestreamDimensionTypeDef",
    {
        "name": str,
        "value": str,
    },
)

TimestreamTimestampTypeDef = TypedDict(
    "TimestreamTimestampTypeDef",
    {
        "value": str,
        "unit": str,
    },
)

TlsContextTypeDef = TypedDict(
    "TlsContextTypeDef",
    {
        "serverName": str,
    },
    total=False,
)

TopicRuleDestinationConfigurationTypeDef = TypedDict(
    "TopicRuleDestinationConfigurationTypeDef",
    {
        "httpUrlConfiguration": "HttpUrlDestinationConfigurationTypeDef",
        "vpcConfiguration": "VpcDestinationConfigurationTypeDef",
    },
    total=False,
)

TopicRuleDestinationSummaryTypeDef = TypedDict(
    "TopicRuleDestinationSummaryTypeDef",
    {
        "arn": str,
        "status": TopicRuleDestinationStatusType,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "statusReason": str,
        "httpUrlSummary": "HttpUrlDestinationSummaryTypeDef",
        "vpcDestinationSummary": "VpcDestinationSummaryTypeDef",
    },
    total=False,
)

TopicRuleDestinationTypeDef = TypedDict(
    "TopicRuleDestinationTypeDef",
    {
        "arn": str,
        "status": TopicRuleDestinationStatusType,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "statusReason": str,
        "httpUrlProperties": "HttpUrlDestinationPropertiesTypeDef",
        "vpcProperties": "VpcDestinationPropertiesTypeDef",
    },
    total=False,
)

TopicRuleListItemTypeDef = TypedDict(
    "TopicRuleListItemTypeDef",
    {
        "ruleArn": str,
        "ruleName": str,
        "topicPattern": str,
        "createdAt": datetime,
        "ruleDisabled": bool,
    },
    total=False,
)

_RequiredTopicRulePayloadTypeDef = TypedDict(
    "_RequiredTopicRulePayloadTypeDef",
    {
        "sql": str,
        "actions": List["ActionTypeDef"],
    },
)
_OptionalTopicRulePayloadTypeDef = TypedDict(
    "_OptionalTopicRulePayloadTypeDef",
    {
        "description": str,
        "ruleDisabled": bool,
        "awsIotSqlVersion": str,
        "errorAction": "ActionTypeDef",
    },
    total=False,
)

class TopicRulePayloadTypeDef(_RequiredTopicRulePayloadTypeDef, _OptionalTopicRulePayloadTypeDef):
    pass

TopicRuleTypeDef = TypedDict(
    "TopicRuleTypeDef",
    {
        "ruleName": str,
        "sql": str,
        "description": str,
        "createdAt": datetime,
        "actions": List["ActionTypeDef"],
        "ruleDisabled": bool,
        "awsIotSqlVersion": str,
        "errorAction": "ActionTypeDef",
    },
    total=False,
)

_RequiredTransferCertificateRequestRequestTypeDef = TypedDict(
    "_RequiredTransferCertificateRequestRequestTypeDef",
    {
        "certificateId": str,
        "targetAwsAccount": str,
    },
)
_OptionalTransferCertificateRequestRequestTypeDef = TypedDict(
    "_OptionalTransferCertificateRequestRequestTypeDef",
    {
        "transferMessage": str,
    },
    total=False,
)

class TransferCertificateRequestRequestTypeDef(
    _RequiredTransferCertificateRequestRequestTypeDef,
    _OptionalTransferCertificateRequestRequestTypeDef,
):
    pass

TransferCertificateResponseTypeDef = TypedDict(
    "TransferCertificateResponseTypeDef",
    {
        "transferredCertificateArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TransferDataTypeDef = TypedDict(
    "TransferDataTypeDef",
    {
        "transferMessage": str,
        "rejectReason": str,
        "transferDate": datetime,
        "acceptDate": datetime,
        "rejectDate": datetime,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateAccountAuditConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateAccountAuditConfigurationRequestRequestTypeDef",
    {
        "roleArn": str,
        "auditNotificationTargetConfigurations": Dict[
            Literal["SNS"], "AuditNotificationTargetTypeDef"
        ],
        "auditCheckConfigurations": Dict[str, "AuditCheckConfigurationTypeDef"],
    },
    total=False,
)

_RequiredUpdateAuditSuppressionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAuditSuppressionRequestRequestTypeDef",
    {
        "checkName": str,
        "resourceIdentifier": "ResourceIdentifierTypeDef",
    },
)
_OptionalUpdateAuditSuppressionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAuditSuppressionRequestRequestTypeDef",
    {
        "expirationDate": Union[datetime, str],
        "suppressIndefinitely": bool,
        "description": str,
    },
    total=False,
)

class UpdateAuditSuppressionRequestRequestTypeDef(
    _RequiredUpdateAuditSuppressionRequestRequestTypeDef,
    _OptionalUpdateAuditSuppressionRequestRequestTypeDef,
):
    pass

_RequiredUpdateAuthorizerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAuthorizerRequestRequestTypeDef",
    {
        "authorizerName": str,
    },
)
_OptionalUpdateAuthorizerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAuthorizerRequestRequestTypeDef",
    {
        "authorizerFunctionArn": str,
        "tokenKeyName": str,
        "tokenSigningPublicKeys": Dict[str, str],
        "status": AuthorizerStatusType,
    },
    total=False,
)

class UpdateAuthorizerRequestRequestTypeDef(
    _RequiredUpdateAuthorizerRequestRequestTypeDef, _OptionalUpdateAuthorizerRequestRequestTypeDef
):
    pass

UpdateAuthorizerResponseTypeDef = TypedDict(
    "UpdateAuthorizerResponseTypeDef",
    {
        "authorizerName": str,
        "authorizerArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateBillingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBillingGroupRequestRequestTypeDef",
    {
        "billingGroupName": str,
        "billingGroupProperties": "BillingGroupPropertiesTypeDef",
    },
)
_OptionalUpdateBillingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBillingGroupRequestRequestTypeDef",
    {
        "expectedVersion": int,
    },
    total=False,
)

class UpdateBillingGroupRequestRequestTypeDef(
    _RequiredUpdateBillingGroupRequestRequestTypeDef,
    _OptionalUpdateBillingGroupRequestRequestTypeDef,
):
    pass

UpdateBillingGroupResponseTypeDef = TypedDict(
    "UpdateBillingGroupResponseTypeDef",
    {
        "version": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCACertificateParamsTypeDef = TypedDict(
    "UpdateCACertificateParamsTypeDef",
    {
        "action": Literal["DEACTIVATE"],
    },
)

_RequiredUpdateCACertificateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCACertificateRequestRequestTypeDef",
    {
        "certificateId": str,
    },
)
_OptionalUpdateCACertificateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCACertificateRequestRequestTypeDef",
    {
        "newStatus": CACertificateStatusType,
        "newAutoRegistrationStatus": AutoRegistrationStatusType,
        "registrationConfig": "RegistrationConfigTypeDef",
        "removeAutoRegistration": bool,
    },
    total=False,
)

class UpdateCACertificateRequestRequestTypeDef(
    _RequiredUpdateCACertificateRequestRequestTypeDef,
    _OptionalUpdateCACertificateRequestRequestTypeDef,
):
    pass

UpdateCertificateRequestRequestTypeDef = TypedDict(
    "UpdateCertificateRequestRequestTypeDef",
    {
        "certificateId": str,
        "newStatus": CertificateStatusType,
    },
)

UpdateCustomMetricRequestRequestTypeDef = TypedDict(
    "UpdateCustomMetricRequestRequestTypeDef",
    {
        "metricName": str,
        "displayName": str,
    },
)

UpdateCustomMetricResponseTypeDef = TypedDict(
    "UpdateCustomMetricResponseTypeDef",
    {
        "metricName": str,
        "metricArn": str,
        "metricType": CustomMetricTypeType,
        "displayName": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDeviceCertificateParamsTypeDef = TypedDict(
    "UpdateDeviceCertificateParamsTypeDef",
    {
        "action": Literal["DEACTIVATE"],
    },
)

UpdateDimensionRequestRequestTypeDef = TypedDict(
    "UpdateDimensionRequestRequestTypeDef",
    {
        "name": str,
        "stringValues": List[str],
    },
)

UpdateDimensionResponseTypeDef = TypedDict(
    "UpdateDimensionResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "type": Literal["TOPIC_FILTER"],
        "stringValues": List[str],
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDomainConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainConfigurationRequestRequestTypeDef",
    {
        "domainConfigurationName": str,
    },
)
_OptionalUpdateDomainConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainConfigurationRequestRequestTypeDef",
    {
        "authorizerConfig": "AuthorizerConfigTypeDef",
        "domainConfigurationStatus": DomainConfigurationStatusType,
        "removeAuthorizerConfig": bool,
    },
    total=False,
)

class UpdateDomainConfigurationRequestRequestTypeDef(
    _RequiredUpdateDomainConfigurationRequestRequestTypeDef,
    _OptionalUpdateDomainConfigurationRequestRequestTypeDef,
):
    pass

UpdateDomainConfigurationResponseTypeDef = TypedDict(
    "UpdateDomainConfigurationResponseTypeDef",
    {
        "domainConfigurationName": str,
        "domainConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDynamicThingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDynamicThingGroupRequestRequestTypeDef",
    {
        "thingGroupName": str,
        "thingGroupProperties": "ThingGroupPropertiesTypeDef",
    },
)
_OptionalUpdateDynamicThingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDynamicThingGroupRequestRequestTypeDef",
    {
        "expectedVersion": int,
        "indexName": str,
        "queryString": str,
        "queryVersion": str,
    },
    total=False,
)

class UpdateDynamicThingGroupRequestRequestTypeDef(
    _RequiredUpdateDynamicThingGroupRequestRequestTypeDef,
    _OptionalUpdateDynamicThingGroupRequestRequestTypeDef,
):
    pass

UpdateDynamicThingGroupResponseTypeDef = TypedDict(
    "UpdateDynamicThingGroupResponseTypeDef",
    {
        "version": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEventConfigurationsRequestRequestTypeDef = TypedDict(
    "UpdateEventConfigurationsRequestRequestTypeDef",
    {
        "eventConfigurations": Dict[EventTypeType, "ConfigurationTypeDef"],
    },
    total=False,
)

UpdateIndexingConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateIndexingConfigurationRequestRequestTypeDef",
    {
        "thingIndexingConfiguration": "ThingIndexingConfigurationTypeDef",
        "thingGroupIndexingConfiguration": "ThingGroupIndexingConfigurationTypeDef",
    },
    total=False,
)

_RequiredUpdateJobRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)
_OptionalUpdateJobRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateJobRequestRequestTypeDef",
    {
        "description": str,
        "presignedUrlConfig": "PresignedUrlConfigTypeDef",
        "jobExecutionsRolloutConfig": "JobExecutionsRolloutConfigTypeDef",
        "abortConfig": "AbortConfigTypeDef",
        "timeoutConfig": "TimeoutConfigTypeDef",
        "namespaceId": str,
    },
    total=False,
)

class UpdateJobRequestRequestTypeDef(
    _RequiredUpdateJobRequestRequestTypeDef, _OptionalUpdateJobRequestRequestTypeDef
):
    pass

_RequiredUpdateMitigationActionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMitigationActionRequestRequestTypeDef",
    {
        "actionName": str,
    },
)
_OptionalUpdateMitigationActionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMitigationActionRequestRequestTypeDef",
    {
        "roleArn": str,
        "actionParams": "MitigationActionParamsTypeDef",
    },
    total=False,
)

class UpdateMitigationActionRequestRequestTypeDef(
    _RequiredUpdateMitigationActionRequestRequestTypeDef,
    _OptionalUpdateMitigationActionRequestRequestTypeDef,
):
    pass

UpdateMitigationActionResponseTypeDef = TypedDict(
    "UpdateMitigationActionResponseTypeDef",
    {
        "actionArn": str,
        "actionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProvisioningTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProvisioningTemplateRequestRequestTypeDef",
    {
        "templateName": str,
    },
)
_OptionalUpdateProvisioningTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProvisioningTemplateRequestRequestTypeDef",
    {
        "description": str,
        "enabled": bool,
        "defaultVersionId": int,
        "provisioningRoleArn": str,
        "preProvisioningHook": "ProvisioningHookTypeDef",
        "removePreProvisioningHook": bool,
    },
    total=False,
)

class UpdateProvisioningTemplateRequestRequestTypeDef(
    _RequiredUpdateProvisioningTemplateRequestRequestTypeDef,
    _OptionalUpdateProvisioningTemplateRequestRequestTypeDef,
):
    pass

_RequiredUpdateRoleAliasRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRoleAliasRequestRequestTypeDef",
    {
        "roleAlias": str,
    },
)
_OptionalUpdateRoleAliasRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRoleAliasRequestRequestTypeDef",
    {
        "roleArn": str,
        "credentialDurationSeconds": int,
    },
    total=False,
)

class UpdateRoleAliasRequestRequestTypeDef(
    _RequiredUpdateRoleAliasRequestRequestTypeDef, _OptionalUpdateRoleAliasRequestRequestTypeDef
):
    pass

UpdateRoleAliasResponseTypeDef = TypedDict(
    "UpdateRoleAliasResponseTypeDef",
    {
        "roleAlias": str,
        "roleAliasArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateScheduledAuditRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateScheduledAuditRequestRequestTypeDef",
    {
        "scheduledAuditName": str,
    },
)
_OptionalUpdateScheduledAuditRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateScheduledAuditRequestRequestTypeDef",
    {
        "frequency": AuditFrequencyType,
        "dayOfMonth": str,
        "dayOfWeek": DayOfWeekType,
        "targetCheckNames": List[str],
    },
    total=False,
)

class UpdateScheduledAuditRequestRequestTypeDef(
    _RequiredUpdateScheduledAuditRequestRequestTypeDef,
    _OptionalUpdateScheduledAuditRequestRequestTypeDef,
):
    pass

UpdateScheduledAuditResponseTypeDef = TypedDict(
    "UpdateScheduledAuditResponseTypeDef",
    {
        "scheduledAuditArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSecurityProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSecurityProfileRequestRequestTypeDef",
    {
        "securityProfileName": str,
    },
)
_OptionalUpdateSecurityProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSecurityProfileRequestRequestTypeDef",
    {
        "securityProfileDescription": str,
        "behaviors": List["BehaviorTypeDef"],
        "alertTargets": Dict[Literal["SNS"], "AlertTargetTypeDef"],
        "additionalMetricsToRetain": List[str],
        "additionalMetricsToRetainV2": List["MetricToRetainTypeDef"],
        "deleteBehaviors": bool,
        "deleteAlertTargets": bool,
        "deleteAdditionalMetricsToRetain": bool,
        "expectedVersion": int,
    },
    total=False,
)

class UpdateSecurityProfileRequestRequestTypeDef(
    _RequiredUpdateSecurityProfileRequestRequestTypeDef,
    _OptionalUpdateSecurityProfileRequestRequestTypeDef,
):
    pass

UpdateSecurityProfileResponseTypeDef = TypedDict(
    "UpdateSecurityProfileResponseTypeDef",
    {
        "securityProfileName": str,
        "securityProfileArn": str,
        "securityProfileDescription": str,
        "behaviors": List["BehaviorTypeDef"],
        "alertTargets": Dict[Literal["SNS"], "AlertTargetTypeDef"],
        "additionalMetricsToRetain": List[str],
        "additionalMetricsToRetainV2": List["MetricToRetainTypeDef"],
        "version": int,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateStreamRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateStreamRequestRequestTypeDef",
    {
        "streamId": str,
    },
)
_OptionalUpdateStreamRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateStreamRequestRequestTypeDef",
    {
        "description": str,
        "files": List["StreamFileTypeDef"],
        "roleArn": str,
    },
    total=False,
)

class UpdateStreamRequestRequestTypeDef(
    _RequiredUpdateStreamRequestRequestTypeDef, _OptionalUpdateStreamRequestRequestTypeDef
):
    pass

UpdateStreamResponseTypeDef = TypedDict(
    "UpdateStreamResponseTypeDef",
    {
        "streamId": str,
        "streamArn": str,
        "description": str,
        "streamVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateThingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateThingGroupRequestRequestTypeDef",
    {
        "thingGroupName": str,
        "thingGroupProperties": "ThingGroupPropertiesTypeDef",
    },
)
_OptionalUpdateThingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateThingGroupRequestRequestTypeDef",
    {
        "expectedVersion": int,
    },
    total=False,
)

class UpdateThingGroupRequestRequestTypeDef(
    _RequiredUpdateThingGroupRequestRequestTypeDef, _OptionalUpdateThingGroupRequestRequestTypeDef
):
    pass

UpdateThingGroupResponseTypeDef = TypedDict(
    "UpdateThingGroupResponseTypeDef",
    {
        "version": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateThingGroupsForThingRequestRequestTypeDef = TypedDict(
    "UpdateThingGroupsForThingRequestRequestTypeDef",
    {
        "thingName": str,
        "thingGroupsToAdd": List[str],
        "thingGroupsToRemove": List[str],
        "overrideDynamicGroups": bool,
    },
    total=False,
)

_RequiredUpdateThingRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateThingRequestRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalUpdateThingRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateThingRequestRequestTypeDef",
    {
        "thingTypeName": str,
        "attributePayload": "AttributePayloadTypeDef",
        "expectedVersion": int,
        "removeThingType": bool,
    },
    total=False,
)

class UpdateThingRequestRequestTypeDef(
    _RequiredUpdateThingRequestRequestTypeDef, _OptionalUpdateThingRequestRequestTypeDef
):
    pass

UpdateTopicRuleDestinationRequestRequestTypeDef = TypedDict(
    "UpdateTopicRuleDestinationRequestRequestTypeDef",
    {
        "arn": str,
        "status": TopicRuleDestinationStatusType,
    },
)

ValidateSecurityProfileBehaviorsRequestRequestTypeDef = TypedDict(
    "ValidateSecurityProfileBehaviorsRequestRequestTypeDef",
    {
        "behaviors": List["BehaviorTypeDef"],
    },
)

ValidateSecurityProfileBehaviorsResponseTypeDef = TypedDict(
    "ValidateSecurityProfileBehaviorsResponseTypeDef",
    {
        "valid": bool,
        "validationErrors": List["ValidationErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidationErrorTypeDef = TypedDict(
    "ValidationErrorTypeDef",
    {
        "errorMessage": str,
    },
    total=False,
)

ViolationEventAdditionalInfoTypeDef = TypedDict(
    "ViolationEventAdditionalInfoTypeDef",
    {
        "confidenceLevel": ConfidenceLevelType,
    },
    total=False,
)

ViolationEventOccurrenceRangeTypeDef = TypedDict(
    "ViolationEventOccurrenceRangeTypeDef",
    {
        "startTime": datetime,
        "endTime": datetime,
    },
)

ViolationEventTypeDef = TypedDict(
    "ViolationEventTypeDef",
    {
        "violationId": str,
        "thingName": str,
        "securityProfileName": str,
        "behavior": "BehaviorTypeDef",
        "metricValue": "MetricValueTypeDef",
        "violationEventAdditionalInfo": "ViolationEventAdditionalInfoTypeDef",
        "violationEventType": ViolationEventTypeType,
        "violationEventTime": datetime,
    },
    total=False,
)

_RequiredVpcDestinationConfigurationTypeDef = TypedDict(
    "_RequiredVpcDestinationConfigurationTypeDef",
    {
        "subnetIds": List[str],
        "vpcId": str,
        "roleArn": str,
    },
)
_OptionalVpcDestinationConfigurationTypeDef = TypedDict(
    "_OptionalVpcDestinationConfigurationTypeDef",
    {
        "securityGroups": List[str],
    },
    total=False,
)

class VpcDestinationConfigurationTypeDef(
    _RequiredVpcDestinationConfigurationTypeDef, _OptionalVpcDestinationConfigurationTypeDef
):
    pass

VpcDestinationPropertiesTypeDef = TypedDict(
    "VpcDestinationPropertiesTypeDef",
    {
        "subnetIds": List[str],
        "securityGroups": List[str],
        "vpcId": str,
        "roleArn": str,
    },
    total=False,
)

VpcDestinationSummaryTypeDef = TypedDict(
    "VpcDestinationSummaryTypeDef",
    {
        "subnetIds": List[str],
        "securityGroups": List[str],
        "vpcId": str,
        "roleArn": str,
    },
    total=False,
)
