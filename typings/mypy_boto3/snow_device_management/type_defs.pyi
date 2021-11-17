"""
Type annotations for snow-device-management service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/type_defs.html)

Usage::

    ```python
    from mypy_boto3_snow_device_management.type_defs import CancelTaskInputRequestTypeDef

    data: CancelTaskInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AttachmentStatusType,
    ExecutionStateType,
    InstanceStateNameType,
    IpAddressAssignmentType,
    PhysicalConnectorTypeType,
    TaskStateType,
    UnlockStateType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CancelTaskInputRequestTypeDef",
    "CancelTaskOutputTypeDef",
    "CapacityTypeDef",
    "CommandTypeDef",
    "CpuOptionsTypeDef",
    "CreateTaskInputRequestTypeDef",
    "CreateTaskOutputTypeDef",
    "DescribeDeviceEc2InputRequestTypeDef",
    "DescribeDeviceEc2OutputTypeDef",
    "DescribeDeviceInputRequestTypeDef",
    "DescribeDeviceOutputTypeDef",
    "DescribeExecutionInputRequestTypeDef",
    "DescribeExecutionOutputTypeDef",
    "DescribeTaskInputRequestTypeDef",
    "DescribeTaskOutputTypeDef",
    "DeviceSummaryTypeDef",
    "EbsInstanceBlockDeviceTypeDef",
    "ExecutionSummaryTypeDef",
    "InstanceBlockDeviceMappingTypeDef",
    "InstanceStateTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTypeDef",
    "ListDeviceResourcesInputRequestTypeDef",
    "ListDeviceResourcesOutputTypeDef",
    "ListDevicesInputRequestTypeDef",
    "ListDevicesOutputTypeDef",
    "ListExecutionsInputRequestTypeDef",
    "ListExecutionsOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListTasksInputRequestTypeDef",
    "ListTasksOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PhysicalNetworkInterfaceTypeDef",
    "ResourceSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "SecurityGroupIdentifierTypeDef",
    "SoftwareInformationTypeDef",
    "TagResourceInputRequestTypeDef",
    "TaskSummaryTypeDef",
    "UntagResourceInputRequestTypeDef",
)

CancelTaskInputRequestTypeDef = TypedDict(
    "CancelTaskInputRequestTypeDef",
    {
        "taskId": str,
    },
)

CancelTaskOutputTypeDef = TypedDict(
    "CancelTaskOutputTypeDef",
    {
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CapacityTypeDef = TypedDict(
    "CapacityTypeDef",
    {
        "available": int,
        "name": str,
        "total": int,
        "unit": str,
        "used": int,
    },
    total=False,
)

CommandTypeDef = TypedDict(
    "CommandTypeDef",
    {
        "reboot": Dict[str, Any],
        "unlock": Dict[str, Any],
    },
    total=False,
)

CpuOptionsTypeDef = TypedDict(
    "CpuOptionsTypeDef",
    {
        "coreCount": int,
        "threadsPerCore": int,
    },
    total=False,
)

_RequiredCreateTaskInputRequestTypeDef = TypedDict(
    "_RequiredCreateTaskInputRequestTypeDef",
    {
        "command": "CommandTypeDef",
        "targets": List[str],
    },
)
_OptionalCreateTaskInputRequestTypeDef = TypedDict(
    "_OptionalCreateTaskInputRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateTaskInputRequestTypeDef(
    _RequiredCreateTaskInputRequestTypeDef, _OptionalCreateTaskInputRequestTypeDef
):
    pass

CreateTaskOutputTypeDef = TypedDict(
    "CreateTaskOutputTypeDef",
    {
        "taskArn": str,
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeviceEc2InputRequestTypeDef = TypedDict(
    "DescribeDeviceEc2InputRequestTypeDef",
    {
        "instanceIds": List[str],
        "managedDeviceId": str,
    },
)

DescribeDeviceEc2OutputTypeDef = TypedDict(
    "DescribeDeviceEc2OutputTypeDef",
    {
        "instances": List["InstanceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeviceInputRequestTypeDef = TypedDict(
    "DescribeDeviceInputRequestTypeDef",
    {
        "managedDeviceId": str,
    },
)

DescribeDeviceOutputTypeDef = TypedDict(
    "DescribeDeviceOutputTypeDef",
    {
        "associatedWithJob": str,
        "deviceCapacities": List["CapacityTypeDef"],
        "deviceState": UnlockStateType,
        "deviceType": str,
        "lastReachedOutAt": datetime,
        "lastUpdatedAt": datetime,
        "managedDeviceArn": str,
        "managedDeviceId": str,
        "physicalNetworkInterfaces": List["PhysicalNetworkInterfaceTypeDef"],
        "software": "SoftwareInformationTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExecutionInputRequestTypeDef = TypedDict(
    "DescribeExecutionInputRequestTypeDef",
    {
        "managedDeviceId": str,
        "taskId": str,
    },
)

DescribeExecutionOutputTypeDef = TypedDict(
    "DescribeExecutionOutputTypeDef",
    {
        "executionId": str,
        "lastUpdatedAt": datetime,
        "managedDeviceId": str,
        "startedAt": datetime,
        "state": ExecutionStateType,
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTaskInputRequestTypeDef = TypedDict(
    "DescribeTaskInputRequestTypeDef",
    {
        "taskId": str,
    },
)

DescribeTaskOutputTypeDef = TypedDict(
    "DescribeTaskOutputTypeDef",
    {
        "completedAt": datetime,
        "createdAt": datetime,
        "description": str,
        "lastUpdatedAt": datetime,
        "state": TaskStateType,
        "tags": Dict[str, str],
        "targets": List[str],
        "taskArn": str,
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceSummaryTypeDef = TypedDict(
    "DeviceSummaryTypeDef",
    {
        "associatedWithJob": str,
        "managedDeviceArn": str,
        "managedDeviceId": str,
        "tags": Dict[str, str],
    },
    total=False,
)

EbsInstanceBlockDeviceTypeDef = TypedDict(
    "EbsInstanceBlockDeviceTypeDef",
    {
        "attachTime": datetime,
        "deleteOnTermination": bool,
        "status": AttachmentStatusType,
        "volumeId": str,
    },
    total=False,
)

ExecutionSummaryTypeDef = TypedDict(
    "ExecutionSummaryTypeDef",
    {
        "executionId": str,
        "managedDeviceId": str,
        "state": ExecutionStateType,
        "taskId": str,
    },
    total=False,
)

InstanceBlockDeviceMappingTypeDef = TypedDict(
    "InstanceBlockDeviceMappingTypeDef",
    {
        "deviceName": str,
        "ebs": "EbsInstanceBlockDeviceTypeDef",
    },
    total=False,
)

InstanceStateTypeDef = TypedDict(
    "InstanceStateTypeDef",
    {
        "code": int,
        "name": InstanceStateNameType,
    },
    total=False,
)

InstanceSummaryTypeDef = TypedDict(
    "InstanceSummaryTypeDef",
    {
        "instance": "InstanceTypeDef",
        "lastUpdatedAt": datetime,
    },
    total=False,
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "amiLaunchIndex": int,
        "blockDeviceMappings": List["InstanceBlockDeviceMappingTypeDef"],
        "cpuOptions": "CpuOptionsTypeDef",
        "createdAt": datetime,
        "imageId": str,
        "instanceId": str,
        "instanceType": str,
        "privateIpAddress": str,
        "publicIpAddress": str,
        "rootDeviceName": str,
        "securityGroups": List["SecurityGroupIdentifierTypeDef"],
        "state": "InstanceStateTypeDef",
        "updatedAt": datetime,
    },
    total=False,
)

_RequiredListDeviceResourcesInputRequestTypeDef = TypedDict(
    "_RequiredListDeviceResourcesInputRequestTypeDef",
    {
        "managedDeviceId": str,
    },
)
_OptionalListDeviceResourcesInputRequestTypeDef = TypedDict(
    "_OptionalListDeviceResourcesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "type": str,
    },
    total=False,
)

class ListDeviceResourcesInputRequestTypeDef(
    _RequiredListDeviceResourcesInputRequestTypeDef, _OptionalListDeviceResourcesInputRequestTypeDef
):
    pass

ListDeviceResourcesOutputTypeDef = TypedDict(
    "ListDeviceResourcesOutputTypeDef",
    {
        "nextToken": str,
        "resources": List["ResourceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevicesInputRequestTypeDef = TypedDict(
    "ListDevicesInputRequestTypeDef",
    {
        "jobId": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListDevicesOutputTypeDef = TypedDict(
    "ListDevicesOutputTypeDef",
    {
        "devices": List["DeviceSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListExecutionsInputRequestTypeDef = TypedDict(
    "_RequiredListExecutionsInputRequestTypeDef",
    {
        "taskId": str,
    },
)
_OptionalListExecutionsInputRequestTypeDef = TypedDict(
    "_OptionalListExecutionsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "state": ExecutionStateType,
    },
    total=False,
)

class ListExecutionsInputRequestTypeDef(
    _RequiredListExecutionsInputRequestTypeDef, _OptionalListExecutionsInputRequestTypeDef
):
    pass

ListExecutionsOutputTypeDef = TypedDict(
    "ListExecutionsOutputTypeDef",
    {
        "executions": List["ExecutionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTasksInputRequestTypeDef = TypedDict(
    "ListTasksInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "state": TaskStateType,
    },
    total=False,
)

ListTasksOutputTypeDef = TypedDict(
    "ListTasksOutputTypeDef",
    {
        "nextToken": str,
        "tasks": List["TaskSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PhysicalNetworkInterfaceTypeDef = TypedDict(
    "PhysicalNetworkInterfaceTypeDef",
    {
        "defaultGateway": str,
        "ipAddress": str,
        "ipAddressAssignment": IpAddressAssignmentType,
        "macAddress": str,
        "netmask": str,
        "physicalConnectorType": PhysicalConnectorTypeType,
        "physicalNetworkInterfaceId": str,
    },
    total=False,
)

_RequiredResourceSummaryTypeDef = TypedDict(
    "_RequiredResourceSummaryTypeDef",
    {
        "resourceType": str,
    },
)
_OptionalResourceSummaryTypeDef = TypedDict(
    "_OptionalResourceSummaryTypeDef",
    {
        "arn": str,
        "id": str,
    },
    total=False,
)

class ResourceSummaryTypeDef(_RequiredResourceSummaryTypeDef, _OptionalResourceSummaryTypeDef):
    pass

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

SecurityGroupIdentifierTypeDef = TypedDict(
    "SecurityGroupIdentifierTypeDef",
    {
        "groupId": str,
        "groupName": str,
    },
    total=False,
)

SoftwareInformationTypeDef = TypedDict(
    "SoftwareInformationTypeDef",
    {
        "installState": str,
        "installedVersion": str,
        "installingVersion": str,
    },
    total=False,
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

_RequiredTaskSummaryTypeDef = TypedDict(
    "_RequiredTaskSummaryTypeDef",
    {
        "taskId": str,
    },
)
_OptionalTaskSummaryTypeDef = TypedDict(
    "_OptionalTaskSummaryTypeDef",
    {
        "state": TaskStateType,
        "tags": Dict[str, str],
        "taskArn": str,
    },
    total=False,
)

class TaskSummaryTypeDef(_RequiredTaskSummaryTypeDef, _OptionalTaskSummaryTypeDef):
    pass

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)
