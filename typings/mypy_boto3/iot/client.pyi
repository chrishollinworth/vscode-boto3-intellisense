"""
Type annotations for iot service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_iot import IoTClient

    client: IoTClient = boto3.client("iot")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AuditFrequencyType,
    AuditMitigationActionsExecutionStatusType,
    AuditMitigationActionsTaskStatusType,
    AuditTaskStatusType,
    AuditTaskTypeType,
    AuthorizerStatusType,
    AutoRegistrationStatusType,
    BehaviorCriteriaTypeType,
    CACertificateStatusType,
    CertificateStatusType,
    CustomMetricTypeType,
    DayOfWeekType,
    DomainConfigurationStatusType,
    EventTypeType,
    JobExecutionStatusType,
    JobStatusType,
    LogLevelType,
    LogTargetTypeType,
    MitigationActionTypeType,
    OTAUpdateStatusType,
    ProtocolType,
    ReportTypeType,
    ServiceTypeType,
    StatusType,
    TargetSelectionType,
    TopicRuleDestinationStatusType,
)
from .paginator import (
    GetBehaviorModelTrainingSummariesPaginator,
    ListActiveViolationsPaginator,
    ListAttachedPoliciesPaginator,
    ListAuditFindingsPaginator,
    ListAuditMitigationActionsExecutionsPaginator,
    ListAuditMitigationActionsTasksPaginator,
    ListAuditSuppressionsPaginator,
    ListAuditTasksPaginator,
    ListAuthorizersPaginator,
    ListBillingGroupsPaginator,
    ListCACertificatesPaginator,
    ListCertificatesByCAPaginator,
    ListCertificatesPaginator,
    ListCustomMetricsPaginator,
    ListDetectMitigationActionsExecutionsPaginator,
    ListDetectMitigationActionsTasksPaginator,
    ListDimensionsPaginator,
    ListDomainConfigurationsPaginator,
    ListIndicesPaginator,
    ListJobExecutionsForJobPaginator,
    ListJobExecutionsForThingPaginator,
    ListJobsPaginator,
    ListMitigationActionsPaginator,
    ListOTAUpdatesPaginator,
    ListOutgoingCertificatesPaginator,
    ListPoliciesPaginator,
    ListPolicyPrincipalsPaginator,
    ListPrincipalPoliciesPaginator,
    ListPrincipalThingsPaginator,
    ListProvisioningTemplatesPaginator,
    ListProvisioningTemplateVersionsPaginator,
    ListRoleAliasesPaginator,
    ListScheduledAuditsPaginator,
    ListSecurityProfilesForTargetPaginator,
    ListSecurityProfilesPaginator,
    ListStreamsPaginator,
    ListTagsForResourcePaginator,
    ListTargetsForPolicyPaginator,
    ListTargetsForSecurityProfilePaginator,
    ListThingGroupsForThingPaginator,
    ListThingGroupsPaginator,
    ListThingPrincipalsPaginator,
    ListThingRegistrationTaskReportsPaginator,
    ListThingRegistrationTasksPaginator,
    ListThingsInBillingGroupPaginator,
    ListThingsInThingGroupPaginator,
    ListThingsPaginator,
    ListThingTypesPaginator,
    ListTopicRuleDestinationsPaginator,
    ListTopicRulesPaginator,
    ListV2LoggingLevelsPaginator,
    ListViolationEventsPaginator,
)
from .type_defs import (
    AbortConfigTypeDef,
    AlertTargetTypeDef,
    AssociateTargetsWithJobResponseTypeDef,
    AttributePayloadTypeDef,
    AuditCheckConfigurationTypeDef,
    AuditMitigationActionsTaskTargetTypeDef,
    AuditNotificationTargetTypeDef,
    AuthInfoTypeDef,
    AuthorizerConfigTypeDef,
    AwsJobAbortConfigTypeDef,
    AwsJobExecutionsRolloutConfigTypeDef,
    AwsJobPresignedUrlConfigTypeDef,
    AwsJobTimeoutConfigTypeDef,
    BehaviorTypeDef,
    BillingGroupPropertiesTypeDef,
    CancelJobResponseTypeDef,
    ConfigurationTypeDef,
    CreateAuthorizerResponseTypeDef,
    CreateBillingGroupResponseTypeDef,
    CreateCertificateFromCsrResponseTypeDef,
    CreateCustomMetricResponseTypeDef,
    CreateDimensionResponseTypeDef,
    CreateDomainConfigurationResponseTypeDef,
    CreateDynamicThingGroupResponseTypeDef,
    CreateJobResponseTypeDef,
    CreateJobTemplateResponseTypeDef,
    CreateKeysAndCertificateResponseTypeDef,
    CreateMitigationActionResponseTypeDef,
    CreateOTAUpdateResponseTypeDef,
    CreatePolicyResponseTypeDef,
    CreatePolicyVersionResponseTypeDef,
    CreateProvisioningClaimResponseTypeDef,
    CreateProvisioningTemplateResponseTypeDef,
    CreateProvisioningTemplateVersionResponseTypeDef,
    CreateRoleAliasResponseTypeDef,
    CreateScheduledAuditResponseTypeDef,
    CreateSecurityProfileResponseTypeDef,
    CreateStreamResponseTypeDef,
    CreateThingGroupResponseTypeDef,
    CreateThingResponseTypeDef,
    CreateThingTypeResponseTypeDef,
    CreateTopicRuleDestinationResponseTypeDef,
    DescribeAccountAuditConfigurationResponseTypeDef,
    DescribeAuditFindingResponseTypeDef,
    DescribeAuditMitigationActionsTaskResponseTypeDef,
    DescribeAuditSuppressionResponseTypeDef,
    DescribeAuditTaskResponseTypeDef,
    DescribeAuthorizerResponseTypeDef,
    DescribeBillingGroupResponseTypeDef,
    DescribeCACertificateResponseTypeDef,
    DescribeCertificateResponseTypeDef,
    DescribeCustomMetricResponseTypeDef,
    DescribeDefaultAuthorizerResponseTypeDef,
    DescribeDetectMitigationActionsTaskResponseTypeDef,
    DescribeDimensionResponseTypeDef,
    DescribeDomainConfigurationResponseTypeDef,
    DescribeEndpointResponseTypeDef,
    DescribeEventConfigurationsResponseTypeDef,
    DescribeIndexResponseTypeDef,
    DescribeJobExecutionResponseTypeDef,
    DescribeJobResponseTypeDef,
    DescribeJobTemplateResponseTypeDef,
    DescribeMitigationActionResponseTypeDef,
    DescribeProvisioningTemplateResponseTypeDef,
    DescribeProvisioningTemplateVersionResponseTypeDef,
    DescribeRoleAliasResponseTypeDef,
    DescribeScheduledAuditResponseTypeDef,
    DescribeSecurityProfileResponseTypeDef,
    DescribeStreamResponseTypeDef,
    DescribeThingGroupResponseTypeDef,
    DescribeThingRegistrationTaskResponseTypeDef,
    DescribeThingResponseTypeDef,
    DescribeThingTypeResponseTypeDef,
    DetectMitigationActionsTaskTargetTypeDef,
    GetBehaviorModelTrainingSummariesResponseTypeDef,
    GetCardinalityResponseTypeDef,
    GetEffectivePoliciesResponseTypeDef,
    GetIndexingConfigurationResponseTypeDef,
    GetJobDocumentResponseTypeDef,
    GetLoggingOptionsResponseTypeDef,
    GetOTAUpdateResponseTypeDef,
    GetPercentilesResponseTypeDef,
    GetPolicyResponseTypeDef,
    GetPolicyVersionResponseTypeDef,
    GetRegistrationCodeResponseTypeDef,
    GetStatisticsResponseTypeDef,
    GetTopicRuleDestinationResponseTypeDef,
    GetTopicRuleResponseTypeDef,
    GetV2LoggingOptionsResponseTypeDef,
    HttpContextTypeDef,
    JobExecutionsRolloutConfigTypeDef,
    ListActiveViolationsResponseTypeDef,
    ListAttachedPoliciesResponseTypeDef,
    ListAuditFindingsResponseTypeDef,
    ListAuditMitigationActionsExecutionsResponseTypeDef,
    ListAuditMitigationActionsTasksResponseTypeDef,
    ListAuditSuppressionsResponseTypeDef,
    ListAuditTasksResponseTypeDef,
    ListAuthorizersResponseTypeDef,
    ListBillingGroupsResponseTypeDef,
    ListCACertificatesResponseTypeDef,
    ListCertificatesByCAResponseTypeDef,
    ListCertificatesResponseTypeDef,
    ListCustomMetricsResponseTypeDef,
    ListDetectMitigationActionsExecutionsResponseTypeDef,
    ListDetectMitigationActionsTasksResponseTypeDef,
    ListDimensionsResponseTypeDef,
    ListDomainConfigurationsResponseTypeDef,
    ListIndicesResponseTypeDef,
    ListJobExecutionsForJobResponseTypeDef,
    ListJobExecutionsForThingResponseTypeDef,
    ListJobsResponseTypeDef,
    ListJobTemplatesResponseTypeDef,
    ListMitigationActionsResponseTypeDef,
    ListOTAUpdatesResponseTypeDef,
    ListOutgoingCertificatesResponseTypeDef,
    ListPoliciesResponseTypeDef,
    ListPolicyPrincipalsResponseTypeDef,
    ListPolicyVersionsResponseTypeDef,
    ListPrincipalPoliciesResponseTypeDef,
    ListPrincipalThingsResponseTypeDef,
    ListProvisioningTemplatesResponseTypeDef,
    ListProvisioningTemplateVersionsResponseTypeDef,
    ListRoleAliasesResponseTypeDef,
    ListScheduledAuditsResponseTypeDef,
    ListSecurityProfilesForTargetResponseTypeDef,
    ListSecurityProfilesResponseTypeDef,
    ListStreamsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTargetsForPolicyResponseTypeDef,
    ListTargetsForSecurityProfileResponseTypeDef,
    ListThingGroupsForThingResponseTypeDef,
    ListThingGroupsResponseTypeDef,
    ListThingPrincipalsResponseTypeDef,
    ListThingRegistrationTaskReportsResponseTypeDef,
    ListThingRegistrationTasksResponseTypeDef,
    ListThingsInBillingGroupResponseTypeDef,
    ListThingsInThingGroupResponseTypeDef,
    ListThingsResponseTypeDef,
    ListThingTypesResponseTypeDef,
    ListTopicRuleDestinationsResponseTypeDef,
    ListTopicRulesResponseTypeDef,
    ListV2LoggingLevelsResponseTypeDef,
    ListViolationEventsResponseTypeDef,
    LoggingOptionsPayloadTypeDef,
    LogTargetTypeDef,
    MetricToRetainTypeDef,
    MitigationActionParamsTypeDef,
    MqttContextTypeDef,
    OTAUpdateFileTypeDef,
    PresignedUrlConfigTypeDef,
    ProvisioningHookTypeDef,
    RegisterCACertificateResponseTypeDef,
    RegisterCertificateResponseTypeDef,
    RegisterCertificateWithoutCAResponseTypeDef,
    RegisterThingResponseTypeDef,
    RegistrationConfigTypeDef,
    ResourceIdentifierTypeDef,
    SearchIndexResponseTypeDef,
    SetDefaultAuthorizerResponseTypeDef,
    StartAuditMitigationActionsTaskResponseTypeDef,
    StartDetectMitigationActionsTaskResponseTypeDef,
    StartOnDemandAuditTaskResponseTypeDef,
    StartThingRegistrationTaskResponseTypeDef,
    StreamFileTypeDef,
    TagTypeDef,
    TestAuthorizationResponseTypeDef,
    TestInvokeAuthorizerResponseTypeDef,
    ThingGroupIndexingConfigurationTypeDef,
    ThingGroupPropertiesTypeDef,
    ThingIndexingConfigurationTypeDef,
    ThingTypePropertiesTypeDef,
    TimeoutConfigTypeDef,
    TlsContextTypeDef,
    TopicRuleDestinationConfigurationTypeDef,
    TopicRulePayloadTypeDef,
    TransferCertificateResponseTypeDef,
    UpdateAuthorizerResponseTypeDef,
    UpdateBillingGroupResponseTypeDef,
    UpdateCustomMetricResponseTypeDef,
    UpdateDimensionResponseTypeDef,
    UpdateDomainConfigurationResponseTypeDef,
    UpdateDynamicThingGroupResponseTypeDef,
    UpdateMitigationActionResponseTypeDef,
    UpdateRoleAliasResponseTypeDef,
    UpdateScheduledAuditResponseTypeDef,
    UpdateSecurityProfileResponseTypeDef,
    UpdateStreamResponseTypeDef,
    UpdateThingGroupResponseTypeDef,
    ValidateSecurityProfileBehaviorsResponseTypeDef,
    ViolationEventOccurrenceRangeTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("IoTClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    CertificateConflictException: Type[BotocoreClientError]
    CertificateStateException: Type[BotocoreClientError]
    CertificateValidationException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ConflictingResourceUpdateException: Type[BotocoreClientError]
    DeleteConflictException: Type[BotocoreClientError]
    IndexNotReadyException: Type[BotocoreClientError]
    InternalException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidAggregationException: Type[BotocoreClientError]
    InvalidQueryException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidResponseException: Type[BotocoreClientError]
    InvalidStateTransitionException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MalformedPolicyException: Type[BotocoreClientError]
    NotConfiguredException: Type[BotocoreClientError]
    RegistrationCodeValidationException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceRegistrationFailureException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    SqlParseException: Type[BotocoreClientError]
    TaskAlreadyExistsException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TransferAlreadyCompletedException: Type[BotocoreClientError]
    TransferConflictException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]
    VersionConflictException: Type[BotocoreClientError]
    VersionsLimitExceededException: Type[BotocoreClientError]

class IoTClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        IoTClient exceptions.
        """
    def accept_certificate_transfer(self, *, certificateId: str, setAsActive: bool = None) -> None:
        """
        Accepts a pending certificate transfer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.accept_certificate_transfer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#accept_certificate_transfer)
        """
    def add_thing_to_billing_group(
        self,
        *,
        billingGroupName: str = None,
        billingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None
    ) -> Dict[str, Any]:
        """
        Adds a thing to a billing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.add_thing_to_billing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#add_thing_to_billing_group)
        """
    def add_thing_to_thing_group(
        self,
        *,
        thingGroupName: str = None,
        thingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None,
        overrideDynamicGroups: bool = None
    ) -> Dict[str, Any]:
        """
        Adds a thing to a thing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.add_thing_to_thing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#add_thing_to_thing_group)
        """
    def associate_targets_with_job(
        self, *, targets: List[str], jobId: str, comment: str = None, namespaceId: str = None
    ) -> AssociateTargetsWithJobResponseTypeDef:
        """
        Associates a group with a continuous job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.associate_targets_with_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#associate_targets_with_job)
        """
    def attach_policy(self, *, policyName: str, target: str) -> None:
        """
        Attaches the specified policy to the specified principal (certificate or other
        credential).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.attach_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#attach_policy)
        """
    def attach_principal_policy(self, *, policyName: str, principal: str) -> None:
        """
        Attaches the specified policy to the specified principal (certificate or other
        credential).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.attach_principal_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#attach_principal_policy)
        """
    def attach_security_profile(
        self, *, securityProfileName: str, securityProfileTargetArn: str
    ) -> Dict[str, Any]:
        """
        Associates a Device Defender security profile with a thing group or this
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.attach_security_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#attach_security_profile)
        """
    def attach_thing_principal(self, *, thingName: str, principal: str) -> Dict[str, Any]:
        """
        Attaches the specified principal to the specified thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.attach_thing_principal)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#attach_thing_principal)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#can_paginate)
        """
    def cancel_audit_mitigation_actions_task(self, *, taskId: str) -> Dict[str, Any]:
        """
        Cancels a mitigation action task that is in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.cancel_audit_mitigation_actions_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#cancel_audit_mitigation_actions_task)
        """
    def cancel_audit_task(self, *, taskId: str) -> Dict[str, Any]:
        """
        Cancels an audit that is in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.cancel_audit_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#cancel_audit_task)
        """
    def cancel_certificate_transfer(self, *, certificateId: str) -> None:
        """
        Cancels a pending transfer for the specified certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.cancel_certificate_transfer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#cancel_certificate_transfer)
        """
    def cancel_detect_mitigation_actions_task(self, *, taskId: str) -> Dict[str, Any]:
        """
        Cancels a Device Defender ML Detect mitigation action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.cancel_detect_mitigation_actions_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#cancel_detect_mitigation_actions_task)
        """
    def cancel_job(
        self, *, jobId: str, reasonCode: str = None, comment: str = None, force: bool = None
    ) -> CancelJobResponseTypeDef:
        """
        Cancels a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.cancel_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#cancel_job)
        """
    def cancel_job_execution(
        self,
        *,
        jobId: str,
        thingName: str,
        force: bool = None,
        expectedVersion: int = None,
        statusDetails: Dict[str, str] = None
    ) -> None:
        """
        Cancels the execution of a job for a given thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.cancel_job_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#cancel_job_execution)
        """
    def clear_default_authorizer(self) -> Dict[str, Any]:
        """
        Clears the default authorizer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.clear_default_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#clear_default_authorizer)
        """
    def confirm_topic_rule_destination(self, *, confirmationToken: str) -> Dict[str, Any]:
        """
        Confirms a topic rule destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.confirm_topic_rule_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#confirm_topic_rule_destination)
        """
    def create_audit_suppression(
        self,
        *,
        checkName: str,
        resourceIdentifier: "ResourceIdentifierTypeDef",
        clientRequestToken: str,
        expirationDate: Union[datetime, str] = None,
        suppressIndefinitely: bool = None,
        description: str = None
    ) -> Dict[str, Any]:
        """
        Creates a Device Defender audit suppression.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_audit_suppression)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_audit_suppression)
        """
    def create_authorizer(
        self,
        *,
        authorizerName: str,
        authorizerFunctionArn: str,
        tokenKeyName: str = None,
        tokenSigningPublicKeys: Dict[str, str] = None,
        status: AuthorizerStatusType = None,
        tags: List["TagTypeDef"] = None,
        signingDisabled: bool = None
    ) -> CreateAuthorizerResponseTypeDef:
        """
        Creates an authorizer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_authorizer)
        """
    def create_billing_group(
        self,
        *,
        billingGroupName: str,
        billingGroupProperties: "BillingGroupPropertiesTypeDef" = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateBillingGroupResponseTypeDef:
        """
        Creates a billing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_billing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_billing_group)
        """
    def create_certificate_from_csr(
        self, *, certificateSigningRequest: str, setAsActive: bool = None
    ) -> CreateCertificateFromCsrResponseTypeDef:
        """
        Creates an X.509 certificate using the specified certificate signing request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_certificate_from_csr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_certificate_from_csr)
        """
    def create_custom_metric(
        self,
        *,
        metricName: str,
        metricType: CustomMetricTypeType,
        clientRequestToken: str,
        displayName: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateCustomMetricResponseTypeDef:
        """
        Use this API to define a Custom Metric published by your devices to Device
        Defender.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_custom_metric)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_custom_metric)
        """
    def create_dimension(
        self,
        *,
        name: str,
        type: Literal["TOPIC_FILTER"],
        stringValues: List[str],
        clientRequestToken: str,
        tags: List["TagTypeDef"] = None
    ) -> CreateDimensionResponseTypeDef:
        """
        Create a dimension that you can use to limit the scope of a metric used in a
        security profile for AWS IoT Device Defender.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_dimension)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_dimension)
        """
    def create_domain_configuration(
        self,
        *,
        domainConfigurationName: str,
        domainName: str = None,
        serverCertificateArns: List[str] = None,
        validationCertificateArn: str = None,
        authorizerConfig: "AuthorizerConfigTypeDef" = None,
        serviceType: ServiceTypeType = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateDomainConfigurationResponseTypeDef:
        """
        Creates a domain configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_domain_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_domain_configuration)
        """
    def create_dynamic_thing_group(
        self,
        *,
        thingGroupName: str,
        queryString: str,
        thingGroupProperties: "ThingGroupPropertiesTypeDef" = None,
        indexName: str = None,
        queryVersion: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateDynamicThingGroupResponseTypeDef:
        """
        Creates a dynamic thing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_dynamic_thing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_dynamic_thing_group)
        """
    def create_job(
        self,
        *,
        jobId: str,
        targets: List[str],
        documentSource: str = None,
        document: str = None,
        description: str = None,
        presignedUrlConfig: "PresignedUrlConfigTypeDef" = None,
        targetSelection: TargetSelectionType = None,
        jobExecutionsRolloutConfig: "JobExecutionsRolloutConfigTypeDef" = None,
        abortConfig: "AbortConfigTypeDef" = None,
        timeoutConfig: "TimeoutConfigTypeDef" = None,
        tags: List["TagTypeDef"] = None,
        namespaceId: str = None,
        jobTemplateArn: str = None
    ) -> CreateJobResponseTypeDef:
        """
        Creates a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_job)
        """
    def create_job_template(
        self,
        *,
        jobTemplateId: str,
        description: str,
        jobArn: str = None,
        documentSource: str = None,
        document: str = None,
        presignedUrlConfig: "PresignedUrlConfigTypeDef" = None,
        jobExecutionsRolloutConfig: "JobExecutionsRolloutConfigTypeDef" = None,
        abortConfig: "AbortConfigTypeDef" = None,
        timeoutConfig: "TimeoutConfigTypeDef" = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateJobTemplateResponseTypeDef:
        """
        Creates a job template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_job_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_job_template)
        """
    def create_keys_and_certificate(
        self, *, setAsActive: bool = None
    ) -> CreateKeysAndCertificateResponseTypeDef:
        """
        Creates a 2048-bit RSA key pair and issues an X.509 certificate using the issued
        public key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_keys_and_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_keys_and_certificate)
        """
    def create_mitigation_action(
        self,
        *,
        actionName: str,
        roleArn: str,
        actionParams: "MitigationActionParamsTypeDef",
        tags: List["TagTypeDef"] = None
    ) -> CreateMitigationActionResponseTypeDef:
        """
        Defines an action that can be applied to audit findings by using
        StartAuditMitigationActionsTask.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_mitigation_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_mitigation_action)
        """
    def create_ota_update(
        self,
        *,
        otaUpdateId: str,
        targets: List[str],
        files: List["OTAUpdateFileTypeDef"],
        roleArn: str,
        description: str = None,
        protocols: List[ProtocolType] = None,
        targetSelection: TargetSelectionType = None,
        awsJobExecutionsRolloutConfig: "AwsJobExecutionsRolloutConfigTypeDef" = None,
        awsJobPresignedUrlConfig: "AwsJobPresignedUrlConfigTypeDef" = None,
        awsJobAbortConfig: "AwsJobAbortConfigTypeDef" = None,
        awsJobTimeoutConfig: "AwsJobTimeoutConfigTypeDef" = None,
        additionalParameters: Dict[str, str] = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateOTAUpdateResponseTypeDef:
        """
        Creates an AWS IoT OTAUpdate on a target group of things or groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_ota_update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_ota_update)
        """
    def create_policy(
        self, *, policyName: str, policyDocument: str, tags: List["TagTypeDef"] = None
    ) -> CreatePolicyResponseTypeDef:
        """
        Creates an AWS IoT policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_policy)
        """
    def create_policy_version(
        self, *, policyName: str, policyDocument: str, setAsDefault: bool = None
    ) -> CreatePolicyVersionResponseTypeDef:
        """
        Creates a new version of the specified AWS IoT policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_policy_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_policy_version)
        """
    def create_provisioning_claim(
        self, *, templateName: str
    ) -> CreateProvisioningClaimResponseTypeDef:
        """
        Creates a provisioning claim.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_provisioning_claim)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_provisioning_claim)
        """
    def create_provisioning_template(
        self,
        *,
        templateName: str,
        templateBody: str,
        provisioningRoleArn: str,
        description: str = None,
        enabled: bool = None,
        preProvisioningHook: "ProvisioningHookTypeDef" = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateProvisioningTemplateResponseTypeDef:
        """
        Creates a fleet provisioning template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_provisioning_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_provisioning_template)
        """
    def create_provisioning_template_version(
        self, *, templateName: str, templateBody: str, setAsDefault: bool = None
    ) -> CreateProvisioningTemplateVersionResponseTypeDef:
        """
        Creates a new version of a fleet provisioning template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_provisioning_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_provisioning_template_version)
        """
    def create_role_alias(
        self,
        *,
        roleAlias: str,
        roleArn: str,
        credentialDurationSeconds: int = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateRoleAliasResponseTypeDef:
        """
        Creates a role alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_role_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_role_alias)
        """
    def create_scheduled_audit(
        self,
        *,
        frequency: AuditFrequencyType,
        targetCheckNames: List[str],
        scheduledAuditName: str,
        dayOfMonth: str = None,
        dayOfWeek: DayOfWeekType = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateScheduledAuditResponseTypeDef:
        """
        Creates a scheduled audit that is run at a specified time interval.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_scheduled_audit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_scheduled_audit)
        """
    def create_security_profile(
        self,
        *,
        securityProfileName: str,
        securityProfileDescription: str = None,
        behaviors: List["BehaviorTypeDef"] = None,
        alertTargets: Dict[Literal["SNS"], "AlertTargetTypeDef"] = None,
        additionalMetricsToRetain: List[str] = None,
        additionalMetricsToRetainV2: List["MetricToRetainTypeDef"] = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateSecurityProfileResponseTypeDef:
        """
        Creates a Device Defender security profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_security_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_security_profile)
        """
    def create_stream(
        self,
        *,
        streamId: str,
        files: List["StreamFileTypeDef"],
        roleArn: str,
        description: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateStreamResponseTypeDef:
        """
        Creates a stream for delivering one or more large files in chunks over MQTT.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_stream)
        """
    def create_thing(
        self,
        *,
        thingName: str,
        thingTypeName: str = None,
        attributePayload: "AttributePayloadTypeDef" = None,
        billingGroupName: str = None
    ) -> CreateThingResponseTypeDef:
        """
        Creates a thing record in the registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_thing)
        """
    def create_thing_group(
        self,
        *,
        thingGroupName: str,
        parentGroupName: str = None,
        thingGroupProperties: "ThingGroupPropertiesTypeDef" = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateThingGroupResponseTypeDef:
        """
        Create a thing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_thing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_thing_group)
        """
    def create_thing_type(
        self,
        *,
        thingTypeName: str,
        thingTypeProperties: "ThingTypePropertiesTypeDef" = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateThingTypeResponseTypeDef:
        """
        Creates a new thing type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_thing_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_thing_type)
        """
    def create_topic_rule(
        self, *, ruleName: str, topicRulePayload: "TopicRulePayloadTypeDef", tags: str = None
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_topic_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_topic_rule)
        """
    def create_topic_rule_destination(
        self, *, destinationConfiguration: "TopicRuleDestinationConfigurationTypeDef"
    ) -> CreateTopicRuleDestinationResponseTypeDef:
        """
        Creates a topic rule destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.create_topic_rule_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#create_topic_rule_destination)
        """
    def delete_account_audit_configuration(
        self, *, deleteScheduledAudits: bool = None
    ) -> Dict[str, Any]:
        """
        Restores the default settings for Device Defender audits for this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_account_audit_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_account_audit_configuration)
        """
    def delete_audit_suppression(
        self, *, checkName: str, resourceIdentifier: "ResourceIdentifierTypeDef"
    ) -> Dict[str, Any]:
        """
        Deletes a Device Defender audit suppression.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_audit_suppression)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_audit_suppression)
        """
    def delete_authorizer(self, *, authorizerName: str) -> Dict[str, Any]:
        """
        Deletes an authorizer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_authorizer)
        """
    def delete_billing_group(
        self, *, billingGroupName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        """
        Deletes the billing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_billing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_billing_group)
        """
    def delete_ca_certificate(self, *, certificateId: str) -> Dict[str, Any]:
        """
        Deletes a registered CA certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_ca_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_ca_certificate)
        """
    def delete_certificate(self, *, certificateId: str, forceDelete: bool = None) -> None:
        """
        Deletes the specified certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_certificate)
        """
    def delete_custom_metric(self, *, metricName: str) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_custom_metric)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_custom_metric)
        """
    def delete_dimension(self, *, name: str) -> Dict[str, Any]:
        """
        Removes the specified dimension from your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_dimension)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_dimension)
        """
    def delete_domain_configuration(self, *, domainConfigurationName: str) -> Dict[str, Any]:
        """
        Deletes the specified domain configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_domain_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_domain_configuration)
        """
    def delete_dynamic_thing_group(
        self, *, thingGroupName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        """
        Deletes a dynamic thing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_dynamic_thing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_dynamic_thing_group)
        """
    def delete_job(self, *, jobId: str, force: bool = None, namespaceId: str = None) -> None:
        """
        Deletes a job and its related job executions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_job)
        """
    def delete_job_execution(
        self,
        *,
        jobId: str,
        thingName: str,
        executionNumber: int,
        force: bool = None,
        namespaceId: str = None
    ) -> None:
        """
        Deletes a job execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_job_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_job_execution)
        """
    def delete_job_template(self, *, jobTemplateId: str) -> None:
        """
        Deletes the specified job template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_job_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_job_template)
        """
    def delete_mitigation_action(self, *, actionName: str) -> Dict[str, Any]:
        """
        Deletes a defined mitigation action from your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_mitigation_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_mitigation_action)
        """
    def delete_ota_update(
        self, *, otaUpdateId: str, deleteStream: bool = None, forceDeleteAWSJob: bool = None
    ) -> Dict[str, Any]:
        """
        Delete an OTA update.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_ota_update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_ota_update)
        """
    def delete_policy(self, *, policyName: str) -> None:
        """
        Deletes the specified policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_policy)
        """
    def delete_policy_version(self, *, policyName: str, policyVersionId: str) -> None:
        """
        Deletes the specified version of the specified policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_policy_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_policy_version)
        """
    def delete_provisioning_template(self, *, templateName: str) -> Dict[str, Any]:
        """
        Deletes a fleet provisioning template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_provisioning_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_provisioning_template)
        """
    def delete_provisioning_template_version(
        self, *, templateName: str, versionId: int
    ) -> Dict[str, Any]:
        """
        Deletes a fleet provisioning template version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_provisioning_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_provisioning_template_version)
        """
    def delete_registration_code(self) -> Dict[str, Any]:
        """
        Deletes a CA certificate registration code.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_registration_code)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_registration_code)
        """
    def delete_role_alias(self, *, roleAlias: str) -> Dict[str, Any]:
        """
        Deletes a role alias See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteRoleAlias>`_
        **Request Syntax** response = client.delete_role_alias( roleAlias='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_role_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_role_alias)
        """
    def delete_scheduled_audit(self, *, scheduledAuditName: str) -> Dict[str, Any]:
        """
        Deletes a scheduled audit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_scheduled_audit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_scheduled_audit)
        """
    def delete_security_profile(
        self, *, securityProfileName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        """
        Deletes a Device Defender security profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_security_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_security_profile)
        """
    def delete_stream(self, *, streamId: str) -> Dict[str, Any]:
        """
        Deletes a stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_stream)
        """
    def delete_thing(self, *, thingName: str, expectedVersion: int = None) -> Dict[str, Any]:
        """
        Deletes the specified thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_thing)
        """
    def delete_thing_group(
        self, *, thingGroupName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        """
        Deletes a thing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_thing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_thing_group)
        """
    def delete_thing_type(self, *, thingTypeName: str) -> Dict[str, Any]:
        """
        Deletes the specified thing type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_thing_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_thing_type)
        """
    def delete_topic_rule(self, *, ruleName: str) -> None:
        """
        Deletes the rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_topic_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_topic_rule)
        """
    def delete_topic_rule_destination(self, *, arn: str) -> Dict[str, Any]:
        """
        Deletes a topic rule destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_topic_rule_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_topic_rule_destination)
        """
    def delete_v2_logging_level(self, *, targetType: LogTargetTypeType, targetName: str) -> None:
        """
        Deletes a logging level.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.delete_v2_logging_level)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#delete_v2_logging_level)
        """
    def deprecate_thing_type(
        self, *, thingTypeName: str, undoDeprecate: bool = None
    ) -> Dict[str, Any]:
        """
        Deprecates a thing type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.deprecate_thing_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#deprecate_thing_type)
        """
    def describe_account_audit_configuration(
        self,
    ) -> DescribeAccountAuditConfigurationResponseTypeDef:
        """
        Gets information about the Device Defender audit settings for this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_account_audit_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_account_audit_configuration)
        """
    def describe_audit_finding(self, *, findingId: str) -> DescribeAuditFindingResponseTypeDef:
        """
        Gets information about a single audit finding.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_audit_finding)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_audit_finding)
        """
    def describe_audit_mitigation_actions_task(
        self, *, taskId: str
    ) -> DescribeAuditMitigationActionsTaskResponseTypeDef:
        """
        Gets information about an audit mitigation task that is used to apply mitigation
        actions to a set of audit findings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_audit_mitigation_actions_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_audit_mitigation_actions_task)
        """
    def describe_audit_suppression(
        self, *, checkName: str, resourceIdentifier: "ResourceIdentifierTypeDef"
    ) -> DescribeAuditSuppressionResponseTypeDef:
        """
        Gets information about a Device Defender audit suppression.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_audit_suppression)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_audit_suppression)
        """
    def describe_audit_task(self, *, taskId: str) -> DescribeAuditTaskResponseTypeDef:
        """
        Gets information about a Device Defender audit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_audit_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_audit_task)
        """
    def describe_authorizer(self, *, authorizerName: str) -> DescribeAuthorizerResponseTypeDef:
        """
        Describes an authorizer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_authorizer)
        """
    def describe_billing_group(
        self, *, billingGroupName: str
    ) -> DescribeBillingGroupResponseTypeDef:
        """
        Returns information about a billing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_billing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_billing_group)
        """
    def describe_ca_certificate(
        self, *, certificateId: str
    ) -> DescribeCACertificateResponseTypeDef:
        """
        Describes a registered CA certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_ca_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_ca_certificate)
        """
    def describe_certificate(self, *, certificateId: str) -> DescribeCertificateResponseTypeDef:
        """
        Gets information about the specified certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_certificate)
        """
    def describe_custom_metric(self, *, metricName: str) -> DescribeCustomMetricResponseTypeDef:
        """
        Gets information about a Device Defender detect custom metric.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_custom_metric)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_custom_metric)
        """
    def describe_default_authorizer(self) -> DescribeDefaultAuthorizerResponseTypeDef:
        """
        Describes the default authorizer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_default_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_default_authorizer)
        """
    def describe_detect_mitigation_actions_task(
        self, *, taskId: str
    ) -> DescribeDetectMitigationActionsTaskResponseTypeDef:
        """
        Gets information about a Device Defender ML Detect mitigation action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_detect_mitigation_actions_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_detect_mitigation_actions_task)
        """
    def describe_dimension(self, *, name: str) -> DescribeDimensionResponseTypeDef:
        """
        Provides details about a dimension that is defined in your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_dimension)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_dimension)
        """
    def describe_domain_configuration(
        self, *, domainConfigurationName: str
    ) -> DescribeDomainConfigurationResponseTypeDef:
        """
        Gets summary information about a domain configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_domain_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_domain_configuration)
        """
    def describe_endpoint(self, *, endpointType: str = None) -> DescribeEndpointResponseTypeDef:
        """
        Returns a unique endpoint specific to the AWS account making the call.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_endpoint)
        """
    def describe_event_configurations(self) -> DescribeEventConfigurationsResponseTypeDef:
        """
        Describes event configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_event_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_event_configurations)
        """
    def describe_index(self, *, indexName: str) -> DescribeIndexResponseTypeDef:
        """
        Describes a search index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_index)
        """
    def describe_job(self, *, jobId: str) -> DescribeJobResponseTypeDef:
        """
        Describes a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_job)
        """
    def describe_job_execution(
        self, *, jobId: str, thingName: str, executionNumber: int = None
    ) -> DescribeJobExecutionResponseTypeDef:
        """
        Describes a job execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_job_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_job_execution)
        """
    def describe_job_template(self, *, jobTemplateId: str) -> DescribeJobTemplateResponseTypeDef:
        """
        Returns information about a job template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_job_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_job_template)
        """
    def describe_mitigation_action(
        self, *, actionName: str
    ) -> DescribeMitigationActionResponseTypeDef:
        """
        Gets information about a mitigation action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_mitigation_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_mitigation_action)
        """
    def describe_provisioning_template(
        self, *, templateName: str
    ) -> DescribeProvisioningTemplateResponseTypeDef:
        """
        Returns information about a fleet provisioning template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_provisioning_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_provisioning_template)
        """
    def describe_provisioning_template_version(
        self, *, templateName: str, versionId: int
    ) -> DescribeProvisioningTemplateVersionResponseTypeDef:
        """
        Returns information about a fleet provisioning template version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_provisioning_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_provisioning_template_version)
        """
    def describe_role_alias(self, *, roleAlias: str) -> DescribeRoleAliasResponseTypeDef:
        """
        Describes a role alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_role_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_role_alias)
        """
    def describe_scheduled_audit(
        self, *, scheduledAuditName: str
    ) -> DescribeScheduledAuditResponseTypeDef:
        """
        Gets information about a scheduled audit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_scheduled_audit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_scheduled_audit)
        """
    def describe_security_profile(
        self, *, securityProfileName: str
    ) -> DescribeSecurityProfileResponseTypeDef:
        """
        Gets information about a Device Defender security profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_security_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_security_profile)
        """
    def describe_stream(self, *, streamId: str) -> DescribeStreamResponseTypeDef:
        """
        Gets information about a stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_stream)
        """
    def describe_thing(self, *, thingName: str) -> DescribeThingResponseTypeDef:
        """
        Gets information about the specified thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_thing)
        """
    def describe_thing_group(self, *, thingGroupName: str) -> DescribeThingGroupResponseTypeDef:
        """
        Describe a thing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_thing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_thing_group)
        """
    def describe_thing_registration_task(
        self, *, taskId: str
    ) -> DescribeThingRegistrationTaskResponseTypeDef:
        """
        Describes a bulk thing provisioning task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_thing_registration_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_thing_registration_task)
        """
    def describe_thing_type(self, *, thingTypeName: str) -> DescribeThingTypeResponseTypeDef:
        """
        Gets information about the specified thing type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.describe_thing_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#describe_thing_type)
        """
    def detach_policy(self, *, policyName: str, target: str) -> None:
        """
        Detaches a policy from the specified target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.detach_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#detach_policy)
        """
    def detach_principal_policy(self, *, policyName: str, principal: str) -> None:
        """
        Removes the specified policy from the specified certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.detach_principal_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#detach_principal_policy)
        """
    def detach_security_profile(
        self, *, securityProfileName: str, securityProfileTargetArn: str
    ) -> Dict[str, Any]:
        """
        Disassociates a Device Defender security profile from a thing group or from this
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.detach_security_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#detach_security_profile)
        """
    def detach_thing_principal(self, *, thingName: str, principal: str) -> Dict[str, Any]:
        """
        Detaches the specified principal from the specified thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.detach_thing_principal)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#detach_thing_principal)
        """
    def disable_topic_rule(self, *, ruleName: str) -> None:
        """
        Disables the rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.disable_topic_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#disable_topic_rule)
        """
    def enable_topic_rule(self, *, ruleName: str) -> None:
        """
        Enables the rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.enable_topic_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#enable_topic_rule)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#generate_presigned_url)
        """
    def get_behavior_model_training_summaries(
        self, *, securityProfileName: str = None, maxResults: int = None, nextToken: str = None
    ) -> GetBehaviorModelTrainingSummariesResponseTypeDef:
        """
        Returns a Device Defender's ML Detect Security Profile training model's status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.get_behavior_model_training_summaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get_behavior_model_training_summaries)
        """
    def get_cardinality(
        self,
        *,
        queryString: str,
        indexName: str = None,
        aggregationField: str = None,
        queryVersion: str = None
    ) -> GetCardinalityResponseTypeDef:
        """
        Returns the approximate count of unique values that match the query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.get_cardinality)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get_cardinality)
        """
    def get_effective_policies(
        self, *, principal: str = None, cognitoIdentityPoolId: str = None, thingName: str = None
    ) -> GetEffectivePoliciesResponseTypeDef:
        """
        Gets a list of the policies that have an effect on the authorization behavior of
        the specified device when it connects to the AWS IoT device gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.get_effective_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get_effective_policies)
        """
    def get_indexing_configuration(self) -> GetIndexingConfigurationResponseTypeDef:
        """
        Gets the indexing configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.get_indexing_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get_indexing_configuration)
        """
    def get_job_document(self, *, jobId: str) -> GetJobDocumentResponseTypeDef:
        """
        Gets a job document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.get_job_document)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get_job_document)
        """
    def get_logging_options(self) -> GetLoggingOptionsResponseTypeDef:
        """
        Gets the logging options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.get_logging_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get_logging_options)
        """
    def get_ota_update(self, *, otaUpdateId: str) -> GetOTAUpdateResponseTypeDef:
        """
        Gets an OTA update.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.get_ota_update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get_ota_update)
        """
    def get_percentiles(
        self,
        *,
        queryString: str,
        indexName: str = None,
        aggregationField: str = None,
        queryVersion: str = None,
        percents: List[float] = None
    ) -> GetPercentilesResponseTypeDef:
        """
        Groups the aggregated values that match the query into percentile groupings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.get_percentiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get_percentiles)
        """
    def get_policy(self, *, policyName: str) -> GetPolicyResponseTypeDef:
        """
        Gets information about the specified policy with the policy document of the
        default version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.get_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get_policy)
        """
    def get_policy_version(
        self, *, policyName: str, policyVersionId: str
    ) -> GetPolicyVersionResponseTypeDef:
        """
        Gets information about the specified policy version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.get_policy_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get_policy_version)
        """
    def get_registration_code(self) -> GetRegistrationCodeResponseTypeDef:
        """
        Gets a registration code used to register a CA certificate with AWS IoT.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.get_registration_code)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get_registration_code)
        """
    def get_statistics(
        self,
        *,
        queryString: str,
        indexName: str = None,
        aggregationField: str = None,
        queryVersion: str = None
    ) -> GetStatisticsResponseTypeDef:
        """
        Returns the count, average, sum, minimum, maximum, sum of squares, variance, and
        standard deviation for the specified aggregated field.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.get_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get_statistics)
        """
    def get_topic_rule(self, *, ruleName: str) -> GetTopicRuleResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.get_topic_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get_topic_rule)
        """
    def get_topic_rule_destination(self, *, arn: str) -> GetTopicRuleDestinationResponseTypeDef:
        """
        Gets information about a topic rule destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.get_topic_rule_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get_topic_rule_destination)
        """
    def get_v2_logging_options(self) -> GetV2LoggingOptionsResponseTypeDef:
        """
        Gets the fine grained logging options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.get_v2_logging_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#get_v2_logging_options)
        """
    def list_active_violations(
        self,
        *,
        thingName: str = None,
        securityProfileName: str = None,
        behaviorCriteriaType: BehaviorCriteriaTypeType = None,
        listSuppressedAlerts: bool = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListActiveViolationsResponseTypeDef:
        """
        Lists the active violations for a given Device Defender security profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_active_violations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_active_violations)
        """
    def list_attached_policies(
        self, *, target: str, recursive: bool = None, marker: str = None, pageSize: int = None
    ) -> ListAttachedPoliciesResponseTypeDef:
        """
        Lists the policies attached to the specified thing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_attached_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_attached_policies)
        """
    def list_audit_findings(
        self,
        *,
        taskId: str = None,
        checkName: str = None,
        resourceIdentifier: "ResourceIdentifierTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None,
        startTime: Union[datetime, str] = None,
        endTime: Union[datetime, str] = None,
        listSuppressedFindings: bool = None
    ) -> ListAuditFindingsResponseTypeDef:
        """
        Lists the findings (results) of a Device Defender audit or of the audits
        performed during a specified time period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_audit_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_audit_findings)
        """
    def list_audit_mitigation_actions_executions(
        self,
        *,
        taskId: str,
        findingId: str,
        actionStatus: AuditMitigationActionsExecutionStatusType = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListAuditMitigationActionsExecutionsResponseTypeDef:
        """
        Gets the status of audit mitigation action tasks that were executed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_audit_mitigation_actions_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_audit_mitigation_actions_executions)
        """
    def list_audit_mitigation_actions_tasks(
        self,
        *,
        startTime: Union[datetime, str],
        endTime: Union[datetime, str],
        auditTaskId: str = None,
        findingId: str = None,
        taskStatus: AuditMitigationActionsTaskStatusType = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListAuditMitigationActionsTasksResponseTypeDef:
        """
        Gets a list of audit mitigation action tasks that match the specified filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_audit_mitigation_actions_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_audit_mitigation_actions_tasks)
        """
    def list_audit_suppressions(
        self,
        *,
        checkName: str = None,
        resourceIdentifier: "ResourceIdentifierTypeDef" = None,
        ascendingOrder: bool = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListAuditSuppressionsResponseTypeDef:
        """
        Lists your Device Defender audit listings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_audit_suppressions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_audit_suppressions)
        """
    def list_audit_tasks(
        self,
        *,
        startTime: Union[datetime, str],
        endTime: Union[datetime, str],
        taskType: AuditTaskTypeType = None,
        taskStatus: AuditTaskStatusType = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListAuditTasksResponseTypeDef:
        """
        Lists the Device Defender audits that have been performed during a given time
        period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_audit_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_audit_tasks)
        """
    def list_authorizers(
        self,
        *,
        pageSize: int = None,
        marker: str = None,
        ascendingOrder: bool = None,
        status: AuthorizerStatusType = None
    ) -> ListAuthorizersResponseTypeDef:
        """
        Lists the authorizers registered in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_authorizers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_authorizers)
        """
    def list_billing_groups(
        self, *, nextToken: str = None, maxResults: int = None, namePrefixFilter: str = None
    ) -> ListBillingGroupsResponseTypeDef:
        """
        Lists the billing groups you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_billing_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_billing_groups)
        """
    def list_ca_certificates(
        self, *, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> ListCACertificatesResponseTypeDef:
        """
        Lists the CA certificates registered for your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_ca_certificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_ca_certificates)
        """
    def list_certificates(
        self, *, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> ListCertificatesResponseTypeDef:
        """
        Lists the certificates registered in your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_certificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_certificates)
        """
    def list_certificates_by_ca(
        self,
        *,
        caCertificateId: str,
        pageSize: int = None,
        marker: str = None,
        ascendingOrder: bool = None
    ) -> ListCertificatesByCAResponseTypeDef:
        """
        List the device certificates signed by the specified CA certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_certificates_by_ca)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_certificates_by_ca)
        """
    def list_custom_metrics(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListCustomMetricsResponseTypeDef:
        """
        Lists your Device Defender detect custom metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_custom_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_custom_metrics)
        """
    def list_detect_mitigation_actions_executions(
        self,
        *,
        taskId: str = None,
        violationId: str = None,
        thingName: str = None,
        startTime: Union[datetime, str] = None,
        endTime: Union[datetime, str] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListDetectMitigationActionsExecutionsResponseTypeDef:
        """
        Lists mitigation actions executions for a Device Defender ML Detect Security
        Profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_detect_mitigation_actions_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_detect_mitigation_actions_executions)
        """
    def list_detect_mitigation_actions_tasks(
        self,
        *,
        startTime: Union[datetime, str],
        endTime: Union[datetime, str],
        maxResults: int = None,
        nextToken: str = None
    ) -> ListDetectMitigationActionsTasksResponseTypeDef:
        """
        List of Device Defender ML Detect mitigation actions tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_detect_mitigation_actions_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_detect_mitigation_actions_tasks)
        """
    def list_dimensions(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListDimensionsResponseTypeDef:
        """
        List the set of dimensions that are defined for your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_dimensions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_dimensions)
        """
    def list_domain_configurations(
        self, *, marker: str = None, pageSize: int = None, serviceType: ServiceTypeType = None
    ) -> ListDomainConfigurationsResponseTypeDef:
        """
        Gets a list of domain configurations for the user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_domain_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_domain_configurations)
        """
    def list_indices(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListIndicesResponseTypeDef:
        """
        Lists the search indices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_indices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_indices)
        """
    def list_job_executions_for_job(
        self,
        *,
        jobId: str,
        status: JobExecutionStatusType = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListJobExecutionsForJobResponseTypeDef:
        """
        Lists the job executions for a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_job_executions_for_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_job_executions_for_job)
        """
    def list_job_executions_for_thing(
        self,
        *,
        thingName: str,
        status: JobExecutionStatusType = None,
        namespaceId: str = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListJobExecutionsForThingResponseTypeDef:
        """
        Lists the job executions for the specified thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_job_executions_for_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_job_executions_for_thing)
        """
    def list_job_templates(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListJobTemplatesResponseTypeDef:
        """
        Returns a list of job templates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_job_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_job_templates)
        """
    def list_jobs(
        self,
        *,
        status: JobStatusType = None,
        targetSelection: TargetSelectionType = None,
        maxResults: int = None,
        nextToken: str = None,
        thingGroupName: str = None,
        thingGroupId: str = None,
        namespaceId: str = None
    ) -> ListJobsResponseTypeDef:
        """
        Lists jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_jobs)
        """
    def list_mitigation_actions(
        self,
        *,
        actionType: MitigationActionTypeType = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListMitigationActionsResponseTypeDef:
        """
        Gets a list of all mitigation actions that match the specified filter criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_mitigation_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_mitigation_actions)
        """
    def list_ota_updates(
        self,
        *,
        maxResults: int = None,
        nextToken: str = None,
        otaUpdateStatus: OTAUpdateStatusType = None
    ) -> ListOTAUpdatesResponseTypeDef:
        """
        Lists OTA updates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_ota_updates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_ota_updates)
        """
    def list_outgoing_certificates(
        self, *, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> ListOutgoingCertificatesResponseTypeDef:
        """
        Lists certificates that are being transferred but not yet accepted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_outgoing_certificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_outgoing_certificates)
        """
    def list_policies(
        self, *, marker: str = None, pageSize: int = None, ascendingOrder: bool = None
    ) -> ListPoliciesResponseTypeDef:
        """
        Lists your policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_policies)
        """
    def list_policy_principals(
        self,
        *,
        policyName: str,
        marker: str = None,
        pageSize: int = None,
        ascendingOrder: bool = None
    ) -> ListPolicyPrincipalsResponseTypeDef:
        """
        Lists the principals associated with the specified policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_policy_principals)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_policy_principals)
        """
    def list_policy_versions(self, *, policyName: str) -> ListPolicyVersionsResponseTypeDef:
        """
        Lists the versions of the specified policy and identifies the default version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_policy_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_policy_versions)
        """
    def list_principal_policies(
        self,
        *,
        principal: str,
        marker: str = None,
        pageSize: int = None,
        ascendingOrder: bool = None
    ) -> ListPrincipalPoliciesResponseTypeDef:
        """
        Lists the policies attached to the specified principal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_principal_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_principal_policies)
        """
    def list_principal_things(
        self, *, principal: str, nextToken: str = None, maxResults: int = None
    ) -> ListPrincipalThingsResponseTypeDef:
        """
        Lists the things associated with the specified principal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_principal_things)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_principal_things)
        """
    def list_provisioning_template_versions(
        self, *, templateName: str, maxResults: int = None, nextToken: str = None
    ) -> ListProvisioningTemplateVersionsResponseTypeDef:
        """
        A list of fleet provisioning template versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_provisioning_template_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_provisioning_template_versions)
        """
    def list_provisioning_templates(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListProvisioningTemplatesResponseTypeDef:
        """
        Lists the fleet provisioning templates in your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_provisioning_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_provisioning_templates)
        """
    def list_role_aliases(
        self, *, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> ListRoleAliasesResponseTypeDef:
        """
        Lists the role aliases registered in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_role_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_role_aliases)
        """
    def list_scheduled_audits(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListScheduledAuditsResponseTypeDef:
        """
        Lists all of your scheduled audits.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_scheduled_audits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_scheduled_audits)
        """
    def list_security_profiles(
        self,
        *,
        nextToken: str = None,
        maxResults: int = None,
        dimensionName: str = None,
        metricName: str = None
    ) -> ListSecurityProfilesResponseTypeDef:
        """
        Lists the Device Defender security profiles you've created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_security_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_security_profiles)
        """
    def list_security_profiles_for_target(
        self,
        *,
        securityProfileTargetArn: str,
        nextToken: str = None,
        maxResults: int = None,
        recursive: bool = None
    ) -> ListSecurityProfilesForTargetResponseTypeDef:
        """
        Lists the Device Defender security profiles attached to a target (thing group).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_security_profiles_for_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_security_profiles_for_target)
        """
    def list_streams(
        self, *, maxResults: int = None, nextToken: str = None, ascendingOrder: bool = None
    ) -> ListStreamsResponseTypeDef:
        """
        Lists all of the streams in your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_streams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_streams)
        """
    def list_tags_for_resource(
        self, *, resourceArn: str, nextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags (metadata) you have assigned to the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_tags_for_resource)
        """
    def list_targets_for_policy(
        self, *, policyName: str, marker: str = None, pageSize: int = None
    ) -> ListTargetsForPolicyResponseTypeDef:
        """
        List targets for the specified policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_targets_for_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_targets_for_policy)
        """
    def list_targets_for_security_profile(
        self, *, securityProfileName: str, nextToken: str = None, maxResults: int = None
    ) -> ListTargetsForSecurityProfileResponseTypeDef:
        """
        Lists the targets (thing groups) associated with a given Device Defender
        security profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_targets_for_security_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_targets_for_security_profile)
        """
    def list_thing_groups(
        self,
        *,
        nextToken: str = None,
        maxResults: int = None,
        parentGroup: str = None,
        namePrefixFilter: str = None,
        recursive: bool = None
    ) -> ListThingGroupsResponseTypeDef:
        """
        List the thing groups in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_thing_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_thing_groups)
        """
    def list_thing_groups_for_thing(
        self, *, thingName: str, nextToken: str = None, maxResults: int = None
    ) -> ListThingGroupsForThingResponseTypeDef:
        """
        List the thing groups to which the specified thing belongs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_thing_groups_for_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_thing_groups_for_thing)
        """
    def list_thing_principals(
        self, *, thingName: str, nextToken: str = None, maxResults: int = None
    ) -> ListThingPrincipalsResponseTypeDef:
        """
        Lists the principals associated with the specified thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_thing_principals)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_thing_principals)
        """
    def list_thing_registration_task_reports(
        self,
        *,
        taskId: str,
        reportType: ReportTypeType,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListThingRegistrationTaskReportsResponseTypeDef:
        """
        Information about the thing registration tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_thing_registration_task_reports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_thing_registration_task_reports)
        """
    def list_thing_registration_tasks(
        self, *, nextToken: str = None, maxResults: int = None, status: StatusType = None
    ) -> ListThingRegistrationTasksResponseTypeDef:
        """
        List bulk thing provisioning tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_thing_registration_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_thing_registration_tasks)
        """
    def list_thing_types(
        self, *, nextToken: str = None, maxResults: int = None, thingTypeName: str = None
    ) -> ListThingTypesResponseTypeDef:
        """
        Lists the existing thing types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_thing_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_thing_types)
        """
    def list_things(
        self,
        *,
        nextToken: str = None,
        maxResults: int = None,
        attributeName: str = None,
        attributeValue: str = None,
        thingTypeName: str = None,
        usePrefixAttributeValue: bool = None
    ) -> ListThingsResponseTypeDef:
        """
        Lists your things.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_things)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_things)
        """
    def list_things_in_billing_group(
        self, *, billingGroupName: str, nextToken: str = None, maxResults: int = None
    ) -> ListThingsInBillingGroupResponseTypeDef:
        """
        Lists the things you have added to the given billing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_things_in_billing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_things_in_billing_group)
        """
    def list_things_in_thing_group(
        self,
        *,
        thingGroupName: str,
        recursive: bool = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListThingsInThingGroupResponseTypeDef:
        """
        Lists the things in the specified group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_things_in_thing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_things_in_thing_group)
        """
    def list_topic_rule_destinations(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListTopicRuleDestinationsResponseTypeDef:
        """
        Lists all the topic rule destinations in your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_topic_rule_destinations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_topic_rule_destinations)
        """
    def list_topic_rules(
        self,
        *,
        topic: str = None,
        maxResults: int = None,
        nextToken: str = None,
        ruleDisabled: bool = None
    ) -> ListTopicRulesResponseTypeDef:
        """
        Lists the rules for the specific topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_topic_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_topic_rules)
        """
    def list_v2_logging_levels(
        self, *, targetType: LogTargetTypeType = None, nextToken: str = None, maxResults: int = None
    ) -> ListV2LoggingLevelsResponseTypeDef:
        """
        Lists logging levels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_v2_logging_levels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_v2_logging_levels)
        """
    def list_violation_events(
        self,
        *,
        startTime: Union[datetime, str],
        endTime: Union[datetime, str],
        thingName: str = None,
        securityProfileName: str = None,
        behaviorCriteriaType: BehaviorCriteriaTypeType = None,
        listSuppressedAlerts: bool = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListViolationEventsResponseTypeDef:
        """
        Lists the Device Defender security profile violations discovered during the
        given time period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.list_violation_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#list_violation_events)
        """
    def register_ca_certificate(
        self,
        *,
        caCertificate: str,
        verificationCertificate: str,
        setAsActive: bool = None,
        allowAutoRegistration: bool = None,
        registrationConfig: "RegistrationConfigTypeDef" = None,
        tags: List["TagTypeDef"] = None
    ) -> RegisterCACertificateResponseTypeDef:
        """
        Registers a CA certificate with AWS IoT.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.register_ca_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#register_ca_certificate)
        """
    def register_certificate(
        self,
        *,
        certificatePem: str,
        caCertificatePem: str = None,
        setAsActive: bool = None,
        status: CertificateStatusType = None
    ) -> RegisterCertificateResponseTypeDef:
        """
        Registers a device certificate with AWS IoT.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.register_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#register_certificate)
        """
    def register_certificate_without_ca(
        self, *, certificatePem: str, status: CertificateStatusType = None
    ) -> RegisterCertificateWithoutCAResponseTypeDef:
        """
        Register a certificate that does not have a certificate authority (CA).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.register_certificate_without_ca)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#register_certificate_without_ca)
        """
    def register_thing(
        self, *, templateBody: str, parameters: Dict[str, str] = None
    ) -> RegisterThingResponseTypeDef:
        """
        Provisions a thing in the device registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.register_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#register_thing)
        """
    def reject_certificate_transfer(self, *, certificateId: str, rejectReason: str = None) -> None:
        """
        Rejects a pending certificate transfer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.reject_certificate_transfer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#reject_certificate_transfer)
        """
    def remove_thing_from_billing_group(
        self,
        *,
        billingGroupName: str = None,
        billingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None
    ) -> Dict[str, Any]:
        """
        Removes the given thing from the billing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.remove_thing_from_billing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#remove_thing_from_billing_group)
        """
    def remove_thing_from_thing_group(
        self,
        *,
        thingGroupName: str = None,
        thingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None
    ) -> Dict[str, Any]:
        """
        Remove the specified thing from the specified group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.remove_thing_from_thing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#remove_thing_from_thing_group)
        """
    def replace_topic_rule(
        self, *, ruleName: str, topicRulePayload: "TopicRulePayloadTypeDef"
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.replace_topic_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#replace_topic_rule)
        """
    def search_index(
        self,
        *,
        queryString: str,
        indexName: str = None,
        nextToken: str = None,
        maxResults: int = None,
        queryVersion: str = None
    ) -> SearchIndexResponseTypeDef:
        """
        The query search index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.search_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#search_index)
        """
    def set_default_authorizer(self, *, authorizerName: str) -> SetDefaultAuthorizerResponseTypeDef:
        """
        Sets the default authorizer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.set_default_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#set_default_authorizer)
        """
    def set_default_policy_version(self, *, policyName: str, policyVersionId: str) -> None:
        """
        Sets the specified version of the specified policy as the policy's default
        (operative) version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.set_default_policy_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#set_default_policy_version)
        """
    def set_logging_options(self, *, loggingOptionsPayload: "LoggingOptionsPayloadTypeDef") -> None:
        """
        Sets the logging options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.set_logging_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#set_logging_options)
        """
    def set_v2_logging_level(
        self, *, logTarget: "LogTargetTypeDef", logLevel: LogLevelType
    ) -> None:
        """
        Sets the logging level.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.set_v2_logging_level)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#set_v2_logging_level)
        """
    def set_v2_logging_options(
        self,
        *,
        roleArn: str = None,
        defaultLogLevel: LogLevelType = None,
        disableAllLogs: bool = None
    ) -> None:
        """
        Sets the logging options for the V2 logging service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.set_v2_logging_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#set_v2_logging_options)
        """
    def start_audit_mitigation_actions_task(
        self,
        *,
        taskId: str,
        target: "AuditMitigationActionsTaskTargetTypeDef",
        auditCheckToActionsMapping: Dict[str, List[str]],
        clientRequestToken: str
    ) -> StartAuditMitigationActionsTaskResponseTypeDef:
        """
        Starts a task that applies a set of mitigation actions to the specified target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.start_audit_mitigation_actions_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#start_audit_mitigation_actions_task)
        """
    def start_detect_mitigation_actions_task(
        self,
        *,
        taskId: str,
        target: "DetectMitigationActionsTaskTargetTypeDef",
        actions: List[str],
        clientRequestToken: str,
        violationEventOccurrenceRange: "ViolationEventOccurrenceRangeTypeDef" = None,
        includeOnlyActiveViolations: bool = None,
        includeSuppressedAlerts: bool = None
    ) -> StartDetectMitigationActionsTaskResponseTypeDef:
        """
        Starts a Device Defender ML Detect mitigation actions task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.start_detect_mitigation_actions_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#start_detect_mitigation_actions_task)
        """
    def start_on_demand_audit_task(
        self, *, targetCheckNames: List[str]
    ) -> StartOnDemandAuditTaskResponseTypeDef:
        """
        Starts an on-demand Device Defender audit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.start_on_demand_audit_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#start_on_demand_audit_task)
        """
    def start_thing_registration_task(
        self, *, templateBody: str, inputFileBucket: str, inputFileKey: str, roleArn: str
    ) -> StartThingRegistrationTaskResponseTypeDef:
        """
        Creates a bulk thing provisioning task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.start_thing_registration_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#start_thing_registration_task)
        """
    def stop_thing_registration_task(self, *, taskId: str) -> Dict[str, Any]:
        """
        Cancels a bulk thing provisioning task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.stop_thing_registration_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#stop_thing_registration_task)
        """
    def tag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds to or modifies the tags of the given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#tag_resource)
        """
    def test_authorization(
        self,
        *,
        authInfos: List["AuthInfoTypeDef"],
        principal: str = None,
        cognitoIdentityPoolId: str = None,
        clientId: str = None,
        policyNamesToAdd: List[str] = None,
        policyNamesToSkip: List[str] = None
    ) -> TestAuthorizationResponseTypeDef:
        """
        Tests if a specified principal is authorized to perform an AWS IoT action on a
        specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.test_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#test_authorization)
        """
    def test_invoke_authorizer(
        self,
        *,
        authorizerName: str,
        token: str = None,
        tokenSignature: str = None,
        httpContext: "HttpContextTypeDef" = None,
        mqttContext: "MqttContextTypeDef" = None,
        tlsContext: "TlsContextTypeDef" = None
    ) -> TestInvokeAuthorizerResponseTypeDef:
        """
        Tests a custom authorization behavior by invoking a specified custom authorizer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.test_invoke_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#test_invoke_authorizer)
        """
    def transfer_certificate(
        self, *, certificateId: str, targetAwsAccount: str, transferMessage: str = None
    ) -> TransferCertificateResponseTypeDef:
        """
        Transfers the specified certificate to the specified AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.transfer_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#transfer_certificate)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the given tags (metadata) from the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#untag_resource)
        """
    def update_account_audit_configuration(
        self,
        *,
        roleArn: str = None,
        auditNotificationTargetConfigurations: Dict[
            Literal["SNS"], "AuditNotificationTargetTypeDef"
        ] = None,
        auditCheckConfigurations: Dict[str, "AuditCheckConfigurationTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Configures or reconfigures the Device Defender audit settings for this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.update_account_audit_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update_account_audit_configuration)
        """
    def update_audit_suppression(
        self,
        *,
        checkName: str,
        resourceIdentifier: "ResourceIdentifierTypeDef",
        expirationDate: Union[datetime, str] = None,
        suppressIndefinitely: bool = None,
        description: str = None
    ) -> Dict[str, Any]:
        """
        Updates a Device Defender audit suppression.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.update_audit_suppression)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update_audit_suppression)
        """
    def update_authorizer(
        self,
        *,
        authorizerName: str,
        authorizerFunctionArn: str = None,
        tokenKeyName: str = None,
        tokenSigningPublicKeys: Dict[str, str] = None,
        status: AuthorizerStatusType = None
    ) -> UpdateAuthorizerResponseTypeDef:
        """
        Updates an authorizer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.update_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update_authorizer)
        """
    def update_billing_group(
        self,
        *,
        billingGroupName: str,
        billingGroupProperties: "BillingGroupPropertiesTypeDef",
        expectedVersion: int = None
    ) -> UpdateBillingGroupResponseTypeDef:
        """
        Updates information about the billing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.update_billing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update_billing_group)
        """
    def update_ca_certificate(
        self,
        *,
        certificateId: str,
        newStatus: CACertificateStatusType = None,
        newAutoRegistrationStatus: AutoRegistrationStatusType = None,
        registrationConfig: "RegistrationConfigTypeDef" = None,
        removeAutoRegistration: bool = None
    ) -> None:
        """
        Updates a registered CA certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.update_ca_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update_ca_certificate)
        """
    def update_certificate(self, *, certificateId: str, newStatus: CertificateStatusType) -> None:
        """
        Updates the status of the specified certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.update_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update_certificate)
        """
    def update_custom_metric(
        self, *, metricName: str, displayName: str
    ) -> UpdateCustomMetricResponseTypeDef:
        """
        Updates a Device Defender detect custom metric.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.update_custom_metric)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update_custom_metric)
        """
    def update_dimension(
        self, *, name: str, stringValues: List[str]
    ) -> UpdateDimensionResponseTypeDef:
        """
        Updates the definition for a dimension.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.update_dimension)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update_dimension)
        """
    def update_domain_configuration(
        self,
        *,
        domainConfigurationName: str,
        authorizerConfig: "AuthorizerConfigTypeDef" = None,
        domainConfigurationStatus: DomainConfigurationStatusType = None,
        removeAuthorizerConfig: bool = None
    ) -> UpdateDomainConfigurationResponseTypeDef:
        """
        Updates values stored in the domain configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.update_domain_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update_domain_configuration)
        """
    def update_dynamic_thing_group(
        self,
        *,
        thingGroupName: str,
        thingGroupProperties: "ThingGroupPropertiesTypeDef",
        expectedVersion: int = None,
        indexName: str = None,
        queryString: str = None,
        queryVersion: str = None
    ) -> UpdateDynamicThingGroupResponseTypeDef:
        """
        Updates a dynamic thing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.update_dynamic_thing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update_dynamic_thing_group)
        """
    def update_event_configurations(
        self, *, eventConfigurations: Dict[EventTypeType, "ConfigurationTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Updates the event configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.update_event_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update_event_configurations)
        """
    def update_indexing_configuration(
        self,
        *,
        thingIndexingConfiguration: "ThingIndexingConfigurationTypeDef" = None,
        thingGroupIndexingConfiguration: "ThingGroupIndexingConfigurationTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates the search configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.update_indexing_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update_indexing_configuration)
        """
    def update_job(
        self,
        *,
        jobId: str,
        description: str = None,
        presignedUrlConfig: "PresignedUrlConfigTypeDef" = None,
        jobExecutionsRolloutConfig: "JobExecutionsRolloutConfigTypeDef" = None,
        abortConfig: "AbortConfigTypeDef" = None,
        timeoutConfig: "TimeoutConfigTypeDef" = None,
        namespaceId: str = None
    ) -> None:
        """
        Updates supported fields of the specified job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.update_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update_job)
        """
    def update_mitigation_action(
        self,
        *,
        actionName: str,
        roleArn: str = None,
        actionParams: "MitigationActionParamsTypeDef" = None
    ) -> UpdateMitigationActionResponseTypeDef:
        """
        Updates the definition for the specified mitigation action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.update_mitigation_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update_mitigation_action)
        """
    def update_provisioning_template(
        self,
        *,
        templateName: str,
        description: str = None,
        enabled: bool = None,
        defaultVersionId: int = None,
        provisioningRoleArn: str = None,
        preProvisioningHook: "ProvisioningHookTypeDef" = None,
        removePreProvisioningHook: bool = None
    ) -> Dict[str, Any]:
        """
        Updates a fleet provisioning template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.update_provisioning_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update_provisioning_template)
        """
    def update_role_alias(
        self, *, roleAlias: str, roleArn: str = None, credentialDurationSeconds: int = None
    ) -> UpdateRoleAliasResponseTypeDef:
        """
        Updates a role alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.update_role_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update_role_alias)
        """
    def update_scheduled_audit(
        self,
        *,
        scheduledAuditName: str,
        frequency: AuditFrequencyType = None,
        dayOfMonth: str = None,
        dayOfWeek: DayOfWeekType = None,
        targetCheckNames: List[str] = None
    ) -> UpdateScheduledAuditResponseTypeDef:
        """
        Updates a scheduled audit, including which checks are performed and how often
        the audit takes place.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.update_scheduled_audit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update_scheduled_audit)
        """
    def update_security_profile(
        self,
        *,
        securityProfileName: str,
        securityProfileDescription: str = None,
        behaviors: List["BehaviorTypeDef"] = None,
        alertTargets: Dict[Literal["SNS"], "AlertTargetTypeDef"] = None,
        additionalMetricsToRetain: List[str] = None,
        additionalMetricsToRetainV2: List["MetricToRetainTypeDef"] = None,
        deleteBehaviors: bool = None,
        deleteAlertTargets: bool = None,
        deleteAdditionalMetricsToRetain: bool = None,
        expectedVersion: int = None
    ) -> UpdateSecurityProfileResponseTypeDef:
        """
        Updates a Device Defender security profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.update_security_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update_security_profile)
        """
    def update_stream(
        self,
        *,
        streamId: str,
        description: str = None,
        files: List["StreamFileTypeDef"] = None,
        roleArn: str = None
    ) -> UpdateStreamResponseTypeDef:
        """
        Updates an existing stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.update_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update_stream)
        """
    def update_thing(
        self,
        *,
        thingName: str,
        thingTypeName: str = None,
        attributePayload: "AttributePayloadTypeDef" = None,
        expectedVersion: int = None,
        removeThingType: bool = None
    ) -> Dict[str, Any]:
        """
        Updates the data for a thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.update_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update_thing)
        """
    def update_thing_group(
        self,
        *,
        thingGroupName: str,
        thingGroupProperties: "ThingGroupPropertiesTypeDef",
        expectedVersion: int = None
    ) -> UpdateThingGroupResponseTypeDef:
        """
        Update a thing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.update_thing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update_thing_group)
        """
    def update_thing_groups_for_thing(
        self,
        *,
        thingName: str = None,
        thingGroupsToAdd: List[str] = None,
        thingGroupsToRemove: List[str] = None,
        overrideDynamicGroups: bool = None
    ) -> Dict[str, Any]:
        """
        Updates the groups to which the thing belongs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.update_thing_groups_for_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update_thing_groups_for_thing)
        """
    def update_topic_rule_destination(
        self, *, arn: str, status: TopicRuleDestinationStatusType
    ) -> Dict[str, Any]:
        """
        Updates a topic rule destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.update_topic_rule_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#update_topic_rule_destination)
        """
    def validate_security_profile_behaviors(
        self, *, behaviors: List["BehaviorTypeDef"]
    ) -> ValidateSecurityProfileBehaviorsResponseTypeDef:
        """
        Validates a Device Defender security profile behaviors specification.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Client.validate_security_profile_behaviors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/client.html#validate_security_profile_behaviors)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_behavior_model_training_summaries"]
    ) -> GetBehaviorModelTrainingSummariesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.GetBehaviorModelTrainingSummaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#getbehaviormodeltrainingsummariespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_active_violations"]
    ) -> ListActiveViolationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListActiveViolations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listactiveviolationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_attached_policies"]
    ) -> ListAttachedPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListAttachedPolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listattachedpoliciespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_audit_findings"]
    ) -> ListAuditFindingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListAuditFindings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listauditfindingspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_audit_mitigation_actions_executions"]
    ) -> ListAuditMitigationActionsExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListAuditMitigationActionsExecutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listauditmitigationactionsexecutionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_audit_mitigation_actions_tasks"]
    ) -> ListAuditMitigationActionsTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListAuditMitigationActionsTasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listauditmitigationactionstaskspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_audit_suppressions"]
    ) -> ListAuditSuppressionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListAuditSuppressions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listauditsuppressionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_audit_tasks"]) -> ListAuditTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListAuditTasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listaudittaskspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_authorizers"]
    ) -> ListAuthorizersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListAuthorizers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listauthorizerspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_billing_groups"]
    ) -> ListBillingGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListBillingGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listbillinggroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_ca_certificates"]
    ) -> ListCACertificatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListCACertificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listcacertificatespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_certificates"]
    ) -> ListCertificatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListCertificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listcertificatespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_certificates_by_ca"]
    ) -> ListCertificatesByCAPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListCertificatesByCA)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listcertificatesbycapaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_metrics"]
    ) -> ListCustomMetricsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListCustomMetrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listcustommetricspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_detect_mitigation_actions_executions"]
    ) -> ListDetectMitigationActionsExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListDetectMitigationActionsExecutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listdetectmitigationactionsexecutionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_detect_mitigation_actions_tasks"]
    ) -> ListDetectMitigationActionsTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListDetectMitigationActionsTasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listdetectmitigationactionstaskspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_dimensions"]) -> ListDimensionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListDimensions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listdimensionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_domain_configurations"]
    ) -> ListDomainConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListDomainConfigurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listdomainconfigurationspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_indices"]) -> ListIndicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListIndices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listindicespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_job_executions_for_job"]
    ) -> ListJobExecutionsForJobPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForJob)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listjobexecutionsforjobpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_job_executions_for_thing"]
    ) -> ListJobExecutionsForThingPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForThing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listjobexecutionsforthingpaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_mitigation_actions"]
    ) -> ListMitigationActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListMitigationActions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listmitigationactionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_ota_updates"]) -> ListOTAUpdatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListOTAUpdates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listotaupdatespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_outgoing_certificates"]
    ) -> ListOutgoingCertificatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListOutgoingCertificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listoutgoingcertificatespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_policies"]) -> ListPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListPolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listpoliciespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_policy_principals"]
    ) -> ListPolicyPrincipalsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListPolicyPrincipals)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listpolicyprincipalspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_principal_policies"]
    ) -> ListPrincipalPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListPrincipalPolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listprincipalpoliciespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_principal_things"]
    ) -> ListPrincipalThingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListPrincipalThings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listprincipalthingspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_provisioning_template_versions"]
    ) -> ListProvisioningTemplateVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListProvisioningTemplateVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listprovisioningtemplateversionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_provisioning_templates"]
    ) -> ListProvisioningTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListProvisioningTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listprovisioningtemplatespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_role_aliases"]
    ) -> ListRoleAliasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListRoleAliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listrolealiasespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_scheduled_audits"]
    ) -> ListScheduledAuditsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListScheduledAudits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listscheduledauditspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_profiles"]
    ) -> ListSecurityProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListSecurityProfiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listsecurityprofilespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_profiles_for_target"]
    ) -> ListSecurityProfilesForTargetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListSecurityProfilesForTarget)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listsecurityprofilesfortargetpaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_streams"]) -> ListStreamsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListStreams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#liststreamspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListTagsForResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listtagsforresourcepaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_targets_for_policy"]
    ) -> ListTargetsForPolicyPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListTargetsForPolicy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listtargetsforpolicypaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_targets_for_security_profile"]
    ) -> ListTargetsForSecurityProfilePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListTargetsForSecurityProfile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listtargetsforsecurityprofilepaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_thing_groups"]
    ) -> ListThingGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListThingGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthinggroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_thing_groups_for_thing"]
    ) -> ListThingGroupsForThingPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListThingGroupsForThing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthinggroupsforthingpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_thing_principals"]
    ) -> ListThingPrincipalsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListThingPrincipals)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingprincipalspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_thing_registration_task_reports"]
    ) -> ListThingRegistrationTaskReportsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListThingRegistrationTaskReports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingregistrationtaskreportspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_thing_registration_tasks"]
    ) -> ListThingRegistrationTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListThingRegistrationTasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingregistrationtaskspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_thing_types"]) -> ListThingTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListThingTypes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingtypespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_things"]) -> ListThingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListThings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_things_in_billing_group"]
    ) -> ListThingsInBillingGroupPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListThingsInBillingGroup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingsinbillinggrouppaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_things_in_thing_group"]
    ) -> ListThingsInThingGroupPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListThingsInThingGroup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingsinthinggrouppaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_topic_rule_destinations"]
    ) -> ListTopicRuleDestinationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListTopicRuleDestinations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listtopicruledestinationspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_topic_rules"]) -> ListTopicRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListTopicRules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listtopicrulespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_v2_logging_levels"]
    ) -> ListV2LoggingLevelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListV2LoggingLevels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listv2logginglevelspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_violation_events"]
    ) -> ListViolationEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iot.html#IoT.Paginator.ListViolationEvents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listviolationeventspaginator)
        """
