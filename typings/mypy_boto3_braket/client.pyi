"""
Type annotations for braket service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_braket.client import BraketClient

    session = Session()
    client: BraketClient = session.client("braket")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import SearchDevicesPaginator, SearchJobsPaginator, SearchQuantumTasksPaginator
from .type_defs import (
    CancelJobRequestTypeDef,
    CancelJobResponseTypeDef,
    CancelQuantumTaskRequestTypeDef,
    CancelQuantumTaskResponseTypeDef,
    CreateJobRequestTypeDef,
    CreateJobResponseTypeDef,
    CreateQuantumTaskRequestTypeDef,
    CreateQuantumTaskResponseTypeDef,
    GetDeviceRequestTypeDef,
    GetDeviceResponseTypeDef,
    GetJobRequestTypeDef,
    GetJobResponseTypeDef,
    GetQuantumTaskRequestTypeDef,
    GetQuantumTaskResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    SearchDevicesRequestTypeDef,
    SearchDevicesResponseTypeDef,
    SearchJobsRequestTypeDef,
    SearchJobsResponseTypeDef,
    SearchQuantumTasksRequestTypeDef,
    SearchQuantumTasksResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
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

__all__ = ("BraketClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        BraketClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#generate_presigned_url)
        """

    def cancel_job(self, **kwargs: Unpack[CancelJobRequestTypeDef]) -> CancelJobResponseTypeDef:
        """
        Cancels an Amazon Braket job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/client/cancel_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#cancel_job)
        """

    def cancel_quantum_task(
        self, **kwargs: Unpack[CancelQuantumTaskRequestTypeDef]
    ) -> CancelQuantumTaskResponseTypeDef:
        """
        Cancels the specified task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/client/cancel_quantum_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#cancel_quantum_task)
        """

    def create_job(self, **kwargs: Unpack[CreateJobRequestTypeDef]) -> CreateJobResponseTypeDef:
        """
        Creates an Amazon Braket job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/client/create_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#create_job)
        """

    def create_quantum_task(
        self, **kwargs: Unpack[CreateQuantumTaskRequestTypeDef]
    ) -> CreateQuantumTaskResponseTypeDef:
        """
        Creates a quantum task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/client/create_quantum_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#create_quantum_task)
        """

    def get_device(self, **kwargs: Unpack[GetDeviceRequestTypeDef]) -> GetDeviceResponseTypeDef:
        """
        Retrieves the devices available in Amazon Braket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/client/get_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#get_device)
        """

    def get_job(self, **kwargs: Unpack[GetJobRequestTypeDef]) -> GetJobResponseTypeDef:
        """
        Retrieves the specified Amazon Braket job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/client/get_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#get_job)
        """

    def get_quantum_task(
        self, **kwargs: Unpack[GetQuantumTaskRequestTypeDef]
    ) -> GetQuantumTaskResponseTypeDef:
        """
        Retrieves the specified quantum task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/client/get_quantum_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#get_quantum_task)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Shows the tags associated with this resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#list_tags_for_resource)
        """

    def search_devices(
        self, **kwargs: Unpack[SearchDevicesRequestTypeDef]
    ) -> SearchDevicesResponseTypeDef:
        """
        Searches for devices using the specified filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/client/search_devices.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#search_devices)
        """

    def search_jobs(self, **kwargs: Unpack[SearchJobsRequestTypeDef]) -> SearchJobsResponseTypeDef:
        """
        Searches for Amazon Braket jobs that match the specified filter values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/client/search_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#search_jobs)
        """

    def search_quantum_tasks(
        self, **kwargs: Unpack[SearchQuantumTasksRequestTypeDef]
    ) -> SearchQuantumTasksResponseTypeDef:
        """
        Searches for tasks that match the specified filter values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/client/search_quantum_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#search_quantum_tasks)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Add a tag to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Remove tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#untag_resource)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_devices"]
    ) -> SearchDevicesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_jobs"]
    ) -> SearchJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_quantum_tasks"]
    ) -> SearchQuantumTasksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#get_paginator)
        """
