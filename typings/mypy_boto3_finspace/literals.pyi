"""
Type annotations for finspace service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace/literals.html)

Usage::

    ```python
    from mypy_boto3_finspace.literals import AutoScalingMetricType

    data: AutoScalingMetricType = "CPU_UTILIZATION_PERCENTAGE"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AutoScalingMetricType",
    "ChangeTypeType",
    "ChangesetStatusType",
    "EnvironmentStatusType",
    "ErrorDetailsType",
    "FederationModeType",
    "IPAddressTypeType",
    "KxAzModeType",
    "KxClusterCodeDeploymentStrategyType",
    "KxClusterStatusType",
    "KxClusterTypeType",
    "KxDataviewStatusType",
    "KxDeploymentStrategyType",
    "KxNAS1TypeType",
    "KxNodeStatusType",
    "KxSavedownStorageTypeType",
    "KxScalingGroupStatusType",
    "KxVolumeStatusType",
    "KxVolumeTypeType",
    "ListKxEnvironmentsPaginatorName",
    "RuleActionType",
    "VolumeTypeType",
    "dnsStatusType",
    "tgwStatusType",
)

AutoScalingMetricType = Literal["CPU_UTILIZATION_PERCENTAGE"]
ChangeTypeType = Literal["DELETE", "PUT"]
ChangesetStatusType = Literal["COMPLETED", "FAILED", "PENDING", "PROCESSING"]
EnvironmentStatusType = Literal[
    "CREATED",
    "CREATE_REQUESTED",
    "CREATING",
    "DELETED",
    "DELETE_REQUESTED",
    "DELETING",
    "FAILED_CREATION",
    "FAILED_DELETION",
    "FAILED_UPDATING_NETWORK",
    "RETRY_DELETION",
    "SUSPENDED",
    "UPDATE_NETWORK_REQUESTED",
    "UPDATING_NETWORK",
]
ErrorDetailsType = Literal[
    "A user recoverable error has occurred",
    "An internal error has occurred.",
    "Cancelled",
    "Missing required permission to perform this request.",
    "One or more inputs to this request were not found.",
    "Service limits have been exceeded.",
    "The inputs to this request are invalid.",
    "The system temporarily lacks sufficient resources to process the request.",
]
FederationModeType = Literal["FEDERATED", "LOCAL"]
IPAddressTypeType = Literal["IP_V4"]
KxAzModeType = Literal["MULTI", "SINGLE"]
KxClusterCodeDeploymentStrategyType = Literal["FORCE", "NO_RESTART", "ROLLING"]
KxClusterStatusType = Literal[
    "CREATE_FAILED",
    "CREATING",
    "DELETED",
    "DELETE_FAILED",
    "DELETING",
    "PENDING",
    "RUNNING",
    "UPDATING",
]
KxClusterTypeType = Literal["GATEWAY", "GP", "HDB", "RDB", "TICKERPLANT"]
KxDataviewStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
KxDeploymentStrategyType = Literal["NO_RESTART", "ROLLING"]
KxNAS1TypeType = Literal["HDD_12", "SSD_1000", "SSD_250"]
KxNodeStatusType = Literal["PROVISIONING", "RUNNING"]
KxSavedownStorageTypeType = Literal["SDS01"]
KxScalingGroupStatusType = Literal[
    "ACTIVE", "CREATE_FAILED", "CREATING", "DELETED", "DELETE_FAILED", "DELETING"
]
KxVolumeStatusType = Literal[
    "ACTIVE",
    "CREATE_FAILED",
    "CREATING",
    "DELETED",
    "DELETE_FAILED",
    "DELETING",
    "UPDATED",
    "UPDATE_FAILED",
    "UPDATING",
]
KxVolumeTypeType = Literal["NAS_1"]
ListKxEnvironmentsPaginatorName = Literal["list_kx_environments"]
RuleActionType = Literal["allow", "deny"]
VolumeTypeType = Literal["NAS_1"]
dnsStatusType = Literal[
    "FAILED_UPDATE", "NONE", "SUCCESSFULLY_UPDATED", "UPDATE_REQUESTED", "UPDATING"
]
tgwStatusType = Literal[
    "FAILED_UPDATE", "NONE", "SUCCESSFULLY_UPDATED", "UPDATE_REQUESTED", "UPDATING"
]
