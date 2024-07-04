"""
Type annotations for deadline service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_deadline import DeadlineCloudClient

    client: DeadlineCloudClient = boto3.client("deadline")
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    BudgetStatusType,
    CreateJobTargetTaskRunStatusType,
    DefaultQueueBudgetActionType,
    EnvironmentTemplateTypeType,
    FleetStatusType,
    JobTargetTaskRunStatusType,
    JobTemplateTypeType,
    MembershipLevelType,
    PeriodType,
    PrincipalTypeType,
    QueueStatusType,
    StepTargetTaskRunStatusType,
    StorageProfileOperatingSystemFamilyType,
    TaskTargetRunStatusType,
    UpdatedWorkerStatusType,
    UpdateQueueFleetAssociationStatusType,
    UsageGroupByFieldType,
    UsageStatisticType,
)
from .paginator import (
    GetSessionsStatisticsAggregationPaginator,
    ListAvailableMeteredProductsPaginator,
    ListBudgetsPaginator,
    ListFarmMembersPaginator,
    ListFarmsPaginator,
    ListFleetMembersPaginator,
    ListFleetsPaginator,
    ListJobMembersPaginator,
    ListJobsPaginator,
    ListLicenseEndpointsPaginator,
    ListMeteredProductsPaginator,
    ListMonitorsPaginator,
    ListQueueEnvironmentsPaginator,
    ListQueueFleetAssociationsPaginator,
    ListQueueMembersPaginator,
    ListQueuesPaginator,
    ListSessionActionsPaginator,
    ListSessionsForWorkerPaginator,
    ListSessionsPaginator,
    ListStepConsumersPaginator,
    ListStepDependenciesPaginator,
    ListStepsPaginator,
    ListStorageProfilesForQueuePaginator,
    ListStorageProfilesPaginator,
    ListTasksPaginator,
    ListWorkersPaginator,
)
from .type_defs import (
    AssumeFleetRoleForReadResponseTypeDef,
    AssumeFleetRoleForWorkerResponseTypeDef,
    AssumeQueueRoleForReadResponseTypeDef,
    AssumeQueueRoleForUserResponseTypeDef,
    AssumeQueueRoleForWorkerResponseTypeDef,
    AttachmentsTypeDef,
    BatchGetJobEntityResponseTypeDef,
    BudgetActionToAddTypeDef,
    BudgetActionToRemoveTypeDef,
    BudgetScheduleTypeDef,
    CopyJobTemplateResponseTypeDef,
    CreateBudgetResponseTypeDef,
    CreateFarmResponseTypeDef,
    CreateFleetResponseTypeDef,
    CreateJobResponseTypeDef,
    CreateLicenseEndpointResponseTypeDef,
    CreateMonitorResponseTypeDef,
    CreateQueueEnvironmentResponseTypeDef,
    CreateQueueResponseTypeDef,
    CreateStorageProfileResponseTypeDef,
    CreateWorkerResponseTypeDef,
    FileSystemLocationTypeDef,
    FleetConfigurationTypeDef,
    GetBudgetResponseTypeDef,
    GetFarmResponseTypeDef,
    GetFleetResponseTypeDef,
    GetJobResponseTypeDef,
    GetLicenseEndpointResponseTypeDef,
    GetMonitorResponseTypeDef,
    GetQueueEnvironmentResponseTypeDef,
    GetQueueFleetAssociationResponseTypeDef,
    GetQueueResponseTypeDef,
    GetSessionActionResponseTypeDef,
    GetSessionResponseTypeDef,
    GetSessionsStatisticsAggregationResponseTypeDef,
    GetStepResponseTypeDef,
    GetStorageProfileForQueueResponseTypeDef,
    GetStorageProfileResponseTypeDef,
    GetTaskResponseTypeDef,
    GetWorkerResponseTypeDef,
    HostPropertiesRequestTypeDef,
    JobAttachmentSettingsTypeDef,
    JobEntityIdentifiersUnionTypeDef,
    JobParameterTypeDef,
    JobRunAsUserTypeDef,
    ListAvailableMeteredProductsResponseTypeDef,
    ListBudgetsResponseTypeDef,
    ListFarmMembersResponseTypeDef,
    ListFarmsResponseTypeDef,
    ListFleetMembersResponseTypeDef,
    ListFleetsResponseTypeDef,
    ListJobMembersResponseTypeDef,
    ListJobsResponseTypeDef,
    ListLicenseEndpointsResponseTypeDef,
    ListMeteredProductsResponseTypeDef,
    ListMonitorsResponseTypeDef,
    ListQueueEnvironmentsResponseTypeDef,
    ListQueueFleetAssociationsResponseTypeDef,
    ListQueueMembersResponseTypeDef,
    ListQueuesResponseTypeDef,
    ListSessionActionsResponseTypeDef,
    ListSessionsForWorkerResponseTypeDef,
    ListSessionsResponseTypeDef,
    ListStepConsumersResponseTypeDef,
    ListStepDependenciesResponseTypeDef,
    ListStepsResponseTypeDef,
    ListStorageProfilesForQueueResponseTypeDef,
    ListStorageProfilesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTasksResponseTypeDef,
    ListWorkersResponseTypeDef,
    S3LocationTypeDef,
    SearchGroupedFilterExpressionsTypeDef,
    SearchJobsResponseTypeDef,
    SearchSortExpressionTypeDef,
    SearchStepsResponseTypeDef,
    SearchTasksResponseTypeDef,
    SearchWorkersResponseTypeDef,
    SessionsStatisticsResourcesTypeDef,
    StartSessionsStatisticsAggregationResponseTypeDef,
    UpdatedSessionActionInfoTypeDef,
    UpdateWorkerResponseTypeDef,
    UpdateWorkerScheduleResponseTypeDef,
    UsageTrackingResourceTypeDef,
    WorkerCapabilitiesTypeDef,
)
from .waiter import (
    FleetActiveWaiter,
    JobCreateCompleteWaiter,
    LicenseEndpointDeletedWaiter,
    LicenseEndpointValidWaiter,
    QueueFleetAssociationStoppedWaiter,
    QueueSchedulingBlockedWaiter,
    QueueSchedulingWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("DeadlineCloudClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class DeadlineCloudClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DeadlineCloudClient exceptions.
        """

    def associate_member_to_farm(
        self,
        *,
        farmId: str,
        identityStoreId: str,
        membershipLevel: MembershipLevelType,
        principalId: str,
        principalType: PrincipalTypeType
    ) -> Dict[str, Any]:
        """
        Assigns a farm membership level to a member.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.associate_member_to_farm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#associate_member_to_farm)
        """

    def associate_member_to_fleet(
        self,
        *,
        farmId: str,
        fleetId: str,
        identityStoreId: str,
        membershipLevel: MembershipLevelType,
        principalId: str,
        principalType: PrincipalTypeType
    ) -> Dict[str, Any]:
        """
        Assigns a fleet membership level to a member.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.associate_member_to_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#associate_member_to_fleet)
        """

    def associate_member_to_job(
        self,
        *,
        farmId: str,
        identityStoreId: str,
        jobId: str,
        membershipLevel: MembershipLevelType,
        principalId: str,
        principalType: PrincipalTypeType,
        queueId: str
    ) -> Dict[str, Any]:
        """
        Assigns a job membership level to a member See also: `AWS API Documentation <htt
        ps://docs.aws.amazon.com/goto/WebAPI/deadline-2023-10-12/AssociateMemberToJob>`_
        **Request Syntax** response = client.associate_member_to_job( farmId='string',
        identityStoreId='string', jo...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.associate_member_to_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#associate_member_to_job)
        """

    def associate_member_to_queue(
        self,
        *,
        farmId: str,
        identityStoreId: str,
        membershipLevel: MembershipLevelType,
        principalId: str,
        principalType: PrincipalTypeType,
        queueId: str
    ) -> Dict[str, Any]:
        """
        Assigns a queue membership level to a member See also: `AWS API Documentation <h
        ttps://docs.aws.amazon.com/goto/WebAPI/deadline-2023-10-
        12/AssociateMemberToQueue>`_ **Request Syntax** response =
        client.associate_member_to_queue( farmId='string', identityStoreId='string', ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.associate_member_to_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#associate_member_to_queue)
        """

    def assume_fleet_role_for_read(
        self, *, farmId: str, fleetId: str
    ) -> AssumeFleetRoleForReadResponseTypeDef:
        """
        Get Amazon Web Services credentials from the fleet role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.assume_fleet_role_for_read)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#assume_fleet_role_for_read)
        """

    def assume_fleet_role_for_worker(
        self, *, farmId: str, fleetId: str, workerId: str
    ) -> AssumeFleetRoleForWorkerResponseTypeDef:
        """
        Get credentials from the fleet role for a worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.assume_fleet_role_for_worker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#assume_fleet_role_for_worker)
        """

    def assume_queue_role_for_read(
        self, *, farmId: str, queueId: str
    ) -> AssumeQueueRoleForReadResponseTypeDef:
        """
        Gets Amazon Web Services credentials from the queue role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.assume_queue_role_for_read)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#assume_queue_role_for_read)
        """

    def assume_queue_role_for_user(
        self, *, farmId: str, queueId: str
    ) -> AssumeQueueRoleForUserResponseTypeDef:
        """
        Allows a user to assume a role for a queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.assume_queue_role_for_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#assume_queue_role_for_user)
        """

    def assume_queue_role_for_worker(
        self, *, farmId: str, fleetId: str, queueId: str, workerId: str
    ) -> AssumeQueueRoleForWorkerResponseTypeDef:
        """
        Allows a worker to assume a queue role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.assume_queue_role_for_worker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#assume_queue_role_for_worker)
        """

    def batch_get_job_entity(
        self,
        *,
        farmId: str,
        fleetId: str,
        identifiers: List["JobEntityIdentifiersUnionTypeDef"],
        workerId: str
    ) -> BatchGetJobEntityResponseTypeDef:
        """
        Get batched job details for a worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.batch_get_job_entity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#batch_get_job_entity)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#close)
        """

    def copy_job_template(
        self, *, farmId: str, jobId: str, queueId: str, targetS3Location: "S3LocationTypeDef"
    ) -> CopyJobTemplateResponseTypeDef:
        """
        Copies a job template to an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.copy_job_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#copy_job_template)
        """

    def create_budget(
        self,
        *,
        actions: List["BudgetActionToAddTypeDef"],
        approximateDollarLimit: float,
        displayName: str,
        farmId: str,
        schedule: "BudgetScheduleTypeDef",
        usageTrackingResource: "UsageTrackingResourceTypeDef",
        clientToken: str = None,
        description: str = None
    ) -> CreateBudgetResponseTypeDef:
        """
        Creates a budget to set spending thresholds for your rendering activity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.create_budget)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#create_budget)
        """

    def create_farm(
        self,
        *,
        displayName: str,
        clientToken: str = None,
        description: str = None,
        kmsKeyArn: str = None,
        tags: Dict[str, str] = None
    ) -> CreateFarmResponseTypeDef:
        """
        Creates a farm to allow space for queues and fleets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.create_farm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#create_farm)
        """

    def create_fleet(
        self,
        *,
        configuration: "FleetConfigurationTypeDef",
        displayName: str,
        farmId: str,
        maxWorkerCount: int,
        roleArn: str,
        clientToken: str = None,
        description: str = None,
        minWorkerCount: int = None,
        tags: Dict[str, str] = None
    ) -> CreateFleetResponseTypeDef:
        """
        Creates a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.create_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#create_fleet)
        """

    def create_job(
        self,
        *,
        farmId: str,
        priority: int,
        queueId: str,
        template: str,
        templateType: JobTemplateTypeType,
        attachments: "AttachmentsTypeDef" = None,
        clientToken: str = None,
        maxFailedTasksCount: int = None,
        maxRetriesPerTask: int = None,
        parameters: Dict[str, "JobParameterTypeDef"] = None,
        storageProfileId: str = None,
        targetTaskRunStatus: CreateJobTargetTaskRunStatusType = None
    ) -> CreateJobResponseTypeDef:
        """
        Creates a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.create_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#create_job)
        """

    def create_license_endpoint(
        self,
        *,
        securityGroupIds: List[str],
        subnetIds: List[str],
        vpcId: str,
        clientToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreateLicenseEndpointResponseTypeDef:
        """
        Creates a license endpoint to integrate your various licensed software used for
        rendering on Deadline Cloud.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.create_license_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#create_license_endpoint)
        """

    def create_monitor(
        self,
        *,
        displayName: str,
        identityCenterInstanceArn: str,
        roleArn: str,
        subdomain: str,
        clientToken: str = None
    ) -> CreateMonitorResponseTypeDef:
        """
        Creates an Amazon Web Services Deadline Cloud monitor that you can use to view
        your farms, queues, and fleets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.create_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#create_monitor)
        """

    def create_queue(
        self,
        *,
        displayName: str,
        farmId: str,
        allowedStorageProfileIds: List[str] = None,
        clientToken: str = None,
        defaultBudgetAction: DefaultQueueBudgetActionType = None,
        description: str = None,
        jobAttachmentSettings: "JobAttachmentSettingsTypeDef" = None,
        jobRunAsUser: "JobRunAsUserTypeDef" = None,
        requiredFileSystemLocationNames: List[str] = None,
        roleArn: str = None,
        tags: Dict[str, str] = None
    ) -> CreateQueueResponseTypeDef:
        """
        Creates a queue to coordinate the order in which jobs run on a farm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.create_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#create_queue)
        """

    def create_queue_environment(
        self,
        *,
        farmId: str,
        priority: int,
        queueId: str,
        template: str,
        templateType: EnvironmentTemplateTypeType,
        clientToken: str = None
    ) -> CreateQueueEnvironmentResponseTypeDef:
        """
        Creates an environment for a queue that defines how jobs in the queue run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.create_queue_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#create_queue_environment)
        """

    def create_queue_fleet_association(
        self, *, farmId: str, fleetId: str, queueId: str
    ) -> Dict[str, Any]:
        """
        Creates an association between a queue and a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.create_queue_fleet_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#create_queue_fleet_association)
        """

    def create_storage_profile(
        self,
        *,
        displayName: str,
        farmId: str,
        osFamily: StorageProfileOperatingSystemFamilyType,
        clientToken: str = None,
        fileSystemLocations: List["FileSystemLocationTypeDef"] = None
    ) -> CreateStorageProfileResponseTypeDef:
        """
        Creates a storage profile that specifies the operating system, file type, and
        file location of resources used on a farm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.create_storage_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#create_storage_profile)
        """

    def create_worker(
        self,
        *,
        farmId: str,
        fleetId: str,
        clientToken: str = None,
        hostProperties: "HostPropertiesRequestTypeDef" = None
    ) -> CreateWorkerResponseTypeDef:
        """
        Creates a worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.create_worker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#create_worker)
        """

    def delete_budget(self, *, budgetId: str, farmId: str) -> Dict[str, Any]:
        """
        Deletes a budget.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.delete_budget)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#delete_budget)
        """

    def delete_farm(self, *, farmId: str) -> Dict[str, Any]:
        """
        Deletes a farm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.delete_farm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#delete_farm)
        """

    def delete_fleet(self, *, farmId: str, fleetId: str, clientToken: str = None) -> Dict[str, Any]:
        """
        Deletes a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.delete_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#delete_fleet)
        """

    def delete_license_endpoint(self, *, licenseEndpointId: str) -> Dict[str, Any]:
        """
        Deletes a license endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.delete_license_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#delete_license_endpoint)
        """

    def delete_metered_product(self, *, licenseEndpointId: str, productId: str) -> Dict[str, Any]:
        """
        Deletes a metered product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.delete_metered_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#delete_metered_product)
        """

    def delete_monitor(self, *, monitorId: str) -> Dict[str, Any]:
        """
        Removes a Deadline Cloud monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.delete_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#delete_monitor)
        """

    def delete_queue(self, *, farmId: str, queueId: str) -> Dict[str, Any]:
        """
        Deletes a queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.delete_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#delete_queue)
        """

    def delete_queue_environment(
        self, *, farmId: str, queueEnvironmentId: str, queueId: str
    ) -> Dict[str, Any]:
        """
        Deletes a queue environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.delete_queue_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#delete_queue_environment)
        """

    def delete_queue_fleet_association(
        self, *, farmId: str, fleetId: str, queueId: str
    ) -> Dict[str, Any]:
        """
        Deletes a queue-fleet association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.delete_queue_fleet_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#delete_queue_fleet_association)
        """

    def delete_storage_profile(self, *, farmId: str, storageProfileId: str) -> Dict[str, Any]:
        """
        Deletes a storage profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.delete_storage_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#delete_storage_profile)
        """

    def delete_worker(self, *, farmId: str, fleetId: str, workerId: str) -> Dict[str, Any]:
        """
        Deletes a worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.delete_worker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#delete_worker)
        """

    def disassociate_member_from_farm(self, *, farmId: str, principalId: str) -> Dict[str, Any]:
        """
        Disassociates a member from a farm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.disassociate_member_from_farm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#disassociate_member_from_farm)
        """

    def disassociate_member_from_fleet(
        self, *, farmId: str, fleetId: str, principalId: str
    ) -> Dict[str, Any]:
        """
        Disassociates a member from a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.disassociate_member_from_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#disassociate_member_from_fleet)
        """

    def disassociate_member_from_job(
        self, *, farmId: str, jobId: str, principalId: str, queueId: str
    ) -> Dict[str, Any]:
        """
        Disassociates a member from a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.disassociate_member_from_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#disassociate_member_from_job)
        """

    def disassociate_member_from_queue(
        self, *, farmId: str, principalId: str, queueId: str
    ) -> Dict[str, Any]:
        """
        Disassociates a member from a queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.disassociate_member_from_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#disassociate_member_from_queue)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#generate_presigned_url)
        """

    def get_budget(self, *, budgetId: str, farmId: str) -> GetBudgetResponseTypeDef:
        """
        Get a budget.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.get_budget)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#get_budget)
        """

    def get_farm(self, *, farmId: str) -> GetFarmResponseTypeDef:
        """
        Get a farm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.get_farm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#get_farm)
        """

    def get_fleet(self, *, farmId: str, fleetId: str) -> GetFleetResponseTypeDef:
        """
        Get a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.get_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#get_fleet)
        """

    def get_job(self, *, farmId: str, jobId: str, queueId: str) -> GetJobResponseTypeDef:
        """
        Gets a Deadline Cloud job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.get_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#get_job)
        """

    def get_license_endpoint(self, *, licenseEndpointId: str) -> GetLicenseEndpointResponseTypeDef:
        """
        Gets a licence endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.get_license_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#get_license_endpoint)
        """

    def get_monitor(self, *, monitorId: str) -> GetMonitorResponseTypeDef:
        """
        Gets information about the specified monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.get_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#get_monitor)
        """

    def get_queue(self, *, farmId: str, queueId: str) -> GetQueueResponseTypeDef:
        """
        Gets a queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.get_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#get_queue)
        """

    def get_queue_environment(
        self, *, farmId: str, queueEnvironmentId: str, queueId: str
    ) -> GetQueueEnvironmentResponseTypeDef:
        """
        Gets a queue environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.get_queue_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#get_queue_environment)
        """

    def get_queue_fleet_association(
        self, *, farmId: str, fleetId: str, queueId: str
    ) -> GetQueueFleetAssociationResponseTypeDef:
        """
        Gets a queue-fleet association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.get_queue_fleet_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#get_queue_fleet_association)
        """

    def get_session(
        self, *, farmId: str, jobId: str, queueId: str, sessionId: str
    ) -> GetSessionResponseTypeDef:
        """
        Gets a session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.get_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#get_session)
        """

    def get_session_action(
        self, *, farmId: str, jobId: str, queueId: str, sessionActionId: str
    ) -> GetSessionActionResponseTypeDef:
        """
        Gets a session action for the job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.get_session_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#get_session_action)
        """

    def get_sessions_statistics_aggregation(
        self, *, aggregationId: str, farmId: str, maxResults: int = None, nextToken: str = None
    ) -> GetSessionsStatisticsAggregationResponseTypeDef:
        """
        Gets a set of statistics for queues or farms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.get_sessions_statistics_aggregation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#get_sessions_statistics_aggregation)
        """

    def get_step(
        self, *, farmId: str, jobId: str, queueId: str, stepId: str
    ) -> GetStepResponseTypeDef:
        """
        Gets a step.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.get_step)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#get_step)
        """

    def get_storage_profile(
        self, *, farmId: str, storageProfileId: str
    ) -> GetStorageProfileResponseTypeDef:
        """
        Gets a storage profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.get_storage_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#get_storage_profile)
        """

    def get_storage_profile_for_queue(
        self, *, farmId: str, queueId: str, storageProfileId: str
    ) -> GetStorageProfileForQueueResponseTypeDef:
        """
        Gets a storage profile for a queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.get_storage_profile_for_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#get_storage_profile_for_queue)
        """

    def get_task(
        self, *, farmId: str, jobId: str, queueId: str, stepId: str, taskId: str
    ) -> GetTaskResponseTypeDef:
        """
        Gets a task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.get_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#get_task)
        """

    def get_worker(self, *, farmId: str, fleetId: str, workerId: str) -> GetWorkerResponseTypeDef:
        """
        Gets a worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.get_worker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#get_worker)
        """

    def list_available_metered_products(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListAvailableMeteredProductsResponseTypeDef:
        """
        A list of the available metered products.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_available_metered_products)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_available_metered_products)
        """

    def list_budgets(
        self,
        *,
        farmId: str,
        maxResults: int = None,
        nextToken: str = None,
        status: BudgetStatusType = None
    ) -> ListBudgetsResponseTypeDef:
        """
        A list of budgets in a farm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_budgets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_budgets)
        """

    def list_farm_members(
        self, *, farmId: str, maxResults: int = None, nextToken: str = None
    ) -> ListFarmMembersResponseTypeDef:
        """
        Lists the members of a farm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_farm_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_farm_members)
        """

    def list_farms(
        self, *, maxResults: int = None, nextToken: str = None, principalId: str = None
    ) -> ListFarmsResponseTypeDef:
        """
        Lists farms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_farms)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_farms)
        """

    def list_fleet_members(
        self, *, farmId: str, fleetId: str, maxResults: int = None, nextToken: str = None
    ) -> ListFleetMembersResponseTypeDef:
        """
        Lists fleet members.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_fleet_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_fleet_members)
        """

    def list_fleets(
        self,
        *,
        farmId: str,
        displayName: str = None,
        maxResults: int = None,
        nextToken: str = None,
        principalId: str = None,
        status: FleetStatusType = None
    ) -> ListFleetsResponseTypeDef:
        """
        Lists fleets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_fleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_fleets)
        """

    def list_job_members(
        self,
        *,
        farmId: str,
        jobId: str,
        queueId: str,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListJobMembersResponseTypeDef:
        """
        Lists members on a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_job_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_job_members)
        """

    def list_jobs(
        self,
        *,
        farmId: str,
        queueId: str,
        maxResults: int = None,
        nextToken: str = None,
        principalId: str = None
    ) -> ListJobsResponseTypeDef:
        """
        Lists jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_jobs)
        """

    def list_license_endpoints(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListLicenseEndpointsResponseTypeDef:
        """
        Lists license endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_license_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_license_endpoints)
        """

    def list_metered_products(
        self, *, licenseEndpointId: str, maxResults: int = None, nextToken: str = None
    ) -> ListMeteredProductsResponseTypeDef:
        """
        Lists metered products.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_metered_products)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_metered_products)
        """

    def list_monitors(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListMonitorsResponseTypeDef:
        """
        Gets a list of your monitors in Deadline Cloud.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_monitors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_monitors)
        """

    def list_queue_environments(
        self, *, farmId: str, queueId: str, maxResults: int = None, nextToken: str = None
    ) -> ListQueueEnvironmentsResponseTypeDef:
        """
        Lists queue environments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_queue_environments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_queue_environments)
        """

    def list_queue_fleet_associations(
        self,
        *,
        farmId: str,
        fleetId: str = None,
        maxResults: int = None,
        nextToken: str = None,
        queueId: str = None
    ) -> ListQueueFleetAssociationsResponseTypeDef:
        """
        Lists queue-fleet associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_queue_fleet_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_queue_fleet_associations)
        """

    def list_queue_members(
        self, *, farmId: str, queueId: str, maxResults: int = None, nextToken: str = None
    ) -> ListQueueMembersResponseTypeDef:
        """
        Lists the members in a queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_queue_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_queue_members)
        """

    def list_queues(
        self,
        *,
        farmId: str,
        maxResults: int = None,
        nextToken: str = None,
        principalId: str = None,
        status: QueueStatusType = None
    ) -> ListQueuesResponseTypeDef:
        """
        Lists queues.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_queues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_queues)
        """

    def list_session_actions(
        self,
        *,
        farmId: str,
        jobId: str,
        queueId: str,
        maxResults: int = None,
        nextToken: str = None,
        sessionId: str = None,
        taskId: str = None
    ) -> ListSessionActionsResponseTypeDef:
        """
        Lists session actions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_session_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_session_actions)
        """

    def list_sessions(
        self,
        *,
        farmId: str,
        jobId: str,
        queueId: str,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListSessionsResponseTypeDef:
        """
        Lists sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_sessions)
        """

    def list_sessions_for_worker(
        self,
        *,
        farmId: str,
        fleetId: str,
        workerId: str,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListSessionsForWorkerResponseTypeDef:
        """
        Lists sessions for a worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_sessions_for_worker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_sessions_for_worker)
        """

    def list_step_consumers(
        self,
        *,
        farmId: str,
        jobId: str,
        queueId: str,
        stepId: str,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListStepConsumersResponseTypeDef:
        """
        Lists step consumers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_step_consumers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_step_consumers)
        """

    def list_step_dependencies(
        self,
        *,
        farmId: str,
        jobId: str,
        queueId: str,
        stepId: str,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListStepDependenciesResponseTypeDef:
        """
        Lists the dependencies for a step.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_step_dependencies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_step_dependencies)
        """

    def list_steps(
        self,
        *,
        farmId: str,
        jobId: str,
        queueId: str,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListStepsResponseTypeDef:
        """
        Lists steps for a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_steps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_steps)
        """

    def list_storage_profiles(
        self, *, farmId: str, maxResults: int = None, nextToken: str = None
    ) -> ListStorageProfilesResponseTypeDef:
        """
        Lists storage profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_storage_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_storage_profiles)
        """

    def list_storage_profiles_for_queue(
        self, *, farmId: str, queueId: str, maxResults: int = None, nextToken: str = None
    ) -> ListStorageProfilesForQueueResponseTypeDef:
        """
        Lists storage profiles for a queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_storage_profiles_for_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_storage_profiles_for_queue)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_tags_for_resource)
        """

    def list_tasks(
        self,
        *,
        farmId: str,
        jobId: str,
        queueId: str,
        stepId: str,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListTasksResponseTypeDef:
        """
        Lists tasks for a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_tasks)
        """

    def list_workers(
        self, *, farmId: str, fleetId: str, maxResults: int = None, nextToken: str = None
    ) -> ListWorkersResponseTypeDef:
        """
        Lists workers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.list_workers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#list_workers)
        """

    def put_metered_product(self, *, licenseEndpointId: str, productId: str) -> Dict[str, Any]:
        """
        Adds a metered product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.put_metered_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#put_metered_product)
        """

    def search_jobs(
        self,
        *,
        farmId: str,
        itemOffset: int,
        queueIds: List[str],
        filterExpressions: "SearchGroupedFilterExpressionsTypeDef" = None,
        pageSize: int = None,
        sortExpressions: List["SearchSortExpressionTypeDef"] = None
    ) -> SearchJobsResponseTypeDef:
        """
        Searches for jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.search_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#search_jobs)
        """

    def search_steps(
        self,
        *,
        farmId: str,
        itemOffset: int,
        queueIds: List[str],
        filterExpressions: "SearchGroupedFilterExpressionsTypeDef" = None,
        jobId: str = None,
        pageSize: int = None,
        sortExpressions: List["SearchSortExpressionTypeDef"] = None
    ) -> SearchStepsResponseTypeDef:
        """
        Searches for steps.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.search_steps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#search_steps)
        """

    def search_tasks(
        self,
        *,
        farmId: str,
        itemOffset: int,
        queueIds: List[str],
        filterExpressions: "SearchGroupedFilterExpressionsTypeDef" = None,
        jobId: str = None,
        pageSize: int = None,
        sortExpressions: List["SearchSortExpressionTypeDef"] = None
    ) -> SearchTasksResponseTypeDef:
        """
        Searches for tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.search_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#search_tasks)
        """

    def search_workers(
        self,
        *,
        farmId: str,
        fleetIds: List[str],
        itemOffset: int,
        filterExpressions: "SearchGroupedFilterExpressionsTypeDef" = None,
        pageSize: int = None,
        sortExpressions: List["SearchSortExpressionTypeDef"] = None
    ) -> SearchWorkersResponseTypeDef:
        """
        Searches for workers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.search_workers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#search_workers)
        """

    def start_sessions_statistics_aggregation(
        self,
        *,
        endTime: Union[datetime, str],
        farmId: str,
        groupBy: List[UsageGroupByFieldType],
        resourceIds: "SessionsStatisticsResourcesTypeDef",
        startTime: Union[datetime, str],
        statistics: List[UsageStatisticType],
        period: PeriodType = None,
        timezone: str = None
    ) -> StartSessionsStatisticsAggregationResponseTypeDef:
        """
        Starts an asynchronous request for getting aggregated statistics about queues
        and farms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.start_sessions_statistics_aggregation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#start_sessions_statistics_aggregation)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str] = None) -> Dict[str, Any]:
        """
        Tags a resource using the resource's ARN and desired tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag from a resource using the resource's ARN and tag to remove.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#untag_resource)
        """

    def update_budget(
        self,
        *,
        budgetId: str,
        farmId: str,
        actionsToAdd: List["BudgetActionToAddTypeDef"] = None,
        actionsToRemove: List["BudgetActionToRemoveTypeDef"] = None,
        approximateDollarLimit: float = None,
        clientToken: str = None,
        description: str = None,
        displayName: str = None,
        schedule: "BudgetScheduleTypeDef" = None,
        status: BudgetStatusType = None
    ) -> Dict[str, Any]:
        """
        Updates a budget that sets spending thresholds for rendering activity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.update_budget)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#update_budget)
        """

    def update_farm(
        self, *, farmId: str, description: str = None, displayName: str = None
    ) -> Dict[str, Any]:
        """
        Updates a farm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.update_farm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#update_farm)
        """

    def update_fleet(
        self,
        *,
        farmId: str,
        fleetId: str,
        clientToken: str = None,
        configuration: "FleetConfigurationTypeDef" = None,
        description: str = None,
        displayName: str = None,
        maxWorkerCount: int = None,
        minWorkerCount: int = None,
        roleArn: str = None
    ) -> Dict[str, Any]:
        """
        Updates a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.update_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#update_fleet)
        """

    def update_job(
        self,
        *,
        farmId: str,
        jobId: str,
        queueId: str,
        clientToken: str = None,
        lifecycleStatus: Literal["ARCHIVED"] = None,
        maxFailedTasksCount: int = None,
        maxRetriesPerTask: int = None,
        priority: int = None,
        targetTaskRunStatus: JobTargetTaskRunStatusType = None
    ) -> Dict[str, Any]:
        """
        Updates a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.update_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#update_job)
        """

    def update_monitor(
        self, *, monitorId: str, displayName: str = None, roleArn: str = None, subdomain: str = None
    ) -> Dict[str, Any]:
        """
        Modifies the settings for a Deadline Cloud monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.update_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#update_monitor)
        """

    def update_queue(
        self,
        *,
        farmId: str,
        queueId: str,
        allowedStorageProfileIdsToAdd: List[str] = None,
        allowedStorageProfileIdsToRemove: List[str] = None,
        clientToken: str = None,
        defaultBudgetAction: DefaultQueueBudgetActionType = None,
        description: str = None,
        displayName: str = None,
        jobAttachmentSettings: "JobAttachmentSettingsTypeDef" = None,
        jobRunAsUser: "JobRunAsUserTypeDef" = None,
        requiredFileSystemLocationNamesToAdd: List[str] = None,
        requiredFileSystemLocationNamesToRemove: List[str] = None,
        roleArn: str = None
    ) -> Dict[str, Any]:
        """
        Updates a queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.update_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#update_queue)
        """

    def update_queue_environment(
        self,
        *,
        farmId: str,
        queueEnvironmentId: str,
        queueId: str,
        clientToken: str = None,
        priority: int = None,
        template: str = None,
        templateType: EnvironmentTemplateTypeType = None
    ) -> Dict[str, Any]:
        """
        Updates the queue environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.update_queue_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#update_queue_environment)
        """

    def update_queue_fleet_association(
        self,
        *,
        farmId: str,
        fleetId: str,
        queueId: str,
        status: UpdateQueueFleetAssociationStatusType
    ) -> Dict[str, Any]:
        """
        Updates a queue-fleet association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.update_queue_fleet_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#update_queue_fleet_association)
        """

    def update_session(
        self,
        *,
        farmId: str,
        jobId: str,
        queueId: str,
        sessionId: str,
        targetLifecycleStatus: Literal["ENDED"],
        clientToken: str = None
    ) -> Dict[str, Any]:
        """
        Updates a session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.update_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#update_session)
        """

    def update_step(
        self,
        *,
        farmId: str,
        jobId: str,
        queueId: str,
        stepId: str,
        targetTaskRunStatus: StepTargetTaskRunStatusType,
        clientToken: str = None
    ) -> Dict[str, Any]:
        """
        Updates a step.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.update_step)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#update_step)
        """

    def update_storage_profile(
        self,
        *,
        farmId: str,
        storageProfileId: str,
        clientToken: str = None,
        displayName: str = None,
        fileSystemLocationsToAdd: List["FileSystemLocationTypeDef"] = None,
        fileSystemLocationsToRemove: List["FileSystemLocationTypeDef"] = None,
        osFamily: StorageProfileOperatingSystemFamilyType = None
    ) -> Dict[str, Any]:
        """
        Updates a storage profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.update_storage_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#update_storage_profile)
        """

    def update_task(
        self,
        *,
        farmId: str,
        jobId: str,
        queueId: str,
        stepId: str,
        targetRunStatus: TaskTargetRunStatusType,
        taskId: str,
        clientToken: str = None
    ) -> Dict[str, Any]:
        """
        Updates a task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.update_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#update_task)
        """

    def update_worker(
        self,
        *,
        farmId: str,
        fleetId: str,
        workerId: str,
        capabilities: "WorkerCapabilitiesTypeDef" = None,
        hostProperties: "HostPropertiesRequestTypeDef" = None,
        status: UpdatedWorkerStatusType = None
    ) -> UpdateWorkerResponseTypeDef:
        """
        Updates a worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.update_worker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#update_worker)
        """

    def update_worker_schedule(
        self,
        *,
        farmId: str,
        fleetId: str,
        workerId: str,
        updatedSessionActions: Dict[str, "UpdatedSessionActionInfoTypeDef"] = None
    ) -> UpdateWorkerScheduleResponseTypeDef:
        """
        Updates the schedule for a worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Client.update_worker_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/client.html#update_worker_schedule)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_sessions_statistics_aggregation"]
    ) -> GetSessionsStatisticsAggregationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.GetSessionsStatisticsAggregation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#getsessionsstatisticsaggregationpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_available_metered_products"]
    ) -> ListAvailableMeteredProductsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListAvailableMeteredProducts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listavailablemeteredproductspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_budgets"]) -> ListBudgetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListBudgets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listbudgetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_farm_members"]
    ) -> ListFarmMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListFarmMembers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listfarmmemberspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_farms"]) -> ListFarmsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListFarms)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listfarmspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_fleet_members"]
    ) -> ListFleetMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListFleetMembers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listfleetmemberspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_fleets"]) -> ListFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListFleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listfleetspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_job_members"]) -> ListJobMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListJobMembers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listjobmemberspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_license_endpoints"]
    ) -> ListLicenseEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListLicenseEndpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listlicenseendpointspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_metered_products"]
    ) -> ListMeteredProductsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListMeteredProducts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listmeteredproductspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_monitors"]) -> ListMonitorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListMonitors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listmonitorspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_queue_environments"]
    ) -> ListQueueEnvironmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListQueueEnvironments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listqueueenvironmentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_queue_fleet_associations"]
    ) -> ListQueueFleetAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListQueueFleetAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listqueuefleetassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_queue_members"]
    ) -> ListQueueMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListQueueMembers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listqueuememberspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_queues"]) -> ListQueuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListQueues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listqueuespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_session_actions"]
    ) -> ListSessionActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListSessionActions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listsessionactionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_sessions"]) -> ListSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListSessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listsessionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_sessions_for_worker"]
    ) -> ListSessionsForWorkerPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListSessionsForWorker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listsessionsforworkerpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_step_consumers"]
    ) -> ListStepConsumersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListStepConsumers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#liststepconsumerspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_step_dependencies"]
    ) -> ListStepDependenciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListStepDependencies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#liststepdependenciespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_steps"]) -> ListStepsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListSteps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#liststepspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_storage_profiles"]
    ) -> ListStorageProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListStorageProfiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#liststorageprofilespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_storage_profiles_for_queue"]
    ) -> ListStorageProfilesForQueuePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListStorageProfilesForQueue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#liststorageprofilesforqueuepaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tasks"]) -> ListTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListTasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listtaskspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_workers"]) -> ListWorkersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Paginator.ListWorkers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/paginators.html#listworkerspaginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["fleet_active"]) -> FleetActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Waiter.FleetActive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters.html#fleetactivewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["job_create_complete"]) -> JobCreateCompleteWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Waiter.JobCreateComplete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters.html#jobcreatecompletewaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["license_endpoint_deleted"]
    ) -> LicenseEndpointDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Waiter.LicenseEndpointDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters.html#licenseendpointdeletedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["license_endpoint_valid"]
    ) -> LicenseEndpointValidWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Waiter.LicenseEndpointValid)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters.html#licenseendpointvalidwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["queue_fleet_association_stopped"]
    ) -> QueueFleetAssociationStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Waiter.QueueFleetAssociationStopped)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters.html#queuefleetassociationstoppedwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["queue_scheduling"]) -> QueueSchedulingWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Waiter.QueueScheduling)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters.html#queueschedulingwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["queue_scheduling_blocked"]
    ) -> QueueSchedulingBlockedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/deadline.html#DeadlineCloud.Waiter.QueueSchedulingBlocked)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_deadline/waiters.html#queueschedulingblockedwaiter)
        """
