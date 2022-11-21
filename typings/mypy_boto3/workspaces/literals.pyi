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
    "BundleTypeType",
    "CertificateBasedAuthStatusEnumType",
    "ClientDeviceTypeType",
    "ComputeType",
    "ConnectionAliasStateType",
    "ConnectionStateType",
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
    "ImageTypeType",
    "ListAvailableManagementCidrRangesPaginatorName",
    "LogUploadEnumType",
    "ModificationResourceEnumType",
    "ModificationStateEnumType",
    "OperatingSystemTypeType",
    "ProtocolType",
    "ReconnectEnumType",
    "RunningModeType",
    "SamlStatusEnumType",
    "StandbyWorkspaceRelationshipTypeType",
    "TargetWorkspaceStateType",
    "TenancyType",
    "WorkspaceBundleStateType",
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
ImageTypeType = Literal["OWNED", "SHARED"]
ListAvailableManagementCidrRangesPaginatorName = Literal["list_available_management_cidr_ranges"]
LogUploadEnumType = Literal["DISABLED", "ENABLED"]
ModificationResourceEnumType = Literal["COMPUTE_TYPE", "ROOT_VOLUME", "USER_VOLUME"]
ModificationStateEnumType = Literal["UPDATE_INITIATED", "UPDATE_IN_PROGRESS"]
OperatingSystemTypeType = Literal["LINUX", "WINDOWS"]
ProtocolType = Literal["PCOIP", "WSP"]
ReconnectEnumType = Literal["DISABLED", "ENABLED"]
RunningModeType = Literal["ALWAYS_ON", "AUTO_STOP", "MANUAL"]
SamlStatusEnumType = Literal["DISABLED", "ENABLED", "ENABLED_WITH_DIRECTORY_LOGIN_FALLBACK"]
StandbyWorkspaceRelationshipTypeType = Literal["PRIMARY", "STANDBY"]
TargetWorkspaceStateType = Literal["ADMIN_MAINTENANCE", "AVAILABLE"]
TenancyType = Literal["DEDICATED", "SHARED"]
WorkspaceBundleStateType = Literal["AVAILABLE", "ERROR", "PENDING"]
WorkspaceDirectoryStateType = Literal[
    "DEREGISTERED", "DEREGISTERING", "ERROR", "REGISTERED", "REGISTERING"
]
WorkspaceDirectoryTypeType = Literal["AD_CONNECTOR", "SIMPLE_AD"]
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
