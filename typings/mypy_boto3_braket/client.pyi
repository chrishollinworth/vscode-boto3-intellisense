"""
Type annotations for braket service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_braket import BraketClient

    client: BraketClient = boto3.client("braket")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import SearchDevicesPaginator, SearchJobsPaginator, SearchQuantumTasksPaginator
from .type_defs import (
    AlgorithmSpecificationTypeDef,
    CancelJobResponseTypeDef,
    CancelQuantumTaskResponseTypeDef,
    CreateJobResponseTypeDef,
    CreateQuantumTaskResponseTypeDef,
    DeviceConfigTypeDef,
    GetDeviceResponseTypeDef,
    GetJobResponseTypeDef,
    GetQuantumTaskResponseTypeDef,
    InputFileConfigTypeDef,
    InstanceConfigTypeDef,
    JobCheckpointConfigTypeDef,
    JobOutputDataConfigTypeDef,
    JobStoppingConditionTypeDef,
    ListTagsForResourceResponseTypeDef,
    SearchDevicesFilterTypeDef,
    SearchDevicesResponseTypeDef,
    SearchJobsFilterTypeDef,
    SearchJobsResponseTypeDef,
    SearchQuantumTasksFilterTypeDef,
    SearchQuantumTasksResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("BraketClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DeviceOfflineException: Type[BotocoreClientError]
    DeviceRetiredException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class BraketClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/braket.html#Braket.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        BraketClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/braket.html#Braket.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#can_paginate)
        """
    def cancel_job(self, *, jobArn: str) -> CancelJobResponseTypeDef:
        """
        Cancels an Amazon Braket job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/braket.html#Braket.Client.cancel_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#cancel_job)
        """
    def cancel_quantum_task(
        self, *, clientToken: str, quantumTaskArn: str
    ) -> CancelQuantumTaskResponseTypeDef:
        """
        Cancels the specified task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/braket.html#Braket.Client.cancel_quantum_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#cancel_quantum_task)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/braket.html#Braket.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#close)
        """
    def create_job(
        self,
        *,
        algorithmSpecification: "AlgorithmSpecificationTypeDef",
        clientToken: str,
        deviceConfig: "DeviceConfigTypeDef",
        instanceConfig: "InstanceConfigTypeDef",
        jobName: str,
        outputDataConfig: "JobOutputDataConfigTypeDef",
        roleArn: str,
        checkpointConfig: "JobCheckpointConfigTypeDef" = None,
        hyperParameters: Dict[str, str] = None,
        inputDataConfig: List["InputFileConfigTypeDef"] = None,
        stoppingCondition: "JobStoppingConditionTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateJobResponseTypeDef:
        """
        Creates an Amazon Braket job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/braket.html#Braket.Client.create_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#create_job)
        """
    def create_quantum_task(
        self,
        *,
        action: str,
        clientToken: str,
        deviceArn: str,
        outputS3Bucket: str,
        outputS3KeyPrefix: str,
        shots: int,
        deviceParameters: str = None,
        jobToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreateQuantumTaskResponseTypeDef:
        """
        Creates a quantum task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/braket.html#Braket.Client.create_quantum_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#create_quantum_task)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/braket.html#Braket.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#generate_presigned_url)
        """
    def get_device(self, *, deviceArn: str) -> GetDeviceResponseTypeDef:
        """
        Retrieves the devices available in Amazon Braket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/braket.html#Braket.Client.get_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#get_device)
        """
    def get_job(self, *, jobArn: str) -> GetJobResponseTypeDef:
        """
        Retrieves the specified Amazon Braket job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/braket.html#Braket.Client.get_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#get_job)
        """
    def get_quantum_task(self, *, quantumTaskArn: str) -> GetQuantumTaskResponseTypeDef:
        """
        Retrieves the specified quantum task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/braket.html#Braket.Client.get_quantum_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#get_quantum_task)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Shows the tags associated with this resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/braket.html#Braket.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#list_tags_for_resource)
        """
    def search_devices(
        self,
        *,
        filters: List["SearchDevicesFilterTypeDef"],
        maxResults: int = None,
        nextToken: str = None
    ) -> SearchDevicesResponseTypeDef:
        """
        Searches for devices using the specified filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/braket.html#Braket.Client.search_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#search_devices)
        """
    def search_jobs(
        self,
        *,
        filters: List["SearchJobsFilterTypeDef"],
        maxResults: int = None,
        nextToken: str = None
    ) -> SearchJobsResponseTypeDef:
        """
        Searches for Amazon Braket jobs that match the specified filter values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/braket.html#Braket.Client.search_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#search_jobs)
        """
    def search_quantum_tasks(
        self,
        *,
        filters: List["SearchQuantumTasksFilterTypeDef"],
        maxResults: int = None,
        nextToken: str = None
    ) -> SearchQuantumTasksResponseTypeDef:
        """
        Searches for tasks that match the specified filter values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/braket.html#Braket.Client.search_quantum_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#search_quantum_tasks)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Add a tag to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/braket.html#Braket.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Remove tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/braket.html#Braket.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#untag_resource)
        """
    @overload
    def get_paginator(self, operation_name: Literal["search_devices"]) -> SearchDevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/braket.html#Braket.Paginator.SearchDevices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/paginators.html#searchdevicespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["search_jobs"]) -> SearchJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/braket.html#Braket.Paginator.SearchJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/paginators.html#searchjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["search_quantum_tasks"]
    ) -> SearchQuantumTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/braket.html#Braket.Paginator.SearchQuantumTasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/paginators.html#searchquantumtaskspaginator)
        """
