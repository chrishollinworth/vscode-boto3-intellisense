"""
Type annotations for codeconnections service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codeconnections.type_defs import ConnectionTypeDef

    data: ConnectionTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    BlockerStatusType,
    ConnectionStatusType,
    ProviderTypeType,
    PublishDeploymentStatusType,
    RepositorySyncStatusType,
    ResourceSyncStatusType,
    TriggerResourceUpdateOnType,
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
    "ConnectionTypeDef",
    "CreateConnectionInputRequestTypeDef",
    "CreateConnectionOutputTypeDef",
    "CreateHostInputRequestTypeDef",
    "CreateHostOutputTypeDef",
    "CreateRepositoryLinkInputRequestTypeDef",
    "CreateRepositoryLinkOutputTypeDef",
    "CreateSyncConfigurationInputRequestTypeDef",
    "CreateSyncConfigurationOutputTypeDef",
    "DeleteConnectionInputRequestTypeDef",
    "DeleteHostInputRequestTypeDef",
    "DeleteRepositoryLinkInputRequestTypeDef",
    "DeleteSyncConfigurationInputRequestTypeDef",
    "GetConnectionInputRequestTypeDef",
    "GetConnectionOutputTypeDef",
    "GetHostInputRequestTypeDef",
    "GetHostOutputTypeDef",
    "GetRepositoryLinkInputRequestTypeDef",
    "GetRepositoryLinkOutputTypeDef",
    "GetRepositorySyncStatusInputRequestTypeDef",
    "GetRepositorySyncStatusOutputTypeDef",
    "GetResourceSyncStatusInputRequestTypeDef",
    "GetResourceSyncStatusOutputTypeDef",
    "GetSyncBlockerSummaryInputRequestTypeDef",
    "GetSyncBlockerSummaryOutputTypeDef",
    "GetSyncConfigurationInputRequestTypeDef",
    "GetSyncConfigurationOutputTypeDef",
    "HostTypeDef",
    "ListConnectionsInputRequestTypeDef",
    "ListConnectionsOutputTypeDef",
    "ListHostsInputRequestTypeDef",
    "ListHostsOutputTypeDef",
    "ListRepositoryLinksInputRequestTypeDef",
    "ListRepositoryLinksOutputTypeDef",
    "ListRepositorySyncDefinitionsInputRequestTypeDef",
    "ListRepositorySyncDefinitionsOutputTypeDef",
    "ListSyncConfigurationsInputRequestTypeDef",
    "ListSyncConfigurationsOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
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
    "TagResourceInputRequestTypeDef",
    "TagTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateHostInputRequestTypeDef",
    "UpdateRepositoryLinkInputRequestTypeDef",
    "UpdateRepositoryLinkOutputTypeDef",
    "UpdateSyncBlockerInputRequestTypeDef",
    "UpdateSyncBlockerOutputTypeDef",
    "UpdateSyncConfigurationInputRequestTypeDef",
    "UpdateSyncConfigurationOutputTypeDef",
    "VpcConfigurationTypeDef",
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ConnectionName": str,
        "ConnectionArn": str,
        "ProviderType": ProviderTypeType,
        "OwnerAccountId": str,
        "ConnectionStatus": ConnectionStatusType,
        "HostArn": str,
    },
    total=False,
)

_RequiredCreateConnectionInputRequestTypeDef = TypedDict(
    "_RequiredCreateConnectionInputRequestTypeDef",
    {
        "ConnectionName": str,
    },
)
_OptionalCreateConnectionInputRequestTypeDef = TypedDict(
    "_OptionalCreateConnectionInputRequestTypeDef",
    {
        "ProviderType": ProviderTypeType,
        "Tags": List["TagTypeDef"],
        "HostArn": str,
    },
    total=False,
)

class CreateConnectionInputRequestTypeDef(
    _RequiredCreateConnectionInputRequestTypeDef, _OptionalCreateConnectionInputRequestTypeDef
):
    pass

CreateConnectionOutputTypeDef = TypedDict(
    "CreateConnectionOutputTypeDef",
    {
        "ConnectionArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateHostInputRequestTypeDef = TypedDict(
    "_RequiredCreateHostInputRequestTypeDef",
    {
        "Name": str,
        "ProviderType": ProviderTypeType,
        "ProviderEndpoint": str,
    },
)
_OptionalCreateHostInputRequestTypeDef = TypedDict(
    "_OptionalCreateHostInputRequestTypeDef",
    {
        "VpcConfiguration": "VpcConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateHostInputRequestTypeDef(
    _RequiredCreateHostInputRequestTypeDef, _OptionalCreateHostInputRequestTypeDef
):
    pass

CreateHostOutputTypeDef = TypedDict(
    "CreateHostOutputTypeDef",
    {
        "HostArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRepositoryLinkInputRequestTypeDef = TypedDict(
    "_RequiredCreateRepositoryLinkInputRequestTypeDef",
    {
        "ConnectionArn": str,
        "OwnerId": str,
        "RepositoryName": str,
    },
)
_OptionalCreateRepositoryLinkInputRequestTypeDef = TypedDict(
    "_OptionalCreateRepositoryLinkInputRequestTypeDef",
    {
        "EncryptionKeyArn": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateRepositoryLinkInputRequestTypeDef(
    _RequiredCreateRepositoryLinkInputRequestTypeDef,
    _OptionalCreateRepositoryLinkInputRequestTypeDef,
):
    pass

CreateRepositoryLinkOutputTypeDef = TypedDict(
    "CreateRepositoryLinkOutputTypeDef",
    {
        "RepositoryLinkInfo": "RepositoryLinkInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSyncConfigurationInputRequestTypeDef = TypedDict(
    "_RequiredCreateSyncConfigurationInputRequestTypeDef",
    {
        "Branch": str,
        "ConfigFile": str,
        "RepositoryLinkId": str,
        "ResourceName": str,
        "RoleArn": str,
        "SyncType": Literal["CFN_STACK_SYNC"],
    },
)
_OptionalCreateSyncConfigurationInputRequestTypeDef = TypedDict(
    "_OptionalCreateSyncConfigurationInputRequestTypeDef",
    {
        "PublishDeploymentStatus": PublishDeploymentStatusType,
        "TriggerResourceUpdateOn": TriggerResourceUpdateOnType,
    },
    total=False,
)

class CreateSyncConfigurationInputRequestTypeDef(
    _RequiredCreateSyncConfigurationInputRequestTypeDef,
    _OptionalCreateSyncConfigurationInputRequestTypeDef,
):
    pass

CreateSyncConfigurationOutputTypeDef = TypedDict(
    "CreateSyncConfigurationOutputTypeDef",
    {
        "SyncConfiguration": "SyncConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConnectionInputRequestTypeDef = TypedDict(
    "DeleteConnectionInputRequestTypeDef",
    {
        "ConnectionArn": str,
    },
)

DeleteHostInputRequestTypeDef = TypedDict(
    "DeleteHostInputRequestTypeDef",
    {
        "HostArn": str,
    },
)

DeleteRepositoryLinkInputRequestTypeDef = TypedDict(
    "DeleteRepositoryLinkInputRequestTypeDef",
    {
        "RepositoryLinkId": str,
    },
)

DeleteSyncConfigurationInputRequestTypeDef = TypedDict(
    "DeleteSyncConfigurationInputRequestTypeDef",
    {
        "SyncType": Literal["CFN_STACK_SYNC"],
        "ResourceName": str,
    },
)

GetConnectionInputRequestTypeDef = TypedDict(
    "GetConnectionInputRequestTypeDef",
    {
        "ConnectionArn": str,
    },
)

GetConnectionOutputTypeDef = TypedDict(
    "GetConnectionOutputTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHostInputRequestTypeDef = TypedDict(
    "GetHostInputRequestTypeDef",
    {
        "HostArn": str,
    },
)

GetHostOutputTypeDef = TypedDict(
    "GetHostOutputTypeDef",
    {
        "Name": str,
        "Status": str,
        "ProviderType": ProviderTypeType,
        "ProviderEndpoint": str,
        "VpcConfiguration": "VpcConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRepositoryLinkInputRequestTypeDef = TypedDict(
    "GetRepositoryLinkInputRequestTypeDef",
    {
        "RepositoryLinkId": str,
    },
)

GetRepositoryLinkOutputTypeDef = TypedDict(
    "GetRepositoryLinkOutputTypeDef",
    {
        "RepositoryLinkInfo": "RepositoryLinkInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRepositorySyncStatusInputRequestTypeDef = TypedDict(
    "GetRepositorySyncStatusInputRequestTypeDef",
    {
        "Branch": str,
        "RepositoryLinkId": str,
        "SyncType": Literal["CFN_STACK_SYNC"],
    },
)

GetRepositorySyncStatusOutputTypeDef = TypedDict(
    "GetRepositorySyncStatusOutputTypeDef",
    {
        "LatestSync": "RepositorySyncAttemptTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceSyncStatusInputRequestTypeDef = TypedDict(
    "GetResourceSyncStatusInputRequestTypeDef",
    {
        "ResourceName": str,
        "SyncType": Literal["CFN_STACK_SYNC"],
    },
)

GetResourceSyncStatusOutputTypeDef = TypedDict(
    "GetResourceSyncStatusOutputTypeDef",
    {
        "DesiredState": "RevisionTypeDef",
        "LatestSuccessfulSync": "ResourceSyncAttemptTypeDef",
        "LatestSync": "ResourceSyncAttemptTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSyncBlockerSummaryInputRequestTypeDef = TypedDict(
    "GetSyncBlockerSummaryInputRequestTypeDef",
    {
        "SyncType": Literal["CFN_STACK_SYNC"],
        "ResourceName": str,
    },
)

GetSyncBlockerSummaryOutputTypeDef = TypedDict(
    "GetSyncBlockerSummaryOutputTypeDef",
    {
        "SyncBlockerSummary": "SyncBlockerSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSyncConfigurationInputRequestTypeDef = TypedDict(
    "GetSyncConfigurationInputRequestTypeDef",
    {
        "SyncType": Literal["CFN_STACK_SYNC"],
        "ResourceName": str,
    },
)

GetSyncConfigurationOutputTypeDef = TypedDict(
    "GetSyncConfigurationOutputTypeDef",
    {
        "SyncConfiguration": "SyncConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HostTypeDef = TypedDict(
    "HostTypeDef",
    {
        "Name": str,
        "HostArn": str,
        "ProviderType": ProviderTypeType,
        "ProviderEndpoint": str,
        "VpcConfiguration": "VpcConfigurationTypeDef",
        "Status": str,
        "StatusMessage": str,
    },
    total=False,
)

ListConnectionsInputRequestTypeDef = TypedDict(
    "ListConnectionsInputRequestTypeDef",
    {
        "ProviderTypeFilter": ProviderTypeType,
        "HostArnFilter": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListConnectionsOutputTypeDef = TypedDict(
    "ListConnectionsOutputTypeDef",
    {
        "Connections": List["ConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHostsInputRequestTypeDef = TypedDict(
    "ListHostsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListHostsOutputTypeDef = TypedDict(
    "ListHostsOutputTypeDef",
    {
        "Hosts": List["HostTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRepositoryLinksInputRequestTypeDef = TypedDict(
    "ListRepositoryLinksInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListRepositoryLinksOutputTypeDef = TypedDict(
    "ListRepositoryLinksOutputTypeDef",
    {
        "RepositoryLinks": List["RepositoryLinkInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRepositorySyncDefinitionsInputRequestTypeDef = TypedDict(
    "ListRepositorySyncDefinitionsInputRequestTypeDef",
    {
        "RepositoryLinkId": str,
        "SyncType": Literal["CFN_STACK_SYNC"],
    },
)

ListRepositorySyncDefinitionsOutputTypeDef = TypedDict(
    "ListRepositorySyncDefinitionsOutputTypeDef",
    {
        "RepositorySyncDefinitions": List["RepositorySyncDefinitionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSyncConfigurationsInputRequestTypeDef = TypedDict(
    "_RequiredListSyncConfigurationsInputRequestTypeDef",
    {
        "RepositoryLinkId": str,
        "SyncType": Literal["CFN_STACK_SYNC"],
    },
)
_OptionalListSyncConfigurationsInputRequestTypeDef = TypedDict(
    "_OptionalListSyncConfigurationsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListSyncConfigurationsInputRequestTypeDef(
    _RequiredListSyncConfigurationsInputRequestTypeDef,
    _OptionalListSyncConfigurationsInputRequestTypeDef,
):
    pass

ListSyncConfigurationsOutputTypeDef = TypedDict(
    "ListSyncConfigurationsOutputTypeDef",
    {
        "SyncConfigurations": List["SyncConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRepositoryLinkInfoTypeDef = TypedDict(
    "_RequiredRepositoryLinkInfoTypeDef",
    {
        "ConnectionArn": str,
        "OwnerId": str,
        "ProviderType": ProviderTypeType,
        "RepositoryLinkArn": str,
        "RepositoryLinkId": str,
        "RepositoryName": str,
    },
)
_OptionalRepositoryLinkInfoTypeDef = TypedDict(
    "_OptionalRepositoryLinkInfoTypeDef",
    {
        "EncryptionKeyArn": str,
    },
    total=False,
)

class RepositoryLinkInfoTypeDef(
    _RequiredRepositoryLinkInfoTypeDef, _OptionalRepositoryLinkInfoTypeDef
):
    pass

RepositorySyncAttemptTypeDef = TypedDict(
    "RepositorySyncAttemptTypeDef",
    {
        "StartedAt": datetime,
        "Status": RepositorySyncStatusType,
        "Events": List["RepositorySyncEventTypeDef"],
    },
)

RepositorySyncDefinitionTypeDef = TypedDict(
    "RepositorySyncDefinitionTypeDef",
    {
        "Branch": str,
        "Directory": str,
        "Parent": str,
        "Target": str,
    },
)

_RequiredRepositorySyncEventTypeDef = TypedDict(
    "_RequiredRepositorySyncEventTypeDef",
    {
        "Event": str,
        "Time": datetime,
        "Type": str,
    },
)
_OptionalRepositorySyncEventTypeDef = TypedDict(
    "_OptionalRepositorySyncEventTypeDef",
    {
        "ExternalId": str,
    },
    total=False,
)

class RepositorySyncEventTypeDef(
    _RequiredRepositorySyncEventTypeDef, _OptionalRepositorySyncEventTypeDef
):
    pass

ResourceSyncAttemptTypeDef = TypedDict(
    "ResourceSyncAttemptTypeDef",
    {
        "Events": List["ResourceSyncEventTypeDef"],
        "InitialRevision": "RevisionTypeDef",
        "StartedAt": datetime,
        "Status": ResourceSyncStatusType,
        "TargetRevision": "RevisionTypeDef",
        "Target": str,
    },
)

_RequiredResourceSyncEventTypeDef = TypedDict(
    "_RequiredResourceSyncEventTypeDef",
    {
        "Event": str,
        "Time": datetime,
        "Type": str,
    },
)
_OptionalResourceSyncEventTypeDef = TypedDict(
    "_OptionalResourceSyncEventTypeDef",
    {
        "ExternalId": str,
    },
    total=False,
)

class ResourceSyncEventTypeDef(
    _RequiredResourceSyncEventTypeDef, _OptionalResourceSyncEventTypeDef
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

RevisionTypeDef = TypedDict(
    "RevisionTypeDef",
    {
        "Branch": str,
        "Directory": str,
        "OwnerId": str,
        "RepositoryName": str,
        "ProviderType": ProviderTypeType,
        "Sha": str,
    },
)

SyncBlockerContextTypeDef = TypedDict(
    "SyncBlockerContextTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

_RequiredSyncBlockerSummaryTypeDef = TypedDict(
    "_RequiredSyncBlockerSummaryTypeDef",
    {
        "ResourceName": str,
    },
)
_OptionalSyncBlockerSummaryTypeDef = TypedDict(
    "_OptionalSyncBlockerSummaryTypeDef",
    {
        "ParentResourceName": str,
        "LatestBlockers": List["SyncBlockerTypeDef"],
    },
    total=False,
)

class SyncBlockerSummaryTypeDef(
    _RequiredSyncBlockerSummaryTypeDef, _OptionalSyncBlockerSummaryTypeDef
):
    pass

_RequiredSyncBlockerTypeDef = TypedDict(
    "_RequiredSyncBlockerTypeDef",
    {
        "Id": str,
        "Type": Literal["AUTOMATED"],
        "Status": BlockerStatusType,
        "CreatedReason": str,
        "CreatedAt": datetime,
    },
)
_OptionalSyncBlockerTypeDef = TypedDict(
    "_OptionalSyncBlockerTypeDef",
    {
        "Contexts": List["SyncBlockerContextTypeDef"],
        "ResolvedReason": str,
        "ResolvedAt": datetime,
    },
    total=False,
)

class SyncBlockerTypeDef(_RequiredSyncBlockerTypeDef, _OptionalSyncBlockerTypeDef):
    pass

_RequiredSyncConfigurationTypeDef = TypedDict(
    "_RequiredSyncConfigurationTypeDef",
    {
        "Branch": str,
        "OwnerId": str,
        "ProviderType": ProviderTypeType,
        "RepositoryLinkId": str,
        "RepositoryName": str,
        "ResourceName": str,
        "RoleArn": str,
        "SyncType": Literal["CFN_STACK_SYNC"],
    },
)
_OptionalSyncConfigurationTypeDef = TypedDict(
    "_OptionalSyncConfigurationTypeDef",
    {
        "ConfigFile": str,
        "PublishDeploymentStatus": PublishDeploymentStatusType,
        "TriggerResourceUpdateOn": TriggerResourceUpdateOnType,
    },
    total=False,
)

class SyncConfigurationTypeDef(
    _RequiredSyncConfigurationTypeDef, _OptionalSyncConfigurationTypeDef
):
    pass

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateHostInputRequestTypeDef = TypedDict(
    "_RequiredUpdateHostInputRequestTypeDef",
    {
        "HostArn": str,
    },
)
_OptionalUpdateHostInputRequestTypeDef = TypedDict(
    "_OptionalUpdateHostInputRequestTypeDef",
    {
        "ProviderEndpoint": str,
        "VpcConfiguration": "VpcConfigurationTypeDef",
    },
    total=False,
)

class UpdateHostInputRequestTypeDef(
    _RequiredUpdateHostInputRequestTypeDef, _OptionalUpdateHostInputRequestTypeDef
):
    pass

_RequiredUpdateRepositoryLinkInputRequestTypeDef = TypedDict(
    "_RequiredUpdateRepositoryLinkInputRequestTypeDef",
    {
        "RepositoryLinkId": str,
    },
)
_OptionalUpdateRepositoryLinkInputRequestTypeDef = TypedDict(
    "_OptionalUpdateRepositoryLinkInputRequestTypeDef",
    {
        "ConnectionArn": str,
        "EncryptionKeyArn": str,
    },
    total=False,
)

class UpdateRepositoryLinkInputRequestTypeDef(
    _RequiredUpdateRepositoryLinkInputRequestTypeDef,
    _OptionalUpdateRepositoryLinkInputRequestTypeDef,
):
    pass

UpdateRepositoryLinkOutputTypeDef = TypedDict(
    "UpdateRepositoryLinkOutputTypeDef",
    {
        "RepositoryLinkInfo": "RepositoryLinkInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSyncBlockerInputRequestTypeDef = TypedDict(
    "UpdateSyncBlockerInputRequestTypeDef",
    {
        "Id": str,
        "SyncType": Literal["CFN_STACK_SYNC"],
        "ResourceName": str,
        "ResolvedReason": str,
    },
)

UpdateSyncBlockerOutputTypeDef = TypedDict(
    "UpdateSyncBlockerOutputTypeDef",
    {
        "ResourceName": str,
        "ParentResourceName": str,
        "SyncBlocker": "SyncBlockerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSyncConfigurationInputRequestTypeDef = TypedDict(
    "_RequiredUpdateSyncConfigurationInputRequestTypeDef",
    {
        "ResourceName": str,
        "SyncType": Literal["CFN_STACK_SYNC"],
    },
)
_OptionalUpdateSyncConfigurationInputRequestTypeDef = TypedDict(
    "_OptionalUpdateSyncConfigurationInputRequestTypeDef",
    {
        "Branch": str,
        "ConfigFile": str,
        "RepositoryLinkId": str,
        "RoleArn": str,
        "PublishDeploymentStatus": PublishDeploymentStatusType,
        "TriggerResourceUpdateOn": TriggerResourceUpdateOnType,
    },
    total=False,
)

class UpdateSyncConfigurationInputRequestTypeDef(
    _RequiredUpdateSyncConfigurationInputRequestTypeDef,
    _OptionalUpdateSyncConfigurationInputRequestTypeDef,
):
    pass

UpdateSyncConfigurationOutputTypeDef = TypedDict(
    "UpdateSyncConfigurationOutputTypeDef",
    {
        "SyncConfiguration": "SyncConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredVpcConfigurationTypeDef = TypedDict(
    "_RequiredVpcConfigurationTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
    },
)
_OptionalVpcConfigurationTypeDef = TypedDict(
    "_OptionalVpcConfigurationTypeDef",
    {
        "TlsCertificate": str,
    },
    total=False,
)

class VpcConfigurationTypeDef(_RequiredVpcConfigurationTypeDef, _OptionalVpcConfigurationTypeDef):
    pass
