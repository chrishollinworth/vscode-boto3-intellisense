# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for iot service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_iot import IoTClient
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
        ListCertificatesPaginator,
        ListCertificatesByCAPaginator,
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
    list_dimensions_paginator: ListDimensionsPaginator = client.get_paginator("list_dimensions")
    list_domain_configurations_paginator: ListDomainConfigurationsPaginator = client.get_paginator("list_domain_configurations")
    list_indices_paginator: ListIndicesPaginator = client.get_paginator("list_indices")
    list_job_executions_for_job_paginator: ListJobExecutionsForJobPaginator = client.get_paginator("list_job_executions_for_job")
    list_job_executions_for_thing_paginator: ListJobExecutionsForThingPaginator = client.get_paginator("list_job_executions_for_thing")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
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
import sys
from datetime import datetime
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_iot.type_defs import (
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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
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
    "ListDimensionsPaginator",
    "ListDomainConfigurationsPaginator",
    "ListIndicesPaginator",
    "ListJobExecutionsForJobPaginator",
    "ListJobExecutionsForThingPaginator",
    "ListJobsPaginator",
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


class ListActiveViolationsPaginator(Boto3Paginator):
    """
    [Paginator.ListActiveViolations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListActiveViolations)
    """

    def paginate(
        self,
        thingName: str = None,
        securityProfileName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListActiveViolationsResponseTypeDef]:
        """
        [ListActiveViolations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListActiveViolations.paginate)
        """


class ListAttachedPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListAttachedPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListAttachedPolicies)
    """

    def paginate(
        self, target: str, recursive: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAttachedPoliciesResponseTypeDef]:
        """
        [ListAttachedPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListAttachedPolicies.paginate)
        """


class ListAuditFindingsPaginator(Boto3Paginator):
    """
    [Paginator.ListAuditFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListAuditFindings)
    """

    def paginate(
        self,
        taskId: str = None,
        checkName: str = None,
        resourceIdentifier: "ResourceIdentifierTypeDef" = None,
        startTime: datetime = None,
        endTime: datetime = None,
        listSuppressedFindings: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAuditFindingsResponseTypeDef]:
        """
        [ListAuditFindings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListAuditFindings.paginate)
        """


class ListAuditMitigationActionsExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.ListAuditMitigationActionsExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListAuditMitigationActionsExecutions)
    """

    def paginate(
        self,
        taskId: str,
        findingId: str,
        actionStatus: Literal[
            "IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED", "SKIPPED", "PENDING"
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAuditMitigationActionsExecutionsResponseTypeDef]:
        """
        [ListAuditMitigationActionsExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListAuditMitigationActionsExecutions.paginate)
        """


class ListAuditMitigationActionsTasksPaginator(Boto3Paginator):
    """
    [Paginator.ListAuditMitigationActionsTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListAuditMitigationActionsTasks)
    """

    def paginate(
        self,
        startTime: datetime,
        endTime: datetime,
        auditTaskId: str = None,
        findingId: str = None,
        taskStatus: Literal["IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAuditMitigationActionsTasksResponseTypeDef]:
        """
        [ListAuditMitigationActionsTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListAuditMitigationActionsTasks.paginate)
        """


class ListAuditSuppressionsPaginator(Boto3Paginator):
    """
    [Paginator.ListAuditSuppressions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListAuditSuppressions)
    """

    def paginate(
        self,
        checkName: str = None,
        resourceIdentifier: "ResourceIdentifierTypeDef" = None,
        ascendingOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAuditSuppressionsResponseTypeDef]:
        """
        [ListAuditSuppressions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListAuditSuppressions.paginate)
        """


class ListAuditTasksPaginator(Boto3Paginator):
    """
    [Paginator.ListAuditTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListAuditTasks)
    """

    def paginate(
        self,
        startTime: datetime,
        endTime: datetime,
        taskType: Literal["ON_DEMAND_AUDIT_TASK", "SCHEDULED_AUDIT_TASK"] = None,
        taskStatus: Literal["IN_PROGRESS", "COMPLETED", "FAILED", "CANCELED"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAuditTasksResponseTypeDef]:
        """
        [ListAuditTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListAuditTasks.paginate)
        """


class ListAuthorizersPaginator(Boto3Paginator):
    """
    [Paginator.ListAuthorizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListAuthorizers)
    """

    def paginate(
        self,
        ascendingOrder: bool = None,
        status: Literal["ACTIVE", "INACTIVE"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAuthorizersResponseTypeDef]:
        """
        [ListAuthorizers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListAuthorizers.paginate)
        """


class ListBillingGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListBillingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListBillingGroups)
    """

    def paginate(
        self, namePrefixFilter: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBillingGroupsResponseTypeDef]:
        """
        [ListBillingGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListBillingGroups.paginate)
        """


class ListCACertificatesPaginator(Boto3Paginator):
    """
    [Paginator.ListCACertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListCACertificates)
    """

    def paginate(
        self, ascendingOrder: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCACertificatesResponseTypeDef]:
        """
        [ListCACertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListCACertificates.paginate)
        """


class ListCertificatesPaginator(Boto3Paginator):
    """
    [Paginator.ListCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListCertificates)
    """

    def paginate(
        self, ascendingOrder: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCertificatesResponseTypeDef]:
        """
        [ListCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListCertificates.paginate)
        """


class ListCertificatesByCAPaginator(Boto3Paginator):
    """
    [Paginator.ListCertificatesByCA documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListCertificatesByCA)
    """

    def paginate(
        self,
        caCertificateId: str,
        ascendingOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListCertificatesByCAResponseTypeDef]:
        """
        [ListCertificatesByCA.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListCertificatesByCA.paginate)
        """


class ListDimensionsPaginator(Boto3Paginator):
    """
    [Paginator.ListDimensions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListDimensions)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDimensionsResponseTypeDef]:
        """
        [ListDimensions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListDimensions.paginate)
        """


class ListDomainConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.ListDomainConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListDomainConfigurations)
    """

    def paginate(
        self,
        serviceType: Literal["DATA", "CREDENTIAL_PROVIDER", "JOBS"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDomainConfigurationsResponseTypeDef]:
        """
        [ListDomainConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListDomainConfigurations.paginate)
        """


class ListIndicesPaginator(Boto3Paginator):
    """
    [Paginator.ListIndices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListIndices)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIndicesResponseTypeDef]:
        """
        [ListIndices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListIndices.paginate)
        """


class ListJobExecutionsForJobPaginator(Boto3Paginator):
    """
    [Paginator.ListJobExecutionsForJob documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForJob)
    """

    def paginate(
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
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListJobExecutionsForJobResponseTypeDef]:
        """
        [ListJobExecutionsForJob.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForJob.paginate)
        """


class ListJobExecutionsForThingPaginator(Boto3Paginator):
    """
    [Paginator.ListJobExecutionsForThing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForThing)
    """

    def paginate(
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
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListJobExecutionsForThingResponseTypeDef]:
        """
        [ListJobExecutionsForThing.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForThing.paginate)
        """


class ListJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListJobs)
    """

    def paginate(
        self,
        status: Literal["IN_PROGRESS", "CANCELED", "COMPLETED", "DELETION_IN_PROGRESS"] = None,
        targetSelection: Literal["CONTINUOUS", "SNAPSHOT"] = None,
        thingGroupName: str = None,
        thingGroupId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListJobsResponseTypeDef]:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListJobs.paginate)
        """


