"""
Type annotations for iot service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_iot import IoTClient
    from mypy_boto3_iot.paginator import (
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
        ListCertificatesPaginator,
        ListCertificatesByCAPaginator,
        ListCustomMetricsPaginator,
        ListDetectMitigationActionsExecutionsPaginator,
        ListDetectMitigationActionsTasksPaginator,
        ListDimensionsPaginator,
        ListDomainConfigurationsPaginator,
        ListFleetMetricsPaginator,
        ListIndicesPaginator,
        ListJobExecutionsForJobPaginator,
        ListJobExecutionsForThingPaginator,
        ListJobTemplatesPaginator,
        ListJobsPaginator,
        ListMetricValuesPaginator,
        ListMitigationActionsPaginator,
        ListOTAUpdatesPaginator,
        ListOutgoingCertificatesPaginator,
        ListPoliciesPaginator,
        ListPolicyPrincipalsPaginator,
        ListPrincipalPoliciesPaginator,
        ListPrincipalThingsPaginator,
        ListProvisioningTemplateVersionsPaginator,
        ListProvisioningTemplatesPaginator,
        ListRoleAliasesPaginator,
        ListScheduledAuditsPaginator,
        ListSecurityProfilesPaginator,
        ListSecurityProfilesForTargetPaginator,
        ListStreamsPaginator,
        ListTagsForResourcePaginator,
        ListTargetsForPolicyPaginator,
        ListTargetsForSecurityProfilePaginator,
        ListThingGroupsPaginator,
        ListThingGroupsForThingPaginator,
        ListThingPrincipalsPaginator,
        ListThingRegistrationTaskReportsPaginator,
        ListThingRegistrationTasksPaginator,
        ListThingTypesPaginator,
        ListThingsPaginator,
        ListThingsInBillingGroupPaginator,
        ListThingsInThingGroupPaginator,
        ListTopicRuleDestinationsPaginator,
        ListTopicRulesPaginator,
        ListV2LoggingLevelsPaginator,
        ListViolationEventsPaginator,
    )

    client: IoTClient = boto3.client("iot")

    get_behavior_model_training_summaries_paginator: GetBehaviorModelTrainingSummariesPaginator = client.get_paginator("get_behavior_model_training_summaries")
    list_active_violations_paginator: ListActiveViolationsPaginator = client.get_paginator("list_active_violations")
    list_attached_policies_paginator: ListAttachedPoliciesPaginator = client.get_paginator("list_attached_policies")
    list_audit_findings_paginator: ListAuditFindingsPaginator = client.get_paginator("list_audit_findings")
    list_audit_mitigation_actions_executions_paginator: ListAuditMitigationActionsExecutionsPaginator = client.get_paginator("list_audit_mitigation_actions_executions")
    list_audit_mitigation_actions_tasks_paginator: ListAuditMitigationActionsTasksPaginator = client.get_paginator("list_audit_mitigation_actions_tasks")
    list_audit_suppressions_paginator: ListAuditSuppressionsPaginator = client.get_paginator("list_audit_suppressions")
    list_audit_tasks_paginator: ListAuditTasksPaginator = client.get_paginator("list_audit_tasks")
    list_authorizers_paginator: ListAuthorizersPaginator = client.get_paginator("list_authorizers")
    list_billing_groups_paginator: ListBillingGroupsPaginator = client.get_paginator("list_billing_groups")
    list_ca_certificates_paginator: ListCACertificatesPaginator = client.get_paginator("list_ca_certificates")
    list_certificates_paginator: ListCertificatesPaginator = client.get_paginator("list_certificates")
    list_certificates_by_ca_paginator: ListCertificatesByCAPaginator = client.get_paginator("list_certificates_by_ca")
    list_custom_metrics_paginator: ListCustomMetricsPaginator = client.get_paginator("list_custom_metrics")
    list_detect_mitigation_actions_executions_paginator: ListDetectMitigationActionsExecutionsPaginator = client.get_paginator("list_detect_mitigation_actions_executions")
    list_detect_mitigation_actions_tasks_paginator: ListDetectMitigationActionsTasksPaginator = client.get_paginator("list_detect_mitigation_actions_tasks")
    list_dimensions_paginator: ListDimensionsPaginator = client.get_paginator("list_dimensions")
    list_domain_configurations_paginator: ListDomainConfigurationsPaginator = client.get_paginator("list_domain_configurations")
    list_fleet_metrics_paginator: ListFleetMetricsPaginator = client.get_paginator("list_fleet_metrics")
    list_indices_paginator: ListIndicesPaginator = client.get_paginator("list_indices")
    list_job_executions_for_job_paginator: ListJobExecutionsForJobPaginator = client.get_paginator("list_job_executions_for_job")
    list_job_executions_for_thing_paginator: ListJobExecutionsForThingPaginator = client.get_paginator("list_job_executions_for_thing")
    list_job_templates_paginator: ListJobTemplatesPaginator = client.get_paginator("list_job_templates")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    list_metric_values_paginator: ListMetricValuesPaginator = client.get_paginator("list_metric_values")
    list_mitigation_actions_paginator: ListMitigationActionsPaginator = client.get_paginator("list_mitigation_actions")
    list_ota_updates_paginator: ListOTAUpdatesPaginator = client.get_paginator("list_ota_updates")
    list_outgoing_certificates_paginator: ListOutgoingCertificatesPaginator = client.get_paginator("list_outgoing_certificates")
    list_policies_paginator: ListPoliciesPaginator = client.get_paginator("list_policies")
    list_policy_principals_paginator: ListPolicyPrincipalsPaginator = client.get_paginator("list_policy_principals")
    list_principal_policies_paginator: ListPrincipalPoliciesPaginator = client.get_paginator("list_principal_policies")
    list_principal_things_paginator: ListPrincipalThingsPaginator = client.get_paginator("list_principal_things")
    list_provisioning_template_versions_paginator: ListProvisioningTemplateVersionsPaginator = client.get_paginator("list_provisioning_template_versions")
    list_provisioning_templates_paginator: ListProvisioningTemplatesPaginator = client.get_paginator("list_provisioning_templates")
    list_role_aliases_paginator: ListRoleAliasesPaginator = client.get_paginator("list_role_aliases")
    list_scheduled_audits_paginator: ListScheduledAuditsPaginator = client.get_paginator("list_scheduled_audits")
    list_security_profiles_paginator: ListSecurityProfilesPaginator = client.get_paginator("list_security_profiles")
    list_security_profiles_for_target_paginator: ListSecurityProfilesForTargetPaginator = client.get_paginator("list_security_profiles_for_target")
    list_streams_paginator: ListStreamsPaginator = client.get_paginator("list_streams")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    list_targets_for_policy_paginator: ListTargetsForPolicyPaginator = client.get_paginator("list_targets_for_policy")
    list_targets_for_security_profile_paginator: ListTargetsForSecurityProfilePaginator = client.get_paginator("list_targets_for_security_profile")
    list_thing_groups_paginator: ListThingGroupsPaginator = client.get_paginator("list_thing_groups")
    list_thing_groups_for_thing_paginator: ListThingGroupsForThingPaginator = client.get_paginator("list_thing_groups_for_thing")
    list_thing_principals_paginator: ListThingPrincipalsPaginator = client.get_paginator("list_thing_principals")
    list_thing_registration_task_reports_paginator: ListThingRegistrationTaskReportsPaginator = client.get_paginator("list_thing_registration_task_reports")
    list_thing_registration_tasks_paginator: ListThingRegistrationTasksPaginator = client.get_paginator("list_thing_registration_tasks")
    list_thing_types_paginator: ListThingTypesPaginator = client.get_paginator("list_thing_types")
    list_things_paginator: ListThingsPaginator = client.get_paginator("list_things")
    list_things_in_billing_group_paginator: ListThingsInBillingGroupPaginator = client.get_paginator("list_things_in_billing_group")
    list_things_in_thing_group_paginator: ListThingsInThingGroupPaginator = client.get_paginator("list_things_in_thing_group")
    list_topic_rule_destinations_paginator: ListTopicRuleDestinationsPaginator = client.get_paginator("list_topic_rule_destinations")
    list_topic_rules_paginator: ListTopicRulesPaginator = client.get_paginator("list_topic_rules")
    list_v2_logging_levels_paginator: ListV2LoggingLevelsPaginator = client.get_paginator("list_v2_logging_levels")
    list_violation_events_paginator: ListViolationEventsPaginator = client.get_paginator("list_violation_events")
    ```
"""
from datetime import datetime
from typing import Iterator, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    AuditMitigationActionsExecutionStatusType,
    AuditMitigationActionsTaskStatusType,
    AuditTaskStatusType,
    AuditTaskTypeType,
    AuthorizerStatusType,
    BehaviorCriteriaTypeType,
    DimensionValueOperatorType,
    JobExecutionStatusType,
    JobStatusType,
    LogTargetTypeType,
    MitigationActionTypeType,
    OTAUpdateStatusType,
    ReportTypeType,
    ServiceTypeType,
    StatusType,
    TargetSelectionType,
    VerificationStateType,
)
from .type_defs import (
    GetBehaviorModelTrainingSummariesResponseTypeDef,
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
    ListFleetMetricsResponseTypeDef,
    ListIndicesResponseTypeDef,
    ListJobExecutionsForJobResponseTypeDef,
    ListJobExecutionsForThingResponseTypeDef,
    ListJobsResponseTypeDef,
    ListJobTemplatesResponseTypeDef,
    ListMetricValuesResponseTypeDef,
    ListMitigationActionsResponseTypeDef,
    ListOTAUpdatesResponseTypeDef,
    ListOutgoingCertificatesResponseTypeDef,
    ListPoliciesResponseTypeDef,
    ListPolicyPrincipalsResponseTypeDef,
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
    PaginatorConfigTypeDef,
    ResourceIdentifierTypeDef,
)

