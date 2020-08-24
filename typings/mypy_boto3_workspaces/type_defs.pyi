"""
Main interface for workspaces service type definitions.

Usage::

    ```python
    from mypy_boto3_workspaces.type_defs import AccountModificationTypeDef

    data: AccountModificationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountModificationTypeDef",
    "ClientPropertiesResultTypeDef",
    "ClientPropertiesTypeDef",
    "ComputeTypeTypeDef",
    "DefaultWorkspaceCreationPropertiesTypeDef",
    "FailedCreateWorkspaceRequestTypeDef",
    "FailedWorkspaceChangeRequestTypeDef",
    "ImagePermissionTypeDef",
    "IpRuleItemTypeDef",
    "ModificationStateTypeDef",
    "OperatingSystemTypeDef",
    "RootStorageTypeDef",
    "SelfservicePermissionsTypeDef",
    "SnapshotTypeDef",
    "TagTypeDef",
    "UserStorageTypeDef",
    "WorkspaceAccessPropertiesTypeDef",
    "WorkspaceBundleTypeDef",
    "WorkspaceConnectionStatusTypeDef",
    "WorkspaceDirectoryTypeDef",
    "WorkspaceImageTypeDef",
    "WorkspacePropertiesTypeDef",
    "WorkspaceRequestTypeDef",
    "WorkspaceTypeDef",
    "WorkspacesIpGroupTypeDef",
    "CopyWorkspaceImageResultTypeDef",
    "CreateIpGroupResultTypeDef",
    "CreateWorkspacesResultTypeDef",
    "DescribeAccountModificationsResultTypeDef",
    "DescribeAccountResultTypeDef",
    "DescribeClientPropertiesResultTypeDef",
    "DescribeIpGroupsResultTypeDef",
    "DescribeTagsResultTypeDef",
    "DescribeWorkspaceBundlesResultTypeDef",
    "DescribeWorkspaceDirectoriesResultTypeDef",
    "DescribeWorkspaceImagePermissionsResultTypeDef",
    "DescribeWorkspaceImagesResultTypeDef",
    "DescribeWorkspaceSnapshotsResultTypeDef",
    "DescribeWorkspacesConnectionStatusResultTypeDef",
    "DescribeWorkspacesResultTypeDef",
    "ImportWorkspaceImageResultTypeDef",
    "ListAvailableManagementCidrRangesResultTypeDef",
    "MigrateWorkspaceResultTypeDef",
    "PaginatorConfigTypeDef",
    "RebootRequestTypeDef",
    "RebootWorkspacesResultTypeDef",
    "RebuildRequestTypeDef",
    "RebuildWorkspacesResultTypeDef",
    "StartRequestTypeDef",
    "StartWorkspacesResultTypeDef",
    "StopRequestTypeDef",
    "StopWorkspacesResultTypeDef",
    "TerminateRequestTypeDef",
    "TerminateWorkspacesResultTypeDef",
    "WorkspaceCreationPropertiesTypeDef",
)

AccountModificationTypeDef = TypedDict(
    "AccountModificationTypeDef",
    {
        "ModificationState": Literal["PENDING", "COMPLETED", "FAILED"],
        "DedicatedTenancySupport": Literal["ENABLED", "DISABLED"],
        "DedicatedTenancyManagementCidrRange": str,
        "StartTime": datetime,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

ClientPropertiesResultTypeDef = TypedDict(
    "ClientPropertiesResultTypeDef",
    {"ResourceId": str, "ClientProperties": "ClientPropertiesTypeDef"},
    total=False,
)

ClientPropertiesTypeDef = TypedDict(
    "ClientPropertiesTypeDef", {"ReconnectEnabled": Literal["ENABLED", "DISABLED"]}, total=False
)

ComputeTypeTypeDef = TypedDict(
    "ComputeTypeTypeDef",
    {
        "Name": Literal[
            "VALUE", "STANDARD", "PERFORMANCE", "POWER", "GRAPHICS", "POWERPRO", "GRAPHICSPRO"
        ]
    },
    total=False,
)

DefaultWorkspaceCreationPropertiesTypeDef = TypedDict(
    "DefaultWorkspaceCreationPropertiesTypeDef",
    {
        "EnableWorkDocs": bool,
        "EnableInternetAccess": bool,
        "DefaultOu": str,
        "CustomSecurityGroupId": str,
        "UserEnabledAsLocalAdministrator": bool,
        "EnableMaintenanceMode": bool,
    },
    total=False,
)

FailedCreateWorkspaceRequestTypeDef = TypedDict(
    "FailedCreateWorkspaceRequestTypeDef",
    {"WorkspaceRequest": "WorkspaceRequestTypeDef", "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

FailedWorkspaceChangeRequestTypeDef = TypedDict(
    "FailedWorkspaceChangeRequestTypeDef",
    {"WorkspaceId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ImagePermissionTypeDef = TypedDict("ImagePermissionTypeDef", {"SharedAccountId": str}, total=False)

IpRuleItemTypeDef = TypedDict("IpRuleItemTypeDef", {"ipRule": str, "ruleDesc": str}, total=False)

ModificationStateTypeDef = TypedDict(
    "ModificationStateTypeDef",
    {
        "Resource": Literal["ROOT_VOLUME", "USER_VOLUME", "COMPUTE_TYPE"],
        "State": Literal["UPDATE_INITIATED", "UPDATE_IN_PROGRESS"],
    },
    total=False,
)

OperatingSystemTypeDef = TypedDict(
    "OperatingSystemTypeDef", {"Type": Literal["WINDOWS", "LINUX"]}, total=False
)

RootStorageTypeDef = TypedDict("RootStorageTypeDef", {"Capacity": str}, total=False)

SelfservicePermissionsTypeDef = TypedDict(
    "SelfservicePermissionsTypeDef",
    {
        "RestartWorkspace": Literal["ENABLED", "DISABLED"],
        "IncreaseVolumeSize": Literal["ENABLED", "DISABLED"],
        "ChangeComputeType": Literal["ENABLED", "DISABLED"],
        "SwitchRunningMode": Literal["ENABLED", "DISABLED"],
        "RebuildWorkspace": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

SnapshotTypeDef = TypedDict("SnapshotTypeDef", {"SnapshotTime": datetime}, total=False)

_RequiredTagTypeDef = TypedDict("_RequiredTagTypeDef", {"Key": str})
_OptionalTagTypeDef = TypedDict("_OptionalTagTypeDef", {"Value": str}, total=False)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


UserStorageTypeDef = TypedDict("UserStorageTypeDef", {"Capacity": str}, total=False)

WorkspaceAccessPropertiesTypeDef = TypedDict(
    "WorkspaceAccessPropertiesTypeDef",
    {
        "DeviceTypeWindows": Literal["ALLOW", "DENY"],
        "DeviceTypeOsx": Literal["ALLOW", "DENY"],
        "DeviceTypeWeb": Literal["ALLOW", "DENY"],
        "DeviceTypeIos": Literal["ALLOW", "DENY"],
        "DeviceTypeAndroid": Literal["ALLOW", "DENY"],
        "DeviceTypeChromeOs": Literal["ALLOW", "DENY"],
        "DeviceTypeZeroClient": Literal["ALLOW", "DENY"],
    },
    total=False,
)

WorkspaceBundleTypeDef = TypedDict(
    "WorkspaceBundleTypeDef",
    {
        "BundleId": str,
        "Name": str,
        "Owner": str,
        "Description": str,
        "ImageId": str,
        "RootStorage": "RootStorageTypeDef",
        "UserStorage": "UserStorageTypeDef",
        "ComputeType": "ComputeTypeTypeDef",
        "LastUpdatedTime": datetime,
    },
    total=False,
)

WorkspaceConnectionStatusTypeDef = TypedDict(
    "WorkspaceConnectionStatusTypeDef",
    {
        "WorkspaceId": str,
        "ConnectionState": Literal["CONNECTED", "DISCONNECTED", "UNKNOWN"],
        "ConnectionStateCheckTimestamp": datetime,
        "LastKnownUserConnectionTimestamp": datetime,
    },
    total=False,
)

WorkspaceDirectoryTypeDef = TypedDict(
    "WorkspaceDirectoryTypeDef",
    {
        "DirectoryId": str,
        "Alias": str,
        "DirectoryName": str,
        "RegistrationCode": str,
        "SubnetIds": List[str],
        "DnsIpAddresses": List[str],
        "CustomerUserName": str,
        "IamRoleId": str,
        "DirectoryType": Literal["SIMPLE_AD", "AD_CONNECTOR"],
        "WorkspaceSecurityGroupId": str,
        "State": Literal["REGISTERING", "REGISTERED", "DEREGISTERING", "DEREGISTERED", "ERROR"],
        "WorkspaceCreationProperties": "DefaultWorkspaceCreationPropertiesTypeDef",
        "ipGroupIds": List[str],
        "WorkspaceAccessProperties": "WorkspaceAccessPropertiesTypeDef",
        "Tenancy": Literal["DEDICATED", "SHARED"],
        "SelfservicePermissions": "SelfservicePermissionsTypeDef",
    },
    total=False,
)

WorkspaceImageTypeDef = TypedDict(
    "WorkspaceImageTypeDef",
    {
        "ImageId": str,
        "Name": str,
        "Description": str,
        "OperatingSystem": "OperatingSystemTypeDef",
        "State": Literal["AVAILABLE", "PENDING", "ERROR"],
        "RequiredTenancy": Literal["DEFAULT", "DEDICATED"],
        "ErrorCode": str,
        "ErrorMessage": str,
        "Created": datetime,
        "OwnerAccountId": str,
    },
    total=False,
)

WorkspacePropertiesTypeDef = TypedDict(
    "WorkspacePropertiesTypeDef",
    {
        "RunningMode": Literal["AUTO_STOP", "ALWAYS_ON"],
        "RunningModeAutoStopTimeoutInMinutes": int,
        "RootVolumeSizeGib": int,
        "UserVolumeSizeGib": int,
        "ComputeTypeName": Literal[
            "VALUE", "STANDARD", "PERFORMANCE", "POWER", "GRAPHICS", "POWERPRO", "GRAPHICSPRO"
        ],
    },
    total=False,
)

_RequiredWorkspaceRequestTypeDef = TypedDict(
    "_RequiredWorkspaceRequestTypeDef", {"DirectoryId": str, "UserName": str, "BundleId": str}
)
_OptionalWorkspaceRequestTypeDef = TypedDict(
    "_OptionalWorkspaceRequestTypeDef",
    {
        "VolumeEncryptionKey": str,
        "UserVolumeEncryptionEnabled": bool,
        "RootVolumeEncryptionEnabled": bool,
        "WorkspaceProperties": "WorkspacePropertiesTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class WorkspaceRequestTypeDef(_RequiredWorkspaceRequestTypeDef, _OptionalWorkspaceRequestTypeDef):
    pass


WorkspaceTypeDef = TypedDict(
    "WorkspaceTypeDef",
    {
        "WorkspaceId": str,
        "DirectoryId": str,
        "UserName": str,
        "IpAddress": str,
        "State": Literal[
            "PENDING",
            "AVAILABLE",
            "IMPAIRED",
            "UNHEALTHY",
            "REBOOTING",
            "STARTING",
            "REBUILDING",
            "RESTORING",
            "MAINTENANCE",
            "ADMIN_MAINTENANCE",
            "TERMINATING",
            "TERMINATED",
            "SUSPENDED",
            "UPDATING",
            "STOPPING",
            "STOPPED",
            "ERROR",
        ],
        "BundleId": str,
        "SubnetId": str,
        "ErrorMessage": str,
        "ErrorCode": str,
        "ComputerName": str,
        "VolumeEncryptionKey": str,
        "UserVolumeEncryptionEnabled": bool,
        "RootVolumeEncryptionEnabled": bool,
        "WorkspaceProperties": "WorkspacePropertiesTypeDef",
        "ModificationStates": List["ModificationStateTypeDef"],
    },
    total=False,
)

WorkspacesIpGroupTypeDef = TypedDict(
    "WorkspacesIpGroupTypeDef",
    {"groupId": str, "groupName": str, "groupDesc": str, "userRules": List["IpRuleItemTypeDef"]},
    total=False,
)

CopyWorkspaceImageResultTypeDef = TypedDict(
    "CopyWorkspaceImageResultTypeDef", {"ImageId": str}, total=False
)

CreateIpGroupResultTypeDef = TypedDict("CreateIpGroupResultTypeDef", {"GroupId": str}, total=False)

CreateWorkspacesResultTypeDef = TypedDict(
    "CreateWorkspacesResultTypeDef",
    {
        "FailedRequests": List["FailedCreateWorkspaceRequestTypeDef"],
        "PendingRequests": List["WorkspaceTypeDef"],
    },
    total=False,
)

DescribeAccountModificationsResultTypeDef = TypedDict(
    "DescribeAccountModificationsResultTypeDef",
    {"AccountModifications": List["AccountModificationTypeDef"], "NextToken": str},
    total=False,
)

DescribeAccountResultTypeDef = TypedDict(
    "DescribeAccountResultTypeDef",
    {
        "DedicatedTenancySupport": Literal["ENABLED", "DISABLED"],
        "DedicatedTenancyManagementCidrRange": str,
    },
    total=False,
)

DescribeClientPropertiesResultTypeDef = TypedDict(
    "DescribeClientPropertiesResultTypeDef",
    {"ClientPropertiesList": List["ClientPropertiesResultTypeDef"]},
    total=False,
)

DescribeIpGroupsResultTypeDef = TypedDict(
    "DescribeIpGroupsResultTypeDef",
    {"Result": List["WorkspacesIpGroupTypeDef"], "NextToken": str},
    total=False,
)

DescribeTagsResultTypeDef = TypedDict(
    "DescribeTagsResultTypeDef", {"TagList": List["TagTypeDef"]}, total=False
)

DescribeWorkspaceBundlesResultTypeDef = TypedDict(
    "DescribeWorkspaceBundlesResultTypeDef",
    {"Bundles": List["WorkspaceBundleTypeDef"], "NextToken": str},
    total=False,
)

DescribeWorkspaceDirectoriesResultTypeDef = TypedDict(
    "DescribeWorkspaceDirectoriesResultTypeDef",
    {"Directories": List["WorkspaceDirectoryTypeDef"], "NextToken": str},
    total=False,
)

DescribeWorkspaceImagePermissionsResultTypeDef = TypedDict(
    "DescribeWorkspaceImagePermissionsResultTypeDef",
    {"ImageId": str, "ImagePermissions": List["ImagePermissionTypeDef"], "NextToken": str},
    total=False,
)

DescribeWorkspaceImagesResultTypeDef = TypedDict(
    "DescribeWorkspaceImagesResultTypeDef",
    {"Images": List["WorkspaceImageTypeDef"], "NextToken": str},
    total=False,
)

DescribeWorkspaceSnapshotsResultTypeDef = TypedDict(
    "DescribeWorkspaceSnapshotsResultTypeDef",
    {"RebuildSnapshots": List["SnapshotTypeDef"], "RestoreSnapshots": List["SnapshotTypeDef"]},
    total=False,
)

DescribeWorkspacesConnectionStatusResultTypeDef = TypedDict(
    "DescribeWorkspacesConnectionStatusResultTypeDef",
    {"WorkspacesConnectionStatus": List["WorkspaceConnectionStatusTypeDef"], "NextToken": str},
    total=False,
)

DescribeWorkspacesResultTypeDef = TypedDict(
    "DescribeWorkspacesResultTypeDef",
    {"Workspaces": List["WorkspaceTypeDef"], "NextToken": str},
    total=False,
)

ImportWorkspaceImageResultTypeDef = TypedDict(
    "ImportWorkspaceImageResultTypeDef", {"ImageId": str}, total=False
)

ListAvailableManagementCidrRangesResultTypeDef = TypedDict(
    "ListAvailableManagementCidrRangesResultTypeDef",
    {"ManagementCidrRanges": List[str], "NextToken": str},
    total=False,
)

MigrateWorkspaceResultTypeDef = TypedDict(
    "MigrateWorkspaceResultTypeDef",
    {"SourceWorkspaceId": str, "TargetWorkspaceId": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RebootRequestTypeDef = TypedDict("RebootRequestTypeDef", {"WorkspaceId": str})

RebootWorkspacesResultTypeDef = TypedDict(
    "RebootWorkspacesResultTypeDef",
    {"FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"]},
    total=False,
)

RebuildRequestTypeDef = TypedDict("RebuildRequestTypeDef", {"WorkspaceId": str})

RebuildWorkspacesResultTypeDef = TypedDict(
    "RebuildWorkspacesResultTypeDef",
    {"FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"]},
    total=False,
)

StartRequestTypeDef = TypedDict("StartRequestTypeDef", {"WorkspaceId": str}, total=False)

StartWorkspacesResultTypeDef = TypedDict(
    "StartWorkspacesResultTypeDef",
    {"FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"]},
    total=False,
)

StopRequestTypeDef = TypedDict("StopRequestTypeDef", {"WorkspaceId": str}, total=False)

StopWorkspacesResultTypeDef = TypedDict(
    "StopWorkspacesResultTypeDef",
    {"FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"]},
    total=False,
)

TerminateRequestTypeDef = TypedDict("TerminateRequestTypeDef", {"WorkspaceId": str})

TerminateWorkspacesResultTypeDef = TypedDict(
    "TerminateWorkspacesResultTypeDef",
    {"FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"]},
    total=False,
)

WorkspaceCreationPropertiesTypeDef = TypedDict(
    "WorkspaceCreationPropertiesTypeDef",
    {
        "EnableWorkDocs": bool,
        "EnableInternetAccess": bool,
        "DefaultOu": str,
        "CustomSecurityGroupId": str,
        "UserEnabledAsLocalAdministrator": bool,
        "EnableMaintenanceMode": bool,
    },
    total=False,
)
