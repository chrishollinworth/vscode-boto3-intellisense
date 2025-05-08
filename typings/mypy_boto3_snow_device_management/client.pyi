"""
Type annotations for snow-device-management service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_snow_device_management.client import SnowDeviceManagementClient

    session = Session()
    client: SnowDeviceManagementClient = session.client("snow-device-management")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListDeviceResourcesPaginator,
    ListDevicesPaginator,
    ListExecutionsPaginator,
    ListTasksPaginator,
)
from .type_defs import (
    CancelTaskInputTypeDef,
    CancelTaskOutputTypeDef,
    CreateTaskInputTypeDef,
    CreateTaskOutputTypeDef,
    DescribeDeviceEc2InputTypeDef,
    DescribeDeviceEc2OutputTypeDef,
    DescribeDeviceInputTypeDef,
    DescribeDeviceOutputTypeDef,
    DescribeExecutionInputTypeDef,
    DescribeExecutionOutputTypeDef,
    DescribeTaskInputTypeDef,
    DescribeTaskOutputTypeDef,
    EmptyResponseMetadataTypeDef,
    ListDeviceResourcesInputTypeDef,
    ListDeviceResourcesOutputTypeDef,
    ListDevicesInputTypeDef,
    ListDevicesOutputTypeDef,
    ListExecutionsInputTypeDef,
    ListExecutionsOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListTasksInputTypeDef,
    ListTasksOutputTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("SnowDeviceManagementClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class SnowDeviceManagementClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management.html#SnowDeviceManagement.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SnowDeviceManagementClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management.html#SnowDeviceManagement.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client/#generate_presigned_url)
        """

    def cancel_task(self, **kwargs: Unpack[CancelTaskInputTypeDef]) -> CancelTaskOutputTypeDef:
        """
        Sends a cancel request for a specified task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/client/cancel_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client/#cancel_task)
        """

    def create_task(self, **kwargs: Unpack[CreateTaskInputTypeDef]) -> CreateTaskOutputTypeDef:
        """
        Instructs one or more devices to start a task, such as unlocking or rebooting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/client/create_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client/#create_task)
        """

    def describe_device(
        self, **kwargs: Unpack[DescribeDeviceInputTypeDef]
    ) -> DescribeDeviceOutputTypeDef:
        """
        Checks device-specific information, such as the device type, software version,
        IP addresses, and lock status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/client/describe_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client/#describe_device)
        """

    def describe_device_ec2_instances(
        self, **kwargs: Unpack[DescribeDeviceEc2InputTypeDef]
    ) -> DescribeDeviceEc2OutputTypeDef:
        """
        Checks the current state of the Amazon EC2 instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/client/describe_device_ec2_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client/#describe_device_ec2_instances)
        """

    def describe_execution(
        self, **kwargs: Unpack[DescribeExecutionInputTypeDef]
    ) -> DescribeExecutionOutputTypeDef:
        """
        Checks the status of a remote task running on one or more target devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/client/describe_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client/#describe_execution)
        """

    def describe_task(
        self, **kwargs: Unpack[DescribeTaskInputTypeDef]
    ) -> DescribeTaskOutputTypeDef:
        """
        Checks the metadata for a given task on a device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/client/describe_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client/#describe_task)
        """

    def list_device_resources(
        self, **kwargs: Unpack[ListDeviceResourcesInputTypeDef]
    ) -> ListDeviceResourcesOutputTypeDef:
        """
        Returns a list of the Amazon Web Services resources available for a device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/client/list_device_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client/#list_device_resources)
        """

    def list_devices(self, **kwargs: Unpack[ListDevicesInputTypeDef]) -> ListDevicesOutputTypeDef:
        """
        Returns a list of all devices on your Amazon Web Services account that have
        Amazon Web Services Snow Device Management enabled in the Amazon Web Services
        Region where the command is run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/client/list_devices.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client/#list_devices)
        """

    def list_executions(
        self, **kwargs: Unpack[ListExecutionsInputTypeDef]
    ) -> ListExecutionsOutputTypeDef:
        """
        Returns the status of tasks for one or more target devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/client/list_executions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client/#list_executions)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Returns a list of tags for a managed device or task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client/#list_tags_for_resource)
        """

    def list_tasks(self, **kwargs: Unpack[ListTasksInputTypeDef]) -> ListTasksOutputTypeDef:
        """
        Returns a list of tasks that can be filtered by state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/client/list_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client/#list_tasks)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds or replaces tags on a device or task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes a tag from a device or task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client/#untag_resource)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_device_resources"]
    ) -> ListDeviceResourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_devices"]
    ) -> ListDevicesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_executions"]
    ) -> ListExecutionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tasks"]
    ) -> ListTasksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client/#get_paginator)
        """
