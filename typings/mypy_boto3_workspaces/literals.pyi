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
    "ApplicationSettingsStatusEnumType",
    "ApplicationType",
    "AssociationErrorCodeType",
    "AssociationStateType",
    "AssociationStatusType",
    "AuthenticationTypeType",
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
    "DescribeWorkspacesPoolsFilterNameType",
    "DescribeWorkspacesPoolsFilterOperatorType",
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
    "SessionConnectionStateType",
    "StandbyWorkspaceRelationshipTypeType",
    "StorageConnectorStatusEnumType",
    "StorageConnectorTypeEnumType",
    "StreamingExperiencePreferredProtocolEnumType",
    "TargetWorkspaceStateType",
    "TenancyType",
    "UserIdentityTypeType",
    "UserSettingActionEnumType",
    "UserSettingPermissionEnumType",
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
    "WorkspaceTypeType",
    "WorkspacesPoolErrorCodeType",
    "WorkspacesPoolStateType",
)

AccessPropertyValueType = Literal["ALLOW", "DENY"]
AccountLinkStatusEnumType = Literal[
    "LINKED", "LINKING_FAILED", "LINK_NOT_FOUND", "PENDING_ACCEPTANCE_BY_TARGET_ACCOUNT", "REJECTED"
]
ApplicationAssociatedResourceTypeType = Literal["BUNDLE", "IMAGE", "WORKSPACE"]
ApplicationSettingsStatusEnumType = Literal["DISABLED", "ENABLED"]
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
AuthenticationTypeType = Literal["SAML"]
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
DescribeWorkspacesPoolsFilterNameType = Literal["PoolName"]
DescribeWorkspacesPoolsFilterOperatorType = Literal[
    "CONTAINS", "EQUALS", "NOTCONTAINS", "NOTEQUALS"
]
ImageAssociatedResourceTypeType = Literal["APPLICATION"]
ImageTypeType = Literal["OWNED", "SHARED"]
ListAccountLinksPaginatorName = Literal["list_account_links"]
ListAvailableManagementCidrRangesPaginatorName = Literal["list_available_management_cidr_ranges"]
LogUploadEnumType = Literal["DISABLED", "ENABLED"]
ModificationResourceEnumType = Literal["COMPUTE_TYPE", "ROOT_VOLUME", "USER_VOLUME"]
ModificationStateEnumType = Literal["UPDATE_INITIATED", "UPDATE_IN_PROGRESS"]
OperatingSystemNameType = Literal[
    "AMAZON_LINUX_2",
    "RHEL_8",
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
SessionConnectionStateType = Literal["CONNECTED", "NOT_CONNECTED"]
StandbyWorkspaceRelationshipTypeType = Literal["PRIMARY", "STANDBY"]
StorageConnectorStatusEnumType = Literal["DISABLED", "ENABLED"]
StorageConnectorTypeEnumType = Literal["HOME_FOLDER"]
StreamingExperiencePreferredProtocolEnumType = Literal["TCP", "UDP"]
TargetWorkspaceStateType = Literal["ADMIN_MAINTENANCE", "AVAILABLE"]
TenancyType = Literal["DEDICATED", "SHARED"]
UserIdentityTypeType = Literal["AWS_DIRECTORY_SERVICE", "CUSTOMER_MANAGED"]
UserSettingActionEnumType = Literal[
    "CLIPBOARD_COPY_FROM_LOCAL_DEVICE",
    "CLIPBOARD_COPY_TO_LOCAL_DEVICE",
    "PRINTING_TO_LOCAL_DEVICE",
    "SMART_CARD",
]
UserSettingPermissionEnumType = Literal["DISABLED", "ENABLED"]
WorkSpaceApplicationLicenseTypeType = Literal["LICENSED", "UNLICENSED"]
WorkSpaceApplicationStateType = Literal["AVAILABLE", "ERROR", "PENDING", "UNINSTALL_ONLY"]
WorkSpaceAssociatedResourceTypeType = Literal["APPLICATION"]
WorkspaceBundleStateType = Literal["AVAILABLE", "ERROR", "PENDING"]
WorkspaceDirectoryStateType = Literal[
    "DEREGISTERED", "DEREGISTERING", "ERROR", "REGISTERED", "REGISTERING"
]
WorkspaceDirectoryTypeType = Literal["AD_CONNECTOR", "CUSTOMER_MANAGED", "SIMPLE_AD"]
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
WorkspaceTypeType = Literal["PERSONAL", "POOLS"]
WorkspacesPoolErrorCodeType = Literal[
    "BUNDLE_NOT_FOUND",
    "DEFAULT_OU_IS_MISSING",
    "DIRECTORY_NOT_FOUND",
    "DOMAIN_JOIN_ERROR_ACCESS_DENIED",
    "DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED",
    "DOMAIN_JOIN_ERROR_FILE_NOT_FOUND",
    "DOMAIN_JOIN_ERROR_INVALID_PARAMETER",
    "DOMAIN_JOIN_ERROR_LOGON_FAILURE",
    "DOMAIN_JOIN_ERROR_MORE_DATA",
    "DOMAIN_JOIN_ERROR_NOT_SUPPORTED",
    "DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN",
    "DOMAIN_JOIN_ERROR_SECRET_ACTION_PERMISSION_IS_MISSING",
    "DOMAIN_JOIN_ERROR_SECRET_DECRYPTION_FAILURE",
    "DOMAIN_JOIN_ERROR_SECRET_INVALID",
    "DOMAIN_JOIN_ERROR_SECRET_NOT_FOUND",
    "DOMAIN_JOIN_ERROR_SECRET_STATE_INVALID",
    "DOMAIN_JOIN_ERROR_SECRET_VALUE_KEY_NOT_FOUND",
    "DOMAIN_JOIN_INTERNAL_SERVICE_ERROR",
    "DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME",
    "DOMAIN_JOIN_NERR_PASSWORD_EXPIRED",
    "DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED",
    "IAM_SERVICE_ROLE_IS_MISSING",
    "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION",
    "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION",
    "IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION",
    "IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION",
    "IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION",
    "IGW_NOT_ATTACHED",
    "IMAGE_NOT_FOUND",
    "INSUFFICIENT_PERMISSIONS_ERROR",
    "INTERNAL_SERVICE_ERROR",
    "INVALID_SUBNET_CONFIGURATION",
    "MACHINE_ROLE_IS_MISSING",
    "NETWORK_INTERFACE_LIMIT_EXCEEDED",
    "SECURITY_GROUPS_NOT_FOUND",
    "STS_DISABLED_IN_REGION",
    "SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES",
    "SUBNET_NOT_FOUND",
    "WORKSPACES_POOL_INSTANCE_PROVISIONING_FAILURE",
    "WORKSPACES_POOL_STOPPED",
]
WorkspacesPoolStateType = Literal[
    "CREATING", "DELETING", "RUNNING", "STARTING", "STOPPED", "STOPPING", "UPDATING"
]
