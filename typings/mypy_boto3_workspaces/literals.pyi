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
    "AccountLinkStatusEnumType",
    "ApplicationAssociatedResourceTypeType",
    "ApplicationType",
    "AssociationErrorCodeType",
    "AssociationStateType",
    "AssociationStatusType",
    "BundleAssociatedResourceTypeType",
    "BundleTypeType",
    "CertificateBasedAuthStatusEnumType",
    "ClientDeviceTypeType",
    "ComputeType",
    "ConnectionAliasStateType",
    "ConnectionStateType",
    "DataReplicationType",
    "DedicatedTenancyAccountTypeType",
    "DedicatedTenancyModificationStateEnumType",
    "DedicatedTenancySupportEnumType",
    "DedicatedTenancySupportResultEnumType",
    "DeletableCertificateBasedAuthPropertyType",
    "DeletableSamlPropertyType",
    "DescribeAccountModificationsPaginatorName",
    "DescribeIpGroupsPaginatorName",
    "DescribeWorkspaceBundlesPaginatorName",
    "DescribeWorkspaceDirectoriesPaginatorName",
    "DescribeWorkspaceImagesPaginatorName",
    "DescribeWorkspacesConnectionStatusPaginatorName",
    "DescribeWorkspacesPaginatorName",
    "ImageAssociatedResourceTypeType",
    "ImageTypeType",
    "ListAccountLinksPaginatorName",
    "ListAvailableManagementCidrRangesPaginatorName",
    "LogUploadEnumType",
    "ModificationResourceEnumType",
    "ModificationStateEnumType",
    "OperatingSystemNameType",
    "OperatingSystemTypeType",
    "ProtocolType",
    "ReconnectEnumType",
    "RunningModeType",
    "SamlStatusEnumType",
    "StandbyWorkspaceRelationshipTypeType",
    "TargetWorkspaceStateType",
    "TenancyType",
    "WorkSpaceApplicationLicenseTypeType",
    "WorkSpaceApplicationStateType",
    "WorkSpaceAssociatedResourceTypeType",
    "WorkspaceBundleStateType",
    "WorkspaceDirectoryStateType",
    "WorkspaceDirectoryTypeType",
    "WorkspaceImageErrorDetailCodeType",
    "WorkspaceImageIngestionProcessType",
    "WorkspaceImageRequiredTenancyType",
    "WorkspaceImageStateType",
    "WorkspaceStateType",
)

