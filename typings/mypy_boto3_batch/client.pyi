# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for batch service client

Usage::

    ```python
    import boto3
    from mypy_boto3_batch import BatchClient

    client: BatchClient = boto3.client("batch")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_batch.paginator import (
    DescribeComputeEnvironmentsPaginator,
    DescribeJobDefinitionsPaginator,
    DescribeJobQueuesPaginator,
    ListJobsPaginator,
)
from mypy_boto3_batch.type_defs import (
    ArrayPropertiesTypeDef,
    ComputeEnvironmentOrderTypeDef,
    ComputeResourceTypeDef,
    ComputeResourceUpdateTypeDef,
    ContainerOverridesTypeDef,
    ContainerPropertiesTypeDef,
    CreateComputeEnvironmentResponseTypeDef,
    CreateJobQueueResponseTypeDef,
    DescribeComputeEnvironmentsResponseTypeDef,
    DescribeJobDefinitionsResponseTypeDef,
    DescribeJobQueuesResponseTypeDef,
    DescribeJobsResponseTypeDef,
    JobDependencyTypeDef,
    JobTimeoutTypeDef,
    ListJobsResponseTypeDef,
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


class BatchClient:
    """
    [Batch.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Client.can_paginate)
        """

    def cancel_job(self, jobId: str, reason: str) -> Dict[str, Any]:
        """
        [Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Client.cancel_job)
        """

    def create_compute_environment(
        self,
        computeEnvironmentName: str,
        type: Literal["MANAGED", "UNMANAGED"],
        serviceRole: str,
        state: Literal["ENABLED", "DISABLED"] = None,
        computeResources: "ComputeResourceTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> CreateComputeEnvironmentResponseTypeDef:
        """
        [Client.create_compute_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Client.create_compute_environment)
        """

    def create_job_queue(
        self,
        jobQueueName: str,
        priority: int,
        computeEnvironmentOrder: List["ComputeEnvironmentOrderTypeDef"],
        state: Literal["ENABLED", "DISABLED"] = None,
        tags: Dict[str, str] = None,
    ) -> CreateJobQueueResponseTypeDef:
        """
        [Client.create_job_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Client.create_job_queue)
        """

    def delete_compute_environment(self, computeEnvironment: str) -> Dict[str, Any]:
        """
        [Client.delete_compute_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Client.delete_compute_environment)
        """

    def delete_job_queue(self, jobQueue: str) -> Dict[str, Any]:
        """
        [Client.delete_job_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Client.delete_job_queue)
        """

    def deregister_job_definition(self, jobDefinition: str) -> Dict[str, Any]:
        """
        [Client.deregister_job_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Client.deregister_job_definition)
        """

    def describe_compute_environments(
        self, computeEnvironments: List[str] = None, maxResults: int = None, nextToken: str = None
    ) -> DescribeComputeEnvironmentsResponseTypeDef:
        """
        [Client.describe_compute_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Client.describe_compute_environments)
        """

    def describe_job_definitions(
        self,
        jobDefinitions: List[str] = None,
        maxResults: int = None,
        jobDefinitionName: str = None,
        status: str = None,
        nextToken: str = None,
    ) -> DescribeJobDefinitionsResponseTypeDef:
        """
        [Client.describe_job_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Client.describe_job_definitions)
        """

    def describe_job_queues(
        self, jobQueues: List[str] = None, maxResults: int = None, nextToken: str = None
    ) -> DescribeJobQueuesResponseTypeDef:
        """
        [Client.describe_job_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Client.describe_job_queues)
        """

    def describe_jobs(self, jobs: List[str]) -> DescribeJobsResponseTypeDef:
        """
        [Client.describe_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Client.describe_jobs)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Client.generate_presigned_url)
        """

    def list_jobs(
        self,
        jobQueue: str = None,
        arrayJobId: str = None,
        multiNodeJobId: str = None,
        jobStatus: Literal[
            "SUBMITTED", "PENDING", "RUNNABLE", "STARTING", "RUNNING", "SUCCEEDED", "FAILED"
        ] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListJobsResponseTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Client.list_jobs)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Client.list_tags_for_resource)
        """

    def register_job_definition(
        self,
        jobDefinitionName: str,
        type: Literal["container", "multinode"],
        parameters: Dict[str, str] = None,
        containerProperties: "ContainerPropertiesTypeDef" = None,
        nodeProperties: "NodePropertiesTypeDef" = None,
        retryStrategy: "RetryStrategyTypeDef" = None,
        timeout: "JobTimeoutTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> RegisterJobDefinitionResponseTypeDef:
        """
        [Client.register_job_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Client.register_job_definition)
        """

    def submit_job(
        self,
        jobName: str,
        jobQueue: str,
        jobDefinition: str,
        arrayProperties: ArrayPropertiesTypeDef = None,
        dependsOn: List["JobDependencyTypeDef"] = None,
        parameters: Dict[str, str] = None,
        containerOverrides: "ContainerOverridesTypeDef" = None,
        nodeOverrides: NodeOverridesTypeDef = None,
        retryStrategy: "RetryStrategyTypeDef" = None,
        timeout: "JobTimeoutTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> SubmitJobResponseTypeDef:
        """
        [Client.submit_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Client.submit_job)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Client.tag_resource)
        """

    def terminate_job(self, jobId: str, reason: str) -> Dict[str, Any]:
        """
        [Client.terminate_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Client.terminate_job)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Client.untag_resource)
        """

    def update_compute_environment(
        self,
        computeEnvironment: str,
        state: Literal["ENABLED", "DISABLED"] = None,
        computeResources: ComputeResourceUpdateTypeDef = None,
        serviceRole: str = None,
    ) -> UpdateComputeEnvironmentResponseTypeDef:
        """
        [Client.update_compute_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Client.update_compute_environment)
        """

    def update_job_queue(
        self,
        jobQueue: str,
        state: Literal["ENABLED", "DISABLED"] = None,
        priority: int = None,
        computeEnvironmentOrder: List["ComputeEnvironmentOrderTypeDef"] = None,
    ) -> UpdateJobQueueResponseTypeDef:
        """
        [Client.update_job_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Client.update_job_queue)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_compute_environments"]
    ) -> DescribeComputeEnvironmentsPaginator:
        """
        [Paginator.DescribeComputeEnvironments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Paginator.DescribeComputeEnvironments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_job_definitions"]
    ) -> DescribeJobDefinitionsPaginator:
        """
        [Paginator.DescribeJobDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Paginator.DescribeJobDefinitions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_job_queues"]
    ) -> DescribeJobQueuesPaginator:
        """
        [Paginator.DescribeJobQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Paginator.DescribeJobQueues)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Paginator.ListJobs)
        """
