"""
Type annotations for batch service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_batch import BatchClient

    client: BatchClient = boto3.client("batch")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    CEStateType,
    CETypeType,
    JobDefinitionTypeType,
    JobStatusType,
    JQStateType,
    PlatformCapabilityType,
)
from .paginator import (
    DescribeComputeEnvironmentsPaginator,
    DescribeJobDefinitionsPaginator,
    DescribeJobQueuesPaginator,
    ListJobsPaginator,
    ListSchedulingPoliciesPaginator,
)
from .type_defs import (
    ArrayPropertiesTypeDef,
    ComputeEnvironmentOrderTypeDef,
    ComputeResourceTypeDef,
    ComputeResourceUpdateTypeDef,
    ContainerOverridesTypeDef,
    ContainerPropertiesTypeDef,
    CreateComputeEnvironmentResponseTypeDef,
    CreateJobQueueResponseTypeDef,
    CreateSchedulingPolicyResponseTypeDef,
    DescribeComputeEnvironmentsResponseTypeDef,
    DescribeJobDefinitionsResponseTypeDef,
    DescribeJobQueuesResponseTypeDef,
    DescribeJobsResponseTypeDef,
    DescribeSchedulingPoliciesResponseTypeDef,
    FairsharePolicyTypeDef,
    JobDependencyTypeDef,
    JobTimeoutTypeDef,
    KeyValuesPairTypeDef,
    ListJobsResponseTypeDef,
    ListSchedulingPoliciesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    NodeOverridesTypeDef,
    NodePropertiesTypeDef,
    RegisterJobDefinitionResponseTypeDef,
    RetryStrategyTypeDef,
    SubmitJobResponseTypeDef,
    UpdateComputeEnvironmentResponseTypeDef,
    UpdateJobQueueResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("BatchClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ClientException: Type[BotocoreClientError]
    ServerException: Type[BotocoreClientError]

class BatchClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        BatchClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#can_paginate)
        """
    def cancel_job(self, *, jobId: str, reason: str) -> Dict[str, Any]:
        """
        Cancels a job in an Batch job queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.cancel_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#cancel_job)
        """
    def create_compute_environment(
        self,
        *,
        computeEnvironmentName: str,
        type: CETypeType,
        state: CEStateType = None,
        unmanagedvCpus: int = None,
        computeResources: "ComputeResourceTypeDef" = None,
        serviceRole: str = None,
        tags: Dict[str, str] = None
    ) -> CreateComputeEnvironmentResponseTypeDef:
        """
        Creates an Batch compute environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.create_compute_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#create_compute_environment)
        """
    def create_job_queue(
        self,
        *,
        jobQueueName: str,
        priority: int,
        computeEnvironmentOrder: List["ComputeEnvironmentOrderTypeDef"],
        state: JQStateType = None,
        schedulingPolicyArn: str = None,
        tags: Dict[str, str] = None
    ) -> CreateJobQueueResponseTypeDef:
        """
        Creates an Batch job queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.create_job_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#create_job_queue)
        """
    def create_scheduling_policy(
        self,
        *,
        name: str,
        fairsharePolicy: "FairsharePolicyTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateSchedulingPolicyResponseTypeDef:
        """
        Creates an Batch scheduling policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.create_scheduling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#create_scheduling_policy)
        """
    def delete_compute_environment(self, *, computeEnvironment: str) -> Dict[str, Any]:
        """
        Deletes an Batch compute environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.delete_compute_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#delete_compute_environment)
        """
    def delete_job_queue(self, *, jobQueue: str) -> Dict[str, Any]:
        """
        Deletes the specified job queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.delete_job_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#delete_job_queue)
        """
    def delete_scheduling_policy(self, *, arn: str) -> Dict[str, Any]:
        """
        Deletes the specified scheduling policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.delete_scheduling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#delete_scheduling_policy)
        """
    def deregister_job_definition(self, *, jobDefinition: str) -> Dict[str, Any]:
        """
        Deregisters an Batch job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.deregister_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#deregister_job_definition)
        """
    def describe_compute_environments(
        self,
        *,
        computeEnvironments: List[str] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeComputeEnvironmentsResponseTypeDef:
        """
        Describes one or more of your compute environments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.describe_compute_environments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#describe_compute_environments)
        """
    def describe_job_definitions(
        self,
        *,
        jobDefinitions: List[str] = None,
        maxResults: int = None,
        jobDefinitionName: str = None,
        status: str = None,
        nextToken: str = None
    ) -> DescribeJobDefinitionsResponseTypeDef:
        """
        Describes a list of job definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.describe_job_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#describe_job_definitions)
        """
    def describe_job_queues(
        self, *, jobQueues: List[str] = None, maxResults: int = None, nextToken: str = None
    ) -> DescribeJobQueuesResponseTypeDef:
        """
        Describes one or more of your job queues.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.describe_job_queues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#describe_job_queues)
        """
    def describe_jobs(self, *, jobs: List[str]) -> DescribeJobsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.describe_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#describe_jobs)
        """
    def describe_scheduling_policies(
        self, *, arns: List[str]
    ) -> DescribeSchedulingPoliciesResponseTypeDef:
        """
        Describes one or more of your scheduling policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.describe_scheduling_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#describe_scheduling_policies)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#generate_presigned_url)
        """
    def list_jobs(
        self,
        *,
        jobQueue: str = None,
        arrayJobId: str = None,
        multiNodeJobId: str = None,
        jobStatus: JobStatusType = None,
        maxResults: int = None,
        nextToken: str = None,
        filters: List["KeyValuesPairTypeDef"] = None
    ) -> ListJobsResponseTypeDef:
        """
        Returns a list of Batch jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.list_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#list_jobs)
        """
    def list_scheduling_policies(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListSchedulingPoliciesResponseTypeDef:
        """
        Returns a list of Batch scheduling policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.list_scheduling_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#list_scheduling_policies)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for an Batch resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#list_tags_for_resource)
        """
    def register_job_definition(
        self,
        *,
        jobDefinitionName: str,
        type: JobDefinitionTypeType,
        parameters: Dict[str, str] = None,
        schedulingPriority: int = None,
        containerProperties: "ContainerPropertiesTypeDef" = None,
        nodeProperties: "NodePropertiesTypeDef" = None,
        retryStrategy: "RetryStrategyTypeDef" = None,
        propagateTags: bool = None,
        timeout: "JobTimeoutTypeDef" = None,
        tags: Dict[str, str] = None,
        platformCapabilities: List[PlatformCapabilityType] = None
    ) -> RegisterJobDefinitionResponseTypeDef:
        """
        Registers an Batch job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.register_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#register_job_definition)
        """
    def submit_job(
        self,
        *,
        jobName: str,
        jobQueue: str,
        jobDefinition: str,
        shareIdentifier: str = None,
        schedulingPriorityOverride: int = None,
        arrayProperties: "ArrayPropertiesTypeDef" = None,
        dependsOn: List["JobDependencyTypeDef"] = None,
        parameters: Dict[str, str] = None,
        containerOverrides: "ContainerOverridesTypeDef" = None,
        nodeOverrides: "NodeOverridesTypeDef" = None,
        retryStrategy: "RetryStrategyTypeDef" = None,
        propagateTags: bool = None,
        timeout: "JobTimeoutTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> SubmitJobResponseTypeDef:
        """
        Submits an Batch job from a job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.submit_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#submit_job)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Associates the specified tags to a resource with the specified `resourceArn`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#tag_resource)
        """
    def terminate_job(self, *, jobId: str, reason: str) -> Dict[str, Any]:
        """
        Terminates a job in a job queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.terminate_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#terminate_job)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Deletes specified tags from an Batch resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#untag_resource)
        """
    def update_compute_environment(
        self,
        *,
        computeEnvironment: str,
        state: CEStateType = None,
        unmanagedvCpus: int = None,
        computeResources: "ComputeResourceUpdateTypeDef" = None,
        serviceRole: str = None
    ) -> UpdateComputeEnvironmentResponseTypeDef:
        """
        Updates an Batch compute environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.update_compute_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#update_compute_environment)
        """
    def update_job_queue(
        self,
        *,
        jobQueue: str,
        state: JQStateType = None,
        schedulingPolicyArn: str = None,
        priority: int = None,
        computeEnvironmentOrder: List["ComputeEnvironmentOrderTypeDef"] = None
    ) -> UpdateJobQueueResponseTypeDef:
        """
        Updates a job queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.update_job_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#update_job_queue)
        """
    def update_scheduling_policy(
        self, *, arn: str, fairsharePolicy: "FairsharePolicyTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates a scheduling policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Client.update_scheduling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/client.html#update_scheduling_policy)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_compute_environments"]
    ) -> DescribeComputeEnvironmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Paginator.DescribeComputeEnvironments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators.html#describecomputeenvironmentspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_job_definitions"]
    ) -> DescribeJobDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Paginator.DescribeJobDefinitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators.html#describejobdefinitionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_job_queues"]
    ) -> DescribeJobQueuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Paginator.DescribeJobQueues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators.html#describejobqueuespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Paginator.ListJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators.html#listjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_scheduling_policies"]
    ) -> ListSchedulingPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/batch.html#Batch.Paginator.ListSchedulingPolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators.html#listschedulingpoliciespaginator)
        """
