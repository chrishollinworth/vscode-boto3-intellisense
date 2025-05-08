"""
Type annotations for iot-jobs-data service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_iot_jobs_data.client import IoTJobsDataPlaneClient

    session = Session()
    client: IoTJobsDataPlaneClient = session.client("iot-jobs-data")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    DescribeJobExecutionRequestTypeDef,
    DescribeJobExecutionResponseTypeDef,
    GetPendingJobExecutionsRequestTypeDef,
    GetPendingJobExecutionsResponseTypeDef,
    StartCommandExecutionRequestTypeDef,
    StartCommandExecutionResponseTypeDef,
    StartNextPendingJobExecutionRequestTypeDef,
    StartNextPendingJobExecutionResponseTypeDef,
    UpdateJobExecutionRequestTypeDef,
    UpdateJobExecutionResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("IoTJobsDataPlaneClient",)

class Exceptions(BaseClientExceptions):
    CertificateValidationException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidStateTransitionException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TerminalStateException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class IoTJobsDataPlaneClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IoTJobsDataPlaneClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-jobs-data/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-jobs-data/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/client/#generate_presigned_url)
        """

    def describe_job_execution(
        self, **kwargs: Unpack[DescribeJobExecutionRequestTypeDef]
    ) -> DescribeJobExecutionResponseTypeDef:
        """
        Gets details of a job execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-jobs-data/client/describe_job_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/client/#describe_job_execution)
        """

    def get_pending_job_executions(
        self, **kwargs: Unpack[GetPendingJobExecutionsRequestTypeDef]
    ) -> GetPendingJobExecutionsResponseTypeDef:
        """
        Gets the list of all jobs for a thing that are not in a terminal status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-jobs-data/client/get_pending_job_executions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/client/#get_pending_job_executions)
        """

    def start_command_execution(
        self, **kwargs: Unpack[StartCommandExecutionRequestTypeDef]
    ) -> StartCommandExecutionResponseTypeDef:
        """
        Using the command created with the <code>CreateCommand</code> API, start a
        command execution on a specific device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-jobs-data/client/start_command_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/client/#start_command_execution)
        """

    def start_next_pending_job_execution(
        self, **kwargs: Unpack[StartNextPendingJobExecutionRequestTypeDef]
    ) -> StartNextPendingJobExecutionResponseTypeDef:
        """
        Gets and starts the next pending (status IN_PROGRESS or QUEUED) job execution
        for a thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-jobs-data/client/start_next_pending_job_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/client/#start_next_pending_job_execution)
        """

    def update_job_execution(
        self, **kwargs: Unpack[UpdateJobExecutionRequestTypeDef]
    ) -> UpdateJobExecutionResponseTypeDef:
        """
        Updates the status of a job execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-jobs-data/client/update_job_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/client/#update_job_execution)
        """