__all__ = (
    "GetBehaviorModelTrainingSummariesPaginator",
    "ListActiveViolationsPaginator",
    "ListAttachedPoliciesPaginator",
    "ListAuditFindingsPaginator",
    "ListAuditMitigationActionsExecutionsPaginator",
    "ListAuditMitigationActionsTasksPaginator",
    "ListAuditSuppressionsPaginator",
    "ListAuditTasksPaginator",
    "ListAuthorizersPaginator",
    "ListBillingGroupsPaginator",
    "ListCACertificatesPaginator",
    "ListCertificatesPaginator",
    "ListCertificatesByCAPaginator",
    "ListCustomMetricsPaginator",
    "ListDetectMitigationActionsExecutionsPaginator",
    "ListDetectMitigationActionsTasksPaginator",
    "ListDimensionsPaginator",
    "ListDomainConfigurationsPaginator",
    "ListFleetMetricsPaginator",
    "ListIndicesPaginator",
    "ListJobExecutionsForJobPaginator",
    "ListJobExecutionsForThingPaginator",
    "ListJobTemplatesPaginator",
    "ListJobsPaginator",
    "ListMetricValuesPaginator",
    "ListMitigationActionsPaginator",
    "ListOTAUpdatesPaginator",
    "ListOutgoingCertificatesPaginator",
    "ListPoliciesPaginator",
    "ListPolicyPrincipalsPaginator",
    "ListPrincipalPoliciesPaginator",
    "ListPrincipalThingsPaginator",
    "ListProvisioningTemplateVersionsPaginator",
    "ListProvisioningTemplatesPaginator",
    "ListRoleAliasesPaginator",
    "ListScheduledAuditsPaginator",
    "ListSecurityProfilesPaginator",
    "ListSecurityProfilesForTargetPaginator",
    "ListStreamsPaginator",
    "ListTagsForResourcePaginator",
    "ListTargetsForPolicyPaginator",
    "ListTargetsForSecurityProfilePaginator",
    "ListThingGroupsPaginator",
    "ListThingGroupsForThingPaginator",
    "ListThingPrincipalsPaginator",
    "ListThingRegistrationTaskReportsPaginator",
    "ListThingRegistrationTasksPaginator",
    "ListThingTypesPaginator",
    "ListThingsPaginator",
    "ListThingsInBillingGroupPaginator",
    "ListThingsInThingGroupPaginator",
    "ListTopicRuleDestinationsPaginator",
    "ListTopicRulesPaginator",
    "ListV2LoggingLevelsPaginator",
    "ListViolationEventsPaginator",
)

class GetBehaviorModelTrainingSummariesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.GetBehaviorModelTrainingSummaries)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#getbehaviormodeltrainingsummariespaginator)
    """

    def paginate(
        self, *, securityProfileName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetBehaviorModelTrainingSummariesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.GetBehaviorModelTrainingSummaries.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#getbehaviormodeltrainingsummariespaginator)
        """

class ListActiveViolationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListActiveViolations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listactiveviolationspaginator)
    """

    def paginate(
        self,
        *,
        thingName: str = None,
        securityProfileName: str = None,
        behaviorCriteriaType: BehaviorCriteriaTypeType = None,
        listSuppressedAlerts: bool = None,
        verificationState: VerificationStateType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListActiveViolationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListActiveViolations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listactiveviolationspaginator)
        """

class ListAttachedPoliciesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListAttachedPolicies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listattachedpoliciespaginator)
    """

    def paginate(
        self,
        *,
        target: str,
        recursive: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAttachedPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListAttachedPolicies.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listattachedpoliciespaginator)
        """

class ListAuditFindingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListAuditFindings)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listauditfindingspaginator)
    """

    def paginate(
        self,
        *,
        taskId: str = None,
        checkName: str = None,
        resourceIdentifier: "ResourceIdentifierTypeDef" = None,
        startTime: Union[datetime, str] = None,
        endTime: Union[datetime, str] = None,
        listSuppressedFindings: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAuditFindingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListAuditFindings.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listauditfindingspaginator)
        """

class ListAuditMitigationActionsExecutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListAuditMitigationActionsExecutions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listauditmitigationactionsexecutionspaginator)
    """

    def paginate(
        self,
        *,
        taskId: str,
        findingId: str,
        actionStatus: AuditMitigationActionsExecutionStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAuditMitigationActionsExecutionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListAuditMitigationActionsExecutions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listauditmitigationactionsexecutionspaginator)
        """

class ListAuditMitigationActionsTasksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListAuditMitigationActionsTasks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listauditmitigationactionstaskspaginator)
    """

    def paginate(
        self,
        *,
        startTime: Union[datetime, str],
        endTime: Union[datetime, str],
        auditTaskId: str = None,
        findingId: str = None,
        taskStatus: AuditMitigationActionsTaskStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAuditMitigationActionsTasksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListAuditMitigationActionsTasks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listauditmitigationactionstaskspaginator)
        """

class ListAuditSuppressionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListAuditSuppressions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listauditsuppressionspaginator)
    """

    def paginate(
        self,
        *,
        checkName: str = None,
        resourceIdentifier: "ResourceIdentifierTypeDef" = None,
        ascendingOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAuditSuppressionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListAuditSuppressions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listauditsuppressionspaginator)
        """

class ListAuditTasksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListAuditTasks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listaudittaskspaginator)
    """

    def paginate(
        self,
        *,
        startTime: Union[datetime, str],
        endTime: Union[datetime, str],
        taskType: AuditTaskTypeType = None,
        taskStatus: AuditTaskStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAuditTasksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListAuditTasks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listaudittaskspaginator)
        """

class ListAuthorizersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListAuthorizers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listauthorizerspaginator)
    """

    def paginate(
        self,
        *,
        ascendingOrder: bool = None,
        status: AuthorizerStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAuthorizersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListAuthorizers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listauthorizerspaginator)
        """

class ListBillingGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListBillingGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listbillinggroupspaginator)
    """

    def paginate(
        self, *, namePrefixFilter: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBillingGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListBillingGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listbillinggroupspaginator)
        """

class ListCACertificatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListCACertificates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listcacertificatespaginator)
    """

    def paginate(
        self, *, ascendingOrder: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCACertificatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListCACertificates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listcacertificatespaginator)
        """

class ListCertificatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListCertificates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listcertificatespaginator)
    """

    def paginate(
        self, *, ascendingOrder: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCertificatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListCertificates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listcertificatespaginator)
        """

class ListCertificatesByCAPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListCertificatesByCA)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listcertificatesbycapaginator)
    """

    def paginate(
        self,
        *,
        caCertificateId: str,
        ascendingOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCertificatesByCAResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListCertificatesByCA.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listcertificatesbycapaginator)
        """

class ListCustomMetricsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListCustomMetrics)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listcustommetricspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCustomMetricsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListCustomMetrics.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listcustommetricspaginator)
        """

class ListDetectMitigationActionsExecutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListDetectMitigationActionsExecutions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listdetectmitigationactionsexecutionspaginator)
    """

    def paginate(
        self,
        *,
        taskId: str = None,
        violationId: str = None,
        thingName: str = None,
        startTime: Union[datetime, str] = None,
        endTime: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDetectMitigationActionsExecutionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListDetectMitigationActionsExecutions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listdetectmitigationactionsexecutionspaginator)
        """

class ListDetectMitigationActionsTasksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListDetectMitigationActionsTasks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listdetectmitigationactionstaskspaginator)
    """

    def paginate(
        self,
        *,
        startTime: Union[datetime, str],
        endTime: Union[datetime, str],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDetectMitigationActionsTasksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListDetectMitigationActionsTasks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listdetectmitigationactionstaskspaginator)
        """

class ListDimensionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListDimensions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listdimensionspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDimensionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListDimensions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listdimensionspaginator)
        """

class ListDomainConfigurationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListDomainConfigurations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listdomainconfigurationspaginator)
    """

    def paginate(
        self,
        *,
        serviceType: ServiceTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDomainConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListDomainConfigurations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listdomainconfigurationspaginator)
        """

class ListFleetMetricsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListFleetMetrics)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listfleetmetricspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFleetMetricsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListFleetMetrics.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listfleetmetricspaginator)
        """

class ListIndicesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListIndices)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listindicespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIndicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListIndices.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listindicespaginator)
        """

class ListJobExecutionsForJobPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForJob)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listjobexecutionsforjobpaginator)
    """

    def paginate(
        self,
        *,
        jobId: str,
        status: JobExecutionStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobExecutionsForJobResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForJob.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listjobexecutionsforjobpaginator)
        """

class ListJobExecutionsForThingPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForThing)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listjobexecutionsforthingpaginator)
    """

    def paginate(
        self,
        *,
        thingName: str,
        status: JobExecutionStatusType = None,
        namespaceId: str = None,
        jobId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobExecutionsForThingResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForThing.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listjobexecutionsforthingpaginator)
        """

class ListJobTemplatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListJobTemplates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listjobtemplatespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListJobTemplates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listjobtemplatespaginator)
        """

class ListJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listjobspaginator)
    """

    def paginate(
        self,
        *,
        status: JobStatusType = None,
        targetSelection: TargetSelectionType = None,
        thingGroupName: str = None,
        thingGroupId: str = None,
        namespaceId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listjobspaginator)
        """

class ListMetricValuesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListMetricValues)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listmetricvaluespaginator)
    """

    def paginate(
        self,
        *,
        thingName: str,
        metricName: str,
        startTime: Union[datetime, str],
        endTime: Union[datetime, str],
        dimensionName: str = None,
        dimensionValueOperator: DimensionValueOperatorType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMetricValuesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListMetricValues.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listmetricvaluespaginator)
        """

class ListMitigationActionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListMitigationActions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listmitigationactionspaginator)
    """

    def paginate(
        self,
        *,
        actionType: MitigationActionTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMitigationActionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListMitigationActions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listmitigationactionspaginator)
        """

class ListOTAUpdatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListOTAUpdates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listotaupdatespaginator)
    """

    def paginate(
        self,
        *,
        otaUpdateStatus: OTAUpdateStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOTAUpdatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListOTAUpdates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listotaupdatespaginator)
        """

class ListOutgoingCertificatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListOutgoingCertificates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listoutgoingcertificatespaginator)
    """

    def paginate(
        self, *, ascendingOrder: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOutgoingCertificatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListOutgoingCertificates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listoutgoingcertificatespaginator)
        """

class ListPoliciesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListPolicies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listpoliciespaginator)
    """

    def paginate(
        self, *, ascendingOrder: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListPolicies.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listpoliciespaginator)
        """

class ListPolicyPrincipalsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListPolicyPrincipals)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listpolicyprincipalspaginator)
    """

    def paginate(
        self,
        *,
        policyName: str,
        ascendingOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPolicyPrincipalsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListPolicyPrincipals.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listpolicyprincipalspaginator)
        """

class ListPrincipalPoliciesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListPrincipalPolicies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listprincipalpoliciespaginator)
    """

    def paginate(
        self,
        *,
        principal: str,
        ascendingOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPrincipalPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListPrincipalPolicies.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listprincipalpoliciespaginator)
        """

class ListPrincipalThingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListPrincipalThings)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listprincipalthingspaginator)
    """

    def paginate(
        self, *, principal: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPrincipalThingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListPrincipalThings.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listprincipalthingspaginator)
        """

class ListProvisioningTemplateVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListProvisioningTemplateVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listprovisioningtemplateversionspaginator)
    """

    def paginate(
        self, *, templateName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProvisioningTemplateVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListProvisioningTemplateVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listprovisioningtemplateversionspaginator)
        """

class ListProvisioningTemplatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListProvisioningTemplates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listprovisioningtemplatespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProvisioningTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListProvisioningTemplates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listprovisioningtemplatespaginator)
        """

class ListRoleAliasesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListRoleAliases)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listrolealiasespaginator)
    """

    def paginate(
        self, *, ascendingOrder: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRoleAliasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListRoleAliases.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listrolealiasespaginator)
        """

class ListScheduledAuditsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListScheduledAudits)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listscheduledauditspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListScheduledAuditsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListScheduledAudits.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listscheduledauditspaginator)
        """

class ListSecurityProfilesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListSecurityProfiles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listsecurityprofilespaginator)
    """

    def paginate(
        self,
        *,
        dimensionName: str = None,
        metricName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSecurityProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListSecurityProfiles.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listsecurityprofilespaginator)
        """

class ListSecurityProfilesForTargetPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListSecurityProfilesForTarget)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listsecurityprofilesfortargetpaginator)
    """

    def paginate(
        self,
        *,
        securityProfileTargetArn: str,
        recursive: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSecurityProfilesForTargetResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListSecurityProfilesForTarget.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listsecurityprofilesfortargetpaginator)
        """

class ListStreamsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListStreams)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#liststreamspaginator)
    """

    def paginate(
        self, *, ascendingOrder: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStreamsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListStreams.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#liststreamspaginator)
        """

class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listtagsforresourcepaginator)
    """

    def paginate(
        self, *, resourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listtagsforresourcepaginator)
        """

class ListTargetsForPolicyPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListTargetsForPolicy)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listtargetsforpolicypaginator)
    """

    def paginate(
        self, *, policyName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTargetsForPolicyResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListTargetsForPolicy.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listtargetsforpolicypaginator)
        """

class ListTargetsForSecurityProfilePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListTargetsForSecurityProfile)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listtargetsforsecurityprofilepaginator)
    """

    def paginate(
        self, *, securityProfileName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTargetsForSecurityProfileResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListTargetsForSecurityProfile.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listtargetsforsecurityprofilepaginator)
        """

class ListThingGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListThingGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthinggroupspaginator)
    """

    def paginate(
        self,
        *,
        parentGroup: str = None,
        namePrefixFilter: str = None,
        recursive: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThingGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListThingGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthinggroupspaginator)
        """

class ListThingGroupsForThingPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListThingGroupsForThing)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthinggroupsforthingpaginator)
    """

    def paginate(
        self, *, thingName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThingGroupsForThingResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListThingGroupsForThing.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthinggroupsforthingpaginator)
        """

class ListThingPrincipalsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListThingPrincipals)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingprincipalspaginator)
    """

    def paginate(
        self, *, thingName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThingPrincipalsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListThingPrincipals.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingprincipalspaginator)
        """

class ListThingRegistrationTaskReportsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListThingRegistrationTaskReports)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingregistrationtaskreportspaginator)
    """

    def paginate(
        self,
        *,
        taskId: str,
        reportType: ReportTypeType,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThingRegistrationTaskReportsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListThingRegistrationTaskReports.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingregistrationtaskreportspaginator)
        """

class ListThingRegistrationTasksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListThingRegistrationTasks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingregistrationtaskspaginator)
    """

    def paginate(
        self, *, status: StatusType = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThingRegistrationTasksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListThingRegistrationTasks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingregistrationtaskspaginator)
        """

class ListThingTypesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListThingTypes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingtypespaginator)
    """

    def paginate(
        self, *, thingTypeName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThingTypesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListThingTypes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingtypespaginator)
        """

class ListThingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListThings)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingspaginator)
    """

    def paginate(
        self,
        *,
        attributeName: str = None,
        attributeValue: str = None,
        thingTypeName: str = None,
        usePrefixAttributeValue: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListThings.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingspaginator)
        """

class ListThingsInBillingGroupPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListThingsInBillingGroup)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingsinbillinggrouppaginator)
    """

    def paginate(
        self, *, billingGroupName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThingsInBillingGroupResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListThingsInBillingGroup.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingsinbillinggrouppaginator)
        """

class ListThingsInThingGroupPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListThingsInThingGroup)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingsinthinggrouppaginator)
    """

    def paginate(
        self,
        *,
        thingGroupName: str,
        recursive: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThingsInThingGroupResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListThingsInThingGroup.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listthingsinthinggrouppaginator)
        """

class ListTopicRuleDestinationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListTopicRuleDestinations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listtopicruledestinationspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTopicRuleDestinationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListTopicRuleDestinations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listtopicruledestinationspaginator)
        """

class ListTopicRulesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListTopicRules)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listtopicrulespaginator)
    """

    def paginate(
        self,
        *,
        topic: str = None,
        ruleDisabled: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTopicRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListTopicRules.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listtopicrulespaginator)
        """

class ListV2LoggingLevelsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListV2LoggingLevels)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listv2logginglevelspaginator)
    """

    def paginate(
        self,
        *,
        targetType: LogTargetTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListV2LoggingLevelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListV2LoggingLevels.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listv2logginglevelspaginator)
        """

class ListViolationEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListViolationEvents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listviolationeventspaginator)
    """

    def paginate(
        self,
        *,
        startTime: Union[datetime, str],
        endTime: Union[datetime, str],
        thingName: str = None,
        securityProfileName: str = None,
        behaviorCriteriaType: BehaviorCriteriaTypeType = None,
        listSuppressedAlerts: bool = None,
        verificationState: VerificationStateType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListViolationEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/iot.html#IoT.Paginator.ListViolationEvents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/paginators.html#listviolationeventspaginator)
        """
