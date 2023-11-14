"""
Type annotations for ds service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/literals.html)

Usage::

    ```python
    from mypy_boto3_ds.literals import CertificateStateType

    data: CertificateStateType = "Deregistered"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CertificateStateType",
    "CertificateTypeType",
    "ClientAuthenticationStatusType",
    "ClientAuthenticationTypeType",
    "DescribeClientAuthenticationSettingsPaginatorName",
    "DescribeDirectoriesPaginatorName",
    "DescribeDomainControllersPaginatorName",
    "DescribeLDAPSSettingsPaginatorName",
    "DescribeRegionsPaginatorName",
    "DescribeSharedDirectoriesPaginatorName",
    "DescribeSnapshotsPaginatorName",
    "DescribeTrustsPaginatorName",
    "DescribeUpdateDirectoryPaginatorName",
    "DirectoryConfigurationStatusType",
    "DirectoryEditionType",
    "DirectorySizeType",
    "DirectoryStageType",
    "DirectoryTypeType",
    "DomainControllerStatusType",
    "IpRouteStatusMsgType",
    "LDAPSStatusType",
    "LDAPSTypeType",
    "ListCertificatesPaginatorName",
    "ListIpRoutesPaginatorName",
    "ListLogSubscriptionsPaginatorName",
    "ListSchemaExtensionsPaginatorName",
    "ListTagsForResourcePaginatorName",
    "OSVersionType",
    "RadiusAuthenticationProtocolType",
    "RadiusStatusType",
    "RegionTypeType",
    "ReplicationScopeType",
    "SchemaExtensionStatusType",
    "SelectiveAuthType",
    "ShareMethodType",
    "ShareStatusType",
    "SnapshotStatusType",
    "SnapshotTypeType",
    "TargetTypeType",
    "TopicStatusType",
    "TrustDirectionType",
    "TrustStateType",
    "TrustTypeType",
    "UpdateStatusType",
    "UpdateTypeType",
)

CertificateStateType = Literal[
    "DeregisterFailed",
    "Deregistered",
    "Deregistering",
    "RegisterFailed",
    "Registered",
    "Registering",
]
CertificateTypeType = Literal["ClientCertAuth", "ClientLDAPS"]
ClientAuthenticationStatusType = Literal["Disabled", "Enabled"]
ClientAuthenticationTypeType = Literal["SmartCard", "SmartCardOrPassword"]
DescribeClientAuthenticationSettingsPaginatorName = Literal[
    "describe_client_authentication_settings"
]
DescribeDirectoriesPaginatorName = Literal["describe_directories"]
DescribeDomainControllersPaginatorName = Literal["describe_domain_controllers"]
DescribeLDAPSSettingsPaginatorName = Literal["describe_ldaps_settings"]
DescribeRegionsPaginatorName = Literal["describe_regions"]
DescribeSharedDirectoriesPaginatorName = Literal["describe_shared_directories"]
DescribeSnapshotsPaginatorName = Literal["describe_snapshots"]
DescribeTrustsPaginatorName = Literal["describe_trusts"]
DescribeUpdateDirectoryPaginatorName = Literal["describe_update_directory"]
DirectoryConfigurationStatusType = Literal["Default", "Failed", "Requested", "Updated", "Updating"]
DirectoryEditionType = Literal["Enterprise", "Standard"]
DirectorySizeType = Literal["Large", "Small"]
DirectoryStageType = Literal[
    "Active",
    "Created",
    "Creating",
    "Deleted",
    "Deleting",
    "Failed",
    "Impaired",
    "Inoperable",
    "Requested",
    "RestoreFailed",
    "Restoring",
]
DirectoryTypeType = Literal["ADConnector", "MicrosoftAD", "SharedMicrosoftAD", "SimpleAD"]
DomainControllerStatusType = Literal[
    "Active", "Creating", "Deleted", "Deleting", "Failed", "Impaired", "Restoring"
]
IpRouteStatusMsgType = Literal[
    "AddFailed", "Added", "Adding", "RemoveFailed", "Removed", "Removing"
]
LDAPSStatusType = Literal["Disabled", "EnableFailed", "Enabled", "Enabling"]
LDAPSTypeType = Literal["Client"]
ListCertificatesPaginatorName = Literal["list_certificates"]
ListIpRoutesPaginatorName = Literal["list_ip_routes"]
ListLogSubscriptionsPaginatorName = Literal["list_log_subscriptions"]
ListSchemaExtensionsPaginatorName = Literal["list_schema_extensions"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
OSVersionType = Literal["SERVER_2012", "SERVER_2019"]
RadiusAuthenticationProtocolType = Literal["CHAP", "MS-CHAPv1", "MS-CHAPv2", "PAP"]
RadiusStatusType = Literal["Completed", "Creating", "Failed"]
RegionTypeType = Literal["Additional", "Primary"]
ReplicationScopeType = Literal["Domain"]
SchemaExtensionStatusType = Literal[
    "CancelInProgress",
    "Cancelled",
    "Completed",
    "CreatingSnapshot",
    "Failed",
    "Initializing",
    "Replicating",
    "RollbackInProgress",
    "UpdatingSchema",
]
SelectiveAuthType = Literal["Disabled", "Enabled"]
ShareMethodType = Literal["HANDSHAKE", "ORGANIZATIONS"]
ShareStatusType = Literal[
    "Deleted",
    "Deleting",
    "PendingAcceptance",
    "RejectFailed",
    "Rejected",
    "Rejecting",
    "ShareFailed",
    "Shared",
    "Sharing",
]
SnapshotStatusType = Literal["Completed", "Creating", "Failed"]
SnapshotTypeType = Literal["Auto", "Manual"]
TargetTypeType = Literal["ACCOUNT"]
TopicStatusType = Literal["Deleted", "Failed", "Registered", "Topic not found"]
TrustDirectionType = Literal["One-Way: Incoming", "One-Way: Outgoing", "Two-Way"]
TrustStateType = Literal[
    "Created",
    "Creating",
    "Deleted",
    "Deleting",
    "Failed",
    "UpdateFailed",
    "Updated",
    "Updating",
    "Verified",
    "VerifyFailed",
    "Verifying",
]
TrustTypeType = Literal["External", "Forest"]
UpdateStatusType = Literal["UpdateFailed", "Updated", "Updating"]
UpdateTypeType = Literal["OS"]
