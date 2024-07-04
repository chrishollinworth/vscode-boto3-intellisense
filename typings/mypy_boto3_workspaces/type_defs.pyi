"""
Type annotations for workspaces service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/type_defs.html)

Usage::

    ```python
    from mypy_boto3_workspaces.type_defs import AcceptAccountLinkInvitationRequestRequestTypeDef

    data: AcceptAccountLinkInvitationRequestRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AccessPropertyValueType,
    AccountLinkStatusEnumType,
    ApplicationAssociatedResourceTypeType,
    ApplicationSettingsStatusEnumType,
    ApplicationType,
    AssociationErrorCodeType,
    AssociationStateType,
    AssociationStatusType,
    BundleTypeType,
    CertificateBasedAuthStatusEnumType,
    ClientDeviceTypeType,
    ComputeType,
    ConnectionAliasStateType,
    ConnectionStateType,
    DataReplicationType,
    DedicatedTenancyAccountTypeType,
    DedicatedTenancyModificationStateEnumType,
    DedicatedTenancySupportResultEnumType,
    DeletableSamlPropertyType,
    DescribeWorkspacesPoolsFilterOperatorType,
    ImageTypeType,
    LogUploadEnumType,
    ModificationResourceEnumType,
    ModificationStateEnumType,
    OperatingSystemNameType,
    OperatingSystemTypeType,
    ProtocolType,
    ReconnectEnumType,
    RunningModeType,
    SamlStatusEnumType,
    SessionConnectionStateType,
    StandbyWorkspaceRelationshipTypeType,
    StorageConnectorStatusEnumType,
    StreamingExperiencePreferredProtocolEnumType,
    TargetWorkspaceStateType,
    TenancyType,
    UserIdentityTypeType,
    UserSettingActionEnumType,
    UserSettingPermissionEnumType,
    WorkSpaceApplicationLicenseTypeType,
    WorkSpaceApplicationStateType,
    WorkspaceBundleStateType,
    WorkspaceDirectoryStateType,
    WorkspaceDirectoryTypeType,
    WorkspaceImageErrorDetailCodeType,
    WorkspaceImageIngestionProcessType,
    WorkspaceImageRequiredTenancyType,
    WorkspaceImageStateType,
    WorkspacesPoolErrorCodeType,
    WorkspacesPoolStateType,
    WorkspaceStateType,
    WorkspaceTypeType,
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
    "AcceptAccountLinkInvitationRequestRequestTypeDef",
    "AcceptAccountLinkInvitationResultTypeDef",
    "AccountLinkTypeDef",
    "AccountModificationTypeDef",
    "ActiveDirectoryConfigTypeDef",
    "ApplicationResourceAssociationTypeDef",
    "ApplicationSettingsRequestTypeDef",
    "ApplicationSettingsResponseTypeDef",
    "AssociateConnectionAliasRequestRequestTypeDef",
    "AssociateConnectionAliasResultTypeDef",
    "AssociateIpGroupsRequestRequestTypeDef",
    "AssociateWorkspaceApplicationRequestRequestTypeDef",
    "AssociateWorkspaceApplicationResultTypeDef",
    "AssociationStateReasonTypeDef",
    "AuthorizeIpRulesRequestRequestTypeDef",
    "BundleResourceAssociationTypeDef",
    "CapacityStatusTypeDef",
    "CapacityTypeDef",
    "CertificateBasedAuthPropertiesTypeDef",
    "ClientPropertiesResultTypeDef",
    "ClientPropertiesTypeDef",
    "ComputeTypeTypeDef",
    "ConnectClientAddInTypeDef",
    "ConnectionAliasAssociationTypeDef",
    "ConnectionAliasPermissionTypeDef",
    "ConnectionAliasTypeDef",
    "CopyWorkspaceImageRequestRequestTypeDef",
    "CopyWorkspaceImageResultTypeDef",
    "CreateAccountLinkInvitationRequestRequestTypeDef",
    "CreateAccountLinkInvitationResultTypeDef",
    "CreateConnectClientAddInRequestRequestTypeDef",
    "CreateConnectClientAddInResultTypeDef",
    "CreateConnectionAliasRequestRequestTypeDef",
    "CreateConnectionAliasResultTypeDef",
    "CreateIpGroupRequestRequestTypeDef",
    "CreateIpGroupResultTypeDef",
    "CreateStandbyWorkspacesRequestRequestTypeDef",
    "CreateStandbyWorkspacesResultTypeDef",
    "CreateTagsRequestRequestTypeDef",
    "CreateUpdatedWorkspaceImageRequestRequestTypeDef",
    "CreateUpdatedWorkspaceImageResultTypeDef",
    "CreateWorkspaceBundleRequestRequestTypeDef",
    "CreateWorkspaceBundleResultTypeDef",
    "CreateWorkspaceImageRequestRequestTypeDef",
    "CreateWorkspaceImageResultTypeDef",
    "CreateWorkspacesPoolRequestRequestTypeDef",
    "CreateWorkspacesPoolResultTypeDef",
    "CreateWorkspacesRequestRequestTypeDef",
    "CreateWorkspacesResultTypeDef",
    "DataReplicationSettingsTypeDef",
    "DefaultClientBrandingAttributesTypeDef",
    "DefaultImportClientBrandingAttributesTypeDef",
    "DefaultWorkspaceCreationPropertiesTypeDef",
    "DeleteAccountLinkInvitationRequestRequestTypeDef",
    "DeleteAccountLinkInvitationResultTypeDef",
    "DeleteClientBrandingRequestRequestTypeDef",
    "DeleteConnectClientAddInRequestRequestTypeDef",
    "DeleteConnectionAliasRequestRequestTypeDef",
    "DeleteIpGroupRequestRequestTypeDef",
    "DeleteTagsRequestRequestTypeDef",
    "DeleteWorkspaceBundleRequestRequestTypeDef",
    "DeleteWorkspaceImageRequestRequestTypeDef",
    "DeployWorkspaceApplicationsRequestRequestTypeDef",
    "DeployWorkspaceApplicationsResultTypeDef",
    "DeregisterWorkspaceDirectoryRequestRequestTypeDef",
    "DescribeAccountModificationsRequestRequestTypeDef",
    "DescribeAccountModificationsResultTypeDef",
    "DescribeAccountResultTypeDef",
    "DescribeApplicationAssociationsRequestRequestTypeDef",
    "DescribeApplicationAssociationsResultTypeDef",
    "DescribeApplicationsRequestRequestTypeDef",
    "DescribeApplicationsResultTypeDef",
    "DescribeBundleAssociationsRequestRequestTypeDef",
    "DescribeBundleAssociationsResultTypeDef",
    "DescribeClientBrandingRequestRequestTypeDef",
    "DescribeClientBrandingResultTypeDef",
    "DescribeClientPropertiesRequestRequestTypeDef",
    "DescribeClientPropertiesResultTypeDef",
    "DescribeConnectClientAddInsRequestRequestTypeDef",
    "DescribeConnectClientAddInsResultTypeDef",
    "DescribeConnectionAliasPermissionsRequestRequestTypeDef",
    "DescribeConnectionAliasPermissionsResultTypeDef",
    "DescribeConnectionAliasesRequestRequestTypeDef",
    "DescribeConnectionAliasesResultTypeDef",
    "DescribeImageAssociationsRequestRequestTypeDef",
    "DescribeImageAssociationsResultTypeDef",
    "DescribeIpGroupsRequestRequestTypeDef",
    "DescribeIpGroupsResultTypeDef",
    "DescribeTagsRequestRequestTypeDef",
    "DescribeTagsResultTypeDef",
    "DescribeWorkspaceAssociationsRequestRequestTypeDef",
    "DescribeWorkspaceAssociationsResultTypeDef",
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
    "DescribeWorkspacesPoolSessionsRequestRequestTypeDef",
    "DescribeWorkspacesPoolSessionsResultTypeDef",
    "DescribeWorkspacesPoolsFilterTypeDef",
    "DescribeWorkspacesPoolsRequestRequestTypeDef",
    "DescribeWorkspacesPoolsResultTypeDef",
    "DescribeWorkspacesRequestRequestTypeDef",
    "DescribeWorkspacesResultTypeDef",
    "DisassociateConnectionAliasRequestRequestTypeDef",
    "DisassociateIpGroupsRequestRequestTypeDef",
    "DisassociateWorkspaceApplicationRequestRequestTypeDef",
    "DisassociateWorkspaceApplicationResultTypeDef",
    "ErrorDetailsTypeDef",
    "FailedCreateStandbyWorkspacesRequestTypeDef",
    "FailedCreateWorkspaceRequestTypeDef",
    "FailedWorkspaceChangeRequestTypeDef",
    "GetAccountLinkRequestRequestTypeDef",
    "GetAccountLinkResultTypeDef",
    "ImagePermissionTypeDef",
    "ImageResourceAssociationTypeDef",
    "ImportClientBrandingRequestRequestTypeDef",
    "ImportClientBrandingResultTypeDef",
    "ImportWorkspaceImageRequestRequestTypeDef",
    "ImportWorkspaceImageResultTypeDef",
    "IosClientBrandingAttributesTypeDef",
    "IosImportClientBrandingAttributesTypeDef",
    "IpRuleItemTypeDef",
    "ListAccountLinksRequestRequestTypeDef",
    "ListAccountLinksResultTypeDef",
    "ListAvailableManagementCidrRangesRequestRequestTypeDef",
    "ListAvailableManagementCidrRangesResultTypeDef",
    "MigrateWorkspaceRequestRequestTypeDef",
    "MigrateWorkspaceResultTypeDef",
    "ModificationStateTypeDef",
    "ModifyAccountRequestRequestTypeDef",
    "ModifyCertificateBasedAuthPropertiesRequestRequestTypeDef",
    "ModifyClientPropertiesRequestRequestTypeDef",
    "ModifySamlPropertiesRequestRequestTypeDef",
    "ModifySelfservicePermissionsRequestRequestTypeDef",
    "ModifyStreamingPropertiesRequestRequestTypeDef",
    "ModifyWorkspaceAccessPropertiesRequestRequestTypeDef",
    "ModifyWorkspaceCreationPropertiesRequestRequestTypeDef",
    "ModifyWorkspacePropertiesRequestRequestTypeDef",
    "ModifyWorkspaceStateRequestRequestTypeDef",
    "NetworkAccessConfigurationTypeDef",
    "OperatingSystemTypeDef",
    "PaginatorConfigTypeDef",
    "PendingCreateStandbyWorkspacesRequestTypeDef",
    "RebootRequestTypeDef",
    "RebootWorkspacesRequestRequestTypeDef",
    "RebootWorkspacesResultTypeDef",
    "RebuildRequestTypeDef",
    "RebuildWorkspacesRequestRequestTypeDef",
    "RebuildWorkspacesResultTypeDef",
    "RegisterWorkspaceDirectoryRequestRequestTypeDef",
    "RegisterWorkspaceDirectoryResultTypeDef",
    "RejectAccountLinkInvitationRequestRequestTypeDef",
    "RejectAccountLinkInvitationResultTypeDef",
    "RelatedWorkspacePropertiesTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreWorkspaceRequestRequestTypeDef",
    "RevokeIpRulesRequestRequestTypeDef",
    "RootStorageTypeDef",
    "SamlPropertiesTypeDef",
    "SelfservicePermissionsTypeDef",
    "SnapshotTypeDef",
    "StandbyWorkspaceTypeDef",
    "StandbyWorkspacesPropertiesTypeDef",
    "StartRequestTypeDef",
    "StartWorkspacesPoolRequestRequestTypeDef",
    "StartWorkspacesRequestRequestTypeDef",
    "StartWorkspacesResultTypeDef",
    "StopRequestTypeDef",
    "StopWorkspacesPoolRequestRequestTypeDef",
    "StopWorkspacesRequestRequestTypeDef",
    "StopWorkspacesResultTypeDef",
    "StorageConnectorTypeDef",
    "StreamingPropertiesTypeDef",
    "TagTypeDef",
    "TerminateRequestTypeDef",
    "TerminateWorkspacesPoolRequestRequestTypeDef",
    "TerminateWorkspacesPoolSessionRequestRequestTypeDef",
    "TerminateWorkspacesRequestRequestTypeDef",
    "TerminateWorkspacesResultTypeDef",
    "TimeoutSettingsTypeDef",
    "UpdateConnectClientAddInRequestRequestTypeDef",
    "UpdateConnectionAliasPermissionRequestRequestTypeDef",
    "UpdateResultTypeDef",
    "UpdateRulesOfIpGroupRequestRequestTypeDef",
    "UpdateWorkspaceBundleRequestRequestTypeDef",
    "UpdateWorkspaceImagePermissionRequestRequestTypeDef",
    "UpdateWorkspacesPoolRequestRequestTypeDef",
    "UpdateWorkspacesPoolResultTypeDef",
    "UserSettingTypeDef",
    "UserStorageTypeDef",
    "WorkSpaceApplicationDeploymentTypeDef",
    "WorkSpaceApplicationTypeDef",
    "WorkspaceAccessPropertiesTypeDef",
    "WorkspaceBundleTypeDef",
    "WorkspaceConnectionStatusTypeDef",
    "WorkspaceCreationPropertiesTypeDef",
    "WorkspaceDirectoryTypeDef",
    "WorkspaceImageTypeDef",
    "WorkspacePropertiesTypeDef",
    "WorkspaceRequestTypeDef",
    "WorkspaceResourceAssociationTypeDef",
    "WorkspaceTypeDef",
    "WorkspacesIpGroupTypeDef",
    "WorkspacesPoolErrorTypeDef",
    "WorkspacesPoolSessionTypeDef",
    "WorkspacesPoolTypeDef",
)

_RequiredAcceptAccountLinkInvitationRequestRequestTypeDef = TypedDict(
    "_RequiredAcceptAccountLinkInvitationRequestRequestTypeDef",
    {
        "LinkId": str,
    },
)
_OptionalAcceptAccountLinkInvitationRequestRequestTypeDef = TypedDict(
    "_OptionalAcceptAccountLinkInvitationRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class AcceptAccountLinkInvitationRequestRequestTypeDef(
    _RequiredAcceptAccountLinkInvitationRequestRequestTypeDef,
    _OptionalAcceptAccountLinkInvitationRequestRequestTypeDef,
):
    pass

AcceptAccountLinkInvitationResultTypeDef = TypedDict(
    "AcceptAccountLinkInvitationResultTypeDef",
    {
        "AccountLink": "AccountLinkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AccountLinkTypeDef = TypedDict(
    "AccountLinkTypeDef",
    {
        "AccountLinkId": str,
        "AccountLinkStatus": AccountLinkStatusEnumType,
        "SourceAccountId": str,
        "TargetAccountId": str,
    },
    total=False,
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

ActiveDirectoryConfigTypeDef = TypedDict(
    "ActiveDirectoryConfigTypeDef",
    {
        "DomainName": str,
        "ServiceAccountSecretArn": str,
    },
)

ApplicationResourceAssociationTypeDef = TypedDict(
    "ApplicationResourceAssociationTypeDef",
    {
        "ApplicationId": str,
        "AssociatedResourceId": str,
        "AssociatedResourceType": ApplicationAssociatedResourceTypeType,
        "Created": datetime,
        "LastUpdatedTime": datetime,
        "State": AssociationStateType,
        "StateReason": "AssociationStateReasonTypeDef",
    },
    total=False,
)

_RequiredApplicationSettingsRequestTypeDef = TypedDict(
    "_RequiredApplicationSettingsRequestTypeDef",
    {
        "Status": ApplicationSettingsStatusEnumType,
    },
)
_OptionalApplicationSettingsRequestTypeDef = TypedDict(
    "_OptionalApplicationSettingsRequestTypeDef",
    {
        "SettingsGroup": str,
    },
    total=False,
)

class ApplicationSettingsRequestTypeDef(
    _RequiredApplicationSettingsRequestTypeDef, _OptionalApplicationSettingsRequestTypeDef
):
    pass

_RequiredApplicationSettingsResponseTypeDef = TypedDict(
    "_RequiredApplicationSettingsResponseTypeDef",
    {
        "Status": ApplicationSettingsStatusEnumType,
    },
)
_OptionalApplicationSettingsResponseTypeDef = TypedDict(
    "_OptionalApplicationSettingsResponseTypeDef",
    {
        "SettingsGroup": str,
        "S3BucketName": str,
    },
    total=False,
)

class ApplicationSettingsResponseTypeDef(
    _RequiredApplicationSettingsResponseTypeDef, _OptionalApplicationSettingsResponseTypeDef
):
    pass

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

AssociateWorkspaceApplicationRequestRequestTypeDef = TypedDict(
    "AssociateWorkspaceApplicationRequestRequestTypeDef",
    {
        "WorkspaceId": str,
        "ApplicationId": str,
    },
)

AssociateWorkspaceApplicationResultTypeDef = TypedDict(
    "AssociateWorkspaceApplicationResultTypeDef",
    {
        "Association": "WorkspaceResourceAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociationStateReasonTypeDef = TypedDict(
    "AssociationStateReasonTypeDef",
    {
        "ErrorCode": AssociationErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

AuthorizeIpRulesRequestRequestTypeDef = TypedDict(
    "AuthorizeIpRulesRequestRequestTypeDef",
    {
        "GroupId": str,
        "UserRules": List["IpRuleItemTypeDef"],
    },
)

BundleResourceAssociationTypeDef = TypedDict(
    "BundleResourceAssociationTypeDef",
    {
        "AssociatedResourceId": str,
        "AssociatedResourceType": Literal["APPLICATION"],
        "BundleId": str,
        "Created": datetime,
        "LastUpdatedTime": datetime,
        "State": AssociationStateType,
        "StateReason": "AssociationStateReasonTypeDef",
    },
    total=False,
)

CapacityStatusTypeDef = TypedDict(
    "CapacityStatusTypeDef",
    {
        "AvailableUserSessions": int,
        "DesiredUserSessions": int,
        "ActualUserSessions": int,
        "ActiveUserSessions": int,
    },
)

CapacityTypeDef = TypedDict(
    "CapacityTypeDef",
    {
        "DesiredUserSessions": int,
    },
)

CertificateBasedAuthPropertiesTypeDef = TypedDict(
    "CertificateBasedAuthPropertiesTypeDef",
    {
        "Status": CertificateBasedAuthStatusEnumType,
        "CertificateAuthorityArn": str,
    },
    total=False,
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
        "LogUploadEnabled": LogUploadEnumType,
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

ConnectClientAddInTypeDef = TypedDict(
    "ConnectClientAddInTypeDef",
    {
        "AddInId": str,
        "ResourceId": str,
        "Name": str,
        "URL": str,
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

_RequiredCreateAccountLinkInvitationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAccountLinkInvitationRequestRequestTypeDef",
    {
        "TargetAccountId": str,
    },
)
_OptionalCreateAccountLinkInvitationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAccountLinkInvitationRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class CreateAccountLinkInvitationRequestRequestTypeDef(
    _RequiredCreateAccountLinkInvitationRequestRequestTypeDef,
    _OptionalCreateAccountLinkInvitationRequestRequestTypeDef,
):
    pass

CreateAccountLinkInvitationResultTypeDef = TypedDict(
    "CreateAccountLinkInvitationResultTypeDef",
    {
        "AccountLink": "AccountLinkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateConnectClientAddInRequestRequestTypeDef = TypedDict(
    "CreateConnectClientAddInRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Name": str,
        "URL": str,
    },
)

CreateConnectClientAddInResultTypeDef = TypedDict(
    "CreateConnectClientAddInResultTypeDef",
    {
        "AddInId": str,
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

CreateStandbyWorkspacesRequestRequestTypeDef = TypedDict(
    "CreateStandbyWorkspacesRequestRequestTypeDef",
    {
        "PrimaryRegion": str,
        "StandbyWorkspaces": List["StandbyWorkspaceTypeDef"],
    },
)

CreateStandbyWorkspacesResultTypeDef = TypedDict(
    "CreateStandbyWorkspacesResultTypeDef",
    {
        "FailedStandbyRequests": List["FailedCreateStandbyWorkspacesRequestTypeDef"],
        "PendingStandbyRequests": List["PendingCreateStandbyWorkspacesRequestTypeDef"],
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

_RequiredCreateUpdatedWorkspaceImageRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUpdatedWorkspaceImageRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "SourceImageId": str,
    },
)
_OptionalCreateUpdatedWorkspaceImageRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUpdatedWorkspaceImageRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateUpdatedWorkspaceImageRequestRequestTypeDef(
    _RequiredCreateUpdatedWorkspaceImageRequestRequestTypeDef,
    _OptionalCreateUpdatedWorkspaceImageRequestRequestTypeDef,
):
    pass

CreateUpdatedWorkspaceImageResultTypeDef = TypedDict(
    "CreateUpdatedWorkspaceImageResultTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

_RequiredCreateWorkspaceImageRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWorkspaceImageRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "WorkspaceId": str,
    },
)
_OptionalCreateWorkspaceImageRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWorkspaceImageRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateWorkspaceImageRequestRequestTypeDef(
    _RequiredCreateWorkspaceImageRequestRequestTypeDef,
    _OptionalCreateWorkspaceImageRequestRequestTypeDef,
):
    pass

CreateWorkspaceImageResultTypeDef = TypedDict(
    "CreateWorkspaceImageResultTypeDef",
    {
        "ImageId": str,
        "Name": str,
        "Description": str,
        "OperatingSystem": "OperatingSystemTypeDef",
        "State": WorkspaceImageStateType,
        "RequiredTenancy": WorkspaceImageRequiredTenancyType,
        "Created": datetime,
        "OwnerAccountId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWorkspacesPoolRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWorkspacesPoolRequestRequestTypeDef",
    {
        "PoolName": str,
        "Description": str,
        "BundleId": str,
        "DirectoryId": str,
        "Capacity": "CapacityTypeDef",
    },
)
_OptionalCreateWorkspacesPoolRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWorkspacesPoolRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ApplicationSettings": "ApplicationSettingsRequestTypeDef",
        "TimeoutSettings": "TimeoutSettingsTypeDef",
    },
    total=False,
)

class CreateWorkspacesPoolRequestRequestTypeDef(
    _RequiredCreateWorkspacesPoolRequestRequestTypeDef,
    _OptionalCreateWorkspacesPoolRequestRequestTypeDef,
):
    pass

CreateWorkspacesPoolResultTypeDef = TypedDict(
    "CreateWorkspacesPoolResultTypeDef",
    {
        "WorkspacesPool": "WorkspacesPoolTypeDef",
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

DataReplicationSettingsTypeDef = TypedDict(
    "DataReplicationSettingsTypeDef",
    {
        "DataReplication": DataReplicationType,
        "RecoverySnapshotTime": datetime,
    },
    total=False,
)

DefaultClientBrandingAttributesTypeDef = TypedDict(
    "DefaultClientBrandingAttributesTypeDef",
    {
        "LogoUrl": str,
        "SupportEmail": str,
        "SupportLink": str,
        "ForgotPasswordLink": str,
        "LoginMessage": Dict[str, str],
    },
    total=False,
)

DefaultImportClientBrandingAttributesTypeDef = TypedDict(
    "DefaultImportClientBrandingAttributesTypeDef",
    {
        "Logo": Union[bytes, IO[bytes], StreamingBody],
        "SupportEmail": str,
        "SupportLink": str,
        "ForgotPasswordLink": str,
        "LoginMessage": Dict[str, str],
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
        "InstanceIamRoleArn": str,
    },
    total=False,
)

_RequiredDeleteAccountLinkInvitationRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAccountLinkInvitationRequestRequestTypeDef",
    {
        "LinkId": str,
    },
)
_OptionalDeleteAccountLinkInvitationRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAccountLinkInvitationRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class DeleteAccountLinkInvitationRequestRequestTypeDef(
    _RequiredDeleteAccountLinkInvitationRequestRequestTypeDef,
    _OptionalDeleteAccountLinkInvitationRequestRequestTypeDef,
):
    pass

DeleteAccountLinkInvitationResultTypeDef = TypedDict(
    "DeleteAccountLinkInvitationResultTypeDef",
    {
        "AccountLink": "AccountLinkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClientBrandingRequestRequestTypeDef = TypedDict(
    "DeleteClientBrandingRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Platforms": List[ClientDeviceTypeType],
    },
)

DeleteConnectClientAddInRequestRequestTypeDef = TypedDict(
    "DeleteConnectClientAddInRequestRequestTypeDef",
    {
        "AddInId": str,
        "ResourceId": str,
    },
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

_RequiredDeployWorkspaceApplicationsRequestRequestTypeDef = TypedDict(
    "_RequiredDeployWorkspaceApplicationsRequestRequestTypeDef",
    {
        "WorkspaceId": str,
    },
)
_OptionalDeployWorkspaceApplicationsRequestRequestTypeDef = TypedDict(
    "_OptionalDeployWorkspaceApplicationsRequestRequestTypeDef",
    {
        "Force": bool,
    },
    total=False,
)

class DeployWorkspaceApplicationsRequestRequestTypeDef(
    _RequiredDeployWorkspaceApplicationsRequestRequestTypeDef,
    _OptionalDeployWorkspaceApplicationsRequestRequestTypeDef,
):
    pass

DeployWorkspaceApplicationsResultTypeDef = TypedDict(
    "DeployWorkspaceApplicationsResultTypeDef",
    {
        "Deployment": "WorkSpaceApplicationDeploymentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
        "DedicatedTenancyAccountType": DedicatedTenancyAccountTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeApplicationAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeApplicationAssociationsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "AssociatedResourceTypes": List[ApplicationAssociatedResourceTypeType],
    },
)
_OptionalDescribeApplicationAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeApplicationAssociationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeApplicationAssociationsRequestRequestTypeDef(
    _RequiredDescribeApplicationAssociationsRequestRequestTypeDef,
    _OptionalDescribeApplicationAssociationsRequestRequestTypeDef,
):
    pass

DescribeApplicationAssociationsResultTypeDef = TypedDict(
    "DescribeApplicationAssociationsResultTypeDef",
    {
        "Associations": List["ApplicationResourceAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeApplicationsRequestRequestTypeDef = TypedDict(
    "DescribeApplicationsRequestRequestTypeDef",
    {
        "ApplicationIds": List[str],
        "ComputeTypeNames": List[ComputeType],
        "LicenseType": WorkSpaceApplicationLicenseTypeType,
        "OperatingSystemNames": List[OperatingSystemNameType],
        "Owner": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeApplicationsResultTypeDef = TypedDict(
    "DescribeApplicationsResultTypeDef",
    {
        "Applications": List["WorkSpaceApplicationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBundleAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeBundleAssociationsRequestRequestTypeDef",
    {
        "BundleId": str,
        "AssociatedResourceTypes": List[Literal["APPLICATION"]],
    },
)

DescribeBundleAssociationsResultTypeDef = TypedDict(
    "DescribeBundleAssociationsResultTypeDef",
    {
        "Associations": List["BundleResourceAssociationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClientBrandingRequestRequestTypeDef = TypedDict(
    "DescribeClientBrandingRequestRequestTypeDef",
    {
        "ResourceId": str,
    },
)

DescribeClientBrandingResultTypeDef = TypedDict(
    "DescribeClientBrandingResultTypeDef",
    {
        "DeviceTypeWindows": "DefaultClientBrandingAttributesTypeDef",
        "DeviceTypeOsx": "DefaultClientBrandingAttributesTypeDef",
        "DeviceTypeAndroid": "DefaultClientBrandingAttributesTypeDef",
        "DeviceTypeIos": "IosClientBrandingAttributesTypeDef",
        "DeviceTypeLinux": "DefaultClientBrandingAttributesTypeDef",
        "DeviceTypeWeb": "DefaultClientBrandingAttributesTypeDef",
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

_RequiredDescribeConnectClientAddInsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeConnectClientAddInsRequestRequestTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalDescribeConnectClientAddInsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeConnectClientAddInsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeConnectClientAddInsRequestRequestTypeDef(
    _RequiredDescribeConnectClientAddInsRequestRequestTypeDef,
    _OptionalDescribeConnectClientAddInsRequestRequestTypeDef,
):
    pass

DescribeConnectClientAddInsResultTypeDef = TypedDict(
    "DescribeConnectClientAddInsResultTypeDef",
    {
        "AddIns": List["ConnectClientAddInTypeDef"],
        "NextToken": str,
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

DescribeImageAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeImageAssociationsRequestRequestTypeDef",
    {
        "ImageId": str,
        "AssociatedResourceTypes": List[Literal["APPLICATION"]],
    },
)

DescribeImageAssociationsResultTypeDef = TypedDict(
    "DescribeImageAssociationsResultTypeDef",
    {
        "Associations": List["ImageResourceAssociationTypeDef"],
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

DescribeWorkspaceAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceAssociationsRequestRequestTypeDef",
    {
        "WorkspaceId": str,
        "AssociatedResourceTypes": List[Literal["APPLICATION"]],
    },
)

DescribeWorkspaceAssociationsResultTypeDef = TypedDict(
    "DescribeWorkspaceAssociationsResultTypeDef",
    {
        "Associations": List["WorkspaceResourceAssociationTypeDef"],
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
        "WorkspaceDirectoryNames": List[str],
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

_RequiredDescribeWorkspacesPoolSessionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeWorkspacesPoolSessionsRequestRequestTypeDef",
    {
        "PoolId": str,
    },
)
_OptionalDescribeWorkspacesPoolSessionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeWorkspacesPoolSessionsRequestRequestTypeDef",
    {
        "UserId": str,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeWorkspacesPoolSessionsRequestRequestTypeDef(
    _RequiredDescribeWorkspacesPoolSessionsRequestRequestTypeDef,
    _OptionalDescribeWorkspacesPoolSessionsRequestRequestTypeDef,
):
    pass

DescribeWorkspacesPoolSessionsResultTypeDef = TypedDict(
    "DescribeWorkspacesPoolSessionsResultTypeDef",
    {
        "Sessions": List["WorkspacesPoolSessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspacesPoolsFilterTypeDef = TypedDict(
    "DescribeWorkspacesPoolsFilterTypeDef",
    {
        "Name": Literal["PoolName"],
        "Values": List[str],
        "Operator": DescribeWorkspacesPoolsFilterOperatorType,
    },
)

DescribeWorkspacesPoolsRequestRequestTypeDef = TypedDict(
    "DescribeWorkspacesPoolsRequestRequestTypeDef",
    {
        "PoolIds": List[str],
        "Filters": List["DescribeWorkspacesPoolsFilterTypeDef"],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeWorkspacesPoolsResultTypeDef = TypedDict(
    "DescribeWorkspacesPoolsResultTypeDef",
    {
        "WorkspacesPools": List["WorkspacesPoolTypeDef"],
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
        "WorkspaceName": str,
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

DisassociateWorkspaceApplicationRequestRequestTypeDef = TypedDict(
    "DisassociateWorkspaceApplicationRequestRequestTypeDef",
    {
        "WorkspaceId": str,
        "ApplicationId": str,
    },
)

DisassociateWorkspaceApplicationResultTypeDef = TypedDict(
    "DisassociateWorkspaceApplicationResultTypeDef",
    {
        "Association": "WorkspaceResourceAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "ErrorCode": WorkspaceImageErrorDetailCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

FailedCreateStandbyWorkspacesRequestTypeDef = TypedDict(
    "FailedCreateStandbyWorkspacesRequestTypeDef",
    {
        "StandbyWorkspaceRequest": "StandbyWorkspaceTypeDef",
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
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

GetAccountLinkRequestRequestTypeDef = TypedDict(
    "GetAccountLinkRequestRequestTypeDef",
    {
        "LinkId": str,
        "LinkedAccountId": str,
    },
    total=False,
)

GetAccountLinkResultTypeDef = TypedDict(
    "GetAccountLinkResultTypeDef",
    {
        "AccountLink": "AccountLinkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImagePermissionTypeDef = TypedDict(
    "ImagePermissionTypeDef",
    {
        "SharedAccountId": str,
    },
    total=False,
)

ImageResourceAssociationTypeDef = TypedDict(
    "ImageResourceAssociationTypeDef",
    {
        "AssociatedResourceId": str,
        "AssociatedResourceType": Literal["APPLICATION"],
        "Created": datetime,
        "LastUpdatedTime": datetime,
        "ImageId": str,
        "State": AssociationStateType,
        "StateReason": "AssociationStateReasonTypeDef",
    },
    total=False,
)

_RequiredImportClientBrandingRequestRequestTypeDef = TypedDict(
    "_RequiredImportClientBrandingRequestRequestTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalImportClientBrandingRequestRequestTypeDef = TypedDict(
    "_OptionalImportClientBrandingRequestRequestTypeDef",
    {
        "DeviceTypeWindows": "DefaultImportClientBrandingAttributesTypeDef",
        "DeviceTypeOsx": "DefaultImportClientBrandingAttributesTypeDef",
        "DeviceTypeAndroid": "DefaultImportClientBrandingAttributesTypeDef",
        "DeviceTypeIos": "IosImportClientBrandingAttributesTypeDef",
        "DeviceTypeLinux": "DefaultImportClientBrandingAttributesTypeDef",
        "DeviceTypeWeb": "DefaultImportClientBrandingAttributesTypeDef",
    },
    total=False,
)

class ImportClientBrandingRequestRequestTypeDef(
    _RequiredImportClientBrandingRequestRequestTypeDef,
    _OptionalImportClientBrandingRequestRequestTypeDef,
):
    pass

ImportClientBrandingResultTypeDef = TypedDict(
    "ImportClientBrandingResultTypeDef",
    {
        "DeviceTypeWindows": "DefaultClientBrandingAttributesTypeDef",
        "DeviceTypeOsx": "DefaultClientBrandingAttributesTypeDef",
        "DeviceTypeAndroid": "DefaultClientBrandingAttributesTypeDef",
        "DeviceTypeIos": "IosClientBrandingAttributesTypeDef",
        "DeviceTypeLinux": "DefaultClientBrandingAttributesTypeDef",
        "DeviceTypeWeb": "DefaultClientBrandingAttributesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

IosClientBrandingAttributesTypeDef = TypedDict(
    "IosClientBrandingAttributesTypeDef",
    {
        "LogoUrl": str,
        "Logo2xUrl": str,
        "Logo3xUrl": str,
        "SupportEmail": str,
        "SupportLink": str,
        "ForgotPasswordLink": str,
        "LoginMessage": Dict[str, str],
    },
    total=False,
)

IosImportClientBrandingAttributesTypeDef = TypedDict(
    "IosImportClientBrandingAttributesTypeDef",
    {
        "Logo": Union[bytes, IO[bytes], StreamingBody],
        "Logo2x": Union[bytes, IO[bytes], StreamingBody],
        "Logo3x": Union[bytes, IO[bytes], StreamingBody],
        "SupportEmail": str,
        "SupportLink": str,
        "ForgotPasswordLink": str,
        "LoginMessage": Dict[str, str],
    },
    total=False,
)

IpRuleItemTypeDef = TypedDict(
    "IpRuleItemTypeDef",
    {
        "ipRule": str,
        "ruleDesc": str,
    },
    total=False,
)

ListAccountLinksRequestRequestTypeDef = TypedDict(
    "ListAccountLinksRequestRequestTypeDef",
    {
        "LinkStatusFilter": List[AccountLinkStatusEnumType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListAccountLinksResultTypeDef = TypedDict(
    "ListAccountLinksResultTypeDef",
    {
        "AccountLinks": List["AccountLinkTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredModifyCertificateBasedAuthPropertiesRequestRequestTypeDef = TypedDict(
    "_RequiredModifyCertificateBasedAuthPropertiesRequestRequestTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalModifyCertificateBasedAuthPropertiesRequestRequestTypeDef = TypedDict(
    "_OptionalModifyCertificateBasedAuthPropertiesRequestRequestTypeDef",
    {
        "CertificateBasedAuthProperties": "CertificateBasedAuthPropertiesTypeDef",
        "PropertiesToDelete": List[
            Literal["CERTIFICATE_BASED_AUTH_PROPERTIES_CERTIFICATE_AUTHORITY_ARN"]
        ],
    },
    total=False,
)

class ModifyCertificateBasedAuthPropertiesRequestRequestTypeDef(
    _RequiredModifyCertificateBasedAuthPropertiesRequestRequestTypeDef,
    _OptionalModifyCertificateBasedAuthPropertiesRequestRequestTypeDef,
):
    pass

ModifyClientPropertiesRequestRequestTypeDef = TypedDict(
    "ModifyClientPropertiesRequestRequestTypeDef",
    {
        "ResourceId": str,
        "ClientProperties": "ClientPropertiesTypeDef",
    },
)

_RequiredModifySamlPropertiesRequestRequestTypeDef = TypedDict(
    "_RequiredModifySamlPropertiesRequestRequestTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalModifySamlPropertiesRequestRequestTypeDef = TypedDict(
    "_OptionalModifySamlPropertiesRequestRequestTypeDef",
    {
        "SamlProperties": "SamlPropertiesTypeDef",
        "PropertiesToDelete": List[DeletableSamlPropertyType],
    },
    total=False,
)

class ModifySamlPropertiesRequestRequestTypeDef(
    _RequiredModifySamlPropertiesRequestRequestTypeDef,
    _OptionalModifySamlPropertiesRequestRequestTypeDef,
):
    pass

ModifySelfservicePermissionsRequestRequestTypeDef = TypedDict(
    "ModifySelfservicePermissionsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "SelfservicePermissions": "SelfservicePermissionsTypeDef",
    },
)

_RequiredModifyStreamingPropertiesRequestRequestTypeDef = TypedDict(
    "_RequiredModifyStreamingPropertiesRequestRequestTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalModifyStreamingPropertiesRequestRequestTypeDef = TypedDict(
    "_OptionalModifyStreamingPropertiesRequestRequestTypeDef",
    {
        "StreamingProperties": "StreamingPropertiesTypeDef",
    },
    total=False,
)

class ModifyStreamingPropertiesRequestRequestTypeDef(
    _RequiredModifyStreamingPropertiesRequestRequestTypeDef,
    _OptionalModifyStreamingPropertiesRequestRequestTypeDef,
):
    pass

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

_RequiredModifyWorkspacePropertiesRequestRequestTypeDef = TypedDict(
    "_RequiredModifyWorkspacePropertiesRequestRequestTypeDef",
    {
        "WorkspaceId": str,
    },
)
_OptionalModifyWorkspacePropertiesRequestRequestTypeDef = TypedDict(
    "_OptionalModifyWorkspacePropertiesRequestRequestTypeDef",
    {
        "WorkspaceProperties": "WorkspacePropertiesTypeDef",
        "DataReplication": DataReplicationType,
    },
    total=False,
)

class ModifyWorkspacePropertiesRequestRequestTypeDef(
    _RequiredModifyWorkspacePropertiesRequestRequestTypeDef,
    _OptionalModifyWorkspacePropertiesRequestRequestTypeDef,
):
    pass

ModifyWorkspaceStateRequestRequestTypeDef = TypedDict(
    "ModifyWorkspaceStateRequestRequestTypeDef",
    {
        "WorkspaceId": str,
        "WorkspaceState": TargetWorkspaceStateType,
    },
)

NetworkAccessConfigurationTypeDef = TypedDict(
    "NetworkAccessConfigurationTypeDef",
    {
        "EniPrivateIpAddress": str,
        "EniId": str,
    },
    total=False,
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

PendingCreateStandbyWorkspacesRequestTypeDef = TypedDict(
    "PendingCreateStandbyWorkspacesRequestTypeDef",
    {
        "UserName": str,
        "DirectoryId": str,
        "State": WorkspaceStateType,
        "WorkspaceId": str,
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

RegisterWorkspaceDirectoryRequestRequestTypeDef = TypedDict(
    "RegisterWorkspaceDirectoryRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "SubnetIds": List[str],
        "EnableWorkDocs": bool,
        "EnableSelfService": bool,
        "Tenancy": TenancyType,
        "Tags": List["TagTypeDef"],
        "WorkspaceDirectoryName": str,
        "WorkspaceDirectoryDescription": str,
        "UserIdentityType": UserIdentityTypeType,
        "WorkspaceType": WorkspaceTypeType,
        "ActiveDirectoryConfig": "ActiveDirectoryConfigTypeDef",
    },
    total=False,
)

RegisterWorkspaceDirectoryResultTypeDef = TypedDict(
    "RegisterWorkspaceDirectoryResultTypeDef",
    {
        "DirectoryId": str,
        "State": WorkspaceDirectoryStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRejectAccountLinkInvitationRequestRequestTypeDef = TypedDict(
    "_RequiredRejectAccountLinkInvitationRequestRequestTypeDef",
    {
        "LinkId": str,
    },
)
_OptionalRejectAccountLinkInvitationRequestRequestTypeDef = TypedDict(
    "_OptionalRejectAccountLinkInvitationRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class RejectAccountLinkInvitationRequestRequestTypeDef(
    _RequiredRejectAccountLinkInvitationRequestRequestTypeDef,
    _OptionalRejectAccountLinkInvitationRequestRequestTypeDef,
):
    pass

RejectAccountLinkInvitationResultTypeDef = TypedDict(
    "RejectAccountLinkInvitationResultTypeDef",
    {
        "AccountLink": "AccountLinkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RelatedWorkspacePropertiesTypeDef = TypedDict(
    "RelatedWorkspacePropertiesTypeDef",
    {
        "WorkspaceId": str,
        "Region": str,
        "State": WorkspaceStateType,
        "Type": StandbyWorkspaceRelationshipTypeType,
    },
    total=False,
)

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

SamlPropertiesTypeDef = TypedDict(
    "SamlPropertiesTypeDef",
    {
        "Status": SamlStatusEnumType,
        "UserAccessUrl": str,
        "RelayStateParameterName": str,
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

_RequiredStandbyWorkspaceTypeDef = TypedDict(
    "_RequiredStandbyWorkspaceTypeDef",
    {
        "PrimaryWorkspaceId": str,
        "DirectoryId": str,
    },
)
_OptionalStandbyWorkspaceTypeDef = TypedDict(
    "_OptionalStandbyWorkspaceTypeDef",
    {
        "VolumeEncryptionKey": str,
        "Tags": List["TagTypeDef"],
        "DataReplication": DataReplicationType,
    },
    total=False,
)

class StandbyWorkspaceTypeDef(_RequiredStandbyWorkspaceTypeDef, _OptionalStandbyWorkspaceTypeDef):
    pass

StandbyWorkspacesPropertiesTypeDef = TypedDict(
    "StandbyWorkspacesPropertiesTypeDef",
    {
        "StandbyWorkspaceId": str,
        "DataReplication": DataReplicationType,
        "RecoverySnapshotTime": datetime,
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

StartWorkspacesPoolRequestRequestTypeDef = TypedDict(
    "StartWorkspacesPoolRequestRequestTypeDef",
    {
        "PoolId": str,
    },
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

StopWorkspacesPoolRequestRequestTypeDef = TypedDict(
    "StopWorkspacesPoolRequestRequestTypeDef",
    {
        "PoolId": str,
    },
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

StorageConnectorTypeDef = TypedDict(
    "StorageConnectorTypeDef",
    {
        "ConnectorType": Literal["HOME_FOLDER"],
        "Status": StorageConnectorStatusEnumType,
    },
)

StreamingPropertiesTypeDef = TypedDict(
    "StreamingPropertiesTypeDef",
    {
        "StreamingExperiencePreferredProtocol": StreamingExperiencePreferredProtocolEnumType,
        "UserSettings": List["UserSettingTypeDef"],
        "StorageConnectors": List["StorageConnectorTypeDef"],
    },
    total=False,
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

TerminateWorkspacesPoolRequestRequestTypeDef = TypedDict(
    "TerminateWorkspacesPoolRequestRequestTypeDef",
    {
        "PoolId": str,
    },
)

TerminateWorkspacesPoolSessionRequestRequestTypeDef = TypedDict(
    "TerminateWorkspacesPoolSessionRequestRequestTypeDef",
    {
        "SessionId": str,
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

TimeoutSettingsTypeDef = TypedDict(
    "TimeoutSettingsTypeDef",
    {
        "DisconnectTimeoutInSeconds": int,
        "IdleDisconnectTimeoutInSeconds": int,
        "MaxUserDurationInSeconds": int,
    },
    total=False,
)

_RequiredUpdateConnectClientAddInRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateConnectClientAddInRequestRequestTypeDef",
    {
        "AddInId": str,
        "ResourceId": str,
    },
)
_OptionalUpdateConnectClientAddInRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateConnectClientAddInRequestRequestTypeDef",
    {
        "Name": str,
        "URL": str,
    },
    total=False,
)

class UpdateConnectClientAddInRequestRequestTypeDef(
    _RequiredUpdateConnectClientAddInRequestRequestTypeDef,
    _OptionalUpdateConnectClientAddInRequestRequestTypeDef,
):
    pass

UpdateConnectionAliasPermissionRequestRequestTypeDef = TypedDict(
    "UpdateConnectionAliasPermissionRequestRequestTypeDef",
    {
        "AliasId": str,
        "ConnectionAliasPermission": "ConnectionAliasPermissionTypeDef",
    },
)

UpdateResultTypeDef = TypedDict(
    "UpdateResultTypeDef",
    {
        "UpdateAvailable": bool,
        "Description": str,
    },
    total=False,
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

_RequiredUpdateWorkspacesPoolRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkspacesPoolRequestRequestTypeDef",
    {
        "PoolId": str,
    },
)
_OptionalUpdateWorkspacesPoolRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkspacesPoolRequestRequestTypeDef",
    {
        "Description": str,
        "BundleId": str,
        "DirectoryId": str,
        "Capacity": "CapacityTypeDef",
        "ApplicationSettings": "ApplicationSettingsRequestTypeDef",
        "TimeoutSettings": "TimeoutSettingsTypeDef",
    },
    total=False,
)

class UpdateWorkspacesPoolRequestRequestTypeDef(
    _RequiredUpdateWorkspacesPoolRequestRequestTypeDef,
    _OptionalUpdateWorkspacesPoolRequestRequestTypeDef,
):
    pass

UpdateWorkspacesPoolResultTypeDef = TypedDict(
    "UpdateWorkspacesPoolResultTypeDef",
    {
        "WorkspacesPool": "WorkspacesPoolTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUserSettingTypeDef = TypedDict(
    "_RequiredUserSettingTypeDef",
    {
        "Action": UserSettingActionEnumType,
        "Permission": UserSettingPermissionEnumType,
    },
)
_OptionalUserSettingTypeDef = TypedDict(
    "_OptionalUserSettingTypeDef",
    {
        "MaximumLength": int,
    },
    total=False,
)

class UserSettingTypeDef(_RequiredUserSettingTypeDef, _OptionalUserSettingTypeDef):
    pass

UserStorageTypeDef = TypedDict(
    "UserStorageTypeDef",
    {
        "Capacity": str,
    },
    total=False,
)

WorkSpaceApplicationDeploymentTypeDef = TypedDict(
    "WorkSpaceApplicationDeploymentTypeDef",
    {
        "Associations": List["WorkspaceResourceAssociationTypeDef"],
    },
    total=False,
)

WorkSpaceApplicationTypeDef = TypedDict(
    "WorkSpaceApplicationTypeDef",
    {
        "ApplicationId": str,
        "Created": datetime,
        "Description": str,
        "LicenseType": WorkSpaceApplicationLicenseTypeType,
        "Name": str,
        "Owner": str,
        "State": WorkSpaceApplicationStateType,
        "SupportedComputeTypeNames": List[ComputeType],
        "SupportedOperatingSystemNames": List[OperatingSystemNameType],
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
        "State": WorkspaceBundleStateType,
        "BundleType": BundleTypeType,
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
        "InstanceIamRoleArn": str,
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
        "SamlProperties": "SamlPropertiesTypeDef",
        "CertificateBasedAuthProperties": "CertificateBasedAuthPropertiesTypeDef",
        "WorkspaceDirectoryName": str,
        "WorkspaceDirectoryDescription": str,
        "UserIdentityType": UserIdentityTypeType,
        "WorkspaceType": WorkspaceTypeType,
        "ActiveDirectoryConfig": "ActiveDirectoryConfigTypeDef",
        "StreamingProperties": "StreamingPropertiesTypeDef",
        "ErrorMessage": str,
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
        "Updates": "UpdateResultTypeDef",
        "ErrorDetails": List["ErrorDetailsTypeDef"],
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
        "Protocols": List[ProtocolType],
        "OperatingSystemName": OperatingSystemNameType,
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
        "WorkspaceName": str,
    },
    total=False,
)

class WorkspaceRequestTypeDef(_RequiredWorkspaceRequestTypeDef, _OptionalWorkspaceRequestTypeDef):
    pass

WorkspaceResourceAssociationTypeDef = TypedDict(
    "WorkspaceResourceAssociationTypeDef",
    {
        "AssociatedResourceId": str,
        "AssociatedResourceType": Literal["APPLICATION"],
        "Created": datetime,
        "LastUpdatedTime": datetime,
        "State": AssociationStateType,
        "StateReason": "AssociationStateReasonTypeDef",
        "WorkspaceId": str,
    },
    total=False,
)

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
        "WorkspaceName": str,
        "WorkspaceProperties": "WorkspacePropertiesTypeDef",
        "ModificationStates": List["ModificationStateTypeDef"],
        "RelatedWorkspaces": List["RelatedWorkspacePropertiesTypeDef"],
        "DataReplicationSettings": "DataReplicationSettingsTypeDef",
        "StandbyWorkspacesProperties": List["StandbyWorkspacesPropertiesTypeDef"],
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

WorkspacesPoolErrorTypeDef = TypedDict(
    "WorkspacesPoolErrorTypeDef",
    {
        "ErrorCode": WorkspacesPoolErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredWorkspacesPoolSessionTypeDef = TypedDict(
    "_RequiredWorkspacesPoolSessionTypeDef",
    {
        "SessionId": str,
        "PoolId": str,
        "UserId": str,
    },
)
_OptionalWorkspacesPoolSessionTypeDef = TypedDict(
    "_OptionalWorkspacesPoolSessionTypeDef",
    {
        "AuthenticationType": Literal["SAML"],
        "ConnectionState": SessionConnectionStateType,
        "InstanceId": str,
        "ExpirationTime": datetime,
        "NetworkAccessConfiguration": "NetworkAccessConfigurationTypeDef",
        "StartTime": datetime,
    },
    total=False,
)

class WorkspacesPoolSessionTypeDef(
    _RequiredWorkspacesPoolSessionTypeDef, _OptionalWorkspacesPoolSessionTypeDef
):
    pass

_RequiredWorkspacesPoolTypeDef = TypedDict(
    "_RequiredWorkspacesPoolTypeDef",
    {
        "PoolId": str,
        "PoolArn": str,
        "CapacityStatus": "CapacityStatusTypeDef",
        "PoolName": str,
        "State": WorkspacesPoolStateType,
        "CreatedAt": datetime,
        "BundleId": str,
        "DirectoryId": str,
    },
)
_OptionalWorkspacesPoolTypeDef = TypedDict(
    "_OptionalWorkspacesPoolTypeDef",
    {
        "Description": str,
        "Errors": List["WorkspacesPoolErrorTypeDef"],
        "ApplicationSettings": "ApplicationSettingsResponseTypeDef",
        "TimeoutSettings": "TimeoutSettingsTypeDef",
    },
    total=False,
)

class WorkspacesPoolTypeDef(_RequiredWorkspacesPoolTypeDef, _OptionalWorkspacesPoolTypeDef):
    pass
