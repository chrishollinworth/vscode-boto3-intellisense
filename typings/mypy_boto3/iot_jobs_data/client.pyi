"""
Type annotations for iot-jobs-data service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_iot_jobs_data import IoTJobsDataPlaneClient

    client: IoTJobsDataPlaneClient = boto3.client("iot-jobs-data")
    ```
"""
from typing import Any, Dict, Type

from botocore.client import BaseClient, ClientMeta

from .literals import JobExecutionStatusType
from .type_defs import (
    DescribeJobExecutionResponseTypeDef,
    GetPendingJobExecutionsResponseTypeDef,
    StartNextPendingJobExecutionResponseTypeDef,
    UpdateJobExecutionResponseTypeDef,
)

__all__ = ("IoTJobsDataPlaneClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    CertificateValidationException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidStateTransitionException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TerminalStateException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class IoTJobsDataPlaneClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IoTJobsDataPlaneClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/client.html#close)
        """
    def describe_job_execution(
        self,
        *,
        jobId: str,
        thingName: str,
        includeJobDocument: bool = None,
        executionNumber: int = None
    ) -> DescribeJobExecutionResponseTypeDef:
        """
        Gets details of a job execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.describe_job_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/client.html#describe_job_execution)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/client.html#generate_presigned_url)
        """
    def get_pending_job_executions(
        self, *, thingName: str
    ) -> GetPendingJobExecutionsResponseTypeDef:
        """
        Gets the list of all jobs for a thing that are not in a terminal status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.get_pending_job_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/client.html#get_pending_job_executions)
        """
    def start_next_pending_job_execution(
        self,
        *,
        thingName: str,
        statusDetails: Dict[str, str] = None,
        stepTimeoutInMinutes: int = None
    ) -> StartNextPendingJobExecutionResponseTypeDef:
        """
        Gets and starts the next pending (status IN_PROGRESS or QUEUED) job execution
        for a thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.start_next_pending_job_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/client.html#start_next_pending_job_execution)
        """
    def update_job_execution(
        self,
        *,
        jobId: str,
        thingName: str,
        status: JobExecutionStatusType,
        statusDetails: Dict[str, str] = None,
        stepTimeoutInMinutes: int = None,
        expectedVersion: int = None,
        includeJobExecutionState: bool = None,
        includeJobDocument: bool = None,
        executionNumber: int = None
    ) -> UpdateJobExecutionResponseTypeDef:
        """
        Updates the status of a job execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.update_job_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/client.html#update_job_execution)
        """