class ListMitigationActionsPaginator(Boto3Paginator):
    """
    [Paginator.ListMitigationActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListMitigationActions)
    """

    def paginate(
        self,
        actionType: Literal[
            "UPDATE_DEVICE_CERTIFICATE",
            "UPDATE_CA_CERTIFICATE",
            "ADD_THINGS_TO_THING_GROUP",
            "REPLACE_DEFAULT_POLICY_VERSION",
            "ENABLE_IOT_LOGGING",
            "PUBLISH_FINDING_TO_SNS",
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListMitigationActionsResponseTypeDef]:
        """
        [ListMitigationActions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListMitigationActions.paginate)
        """


class ListOTAUpdatesPaginator(Boto3Paginator):
    """
    [Paginator.ListOTAUpdates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListOTAUpdates)
    """

    def paginate(
        self,
        otaUpdateStatus: Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "CREATE_FAILED"
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListOTAUpdatesResponseTypeDef]:
        """
        [ListOTAUpdates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListOTAUpdates.paginate)
        """


class ListOutgoingCertificatesPaginator(Boto3Paginator):
    """
    [Paginator.ListOutgoingCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListOutgoingCertificates)
    """

    def paginate(
        self, ascendingOrder: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOutgoingCertificatesResponseTypeDef]:
        """
        [ListOutgoingCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListOutgoingCertificates.paginate)
        """


class ListPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListPolicies)
    """

    def paginate(
        self, ascendingOrder: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPoliciesResponseTypeDef]:
        """
        [ListPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListPolicies.paginate)
        """


class ListPolicyPrincipalsPaginator(Boto3Paginator):
    """
    [Paginator.ListPolicyPrincipals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListPolicyPrincipals)
    """

    def paginate(
        self,
        policyName: str,
        ascendingOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPolicyPrincipalsResponseTypeDef]:
        """
        [ListPolicyPrincipals.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListPolicyPrincipals.paginate)
        """


class ListPrincipalPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListPrincipalPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListPrincipalPolicies)
    """

    def paginate(
        self,
        principal: str,
        ascendingOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPrincipalPoliciesResponseTypeDef]:
        """
        [ListPrincipalPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListPrincipalPolicies.paginate)
        """


