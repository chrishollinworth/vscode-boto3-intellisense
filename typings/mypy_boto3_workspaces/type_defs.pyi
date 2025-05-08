"""
Type annotations for workspaces service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_workspaces.type_defs import AcceptAccountLinkInvitationRequestTypeDef

    data: AcceptAccountLinkInvitationRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    AccessPropertyValueType,
    AccountLinkStatusEnumType,
    AGAModeForDirectoryEnumType,
    AGAModeForWorkSpaceEnumType,
    AGAPreferredProtocolForDirectoryType,
    AGAPreferredProtocolForWorkSpaceType,
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
    DescribeWorkspaceDirectoriesFilterNameType,
    DescribeWorkspacesPoolsFilterOperatorType,
    EndpointEncryptionModeType,
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

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AcceptAccountLinkInvitationRequestTypeDef",
    "AcceptAccountLinkInvitationResultTypeDef",
    "AccountLinkTypeDef",
    "AccountModificationTypeDef",
    "ActiveDirectoryConfigTypeDef",
    "ApplicationResourceAssociationTypeDef",
    "ApplicationSettingsRequestTypeDef",
    "ApplicationSettingsResponseTypeDef",
    "AssociateConnectionAliasRequestTypeDef",
    "AssociateConnectionAliasResultTypeDef",
    "AssociateIpGroupsRequestTypeDef",
    "AssociateWorkspaceApplicationRequestTypeDef",
    "AssociateWorkspaceApplicationResultTypeDef",
    "AssociationStateReasonTypeDef",
    "AuthorizeIpRulesRequestTypeDef",
    "BlobTypeDef",
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
    "CopyWorkspaceImageRequestTypeDef",
    "CopyWorkspaceImageResultTypeDef",
    "CreateAccountLinkInvitationRequestTypeDef",
    "CreateAccountLinkInvitationResultTypeDef",
    "CreateConnectClientAddInRequestTypeDef",
    "CreateConnectClientAddInResultTypeDef",
    "CreateConnectionAliasRequestTypeDef",
    "CreateConnectionAliasResultTypeDef",
    "CreateIpGroupRequestTypeDef",
    "CreateIpGroupResultTypeDef",
    "CreateStandbyWorkspacesRequestTypeDef",
    "CreateStandbyWorkspacesResultTypeDef",
    "CreateTagsRequestTypeDef",
    "CreateUpdatedWorkspaceImageRequestTypeDef",
    "CreateUpdatedWorkspaceImageResultTypeDef",
    "CreateWorkspaceBundleRequestTypeDef",
    "CreateWorkspaceBundleResultTypeDef",
    "CreateWorkspaceImageRequestTypeDef",
    "CreateWorkspaceImageResultTypeDef",
    "CreateWorkspacesPoolRequestTypeDef",
    "CreateWorkspacesPoolResultTypeDef",
    "CreateWorkspacesRequestTypeDef",
    "CreateWorkspacesResultTypeDef",
    "DataReplicationSettingsTypeDef",
    "DefaultClientBrandingAttributesTypeDef",
    "DefaultImportClientBrandingAttributesTypeDef",
    "DefaultWorkspaceCreationPropertiesTypeDef",
    "DeleteAccountLinkInvitationRequestTypeDef",
    "DeleteAccountLinkInvitationResultTypeDef",
    "DeleteClientBrandingRequestTypeDef",
    "DeleteConnectClientAddInRequestTypeDef",
    "DeleteConnectionAliasRequestTypeDef",
    "DeleteIpGroupRequestTypeDef",
    "DeleteTagsRequestTypeDef",
    "DeleteWorkspaceBundleRequestTypeDef",
    "DeleteWorkspaceImageRequestTypeDef",
    "DeployWorkspaceApplicationsRequestTypeDef",
    "DeployWorkspaceApplicationsResultTypeDef",
    "DeregisterWorkspaceDirectoryRequestTypeDef",
    "DescribeAccountModificationsRequestPaginateTypeDef",
    "DescribeAccountModificationsRequestTypeDef",
    "DescribeAccountModificationsResultTypeDef",
    "DescribeAccountResultTypeDef",
    "DescribeApplicationAssociationsRequestTypeDef",
    "DescribeApplicationAssociationsResultTypeDef",
    "DescribeApplicationsRequestTypeDef",
    "DescribeApplicationsResultTypeDef",
    "DescribeBundleAssociationsRequestTypeDef",
    "DescribeBundleAssociationsResultTypeDef",
    "DescribeClientBrandingRequestTypeDef",
    "DescribeClientBrandingResultTypeDef",
    "DescribeClientPropertiesRequestTypeDef",
    "DescribeClientPropertiesResultTypeDef",
    "DescribeConnectClientAddInsRequestTypeDef",
    "DescribeConnectClientAddInsResultTypeDef",
    "DescribeConnectionAliasPermissionsRequestTypeDef",
    "DescribeConnectionAliasPermissionsResultTypeDef",
    "DescribeConnectionAliasesRequestTypeDef",
    "DescribeConnectionAliasesResultTypeDef",
    "DescribeImageAssociationsRequestTypeDef",
    "DescribeImageAssociationsResultTypeDef",
    "DescribeIpGroupsRequestPaginateTypeDef",
    "DescribeIpGroupsRequestTypeDef",
    "DescribeIpGroupsResultTypeDef",
    "DescribeTagsRequestTypeDef",
    "DescribeTagsResultTypeDef",
    "DescribeWorkspaceAssociationsRequestTypeDef",
    "DescribeWorkspaceAssociationsResultTypeDef",
    "DescribeWorkspaceBundlesRequestPaginateTypeDef",
    "DescribeWorkspaceBundlesRequestTypeDef",
    "DescribeWorkspaceBundlesResultTypeDef",
    "DescribeWorkspaceDirectoriesFilterTypeDef",
    "DescribeWorkspaceDirectoriesRequestPaginateTypeDef",
    "DescribeWorkspaceDirectoriesRequestTypeDef",
    "DescribeWorkspaceDirectoriesResultTypeDef",
    "DescribeWorkspaceImagePermissionsRequestTypeDef",
    "DescribeWorkspaceImagePermissionsResultTypeDef",
    "DescribeWorkspaceImagesRequestPaginateTypeDef",
    "DescribeWorkspaceImagesRequestTypeDef",
    "DescribeWorkspaceImagesResultTypeDef",
    "DescribeWorkspaceSnapshotsRequestTypeDef",
    "DescribeWorkspaceSnapshotsResultTypeDef",
    "DescribeWorkspacesConnectionStatusRequestPaginateTypeDef",
    "DescribeWorkspacesConnectionStatusRequestTypeDef",
    "DescribeWorkspacesConnectionStatusResultTypeDef",
    "DescribeWorkspacesPoolSessionsRequestTypeDef",
    "DescribeWorkspacesPoolSessionsResultTypeDef",
    "DescribeWorkspacesPoolsFilterTypeDef",
    "DescribeWorkspacesPoolsRequestTypeDef",
    "DescribeWorkspacesPoolsResultTypeDef",
    "DescribeWorkspacesRequestPaginateTypeDef",
    "DescribeWorkspacesRequestTypeDef",
    "DescribeWorkspacesResultTypeDef",
    "DisassociateConnectionAliasRequestTypeDef",
    "DisassociateIpGroupsRequestTypeDef",
    "DisassociateWorkspaceApplicationRequestTypeDef",
    "DisassociateWorkspaceApplicationResultTypeDef",
    "ErrorDetailsTypeDef",
    "FailedCreateStandbyWorkspacesRequestTypeDef",
    "FailedCreateWorkspaceRequestTypeDef",
    "FailedWorkspaceChangeRequestTypeDef",
    "GetAccountLinkRequestTypeDef",
    "GetAccountLinkResultTypeDef",
    "GlobalAcceleratorForDirectoryTypeDef",
    "GlobalAcceleratorForWorkSpaceTypeDef",
    "IDCConfigTypeDef",
    "ImagePermissionTypeDef",
    "ImageResourceAssociationTypeDef",
    "ImportClientBrandingRequestTypeDef",
    "ImportClientBrandingResultTypeDef",
    "ImportWorkspaceImageRequestTypeDef",
    "ImportWorkspaceImageResultTypeDef",
    "IosClientBrandingAttributesTypeDef",
    "IosImportClientBrandingAttributesTypeDef",
    "IpRuleItemTypeDef",
    "ListAccountLinksRequestPaginateTypeDef",
    "ListAccountLinksRequestTypeDef",
    "ListAccountLinksResultTypeDef",
    "ListAvailableManagementCidrRangesRequestPaginateTypeDef",
    "ListAvailableManagementCidrRangesRequestTypeDef",
    "ListAvailableManagementCidrRangesResultTypeDef",
    "MicrosoftEntraConfigTypeDef",
    "MigrateWorkspaceRequestTypeDef",
    "MigrateWorkspaceResultTypeDef",
    "ModificationStateTypeDef",
    "ModifyAccountRequestTypeDef",
    "ModifyCertificateBasedAuthPropertiesRequestTypeDef",
    "ModifyClientPropertiesRequestTypeDef",
    "ModifyEndpointEncryptionModeRequestTypeDef",
    "ModifySamlPropertiesRequestTypeDef",
    "ModifySelfservicePermissionsRequestTypeDef",
    "ModifyStreamingPropertiesRequestTypeDef",
    "ModifyWorkspaceAccessPropertiesRequestTypeDef",
    "ModifyWorkspaceCreationPropertiesRequestTypeDef",
    "ModifyWorkspacePropertiesRequestTypeDef",
    "ModifyWorkspaceStateRequestTypeDef",
    "NetworkAccessConfigurationTypeDef",
    "OperatingSystemTypeDef",
    "PaginatorConfigTypeDef",
    "PendingCreateStandbyWorkspacesRequestTypeDef",
    "RebootRequestTypeDef",
    "RebootWorkspacesRequestTypeDef",
    "RebootWorkspacesResultTypeDef",
    "RebuildRequestTypeDef",
    "RebuildWorkspacesRequestTypeDef",
    "RebuildWorkspacesResultTypeDef",
    "RegisterWorkspaceDirectoryRequestTypeDef",
    "RegisterWorkspaceDirectoryResultTypeDef",
    "RejectAccountLinkInvitationRequestTypeDef",
    "RejectAccountLinkInvitationResultTypeDef",
    "RelatedWorkspacePropertiesTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreWorkspaceRequestTypeDef",
    "RevokeIpRulesRequestTypeDef",
    "RootStorageTypeDef",
    "SamlPropertiesTypeDef",
    "SelfservicePermissionsTypeDef",
    "SnapshotTypeDef",
    "StandbyWorkspaceOutputTypeDef",
    "StandbyWorkspaceTypeDef",
    "StandbyWorkspaceUnionTypeDef",
    "StandbyWorkspacesPropertiesTypeDef",
    "StartRequestTypeDef",
    "StartWorkspacesPoolRequestTypeDef",
    "StartWorkspacesRequestTypeDef",
    "StartWorkspacesResultTypeDef",
    "StopRequestTypeDef",
    "StopWorkspacesPoolRequestTypeDef",
    "StopWorkspacesRequestTypeDef",
    "StopWorkspacesResultTypeDef",
    "StorageConnectorTypeDef",
    "StreamingPropertiesOutputTypeDef",
    "StreamingPropertiesTypeDef",
    "StreamingPropertiesUnionTypeDef",
    "TagTypeDef",
    "TerminateRequestTypeDef",
    "TerminateWorkspacesPoolRequestTypeDef",
    "TerminateWorkspacesPoolSessionRequestTypeDef",
    "TerminateWorkspacesRequestTypeDef",
    "TerminateWorkspacesResultTypeDef",
    "TimeoutSettingsTypeDef",
    "UpdateConnectClientAddInRequestTypeDef",
    "UpdateConnectionAliasPermissionRequestTypeDef",
    "UpdateResultTypeDef",
    "UpdateRulesOfIpGroupRequestTypeDef",
    "UpdateWorkspaceBundleRequestTypeDef",
    "UpdateWorkspaceImagePermissionRequestTypeDef",
    "UpdateWorkspacesPoolRequestTypeDef",
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
    "WorkspacePropertiesOutputTypeDef",
    "WorkspacePropertiesTypeDef",
    "WorkspacePropertiesUnionTypeDef",
    "WorkspaceRequestOutputTypeDef",
    "WorkspaceRequestTypeDef",
    "WorkspaceRequestUnionTypeDef",
    "WorkspaceResourceAssociationTypeDef",
    "WorkspaceTypeDef",
    "WorkspacesIpGroupTypeDef",
    "WorkspacesPoolErrorTypeDef",
    "WorkspacesPoolSessionTypeDef",
    "WorkspacesPoolTypeDef",
)

class AcceptAccountLinkInvitationRequestTypeDef(TypedDict):
    LinkId: str
    ClientToken: NotRequired[str]

class AccountLinkTypeDef(TypedDict):
    AccountLinkId: NotRequired[str]
    AccountLinkStatus: NotRequired[AccountLinkStatusEnumType]
    SourceAccountId: NotRequired[str]
    TargetAccountId: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AccountModificationTypeDef(TypedDict):
    ModificationState: NotRequired[DedicatedTenancyModificationStateEnumType]
    DedicatedTenancySupport: NotRequired[DedicatedTenancySupportResultEnumType]
    DedicatedTenancyManagementCidrRange: NotRequired[str]
    StartTime: NotRequired[datetime]
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]

class ActiveDirectoryConfigTypeDef(TypedDict):
    DomainName: str
    ServiceAccountSecretArn: str

class AssociationStateReasonTypeDef(TypedDict):
    ErrorCode: NotRequired[AssociationErrorCodeType]
    ErrorMessage: NotRequired[str]

class ApplicationSettingsRequestTypeDef(TypedDict):
    Status: ApplicationSettingsStatusEnumType
    SettingsGroup: NotRequired[str]

class ApplicationSettingsResponseTypeDef(TypedDict):
    Status: ApplicationSettingsStatusEnumType
    SettingsGroup: NotRequired[str]
    S3BucketName: NotRequired[str]

class AssociateConnectionAliasRequestTypeDef(TypedDict):
    AliasId: str
    ResourceId: str

class AssociateIpGroupsRequestTypeDef(TypedDict):
    DirectoryId: str
    GroupIds: Sequence[str]

class AssociateWorkspaceApplicationRequestTypeDef(TypedDict):
    WorkspaceId: str
    ApplicationId: str

class IpRuleItemTypeDef(TypedDict):
    ipRule: NotRequired[str]
    ruleDesc: NotRequired[str]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class CapacityStatusTypeDef(TypedDict):
    AvailableUserSessions: int
    DesiredUserSessions: int
    ActualUserSessions: int
    ActiveUserSessions: int

class CapacityTypeDef(TypedDict):
    DesiredUserSessions: int

class CertificateBasedAuthPropertiesTypeDef(TypedDict):
    Status: NotRequired[CertificateBasedAuthStatusEnumType]
    CertificateAuthorityArn: NotRequired[str]

class ClientPropertiesTypeDef(TypedDict):
    ReconnectEnabled: NotRequired[ReconnectEnumType]
    LogUploadEnabled: NotRequired[LogUploadEnumType]

class ComputeTypeTypeDef(TypedDict):
    Name: NotRequired[ComputeType]

class ConnectClientAddInTypeDef(TypedDict):
    AddInId: NotRequired[str]
    ResourceId: NotRequired[str]
    Name: NotRequired[str]
    URL: NotRequired[str]

class ConnectionAliasAssociationTypeDef(TypedDict):
    AssociationStatus: NotRequired[AssociationStatusType]
    AssociatedAccountId: NotRequired[str]
    ResourceId: NotRequired[str]
    ConnectionIdentifier: NotRequired[str]

class ConnectionAliasPermissionTypeDef(TypedDict):
    SharedAccountId: str
    AllowAssociation: bool

class TagTypeDef(TypedDict):
    Key: str
    Value: NotRequired[str]

class CreateAccountLinkInvitationRequestTypeDef(TypedDict):
    TargetAccountId: str
    ClientToken: NotRequired[str]

class CreateConnectClientAddInRequestTypeDef(TypedDict):
    ResourceId: str
    Name: str
    URL: str

class PendingCreateStandbyWorkspacesRequestTypeDef(TypedDict):
    UserName: NotRequired[str]
    DirectoryId: NotRequired[str]
    State: NotRequired[WorkspaceStateType]
    WorkspaceId: NotRequired[str]

class RootStorageTypeDef(TypedDict):
    Capacity: str

class UserStorageTypeDef(TypedDict):
    Capacity: str

OperatingSystemTypeDef = TypedDict(
    "OperatingSystemTypeDef",
    {
        "Type": NotRequired[OperatingSystemTypeType],
    },
)

class TimeoutSettingsTypeDef(TypedDict):
    DisconnectTimeoutInSeconds: NotRequired[int]
    IdleDisconnectTimeoutInSeconds: NotRequired[int]
    MaxUserDurationInSeconds: NotRequired[int]

class DataReplicationSettingsTypeDef(TypedDict):
    DataReplication: NotRequired[DataReplicationType]
    RecoverySnapshotTime: NotRequired[datetime]

class DefaultClientBrandingAttributesTypeDef(TypedDict):
    LogoUrl: NotRequired[str]
    SupportEmail: NotRequired[str]
    SupportLink: NotRequired[str]
    ForgotPasswordLink: NotRequired[str]
    LoginMessage: NotRequired[Dict[str, str]]

class DefaultWorkspaceCreationPropertiesTypeDef(TypedDict):
    EnableWorkDocs: NotRequired[bool]
    EnableInternetAccess: NotRequired[bool]
    DefaultOu: NotRequired[str]
    CustomSecurityGroupId: NotRequired[str]
    UserEnabledAsLocalAdministrator: NotRequired[bool]
    EnableMaintenanceMode: NotRequired[bool]
    InstanceIamRoleArn: NotRequired[str]

class DeleteAccountLinkInvitationRequestTypeDef(TypedDict):
    LinkId: str
    ClientToken: NotRequired[str]

class DeleteClientBrandingRequestTypeDef(TypedDict):
    ResourceId: str
    Platforms: Sequence[ClientDeviceTypeType]

class DeleteConnectClientAddInRequestTypeDef(TypedDict):
    AddInId: str
    ResourceId: str

class DeleteConnectionAliasRequestTypeDef(TypedDict):
    AliasId: str

class DeleteIpGroupRequestTypeDef(TypedDict):
    GroupId: str

class DeleteTagsRequestTypeDef(TypedDict):
    ResourceId: str
    TagKeys: Sequence[str]

class DeleteWorkspaceBundleRequestTypeDef(TypedDict):
    BundleId: NotRequired[str]

class DeleteWorkspaceImageRequestTypeDef(TypedDict):
    ImageId: str

class DeployWorkspaceApplicationsRequestTypeDef(TypedDict):
    WorkspaceId: str
    Force: NotRequired[bool]

class DeregisterWorkspaceDirectoryRequestTypeDef(TypedDict):
    DirectoryId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeAccountModificationsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]

class DescribeApplicationAssociationsRequestTypeDef(TypedDict):
    ApplicationId: str
    AssociatedResourceTypes: Sequence[ApplicationAssociatedResourceTypeType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeApplicationsRequestTypeDef(TypedDict):
    ApplicationIds: NotRequired[Sequence[str]]
    ComputeTypeNames: NotRequired[Sequence[ComputeType]]
    LicenseType: NotRequired[WorkSpaceApplicationLicenseTypeType]
    OperatingSystemNames: NotRequired[Sequence[OperatingSystemNameType]]
    Owner: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class WorkSpaceApplicationTypeDef(TypedDict):
    ApplicationId: NotRequired[str]
    Created: NotRequired[datetime]
    Description: NotRequired[str]
    LicenseType: NotRequired[WorkSpaceApplicationLicenseTypeType]
    Name: NotRequired[str]
    Owner: NotRequired[str]
    State: NotRequired[WorkSpaceApplicationStateType]
    SupportedComputeTypeNames: NotRequired[List[ComputeType]]
    SupportedOperatingSystemNames: NotRequired[List[OperatingSystemNameType]]

class DescribeBundleAssociationsRequestTypeDef(TypedDict):
    BundleId: str
    AssociatedResourceTypes: Sequence[Literal["APPLICATION"]]

class DescribeClientBrandingRequestTypeDef(TypedDict):
    ResourceId: str

class IosClientBrandingAttributesTypeDef(TypedDict):
    LogoUrl: NotRequired[str]
    Logo2xUrl: NotRequired[str]
    Logo3xUrl: NotRequired[str]
    SupportEmail: NotRequired[str]
    SupportLink: NotRequired[str]
    ForgotPasswordLink: NotRequired[str]
    LoginMessage: NotRequired[Dict[str, str]]

class DescribeClientPropertiesRequestTypeDef(TypedDict):
    ResourceIds: Sequence[str]

class DescribeConnectClientAddInsRequestTypeDef(TypedDict):
    ResourceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeConnectionAliasPermissionsRequestTypeDef(TypedDict):
    AliasId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeConnectionAliasesRequestTypeDef(TypedDict):
    AliasIds: NotRequired[Sequence[str]]
    ResourceId: NotRequired[str]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeImageAssociationsRequestTypeDef(TypedDict):
    ImageId: str
    AssociatedResourceTypes: Sequence[Literal["APPLICATION"]]

class DescribeIpGroupsRequestTypeDef(TypedDict):
    GroupIds: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeTagsRequestTypeDef(TypedDict):
    ResourceId: str

class DescribeWorkspaceAssociationsRequestTypeDef(TypedDict):
    WorkspaceId: str
    AssociatedResourceTypes: Sequence[Literal["APPLICATION"]]

class DescribeWorkspaceBundlesRequestTypeDef(TypedDict):
    BundleIds: NotRequired[Sequence[str]]
    Owner: NotRequired[str]
    NextToken: NotRequired[str]

class DescribeWorkspaceDirectoriesFilterTypeDef(TypedDict):
    Name: DescribeWorkspaceDirectoriesFilterNameType
    Values: Sequence[str]

class DescribeWorkspaceImagePermissionsRequestTypeDef(TypedDict):
    ImageId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ImagePermissionTypeDef(TypedDict):
    SharedAccountId: NotRequired[str]

class DescribeWorkspaceImagesRequestTypeDef(TypedDict):
    ImageIds: NotRequired[Sequence[str]]
    ImageType: NotRequired[ImageTypeType]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeWorkspaceSnapshotsRequestTypeDef(TypedDict):
    WorkspaceId: str

class SnapshotTypeDef(TypedDict):
    SnapshotTime: NotRequired[datetime]

class DescribeWorkspacesConnectionStatusRequestTypeDef(TypedDict):
    WorkspaceIds: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]

class WorkspaceConnectionStatusTypeDef(TypedDict):
    WorkspaceId: NotRequired[str]
    ConnectionState: NotRequired[ConnectionStateType]
    ConnectionStateCheckTimestamp: NotRequired[datetime]
    LastKnownUserConnectionTimestamp: NotRequired[datetime]

class DescribeWorkspacesPoolSessionsRequestTypeDef(TypedDict):
    PoolId: str
    UserId: NotRequired[str]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeWorkspacesPoolsFilterTypeDef(TypedDict):
    Name: Literal["PoolName"]
    Values: Sequence[str]
    Operator: DescribeWorkspacesPoolsFilterOperatorType

class DescribeWorkspacesRequestTypeDef(TypedDict):
    WorkspaceIds: NotRequired[Sequence[str]]
    DirectoryId: NotRequired[str]
    UserName: NotRequired[str]
    BundleId: NotRequired[str]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]
    WorkspaceName: NotRequired[str]

class DisassociateConnectionAliasRequestTypeDef(TypedDict):
    AliasId: str

class DisassociateIpGroupsRequestTypeDef(TypedDict):
    DirectoryId: str
    GroupIds: Sequence[str]

class DisassociateWorkspaceApplicationRequestTypeDef(TypedDict):
    WorkspaceId: str
    ApplicationId: str

class ErrorDetailsTypeDef(TypedDict):
    ErrorCode: NotRequired[WorkspaceImageErrorDetailCodeType]
    ErrorMessage: NotRequired[str]

class FailedWorkspaceChangeRequestTypeDef(TypedDict):
    WorkspaceId: NotRequired[str]
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]

class GetAccountLinkRequestTypeDef(TypedDict):
    LinkId: NotRequired[str]
    LinkedAccountId: NotRequired[str]

class GlobalAcceleratorForDirectoryTypeDef(TypedDict):
    Mode: AGAModeForDirectoryEnumType
    PreferredProtocol: NotRequired[AGAPreferredProtocolForDirectoryType]

class GlobalAcceleratorForWorkSpaceTypeDef(TypedDict):
    Mode: AGAModeForWorkSpaceEnumType
    PreferredProtocol: NotRequired[AGAPreferredProtocolForWorkSpaceType]

class IDCConfigTypeDef(TypedDict):
    InstanceArn: NotRequired[str]
    ApplicationArn: NotRequired[str]

class ListAccountLinksRequestTypeDef(TypedDict):
    LinkStatusFilter: NotRequired[Sequence[AccountLinkStatusEnumType]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListAvailableManagementCidrRangesRequestTypeDef(TypedDict):
    ManagementCidrRangeConstraint: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class MicrosoftEntraConfigTypeDef(TypedDict):
    TenantId: NotRequired[str]
    ApplicationConfigSecretArn: NotRequired[str]

class MigrateWorkspaceRequestTypeDef(TypedDict):
    SourceWorkspaceId: str
    BundleId: str

class ModificationStateTypeDef(TypedDict):
    Resource: NotRequired[ModificationResourceEnumType]
    State: NotRequired[ModificationStateEnumType]

class ModifyAccountRequestTypeDef(TypedDict):
    DedicatedTenancySupport: NotRequired[Literal["ENABLED"]]
    DedicatedTenancyManagementCidrRange: NotRequired[str]

class ModifyEndpointEncryptionModeRequestTypeDef(TypedDict):
    DirectoryId: str
    EndpointEncryptionMode: EndpointEncryptionModeType

class SamlPropertiesTypeDef(TypedDict):
    Status: NotRequired[SamlStatusEnumType]
    UserAccessUrl: NotRequired[str]
    RelayStateParameterName: NotRequired[str]

class SelfservicePermissionsTypeDef(TypedDict):
    RestartWorkspace: NotRequired[ReconnectEnumType]
    IncreaseVolumeSize: NotRequired[ReconnectEnumType]
    ChangeComputeType: NotRequired[ReconnectEnumType]
    SwitchRunningMode: NotRequired[ReconnectEnumType]
    RebuildWorkspace: NotRequired[ReconnectEnumType]

class WorkspaceAccessPropertiesTypeDef(TypedDict):
    DeviceTypeWindows: NotRequired[AccessPropertyValueType]
    DeviceTypeOsx: NotRequired[AccessPropertyValueType]
    DeviceTypeWeb: NotRequired[AccessPropertyValueType]
    DeviceTypeIos: NotRequired[AccessPropertyValueType]
    DeviceTypeAndroid: NotRequired[AccessPropertyValueType]
    DeviceTypeChromeOs: NotRequired[AccessPropertyValueType]
    DeviceTypeZeroClient: NotRequired[AccessPropertyValueType]
    DeviceTypeLinux: NotRequired[AccessPropertyValueType]
    DeviceTypeWorkSpacesThinClient: NotRequired[AccessPropertyValueType]

class WorkspaceCreationPropertiesTypeDef(TypedDict):
    EnableWorkDocs: NotRequired[bool]
    EnableInternetAccess: NotRequired[bool]
    DefaultOu: NotRequired[str]
    CustomSecurityGroupId: NotRequired[str]
    UserEnabledAsLocalAdministrator: NotRequired[bool]
    EnableMaintenanceMode: NotRequired[bool]
    InstanceIamRoleArn: NotRequired[str]

class ModifyWorkspaceStateRequestTypeDef(TypedDict):
    WorkspaceId: str
    WorkspaceState: TargetWorkspaceStateType

class NetworkAccessConfigurationTypeDef(TypedDict):
    EniPrivateIpAddress: NotRequired[str]
    EniId: NotRequired[str]

class RebootRequestTypeDef(TypedDict):
    WorkspaceId: str

class RebuildRequestTypeDef(TypedDict):
    WorkspaceId: str

class RejectAccountLinkInvitationRequestTypeDef(TypedDict):
    LinkId: str
    ClientToken: NotRequired[str]

RelatedWorkspacePropertiesTypeDef = TypedDict(
    "RelatedWorkspacePropertiesTypeDef",
    {
        "WorkspaceId": NotRequired[str],
        "Region": NotRequired[str],
        "State": NotRequired[WorkspaceStateType],
        "Type": NotRequired[StandbyWorkspaceRelationshipTypeType],
    },
)

class RestoreWorkspaceRequestTypeDef(TypedDict):
    WorkspaceId: str

class RevokeIpRulesRequestTypeDef(TypedDict):
    GroupId: str
    UserRules: Sequence[str]

class StandbyWorkspacesPropertiesTypeDef(TypedDict):
    StandbyWorkspaceId: NotRequired[str]
    DataReplication: NotRequired[DataReplicationType]
    RecoverySnapshotTime: NotRequired[datetime]

class StartRequestTypeDef(TypedDict):
    WorkspaceId: NotRequired[str]

class StartWorkspacesPoolRequestTypeDef(TypedDict):
    PoolId: str

class StopRequestTypeDef(TypedDict):
    WorkspaceId: NotRequired[str]

class StopWorkspacesPoolRequestTypeDef(TypedDict):
    PoolId: str

class StorageConnectorTypeDef(TypedDict):
    ConnectorType: Literal["HOME_FOLDER"]
    Status: StorageConnectorStatusEnumType

class UserSettingTypeDef(TypedDict):
    Action: UserSettingActionEnumType
    Permission: UserSettingPermissionEnumType
    MaximumLength: NotRequired[int]

class TerminateRequestTypeDef(TypedDict):
    WorkspaceId: str

class TerminateWorkspacesPoolRequestTypeDef(TypedDict):
    PoolId: str

class TerminateWorkspacesPoolSessionRequestTypeDef(TypedDict):
    SessionId: str

class UpdateConnectClientAddInRequestTypeDef(TypedDict):
    AddInId: str
    ResourceId: str
    Name: NotRequired[str]
    URL: NotRequired[str]

class UpdateResultTypeDef(TypedDict):
    UpdateAvailable: NotRequired[bool]
    Description: NotRequired[str]

class UpdateWorkspaceBundleRequestTypeDef(TypedDict):
    BundleId: NotRequired[str]
    ImageId: NotRequired[str]

class UpdateWorkspaceImagePermissionRequestTypeDef(TypedDict):
    ImageId: str
    AllowCopyImage: bool
    SharedAccountId: str

class WorkspacesPoolErrorTypeDef(TypedDict):
    ErrorCode: NotRequired[WorkspacesPoolErrorCodeType]
    ErrorMessage: NotRequired[str]

class AcceptAccountLinkInvitationResultTypeDef(TypedDict):
    AccountLink: AccountLinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateConnectionAliasResultTypeDef(TypedDict):
    ConnectionIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class CopyWorkspaceImageResultTypeDef(TypedDict):
    ImageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccountLinkInvitationResultTypeDef(TypedDict):
    AccountLink: AccountLinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectClientAddInResultTypeDef(TypedDict):
    AddInId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectionAliasResultTypeDef(TypedDict):
    AliasId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIpGroupResultTypeDef(TypedDict):
    GroupId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUpdatedWorkspaceImageResultTypeDef(TypedDict):
    ImageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAccountLinkInvitationResultTypeDef(TypedDict):
    AccountLink: AccountLinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountResultTypeDef(TypedDict):
    DedicatedTenancySupport: DedicatedTenancySupportResultEnumType
    DedicatedTenancyManagementCidrRange: str
    DedicatedTenancyAccountType: DedicatedTenancyAccountTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountLinkResultTypeDef(TypedDict):
    AccountLink: AccountLinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportWorkspaceImageResultTypeDef(TypedDict):
    ImageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountLinksResultTypeDef(TypedDict):
    AccountLinks: List[AccountLinkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListAvailableManagementCidrRangesResultTypeDef(TypedDict):
    ManagementCidrRanges: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class MigrateWorkspaceResultTypeDef(TypedDict):
    SourceWorkspaceId: str
    TargetWorkspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterWorkspaceDirectoryResultTypeDef(TypedDict):
    DirectoryId: str
    State: WorkspaceDirectoryStateType
    ResponseMetadata: ResponseMetadataTypeDef

class RejectAccountLinkInvitationResultTypeDef(TypedDict):
    AccountLink: AccountLinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountModificationsResultTypeDef(TypedDict):
    AccountModifications: List[AccountModificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ApplicationResourceAssociationTypeDef(TypedDict):
    ApplicationId: NotRequired[str]
    AssociatedResourceId: NotRequired[str]
    AssociatedResourceType: NotRequired[ApplicationAssociatedResourceTypeType]
    Created: NotRequired[datetime]
    LastUpdatedTime: NotRequired[datetime]
    State: NotRequired[AssociationStateType]
    StateReason: NotRequired[AssociationStateReasonTypeDef]

class BundleResourceAssociationTypeDef(TypedDict):
    AssociatedResourceId: NotRequired[str]
    AssociatedResourceType: NotRequired[Literal["APPLICATION"]]
    BundleId: NotRequired[str]
    Created: NotRequired[datetime]
    LastUpdatedTime: NotRequired[datetime]
    State: NotRequired[AssociationStateType]
    StateReason: NotRequired[AssociationStateReasonTypeDef]

class ImageResourceAssociationTypeDef(TypedDict):
    AssociatedResourceId: NotRequired[str]
    AssociatedResourceType: NotRequired[Literal["APPLICATION"]]
    Created: NotRequired[datetime]
    LastUpdatedTime: NotRequired[datetime]
    ImageId: NotRequired[str]
    State: NotRequired[AssociationStateType]
    StateReason: NotRequired[AssociationStateReasonTypeDef]

class WorkspaceResourceAssociationTypeDef(TypedDict):
    AssociatedResourceId: NotRequired[str]
    AssociatedResourceType: NotRequired[Literal["APPLICATION"]]
    Created: NotRequired[datetime]
    LastUpdatedTime: NotRequired[datetime]
    State: NotRequired[AssociationStateType]
    StateReason: NotRequired[AssociationStateReasonTypeDef]
    WorkspaceId: NotRequired[str]

class AuthorizeIpRulesRequestTypeDef(TypedDict):
    GroupId: str
    UserRules: Sequence[IpRuleItemTypeDef]

class UpdateRulesOfIpGroupRequestTypeDef(TypedDict):
    GroupId: str
    UserRules: Sequence[IpRuleItemTypeDef]

class WorkspacesIpGroupTypeDef(TypedDict):
    groupId: NotRequired[str]
    groupName: NotRequired[str]
    groupDesc: NotRequired[str]
    userRules: NotRequired[List[IpRuleItemTypeDef]]

class DefaultImportClientBrandingAttributesTypeDef(TypedDict):
    Logo: NotRequired[BlobTypeDef]
    SupportEmail: NotRequired[str]
    SupportLink: NotRequired[str]
    ForgotPasswordLink: NotRequired[str]
    LoginMessage: NotRequired[Mapping[str, str]]

class IosImportClientBrandingAttributesTypeDef(TypedDict):
    Logo: NotRequired[BlobTypeDef]
    Logo2x: NotRequired[BlobTypeDef]
    Logo3x: NotRequired[BlobTypeDef]
    SupportEmail: NotRequired[str]
    SupportLink: NotRequired[str]
    ForgotPasswordLink: NotRequired[str]
    LoginMessage: NotRequired[Mapping[str, str]]

class ModifyCertificateBasedAuthPropertiesRequestTypeDef(TypedDict):
    ResourceId: str
    CertificateBasedAuthProperties: NotRequired[CertificateBasedAuthPropertiesTypeDef]
    PropertiesToDelete: NotRequired[
        Sequence[Literal["CERTIFICATE_BASED_AUTH_PROPERTIES_CERTIFICATE_AUTHORITY_ARN"]]
    ]

class ClientPropertiesResultTypeDef(TypedDict):
    ResourceId: NotRequired[str]
    ClientProperties: NotRequired[ClientPropertiesTypeDef]

class ModifyClientPropertiesRequestTypeDef(TypedDict):
    ResourceId: str
    ClientProperties: ClientPropertiesTypeDef

class DescribeConnectClientAddInsResultTypeDef(TypedDict):
    AddIns: List[ConnectClientAddInTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ConnectionAliasTypeDef(TypedDict):
    ConnectionString: NotRequired[str]
    AliasId: NotRequired[str]
    State: NotRequired[ConnectionAliasStateType]
    OwnerAccountId: NotRequired[str]
    Associations: NotRequired[List[ConnectionAliasAssociationTypeDef]]

class DescribeConnectionAliasPermissionsResultTypeDef(TypedDict):
    AliasId: str
    ConnectionAliasPermissions: List[ConnectionAliasPermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateConnectionAliasPermissionRequestTypeDef(TypedDict):
    AliasId: str
    ConnectionAliasPermission: ConnectionAliasPermissionTypeDef

class CopyWorkspaceImageRequestTypeDef(TypedDict):
    Name: str
    SourceImageId: str
    SourceRegion: str
    Description: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateConnectionAliasRequestTypeDef(TypedDict):
    ConnectionString: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateIpGroupRequestTypeDef(TypedDict):
    GroupName: str
    GroupDesc: NotRequired[str]
    UserRules: NotRequired[Sequence[IpRuleItemTypeDef]]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateTagsRequestTypeDef(TypedDict):
    ResourceId: str
    Tags: Sequence[TagTypeDef]

class CreateUpdatedWorkspaceImageRequestTypeDef(TypedDict):
    Name: str
    Description: str
    SourceImageId: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateWorkspaceImageRequestTypeDef(TypedDict):
    Name: str
    Description: str
    WorkspaceId: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class DescribeTagsResultTypeDef(TypedDict):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportWorkspaceImageRequestTypeDef(TypedDict):
    Ec2ImageId: str
    IngestionProcess: WorkspaceImageIngestionProcessType
    ImageName: str
    ImageDescription: str
    Tags: NotRequired[Sequence[TagTypeDef]]
    Applications: NotRequired[Sequence[ApplicationType]]

class StandbyWorkspaceOutputTypeDef(TypedDict):
    PrimaryWorkspaceId: str
    DirectoryId: str
    VolumeEncryptionKey: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]
    DataReplication: NotRequired[DataReplicationType]

class StandbyWorkspaceTypeDef(TypedDict):
    PrimaryWorkspaceId: str
    DirectoryId: str
    VolumeEncryptionKey: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    DataReplication: NotRequired[DataReplicationType]

CreateWorkspaceBundleRequestTypeDef = TypedDict(
    "CreateWorkspaceBundleRequestTypeDef",
    {
        "BundleName": str,
        "BundleDescription": str,
        "ImageId": str,
        "ComputeType": ComputeTypeTypeDef,
        "UserStorage": UserStorageTypeDef,
        "RootStorage": NotRequired[RootStorageTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
WorkspaceBundleTypeDef = TypedDict(
    "WorkspaceBundleTypeDef",
    {
        "BundleId": NotRequired[str],
        "Name": NotRequired[str],
        "Owner": NotRequired[str],
        "Description": NotRequired[str],
        "ImageId": NotRequired[str],
        "RootStorage": NotRequired[RootStorageTypeDef],
        "UserStorage": NotRequired[UserStorageTypeDef],
        "ComputeType": NotRequired[ComputeTypeTypeDef],
        "LastUpdatedTime": NotRequired[datetime],
        "CreationTime": NotRequired[datetime],
        "State": NotRequired[WorkspaceBundleStateType],
        "BundleType": NotRequired[BundleTypeType],
    },
)

class CreateWorkspaceImageResultTypeDef(TypedDict):
    ImageId: str
    Name: str
    Description: str
    OperatingSystem: OperatingSystemTypeDef
    State: WorkspaceImageStateType
    RequiredTenancy: WorkspaceImageRequiredTenancyType
    Created: datetime
    OwnerAccountId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkspacesPoolRequestTypeDef(TypedDict):
    PoolName: str
    Description: str
    BundleId: str
    DirectoryId: str
    Capacity: CapacityTypeDef
    Tags: NotRequired[Sequence[TagTypeDef]]
    ApplicationSettings: NotRequired[ApplicationSettingsRequestTypeDef]
    TimeoutSettings: NotRequired[TimeoutSettingsTypeDef]

class UpdateWorkspacesPoolRequestTypeDef(TypedDict):
    PoolId: str
    Description: NotRequired[str]
    BundleId: NotRequired[str]
    DirectoryId: NotRequired[str]
    Capacity: NotRequired[CapacityTypeDef]
    ApplicationSettings: NotRequired[ApplicationSettingsRequestTypeDef]
    TimeoutSettings: NotRequired[TimeoutSettingsTypeDef]

class DescribeAccountModificationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeIpGroupsRequestPaginateTypeDef(TypedDict):
    GroupIds: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeWorkspaceBundlesRequestPaginateTypeDef(TypedDict):
    BundleIds: NotRequired[Sequence[str]]
    Owner: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeWorkspaceImagesRequestPaginateTypeDef(TypedDict):
    ImageIds: NotRequired[Sequence[str]]
    ImageType: NotRequired[ImageTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeWorkspacesConnectionStatusRequestPaginateTypeDef(TypedDict):
    WorkspaceIds: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeWorkspacesRequestPaginateTypeDef(TypedDict):
    WorkspaceIds: NotRequired[Sequence[str]]
    DirectoryId: NotRequired[str]
    UserName: NotRequired[str]
    BundleId: NotRequired[str]
    WorkspaceName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAccountLinksRequestPaginateTypeDef(TypedDict):
    LinkStatusFilter: NotRequired[Sequence[AccountLinkStatusEnumType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAvailableManagementCidrRangesRequestPaginateTypeDef(TypedDict):
    ManagementCidrRangeConstraint: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeApplicationsResultTypeDef(TypedDict):
    Applications: List[WorkSpaceApplicationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeClientBrandingResultTypeDef(TypedDict):
    DeviceTypeWindows: DefaultClientBrandingAttributesTypeDef
    DeviceTypeOsx: DefaultClientBrandingAttributesTypeDef
    DeviceTypeAndroid: DefaultClientBrandingAttributesTypeDef
    DeviceTypeIos: IosClientBrandingAttributesTypeDef
    DeviceTypeLinux: DefaultClientBrandingAttributesTypeDef
    DeviceTypeWeb: DefaultClientBrandingAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportClientBrandingResultTypeDef(TypedDict):
    DeviceTypeWindows: DefaultClientBrandingAttributesTypeDef
    DeviceTypeOsx: DefaultClientBrandingAttributesTypeDef
    DeviceTypeAndroid: DefaultClientBrandingAttributesTypeDef
    DeviceTypeIos: IosClientBrandingAttributesTypeDef
    DeviceTypeLinux: DefaultClientBrandingAttributesTypeDef
    DeviceTypeWeb: DefaultClientBrandingAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorkspaceDirectoriesRequestPaginateTypeDef(TypedDict):
    DirectoryIds: NotRequired[Sequence[str]]
    WorkspaceDirectoryNames: NotRequired[Sequence[str]]
    Limit: NotRequired[int]
    Filters: NotRequired[Sequence[DescribeWorkspaceDirectoriesFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeWorkspaceDirectoriesRequestTypeDef(TypedDict):
    DirectoryIds: NotRequired[Sequence[str]]
    WorkspaceDirectoryNames: NotRequired[Sequence[str]]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]
    Filters: NotRequired[Sequence[DescribeWorkspaceDirectoriesFilterTypeDef]]

class DescribeWorkspaceImagePermissionsResultTypeDef(TypedDict):
    ImageId: str
    ImagePermissions: List[ImagePermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeWorkspaceSnapshotsResultTypeDef(TypedDict):
    RebuildSnapshots: List[SnapshotTypeDef]
    RestoreSnapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorkspacesConnectionStatusResultTypeDef(TypedDict):
    WorkspacesConnectionStatus: List[WorkspaceConnectionStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeWorkspacesPoolsRequestTypeDef(TypedDict):
    PoolIds: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[DescribeWorkspacesPoolsFilterTypeDef]]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class RebootWorkspacesResultTypeDef(TypedDict):
    FailedRequests: List[FailedWorkspaceChangeRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RebuildWorkspacesResultTypeDef(TypedDict):
    FailedRequests: List[FailedWorkspaceChangeRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartWorkspacesResultTypeDef(TypedDict):
    FailedRequests: List[FailedWorkspaceChangeRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StopWorkspacesResultTypeDef(TypedDict):
    FailedRequests: List[FailedWorkspaceChangeRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TerminateWorkspacesResultTypeDef(TypedDict):
    FailedRequests: List[FailedWorkspaceChangeRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class WorkspacePropertiesOutputTypeDef(TypedDict):
    RunningMode: NotRequired[RunningModeType]
    RunningModeAutoStopTimeoutInMinutes: NotRequired[int]
    RootVolumeSizeGib: NotRequired[int]
    UserVolumeSizeGib: NotRequired[int]
    ComputeTypeName: NotRequired[ComputeType]
    Protocols: NotRequired[List[ProtocolType]]
    OperatingSystemName: NotRequired[OperatingSystemNameType]
    GlobalAccelerator: NotRequired[GlobalAcceleratorForWorkSpaceTypeDef]

class WorkspacePropertiesTypeDef(TypedDict):
    RunningMode: NotRequired[RunningModeType]
    RunningModeAutoStopTimeoutInMinutes: NotRequired[int]
    RootVolumeSizeGib: NotRequired[int]
    UserVolumeSizeGib: NotRequired[int]
    ComputeTypeName: NotRequired[ComputeType]
    Protocols: NotRequired[Sequence[ProtocolType]]
    OperatingSystemName: NotRequired[OperatingSystemNameType]
    GlobalAccelerator: NotRequired[GlobalAcceleratorForWorkSpaceTypeDef]

class RegisterWorkspaceDirectoryRequestTypeDef(TypedDict):
    DirectoryId: NotRequired[str]
    SubnetIds: NotRequired[Sequence[str]]
    EnableWorkDocs: NotRequired[bool]
    EnableSelfService: NotRequired[bool]
    Tenancy: NotRequired[TenancyType]
    Tags: NotRequired[Sequence[TagTypeDef]]
    WorkspaceDirectoryName: NotRequired[str]
    WorkspaceDirectoryDescription: NotRequired[str]
    UserIdentityType: NotRequired[UserIdentityTypeType]
    IdcInstanceArn: NotRequired[str]
    MicrosoftEntraConfig: NotRequired[MicrosoftEntraConfigTypeDef]
    WorkspaceType: NotRequired[WorkspaceTypeType]
    ActiveDirectoryConfig: NotRequired[ActiveDirectoryConfigTypeDef]

class ModifySamlPropertiesRequestTypeDef(TypedDict):
    ResourceId: str
    SamlProperties: NotRequired[SamlPropertiesTypeDef]
    PropertiesToDelete: NotRequired[Sequence[DeletableSamlPropertyType]]

class ModifySelfservicePermissionsRequestTypeDef(TypedDict):
    ResourceId: str
    SelfservicePermissions: SelfservicePermissionsTypeDef

class ModifyWorkspaceAccessPropertiesRequestTypeDef(TypedDict):
    ResourceId: str
    WorkspaceAccessProperties: WorkspaceAccessPropertiesTypeDef

class ModifyWorkspaceCreationPropertiesRequestTypeDef(TypedDict):
    ResourceId: str
    WorkspaceCreationProperties: WorkspaceCreationPropertiesTypeDef

class WorkspacesPoolSessionTypeDef(TypedDict):
    SessionId: str
    PoolId: str
    UserId: str
    AuthenticationType: NotRequired[Literal["SAML"]]
    ConnectionState: NotRequired[SessionConnectionStateType]
    InstanceId: NotRequired[str]
    ExpirationTime: NotRequired[datetime]
    NetworkAccessConfiguration: NotRequired[NetworkAccessConfigurationTypeDef]
    StartTime: NotRequired[datetime]

class RebootWorkspacesRequestTypeDef(TypedDict):
    RebootWorkspaceRequests: Sequence[RebootRequestTypeDef]

class RebuildWorkspacesRequestTypeDef(TypedDict):
    RebuildWorkspaceRequests: Sequence[RebuildRequestTypeDef]

class StartWorkspacesRequestTypeDef(TypedDict):
    StartWorkspaceRequests: Sequence[StartRequestTypeDef]

class StopWorkspacesRequestTypeDef(TypedDict):
    StopWorkspaceRequests: Sequence[StopRequestTypeDef]

class StreamingPropertiesOutputTypeDef(TypedDict):
    StreamingExperiencePreferredProtocol: NotRequired[StreamingExperiencePreferredProtocolEnumType]
    UserSettings: NotRequired[List[UserSettingTypeDef]]
    StorageConnectors: NotRequired[List[StorageConnectorTypeDef]]
    GlobalAccelerator: NotRequired[GlobalAcceleratorForDirectoryTypeDef]

class StreamingPropertiesTypeDef(TypedDict):
    StreamingExperiencePreferredProtocol: NotRequired[StreamingExperiencePreferredProtocolEnumType]
    UserSettings: NotRequired[Sequence[UserSettingTypeDef]]
    StorageConnectors: NotRequired[Sequence[StorageConnectorTypeDef]]
    GlobalAccelerator: NotRequired[GlobalAcceleratorForDirectoryTypeDef]

class TerminateWorkspacesRequestTypeDef(TypedDict):
    TerminateWorkspaceRequests: Sequence[TerminateRequestTypeDef]

class WorkspaceImageTypeDef(TypedDict):
    ImageId: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    OperatingSystem: NotRequired[OperatingSystemTypeDef]
    State: NotRequired[WorkspaceImageStateType]
    RequiredTenancy: NotRequired[WorkspaceImageRequiredTenancyType]
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]
    Created: NotRequired[datetime]
    OwnerAccountId: NotRequired[str]
    Updates: NotRequired[UpdateResultTypeDef]
    ErrorDetails: NotRequired[List[ErrorDetailsTypeDef]]

class WorkspacesPoolTypeDef(TypedDict):
    PoolId: str
    PoolArn: str
    CapacityStatus: CapacityStatusTypeDef
    PoolName: str
    State: WorkspacesPoolStateType
    CreatedAt: datetime
    BundleId: str
    DirectoryId: str
    Description: NotRequired[str]
    Errors: NotRequired[List[WorkspacesPoolErrorTypeDef]]
    ApplicationSettings: NotRequired[ApplicationSettingsResponseTypeDef]
    TimeoutSettings: NotRequired[TimeoutSettingsTypeDef]

class DescribeApplicationAssociationsResultTypeDef(TypedDict):
    Associations: List[ApplicationResourceAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeBundleAssociationsResultTypeDef(TypedDict):
    Associations: List[BundleResourceAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeImageAssociationsResultTypeDef(TypedDict):
    Associations: List[ImageResourceAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateWorkspaceApplicationResultTypeDef(TypedDict):
    Association: WorkspaceResourceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorkspaceAssociationsResultTypeDef(TypedDict):
    Associations: List[WorkspaceResourceAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateWorkspaceApplicationResultTypeDef(TypedDict):
    Association: WorkspaceResourceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class WorkSpaceApplicationDeploymentTypeDef(TypedDict):
    Associations: NotRequired[List[WorkspaceResourceAssociationTypeDef]]

class DescribeIpGroupsResultTypeDef(TypedDict):
    Result: List[WorkspacesIpGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ImportClientBrandingRequestTypeDef(TypedDict):
    ResourceId: str
    DeviceTypeWindows: NotRequired[DefaultImportClientBrandingAttributesTypeDef]
    DeviceTypeOsx: NotRequired[DefaultImportClientBrandingAttributesTypeDef]
    DeviceTypeAndroid: NotRequired[DefaultImportClientBrandingAttributesTypeDef]
    DeviceTypeIos: NotRequired[IosImportClientBrandingAttributesTypeDef]
    DeviceTypeLinux: NotRequired[DefaultImportClientBrandingAttributesTypeDef]
    DeviceTypeWeb: NotRequired[DefaultImportClientBrandingAttributesTypeDef]

class DescribeClientPropertiesResultTypeDef(TypedDict):
    ClientPropertiesList: List[ClientPropertiesResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConnectionAliasesResultTypeDef(TypedDict):
    ConnectionAliases: List[ConnectionAliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class FailedCreateStandbyWorkspacesRequestTypeDef(TypedDict):
    StandbyWorkspaceRequest: NotRequired[StandbyWorkspaceOutputTypeDef]
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]

StandbyWorkspaceUnionTypeDef = Union[StandbyWorkspaceTypeDef, StandbyWorkspaceOutputTypeDef]

class CreateWorkspaceBundleResultTypeDef(TypedDict):
    WorkspaceBundle: WorkspaceBundleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorkspaceBundlesResultTypeDef(TypedDict):
    Bundles: List[WorkspaceBundleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class WorkspaceRequestOutputTypeDef(TypedDict):
    DirectoryId: str
    UserName: str
    BundleId: str
    VolumeEncryptionKey: NotRequired[str]
    UserVolumeEncryptionEnabled: NotRequired[bool]
    RootVolumeEncryptionEnabled: NotRequired[bool]
    WorkspaceProperties: NotRequired[WorkspacePropertiesOutputTypeDef]
    Tags: NotRequired[List[TagTypeDef]]
    WorkspaceName: NotRequired[str]

class WorkspaceTypeDef(TypedDict):
    WorkspaceId: NotRequired[str]
    DirectoryId: NotRequired[str]
    UserName: NotRequired[str]
    IpAddress: NotRequired[str]
    State: NotRequired[WorkspaceStateType]
    BundleId: NotRequired[str]
    SubnetId: NotRequired[str]
    ErrorMessage: NotRequired[str]
    ErrorCode: NotRequired[str]
    ComputerName: NotRequired[str]
    VolumeEncryptionKey: NotRequired[str]
    UserVolumeEncryptionEnabled: NotRequired[bool]
    RootVolumeEncryptionEnabled: NotRequired[bool]
    WorkspaceName: NotRequired[str]
    WorkspaceProperties: NotRequired[WorkspacePropertiesOutputTypeDef]
    ModificationStates: NotRequired[List[ModificationStateTypeDef]]
    RelatedWorkspaces: NotRequired[List[RelatedWorkspacePropertiesTypeDef]]
    DataReplicationSettings: NotRequired[DataReplicationSettingsTypeDef]
    StandbyWorkspacesProperties: NotRequired[List[StandbyWorkspacesPropertiesTypeDef]]

WorkspacePropertiesUnionTypeDef = Union[
    WorkspacePropertiesTypeDef, WorkspacePropertiesOutputTypeDef
]

class DescribeWorkspacesPoolSessionsResultTypeDef(TypedDict):
    Sessions: List[WorkspacesPoolSessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class WorkspaceDirectoryTypeDef(TypedDict):
    DirectoryId: NotRequired[str]
    Alias: NotRequired[str]
    DirectoryName: NotRequired[str]
    RegistrationCode: NotRequired[str]
    SubnetIds: NotRequired[List[str]]
    DnsIpAddresses: NotRequired[List[str]]
    CustomerUserName: NotRequired[str]
    IamRoleId: NotRequired[str]
    DirectoryType: NotRequired[WorkspaceDirectoryTypeType]
    WorkspaceSecurityGroupId: NotRequired[str]
    State: NotRequired[WorkspaceDirectoryStateType]
    WorkspaceCreationProperties: NotRequired[DefaultWorkspaceCreationPropertiesTypeDef]
    ipGroupIds: NotRequired[List[str]]
    WorkspaceAccessProperties: NotRequired[WorkspaceAccessPropertiesTypeDef]
    Tenancy: NotRequired[TenancyType]
    SelfservicePermissions: NotRequired[SelfservicePermissionsTypeDef]
    SamlProperties: NotRequired[SamlPropertiesTypeDef]
    CertificateBasedAuthProperties: NotRequired[CertificateBasedAuthPropertiesTypeDef]
    EndpointEncryptionMode: NotRequired[EndpointEncryptionModeType]
    MicrosoftEntraConfig: NotRequired[MicrosoftEntraConfigTypeDef]
    WorkspaceDirectoryName: NotRequired[str]
    WorkspaceDirectoryDescription: NotRequired[str]
    UserIdentityType: NotRequired[UserIdentityTypeType]
    WorkspaceType: NotRequired[WorkspaceTypeType]
    IDCConfig: NotRequired[IDCConfigTypeDef]
    ActiveDirectoryConfig: NotRequired[ActiveDirectoryConfigTypeDef]
    StreamingProperties: NotRequired[StreamingPropertiesOutputTypeDef]
    ErrorMessage: NotRequired[str]

StreamingPropertiesUnionTypeDef = Union[
    StreamingPropertiesTypeDef, StreamingPropertiesOutputTypeDef
]

class DescribeWorkspaceImagesResultTypeDef(TypedDict):
    Images: List[WorkspaceImageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateWorkspacesPoolResultTypeDef(TypedDict):
    WorkspacesPool: WorkspacesPoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorkspacesPoolsResultTypeDef(TypedDict):
    WorkspacesPools: List[WorkspacesPoolTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateWorkspacesPoolResultTypeDef(TypedDict):
    WorkspacesPool: WorkspacesPoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeployWorkspaceApplicationsResultTypeDef(TypedDict):
    Deployment: WorkSpaceApplicationDeploymentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStandbyWorkspacesResultTypeDef(TypedDict):
    FailedStandbyRequests: List[FailedCreateStandbyWorkspacesRequestTypeDef]
    PendingStandbyRequests: List[PendingCreateStandbyWorkspacesRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStandbyWorkspacesRequestTypeDef(TypedDict):
    PrimaryRegion: str
    StandbyWorkspaces: Sequence[StandbyWorkspaceUnionTypeDef]

class FailedCreateWorkspaceRequestTypeDef(TypedDict):
    WorkspaceRequest: NotRequired[WorkspaceRequestOutputTypeDef]
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]

class DescribeWorkspacesResultTypeDef(TypedDict):
    Workspaces: List[WorkspaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ModifyWorkspacePropertiesRequestTypeDef(TypedDict):
    WorkspaceId: str
    WorkspaceProperties: NotRequired[WorkspacePropertiesUnionTypeDef]
    DataReplication: NotRequired[DataReplicationType]

class WorkspaceRequestTypeDef(TypedDict):
    DirectoryId: str
    UserName: str
    BundleId: str
    VolumeEncryptionKey: NotRequired[str]
    UserVolumeEncryptionEnabled: NotRequired[bool]
    RootVolumeEncryptionEnabled: NotRequired[bool]
    WorkspaceProperties: NotRequired[WorkspacePropertiesUnionTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]
    WorkspaceName: NotRequired[str]

class DescribeWorkspaceDirectoriesResultTypeDef(TypedDict):
    Directories: List[WorkspaceDirectoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ModifyStreamingPropertiesRequestTypeDef(TypedDict):
    ResourceId: str
    StreamingProperties: NotRequired[StreamingPropertiesUnionTypeDef]

class CreateWorkspacesResultTypeDef(TypedDict):
    FailedRequests: List[FailedCreateWorkspaceRequestTypeDef]
    PendingRequests: List[WorkspaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

WorkspaceRequestUnionTypeDef = Union[WorkspaceRequestTypeDef, WorkspaceRequestOutputTypeDef]

class CreateWorkspacesRequestTypeDef(TypedDict):
    Workspaces: Sequence[WorkspaceRequestUnionTypeDef]
