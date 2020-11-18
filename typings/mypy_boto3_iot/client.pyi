# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for iot service client

Usage::

    ```python
    import boto3
    from mypy_boto3_iot import IoTClient

    client: IoTClient = boto3.client("iot")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_iot.paginator import (
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
from mypy_boto3_iot.type_defs import (
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
    CreateDimensionResponseTypeDef,
    CreateDomainConfigurationResponseTypeDef,
    CreateDynamicThingGroupResponseTypeDef,
    CreateJobResponseTypeDef,
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
    DescribeDefaultAuthorizerResponseTypeDef,
    DescribeDimensionResponseTypeDef,
    DescribeDomainConfigurationResponseTypeDef,
    DescribeEndpointResponseTypeDef,
    DescribeEventConfigurationsResponseTypeDef,
    DescribeIndexResponseTypeDef,
    DescribeJobExecutionResponseTypeDef,
    DescribeJobResponseTypeDef,
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
    ListDimensionsResponseTypeDef,
    ListDomainConfigurationsResponseTypeDef,
    ListIndicesResponseTypeDef,
    ListJobExecutionsForJobResponseTypeDef,
    ListJobExecutionsForThingResponseTypeDef,
    ListJobsResponseTypeDef,
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


class IoTClient:
    """
    [IoT.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_certificate_transfer(self, certificateId: str, setAsActive: bool = None) -> None:
        """
        [Client.accept_certificate_transfer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.accept_certificate_transfer)
        """

    def add_thing_to_billing_group(
        self,
        billingGroupName: str = None,
        billingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.add_thing_to_billing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.add_thing_to_billing_group)
        """

    def add_thing_to_thing_group(
        self,
        thingGroupName: str = None,
        thingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None,
        overrideDynamicGroups: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.add_thing_to_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.add_thing_to_thing_group)
        """

    def associate_targets_with_job(
        self, targets: List[str], jobId: str, comment: str = None, namespaceId: str = None
    ) -> AssociateTargetsWithJobResponseTypeDef:
        """
        [Client.associate_targets_with_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.associate_targets_with_job)
        """

    def attach_policy(self, policyName: str, target: str) -> None:
        """
        [Client.attach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.attach_policy)
        """

    def attach_principal_policy(self, policyName: str, principal: str) -> None:
        """
        [Client.attach_principal_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.attach_principal_policy)
        """

    def attach_security_profile(
        self, securityProfileName: str, securityProfileTargetArn: str
    ) -> Dict[str, Any]:
        """
        [Client.attach_security_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.attach_security_profile)
        """

    def attach_thing_principal(self, thingName: str, principal: str) -> Dict[str, Any]:
        """
        [Client.attach_thing_principal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.attach_thing_principal)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.can_paginate)
        """

    def cancel_audit_mitigation_actions_task(self, taskId: str) -> Dict[str, Any]:
        """
        [Client.cancel_audit_mitigation_actions_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.cancel_audit_mitigation_actions_task)
        """

    def cancel_audit_task(self, taskId: str) -> Dict[str, Any]:
        """
        [Client.cancel_audit_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.cancel_audit_task)
        """

    def cancel_certificate_transfer(self, certificateId: str) -> None:
        """
        [Client.cancel_certificate_transfer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.cancel_certificate_transfer)
        """

    def cancel_job(
        self, jobId: str, reasonCode: str = None, comment: str = None, force: bool = None
    ) -> CancelJobResponseTypeDef:
        """
        [Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.cancel_job)
        """

    def cancel_job_execution(
        self,
        jobId: str,
        thingName: str,
        force: bool = None,
        expectedVersion: int = None,
        statusDetails: Dict[str, str] = None,
    ) -> None:
        """
        [Client.cancel_job_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.cancel_job_execution)
        """

    def clear_default_authorizer(self) -> Dict[str, Any]:
        """
        [Client.clear_default_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.clear_default_authorizer)
        """

    def confirm_topic_rule_destination(self, confirmationToken: str) -> Dict[str, Any]:
        """
        [Client.confirm_topic_rule_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.confirm_topic_rule_destination)
        """

    def create_audit_suppression(
        self,
        checkName: str,
        resourceIdentifier: "ResourceIdentifierTypeDef",
        clientRequestToken: str,
        expirationDate: datetime = None,
        suppressIndefinitely: bool = None,
        description: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_audit_suppression documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_audit_suppression)
        """

    def create_authorizer(
        self,
        authorizerName: str,
        authorizerFunctionArn: str,
        tokenKeyName: str = None,
        tokenSigningPublicKeys: Dict[str, str] = None,
        status: Literal["ACTIVE", "INACTIVE"] = None,
        tags: List["TagTypeDef"] = None,
        signingDisabled: bool = None,
    ) -> CreateAuthorizerResponseTypeDef:
        """
        [Client.create_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_authorizer)
        """

    def create_billing_group(
        self,
        billingGroupName: str,
        billingGroupProperties: "BillingGroupPropertiesTypeDef" = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateBillingGroupResponseTypeDef:
        """
        [Client.create_billing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_billing_group)
        """

    def create_certificate_from_csr(
        self, certificateSigningRequest: str, setAsActive: bool = None
    ) -> CreateCertificateFromCsrResponseTypeDef:
        """
        [Client.create_certificate_from_csr documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_certificate_from_csr)
        """

    def create_dimension(
        self,
        name: str,
        type: Literal["TOPIC_FILTER"],
        stringValues: List[str],
        clientRequestToken: str,
        tags: List["TagTypeDef"] = None,
    ) -> CreateDimensionResponseTypeDef:
        """
        [Client.create_dimension documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_dimension)
        """

    def create_domain_configuration(
        self,
        domainConfigurationName: str,
        domainName: str = None,
        serverCertificateArns: List[str] = None,
        validationCertificateArn: str = None,
        authorizerConfig: "AuthorizerConfigTypeDef" = None,
        serviceType: Literal["DATA", "CREDENTIAL_PROVIDER", "JOBS"] = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateDomainConfigurationResponseTypeDef:
        """
        [Client.create_domain_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_domain_configuration)
        """

    def create_dynamic_thing_group(
        self,
        thingGroupName: str,
        queryString: str,
        thingGroupProperties: "ThingGroupPropertiesTypeDef" = None,
        indexName: str = None,
        queryVersion: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateDynamicThingGroupResponseTypeDef:
        """
        [Client.create_dynamic_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_dynamic_thing_group)
        """

    def create_job(
        self,
        jobId: str,
        targets: List[str],
        documentSource: str = None,
        document: str = None,
        description: str = None,
        presignedUrlConfig: "PresignedUrlConfigTypeDef" = None,
        targetSelection: Literal["CONTINUOUS", "SNAPSHOT"] = None,
        jobExecutionsRolloutConfig: "JobExecutionsRolloutConfigTypeDef" = None,
        abortConfig: "AbortConfigTypeDef" = None,
        timeoutConfig: "TimeoutConfigTypeDef" = None,
        tags: List["TagTypeDef"] = None,
        namespaceId: str = None,
    ) -> CreateJobResponseTypeDef:
        """
        [Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_job)
        """

    def create_keys_and_certificate(
        self, setAsActive: bool = None
    ) -> CreateKeysAndCertificateResponseTypeDef:
        """
        [Client.create_keys_and_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_keys_and_certificate)
        """

    def create_mitigation_action(
        self,
        actionName: str,
        roleArn: str,
        actionParams: "MitigationActionParamsTypeDef",
        tags: List["TagTypeDef"] = None,
    ) -> CreateMitigationActionResponseTypeDef:
        """
        [Client.create_mitigation_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_mitigation_action)
        """

    def create_ota_update(
        self,
        otaUpdateId: str,
        targets: List[str],
        files: List["OTAUpdateFileTypeDef"],
        roleArn: str,
        description: str = None,
        protocols: List[Literal["MQTT", "HTTP"]] = None,
        targetSelection: Literal["CONTINUOUS", "SNAPSHOT"] = None,
        awsJobExecutionsRolloutConfig: "AwsJobExecutionsRolloutConfigTypeDef" = None,
        awsJobPresignedUrlConfig: "AwsJobPresignedUrlConfigTypeDef" = None,
        awsJobAbortConfig: AwsJobAbortConfigTypeDef = None,
        awsJobTimeoutConfig: AwsJobTimeoutConfigTypeDef = None,
        additionalParameters: Dict[str, str] = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateOTAUpdateResponseTypeDef:
        """
        [Client.create_ota_update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_ota_update)
        """

    def create_policy(
        self, policyName: str, policyDocument: str, tags: List["TagTypeDef"] = None
    ) -> CreatePolicyResponseTypeDef:
        """
        [Client.create_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_policy)
        """

    def create_policy_version(
        self, policyName: str, policyDocument: str, setAsDefault: bool = None
    ) -> CreatePolicyVersionResponseTypeDef:
        """
        [Client.create_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_policy_version)
        """

    def create_provisioning_claim(
        self, templateName: str
    ) -> CreateProvisioningClaimResponseTypeDef:
        """
        [Client.create_provisioning_claim documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_provisioning_claim)
        """

    def create_provisioning_template(
        self,
        templateName: str,
        templateBody: str,
        provisioningRoleArn: str,
        description: str = None,
        enabled: bool = None,
        preProvisioningHook: "ProvisioningHookTypeDef" = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateProvisioningTemplateResponseTypeDef:
        """
        [Client.create_provisioning_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_provisioning_template)
        """

    def create_provisioning_template_version(
        self, templateName: str, templateBody: str, setAsDefault: bool = None
    ) -> CreateProvisioningTemplateVersionResponseTypeDef:
        """
        [Client.create_provisioning_template_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_provisioning_template_version)
        """

    def create_role_alias(
        self,
        roleAlias: str,
        roleArn: str,
        credentialDurationSeconds: int = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateRoleAliasResponseTypeDef:
        """
        [Client.create_role_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_role_alias)
        """

    def create_scheduled_audit(
        self,
        frequency: Literal["DAILY", "WEEKLY", "BIWEEKLY", "MONTHLY"],
        targetCheckNames: List[str],
        scheduledAuditName: str,
        dayOfMonth: str = None,
        dayOfWeek: Literal["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"] = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateScheduledAuditResponseTypeDef:
        """
        [Client.create_scheduled_audit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_scheduled_audit)
        """

    def create_security_profile(
        self,
        securityProfileName: str,
        securityProfileDescription: str = None,
        behaviors: List["BehaviorTypeDef"] = None,
        alertTargets: Dict[Literal["SNS"], "AlertTargetTypeDef"] = None,
        additionalMetricsToRetain: List[str] = None,
        additionalMetricsToRetainV2: List["MetricToRetainTypeDef"] = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateSecurityProfileResponseTypeDef:
        """
        [Client.create_security_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_security_profile)
        """

    def create_stream(
        self,
        streamId: str,
        files: List["StreamFileTypeDef"],
        roleArn: str,
        description: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateStreamResponseTypeDef:
        """
        [Client.create_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_stream)
        """

    def create_thing(
        self,
        thingName: str,
        thingTypeName: str = None,
        attributePayload: "AttributePayloadTypeDef" = None,
        billingGroupName: str = None,
    ) -> CreateThingResponseTypeDef:
        """
        [Client.create_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_thing)
        """

    def create_thing_group(
        self,
        thingGroupName: str,
        parentGroupName: str = None,
        thingGroupProperties: "ThingGroupPropertiesTypeDef" = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateThingGroupResponseTypeDef:
        """
        [Client.create_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_thing_group)
        """

    def create_thing_type(
        self,
        thingTypeName: str,
        thingTypeProperties: "ThingTypePropertiesTypeDef" = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateThingTypeResponseTypeDef:
        """
        [Client.create_thing_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_thing_type)
        """

    def create_topic_rule(
        self, ruleName: str, topicRulePayload: TopicRulePayloadTypeDef, tags: str = None
    ) -> None:
        """
        [Client.create_topic_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_topic_rule)
        """

    def create_topic_rule_destination(
        self, destinationConfiguration: TopicRuleDestinationConfigurationTypeDef
    ) -> CreateTopicRuleDestinationResponseTypeDef:
        """
        [Client.create_topic_rule_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.create_topic_rule_destination)
        """

    def delete_account_audit_configuration(
        self, deleteScheduledAudits: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_account_audit_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_account_audit_configuration)
        """

    def delete_audit_suppression(
        self, checkName: str, resourceIdentifier: "ResourceIdentifierTypeDef"
    ) -> Dict[str, Any]:
        """
        [Client.delete_audit_suppression documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_audit_suppression)
        """

    def delete_authorizer(self, authorizerName: str) -> Dict[str, Any]:
        """
        [Client.delete_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_authorizer)
        """

    def delete_billing_group(
        self, billingGroupName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_billing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_billing_group)
        """

    def delete_ca_certificate(self, certificateId: str) -> Dict[str, Any]:
        """
        [Client.delete_ca_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_ca_certificate)
        """

    def delete_certificate(self, certificateId: str, forceDelete: bool = None) -> None:
        """
        [Client.delete_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_certificate)
        """

    def delete_dimension(self, name: str) -> Dict[str, Any]:
        """
        [Client.delete_dimension documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_dimension)
        """

    def delete_domain_configuration(self, domainConfigurationName: str) -> Dict[str, Any]:
        """
        [Client.delete_domain_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_domain_configuration)
        """

    def delete_dynamic_thing_group(
        self, thingGroupName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_dynamic_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_dynamic_thing_group)
        """

    def delete_job(self, jobId: str, force: bool = None, namespaceId: str = None) -> None:
        """
        [Client.delete_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_job)
        """

    def delete_job_execution(
        self,
        jobId: str,
        thingName: str,
        executionNumber: int,
        force: bool = None,
        namespaceId: str = None,
    ) -> None:
        """
        [Client.delete_job_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_job_execution)
        """

    def delete_mitigation_action(self, actionName: str) -> Dict[str, Any]:
        """
        [Client.delete_mitigation_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_mitigation_action)
        """

    def delete_ota_update(
        self, otaUpdateId: str, deleteStream: bool = None, forceDeleteAWSJob: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_ota_update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_ota_update)
        """

    def delete_policy(self, policyName: str) -> None:
        """
        [Client.delete_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_policy)
        """

    def delete_policy_version(self, policyName: str, policyVersionId: str) -> None:
        """
        [Client.delete_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_policy_version)
        """

    def delete_provisioning_template(self, templateName: str) -> Dict[str, Any]:
        """
        [Client.delete_provisioning_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_provisioning_template)
        """

    def delete_provisioning_template_version(
        self, templateName: str, versionId: int
    ) -> Dict[str, Any]:
        """
        [Client.delete_provisioning_template_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_provisioning_template_version)
        """

    def delete_registration_code(self) -> Dict[str, Any]:
        """
        [Client.delete_registration_code documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_registration_code)
        """

    def delete_role_alias(self, roleAlias: str) -> Dict[str, Any]:
        """
        [Client.delete_role_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_role_alias)
        """

    def delete_scheduled_audit(self, scheduledAuditName: str) -> Dict[str, Any]:
        """
        [Client.delete_scheduled_audit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_scheduled_audit)
        """

    def delete_security_profile(
        self, securityProfileName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_security_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_security_profile)
        """

    def delete_stream(self, streamId: str) -> Dict[str, Any]:
        """
        [Client.delete_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_stream)
        """

    def delete_thing(self, thingName: str, expectedVersion: int = None) -> Dict[str, Any]:
        """
        [Client.delete_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_thing)
        """

    def delete_thing_group(
        self, thingGroupName: str, expectedVersion: int = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_thing_group)
        """

    def delete_thing_type(self, thingTypeName: str) -> Dict[str, Any]:
        """
        [Client.delete_thing_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_thing_type)
        """

    def delete_topic_rule(self, ruleName: str) -> None:
        """
        [Client.delete_topic_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_topic_rule)
        """

    def delete_topic_rule_destination(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_topic_rule_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_topic_rule_destination)
        """

    def delete_v2_logging_level(
        self, targetType: Literal["DEFAULT", "THING_GROUP"], targetName: str
    ) -> None:
        """
        [Client.delete_v2_logging_level documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.delete_v2_logging_level)
        """

    def deprecate_thing_type(
        self, thingTypeName: str, undoDeprecate: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.deprecate_thing_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.deprecate_thing_type)
        """

    def describe_account_audit_configuration(
        self,
    ) -> DescribeAccountAuditConfigurationResponseTypeDef:
        """
        [Client.describe_account_audit_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_account_audit_configuration)
        """

    def describe_audit_finding(self, findingId: str) -> DescribeAuditFindingResponseTypeDef:
        """
        [Client.describe_audit_finding documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_audit_finding)
        """

    def describe_audit_mitigation_actions_task(
        self, taskId: str
    ) -> DescribeAuditMitigationActionsTaskResponseTypeDef:
        """
        [Client.describe_audit_mitigation_actions_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_audit_mitigation_actions_task)
        """

    def describe_audit_suppression(
        self, checkName: str, resourceIdentifier: "ResourceIdentifierTypeDef"
    ) -> DescribeAuditSuppressionResponseTypeDef:
        """
        [Client.describe_audit_suppression documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_audit_suppression)
        """

    def describe_audit_task(self, taskId: str) -> DescribeAuditTaskResponseTypeDef:
        """
        [Client.describe_audit_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_audit_task)
        """

    def describe_authorizer(self, authorizerName: str) -> DescribeAuthorizerResponseTypeDef:
        """
        [Client.describe_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_authorizer)
        """

    def describe_billing_group(self, billingGroupName: str) -> DescribeBillingGroupResponseTypeDef:
        """
        [Client.describe_billing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_billing_group)
        """

    def describe_ca_certificate(self, certificateId: str) -> DescribeCACertificateResponseTypeDef:
        """
        [Client.describe_ca_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_ca_certificate)
        """

    def describe_certificate(self, certificateId: str) -> DescribeCertificateResponseTypeDef:
        """
        [Client.describe_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_certificate)
        """

    def describe_default_authorizer(self) -> DescribeDefaultAuthorizerResponseTypeDef:
        """
        [Client.describe_default_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_default_authorizer)
        """

    def describe_dimension(self, name: str) -> DescribeDimensionResponseTypeDef:
        """
        [Client.describe_dimension documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_dimension)
        """

    def describe_domain_configuration(
        self, domainConfigurationName: str
    ) -> DescribeDomainConfigurationResponseTypeDef:
        """
        [Client.describe_domain_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_domain_configuration)
        """

    def describe_endpoint(self, endpointType: str = None) -> DescribeEndpointResponseTypeDef:
        """
        [Client.describe_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_endpoint)
        """

    def describe_event_configurations(self) -> DescribeEventConfigurationsResponseTypeDef:
        """
        [Client.describe_event_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_event_configurations)
        """

    def describe_index(self, indexName: str) -> DescribeIndexResponseTypeDef:
        """
        [Client.describe_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_index)
        """

    def describe_job(self, jobId: str) -> DescribeJobResponseTypeDef:
        """
        [Client.describe_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_job)
        """

    def describe_job_execution(
        self, jobId: str, thingName: str, executionNumber: int = None
    ) -> DescribeJobExecutionResponseTypeDef:
        """
        [Client.describe_job_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_job_execution)
        """

    def describe_mitigation_action(
        self, actionName: str
    ) -> DescribeMitigationActionResponseTypeDef:
        """
        [Client.describe_mitigation_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_mitigation_action)
        """

    def describe_provisioning_template(
        self, templateName: str
    ) -> DescribeProvisioningTemplateResponseTypeDef:
        """
        [Client.describe_provisioning_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_provisioning_template)
        """

    def describe_provisioning_template_version(
        self, templateName: str, versionId: int
    ) -> DescribeProvisioningTemplateVersionResponseTypeDef:
        """
        [Client.describe_provisioning_template_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_provisioning_template_version)
        """

    def describe_role_alias(self, roleAlias: str) -> DescribeRoleAliasResponseTypeDef:
        """
        [Client.describe_role_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_role_alias)
        """

    def describe_scheduled_audit(
        self, scheduledAuditName: str
    ) -> DescribeScheduledAuditResponseTypeDef:
        """
        [Client.describe_scheduled_audit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_scheduled_audit)
        """

    def describe_security_profile(
        self, securityProfileName: str
    ) -> DescribeSecurityProfileResponseTypeDef:
        """
        [Client.describe_security_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_security_profile)
        """

    def describe_stream(self, streamId: str) -> DescribeStreamResponseTypeDef:
        """
        [Client.describe_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_stream)
        """

    def describe_thing(self, thingName: str) -> DescribeThingResponseTypeDef:
        """
        [Client.describe_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_thing)
        """

    def describe_thing_group(self, thingGroupName: str) -> DescribeThingGroupResponseTypeDef:
        """
        [Client.describe_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_thing_group)
        """

    def describe_thing_registration_task(
        self, taskId: str
    ) -> DescribeThingRegistrationTaskResponseTypeDef:
        """
        [Client.describe_thing_registration_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_thing_registration_task)
        """

    def describe_thing_type(self, thingTypeName: str) -> DescribeThingTypeResponseTypeDef:
        """
        [Client.describe_thing_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.describe_thing_type)
        """

    def detach_policy(self, policyName: str, target: str) -> None:
        """
        [Client.detach_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.detach_policy)
        """

    def detach_principal_policy(self, policyName: str, principal: str) -> None:
        """
        [Client.detach_principal_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.detach_principal_policy)
        """

    def detach_security_profile(
        self, securityProfileName: str, securityProfileTargetArn: str
    ) -> Dict[str, Any]:
        """
        [Client.detach_security_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.detach_security_profile)
        """

    def detach_thing_principal(self, thingName: str, principal: str) -> Dict[str, Any]:
        """
        [Client.detach_thing_principal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.detach_thing_principal)
        """

    def disable_topic_rule(self, ruleName: str) -> None:
        """
        [Client.disable_topic_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.disable_topic_rule)
        """

    def enable_topic_rule(self, ruleName: str) -> None:
        """
        [Client.enable_topic_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.enable_topic_rule)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.generate_presigned_url)
        """

    def get_cardinality(
        self,
        queryString: str,
        indexName: str = None,
        aggregationField: str = None,
        queryVersion: str = None,
    ) -> GetCardinalityResponseTypeDef:
        """
        [Client.get_cardinality documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.get_cardinality)
        """

    def get_effective_policies(
        self, principal: str = None, cognitoIdentityPoolId: str = None, thingName: str = None
    ) -> GetEffectivePoliciesResponseTypeDef:
        """
        [Client.get_effective_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.get_effective_policies)
        """

    def get_indexing_configuration(self) -> GetIndexingConfigurationResponseTypeDef:
        """
        [Client.get_indexing_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.get_indexing_configuration)
        """

    def get_job_document(self, jobId: str) -> GetJobDocumentResponseTypeDef:
        """
        [Client.get_job_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.get_job_document)
        """

    def get_logging_options(self) -> GetLoggingOptionsResponseTypeDef:
        """
        [Client.get_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.get_logging_options)
        """

    def get_ota_update(self, otaUpdateId: str) -> GetOTAUpdateResponseTypeDef:
        """
        [Client.get_ota_update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.get_ota_update)
        """

    def get_percentiles(
        self,
        queryString: str,
        indexName: str = None,
        aggregationField: str = None,
        queryVersion: str = None,
        percents: List[float] = None,
    ) -> GetPercentilesResponseTypeDef:
        """
        [Client.get_percentiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.get_percentiles)
        """

    def get_policy(self, policyName: str) -> GetPolicyResponseTypeDef:
        """
        [Client.get_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.get_policy)
        """

    def get_policy_version(
        self, policyName: str, policyVersionId: str
    ) -> GetPolicyVersionResponseTypeDef:
        """
        [Client.get_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.get_policy_version)
        """

    def get_registration_code(self) -> GetRegistrationCodeResponseTypeDef:
        """
        [Client.get_registration_code documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.get_registration_code)
        """

    def get_statistics(
        self,
        queryString: str,
        indexName: str = None,
        aggregationField: str = None,
        queryVersion: str = None,
    ) -> GetStatisticsResponseTypeDef:
        """
        [Client.get_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.get_statistics)
        """

    def get_topic_rule(self, ruleName: str) -> GetTopicRuleResponseTypeDef:
        """
        [Client.get_topic_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.get_topic_rule)
        """

    def get_topic_rule_destination(self, arn: str) -> GetTopicRuleDestinationResponseTypeDef:
        """
        [Client.get_topic_rule_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.get_topic_rule_destination)
        """

    def get_v2_logging_options(self) -> GetV2LoggingOptionsResponseTypeDef:
        """
        [Client.get_v2_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.get_v2_logging_options)
        """

    def list_active_violations(
        self,
        thingName: str = None,
        securityProfileName: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListActiveViolationsResponseTypeDef:
        """
        [Client.list_active_violations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_active_violations)
        """

    def list_attached_policies(
        self, target: str, recursive: bool = None, marker: str = None, pageSize: int = None
    ) -> ListAttachedPoliciesResponseTypeDef:
        """
        [Client.list_attached_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_attached_policies)
        """

    def list_audit_findings(
        self,
        taskId: str = None,
        checkName: str = None,
        resourceIdentifier: "ResourceIdentifierTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None,
        startTime: datetime = None,
        endTime: datetime = None,
        listSuppressedFindings: bool = None,
    ) -> ListAuditFindingsResponseTypeDef:
        """
        [Client.list_audit_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_audit_findings)
        """

    def list_audit_mitigation_actions_executions(
        self,
        taskId: str,
        findingId: str,
        actionStatus: Literal[
            "IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED", "SKIPPED", "PENDING"
        ] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListAuditMitigationActionsExecutionsResponseTypeDef:
        """
        [Client.list_audit_mitigation_actions_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_audit_mitigation_actions_executions)
        """

    def list_audit_mitigation_actions_tasks(
        self,
        startTime: datetime,
        endTime: datetime,
        auditTaskId: str = None,
        findingId: str = None,
        taskStatus: Literal["IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED"] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListAuditMitigationActionsTasksResponseTypeDef:
        """
        [Client.list_audit_mitigation_actions_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_audit_mitigation_actions_tasks)
        """

    def list_audit_suppressions(
        self,
        checkName: str = None,
        resourceIdentifier: "ResourceIdentifierTypeDef" = None,
        ascendingOrder: bool = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListAuditSuppressionsResponseTypeDef:
        """
        [Client.list_audit_suppressions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_audit_suppressions)
        """

    def list_audit_tasks(
        self,
        startTime: datetime,
        endTime: datetime,
        taskType: Literal["ON_DEMAND_AUDIT_TASK", "SCHEDULED_AUDIT_TASK"] = None,
        taskStatus: Literal["IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListAuditTasksResponseTypeDef:
        """
        [Client.list_audit_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_audit_tasks)
        """

    def list_authorizers(
        self,
        pageSize: int = None,
        marker: str = None,
        ascendingOrder: bool = None,
        status: Literal["ACTIVE", "INACTIVE"] = None,
    ) -> ListAuthorizersResponseTypeDef:
        """
        [Client.list_authorizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_authorizers)
        """

    def list_billing_groups(
        self, nextToken: str = None, maxResults: int = None, namePrefixFilter: str = None
    ) -> ListBillingGroupsResponseTypeDef:
        """
        [Client.list_billing_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_billing_groups)
        """

    def list_ca_certificates(
        self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> ListCACertificatesResponseTypeDef:
        """
        [Client.list_ca_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_ca_certificates)
        """

    def list_certificates(
        self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> ListCertificatesResponseTypeDef:
        """
        [Client.list_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_certificates)
        """

    def list_certificates_by_ca(
        self,
        caCertificateId: str,
        pageSize: int = None,
        marker: str = None,
        ascendingOrder: bool = None,
    ) -> ListCertificatesByCAResponseTypeDef:
        """
        [Client.list_certificates_by_ca documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_certificates_by_ca)
        """

    def list_dimensions(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListDimensionsResponseTypeDef:
        """
        [Client.list_dimensions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_dimensions)
        """

    def list_domain_configurations(
        self,
        marker: str = None,
        pageSize: int = None,
        serviceType: Literal["DATA", "CREDENTIAL_PROVIDER", "JOBS"] = None,
    ) -> ListDomainConfigurationsResponseTypeDef:
        """
        [Client.list_domain_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_domain_configurations)
        """

    def list_indices(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListIndicesResponseTypeDef:
        """
        [Client.list_indices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_indices)
        """

    def list_job_executions_for_job(
        self,
        jobId: str,
        status: Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListJobExecutionsForJobResponseTypeDef:
        """
        [Client.list_job_executions_for_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_job_executions_for_job)
        """

    def list_job_executions_for_thing(
        self,
        thingName: str,
        status: Literal[
            "QUEUED",
            "IN_PROGRESS",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "REJECTED",
            "REMOVED",
            "CANCELED",
        ] = None,
        namespaceId: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListJobExecutionsForThingResponseTypeDef:
        """
        [Client.list_job_executions_for_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_job_executions_for_thing)
        """

    def list_jobs(
        self,
        status: Literal["IN_PROGRESS", "CANCELED", "COMPLETED", "DELETION_IN_PROGRESS"] = None,
        targetSelection: Literal["CONTINUOUS", "SNAPSHOT"] = None,
        maxResults: int = None,
        nextToken: str = None,
        thingGroupName: str = None,
        thingGroupId: str = None,
        namespaceId: str = None,
    ) -> ListJobsResponseTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_jobs)
        """

    def list_mitigation_actions(
        self,
        actionType: Literal[
            "UPDATE_DEVICE_CERTIFICATE",
            "UPDATE_CA_CERTIFICATE",
            "ADD_THINGS_TO_THING_GROUP",
            "REPLACE_DEFAULT_POLICY_VERSION",
            "ENABLE_IOT_LOGGING",
            "PUBLISH_FINDING_TO_SNS",
        ] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListMitigationActionsResponseTypeDef:
        """
        [Client.list_mitigation_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_mitigation_actions)
        """

    def list_ota_updates(
        self,
        maxResults: int = None,
        nextToken: str = None,
        otaUpdateStatus: Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "CREATE_FAILED"
        ] = None,
    ) -> ListOTAUpdatesResponseTypeDef:
        """
        [Client.list_ota_updates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_ota_updates)
        """

    def list_outgoing_certificates(
        self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> ListOutgoingCertificatesResponseTypeDef:
        """
        [Client.list_outgoing_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_outgoing_certificates)
        """

    def list_policies(
        self, marker: str = None, pageSize: int = None, ascendingOrder: bool = None
    ) -> ListPoliciesResponseTypeDef:
        """
        [Client.list_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_policies)
        """

    def list_policy_principals(
        self, policyName: str, marker: str = None, pageSize: int = None, ascendingOrder: bool = None
    ) -> ListPolicyPrincipalsResponseTypeDef:
        """
        [Client.list_policy_principals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_policy_principals)
        """

    def list_policy_versions(self, policyName: str) -> ListPolicyVersionsResponseTypeDef:
        """
        [Client.list_policy_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_policy_versions)
        """

    def list_principal_policies(
        self, principal: str, marker: str = None, pageSize: int = None, ascendingOrder: bool = None
    ) -> ListPrincipalPoliciesResponseTypeDef:
        """
        [Client.list_principal_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_principal_policies)
        """

    def list_principal_things(
        self, principal: str, nextToken: str = None, maxResults: int = None
    ) -> ListPrincipalThingsResponseTypeDef:
        """
        [Client.list_principal_things documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_principal_things)
        """

    def list_provisioning_template_versions(
        self, templateName: str, maxResults: int = None, nextToken: str = None
    ) -> ListProvisioningTemplateVersionsResponseTypeDef:
        """
        [Client.list_provisioning_template_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_provisioning_template_versions)
        """

    def list_provisioning_templates(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListProvisioningTemplatesResponseTypeDef:
        """
        [Client.list_provisioning_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_provisioning_templates)
        """

    def list_role_aliases(
        self, pageSize: int = None, marker: str = None, ascendingOrder: bool = None
    ) -> ListRoleAliasesResponseTypeDef:
        """
        [Client.list_role_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_role_aliases)
        """

    def list_scheduled_audits(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListScheduledAuditsResponseTypeDef:
        """
        [Client.list_scheduled_audits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_scheduled_audits)
        """

    def list_security_profiles(
        self, nextToken: str = None, maxResults: int = None, dimensionName: str = None
    ) -> ListSecurityProfilesResponseTypeDef:
        """
        [Client.list_security_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_security_profiles)
        """

    def list_security_profiles_for_target(
        self,
        securityProfileTargetArn: str,
        nextToken: str = None,
        maxResults: int = None,
        recursive: bool = None,
    ) -> ListSecurityProfilesForTargetResponseTypeDef:
        """
        [Client.list_security_profiles_for_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_security_profiles_for_target)
        """

    def list_streams(
        self, maxResults: int = None, nextToken: str = None, ascendingOrder: bool = None
    ) -> ListStreamsResponseTypeDef:
        """
        [Client.list_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_streams)
        """

    def list_tags_for_resource(
        self, resourceArn: str, nextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_tags_for_resource)
        """

    def list_targets_for_policy(
        self, policyName: str, marker: str = None, pageSize: int = None
    ) -> ListTargetsForPolicyResponseTypeDef:
        """
        [Client.list_targets_for_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_targets_for_policy)
        """

    def list_targets_for_security_profile(
        self, securityProfileName: str, nextToken: str = None, maxResults: int = None
    ) -> ListTargetsForSecurityProfileResponseTypeDef:
        """
        [Client.list_targets_for_security_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_targets_for_security_profile)
        """

    def list_thing_groups(
        self,
        nextToken: str = None,
        maxResults: int = None,
        parentGroup: str = None,
        namePrefixFilter: str = None,
        recursive: bool = None,
    ) -> ListThingGroupsResponseTypeDef:
        """
        [Client.list_thing_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_thing_groups)
        """

    def list_thing_groups_for_thing(
        self, thingName: str, nextToken: str = None, maxResults: int = None
    ) -> ListThingGroupsForThingResponseTypeDef:
        """
        [Client.list_thing_groups_for_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_thing_groups_for_thing)
        """

    def list_thing_principals(
        self, thingName: str, nextToken: str = None, maxResults: int = None
    ) -> ListThingPrincipalsResponseTypeDef:
        """
        [Client.list_thing_principals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_thing_principals)
        """

    def list_thing_registration_task_reports(
        self,
        taskId: str,
        reportType: Literal["ERRORS", "RESULTS"],
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListThingRegistrationTaskReportsResponseTypeDef:
        """
        [Client.list_thing_registration_task_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_thing_registration_task_reports)
        """

    def list_thing_registration_tasks(
        self,
        nextToken: str = None,
        maxResults: int = None,
        status: Literal["InProgress", "Completed", "Failed", "Cancelled", "Cancelling"] = None,
    ) -> ListThingRegistrationTasksResponseTypeDef:
        """
        [Client.list_thing_registration_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_thing_registration_tasks)
        """

    def list_thing_types(
        self, nextToken: str = None, maxResults: int = None, thingTypeName: str = None
    ) -> ListThingTypesResponseTypeDef:
        """
        [Client.list_thing_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_thing_types)
        """

    def list_things(
        self,
        nextToken: str = None,
        maxResults: int = None,
        attributeName: str = None,
        attributeValue: str = None,
        thingTypeName: str = None,
    ) -> ListThingsResponseTypeDef:
        """
        [Client.list_things documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_things)
        """

    def list_things_in_billing_group(
        self, billingGroupName: str, nextToken: str = None, maxResults: int = None
    ) -> ListThingsInBillingGroupResponseTypeDef:
        """
        [Client.list_things_in_billing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_things_in_billing_group)
        """

    def list_things_in_thing_group(
        self,
        thingGroupName: str,
        recursive: bool = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListThingsInThingGroupResponseTypeDef:
        """
        [Client.list_things_in_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_things_in_thing_group)
        """

    def list_topic_rule_destinations(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListTopicRuleDestinationsResponseTypeDef:
        """
        [Client.list_topic_rule_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_topic_rule_destinations)
        """

    def list_topic_rules(
        self,
        topic: str = None,
        maxResults: int = None,
        nextToken: str = None,
        ruleDisabled: bool = None,
    ) -> ListTopicRulesResponseTypeDef:
        """
        [Client.list_topic_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_topic_rules)
        """

    def list_v2_logging_levels(
        self,
        targetType: Literal["DEFAULT", "THING_GROUP"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListV2LoggingLevelsResponseTypeDef:
        """
        [Client.list_v2_logging_levels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_v2_logging_levels)
        """

    def list_violation_events(
        self,
        startTime: datetime,
        endTime: datetime,
        thingName: str = None,
        securityProfileName: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListViolationEventsResponseTypeDef:
        """
        [Client.list_violation_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.list_violation_events)
        """

    def register_ca_certificate(
        self,
        caCertificate: str,
        verificationCertificate: str,
        setAsActive: bool = None,
        allowAutoRegistration: bool = None,
        registrationConfig: "RegistrationConfigTypeDef" = None,
        tags: List["TagTypeDef"] = None,
    ) -> RegisterCACertificateResponseTypeDef:
        """
        [Client.register_ca_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.register_ca_certificate)
        """

    def register_certificate(
        self,
        certificatePem: str,
        caCertificatePem: str = None,
        setAsActive: bool = None,
        status: Literal[
            "ACTIVE",
            "INACTIVE",
            "REVOKED",
            "PENDING_TRANSFER",
            "REGISTER_INACTIVE",
            "PENDING_ACTIVATION",
        ] = None,
    ) -> RegisterCertificateResponseTypeDef:
        """
        [Client.register_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.register_certificate)
        """

    def register_certificate_without_ca(
        self,
        certificatePem: str,
        status: Literal[
            "ACTIVE",
            "INACTIVE",
            "REVOKED",
            "PENDING_TRANSFER",
            "REGISTER_INACTIVE",
            "PENDING_ACTIVATION",
        ] = None,
    ) -> RegisterCertificateWithoutCAResponseTypeDef:
        """
        [Client.register_certificate_without_ca documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.register_certificate_without_ca)
        """

    def register_thing(
        self, templateBody: str, parameters: Dict[str, str] = None
    ) -> RegisterThingResponseTypeDef:
        """
        [Client.register_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.register_thing)
        """

    def reject_certificate_transfer(self, certificateId: str, rejectReason: str = None) -> None:
        """
        [Client.reject_certificate_transfer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.reject_certificate_transfer)
        """

    def remove_thing_from_billing_group(
        self,
        billingGroupName: str = None,
        billingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.remove_thing_from_billing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.remove_thing_from_billing_group)
        """

    def remove_thing_from_thing_group(
        self,
        thingGroupName: str = None,
        thingGroupArn: str = None,
        thingName: str = None,
        thingArn: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.remove_thing_from_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.remove_thing_from_thing_group)
        """

    def replace_topic_rule(self, ruleName: str, topicRulePayload: TopicRulePayloadTypeDef) -> None:
        """
        [Client.replace_topic_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.replace_topic_rule)
        """

    def search_index(
        self,
        queryString: str,
        indexName: str = None,
        nextToken: str = None,
        maxResults: int = None,
        queryVersion: str = None,
    ) -> SearchIndexResponseTypeDef:
        """
        [Client.search_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.search_index)
        """

    def set_default_authorizer(self, authorizerName: str) -> SetDefaultAuthorizerResponseTypeDef:
        """
        [Client.set_default_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.set_default_authorizer)
        """

    def set_default_policy_version(self, policyName: str, policyVersionId: str) -> None:
        """
        [Client.set_default_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.set_default_policy_version)
        """

    def set_logging_options(self, loggingOptionsPayload: LoggingOptionsPayloadTypeDef) -> None:
        """
        [Client.set_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.set_logging_options)
        """

    def set_v2_logging_level(
        self,
        logTarget: "LogTargetTypeDef",
        logLevel: Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"],
    ) -> None:
        """
        [Client.set_v2_logging_level documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.set_v2_logging_level)
        """

    def set_v2_logging_options(
        self,
        roleArn: str = None,
        defaultLogLevel: Literal["DEBUG", "INFO", "ERROR", "WARN", "DISABLED"] = None,
        disableAllLogs: bool = None,
    ) -> None:
        """
        [Client.set_v2_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.set_v2_logging_options)
        """

    def start_audit_mitigation_actions_task(
        self,
        taskId: str,
        target: "AuditMitigationActionsTaskTargetTypeDef",
        auditCheckToActionsMapping: Dict[str, List[str]],
        clientRequestToken: str,
    ) -> StartAuditMitigationActionsTaskResponseTypeDef:
        """
        [Client.start_audit_mitigation_actions_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.start_audit_mitigation_actions_task)
        """

    def start_on_demand_audit_task(
        self, targetCheckNames: List[str]
    ) -> StartOnDemandAuditTaskResponseTypeDef:
        """
        [Client.start_on_demand_audit_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.start_on_demand_audit_task)
        """

    def start_thing_registration_task(
        self, templateBody: str, inputFileBucket: str, inputFileKey: str, roleArn: str
    ) -> StartThingRegistrationTaskResponseTypeDef:
        """
        [Client.start_thing_registration_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.start_thing_registration_task)
        """

    def stop_thing_registration_task(self, taskId: str) -> Dict[str, Any]:
        """
        [Client.stop_thing_registration_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.stop_thing_registration_task)
        """

    def tag_resource(self, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.tag_resource)
        """

    def test_authorization(
        self,
        authInfos: List["AuthInfoTypeDef"],
        principal: str = None,
        cognitoIdentityPoolId: str = None,
        clientId: str = None,
        policyNamesToAdd: List[str] = None,
        policyNamesToSkip: List[str] = None,
    ) -> TestAuthorizationResponseTypeDef:
        """
        [Client.test_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.test_authorization)
        """

    def test_invoke_authorizer(
        self,
        authorizerName: str,
        token: str = None,
        tokenSignature: str = None,
        httpContext: HttpContextTypeDef = None,
        mqttContext: MqttContextTypeDef = None,
        tlsContext: TlsContextTypeDef = None,
    ) -> TestInvokeAuthorizerResponseTypeDef:
        """
        [Client.test_invoke_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.test_invoke_authorizer)
        """

    def transfer_certificate(
        self, certificateId: str, targetAwsAccount: str, transferMessage: str = None
    ) -> TransferCertificateResponseTypeDef:
        """
        [Client.transfer_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.transfer_certificate)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.untag_resource)
        """

    def update_account_audit_configuration(
        self,
        roleArn: str = None,
        auditNotificationTargetConfigurations: Dict[
            Literal["SNS"], "AuditNotificationTargetTypeDef"
        ] = None,
        auditCheckConfigurations: Dict[str, "AuditCheckConfigurationTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_account_audit_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.update_account_audit_configuration)
        """

    def update_audit_suppression(
        self,
        checkName: str,
        resourceIdentifier: "ResourceIdentifierTypeDef",
        expirationDate: datetime = None,
        suppressIndefinitely: bool = None,
        description: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_audit_suppression documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.update_audit_suppression)
        """

    def update_authorizer(
        self,
        authorizerName: str,
        authorizerFunctionArn: str = None,
        tokenKeyName: str = None,
        tokenSigningPublicKeys: Dict[str, str] = None,
        status: Literal["ACTIVE", "INACTIVE"] = None,
    ) -> UpdateAuthorizerResponseTypeDef:
        """
        [Client.update_authorizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.update_authorizer)
        """

    def update_billing_group(
        self,
        billingGroupName: str,
        billingGroupProperties: "BillingGroupPropertiesTypeDef",
        expectedVersion: int = None,
    ) -> UpdateBillingGroupResponseTypeDef:
        """
        [Client.update_billing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.update_billing_group)
        """

    def update_ca_certificate(
        self,
        certificateId: str,
        newStatus: Literal["ACTIVE", "INACTIVE"] = None,
        newAutoRegistrationStatus: Literal["ENABLE", "DISABLE"] = None,
        registrationConfig: "RegistrationConfigTypeDef" = None,
        removeAutoRegistration: bool = None,
    ) -> None:
        """
        [Client.update_ca_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.update_ca_certificate)
        """

    def update_certificate(
        self,
        certificateId: str,
        newStatus: Literal[
            "ACTIVE",
            "INACTIVE",
            "REVOKED",
            "PENDING_TRANSFER",
            "REGISTER_INACTIVE",
            "PENDING_ACTIVATION",
        ],
    ) -> None:
        """
        [Client.update_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.update_certificate)
        """

    def update_dimension(
        self, name: str, stringValues: List[str]
    ) -> UpdateDimensionResponseTypeDef:
        """
        [Client.update_dimension documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.update_dimension)
        """

    def update_domain_configuration(
        self,
        domainConfigurationName: str,
        authorizerConfig: "AuthorizerConfigTypeDef" = None,
        domainConfigurationStatus: Literal["ENABLED", "DISABLED"] = None,
        removeAuthorizerConfig: bool = None,
    ) -> UpdateDomainConfigurationResponseTypeDef:
        """
        [Client.update_domain_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.update_domain_configuration)
        """

    def update_dynamic_thing_group(
        self,
        thingGroupName: str,
        thingGroupProperties: "ThingGroupPropertiesTypeDef",
        expectedVersion: int = None,
        indexName: str = None,
        queryString: str = None,
        queryVersion: str = None,
    ) -> UpdateDynamicThingGroupResponseTypeDef:
        """
        [Client.update_dynamic_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.update_dynamic_thing_group)
        """

    def update_event_configurations(
        self,
        eventConfigurations: Dict[
            Literal[
                "THING",
                "THING_GROUP",
                "THING_TYPE",
                "THING_GROUP_MEMBERSHIP",
                "THING_GROUP_HIERARCHY",
                "THING_TYPE_ASSOCIATION",
                "JOB",
                "JOB_EXECUTION",
                "POLICY",
                "CERTIFICATE",
                "CA_CERTIFICATE",
            ],
            "ConfigurationTypeDef",
        ] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_event_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.update_event_configurations)
        """

    def update_indexing_configuration(
        self,
        thingIndexingConfiguration: "ThingIndexingConfigurationTypeDef" = None,
        thingGroupIndexingConfiguration: "ThingGroupIndexingConfigurationTypeDef" = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_indexing_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.update_indexing_configuration)
        """

    def update_job(
        self,
        jobId: str,
        description: str = None,
        presignedUrlConfig: "PresignedUrlConfigTypeDef" = None,
        jobExecutionsRolloutConfig: "JobExecutionsRolloutConfigTypeDef" = None,
        abortConfig: "AbortConfigTypeDef" = None,
        timeoutConfig: "TimeoutConfigTypeDef" = None,
        namespaceId: str = None,
    ) -> None:
        """
        [Client.update_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.update_job)
        """

    def update_mitigation_action(
        self,
        actionName: str,
        roleArn: str = None,
        actionParams: "MitigationActionParamsTypeDef" = None,
    ) -> UpdateMitigationActionResponseTypeDef:
        """
        [Client.update_mitigation_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.update_mitigation_action)
        """

    def update_provisioning_template(
        self,
        templateName: str,
        description: str = None,
        enabled: bool = None,
        defaultVersionId: int = None,
        provisioningRoleArn: str = None,
        preProvisioningHook: "ProvisioningHookTypeDef" = None,
        removePreProvisioningHook: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_provisioning_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.update_provisioning_template)
        """

    def update_role_alias(
        self, roleAlias: str, roleArn: str = None, credentialDurationSeconds: int = None
    ) -> UpdateRoleAliasResponseTypeDef:
        """
        [Client.update_role_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.update_role_alias)
        """

    def update_scheduled_audit(
        self,
        scheduledAuditName: str,
        frequency: Literal["DAILY", "WEEKLY", "BIWEEKLY", "MONTHLY"] = None,
        dayOfMonth: str = None,
        dayOfWeek: Literal["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"] = None,
        targetCheckNames: List[str] = None,
    ) -> UpdateScheduledAuditResponseTypeDef:
        """
        [Client.update_scheduled_audit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.update_scheduled_audit)
        """

    def update_security_profile(
        self,
        securityProfileName: str,
        securityProfileDescription: str = None,
        behaviors: List["BehaviorTypeDef"] = None,
        alertTargets: Dict[Literal["SNS"], "AlertTargetTypeDef"] = None,
        additionalMetricsToRetain: List[str] = None,
        additionalMetricsToRetainV2: List["MetricToRetainTypeDef"] = None,
        deleteBehaviors: bool = None,
        deleteAlertTargets: bool = None,
        deleteAdditionalMetricsToRetain: bool = None,
        expectedVersion: int = None,
    ) -> UpdateSecurityProfileResponseTypeDef:
        """
        [Client.update_security_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.update_security_profile)
        """

    def update_stream(
        self,
        streamId: str,
        description: str = None,
        files: List["StreamFileTypeDef"] = None,
        roleArn: str = None,
    ) -> UpdateStreamResponseTypeDef:
        """
        [Client.update_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.update_stream)
        """

    def update_thing(
        self,
        thingName: str,
        thingTypeName: str = None,
        attributePayload: "AttributePayloadTypeDef" = None,
        expectedVersion: int = None,
        removeThingType: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.update_thing)
        """

    def update_thing_group(
        self,
        thingGroupName: str,
        thingGroupProperties: "ThingGroupPropertiesTypeDef",
        expectedVersion: int = None,
    ) -> UpdateThingGroupResponseTypeDef:
        """
        [Client.update_thing_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.update_thing_group)
        """

    def update_thing_groups_for_thing(
        self,
        thingName: str = None,
        thingGroupsToAdd: List[str] = None,
        thingGroupsToRemove: List[str] = None,
        overrideDynamicGroups: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_thing_groups_for_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.update_thing_groups_for_thing)
        """

    def update_topic_rule_destination(
        self, arn: str, status: Literal["ENABLED", "IN_PROGRESS", "DISABLED", "ERROR"]
    ) -> Dict[str, Any]:
        """
        [Client.update_topic_rule_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.update_topic_rule_destination)
        """

    def validate_security_profile_behaviors(
        self, behaviors: List["BehaviorTypeDef"]
    ) -> ValidateSecurityProfileBehaviorsResponseTypeDef:
        """
        [Client.validate_security_profile_behaviors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Client.validate_security_profile_behaviors)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_active_violations"]
    ) -> ListActiveViolationsPaginator:
        """
        [Paginator.ListActiveViolations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListActiveViolations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_attached_policies"]
    ) -> ListAttachedPoliciesPaginator:
        """
        [Paginator.ListAttachedPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListAttachedPolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_audit_findings"]
    ) -> ListAuditFindingsPaginator:
        """
        [Paginator.ListAuditFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListAuditFindings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_audit_mitigation_actions_executions"]
    ) -> ListAuditMitigationActionsExecutionsPaginator:
        """
        [Paginator.ListAuditMitigationActionsExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListAuditMitigationActionsExecutions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_audit_mitigation_actions_tasks"]
    ) -> ListAuditMitigationActionsTasksPaginator:
        """
        [Paginator.ListAuditMitigationActionsTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListAuditMitigationActionsTasks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_audit_suppressions"]
    ) -> ListAuditSuppressionsPaginator:
        """
        [Paginator.ListAuditSuppressions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListAuditSuppressions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_audit_tasks"]) -> ListAuditTasksPaginator:
        """
        [Paginator.ListAuditTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListAuditTasks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_authorizers"]
    ) -> ListAuthorizersPaginator:
        """
        [Paginator.ListAuthorizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListAuthorizers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_billing_groups"]
    ) -> ListBillingGroupsPaginator:
        """
        [Paginator.ListBillingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListBillingGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_ca_certificates"]
    ) -> ListCACertificatesPaginator:
        """
        [Paginator.ListCACertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListCACertificates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_certificates"]
    ) -> ListCertificatesPaginator:
        """
        [Paginator.ListCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListCertificates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_certificates_by_ca"]
    ) -> ListCertificatesByCAPaginator:
        """
        [Paginator.ListCertificatesByCA documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListCertificatesByCA)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_dimensions"]) -> ListDimensionsPaginator:
        """
        [Paginator.ListDimensions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListDimensions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_domain_configurations"]
    ) -> ListDomainConfigurationsPaginator:
        """
        [Paginator.ListDomainConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListDomainConfigurations)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_indices"]) -> ListIndicesPaginator:
        """
        [Paginator.ListIndices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListIndices)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_job_executions_for_job"]
    ) -> ListJobExecutionsForJobPaginator:
        """
        [Paginator.ListJobExecutionsForJob documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForJob)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_job_executions_for_thing"]
    ) -> ListJobExecutionsForThingPaginator:
        """
        [Paginator.ListJobExecutionsForThing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForThing)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_mitigation_actions"]
    ) -> ListMitigationActionsPaginator:
        """
        [Paginator.ListMitigationActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListMitigationActions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_ota_updates"]) -> ListOTAUpdatesPaginator:
        """
        [Paginator.ListOTAUpdates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListOTAUpdates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_outgoing_certificates"]
    ) -> ListOutgoingCertificatesPaginator:
        """
        [Paginator.ListOutgoingCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListOutgoingCertificates)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_policies"]) -> ListPoliciesPaginator:
        """
        [Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListPolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_policy_principals"]
    ) -> ListPolicyPrincipalsPaginator:
        """
        [Paginator.ListPolicyPrincipals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListPolicyPrincipals)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_principal_policies"]
    ) -> ListPrincipalPoliciesPaginator:
        """
        [Paginator.ListPrincipalPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListPrincipalPolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_principal_things"]
    ) -> ListPrincipalThingsPaginator:
        """
        [Paginator.ListPrincipalThings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListPrincipalThings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_provisioning_template_versions"]
    ) -> ListProvisioningTemplateVersionsPaginator:
        """
        [Paginator.ListProvisioningTemplateVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListProvisioningTemplateVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_provisioning_templates"]
    ) -> ListProvisioningTemplatesPaginator:
        """
        [Paginator.ListProvisioningTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListProvisioningTemplates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_role_aliases"]
    ) -> ListRoleAliasesPaginator:
        """
        [Paginator.ListRoleAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListRoleAliases)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_scheduled_audits"]
    ) -> ListScheduledAuditsPaginator:
        """
        [Paginator.ListScheduledAudits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListScheduledAudits)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_profiles"]
    ) -> ListSecurityProfilesPaginator:
        """
        [Paginator.ListSecurityProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListSecurityProfiles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_profiles_for_target"]
    ) -> ListSecurityProfilesForTargetPaginator:
        """
        [Paginator.ListSecurityProfilesForTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListSecurityProfilesForTarget)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_streams"]) -> ListStreamsPaginator:
        """
        [Paginator.ListStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListStreams)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListTagsForResource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_targets_for_policy"]
    ) -> ListTargetsForPolicyPaginator:
        """
        [Paginator.ListTargetsForPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListTargetsForPolicy)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_targets_for_security_profile"]
    ) -> ListTargetsForSecurityProfilePaginator:
        """
        [Paginator.ListTargetsForSecurityProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListTargetsForSecurityProfile)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_thing_groups"]
    ) -> ListThingGroupsPaginator:
        """
        [Paginator.ListThingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListThingGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_thing_groups_for_thing"]
    ) -> ListThingGroupsForThingPaginator:
        """
        [Paginator.ListThingGroupsForThing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListThingGroupsForThing)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_thing_principals"]
    ) -> ListThingPrincipalsPaginator:
        """
        [Paginator.ListThingPrincipals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListThingPrincipals)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_thing_registration_task_reports"]
    ) -> ListThingRegistrationTaskReportsPaginator:
        """
        [Paginator.ListThingRegistrationTaskReports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListThingRegistrationTaskReports)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_thing_registration_tasks"]
    ) -> ListThingRegistrationTasksPaginator:
        """
        [Paginator.ListThingRegistrationTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListThingRegistrationTasks)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_thing_types"]) -> ListThingTypesPaginator:
        """
        [Paginator.ListThingTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListThingTypes)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_things"]) -> ListThingsPaginator:
        """
        [Paginator.ListThings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListThings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_things_in_billing_group"]
    ) -> ListThingsInBillingGroupPaginator:
        """
        [Paginator.ListThingsInBillingGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListThingsInBillingGroup)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_things_in_thing_group"]
    ) -> ListThingsInThingGroupPaginator:
        """
        [Paginator.ListThingsInThingGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListThingsInThingGroup)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_topic_rule_destinations"]
    ) -> ListTopicRuleDestinationsPaginator:
        """
        [Paginator.ListTopicRuleDestinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListTopicRuleDestinations)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_topic_rules"]) -> ListTopicRulesPaginator:
        """
        [Paginator.ListTopicRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListTopicRules)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_v2_logging_levels"]
    ) -> ListV2LoggingLevelsPaginator:
        """
        [Paginator.ListV2LoggingLevels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListV2LoggingLevels)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_violation_events"]
    ) -> ListViolationEventsPaginator:
        """
        [Paginator.ListViolationEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot.html#IoT.Paginator.ListViolationEvents)
        """
