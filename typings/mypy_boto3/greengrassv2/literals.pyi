"""
Type annotations for greengrassv2 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/literals.html)

Usage::

    ```python
    from mypy_boto3_greengrassv2.literals import CloudComponentStateType

    data: CloudComponentStateType = "DEPLOYABLE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CloudComponentStateType",
    "ComponentDependencyTypeType",
    "ComponentVisibilityScopeType",
    "CoreDeviceStatusType",
    "DeploymentComponentUpdatePolicyActionType",
    "DeploymentFailureHandlingPolicyType",
    "DeploymentHistoryFilterType",
    "DeploymentStatusType",
    "EffectiveDeploymentExecutionStatusType",
    "InstalledComponentLifecycleStateType",
    "IoTJobAbortActionType",
    "IoTJobExecutionFailureTypeType",
    "LambdaEventSourceTypeType",
    "LambdaFilesystemPermissionType",
    "LambdaInputPayloadEncodingTypeType",
    "LambdaIsolationModeType",
    "ListClientDevicesAssociatedWithCoreDevicePaginatorName",
    "ListComponentVersionsPaginatorName",
    "ListComponentsPaginatorName",
    "ListCoreDevicesPaginatorName",
    "ListDeploymentsPaginatorName",
    "ListEffectiveDeploymentsPaginatorName",
    "ListInstalledComponentsPaginatorName",
    "RecipeOutputFormatType",
)

CloudComponentStateType = Literal["DEPLOYABLE", "DEPRECATED", "FAILED", "INITIATED", "REQUESTED"]
ComponentDependencyTypeType = Literal["HARD", "SOFT"]
ComponentVisibilityScopeType = Literal["PRIVATE", "PUBLIC"]
CoreDeviceStatusType = Literal["HEALTHY", "UNHEALTHY"]
DeploymentComponentUpdatePolicyActionType = Literal["NOTIFY_COMPONENTS", "SKIP_NOTIFY_COMPONENTS"]
DeploymentFailureHandlingPolicyType = Literal["DO_NOTHING", "ROLLBACK"]
DeploymentHistoryFilterType = Literal["ALL", "LATEST_ONLY"]
DeploymentStatusType = Literal["ACTIVE", "CANCELED", "COMPLETED", "FAILED", "INACTIVE"]
EffectiveDeploymentExecutionStatusType = Literal[
    "CANCELED", "COMPLETED", "FAILED", "IN_PROGRESS", "QUEUED", "REJECTED", "TIMED_OUT"
]
InstalledComponentLifecycleStateType = Literal[
    "BROKEN", "ERRORED", "FINISHED", "INSTALLED", "NEW", "RUNNING", "STARTING", "STOPPING"
]
IoTJobAbortActionType = Literal["CANCEL"]
IoTJobExecutionFailureTypeType = Literal["ALL", "FAILED", "REJECTED", "TIMED_OUT"]
LambdaEventSourceTypeType = Literal["IOT_CORE", "PUB_SUB"]
LambdaFilesystemPermissionType = Literal["ro", "rw"]
LambdaInputPayloadEncodingTypeType = Literal["binary", "json"]
LambdaIsolationModeType = Literal["GreengrassContainer", "NoContainer"]
ListClientDevicesAssociatedWithCoreDevicePaginatorName = Literal[
    "list_client_devices_associated_with_core_device"
]
ListComponentVersionsPaginatorName = Literal["list_component_versions"]
ListComponentsPaginatorName = Literal["list_components"]
ListCoreDevicesPaginatorName = Literal["list_core_devices"]
ListDeploymentsPaginatorName = Literal["list_deployments"]
ListEffectiveDeploymentsPaginatorName = Literal["list_effective_deployments"]
ListInstalledComponentsPaginatorName = Literal["list_installed_components"]
RecipeOutputFormatType = Literal["JSON", "YAML"]
