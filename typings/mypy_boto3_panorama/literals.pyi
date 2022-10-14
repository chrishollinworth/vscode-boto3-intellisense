"""
Type annotations for panorama service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_panorama/literals.html)

Usage::

    ```python
    from mypy_boto3_panorama.literals import ApplicationInstanceHealthStatusType

    data: ApplicationInstanceHealthStatusType = "ERROR"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ApplicationInstanceHealthStatusType",
    "ApplicationInstanceStatusType",
    "ConnectionTypeType",
    "DeviceAggregatedStatusType",
    "DeviceBrandType",
    "DeviceConnectionStatusType",
    "DeviceStatusType",
    "DeviceTypeType",
    "JobResourceTypeType",
    "JobTypeType",
    "ListDevicesSortByType",
    "NetworkConnectionStatusType",
    "NodeCategoryType",
    "NodeFromTemplateJobStatusType",
    "NodeInstanceStatusType",
    "PackageImportJobStatusType",
    "PackageImportJobTypeType",
    "PackageVersionStatusType",
    "PortTypeType",
    "SortOrderType",
    "StatusFilterType",
    "TemplateTypeType",
    "UpdateProgressType",
)

ApplicationInstanceHealthStatusType = Literal["ERROR", "NOT_AVAILABLE", "RUNNING"]
ApplicationInstanceStatusType = Literal[
    "DEPLOYMENT_ERROR",
    "DEPLOYMENT_FAILED",
    "DEPLOYMENT_IN_PROGRESS",
    "DEPLOYMENT_PENDING",
    "DEPLOYMENT_REQUESTED",
    "DEPLOYMENT_SUCCEEDED",
    "REMOVAL_FAILED",
    "REMOVAL_IN_PROGRESS",
    "REMOVAL_PENDING",
    "REMOVAL_REQUESTED",
    "REMOVAL_SUCCEEDED",
]
ConnectionTypeType = Literal["DHCP", "STATIC_IP"]
DeviceAggregatedStatusType = Literal[
    "AWAITING_PROVISIONING",
    "DELETING",
    "ERROR",
    "FAILED",
    "LEASE_EXPIRED",
    "OFFLINE",
    "ONLINE",
    "PENDING",
    "UPDATE_NEEDED",
]
DeviceBrandType = Literal["AWS_PANORAMA", "LENOVO"]
DeviceConnectionStatusType = Literal[
    "AWAITING_CREDENTIALS", "ERROR", "NOT_AVAILABLE", "OFFLINE", "ONLINE"
]
DeviceStatusType = Literal[
    "AWAITING_PROVISIONING", "DELETING", "ERROR", "FAILED", "PENDING", "SUCCEEDED"
]
DeviceTypeType = Literal["PANORAMA_APPLIANCE", "PANORAMA_APPLIANCE_DEVELOPER_KIT"]
JobResourceTypeType = Literal["PACKAGE"]
JobTypeType = Literal["OTA"]
ListDevicesSortByType = Literal["CREATED_TIME", "DEVICE_AGGREGATED_STATUS", "DEVICE_ID", "NAME"]
NetworkConnectionStatusType = Literal["CONNECTED", "CONNECTING", "NOT_CONNECTED"]
NodeCategoryType = Literal["BUSINESS_LOGIC", "MEDIA_SINK", "MEDIA_SOURCE", "ML_MODEL"]
NodeFromTemplateJobStatusType = Literal["FAILED", "PENDING", "SUCCEEDED"]
NodeInstanceStatusType = Literal["ERROR", "NOT_AVAILABLE", "RUNNING"]
PackageImportJobStatusType = Literal["FAILED", "PENDING", "SUCCEEDED"]
PackageImportJobTypeType = Literal["MARKETPLACE_NODE_PACKAGE_VERSION", "NODE_PACKAGE_VERSION"]
PackageVersionStatusType = Literal["DELETING", "FAILED", "REGISTER_COMPLETED", "REGISTER_PENDING"]
PortTypeType = Literal["BOOLEAN", "FLOAT32", "INT32", "MEDIA", "STRING"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
StatusFilterType = Literal[
    "DEPLOYMENT_ERROR",
    "DEPLOYMENT_FAILED",
    "DEPLOYMENT_SUCCEEDED",
    "PROCESSING_DEPLOYMENT",
    "PROCESSING_REMOVAL",
    "REMOVAL_FAILED",
    "REMOVAL_SUCCEEDED",
]
TemplateTypeType = Literal["RTSP_CAMERA_STREAM"]
UpdateProgressType = Literal[
    "COMPLETED", "DOWNLOADING", "FAILED", "IN_PROGRESS", "PENDING", "REBOOTING", "VERIFYING"
]
