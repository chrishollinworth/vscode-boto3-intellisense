"""
Type annotations for codestar-connections service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_codestar_connections.type_defs import ConnectionTypeDef

    data: ConnectionTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    BlockerStatusType,
    ConnectionStatusType,
    ProviderTypeType,
    PublishDeploymentStatusType,
    RepositorySyncStatusType,
    ResourceSyncStatusType,
    TriggerResourceUpdateOnType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "ConnectionTypeDef",
    "CreateConnectionInputTypeDef",
    "CreateConnectionOutputTypeDef",
    "CreateHostInputTypeDef",
    "CreateHostOutputTypeDef",
    "CreateRepositoryLinkInputTypeDef",
    "CreateRepositoryLinkOutputTypeDef",
    "CreateSyncConfigurationInputTypeDef",
    "CreateSyncConfigurationOutputTypeDef",
    "DeleteConnectionInputTypeDef",
    "DeleteHostInputTypeDef",
    "DeleteRepositoryLinkInputTypeDef",
    "DeleteSyncConfigurationInputTypeDef",
    "GetConnectionInputTypeDef",
    "GetConnectionOutputTypeDef",
    "GetHostInputTypeDef",
    "GetHostOutputTypeDef",
    "GetRepositoryLinkInputTypeDef",
    "GetRepositoryLinkOutputTypeDef",
    "GetRepositorySyncStatusInputTypeDef",
    "GetRepositorySyncStatusOutputTypeDef",
    "GetResourceSyncStatusInputTypeDef",
    "GetResourceSyncStatusOutputTypeDef",
    "GetSyncBlockerSummaryInputTypeDef",
    "GetSyncBlockerSummaryOutputTypeDef",
    "GetSyncConfigurationInputTypeDef",
    "GetSyncConfigurationOutputTypeDef",
    "HostTypeDef",
    "ListConnectionsInputTypeDef",
    "ListConnectionsOutputTypeDef",
    "ListHostsInputTypeDef",
    "ListHostsOutputTypeDef",
    "ListRepositoryLinksInputTypeDef",
    "ListRepositoryLinksOutputTypeDef",
    "ListRepositorySyncDefinitionsInputTypeDef",
    "ListRepositorySyncDefinitionsOutputTypeDef",
    "ListSyncConfigurationsInputTypeDef",
    "ListSyncConfigurationsOutputTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "RepositoryLinkInfoTypeDef",
    "RepositorySyncAttemptTypeDef",
    "RepositorySyncDefinitionTypeDef",
    "RepositorySyncEventTypeDef",
    "ResourceSyncAttemptTypeDef",
    "ResourceSyncEventTypeDef",
    "ResponseMetadataTypeDef",
    "RevisionTypeDef",
    "SyncBlockerContextTypeDef",
    "SyncBlockerSummaryTypeDef",
    "SyncBlockerTypeDef",
    "SyncConfigurationTypeDef",
    "TagResourceInputTypeDef",
    "TagTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateHostInputTypeDef",
    "UpdateRepositoryLinkInputTypeDef",
    "UpdateRepositoryLinkOutputTypeDef",
    "UpdateSyncBlockerInputTypeDef",
    "UpdateSyncBlockerOutputTypeDef",
    "UpdateSyncConfigurationInputTypeDef",
    "UpdateSyncConfigurationOutputTypeDef",
    "VpcConfigurationOutputTypeDef",
    "VpcConfigurationTypeDef",
    "VpcConfigurationUnionTypeDef",
)

class ConnectionTypeDef(TypedDict):
    ConnectionName: NotRequired[str]
    ConnectionArn: NotRequired[str]
    ProviderType: NotRequired[ProviderTypeType]
    OwnerAccountId: NotRequired[str]
    ConnectionStatus: NotRequired[ConnectionStatusType]
    HostArn: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class RepositoryLinkInfoTypeDef(TypedDict):
    ConnectionArn: str
    OwnerId: str
    ProviderType: ProviderTypeType
    RepositoryLinkArn: str
    RepositoryLinkId: str
    RepositoryName: str
    EncryptionKeyArn: NotRequired[str]

class CreateSyncConfigurationInputTypeDef(TypedDict):
    Branch: str
    ConfigFile: str
    RepositoryLinkId: str
    ResourceName: str
    RoleArn: str
    SyncType: Literal["CFN_STACK_SYNC"]
    PublishDeploymentStatus: NotRequired[PublishDeploymentStatusType]
    TriggerResourceUpdateOn: NotRequired[TriggerResourceUpdateOnType]

class SyncConfigurationTypeDef(TypedDict):
    Branch: str
    OwnerId: str
    ProviderType: ProviderTypeType
    RepositoryLinkId: str
    RepositoryName: str
    ResourceName: str
    RoleArn: str
    SyncType: Literal["CFN_STACK_SYNC"]
    ConfigFile: NotRequired[str]
    PublishDeploymentStatus: NotRequired[PublishDeploymentStatusType]
    TriggerResourceUpdateOn: NotRequired[TriggerResourceUpdateOnType]

class DeleteConnectionInputTypeDef(TypedDict):
    ConnectionArn: str

class DeleteHostInputTypeDef(TypedDict):
    HostArn: str

class DeleteRepositoryLinkInputTypeDef(TypedDict):
    RepositoryLinkId: str

class DeleteSyncConfigurationInputTypeDef(TypedDict):
    SyncType: Literal["CFN_STACK_SYNC"]
    ResourceName: str

class GetConnectionInputTypeDef(TypedDict):
    ConnectionArn: str

class GetHostInputTypeDef(TypedDict):
    HostArn: str

class VpcConfigurationOutputTypeDef(TypedDict):
    VpcId: str
    SubnetIds: List[str]
    SecurityGroupIds: List[str]
    TlsCertificate: NotRequired[str]

class GetRepositoryLinkInputTypeDef(TypedDict):
    RepositoryLinkId: str

class GetRepositorySyncStatusInputTypeDef(TypedDict):
    Branch: str
    RepositoryLinkId: str
    SyncType: Literal["CFN_STACK_SYNC"]

class GetResourceSyncStatusInputTypeDef(TypedDict):
    ResourceName: str
    SyncType: Literal["CFN_STACK_SYNC"]

class RevisionTypeDef(TypedDict):
    Branch: str
    Directory: str
    OwnerId: str
    RepositoryName: str
    ProviderType: ProviderTypeType
    Sha: str

class GetSyncBlockerSummaryInputTypeDef(TypedDict):
    SyncType: Literal["CFN_STACK_SYNC"]
    ResourceName: str

class GetSyncConfigurationInputTypeDef(TypedDict):
    SyncType: Literal["CFN_STACK_SYNC"]
    ResourceName: str

class ListConnectionsInputTypeDef(TypedDict):
    ProviderTypeFilter: NotRequired[ProviderTypeType]
    HostArnFilter: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListHostsInputTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListRepositoryLinksInputTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListRepositorySyncDefinitionsInputTypeDef(TypedDict):
    RepositoryLinkId: str
    SyncType: Literal["CFN_STACK_SYNC"]

class RepositorySyncDefinitionTypeDef(TypedDict):
    Branch: str
    Directory: str
    Parent: str
    Target: str

class ListSyncConfigurationsInputTypeDef(TypedDict):
    RepositoryLinkId: str
    SyncType: Literal["CFN_STACK_SYNC"]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListTagsForResourceInputTypeDef(TypedDict):
    ResourceArn: str

RepositorySyncEventTypeDef = TypedDict(
    "RepositorySyncEventTypeDef",
    {
        "Event": str,
        "Time": datetime,
        "Type": str,
        "ExternalId": NotRequired[str],
    },
)
ResourceSyncEventTypeDef = TypedDict(
    "ResourceSyncEventTypeDef",
    {
        "Event": str,
        "Time": datetime,
        "Type": str,
        "ExternalId": NotRequired[str],
    },
)

class SyncBlockerContextTypeDef(TypedDict):
    Key: str
    Value: str

class UntagResourceInputTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateRepositoryLinkInputTypeDef(TypedDict):
    RepositoryLinkId: str
    ConnectionArn: NotRequired[str]
    EncryptionKeyArn: NotRequired[str]

class UpdateSyncBlockerInputTypeDef(TypedDict):
    Id: str
    SyncType: Literal["CFN_STACK_SYNC"]
    ResourceName: str
    ResolvedReason: str

class UpdateSyncConfigurationInputTypeDef(TypedDict):
    ResourceName: str
    SyncType: Literal["CFN_STACK_SYNC"]
    Branch: NotRequired[str]
    ConfigFile: NotRequired[str]
    RepositoryLinkId: NotRequired[str]
    RoleArn: NotRequired[str]
    PublishDeploymentStatus: NotRequired[PublishDeploymentStatusType]
    TriggerResourceUpdateOn: NotRequired[TriggerResourceUpdateOnType]

class VpcConfigurationTypeDef(TypedDict):
    VpcId: str
    SubnetIds: Sequence[str]
    SecurityGroupIds: Sequence[str]
    TlsCertificate: NotRequired[str]

class CreateConnectionInputTypeDef(TypedDict):
    ConnectionName: str
    ProviderType: NotRequired[ProviderTypeType]
    Tags: NotRequired[Sequence[TagTypeDef]]
    HostArn: NotRequired[str]

class CreateRepositoryLinkInputTypeDef(TypedDict):
    ConnectionArn: str
    OwnerId: str
    RepositoryName: str
    EncryptionKeyArn: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class TagResourceInputTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateConnectionOutputTypeDef(TypedDict):
    ConnectionArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHostOutputTypeDef(TypedDict):
    HostArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectionOutputTypeDef(TypedDict):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConnectionsOutputTypeDef(TypedDict):
    Connections: List[ConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceOutputTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRepositoryLinkOutputTypeDef(TypedDict):
    RepositoryLinkInfo: RepositoryLinkInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRepositoryLinkOutputTypeDef(TypedDict):
    RepositoryLinkInfo: RepositoryLinkInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRepositoryLinksOutputTypeDef(TypedDict):
    RepositoryLinks: List[RepositoryLinkInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateRepositoryLinkOutputTypeDef(TypedDict):
    RepositoryLinkInfo: RepositoryLinkInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSyncConfigurationOutputTypeDef(TypedDict):
    SyncConfiguration: SyncConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSyncConfigurationOutputTypeDef(TypedDict):
    SyncConfiguration: SyncConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSyncConfigurationsOutputTypeDef(TypedDict):
    SyncConfigurations: List[SyncConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateSyncConfigurationOutputTypeDef(TypedDict):
    SyncConfiguration: SyncConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetHostOutputTypeDef(TypedDict):
    Name: str
    Status: str
    ProviderType: ProviderTypeType
    ProviderEndpoint: str
    VpcConfiguration: VpcConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class HostTypeDef(TypedDict):
    Name: NotRequired[str]
    HostArn: NotRequired[str]
    ProviderType: NotRequired[ProviderTypeType]
    ProviderEndpoint: NotRequired[str]
    VpcConfiguration: NotRequired[VpcConfigurationOutputTypeDef]
    Status: NotRequired[str]
    StatusMessage: NotRequired[str]

class ListRepositorySyncDefinitionsOutputTypeDef(TypedDict):
    RepositorySyncDefinitions: List[RepositorySyncDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class RepositorySyncAttemptTypeDef(TypedDict):
    StartedAt: datetime
    Status: RepositorySyncStatusType
    Events: List[RepositorySyncEventTypeDef]

class ResourceSyncAttemptTypeDef(TypedDict):
    Events: List[ResourceSyncEventTypeDef]
    InitialRevision: RevisionTypeDef
    StartedAt: datetime
    Status: ResourceSyncStatusType
    TargetRevision: RevisionTypeDef
    Target: str

SyncBlockerTypeDef = TypedDict(
    "SyncBlockerTypeDef",
    {
        "Id": str,
        "Type": Literal["AUTOMATED"],
        "Status": BlockerStatusType,
        "CreatedReason": str,
        "CreatedAt": datetime,
        "Contexts": NotRequired[List[SyncBlockerContextTypeDef]],
        "ResolvedReason": NotRequired[str],
        "ResolvedAt": NotRequired[datetime],
    },
)
VpcConfigurationUnionTypeDef = Union[VpcConfigurationTypeDef, VpcConfigurationOutputTypeDef]

class ListHostsOutputTypeDef(TypedDict):
    Hosts: List[HostTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetRepositorySyncStatusOutputTypeDef(TypedDict):
    LatestSync: RepositorySyncAttemptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceSyncStatusOutputTypeDef(TypedDict):
    DesiredState: RevisionTypeDef
    LatestSuccessfulSync: ResourceSyncAttemptTypeDef
    LatestSync: ResourceSyncAttemptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SyncBlockerSummaryTypeDef(TypedDict):
    ResourceName: str
    ParentResourceName: NotRequired[str]
    LatestBlockers: NotRequired[List[SyncBlockerTypeDef]]

class UpdateSyncBlockerOutputTypeDef(TypedDict):
    ResourceName: str
    ParentResourceName: str
    SyncBlocker: SyncBlockerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHostInputTypeDef(TypedDict):
    Name: str
    ProviderType: ProviderTypeType
    ProviderEndpoint: str
    VpcConfiguration: NotRequired[VpcConfigurationUnionTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]

class UpdateHostInputTypeDef(TypedDict):
    HostArn: str
    ProviderEndpoint: NotRequired[str]
    VpcConfiguration: NotRequired[VpcConfigurationUnionTypeDef]

class GetSyncBlockerSummaryOutputTypeDef(TypedDict):
    SyncBlockerSummary: SyncBlockerSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
