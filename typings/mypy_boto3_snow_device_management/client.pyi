"""
Type annotations for snow-device-management service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_snow_device_management import SnowDeviceManagementClient

    client: SnowDeviceManagementClient = boto3.client("snow-device-management")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import ExecutionStateType, TaskStateType
from .paginator import (
    ListDeviceResourcesPaginator,
    ListDevicesPaginator,
    ListExecutionsPaginator,
    ListTasksPaginator,
)
from .type_defs import (
    CancelTaskOutputTypeDef,
    CommandTypeDef,
    CreateTaskOutputTypeDef,
    DescribeDeviceEc2OutputTypeDef,
    DescribeDeviceOutputTypeDef,
    DescribeExecutionOutputTypeDef,
    DescribeTaskOutputTypeDef,
    ListDeviceResourcesOutputTypeDef,
    ListDevicesOutputTypeDef,
    ListExecutionsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListTasksOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("SnowDeviceManagementClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class SnowDeviceManagementClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/snow-device-management.html#SnowDeviceManagement.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SnowDeviceManagementClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/snow-device-management.html#SnowDeviceManagement.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client.html#can_paginate)
        """
    def cancel_task(self, *, taskId: str) -> CancelTaskOutputTypeDef:
        """
        Sends a cancel request for a specified task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/snow-device-management.html#SnowDeviceManagement.Client.cancel_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client.html#cancel_task)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/snow-device-management.html#SnowDeviceManagement.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client.html#close)
        """
    def create_task(
        self,
        *,
        command: "CommandTypeDef",
        targets: List[str],
        clientToken: str = None,
        description: str = None,
        tags: Dict[str, str] = None
    ) -> CreateTaskOutputTypeDef:
        """
        Instructs one or more devices to start a task, such as unlocking or rebooting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/snow-device-management.html#SnowDeviceManagement.Client.create_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client.html#create_task)
        """
    def describe_device(self, *, managedDeviceId: str) -> DescribeDeviceOutputTypeDef:
        """
        Checks device-specific information, such as the device type, software version,
        IP addresses, and lock status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/snow-device-management.html#SnowDeviceManagement.Client.describe_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client.html#describe_device)
        """
    def describe_device_ec2_instances(
        self, *, instanceIds: List[str], managedDeviceId: str
    ) -> DescribeDeviceEc2OutputTypeDef:
        """
        Checks the current state of the Amazon EC2 instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/snow-device-management.html#SnowDeviceManagement.Client.describe_device_ec2_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client.html#describe_device_ec2_instances)
        """
    def describe_execution(
        self, *, managedDeviceId: str, taskId: str
    ) -> DescribeExecutionOutputTypeDef:
        """
        Checks the status of a remote task running on one or more target devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/snow-device-management.html#SnowDeviceManagement.Client.describe_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client.html#describe_execution)
        """
    def describe_task(self, *, taskId: str) -> DescribeTaskOutputTypeDef:
        """
        Checks the metadata for a given task on a device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/snow-device-management.html#SnowDeviceManagement.Client.describe_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client.html#describe_task)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/snow-device-management.html#SnowDeviceManagement.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client.html#generate_presigned_url)
        """
    def list_device_resources(
        self,
        *,
        managedDeviceId: str,
        maxResults: int = None,
        nextToken: str = None,
        type: str = None
    ) -> ListDeviceResourcesOutputTypeDef:
        """
        Returns a list of the Amazon Web Services resources available for a device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/snow-device-management.html#SnowDeviceManagement.Client.list_device_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client.html#list_device_resources)
        """
    def list_devices(
        self, *, jobId: str = None, maxResults: int = None, nextToken: str = None
    ) -> ListDevicesOutputTypeDef:
        """
        Returns a list of all devices on your Amazon Web Services account that have
        Amazon Web Services Snow Device Management enabled in the Amazon Web Services
        Region where the command is run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/snow-device-management.html#SnowDeviceManagement.Client.list_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client.html#list_devices)
        """
    def list_executions(
        self,
        *,
        taskId: str,
        maxResults: int = None,
        nextToken: str = None,
        state: ExecutionStateType = None
    ) -> ListExecutionsOutputTypeDef:
        """
        Returns the status of tasks for one or more target devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/snow-device-management.html#SnowDeviceManagement.Client.list_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client.html#list_executions)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        Returns a list of tags for a managed device or task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/snow-device-management.html#SnowDeviceManagement.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client.html#list_tags_for_resource)
        """
    def list_tasks(
        self, *, maxResults: int = None, nextToken: str = None, state: TaskStateType = None
    ) -> ListTasksOutputTypeDef:
        """
        Returns a list of tasks that can be filtered by state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/snow-device-management.html#SnowDeviceManagement.Client.list_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client.html#list_tasks)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> None:
        """
        Adds or replaces tags on a device or task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/snow-device-management.html#SnowDeviceManagement.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> None:
        """
        Removes a tag from a device or task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/snow-device-management.html#SnowDeviceManagement.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/client.html#untag_resource)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_resources"]
    ) -> ListDeviceResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/snow-device-management.html#SnowDeviceManagement.Paginator.ListDeviceResources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/paginators.html#listdeviceresourcespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_devices"]) -> ListDevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/snow-device-management.html#SnowDeviceManagement.Paginator.ListDevices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/paginators.html#listdevicespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_executions"]) -> ListExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/snow-device-management.html#SnowDeviceManagement.Paginator.ListExecutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/paginators.html#listexecutionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_tasks"]) -> ListTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/snow-device-management.html#SnowDeviceManagement.Paginator.ListTasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/paginators.html#listtaskspaginator)
        """
