"""
Type annotations for batch service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_batch.client import BatchClient

    session = Session()
    client: BatchClient = session.client("batch")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeComputeEnvironmentsPaginator,
    DescribeJobDefinitionsPaginator,
    DescribeJobQueuesPaginator,
    DescribeServiceEnvironmentsPaginator,
    ListConsumableResourcesPaginator,
    ListJobsByConsumableResourcePaginator,
    ListJobsPaginator,
    ListSchedulingPoliciesPaginator,
    ListServiceJobsPaginator,
)
from .type_defs import (
    CancelJobRequestTypeDef,
    CreateComputeEnvironmentRequestTypeDef,
    CreateComputeEnvironmentResponseTypeDef,
    CreateConsumableResourceRequestTypeDef,
    CreateConsumableResourceResponseTypeDef,
    CreateJobQueueRequestTypeDef,
    CreateJobQueueResponseTypeDef,
    CreateSchedulingPolicyRequestTypeDef,
    CreateSchedulingPolicyResponseTypeDef,
    CreateServiceEnvironmentRequestTypeDef,
    CreateServiceEnvironmentResponseTypeDef,
    DeleteComputeEnvironmentRequestTypeDef,
    DeleteConsumableResourceRequestTypeDef,
    DeleteJobQueueRequestTypeDef,
    DeleteSchedulingPolicyRequestTypeDef,
    DeleteServiceEnvironmentRequestTypeDef,
    DeregisterJobDefinitionRequestTypeDef,
    DescribeComputeEnvironmentsRequestTypeDef,
    DescribeComputeEnvironmentsResponseTypeDef,
    DescribeConsumableResourceRequestTypeDef,
    DescribeConsumableResourceResponseTypeDef,
    DescribeJobDefinitionsRequestTypeDef,
    DescribeJobDefinitionsResponseTypeDef,
    DescribeJobQueuesRequestTypeDef,
    DescribeJobQueuesResponseTypeDef,
    DescribeJobsRequestTypeDef,
    DescribeJobsResponseTypeDef,
    DescribeSchedulingPoliciesRequestTypeDef,
    DescribeSchedulingPoliciesResponseTypeDef,
    DescribeServiceEnvironmentsRequestTypeDef,
    DescribeServiceEnvironmentsResponseTypeDef,
    DescribeServiceJobRequestTypeDef,
    DescribeServiceJobResponseTypeDef,
    GetJobQueueSnapshotRequestTypeDef,
    GetJobQueueSnapshotResponseTypeDef,
    ListConsumableResourcesRequestTypeDef,
    ListConsumableResourcesResponseTypeDef,
    ListJobsByConsumableResourceRequestTypeDef,
    ListJobsByConsumableResourceResponseTypeDef,
    ListJobsRequestTypeDef,
    ListJobsResponseTypeDef,
    ListSchedulingPoliciesRequestTypeDef,
    ListSchedulingPoliciesResponseTypeDef,
    ListServiceJobsRequestTypeDef,
    ListServiceJobsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    RegisterJobDefinitionRequestTypeDef,
    RegisterJobDefinitionResponseTypeDef,
    SubmitJobRequestTypeDef,
    SubmitJobResponseTypeDef,
    SubmitServiceJobRequestTypeDef,
    SubmitServiceJobResponseTypeDef,
    TagResourceRequestTypeDef,
    TerminateJobRequestTypeDef,
    TerminateServiceJobRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateComputeEnvironmentRequestTypeDef,
    UpdateComputeEnvironmentResponseTypeDef,
    UpdateConsumableResourceRequestTypeDef,
    UpdateConsumableResourceResponseTypeDef,
    UpdateJobQueueRequestTypeDef,
    UpdateJobQueueResponseTypeDef,
    UpdateSchedulingPolicyRequestTypeDef,
    UpdateServiceEnvironmentRequestTypeDef,
    UpdateServiceEnvironmentResponseTypeDef,
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

__all__ = ("BatchClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ClientException: Type[BotocoreClientError]
    ServerException: Type[BotocoreClientError]

class BatchClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        BatchClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#generate_presigned_url)
        """

    def cancel_job(self, **kwargs: Unpack[CancelJobRequestTypeDef]) -> Dict[str, Any]:
        """
        Cancels a job in an Batch job queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/cancel_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#cancel_job)
        """

    def create_compute_environment(
        self, **kwargs: Unpack[CreateComputeEnvironmentRequestTypeDef]
    ) -> CreateComputeEnvironmentResponseTypeDef:
        """
        Creates an Batch compute environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/create_compute_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#create_compute_environment)
        """

    def create_consumable_resource(
        self, **kwargs: Unpack[CreateConsumableResourceRequestTypeDef]
    ) -> CreateConsumableResourceResponseTypeDef:
        """
        Creates an Batch consumable resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/create_consumable_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#create_consumable_resource)
        """

    def create_job_queue(
        self, **kwargs: Unpack[CreateJobQueueRequestTypeDef]
    ) -> CreateJobQueueResponseTypeDef:
        """
        Creates an Batch job queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/create_job_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#create_job_queue)
        """

    def create_scheduling_policy(
        self, **kwargs: Unpack[CreateSchedulingPolicyRequestTypeDef]
    ) -> CreateSchedulingPolicyResponseTypeDef:
        """
        Creates an Batch scheduling policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/create_scheduling_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#create_scheduling_policy)
        """

    def create_service_environment(
        self, **kwargs: Unpack[CreateServiceEnvironmentRequestTypeDef]
    ) -> CreateServiceEnvironmentResponseTypeDef:
        """
        Creates a service environment for running service jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/create_service_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#create_service_environment)
        """

    def delete_compute_environment(
        self, **kwargs: Unpack[DeleteComputeEnvironmentRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an Batch compute environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/delete_compute_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#delete_compute_environment)
        """

    def delete_consumable_resource(
        self, **kwargs: Unpack[DeleteConsumableResourceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified consumable resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/delete_consumable_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#delete_consumable_resource)
        """

    def delete_job_queue(self, **kwargs: Unpack[DeleteJobQueueRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified job queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/delete_job_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#delete_job_queue)
        """

    def delete_scheduling_policy(
        self, **kwargs: Unpack[DeleteSchedulingPolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified scheduling policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/delete_scheduling_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#delete_scheduling_policy)
        """

    def delete_service_environment(
        self, **kwargs: Unpack[DeleteServiceEnvironmentRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a Service environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/delete_service_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#delete_service_environment)
        """

    def deregister_job_definition(
        self, **kwargs: Unpack[DeregisterJobDefinitionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deregisters an Batch job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/deregister_job_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#deregister_job_definition)
        """

    def describe_compute_environments(
        self, **kwargs: Unpack[DescribeComputeEnvironmentsRequestTypeDef]
    ) -> DescribeComputeEnvironmentsResponseTypeDef:
        """
        Describes one or more of your compute environments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/describe_compute_environments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#describe_compute_environments)
        """

    def describe_consumable_resource(
        self, **kwargs: Unpack[DescribeConsumableResourceRequestTypeDef]
    ) -> DescribeConsumableResourceResponseTypeDef:
        """
        Returns a description of the specified consumable resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/describe_consumable_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#describe_consumable_resource)
        """

    def describe_job_definitions(
        self, **kwargs: Unpack[DescribeJobDefinitionsRequestTypeDef]
    ) -> DescribeJobDefinitionsResponseTypeDef:
        """
        Describes a list of job definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/describe_job_definitions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#describe_job_definitions)
        """

    def describe_job_queues(
        self, **kwargs: Unpack[DescribeJobQueuesRequestTypeDef]
    ) -> DescribeJobQueuesResponseTypeDef:
        """
        Describes one or more of your job queues.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/describe_job_queues.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#describe_job_queues)
        """

    def describe_jobs(
        self, **kwargs: Unpack[DescribeJobsRequestTypeDef]
    ) -> DescribeJobsResponseTypeDef:
        """
        Describes a list of Batch jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/describe_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#describe_jobs)
        """

    def describe_scheduling_policies(
        self, **kwargs: Unpack[DescribeSchedulingPoliciesRequestTypeDef]
    ) -> DescribeSchedulingPoliciesResponseTypeDef:
        """
        Describes one or more of your scheduling policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/describe_scheduling_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#describe_scheduling_policies)
        """

    def describe_service_environments(
        self, **kwargs: Unpack[DescribeServiceEnvironmentsRequestTypeDef]
    ) -> DescribeServiceEnvironmentsResponseTypeDef:
        """
        Describes one or more of your service environments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/describe_service_environments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#describe_service_environments)
        """

    def describe_service_job(
        self, **kwargs: Unpack[DescribeServiceJobRequestTypeDef]
    ) -> DescribeServiceJobResponseTypeDef:
        """
        The details of a service job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/describe_service_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#describe_service_job)
        """

    def get_job_queue_snapshot(
        self, **kwargs: Unpack[GetJobQueueSnapshotRequestTypeDef]
    ) -> GetJobQueueSnapshotResponseTypeDef:
        """
        Provides a list of the first 100 <code>RUNNABLE</code> jobs associated to a
        single job queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/get_job_queue_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#get_job_queue_snapshot)
        """

    def list_consumable_resources(
        self, **kwargs: Unpack[ListConsumableResourcesRequestTypeDef]
    ) -> ListConsumableResourcesResponseTypeDef:
        """
        Returns a list of Batch consumable resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/list_consumable_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#list_consumable_resources)
        """

    def list_jobs(self, **kwargs: Unpack[ListJobsRequestTypeDef]) -> ListJobsResponseTypeDef:
        """
        Returns a list of Batch jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/list_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#list_jobs)
        """

    def list_jobs_by_consumable_resource(
        self, **kwargs: Unpack[ListJobsByConsumableResourceRequestTypeDef]
    ) -> ListJobsByConsumableResourceResponseTypeDef:
        """
        Returns a list of Batch jobs that require a specific consumable resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/list_jobs_by_consumable_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#list_jobs_by_consumable_resource)
        """

    def list_scheduling_policies(
        self, **kwargs: Unpack[ListSchedulingPoliciesRequestTypeDef]
    ) -> ListSchedulingPoliciesResponseTypeDef:
        """
        Returns a list of Batch scheduling policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/list_scheduling_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#list_scheduling_policies)
        """

    def list_service_jobs(
        self, **kwargs: Unpack[ListServiceJobsRequestTypeDef]
    ) -> ListServiceJobsResponseTypeDef:
        """
        Returns a list of service jobs for a specified job queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/list_service_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#list_service_jobs)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for an Batch resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#list_tags_for_resource)
        """

    def register_job_definition(
        self, **kwargs: Unpack[RegisterJobDefinitionRequestTypeDef]
    ) -> RegisterJobDefinitionResponseTypeDef:
        """
        Registers an Batch job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/register_job_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#register_job_definition)
        """

    def submit_job(self, **kwargs: Unpack[SubmitJobRequestTypeDef]) -> SubmitJobResponseTypeDef:
        """
        Submits an Batch job from a job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/submit_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#submit_job)
        """

    def submit_service_job(
        self, **kwargs: Unpack[SubmitServiceJobRequestTypeDef]
    ) -> SubmitServiceJobResponseTypeDef:
        """
        Submits a service job to a specified job queue to run on SageMaker AI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/submit_service_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#submit_service_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Associates the specified tags to a resource with the specified
        <code>resourceArn</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#tag_resource)
        """

    def terminate_job(self, **kwargs: Unpack[TerminateJobRequestTypeDef]) -> Dict[str, Any]:
        """
        Terminates a job in a job queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/terminate_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#terminate_job)
        """

    def terminate_service_job(
        self, **kwargs: Unpack[TerminateServiceJobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Terminates a service job in a job queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/terminate_service_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#terminate_service_job)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes specified tags from an Batch resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#untag_resource)
        """

    def update_compute_environment(
        self, **kwargs: Unpack[UpdateComputeEnvironmentRequestTypeDef]
    ) -> UpdateComputeEnvironmentResponseTypeDef:
        """
        Updates an Batch compute environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/update_compute_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#update_compute_environment)
        """

    def update_consumable_resource(
        self, **kwargs: Unpack[UpdateConsumableResourceRequestTypeDef]
    ) -> UpdateConsumableResourceResponseTypeDef:
        """
        Updates a consumable resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/update_consumable_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#update_consumable_resource)
        """

    def update_job_queue(
        self, **kwargs: Unpack[UpdateJobQueueRequestTypeDef]
    ) -> UpdateJobQueueResponseTypeDef:
        """
        Updates a job queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/update_job_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#update_job_queue)
        """

    def update_scheduling_policy(
        self, **kwargs: Unpack[UpdateSchedulingPolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates a scheduling policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/update_scheduling_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#update_scheduling_policy)
        """

    def update_service_environment(
        self, **kwargs: Unpack[UpdateServiceEnvironmentRequestTypeDef]
    ) -> UpdateServiceEnvironmentResponseTypeDef:
        """
        Updates a service environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/update_service_environment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#update_service_environment)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_compute_environments"]
    ) -> DescribeComputeEnvironmentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_job_definitions"]
    ) -> DescribeJobDefinitionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_job_queues"]
    ) -> DescribeJobQueuesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_service_environments"]
    ) -> DescribeServiceEnvironmentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_consumable_resources"]
    ) -> ListConsumableResourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_jobs_by_consumable_resource"]
    ) -> ListJobsByConsumableResourcePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_jobs"]
    ) -> ListJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_scheduling_policies"]
    ) -> ListSchedulingPoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_service_jobs"]
    ) -> ListServiceJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/client/#get_paginator)
        """
