"""
Type annotations for workspaces service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/literals.html)

Usage::

    ```python
    from mypy_boto3_workspaces.literals import AccessPropertyValueType

    data: AccessPropertyValueType = "ALLOW"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccessPropertyValueType",
    "ApplicationType",
    "AssociationStatusType",
    "ComputeType",
    "ConnectionAliasStateType",
    "ConnectionStateType",
    "DedicatedTenancyModificationStateEnumType",
    "DedicatedTenancySupportEnumType",
    "DedicatedTenancySupportResultEnumType",
    "DescribeAccountModificationsPaginatorName",
    "DescribeIpGroupsPaginatorName",
    "DescribeWorkspaceBundlesPaginatorName",
    "DescribeWorkspaceDirectoriesPaginatorName",
    "DescribeWorkspaceImagesPaginatorName",
    "DescribeWorkspacesConnectionStatusPaginatorName",
    "DescribeWorkspacesPaginatorName",
    "ImageTypeType",
    "ListAvailableManagementCidrRangesPaginatorName",
    "ModificationResourceEnumType",
    "ModificationStateEnumType",
    "OperatingSystemTypeType",
    "ReconnectEnumType",
    "RunningModeType",
    "TargetWorkspaceStateType",
    "TenancyType",
    "WorkspaceDirectoryStateType",
    "WorkspaceDirectoryTypeType",
    "WorkspaceImageIngestionProcessType",
    "WorkspaceImageRequiredTenancyType",
    "WorkspaceImageStateType",
    "WorkspaceStateType",
)

AccessPropertyValueType = Literal["ALLOW", "DENY"]
ApplicationType = Literal["Microsoft_Office_2016", "Microsoft_Office_2019"]
AssociationStatusType = Literal[
    "ASSOCIATED_WITH_OWNER_ACCOUNT",
    "ASSOCIATED_WITH_SHARED_ACCOUNT",
    "NOT_ASSOCIATED",
    "PENDING_ASSOCIATION",
    "PENDING_DISASSOCIATION",
]
ComputeType = Literal[
    "GRAPHICS", "GRAPHICSPRO", "PERFORMANCE", "POWER", "POWERPRO", "STANDARD", "VALUE"
]
ConnectionAliasStateType = Literal["CREATED", "CREATING", "DELETING"]
ConnectionStateType = Literal["CONNECTED", "DISCONNECTED", "UNKNOWN"]
DedicatedTenancyModificationStateEnumType = Literal["COMPLETED", "FAILED", "PENDING"]
DedicatedTenancySupportEnumType = Literal["ENABLED"]
DedicatedTenancySupportResultEnumType = Literal["DISABLED", "ENABLED"]
DescribeAccountModificationsPaginatorName = Literal["describe_account_modifications"]
DescribeIpGroupsPaginatorName = Literal["describe_ip_groups"]
DescribeWorkspaceBundlesPaginatorName = Literal["describe_workspace_bundles"]
DescribeWorkspaceDirectoriesPaginatorName = Literal["describe_workspace_directories"]
DescribeWorkspaceImagesPaginatorName = Literal["describe_workspace_images"]
DescribeWorkspacesConnectionStatusPaginatorName = Literal["describe_workspaces_connection_status"]
DescribeWorkspacesPaginatorName = Literal["describe_workspaces"]
ImageTypeType = Literal["OWNED", "SHARED"]
ListAvailableManagementCidrRangesPaginatorName = Literal["list_available_management_cidr_ranges"]
ModificationResourceEnumType = Literal["COMPUTE_TYPE", "ROOT_VOLUME", "USER_VOLUME"]
ModificationStateEnumType = Literal["UPDATE_INITIATED", "UPDATE_IN_PROGRESS"]
OperatingSystemTypeType = Literal["LINUX", "WINDOWS"]
ReconnectEnumType = Literal["DISABLED", "ENABLED"]
RunningModeType = Literal["ALWAYS_ON", "AUTO_STOP"]
TargetWorkspaceStateType = Literal["ADMIN_MAINTENANCE", "AVAILABLE"]
TenancyType = Literal["DEDICATED", "SHARED"]
WorkspaceDirectoryStateType = Literal[
    "DEREGISTERED", "DEREGISTERING", "ERROR", "REGISTERED", "REGISTERING"
]
WorkspaceDirectoryTypeType = Literal["AD_CONNECTOR", "SIMPLE_AD"]
WorkspaceImageIngestionProcessType = Literal[
    "BYOL_GRAPHICS", "BYOL_GRAPHICSPRO", "BYOL_REGULAR", "BYOL_REGULAR_WSP"
]
WorkspaceImageRequiredTenancyType = Literal["DEDICATED", "DEFAULT"]
WorkspaceImageStateType = Literal["AVAILABLE", "ERROR", "PENDING"]
WorkspaceStateType = Literal[
    "ADMIN_MAINTENANCE",
    "AVAILABLE",
    "ERROR",
    "IMPAIRED",
    "MAINTENANCE",
    "PENDING",
    "REBOOTING",
    "REBUILDING",
    "RESTORING",
    "STARTING",
    "STOPPED",
    "STOPPING",
    "SUSPENDED",
    "TERMINATED",
    "TERMINATING",
    "UNHEALTHY",
    "UPDATING",
]
