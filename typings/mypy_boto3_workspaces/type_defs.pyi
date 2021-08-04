"""
Type annotations for workspaces service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/type_defs.html)

Usage::

    ```python
    from mypy_boto3_workspaces.type_defs import AccountModificationTypeDef

    data: AccountModificationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AccessPropertyValueType,
    ApplicationType,
    AssociationStatusType,
    ComputeType,
    ConnectionAliasStateType,
    ConnectionStateType,
    DedicatedTenancyModificationStateEnumType,
    DedicatedTenancySupportResultEnumType,
    ImageTypeType,
    ModificationResourceEnumType,
    ModificationStateEnumType,
    OperatingSystemTypeType,
    ReconnectEnumType,
    RunningModeType,
    TargetWorkspaceStateType,
    TenancyType,
    WorkspaceDirectoryStateType,
    WorkspaceDirectoryTypeType,
    WorkspaceImageIngestionProcessType,
    WorkspaceImageRequiredTenancyType,
    WorkspaceImageStateType,
    WorkspaceStateType,
)

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
    "AssociateConnectionAliasRequestRequestTypeDef",
    "AssociateConnectionAliasResultTypeDef",
    "AssociateIpGroupsRequestRequestTypeDef",
    "AuthorizeIpRulesRequestRequestTypeDef",
    "ClientPropertiesResultTypeDef",
    "ClientPropertiesTypeDef",
    "ComputeTypeTypeDef",
    "ConnectionAliasAssociationTypeDef",
    "ConnectionAliasPermissionTypeDef",
    "ConnectionAliasTypeDef",
    "CopyWorkspaceImageRequestRequestTypeDef",
    "CopyWorkspaceImageResultTypeDef",
    "CreateConnectionAliasRequestRequestTypeDef",
    "CreateConnectionAliasResultTypeDef",
    "CreateIpGroupRequestRequestTypeDef",
    "CreateIpGroupResultTypeDef",
    "CreateTagsRequestRequestTypeDef",
    "CreateWorkspaceBundleRequestRequestTypeDef",
    "CreateWorkspaceBundleResultTypeDef",
    "CreateWorkspacesRequestRequestTypeDef",
    "CreateWorkspacesResultTypeDef",
    "DefaultWorkspaceCreationPropertiesTypeDef",
    "DeleteConnectionAliasRequestRequestTypeDef",
    "DeleteIpGroupRequestRequestTypeDef",
    "DeleteTagsRequestRequestTypeDef",
    "DeleteWorkspaceBundleRequestRequestTypeDef",
    "DeleteWorkspaceImageRequestRequestTypeDef",
    "DeregisterWorkspaceDirectoryRequestRequestTypeDef",
    "DescribeAccountModificationsRequestRequestTypeDef",
    "DescribeAccountModificationsResultTypeDef",
    "DescribeAccountResultTypeDef",
    "DescribeClientPropertiesRequestRequestTypeDef",
    "DescribeClientPropertiesResultTypeDef",
    "DescribeConnectionAliasPermissionsRequestRequestTypeDef",
    "DescribeConnectionAliasPermissionsResultTypeDef",
    "DescribeConnectionAliasesRequestRequestTypeDef",
    "DescribeConnectionAliasesResultTypeDef",
    "DescribeIpGroupsRequestRequestTypeDef",
    "DescribeIpGroupsResultTypeDef",
    "DescribeTagsRequestRequestTypeDef",
    "DescribeTagsResultTypeDef",
    "DescribeWorkspaceBundlesRequestRequestTypeDef",
    "DescribeWorkspaceBundlesResultTypeDef",
    "DescribeWorkspaceDirectoriesRequestRequestTypeDef",
    "DescribeWorkspaceDirectoriesResultTypeDef",
    "DescribeWorkspaceImagePermissionsRequestRequestTypeDef",
    "DescribeWorkspaceImagePermissionsResultTypeDef",
    "DescribeWorkspaceImagesRequestRequestTypeDef",
    "DescribeWorkspaceImagesResultTypeDef",
    "DescribeWorkspaceSnapshotsRequestRequestTypeDef",
    "DescribeWorkspaceSnapshotsResultTypeDef",
    "DescribeWorkspacesConnectionStatusRequestRequestTypeDef",
    "DescribeWorkspacesConnectionStatusResultTypeDef",
    "DescribeWorkspacesRequestRequestTypeDef",
    "DescribeWorkspacesResultTypeDef",
    "DisassociateConnectionAliasRequestRequestTypeDef",
    "DisassociateIpGroupsRequestRequestTypeDef",
    "FailedCreateWorkspaceRequestTypeDef",
    "FailedWorkspaceChangeRequestTypeDef",
    "ImagePermissionTypeDef",
    "ImportWorkspaceImageRequestRequestTypeDef",
    "ImportWorkspaceImageResultTypeDef",
    "IpRuleItemTypeDef",
    "ListAvailableManagementCidrRangesRequestRequestTypeDef",
    "ListAvailableManagementCidrRangesResultTypeDef",
    "MigrateWorkspaceRequestRequestTypeDef",
    "MigrateWorkspaceResultTypeDef",
    "ModificationStateTypeDef",
    "ModifyAccountRequestRequestTypeDef",
    "ModifyClientPropertiesRequestRequestTypeDef",
    "ModifySelfservicePermissionsRequestRequestTypeDef",
    "ModifyWorkspaceAccessPropertiesRequestRequestTypeDef",
    "ModifyWorkspaceCreationPropertiesRequestRequestTypeDef",
    "ModifyWorkspacePropertiesRequestRequestTypeDef",
    "ModifyWorkspaceStateRequestRequestTypeDef",
    "OperatingSystemTypeDef",
    "PaginatorConfigTypeDef",
    "RebootRequestTypeDef",
    "RebootWorkspacesRequestRequestTypeDef",
    "RebootWorkspacesResultTypeDef",
    "RebuildRequestTypeDef",
    "RebuildWorkspacesRequestRequestTypeDef",
    "RebuildWorkspacesResultTypeDef",
    "RegisterWorkspaceDirectoryRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreWorkspaceRequestRequestTypeDef",
    "RevokeIpRulesRequestRequestTypeDef",
    "RootStorageTypeDef",
    "SelfservicePermissionsTypeDef",
    "SnapshotTypeDef",
    "StartRequestTypeDef",
    "StartWorkspacesRequestRequestTypeDef",
    "StartWorkspacesResultTypeDef",
    "StopRequestTypeDef",
    "StopWorkspacesRequestRequestTypeDef",
    "StopWorkspacesResultTypeDef",
    "TagTypeDef",
    "TerminateRequestTypeDef",
    "TerminateWorkspacesRequestRequestTypeDef",
    "TerminateWorkspacesResultTypeDef",
    "UpdateConnectionAliasPermissionRequestRequestTypeDef",
    "UpdateRulesOfIpGroupRequestRequestTypeDef",
    "UpdateWorkspaceBundleRequestRequestTypeDef",
    "UpdateWorkspaceImagePermissionRequestRequestTypeDef",
    "UserStorageTypeDef",
    "WorkspaceAccessPropertiesTypeDef",
    "WorkspaceBundleTypeDef",
    "WorkspaceConnectionStatusTypeDef",
    "WorkspaceCreationPropertiesTypeDef",
    "WorkspaceDirectoryTypeDef",
    "WorkspaceImageTypeDef",
    "WorkspacePropertiesTypeDef",
    "WorkspaceRequestTypeDef",
    "WorkspaceTypeDef",
    "WorkspacesIpGroupTypeDef",
)

AccountModificationTypeDef = TypedDict(
    "AccountModificationTypeDef",
    {
        "ModificationState": DedicatedTenancyModificationStateEnumType,
        "DedicatedTenancySupport": DedicatedTenancySupportResultEnumType,
        "DedicatedTenancyManagementCidrRange": str,
        "StartTime": datetime,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

AssociateConnectionAliasRequestRequestTypeDef = TypedDict(
    "AssociateConnectionAliasRequestRequestTypeDef",
    {
        "AliasId": str,
        "ResourceId": str,
    },
)

AssociateConnectionAliasResultTypeDef = TypedDict(
    "AssociateConnectionAliasResultTypeDef",
    {
        "ConnectionIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateIpGroupsRequestRequestTypeDef = TypedDict(
    "AssociateIpGroupsRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "GroupIds": List[str],
    },
)

AuthorizeIpRulesRequestRequestTypeDef = TypedDict(
    "AuthorizeIpRulesRequestRequestTypeDef",
    {
        "GroupId": str,
        "UserRules": List["IpRuleItemTypeDef"],
    },
)

ClientPropertiesResultTypeDef = TypedDict(
    "ClientPropertiesResultTypeDef",
    {
        "ResourceId": str,
        "ClientProperties": "ClientPropertiesTypeDef",
    },
    total=False,
)

ClientPropertiesTypeDef = TypedDict(
    "ClientPropertiesTypeDef",
    {
        "ReconnectEnabled": ReconnectEnumType,
    },
    total=False,
)

ComputeTypeTypeDef = TypedDict(
    "ComputeTypeTypeDef",
    {
        "Name": ComputeType,
    },
    total=False,
)

ConnectionAliasAssociationTypeDef = TypedDict(
    "ConnectionAliasAssociationTypeDef",
    {
        "AssociationStatus": AssociationStatusType,
        "AssociatedAccountId": str,
        "ResourceId": str,
        "ConnectionIdentifier": str,
    },
    total=False,
)

ConnectionAliasPermissionTypeDef = TypedDict(
    "ConnectionAliasPermissionTypeDef",
    {
        "SharedAccountId": str,
        "AllowAssociation": bool,
    },
)

ConnectionAliasTypeDef = TypedDict(
    "ConnectionAliasTypeDef",
    {
        "ConnectionString": str,
        "AliasId": str,
        "State": ConnectionAliasStateType,
        "OwnerAccountId": str,
        "Associations": List["ConnectionAliasAssociationTypeDef"],
    },
    total=False,
)

_RequiredCopyWorkspaceImageRequestRequestTypeDef = TypedDict(
    "_RequiredCopyWorkspaceImageRequestRequestTypeDef",
    {
        "Name": str,
        "SourceImageId": str,
        "SourceRegion": str,
    },
)
_OptionalCopyWorkspaceImageRequestRequestTypeDef = TypedDict(
    "_OptionalCopyWorkspaceImageRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CopyWorkspaceImageRequestRequestTypeDef(
    _RequiredCopyWorkspaceImageRequestRequestTypeDef,
    _OptionalCopyWorkspaceImageRequestRequestTypeDef,
):
    pass

CopyWorkspaceImageResultTypeDef = TypedDict(
    "CopyWorkspaceImageResultTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConnectionAliasRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConnectionAliasRequestRequestTypeDef",
    {
        "ConnectionString": str,
    },
)
_OptionalCreateConnectionAliasRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConnectionAliasRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateConnectionAliasRequestRequestTypeDef(
    _RequiredCreateConnectionAliasRequestRequestTypeDef,
    _OptionalCreateConnectionAliasRequestRequestTypeDef,
):
    pass

CreateConnectionAliasResultTypeDef = TypedDict(
    "CreateConnectionAliasResultTypeDef",
    {
        "AliasId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIpGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIpGroupRequestRequestTypeDef",
    {
        "GroupName": str,
    },
)
_OptionalCreateIpGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIpGroupRequestRequestTypeDef",
    {
        "GroupDesc": str,
        "UserRules": List["IpRuleItemTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateIpGroupRequestRequestTypeDef(
    _RequiredCreateIpGroupRequestRequestTypeDef, _OptionalCreateIpGroupRequestRequestTypeDef
):
    pass

CreateIpGroupResultTypeDef = TypedDict(
    "CreateIpGroupResultTypeDef",
    {
        "GroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTagsRequestRequestTypeDef = TypedDict(
    "CreateTagsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Tags": List["TagTypeDef"],
    },
)

_RequiredCreateWorkspaceBundleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWorkspaceBundleRequestRequestTypeDef",
    {
        "BundleName": str,
        "BundleDescription": str,
        "ImageId": str,
        "ComputeType": "ComputeTypeTypeDef",
        "UserStorage": "UserStorageTypeDef",
    },
)
_OptionalCreateWorkspaceBundleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWorkspaceBundleRequestRequestTypeDef",
    {
        "RootStorage": "RootStorageTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateWorkspaceBundleRequestRequestTypeDef(
    _RequiredCreateWorkspaceBundleRequestRequestTypeDef,
    _OptionalCreateWorkspaceBundleRequestRequestTypeDef,
):
    pass

CreateWorkspaceBundleResultTypeDef = TypedDict(
    "CreateWorkspaceBundleResultTypeDef",
    {
        "WorkspaceBundle": "WorkspaceBundleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorkspacesRequestRequestTypeDef = TypedDict(
    "CreateWorkspacesRequestRequestTypeDef",
    {
        "Workspaces": List["WorkspaceRequestTypeDef"],
    },
)

CreateWorkspacesResultTypeDef = TypedDict(
    "CreateWorkspacesResultTypeDef",
    {
        "FailedRequests": List["FailedCreateWorkspaceRequestTypeDef"],
        "PendingRequests": List["WorkspaceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

DeleteConnectionAliasRequestRequestTypeDef = TypedDict(
    "DeleteConnectionAliasRequestRequestTypeDef",
    {
        "AliasId": str,
    },
)

DeleteIpGroupRequestRequestTypeDef = TypedDict(
    "DeleteIpGroupRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)

DeleteTagsRequestRequestTypeDef = TypedDict(
    "DeleteTagsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagKeys": List[str],
    },
)

DeleteWorkspaceBundleRequestRequestTypeDef = TypedDict(
    "DeleteWorkspaceBundleRequestRequestTypeDef",
    {
        "BundleId": str,
    },
    total=False,
)

DeleteWorkspaceImageRequestRequestTypeDef = TypedDict(
    "DeleteWorkspaceImageRequestRequestTypeDef",
    {
        "ImageId": str,
    },
)

DeregisterWorkspaceDirectoryRequestRequestTypeDef = TypedDict(
    "DeregisterWorkspaceDirectoryRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)

DescribeAccountModificationsRequestRequestTypeDef = TypedDict(
    "DescribeAccountModificationsRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

DescribeAccountModificationsResultTypeDef = TypedDict(
    "DescribeAccountModificationsResultTypeDef",
    {
        "AccountModifications": List["AccountModificationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountResultTypeDef = TypedDict(
    "DescribeAccountResultTypeDef",
    {
        "DedicatedTenancySupport": DedicatedTenancySupportResultEnumType,
        "DedicatedTenancyManagementCidrRange": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClientPropertiesRequestRequestTypeDef = TypedDict(
    "DescribeClientPropertiesRequestRequestTypeDef",
    {
        "ResourceIds": List[str],
    },
)

DescribeClientPropertiesResultTypeDef = TypedDict(
    "DescribeClientPropertiesResultTypeDef",
    {
        "ClientPropertiesList": List["ClientPropertiesResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeConnectionAliasPermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeConnectionAliasPermissionsRequestRequestTypeDef",
    {
        "AliasId": str,
    },
)
_OptionalDescribeConnectionAliasPermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeConnectionAliasPermissionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeConnectionAliasPermissionsRequestRequestTypeDef(
    _RequiredDescribeConnectionAliasPermissionsRequestRequestTypeDef,
    _OptionalDescribeConnectionAliasPermissionsRequestRequestTypeDef,
):
    pass

DescribeConnectionAliasPermissionsResultTypeDef = TypedDict(
    "DescribeConnectionAliasPermissionsResultTypeDef",
    {
        "AliasId": str,
        "ConnectionAliasPermissions": List["ConnectionAliasPermissionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectionAliasesRequestRequestTypeDef = TypedDict(
    "DescribeConnectionAliasesRequestRequestTypeDef",
    {
        "AliasIds": List[str],
        "ResourceId": str,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeConnectionAliasesResultTypeDef = TypedDict(
    "DescribeConnectionAliasesResultTypeDef",
    {
        "ConnectionAliases": List["ConnectionAliasTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIpGroupsRequestRequestTypeDef = TypedDict(
    "DescribeIpGroupsRequestRequestTypeDef",
    {
        "GroupIds": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeIpGroupsResultTypeDef = TypedDict(
    "DescribeIpGroupsResultTypeDef",
    {
        "Result": List["WorkspacesIpGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagsRequestRequestTypeDef = TypedDict(
    "DescribeTagsRequestRequestTypeDef",
    {
        "ResourceId": str,
    },
)

DescribeTagsResultTypeDef = TypedDict(
    "DescribeTagsResultTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspaceBundlesRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceBundlesRequestRequestTypeDef",
    {
        "BundleIds": List[str],
        "Owner": str,
        "NextToken": str,
    },
    total=False,
)

DescribeWorkspaceBundlesResultTypeDef = TypedDict(
    "DescribeWorkspaceBundlesResultTypeDef",
    {
        "Bundles": List["WorkspaceBundleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspaceDirectoriesRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceDirectoriesRequestRequestTypeDef",
    {
        "DirectoryIds": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeWorkspaceDirectoriesResultTypeDef = TypedDict(
    "DescribeWorkspaceDirectoriesResultTypeDef",
    {
        "Directories": List["WorkspaceDirectoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeWorkspaceImagePermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeWorkspaceImagePermissionsRequestRequestTypeDef",
    {
        "ImageId": str,
    },
)
_OptionalDescribeWorkspaceImagePermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeWorkspaceImagePermissionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeWorkspaceImagePermissionsRequestRequestTypeDef(
    _RequiredDescribeWorkspaceImagePermissionsRequestRequestTypeDef,
    _OptionalDescribeWorkspaceImagePermissionsRequestRequestTypeDef,
):
    pass

DescribeWorkspaceImagePermissionsResultTypeDef = TypedDict(
    "DescribeWorkspaceImagePermissionsResultTypeDef",
    {
        "ImageId": str,
        "ImagePermissions": List["ImagePermissionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspaceImagesRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceImagesRequestRequestTypeDef",
    {
        "ImageIds": List[str],
        "ImageType": ImageTypeType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeWorkspaceImagesResultTypeDef = TypedDict(
    "DescribeWorkspaceImagesResultTypeDef",
    {
        "Images": List["WorkspaceImageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspaceSnapshotsRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceSnapshotsRequestRequestTypeDef",
    {
        "WorkspaceId": str,
    },
)

DescribeWorkspaceSnapshotsResultTypeDef = TypedDict(
    "DescribeWorkspaceSnapshotsResultTypeDef",
    {
        "RebuildSnapshots": List["SnapshotTypeDef"],
        "RestoreSnapshots": List["SnapshotTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspacesConnectionStatusRequestRequestTypeDef = TypedDict(
    "DescribeWorkspacesConnectionStatusRequestRequestTypeDef",
    {
        "WorkspaceIds": List[str],
        "NextToken": str,
    },
    total=False,
)

DescribeWorkspacesConnectionStatusResultTypeDef = TypedDict(
    "DescribeWorkspacesConnectionStatusResultTypeDef",
    {
        "WorkspacesConnectionStatus": List["WorkspaceConnectionStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspacesRequestRequestTypeDef = TypedDict(
    "DescribeWorkspacesRequestRequestTypeDef",
    {
        "WorkspaceIds": List[str],
        "DirectoryId": str,
        "UserName": str,
        "BundleId": str,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeWorkspacesResultTypeDef = TypedDict(
    "DescribeWorkspacesResultTypeDef",
    {
        "Workspaces": List["WorkspaceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateConnectionAliasRequestRequestTypeDef = TypedDict(
    "DisassociateConnectionAliasRequestRequestTypeDef",
    {
        "AliasId": str,
    },
)

DisassociateIpGroupsRequestRequestTypeDef = TypedDict(
    "DisassociateIpGroupsRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "GroupIds": List[str],
    },
)

FailedCreateWorkspaceRequestTypeDef = TypedDict(
    "FailedCreateWorkspaceRequestTypeDef",
    {
        "WorkspaceRequest": "WorkspaceRequestTypeDef",
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

FailedWorkspaceChangeRequestTypeDef = TypedDict(
    "FailedWorkspaceChangeRequestTypeDef",
    {
        "WorkspaceId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

ImagePermissionTypeDef = TypedDict(
    "ImagePermissionTypeDef",
    {
        "SharedAccountId": str,
    },
    total=False,
)

_RequiredImportWorkspaceImageRequestRequestTypeDef = TypedDict(
    "_RequiredImportWorkspaceImageRequestRequestTypeDef",
    {
        "Ec2ImageId": str,
        "IngestionProcess": WorkspaceImageIngestionProcessType,
        "ImageName": str,
        "ImageDescription": str,
    },
)
_OptionalImportWorkspaceImageRequestRequestTypeDef = TypedDict(
    "_OptionalImportWorkspaceImageRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "Applications": List[ApplicationType],
    },
    total=False,
)

class ImportWorkspaceImageRequestRequestTypeDef(
    _RequiredImportWorkspaceImageRequestRequestTypeDef,
    _OptionalImportWorkspaceImageRequestRequestTypeDef,
):
    pass

ImportWorkspaceImageResultTypeDef = TypedDict(
    "ImportWorkspaceImageResultTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IpRuleItemTypeDef = TypedDict(
    "IpRuleItemTypeDef",
    {
        "ipRule": str,
        "ruleDesc": str,
    },
    total=False,
)

_RequiredListAvailableManagementCidrRangesRequestRequestTypeDef = TypedDict(
    "_RequiredListAvailableManagementCidrRangesRequestRequestTypeDef",
    {
        "ManagementCidrRangeConstraint": str,
    },
)
_OptionalListAvailableManagementCidrRangesRequestRequestTypeDef = TypedDict(
    "_OptionalListAvailableManagementCidrRangesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAvailableManagementCidrRangesRequestRequestTypeDef(
    _RequiredListAvailableManagementCidrRangesRequestRequestTypeDef,
    _OptionalListAvailableManagementCidrRangesRequestRequestTypeDef,
):
    pass

ListAvailableManagementCidrRangesResultTypeDef = TypedDict(
    "ListAvailableManagementCidrRangesResultTypeDef",
    {
        "ManagementCidrRanges": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MigrateWorkspaceRequestRequestTypeDef = TypedDict(
    "MigrateWorkspaceRequestRequestTypeDef",
    {
        "SourceWorkspaceId": str,
        "BundleId": str,
    },
)

MigrateWorkspaceResultTypeDef = TypedDict(
    "MigrateWorkspaceResultTypeDef",
    {
        "SourceWorkspaceId": str,
        "TargetWorkspaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModificationStateTypeDef = TypedDict(
    "ModificationStateTypeDef",
    {
        "Resource": ModificationResourceEnumType,
        "State": ModificationStateEnumType,
    },
    total=False,
)

ModifyAccountRequestRequestTypeDef = TypedDict(
    "ModifyAccountRequestRequestTypeDef",
    {
        "DedicatedTenancySupport": Literal["ENABLED"],
        "DedicatedTenancyManagementCidrRange": str,
    },
    total=False,
)

ModifyClientPropertiesRequestRequestTypeDef = TypedDict(
    "ModifyClientPropertiesRequestRequestTypeDef",
    {
        "ResourceId": str,
        "ClientProperties": "ClientPropertiesTypeDef",
    },
)

ModifySelfservicePermissionsRequestRequestTypeDef = TypedDict(
    "ModifySelfservicePermissionsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "SelfservicePermissions": "SelfservicePermissionsTypeDef",
    },
)

ModifyWorkspaceAccessPropertiesRequestRequestTypeDef = TypedDict(
    "ModifyWorkspaceAccessPropertiesRequestRequestTypeDef",
    {
        "ResourceId": str,
        "WorkspaceAccessProperties": "WorkspaceAccessPropertiesTypeDef",
    },
)

ModifyWorkspaceCreationPropertiesRequestRequestTypeDef = TypedDict(
    "ModifyWorkspaceCreationPropertiesRequestRequestTypeDef",
    {
        "ResourceId": str,
        "WorkspaceCreationProperties": "WorkspaceCreationPropertiesTypeDef",
    },
)

ModifyWorkspacePropertiesRequestRequestTypeDef = TypedDict(
    "ModifyWorkspacePropertiesRequestRequestTypeDef",
    {
        "WorkspaceId": str,
        "WorkspaceProperties": "WorkspacePropertiesTypeDef",
    },
)

ModifyWorkspaceStateRequestRequestTypeDef = TypedDict(
    "ModifyWorkspaceStateRequestRequestTypeDef",
    {
        "WorkspaceId": str,
        "WorkspaceState": TargetWorkspaceStateType,
    },
)

OperatingSystemTypeDef = TypedDict(
    "OperatingSystemTypeDef",
    {
        "Type": OperatingSystemTypeType,
    },
    total=False,
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

RebootRequestTypeDef = TypedDict(
    "RebootRequestTypeDef",
    {
        "WorkspaceId": str,
    },
)

RebootWorkspacesRequestRequestTypeDef = TypedDict(
    "RebootWorkspacesRequestRequestTypeDef",
    {
        "RebootWorkspaceRequests": List["RebootRequestTypeDef"],
    },
)

RebootWorkspacesResultTypeDef = TypedDict(
    "RebootWorkspacesResultTypeDef",
    {
        "FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RebuildRequestTypeDef = TypedDict(
    "RebuildRequestTypeDef",
    {
        "WorkspaceId": str,
    },
)

RebuildWorkspacesRequestRequestTypeDef = TypedDict(
    "RebuildWorkspacesRequestRequestTypeDef",
    {
        "RebuildWorkspaceRequests": List["RebuildRequestTypeDef"],
    },
)

RebuildWorkspacesResultTypeDef = TypedDict(
    "RebuildWorkspacesResultTypeDef",
    {
        "FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterWorkspaceDirectoryRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterWorkspaceDirectoryRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "EnableWorkDocs": bool,
    },
)
_OptionalRegisterWorkspaceDirectoryRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterWorkspaceDirectoryRequestRequestTypeDef",
    {
        "SubnetIds": List[str],
        "EnableSelfService": bool,
        "Tenancy": TenancyType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class RegisterWorkspaceDirectoryRequestRequestTypeDef(
    _RequiredRegisterWorkspaceDirectoryRequestRequestTypeDef,
    _OptionalRegisterWorkspaceDirectoryRequestRequestTypeDef,
):
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

RestoreWorkspaceRequestRequestTypeDef = TypedDict(
    "RestoreWorkspaceRequestRequestTypeDef",
    {
        "WorkspaceId": str,
    },
)

RevokeIpRulesRequestRequestTypeDef = TypedDict(
    "RevokeIpRulesRequestRequestTypeDef",
    {
        "GroupId": str,
        "UserRules": List[str],
    },
)

RootStorageTypeDef = TypedDict(
    "RootStorageTypeDef",
    {
        "Capacity": str,
    },
    total=False,
)

SelfservicePermissionsTypeDef = TypedDict(
    "SelfservicePermissionsTypeDef",
    {
        "RestartWorkspace": ReconnectEnumType,
        "IncreaseVolumeSize": ReconnectEnumType,
        "ChangeComputeType": ReconnectEnumType,
        "SwitchRunningMode": ReconnectEnumType,
        "RebuildWorkspace": ReconnectEnumType,
    },
    total=False,
)

SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "SnapshotTime": datetime,
    },
    total=False,
)

StartRequestTypeDef = TypedDict(
    "StartRequestTypeDef",
    {
        "WorkspaceId": str,
    },
    total=False,
)

StartWorkspacesRequestRequestTypeDef = TypedDict(
    "StartWorkspacesRequestRequestTypeDef",
    {
        "StartWorkspaceRequests": List["StartRequestTypeDef"],
    },
)

StartWorkspacesResultTypeDef = TypedDict(
    "StartWorkspacesResultTypeDef",
    {
        "FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopRequestTypeDef = TypedDict(
    "StopRequestTypeDef",
    {
        "WorkspaceId": str,
    },
    total=False,
)

StopWorkspacesRequestRequestTypeDef = TypedDict(
    "StopWorkspacesRequestRequestTypeDef",
    {
        "StopWorkspaceRequests": List["StopRequestTypeDef"],
    },
)

StopWorkspacesResultTypeDef = TypedDict(
    "StopWorkspacesResultTypeDef",
    {
        "FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass

TerminateRequestTypeDef = TypedDict(
    "TerminateRequestTypeDef",
    {
        "WorkspaceId": str,
    },
)

TerminateWorkspacesRequestRequestTypeDef = TypedDict(
    "TerminateWorkspacesRequestRequestTypeDef",
    {
        "TerminateWorkspaceRequests": List["TerminateRequestTypeDef"],
    },
)

TerminateWorkspacesResultTypeDef = TypedDict(
    "TerminateWorkspacesResultTypeDef",
    {
        "FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateConnectionAliasPermissionRequestRequestTypeDef = TypedDict(
    "UpdateConnectionAliasPermissionRequestRequestTypeDef",
    {
        "AliasId": str,
        "ConnectionAliasPermission": "ConnectionAliasPermissionTypeDef",
    },
)

UpdateRulesOfIpGroupRequestRequestTypeDef = TypedDict(
    "UpdateRulesOfIpGroupRequestRequestTypeDef",
    {
        "GroupId": str,
        "UserRules": List["IpRuleItemTypeDef"],
    },
)

UpdateWorkspaceBundleRequestRequestTypeDef = TypedDict(
    "UpdateWorkspaceBundleRequestRequestTypeDef",
    {
        "BundleId": str,
        "ImageId": str,
    },
    total=False,
)

UpdateWorkspaceImagePermissionRequestRequestTypeDef = TypedDict(
    "UpdateWorkspaceImagePermissionRequestRequestTypeDef",
    {
        "ImageId": str,
        "AllowCopyImage": bool,
        "SharedAccountId": str,
    },
)

UserStorageTypeDef = TypedDict(
    "UserStorageTypeDef",
    {
        "Capacity": str,
    },
    total=False,
)

WorkspaceAccessPropertiesTypeDef = TypedDict(
    "WorkspaceAccessPropertiesTypeDef",
    {
        "DeviceTypeWindows": AccessPropertyValueType,
        "DeviceTypeOsx": AccessPropertyValueType,
        "DeviceTypeWeb": AccessPropertyValueType,
        "DeviceTypeIos": AccessPropertyValueType,
        "DeviceTypeAndroid": AccessPropertyValueType,
        "DeviceTypeChromeOs": AccessPropertyValueType,
        "DeviceTypeZeroClient": AccessPropertyValueType,
        "DeviceTypeLinux": AccessPropertyValueType,
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
        "CreationTime": datetime,
    },
    total=False,
)

WorkspaceConnectionStatusTypeDef = TypedDict(
    "WorkspaceConnectionStatusTypeDef",
    {
        "WorkspaceId": str,
        "ConnectionState": ConnectionStateType,
        "ConnectionStateCheckTimestamp": datetime,
        "LastKnownUserConnectionTimestamp": datetime,
    },
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
        "DirectoryType": WorkspaceDirectoryTypeType,
        "WorkspaceSecurityGroupId": str,
        "State": WorkspaceDirectoryStateType,
        "WorkspaceCreationProperties": "DefaultWorkspaceCreationPropertiesTypeDef",
        "ipGroupIds": List[str],
        "WorkspaceAccessProperties": "WorkspaceAccessPropertiesTypeDef",
        "Tenancy": TenancyType,
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
        "State": WorkspaceImageStateType,
        "RequiredTenancy": WorkspaceImageRequiredTenancyType,
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
        "RunningMode": RunningModeType,
        "RunningModeAutoStopTimeoutInMinutes": int,
        "RootVolumeSizeGib": int,
        "UserVolumeSizeGib": int,
        "ComputeTypeName": ComputeType,
    },
    total=False,
)

_RequiredWorkspaceRequestTypeDef = TypedDict(
    "_RequiredWorkspaceRequestTypeDef",
    {
        "DirectoryId": str,
        "UserName": str,
        "BundleId": str,
    },
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
        "State": WorkspaceStateType,
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
    {
        "groupId": str,
        "groupName": str,
        "groupDesc": str,
        "userRules": List["IpRuleItemTypeDef"],
    },
    total=False,
)
