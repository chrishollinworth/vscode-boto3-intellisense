# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for iot-jobs-data service client

Usage::

    ```python
    import boto3
    from mypy_boto3_iot_jobs_data import IoTJobsDataPlaneClient

    client: IoTJobsDataPlaneClient = boto3.client("iot-jobs-data")
    ```
"""
import sys
from typing import Any, Dict, Type

from botocore.client import ClientMeta

from mypy_boto3_iot_jobs_data.type_defs import (
    DescribeJobExecutionResponseTypeDef,
    GetPendingJobExecutionsResponseTypeDef,
    StartNextPendingJobExecutionResponseTypeDef,
    UpdateJobExecutionResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


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


class IoTJobsDataPlaneClient:
    """
    [IoTJobsDataPlane.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.can_paginate)
        """

    def describe_job_execution(
        self,
        jobId: str,
        thingName: str,
        includeJobDocument: bool = None,
        executionNumber: int = None,
    ) -> DescribeJobExecutionResponseTypeDef:
        """
        [Client.describe_job_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.describe_job_execution)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.generate_presigned_url)
        """

    def get_pending_job_executions(self, thingName: str) -> GetPendingJobExecutionsResponseTypeDef:
        """
        [Client.get_pending_job_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.get_pending_job_executions)
        """

    def start_next_pending_job_execution(
        self, thingName: str, statusDetails: Dict[str, str] = None, stepTimeoutInMinutes: int = None
    ) -> StartNextPendingJobExecutionResponseTypeDef:
        """
        [Client.start_next_pending_job_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.start_next_pending_job_execution)
        """

    def update_job_execution(
        self,
        jobId: str,
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
        ],
        statusDetails: Dict[str, str] = None,
        stepTimeoutInMinutes: int = None,
        expectedVersion: int = None,
        includeJobExecutionState: bool = None,
        includeJobDocument: bool = None,
        executionNumber: int = None,
    ) -> UpdateJobExecutionResponseTypeDef:
        """
        [Client.update_job_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.update_job_execution)
        """