class ListPrincipalThingsPaginator(Boto3Paginator):
    """
    [Paginator.ListPrincipalThings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListPrincipalThings)
    """

    def paginate(
        self, principal: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPrincipalThingsResponseTypeDef]:
        """
        [ListPrincipalThings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListPrincipalThings.paginate)
        """


class ListProvisioningTemplateVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListProvisioningTemplateVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListProvisioningTemplateVersions)
    """

    def paginate(
        self, templateName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProvisioningTemplateVersionsResponseTypeDef]:
        """
        [ListProvisioningTemplateVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListProvisioningTemplateVersions.paginate)
        """


class ListProvisioningTemplatesPaginator(Boto3Paginator):
    """
    [Paginator.ListProvisioningTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListProvisioningTemplates)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProvisioningTemplatesResponseTypeDef]:
        """
        [ListProvisioningTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListProvisioningTemplates.paginate)
        """


class ListRoleAliasesPaginator(Boto3Paginator):
    """
    [Paginator.ListRoleAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListRoleAliases)
    """

    def paginate(
        self, ascendingOrder: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRoleAliasesResponseTypeDef]:
        """
        [ListRoleAliases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListRoleAliases.paginate)
        """


class ListScheduledAuditsPaginator(Boto3Paginator):
    """
    [Paginator.ListScheduledAudits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListScheduledAudits)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListScheduledAuditsResponseTypeDef]:
        """
        [ListScheduledAudits.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListScheduledAudits.paginate)
        """


class ListSecurityProfilesPaginator(Boto3Paginator):
    """
    [Paginator.ListSecurityProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListSecurityProfiles)
    """

    def paginate(
        self, dimensionName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSecurityProfilesResponseTypeDef]:
        """
        [ListSecurityProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListSecurityProfiles.paginate)
        """


class ListSecurityProfilesForTargetPaginator(Boto3Paginator):
    """
    [Paginator.ListSecurityProfilesForTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListSecurityProfilesForTarget)
    """

    def paginate(
        self,
        securityProfileTargetArn: str,
        recursive: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListSecurityProfilesForTargetResponseTypeDef]:
        """
        [ListSecurityProfilesForTarget.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListSecurityProfilesForTarget.paginate)
        """


class ListStreamsPaginator(Boto3Paginator):
    """
    [Paginator.ListStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListStreams)
    """

    def paginate(
        self, ascendingOrder: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStreamsResponseTypeDef]:
        """
        [ListStreams.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListStreams.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListTagsForResource)
    """

    def paginate(
        self, resourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListTagsForResource.paginate)
        """


class ListTargetsForPolicyPaginator(Boto3Paginator):
    """
    [Paginator.ListTargetsForPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListTargetsForPolicy)
    """

    def paginate(
        self, policyName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTargetsForPolicyResponseTypeDef]:
        """
        [ListTargetsForPolicy.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListTargetsForPolicy.paginate)
        """


class ListTargetsForSecurityProfilePaginator(Boto3Paginator):
    """
    [Paginator.ListTargetsForSecurityProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListTargetsForSecurityProfile)
    """

    def paginate(
        self, securityProfileName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTargetsForSecurityProfileResponseTypeDef]:
        """
        [ListTargetsForSecurityProfile.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListTargetsForSecurityProfile.paginate)
        """


class ListThingGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListThingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListThingGroups)
    """

    def paginate(
        self,
        parentGroup: str = None,
        namePrefixFilter: str = None,
        recursive: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListThingGroupsResponseTypeDef]:
        """
        [ListThingGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListThingGroups.paginate)
        """


class ListThingGroupsForThingPaginator(Boto3Paginator):
    """
    [Paginator.ListThingGroupsForThing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListThingGroupsForThing)
    """

    def paginate(
        self, thingName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThingGroupsForThingResponseTypeDef]:
        """
        [ListThingGroupsForThing.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListThingGroupsForThing.paginate)
        """


class ListThingRegistrationTaskReportsPaginator(Boto3Paginator):
    """
    [Paginator.ListThingRegistrationTaskReports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListThingRegistrationTaskReports)
    """

    def paginate(
        self,
        taskId: str,
        reportType: Literal["ERRORS", "RESULTS"],
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListThingRegistrationTaskReportsResponseTypeDef]:
        """
        [ListThingRegistrationTaskReports.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListThingRegistrationTaskReports.paginate)
        """


class ListThingRegistrationTasksPaginator(Boto3Paginator):
    """
    [Paginator.ListThingRegistrationTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListThingRegistrationTasks)
    """

    def paginate(
        self,
        status: Literal["InProgress", "Completed", "Failed", "Cancelled", "Cancelling"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListThingRegistrationTasksResponseTypeDef]:
        """
        [ListThingRegistrationTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListThingRegistrationTasks.paginate)
        """


class ListThingTypesPaginator(Boto3Paginator):
    """
    [Paginator.ListThingTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListThingTypes)
    """

    def paginate(
        self, thingTypeName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThingTypesResponseTypeDef]:
        """
        [ListThingTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListThingTypes.paginate)
        """


class ListThingsPaginator(Boto3Paginator):
    """
    [Paginator.ListThings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListThings)
    """

    def paginate(
        self,
        attributeName: str = None,
        attributeValue: str = None,
        thingTypeName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListThingsResponseTypeDef]:
        """
        [ListThings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListThings.paginate)
        """


class ListThingsInBillingGroupPaginator(Boto3Paginator):
    """
    [Paginator.ListThingsInBillingGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListThingsInBillingGroup)
    """

    def paginate(
        self, billingGroupName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThingsInBillingGroupResponseTypeDef]:
        """
        [ListThingsInBillingGroup.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListThingsInBillingGroup.paginate)
        """


class ListThingsInThingGroupPaginator(Boto3Paginator):
    """
    [Paginator.ListThingsInThingGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListThingsInThingGroup)
    """

    def paginate(
        self,
        thingGroupName: str,
        recursive: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListThingsInThingGroupResponseTypeDef]:
        """
        [ListThingsInThingGroup.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListThingsInThingGroup.paginate)
        """


class ListTopicRuleDestinationsPaginator(Boto3Paginator):
    """
    [Paginator.ListTopicRuleDestinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListTopicRuleDestinations)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTopicRuleDestinationsResponseTypeDef]:
        """
        [ListTopicRuleDestinations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListTopicRuleDestinations.paginate)
        """


class ListTopicRulesPaginator(Boto3Paginator):
    """
    [Paginator.ListTopicRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListTopicRules)
    """

    def paginate(
        self,
        topic: str = None,
        ruleDisabled: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTopicRulesResponseTypeDef]:
        """
        [ListTopicRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListTopicRules.paginate)
        """


class ListV2LoggingLevelsPaginator(Boto3Paginator):
    """
    [Paginator.ListV2LoggingLevels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListV2LoggingLevels)
    """

    def paginate(
        self,
        targetType: Literal["DEFAULT", "THING_GROUP"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListV2LoggingLevelsResponseTypeDef]:
        """
        [ListV2LoggingLevels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListV2LoggingLevels.paginate)
        """


class ListViolationEventsPaginator(Boto3Paginator):
    """
    [Paginator.ListViolationEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListViolationEvents)
    """

    def paginate(
        self,
        startTime: datetime,
        endTime: datetime,
        thingName: str = None,
        securityProfileName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListViolationEventsResponseTypeDef]:
        """
        [ListViolationEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot.html#IoT.Paginator.ListViolationEvents.paginate)
        """
