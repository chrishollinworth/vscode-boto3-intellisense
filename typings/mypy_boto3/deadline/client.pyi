"""
Type annotations for deadline service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_deadline.client import DeadlineCloudClient

    session = Session()
    client: DeadlineCloudClient = session.client("deadline")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    GetSessionsStatisticsAggregationPaginator,
    ListAvailableMeteredProductsPaginator,
    ListBudgetsPaginator,
    ListFarmMembersPaginator,
    ListFarmsPaginator,
    ListFleetMembersPaginator,
    ListFleetsPaginator,
    ListJobMembersPaginator,
    ListJobParameterDefinitionsPaginator,
    ListJobsPaginator,
    ListLicenseEndpointsPaginator,
    ListLimitsPaginator,
    ListMeteredProductsPaginator,
    ListMonitorsPaginator,
    ListQueueEnvironmentsPaginator,
    ListQueueFleetAssociationsPaginator,
    ListQueueLimitAssociationsPaginator,
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
    AssociateMemberToFarmRequestTypeDef,
    AssociateMemberToFleetRequestTypeDef,
    AssociateMemberToJobRequestTypeDef,
    AssociateMemberToQueueRequestTypeDef,
    AssumeFleetRoleForReadRequestTypeDef,
    AssumeFleetRoleForReadResponseTypeDef,
    AssumeFleetRoleForWorkerRequestTypeDef,
    AssumeFleetRoleForWorkerResponseTypeDef,
    AssumeQueueRoleForReadRequestTypeDef,
    AssumeQueueRoleForReadResponseTypeDef,
    AssumeQueueRoleForUserRequestTypeDef,
    AssumeQueueRoleForUserResponseTypeDef,
    AssumeQueueRoleForWorkerRequestTypeDef,
    AssumeQueueRoleForWorkerResponseTypeDef,
    BatchGetJobEntityRequestTypeDef,
    BatchGetJobEntityResponseTypeDef,
    CopyJobTemplateRequestTypeDef,
    CopyJobTemplateResponseTypeDef,
    CreateBudgetRequestTypeDef,
    CreateBudgetResponseTypeDef,
    CreateFarmRequestTypeDef,
    CreateFarmResponseTypeDef,
    CreateFleetRequestTypeDef,
    CreateFleetResponseTypeDef,
    CreateJobRequestTypeDef,
    CreateJobResponseTypeDef,
    CreateLicenseEndpointRequestTypeDef,
    CreateLicenseEndpointResponseTypeDef,
    CreateLimitRequestTypeDef,
    CreateLimitResponseTypeDef,
    CreateMonitorRequestTypeDef,
    CreateMonitorResponseTypeDef,
    CreateQueueEnvironmentRequestTypeDef,
    CreateQueueEnvironmentResponseTypeDef,
    CreateQueueFleetAssociationRequestTypeDef,
    CreateQueueLimitAssociationRequestTypeDef,
    CreateQueueRequestTypeDef,
    CreateQueueResponseTypeDef,
    CreateStorageProfileRequestTypeDef,
    CreateStorageProfileResponseTypeDef,
    CreateWorkerRequestTypeDef,
    CreateWorkerResponseTypeDef,
    DeleteBudgetRequestTypeDef,
    DeleteFarmRequestTypeDef,
    DeleteFleetRequestTypeDef,
    DeleteLicenseEndpointRequestTypeDef,
    DeleteLimitRequestTypeDef,
    DeleteMeteredProductRequestTypeDef,
    DeleteMonitorRequestTypeDef,
    DeleteQueueEnvironmentRequestTypeDef,
    DeleteQueueFleetAssociationRequestTypeDef,
    DeleteQueueLimitAssociationRequestTypeDef,
    DeleteQueueRequestTypeDef,
    DeleteStorageProfileRequestTypeDef,
    DeleteWorkerRequestTypeDef,
    DisassociateMemberFromFarmRequestTypeDef,
    DisassociateMemberFromFleetRequestTypeDef,
    DisassociateMemberFromJobRequestTypeDef,
    DisassociateMemberFromQueueRequestTypeDef,
    GetBudgetRequestTypeDef,
    GetBudgetResponseTypeDef,
    GetFarmRequestTypeDef,
    GetFarmResponseTypeDef,
    GetFleetRequestTypeDef,
    GetFleetResponseTypeDef,
    GetJobRequestTypeDef,
    GetJobResponseTypeDef,
    GetLicenseEndpointRequestTypeDef,
    GetLicenseEndpointResponseTypeDef,
    GetLimitRequestTypeDef,
    GetLimitResponseTypeDef,
    GetMonitorRequestTypeDef,
    GetMonitorResponseTypeDef,
    GetQueueEnvironmentRequestTypeDef,
    GetQueueEnvironmentResponseTypeDef,
    GetQueueFleetAssociationRequestTypeDef,
    GetQueueFleetAssociationResponseTypeDef,
    GetQueueLimitAssociationRequestTypeDef,
    GetQueueLimitAssociationResponseTypeDef,
    GetQueueRequestTypeDef,
    GetQueueResponseTypeDef,
    GetSessionActionRequestTypeDef,
    GetSessionActionResponseTypeDef,
    GetSessionRequestTypeDef,
    GetSessionResponseTypeDef,
    GetSessionsStatisticsAggregationRequestTypeDef,
    GetSessionsStatisticsAggregationResponseTypeDef,
    GetStepRequestTypeDef,
    GetStepResponseTypeDef,
    GetStorageProfileForQueueRequestTypeDef,
    GetStorageProfileForQueueResponseTypeDef,
    GetStorageProfileRequestTypeDef,
    GetStorageProfileResponseTypeDef,
    GetTaskRequestTypeDef,
    GetTaskResponseTypeDef,
    GetWorkerRequestTypeDef,
    GetWorkerResponseTypeDef,
    ListAvailableMeteredProductsRequestTypeDef,
    ListAvailableMeteredProductsResponseTypeDef,
    ListBudgetsRequestTypeDef,
    ListBudgetsResponseTypeDef,
    ListFarmMembersRequestTypeDef,
    ListFarmMembersResponseTypeDef,
    ListFarmsRequestTypeDef,
    ListFarmsResponseTypeDef,
    ListFleetMembersRequestTypeDef,
    ListFleetMembersResponseTypeDef,
    ListFleetsRequestTypeDef,
    ListFleetsResponseTypeDef,
    ListJobMembersRequestTypeDef,
    ListJobMembersResponseTypeDef,
    ListJobParameterDefinitionsRequestTypeDef,
    ListJobParameterDefinitionsResponseTypeDef,
    ListJobsRequestTypeDef,
    ListJobsResponseTypeDef,
    ListLicenseEndpointsRequestTypeDef,
    ListLicenseEndpointsResponseTypeDef,
    ListLimitsRequestTypeDef,
    ListLimitsResponseTypeDef,
    ListMeteredProductsRequestTypeDef,
    ListMeteredProductsResponseTypeDef,
    ListMonitorsRequestTypeDef,
    ListMonitorsResponseTypeDef,
    ListQueueEnvironmentsRequestTypeDef,
    ListQueueEnvironmentsResponseTypeDef,
    ListQueueFleetAssociationsRequestTypeDef,
    ListQueueFleetAssociationsResponseTypeDef,
    ListQueueLimitAssociationsRequestTypeDef,
    ListQueueLimitAssociationsResponseTypeDef,
    ListQueueMembersRequestTypeDef,
    ListQueueMembersResponseTypeDef,
    ListQueuesRequestTypeDef,
    ListQueuesResponseTypeDef,
    ListSessionActionsRequestTypeDef,
    ListSessionActionsResponseTypeDef,
    ListSessionsForWorkerRequestTypeDef,
    ListSessionsForWorkerResponseTypeDef,
    ListSessionsRequestTypeDef,
    ListSessionsResponseTypeDef,
    ListStepConsumersRequestTypeDef,
    ListStepConsumersResponseTypeDef,
    ListStepDependenciesRequestTypeDef,
    ListStepDependenciesResponseTypeDef,
    ListStepsRequestTypeDef,
    ListStepsResponseTypeDef,
    ListStorageProfilesForQueueRequestTypeDef,
    ListStorageProfilesForQueueResponseTypeDef,
    ListStorageProfilesRequestTypeDef,
    ListStorageProfilesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTasksRequestTypeDef,
    ListTasksResponseTypeDef,
    ListWorkersRequestTypeDef,
    ListWorkersResponseTypeDef,
    PutMeteredProductRequestTypeDef,
    SearchJobsRequestTypeDef,
    SearchJobsResponseTypeDef,
    SearchStepsRequestTypeDef,
    SearchStepsResponseTypeDef,
    SearchTasksRequestTypeDef,
    SearchTasksResponseTypeDef,
    SearchWorkersRequestTypeDef,
    SearchWorkersResponseTypeDef,
    StartSessionsStatisticsAggregationRequestTypeDef,
    StartSessionsStatisticsAggregationResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateBudgetRequestTypeDef,
    UpdateFarmRequestTypeDef,
    UpdateFleetRequestTypeDef,
    UpdateJobRequestTypeDef,
    UpdateLimitRequestTypeDef,
    UpdateMonitorRequestTypeDef,
    UpdateQueueEnvironmentRequestTypeDef,
    UpdateQueueFleetAssociationRequestTypeDef,
    UpdateQueueLimitAssociationRequestTypeDef,
    UpdateQueueRequestTypeDef,
    UpdateSessionRequestTypeDef,
    UpdateStepRequestTypeDef,
    UpdateStorageProfileRequestTypeDef,
    UpdateTaskRequestTypeDef,
    UpdateWorkerRequestTypeDef,
    UpdateWorkerResponseTypeDef,
    UpdateWorkerScheduleRequestTypeDef,
    UpdateWorkerScheduleResponseTypeDef,
)
from .waiter import (
    FleetActiveWaiter,
    JobCreateCompleteWaiter,
    LicenseEndpointDeletedWaiter,
    LicenseEndpointValidWaiter,
    QueueFleetAssociationStoppedWaiter,
    QueueLimitAssociationStoppedWaiter,
    QueueSchedulingBlockedWaiter,
    QueueSchedulingWaiter,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("DeadlineCloudClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline.html#DeadlineCloud.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DeadlineCloudClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline.html#DeadlineCloud.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#generate_presigned_url)
        """

    def associate_member_to_farm(
        self, **kwargs: Unpack[AssociateMemberToFarmRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Assigns a farm membership level to a member.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/associate_member_to_farm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#associate_member_to_farm)
        """

    def associate_member_to_fleet(
        self, **kwargs: Unpack[AssociateMemberToFleetRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Assigns a fleet membership level to a member.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/associate_member_to_fleet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#associate_member_to_fleet)
        """

    def associate_member_to_job(
        self, **kwargs: Unpack[AssociateMemberToJobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Assigns a job membership level to a member.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/associate_member_to_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#associate_member_to_job)
        """

    def associate_member_to_queue(
        self, **kwargs: Unpack[AssociateMemberToQueueRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Assigns a queue membership level to a member.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/associate_member_to_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#associate_member_to_queue)
        """

    def assume_fleet_role_for_read(
        self, **kwargs: Unpack[AssumeFleetRoleForReadRequestTypeDef]
    ) -> AssumeFleetRoleForReadResponseTypeDef:
        """
        Get Amazon Web Services credentials from the fleet role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/assume_fleet_role_for_read.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#assume_fleet_role_for_read)
        """

    def assume_fleet_role_for_worker(
        self, **kwargs: Unpack[AssumeFleetRoleForWorkerRequestTypeDef]
    ) -> AssumeFleetRoleForWorkerResponseTypeDef:
        """
        Get credentials from the fleet role for a worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/assume_fleet_role_for_worker.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#assume_fleet_role_for_worker)
        """

    def assume_queue_role_for_read(
        self, **kwargs: Unpack[AssumeQueueRoleForReadRequestTypeDef]
    ) -> AssumeQueueRoleForReadResponseTypeDef:
        """
        Gets Amazon Web Services credentials from the queue role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/assume_queue_role_for_read.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#assume_queue_role_for_read)
        """

    def assume_queue_role_for_user(
        self, **kwargs: Unpack[AssumeQueueRoleForUserRequestTypeDef]
    ) -> AssumeQueueRoleForUserResponseTypeDef:
        """
        Allows a user to assume a role for a queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/assume_queue_role_for_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#assume_queue_role_for_user)
        """

    def assume_queue_role_for_worker(
        self, **kwargs: Unpack[AssumeQueueRoleForWorkerRequestTypeDef]
    ) -> AssumeQueueRoleForWorkerResponseTypeDef:
        """
        Allows a worker to assume a queue role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/assume_queue_role_for_worker.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#assume_queue_role_for_worker)
        """

    def batch_get_job_entity(
        self, **kwargs: Unpack[BatchGetJobEntityRequestTypeDef]
    ) -> BatchGetJobEntityResponseTypeDef:
        """
        Get batched job details for a worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/batch_get_job_entity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#batch_get_job_entity)
        """

    def copy_job_template(
        self, **kwargs: Unpack[CopyJobTemplateRequestTypeDef]
    ) -> CopyJobTemplateResponseTypeDef:
        """
        Copies a job template to an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/copy_job_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#copy_job_template)
        """

    def create_budget(
        self, **kwargs: Unpack[CreateBudgetRequestTypeDef]
    ) -> CreateBudgetResponseTypeDef:
        """
        Creates a budget to set spending thresholds for your rendering activity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/create_budget.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#create_budget)
        """

    def create_farm(self, **kwargs: Unpack[CreateFarmRequestTypeDef]) -> CreateFarmResponseTypeDef:
        """
        Creates a farm to allow space for queues and fleets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/create_farm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#create_farm)
        """

    def create_fleet(
        self, **kwargs: Unpack[CreateFleetRequestTypeDef]
    ) -> CreateFleetResponseTypeDef:
        """
        Creates a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/create_fleet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#create_fleet)
        """

    def create_job(self, **kwargs: Unpack[CreateJobRequestTypeDef]) -> CreateJobResponseTypeDef:
        """
        Creates a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/create_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#create_job)
        """

    def create_license_endpoint(
        self, **kwargs: Unpack[CreateLicenseEndpointRequestTypeDef]
    ) -> CreateLicenseEndpointResponseTypeDef:
        """
        Creates a license endpoint to integrate your various licensed software used for
        rendering on Deadline Cloud.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/create_license_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#create_license_endpoint)
        """

    def create_limit(
        self, **kwargs: Unpack[CreateLimitRequestTypeDef]
    ) -> CreateLimitResponseTypeDef:
        """
        Creates a limit that manages the distribution of shared resources, such as
        floating licenses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/create_limit.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#create_limit)
        """

    def create_monitor(
        self, **kwargs: Unpack[CreateMonitorRequestTypeDef]
    ) -> CreateMonitorResponseTypeDef:
        """
        Creates an Amazon Web Services Deadline Cloud monitor that you can use to view
        your farms, queues, and fleets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/create_monitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#create_monitor)
        """

    def create_queue(
        self, **kwargs: Unpack[CreateQueueRequestTypeDef]
    ) -> CreateQueueResponseTypeDef:
        """
        Creates a queue to coordinate the order in which jobs run on a farm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/create_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#create_queue)
        """

    def create_queue_environment(
        self, **kwargs: Unpack[CreateQueueEnvironmentRequestTypeDef]
    ) -> CreateQueueEnvironmentResponseTypeDef:
        """
        Creates an environment for a queue that defines how jobs in the queue run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/create_queue_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#create_queue_environment)
        """

    def create_queue_fleet_association(
        self, **kwargs: Unpack[CreateQueueFleetAssociationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates an association between a queue and a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/create_queue_fleet_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#create_queue_fleet_association)
        """

    def create_queue_limit_association(
        self, **kwargs: Unpack[CreateQueueLimitAssociationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates a limit with a particular queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/create_queue_limit_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#create_queue_limit_association)
        """

    def create_storage_profile(
        self, **kwargs: Unpack[CreateStorageProfileRequestTypeDef]
    ) -> CreateStorageProfileResponseTypeDef:
        """
        Creates a storage profile that specifies the operating system, file type, and
        file location of resources used on a farm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/create_storage_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#create_storage_profile)
        """

    def create_worker(
        self, **kwargs: Unpack[CreateWorkerRequestTypeDef]
    ) -> CreateWorkerResponseTypeDef:
        """
        Creates a worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/create_worker.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#create_worker)
        """

    def delete_budget(self, **kwargs: Unpack[DeleteBudgetRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a budget.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/delete_budget.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#delete_budget)
        """

    def delete_farm(self, **kwargs: Unpack[DeleteFarmRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a farm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/delete_farm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#delete_farm)
        """

    def delete_fleet(self, **kwargs: Unpack[DeleteFleetRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/delete_fleet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#delete_fleet)
        """

    def delete_license_endpoint(
        self, **kwargs: Unpack[DeleteLicenseEndpointRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a license endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/delete_license_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#delete_license_endpoint)
        """

    def delete_limit(self, **kwargs: Unpack[DeleteLimitRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a limit from the specified farm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/delete_limit.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#delete_limit)
        """

    def delete_metered_product(
        self, **kwargs: Unpack[DeleteMeteredProductRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a metered product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/delete_metered_product.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#delete_metered_product)
        """

    def delete_monitor(self, **kwargs: Unpack[DeleteMonitorRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a Deadline Cloud monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/delete_monitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#delete_monitor)
        """

    def delete_queue(self, **kwargs: Unpack[DeleteQueueRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/delete_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#delete_queue)
        """

    def delete_queue_environment(
        self, **kwargs: Unpack[DeleteQueueEnvironmentRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a queue environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/delete_queue_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#delete_queue_environment)
        """

    def delete_queue_fleet_association(
        self, **kwargs: Unpack[DeleteQueueFleetAssociationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a queue-fleet association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/delete_queue_fleet_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#delete_queue_fleet_association)
        """

    def delete_queue_limit_association(
        self, **kwargs: Unpack[DeleteQueueLimitAssociationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the association between a queue and a limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/delete_queue_limit_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#delete_queue_limit_association)
        """

    def delete_storage_profile(
        self, **kwargs: Unpack[DeleteStorageProfileRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a storage profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/delete_storage_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#delete_storage_profile)
        """

    def delete_worker(self, **kwargs: Unpack[DeleteWorkerRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/delete_worker.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#delete_worker)
        """

    def disassociate_member_from_farm(
        self, **kwargs: Unpack[DisassociateMemberFromFarmRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates a member from a farm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/disassociate_member_from_farm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#disassociate_member_from_farm)
        """

    def disassociate_member_from_fleet(
        self, **kwargs: Unpack[DisassociateMemberFromFleetRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates a member from a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/disassociate_member_from_fleet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#disassociate_member_from_fleet)
        """

    def disassociate_member_from_job(
        self, **kwargs: Unpack[DisassociateMemberFromJobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates a member from a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/disassociate_member_from_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#disassociate_member_from_job)
        """

    def disassociate_member_from_queue(
        self, **kwargs: Unpack[DisassociateMemberFromQueueRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates a member from a queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/disassociate_member_from_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#disassociate_member_from_queue)
        """

    def get_budget(self, **kwargs: Unpack[GetBudgetRequestTypeDef]) -> GetBudgetResponseTypeDef:
        """
        Get a budget.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_budget.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_budget)
        """

    def get_farm(self, **kwargs: Unpack[GetFarmRequestTypeDef]) -> GetFarmResponseTypeDef:
        """
        Get a farm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_farm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_farm)
        """

    def get_fleet(self, **kwargs: Unpack[GetFleetRequestTypeDef]) -> GetFleetResponseTypeDef:
        """
        Get a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_fleet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_fleet)
        """

    def get_job(self, **kwargs: Unpack[GetJobRequestTypeDef]) -> GetJobResponseTypeDef:
        """
        Gets a Deadline Cloud job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_job)
        """

    def get_license_endpoint(
        self, **kwargs: Unpack[GetLicenseEndpointRequestTypeDef]
    ) -> GetLicenseEndpointResponseTypeDef:
        """
        Gets a licence endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_license_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_license_endpoint)
        """

    def get_limit(self, **kwargs: Unpack[GetLimitRequestTypeDef]) -> GetLimitResponseTypeDef:
        """
        Gets information about a specific limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_limit.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_limit)
        """

    def get_monitor(self, **kwargs: Unpack[GetMonitorRequestTypeDef]) -> GetMonitorResponseTypeDef:
        """
        Gets information about the specified monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_monitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_monitor)
        """

    def get_queue(self, **kwargs: Unpack[GetQueueRequestTypeDef]) -> GetQueueResponseTypeDef:
        """
        Gets a queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_queue)
        """

    def get_queue_environment(
        self, **kwargs: Unpack[GetQueueEnvironmentRequestTypeDef]
    ) -> GetQueueEnvironmentResponseTypeDef:
        """
        Gets a queue environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_queue_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_queue_environment)
        """

    def get_queue_fleet_association(
        self, **kwargs: Unpack[GetQueueFleetAssociationRequestTypeDef]
    ) -> GetQueueFleetAssociationResponseTypeDef:
        """
        Gets a queue-fleet association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_queue_fleet_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_queue_fleet_association)
        """

    def get_queue_limit_association(
        self, **kwargs: Unpack[GetQueueLimitAssociationRequestTypeDef]
    ) -> GetQueueLimitAssociationResponseTypeDef:
        """
        Gets information about a specific association between a queue and a limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_queue_limit_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_queue_limit_association)
        """

    def get_session(self, **kwargs: Unpack[GetSessionRequestTypeDef]) -> GetSessionResponseTypeDef:
        """
        Gets a session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_session)
        """

    def get_session_action(
        self, **kwargs: Unpack[GetSessionActionRequestTypeDef]
    ) -> GetSessionActionResponseTypeDef:
        """
        Gets a session action for the job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_session_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_session_action)
        """

    def get_sessions_statistics_aggregation(
        self, **kwargs: Unpack[GetSessionsStatisticsAggregationRequestTypeDef]
    ) -> GetSessionsStatisticsAggregationResponseTypeDef:
        """
        Gets a set of statistics for queues or farms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_sessions_statistics_aggregation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_sessions_statistics_aggregation)
        """

    def get_step(self, **kwargs: Unpack[GetStepRequestTypeDef]) -> GetStepResponseTypeDef:
        """
        Gets a step.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_step.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_step)
        """

    def get_storage_profile(
        self, **kwargs: Unpack[GetStorageProfileRequestTypeDef]
    ) -> GetStorageProfileResponseTypeDef:
        """
        Gets a storage profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_storage_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_storage_profile)
        """

    def get_storage_profile_for_queue(
        self, **kwargs: Unpack[GetStorageProfileForQueueRequestTypeDef]
    ) -> GetStorageProfileForQueueResponseTypeDef:
        """
        Gets a storage profile for a queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_storage_profile_for_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_storage_profile_for_queue)
        """

    def get_task(self, **kwargs: Unpack[GetTaskRequestTypeDef]) -> GetTaskResponseTypeDef:
        """
        Gets a task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_task)
        """

    def get_worker(self, **kwargs: Unpack[GetWorkerRequestTypeDef]) -> GetWorkerResponseTypeDef:
        """
        Gets a worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_worker.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_worker)
        """

    def list_available_metered_products(
        self, **kwargs: Unpack[ListAvailableMeteredProductsRequestTypeDef]
    ) -> ListAvailableMeteredProductsResponseTypeDef:
        """
        A list of the available metered products.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_available_metered_products.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_available_metered_products)
        """

    def list_budgets(
        self, **kwargs: Unpack[ListBudgetsRequestTypeDef]
    ) -> ListBudgetsResponseTypeDef:
        """
        A list of budgets in a farm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_budgets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_budgets)
        """

    def list_farm_members(
        self, **kwargs: Unpack[ListFarmMembersRequestTypeDef]
    ) -> ListFarmMembersResponseTypeDef:
        """
        Lists the members of a farm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_farm_members.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_farm_members)
        """

    def list_farms(self, **kwargs: Unpack[ListFarmsRequestTypeDef]) -> ListFarmsResponseTypeDef:
        """
        Lists farms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_farms.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_farms)
        """

    def list_fleet_members(
        self, **kwargs: Unpack[ListFleetMembersRequestTypeDef]
    ) -> ListFleetMembersResponseTypeDef:
        """
        Lists fleet members.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_fleet_members.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_fleet_members)
        """

    def list_fleets(self, **kwargs: Unpack[ListFleetsRequestTypeDef]) -> ListFleetsResponseTypeDef:
        """
        Lists fleets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_fleets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_fleets)
        """

    def list_job_members(
        self, **kwargs: Unpack[ListJobMembersRequestTypeDef]
    ) -> ListJobMembersResponseTypeDef:
        """
        Lists members on a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_job_members.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_job_members)
        """

    def list_job_parameter_definitions(
        self, **kwargs: Unpack[ListJobParameterDefinitionsRequestTypeDef]
    ) -> ListJobParameterDefinitionsResponseTypeDef:
        """
        Lists parameter definitions of a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_job_parameter_definitions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_job_parameter_definitions)
        """

    def list_jobs(self, **kwargs: Unpack[ListJobsRequestTypeDef]) -> ListJobsResponseTypeDef:
        """
        Lists jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_jobs)
        """

    def list_license_endpoints(
        self, **kwargs: Unpack[ListLicenseEndpointsRequestTypeDef]
    ) -> ListLicenseEndpointsResponseTypeDef:
        """
        Lists license endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_license_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_license_endpoints)
        """

    def list_limits(self, **kwargs: Unpack[ListLimitsRequestTypeDef]) -> ListLimitsResponseTypeDef:
        """
        Gets a list of limits defined in the specified farm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_limits.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_limits)
        """

    def list_metered_products(
        self, **kwargs: Unpack[ListMeteredProductsRequestTypeDef]
    ) -> ListMeteredProductsResponseTypeDef:
        """
        Lists metered products.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_metered_products.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_metered_products)
        """

    def list_monitors(
        self, **kwargs: Unpack[ListMonitorsRequestTypeDef]
    ) -> ListMonitorsResponseTypeDef:
        """
        Gets a list of your monitors in Deadline Cloud.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_monitors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_monitors)
        """

    def list_queue_environments(
        self, **kwargs: Unpack[ListQueueEnvironmentsRequestTypeDef]
    ) -> ListQueueEnvironmentsResponseTypeDef:
        """
        Lists queue environments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_queue_environments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_queue_environments)
        """

    def list_queue_fleet_associations(
        self, **kwargs: Unpack[ListQueueFleetAssociationsRequestTypeDef]
    ) -> ListQueueFleetAssociationsResponseTypeDef:
        """
        Lists queue-fleet associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_queue_fleet_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_queue_fleet_associations)
        """

    def list_queue_limit_associations(
        self, **kwargs: Unpack[ListQueueLimitAssociationsRequestTypeDef]
    ) -> ListQueueLimitAssociationsResponseTypeDef:
        """
        Gets a list of the associations between queues and limits defined in a farm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_queue_limit_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_queue_limit_associations)
        """

    def list_queue_members(
        self, **kwargs: Unpack[ListQueueMembersRequestTypeDef]
    ) -> ListQueueMembersResponseTypeDef:
        """
        Lists the members in a queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_queue_members.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_queue_members)
        """

    def list_queues(self, **kwargs: Unpack[ListQueuesRequestTypeDef]) -> ListQueuesResponseTypeDef:
        """
        Lists queues.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_queues.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_queues)
        """

    def list_session_actions(
        self, **kwargs: Unpack[ListSessionActionsRequestTypeDef]
    ) -> ListSessionActionsResponseTypeDef:
        """
        Lists session actions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_session_actions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_session_actions)
        """

    def list_sessions(
        self, **kwargs: Unpack[ListSessionsRequestTypeDef]
    ) -> ListSessionsResponseTypeDef:
        """
        Lists sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_sessions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_sessions)
        """

    def list_sessions_for_worker(
        self, **kwargs: Unpack[ListSessionsForWorkerRequestTypeDef]
    ) -> ListSessionsForWorkerResponseTypeDef:
        """
        Lists sessions for a worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_sessions_for_worker.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_sessions_for_worker)
        """

    def list_step_consumers(
        self, **kwargs: Unpack[ListStepConsumersRequestTypeDef]
    ) -> ListStepConsumersResponseTypeDef:
        """
        Lists step consumers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_step_consumers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_step_consumers)
        """

    def list_step_dependencies(
        self, **kwargs: Unpack[ListStepDependenciesRequestTypeDef]
    ) -> ListStepDependenciesResponseTypeDef:
        """
        Lists the dependencies for a step.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_step_dependencies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_step_dependencies)
        """

    def list_steps(self, **kwargs: Unpack[ListStepsRequestTypeDef]) -> ListStepsResponseTypeDef:
        """
        Lists steps for a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_steps.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_steps)
        """

    def list_storage_profiles(
        self, **kwargs: Unpack[ListStorageProfilesRequestTypeDef]
    ) -> ListStorageProfilesResponseTypeDef:
        """
        Lists storage profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_storage_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_storage_profiles)
        """

    def list_storage_profiles_for_queue(
        self, **kwargs: Unpack[ListStorageProfilesForQueueRequestTypeDef]
    ) -> ListStorageProfilesForQueueResponseTypeDef:
        """
        Lists storage profiles for a queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_storage_profiles_for_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_storage_profiles_for_queue)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_tags_for_resource)
        """

    def list_tasks(self, **kwargs: Unpack[ListTasksRequestTypeDef]) -> ListTasksResponseTypeDef:
        """
        Lists tasks for a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_tasks)
        """

    def list_workers(
        self, **kwargs: Unpack[ListWorkersRequestTypeDef]
    ) -> ListWorkersResponseTypeDef:
        """
        Lists workers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/list_workers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#list_workers)
        """

    def put_metered_product(
        self, **kwargs: Unpack[PutMeteredProductRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds a metered product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/put_metered_product.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#put_metered_product)
        """

    def search_jobs(self, **kwargs: Unpack[SearchJobsRequestTypeDef]) -> SearchJobsResponseTypeDef:
        """
        Searches for jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/search_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#search_jobs)
        """

    def search_steps(
        self, **kwargs: Unpack[SearchStepsRequestTypeDef]
    ) -> SearchStepsResponseTypeDef:
        """
        Searches for steps.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/search_steps.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#search_steps)
        """

    def search_tasks(
        self, **kwargs: Unpack[SearchTasksRequestTypeDef]
    ) -> SearchTasksResponseTypeDef:
        """
        Searches for tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/search_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#search_tasks)
        """

    def search_workers(
        self, **kwargs: Unpack[SearchWorkersRequestTypeDef]
    ) -> SearchWorkersResponseTypeDef:
        """
        Searches for workers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/search_workers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#search_workers)
        """

    def start_sessions_statistics_aggregation(
        self, **kwargs: Unpack[StartSessionsStatisticsAggregationRequestTypeDef]
    ) -> StartSessionsStatisticsAggregationResponseTypeDef:
        """
        Starts an asynchronous request for getting aggregated statistics about queues
        and farms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/start_sessions_statistics_aggregation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#start_sessions_statistics_aggregation)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Tags a resource using the resource's ARN and desired tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a tag from a resource using the resource's ARN and tag to remove.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#untag_resource)
        """

    def update_budget(self, **kwargs: Unpack[UpdateBudgetRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates a budget that sets spending thresholds for rendering activity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/update_budget.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#update_budget)
        """

    def update_farm(self, **kwargs: Unpack[UpdateFarmRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates a farm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/update_farm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#update_farm)
        """

    def update_fleet(self, **kwargs: Unpack[UpdateFleetRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/update_fleet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#update_fleet)
        """

    def update_job(self, **kwargs: Unpack[UpdateJobRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/update_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#update_job)
        """

    def update_limit(self, **kwargs: Unpack[UpdateLimitRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates the properties of the specified limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/update_limit.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#update_limit)
        """

    def update_monitor(self, **kwargs: Unpack[UpdateMonitorRequestTypeDef]) -> Dict[str, Any]:
        """
        Modifies the settings for a Deadline Cloud monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/update_monitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#update_monitor)
        """

    def update_queue(self, **kwargs: Unpack[UpdateQueueRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates a queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/update_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#update_queue)
        """

    def update_queue_environment(
        self, **kwargs: Unpack[UpdateQueueEnvironmentRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the queue environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/update_queue_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#update_queue_environment)
        """

    def update_queue_fleet_association(
        self, **kwargs: Unpack[UpdateQueueFleetAssociationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates a queue-fleet association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/update_queue_fleet_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#update_queue_fleet_association)
        """

    def update_queue_limit_association(
        self, **kwargs: Unpack[UpdateQueueLimitAssociationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the status of the queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/update_queue_limit_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#update_queue_limit_association)
        """

    def update_session(self, **kwargs: Unpack[UpdateSessionRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates a session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/update_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#update_session)
        """

    def update_step(self, **kwargs: Unpack[UpdateStepRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates a step.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/update_step.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#update_step)
        """

    def update_storage_profile(
        self, **kwargs: Unpack[UpdateStorageProfileRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates a storage profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/update_storage_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#update_storage_profile)
        """

    def update_task(self, **kwargs: Unpack[UpdateTaskRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates a task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/update_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#update_task)
        """

    def update_worker(
        self, **kwargs: Unpack[UpdateWorkerRequestTypeDef]
    ) -> UpdateWorkerResponseTypeDef:
        """
        Updates a worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/update_worker.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#update_worker)
        """

    def update_worker_schedule(
        self, **kwargs: Unpack[UpdateWorkerScheduleRequestTypeDef]
    ) -> UpdateWorkerScheduleResponseTypeDef:
        """
        Updates the schedule for a worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/update_worker_schedule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#update_worker_schedule)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_sessions_statistics_aggregation"]
    ) -> GetSessionsStatisticsAggregationPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_available_metered_products"]
    ) -> ListAvailableMeteredProductsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_budgets"]
    ) -> ListBudgetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_farm_members"]
    ) -> ListFarmMembersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_farms"]
    ) -> ListFarmsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_fleet_members"]
    ) -> ListFleetMembersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_fleets"]
    ) -> ListFleetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_job_members"]
    ) -> ListJobMembersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_job_parameter_definitions"]
    ) -> ListJobParameterDefinitionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_jobs"]
    ) -> ListJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_license_endpoints"]
    ) -> ListLicenseEndpointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_limits"]
    ) -> ListLimitsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_metered_products"]
    ) -> ListMeteredProductsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_monitors"]
    ) -> ListMonitorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_queue_environments"]
    ) -> ListQueueEnvironmentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_queue_fleet_associations"]
    ) -> ListQueueFleetAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_queue_limit_associations"]
    ) -> ListQueueLimitAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_queue_members"]
    ) -> ListQueueMembersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_queues"]
    ) -> ListQueuesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_session_actions"]
    ) -> ListSessionActionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_sessions_for_worker"]
    ) -> ListSessionsForWorkerPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_sessions"]
    ) -> ListSessionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_step_consumers"]
    ) -> ListStepConsumersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_step_dependencies"]
    ) -> ListStepDependenciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_steps"]
    ) -> ListStepsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_storage_profiles_for_queue"]
    ) -> ListStorageProfilesForQueuePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_storage_profiles"]
    ) -> ListStorageProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tasks"]
    ) -> ListTasksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workers"]
    ) -> ListWorkersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["fleet_active"]
    ) -> FleetActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["job_create_complete"]
    ) -> JobCreateCompleteWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["license_endpoint_deleted"]
    ) -> LicenseEndpointDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["license_endpoint_valid"]
    ) -> LicenseEndpointValidWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["queue_fleet_association_stopped"]
    ) -> QueueFleetAssociationStoppedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["queue_limit_association_stopped"]
    ) -> QueueLimitAssociationStoppedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["queue_scheduling_blocked"]
    ) -> QueueSchedulingBlockedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["queue_scheduling"]
    ) -> QueueSchedulingWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/deadline/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/client/#get_waiter)
        """