AccessPropertyValueType = Literal["ALLOW", "DENY"]
AccountLinkStatusEnumType = Literal[
    "LINKED", "LINKING_FAILED", "LINK_NOT_FOUND", "PENDING_ACCEPTANCE_BY_TARGET_ACCOUNT", "REJECTED"
]
ApplicationAssociatedResourceTypeType = Literal["BUNDLE", "IMAGE", "WORKSPACE"]
ApplicationType = Literal["Microsoft_Office_2016", "Microsoft_Office_2019"]
AssociationErrorCodeType = Literal[
    "DeploymentError.InternalServerError",
    "DeploymentError.WorkspaceUnreachable",
    "ValidationError.InsufficientDiskSpace",
    "ValidationError.InsufficientMemory",
    "ValidationError.UnsupportedOperatingSystem",
]
AssociationStateType = Literal[
    "COMPLETED",
    "ERROR",
    "INSTALLING",
    "PENDING_INSTALL",
    "PENDING_INSTALL_DEPLOYMENT",
    "PENDING_UNINSTALL",
    "PENDING_UNINSTALL_DEPLOYMENT",
    "REMOVED",
    "UNINSTALLING",
]
AssociationStatusType = Literal[
    "ASSOCIATED_WITH_OWNER_ACCOUNT",
    "ASSOCIATED_WITH_SHARED_ACCOUNT",
    "NOT_ASSOCIATED",
    "PENDING_ASSOCIATION",
    "PENDING_DISASSOCIATION",
]
BundleAssociatedResourceTypeType = Literal["APPLICATION"]
BundleTypeType = Literal["REGULAR", "STANDBY"]
CertificateBasedAuthStatusEnumType = Literal["DISABLED", "ENABLED"]
ClientDeviceTypeType = Literal[
    "DeviceTypeAndroid",
    "DeviceTypeIos",
    "DeviceTypeLinux",
    "DeviceTypeOsx",
    "DeviceTypeWeb",
    "DeviceTypeWindows",
]
ComputeType = Literal[
    "GRAPHICS",
    "GRAPHICSPRO",
    "GRAPHICSPRO_G4DN",
    "GRAPHICS_G4DN",
    "PERFORMANCE",
    "POWER",
    "POWERPRO",
    "STANDARD",
    "VALUE",
]
ConnectionAliasStateType = Literal["CREATED", "CREATING", "DELETING"]
ConnectionStateType = Literal["CONNECTED", "DISCONNECTED", "UNKNOWN"]
DataReplicationType = Literal["NO_REPLICATION", "PRIMARY_AS_SOURCE"]
DedicatedTenancyAccountTypeType = Literal["SOURCE_ACCOUNT", "TARGET_ACCOUNT"]
DedicatedTenancyModificationStateEnumType = Literal["COMPLETED", "FAILED", "PENDING"]
DedicatedTenancySupportEnumType = Literal["ENABLED"]
DedicatedTenancySupportResultEnumType = Literal["DISABLED", "ENABLED"]
DeletableCertificateBasedAuthPropertyType = Literal[
    "CERTIFICATE_BASED_AUTH_PROPERTIES_CERTIFICATE_AUTHORITY_ARN"
]
DeletableSamlPropertyType = Literal[
    "SAML_PROPERTIES_RELAY_STATE_PARAMETER_NAME", "SAML_PROPERTIES_USER_ACCESS_URL"
]
DescribeAccountModificationsPaginatorName = Literal["describe_account_modifications"]
DescribeIpGroupsPaginatorName = Literal["describe_ip_groups"]
DescribeWorkspaceBundlesPaginatorName = Literal["describe_workspace_bundles"]
DescribeWorkspaceDirectoriesPaginatorName = Literal["describe_workspace_directories"]
DescribeWorkspaceImagesPaginatorName = Literal["describe_workspace_images"]
DescribeWorkspacesConnectionStatusPaginatorName = Literal["describe_workspaces_connection_status"]
DescribeWorkspacesPaginatorName = Literal["describe_workspaces"]
ImageAssociatedResourceTypeType = Literal["APPLICATION"]
ImageTypeType = Literal["OWNED", "SHARED"]
ListAccountLinksPaginatorName = Literal["list_account_links"]
ListAvailableManagementCidrRangesPaginatorName = Literal["list_available_management_cidr_ranges"]
LogUploadEnumType = Literal["DISABLED", "ENABLED"]
ModificationResourceEnumType = Literal["COMPUTE_TYPE", "ROOT_VOLUME", "USER_VOLUME"]
ModificationStateEnumType = Literal["UPDATE_INITIATED", "UPDATE_IN_PROGRESS"]
OperatingSystemNameType = Literal[
    "AMAZON_LINUX_2",
    "UBUNTU_18_04",
    "UBUNTU_20_04",
    "UBUNTU_22_04",
    "UNKNOWN",
    "WINDOWS_10",
    "WINDOWS_11",
    "WINDOWS_7",
    "WINDOWS_SERVER_2016",
    "WINDOWS_SERVER_2019",
    "WINDOWS_SERVER_2022",
]
OperatingSystemTypeType = Literal["LINUX", "WINDOWS"]
ProtocolType = Literal["PCOIP", "WSP"]
ReconnectEnumType = Literal["DISABLED", "ENABLED"]
RunningModeType = Literal["ALWAYS_ON", "AUTO_STOP", "MANUAL"]
SamlStatusEnumType = Literal["DISABLED", "ENABLED", "ENABLED_WITH_DIRECTORY_LOGIN_FALLBACK"]
StandbyWorkspaceRelationshipTypeType = Literal["PRIMARY", "STANDBY"]
TargetWorkspaceStateType = Literal["ADMIN_MAINTENANCE", "AVAILABLE"]
TenancyType = Literal["DEDICATED", "SHARED"]
WorkSpaceApplicationLicenseTypeType = Literal["LICENSED", "UNLICENSED"]
WorkSpaceApplicationStateType = Literal["AVAILABLE", "ERROR", "PENDING", "UNINSTALL_ONLY"]
WorkSpaceAssociatedResourceTypeType = Literal["APPLICATION"]
WorkspaceBundleStateType = Literal["AVAILABLE", "ERROR", "PENDING"]
WorkspaceDirectoryStateType = Literal[
    "DEREGISTERED", "DEREGISTERING", "ERROR", "REGISTERED", "REGISTERING"
]
WorkspaceDirectoryTypeType = Literal["AD_CONNECTOR", "SIMPLE_AD"]
WorkspaceImageErrorDetailCodeType = Literal[
    "AdditionalDrivesAttached",
    "AntiVirusInstalled",
    "AutoLogonEnabled",
    "AutoMountDisabled",
    "AzureDomainJoined",
    "DHCPDisabled",
    "DiskFreeSpace",
    "DiskSizeExceeded",
    "DomainJoined",
    "FirewallEnabled",
    "InPlaceUpgrade",
    "IncompatiblePartitioning",
    "MultipleBootPartition",
    "OSNotSupported",
    "OfficeInstalled",
    "OutdatedPowershellVersion",
    "PCoIPAgentInstalled",
    "PendingReboot",
    "RealTimeUniversalDisabled",
    "Requires64BitOS",
    "UEFINotSupported",
    "VMWareToolsInstalled",
    "WindowsUpdatesEnabled",
    "WorkspacesBYOLAccountDisabled",
    "WorkspacesBYOLAccountNotFound",
    "ZeroRearmCount",
]
WorkspaceImageIngestionProcessType = Literal[
    "BYOL_GRAPHICS",
    "BYOL_GRAPHICSPRO",
    "BYOL_GRAPHICS_G4DN",
    "BYOL_GRAPHICS_G4DN_BYOP",
    "BYOL_REGULAR",
    "BYOL_REGULAR_BYOP",
    "BYOL_REGULAR_WSP",
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
