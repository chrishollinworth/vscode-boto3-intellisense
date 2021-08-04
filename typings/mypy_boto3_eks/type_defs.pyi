"""
Type annotations for eks service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/type_defs.html)

Usage::

    ```python
    from mypy_boto3_eks.type_defs import AddonHealthTypeDef

    data: AddonHealthTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AddonIssueCodeType,
    AddonStatusType,
    AMITypesType,
    CapacityTypesType,
    ClusterStatusType,
    ErrorCodeType,
    FargateProfileStatusType,
    LogTypeType,
    NodegroupIssueCodeType,
    NodegroupStatusType,
    ResolveConflictsType,
    TaintEffectType,
    UpdateParamTypeType,
    UpdateStatusType,
    UpdateTypeType,
    configStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AddonHealthTypeDef",
    "AddonInfoTypeDef",
    "AddonIssueTypeDef",
    "AddonTypeDef",
    "AddonVersionInfoTypeDef",
    "AssociateEncryptionConfigRequestRequestTypeDef",
    "AssociateEncryptionConfigResponseTypeDef",
    "AssociateIdentityProviderConfigRequestRequestTypeDef",
    "AssociateIdentityProviderConfigResponseTypeDef",
    "AutoScalingGroupTypeDef",
    "CertificateTypeDef",
    "ClusterTypeDef",
    "CompatibilityTypeDef",
    "CreateAddonRequestRequestTypeDef",
    "CreateAddonResponseTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateFargateProfileRequestRequestTypeDef",
    "CreateFargateProfileResponseTypeDef",
    "CreateNodegroupRequestRequestTypeDef",
    "CreateNodegroupResponseTypeDef",
    "DeleteAddonRequestRequestTypeDef",
    "DeleteAddonResponseTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteFargateProfileRequestRequestTypeDef",
    "DeleteFargateProfileResponseTypeDef",
    "DeleteNodegroupRequestRequestTypeDef",
    "DeleteNodegroupResponseTypeDef",
    "DescribeAddonRequestRequestTypeDef",
    "DescribeAddonResponseTypeDef",
    "DescribeAddonVersionsRequestRequestTypeDef",
    "DescribeAddonVersionsResponseTypeDef",
    "DescribeClusterRequestRequestTypeDef",
    "DescribeClusterResponseTypeDef",
    "DescribeFargateProfileRequestRequestTypeDef",
    "DescribeFargateProfileResponseTypeDef",
    "DescribeIdentityProviderConfigRequestRequestTypeDef",
    "DescribeIdentityProviderConfigResponseTypeDef",
    "DescribeNodegroupRequestRequestTypeDef",
    "DescribeNodegroupResponseTypeDef",
    "DescribeUpdateRequestRequestTypeDef",
    "DescribeUpdateResponseTypeDef",
    "DisassociateIdentityProviderConfigRequestRequestTypeDef",
    "DisassociateIdentityProviderConfigResponseTypeDef",
    "EncryptionConfigTypeDef",
    "ErrorDetailTypeDef",
    "FargateProfileSelectorTypeDef",
    "FargateProfileTypeDef",
    "IdentityProviderConfigResponseTypeDef",
    "IdentityProviderConfigTypeDef",
    "IdentityTypeDef",
    "IssueTypeDef",
    "KubernetesNetworkConfigRequestTypeDef",
    "KubernetesNetworkConfigResponseTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "ListAddonsRequestRequestTypeDef",
    "ListAddonsResponseTypeDef",
    "ListClustersRequestRequestTypeDef",
    "ListClustersResponseTypeDef",
    "ListFargateProfilesRequestRequestTypeDef",
    "ListFargateProfilesResponseTypeDef",
    "ListIdentityProviderConfigsRequestRequestTypeDef",
    "ListIdentityProviderConfigsResponseTypeDef",
    "ListNodegroupsRequestRequestTypeDef",
    "ListNodegroupsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUpdatesRequestRequestTypeDef",
    "ListUpdatesResponseTypeDef",
    "LogSetupTypeDef",
    "LoggingTypeDef",
    "NodegroupHealthTypeDef",
    "NodegroupResourcesTypeDef",
    "NodegroupScalingConfigTypeDef",
    "NodegroupTypeDef",
    "NodegroupUpdateConfigTypeDef",
    "OIDCTypeDef",
    "OidcIdentityProviderConfigRequestTypeDef",
    "OidcIdentityProviderConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ProviderTypeDef",
    "RemoteAccessConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TaintTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAddonRequestRequestTypeDef",
    "UpdateAddonResponseTypeDef",
    "UpdateClusterConfigRequestRequestTypeDef",
    "UpdateClusterConfigResponseTypeDef",
    "UpdateClusterVersionRequestRequestTypeDef",
    "UpdateClusterVersionResponseTypeDef",
    "UpdateLabelsPayloadTypeDef",
    "UpdateNodegroupConfigRequestRequestTypeDef",
    "UpdateNodegroupConfigResponseTypeDef",
    "UpdateNodegroupVersionRequestRequestTypeDef",
    "UpdateNodegroupVersionResponseTypeDef",
    "UpdateParamTypeDef",
    "UpdateTaintsPayloadTypeDef",
    "UpdateTypeDef",
    "VpcConfigRequestTypeDef",
    "VpcConfigResponseTypeDef",
    "WaiterConfigTypeDef",
)

AddonHealthTypeDef = TypedDict(
    "AddonHealthTypeDef",
    {
        "issues": List["AddonIssueTypeDef"],
    },
    total=False,
)

AddonInfoTypeDef = TypedDict(
    "AddonInfoTypeDef",
    {
        "addonName": str,
        "type": str,
        "addonVersions": List["AddonVersionInfoTypeDef"],
    },
    total=False,
)

AddonIssueTypeDef = TypedDict(
    "AddonIssueTypeDef",
    {
        "code": AddonIssueCodeType,
        "message": str,
        "resourceIds": List[str],
    },
    total=False,
)

AddonTypeDef = TypedDict(
    "AddonTypeDef",
    {
        "addonName": str,
        "clusterName": str,
        "status": AddonStatusType,
        "addonVersion": str,
        "health": "AddonHealthTypeDef",
        "addonArn": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "serviceAccountRoleArn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

AddonVersionInfoTypeDef = TypedDict(
    "AddonVersionInfoTypeDef",
    {
        "addonVersion": str,
        "architecture": List[str],
        "compatibilities": List["CompatibilityTypeDef"],
    },
    total=False,
)

_RequiredAssociateEncryptionConfigRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateEncryptionConfigRequestRequestTypeDef",
    {
        "clusterName": str,
        "encryptionConfig": List["EncryptionConfigTypeDef"],
    },
)
_OptionalAssociateEncryptionConfigRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateEncryptionConfigRequestRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)

class AssociateEncryptionConfigRequestRequestTypeDef(
    _RequiredAssociateEncryptionConfigRequestRequestTypeDef,
    _OptionalAssociateEncryptionConfigRequestRequestTypeDef,
):
    pass

AssociateEncryptionConfigResponseTypeDef = TypedDict(
    "AssociateEncryptionConfigResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateIdentityProviderConfigRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateIdentityProviderConfigRequestRequestTypeDef",
    {
        "clusterName": str,
        "oidc": "OidcIdentityProviderConfigRequestTypeDef",
    },
)
_OptionalAssociateIdentityProviderConfigRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateIdentityProviderConfigRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
        "clientRequestToken": str,
    },
    total=False,
)

class AssociateIdentityProviderConfigRequestRequestTypeDef(
    _RequiredAssociateIdentityProviderConfigRequestRequestTypeDef,
    _OptionalAssociateIdentityProviderConfigRequestRequestTypeDef,
):
    pass

AssociateIdentityProviderConfigResponseTypeDef = TypedDict(
    "AssociateIdentityProviderConfigResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AutoScalingGroupTypeDef = TypedDict(
    "AutoScalingGroupTypeDef",
    {
        "name": str,
    },
    total=False,
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "data": str,
    },
    total=False,
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "version": str,
        "endpoint": str,
        "roleArn": str,
        "resourcesVpcConfig": "VpcConfigResponseTypeDef",
        "kubernetesNetworkConfig": "KubernetesNetworkConfigResponseTypeDef",
        "logging": "LoggingTypeDef",
        "identity": "IdentityTypeDef",
        "status": ClusterStatusType,
        "certificateAuthority": "CertificateTypeDef",
        "clientRequestToken": str,
        "platformVersion": str,
        "tags": Dict[str, str],
        "encryptionConfig": List["EncryptionConfigTypeDef"],
    },
    total=False,
)

CompatibilityTypeDef = TypedDict(
    "CompatibilityTypeDef",
    {
        "clusterVersion": str,
        "platformVersions": List[str],
        "defaultVersion": bool,
    },
    total=False,
)

_RequiredCreateAddonRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAddonRequestRequestTypeDef",
    {
        "clusterName": str,
        "addonName": str,
    },
)
_OptionalCreateAddonRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAddonRequestRequestTypeDef",
    {
        "addonVersion": str,
        "serviceAccountRoleArn": str,
        "resolveConflicts": ResolveConflictsType,
        "clientRequestToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateAddonRequestRequestTypeDef(
    _RequiredCreateAddonRequestRequestTypeDef, _OptionalCreateAddonRequestRequestTypeDef
):
    pass

CreateAddonResponseTypeDef = TypedDict(
    "CreateAddonResponseTypeDef",
    {
        "addon": "AddonTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateClusterRequestRequestTypeDef = TypedDict(
    "_RequiredCreateClusterRequestRequestTypeDef",
    {
        "name": str,
        "roleArn": str,
        "resourcesVpcConfig": "VpcConfigRequestTypeDef",
    },
)
_OptionalCreateClusterRequestRequestTypeDef = TypedDict(
    "_OptionalCreateClusterRequestRequestTypeDef",
    {
        "version": str,
        "kubernetesNetworkConfig": "KubernetesNetworkConfigRequestTypeDef",
        "logging": "LoggingTypeDef",
        "clientRequestToken": str,
        "tags": Dict[str, str],
        "encryptionConfig": List["EncryptionConfigTypeDef"],
    },
    total=False,
)

class CreateClusterRequestRequestTypeDef(
    _RequiredCreateClusterRequestRequestTypeDef, _OptionalCreateClusterRequestRequestTypeDef
):
    pass

CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFargateProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFargateProfileRequestRequestTypeDef",
    {
        "fargateProfileName": str,
        "clusterName": str,
        "podExecutionRoleArn": str,
    },
)
_OptionalCreateFargateProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFargateProfileRequestRequestTypeDef",
    {
        "subnets": List[str],
        "selectors": List["FargateProfileSelectorTypeDef"],
        "clientRequestToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateFargateProfileRequestRequestTypeDef(
    _RequiredCreateFargateProfileRequestRequestTypeDef,
    _OptionalCreateFargateProfileRequestRequestTypeDef,
):
    pass

CreateFargateProfileResponseTypeDef = TypedDict(
    "CreateFargateProfileResponseTypeDef",
    {
        "fargateProfile": "FargateProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNodegroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateNodegroupRequestRequestTypeDef",
    {
        "clusterName": str,
        "nodegroupName": str,
        "subnets": List[str],
        "nodeRole": str,
    },
)
_OptionalCreateNodegroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateNodegroupRequestRequestTypeDef",
    {
        "scalingConfig": "NodegroupScalingConfigTypeDef",
        "diskSize": int,
        "instanceTypes": List[str],
        "amiType": AMITypesType,
        "remoteAccess": "RemoteAccessConfigTypeDef",
        "labels": Dict[str, str],
        "taints": List["TaintTypeDef"],
        "tags": Dict[str, str],
        "clientRequestToken": str,
        "launchTemplate": "LaunchTemplateSpecificationTypeDef",
        "updateConfig": "NodegroupUpdateConfigTypeDef",
        "capacityType": CapacityTypesType,
        "version": str,
        "releaseVersion": str,
    },
    total=False,
)

class CreateNodegroupRequestRequestTypeDef(
    _RequiredCreateNodegroupRequestRequestTypeDef, _OptionalCreateNodegroupRequestRequestTypeDef
):
    pass

CreateNodegroupResponseTypeDef = TypedDict(
    "CreateNodegroupResponseTypeDef",
    {
        "nodegroup": "NodegroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAddonRequestRequestTypeDef = TypedDict(
    "DeleteAddonRequestRequestTypeDef",
    {
        "clusterName": str,
        "addonName": str,
    },
)

DeleteAddonResponseTypeDef = TypedDict(
    "DeleteAddonResponseTypeDef",
    {
        "addon": "AddonTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterRequestRequestTypeDef = TypedDict(
    "DeleteClusterRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFargateProfileRequestRequestTypeDef = TypedDict(
    "DeleteFargateProfileRequestRequestTypeDef",
    {
        "clusterName": str,
        "fargateProfileName": str,
    },
)

DeleteFargateProfileResponseTypeDef = TypedDict(
    "DeleteFargateProfileResponseTypeDef",
    {
        "fargateProfile": "FargateProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteNodegroupRequestRequestTypeDef = TypedDict(
    "DeleteNodegroupRequestRequestTypeDef",
    {
        "clusterName": str,
        "nodegroupName": str,
    },
)

DeleteNodegroupResponseTypeDef = TypedDict(
    "DeleteNodegroupResponseTypeDef",
    {
        "nodegroup": "NodegroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAddonRequestRequestTypeDef = TypedDict(
    "DescribeAddonRequestRequestTypeDef",
    {
        "clusterName": str,
        "addonName": str,
    },
)

DescribeAddonResponseTypeDef = TypedDict(
    "DescribeAddonResponseTypeDef",
    {
        "addon": "AddonTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAddonVersionsRequestRequestTypeDef = TypedDict(
    "DescribeAddonVersionsRequestRequestTypeDef",
    {
        "kubernetesVersion": str,
        "maxResults": int,
        "nextToken": str,
        "addonName": str,
    },
    total=False,
)

DescribeAddonVersionsResponseTypeDef = TypedDict(
    "DescribeAddonVersionsResponseTypeDef",
    {
        "addons": List["AddonInfoTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClusterRequestRequestTypeDef = TypedDict(
    "DescribeClusterRequestRequestTypeDef",
    {
        "name": str,
    },
)

DescribeClusterResponseTypeDef = TypedDict(
    "DescribeClusterResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFargateProfileRequestRequestTypeDef = TypedDict(
    "DescribeFargateProfileRequestRequestTypeDef",
    {
        "clusterName": str,
        "fargateProfileName": str,
    },
)

DescribeFargateProfileResponseTypeDef = TypedDict(
    "DescribeFargateProfileResponseTypeDef",
    {
        "fargateProfile": "FargateProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIdentityProviderConfigRequestRequestTypeDef = TypedDict(
    "DescribeIdentityProviderConfigRequestRequestTypeDef",
    {
        "clusterName": str,
        "identityProviderConfig": "IdentityProviderConfigTypeDef",
    },
)

DescribeIdentityProviderConfigResponseTypeDef = TypedDict(
    "DescribeIdentityProviderConfigResponseTypeDef",
    {
        "identityProviderConfig": "IdentityProviderConfigResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNodegroupRequestRequestTypeDef = TypedDict(
    "DescribeNodegroupRequestRequestTypeDef",
    {
        "clusterName": str,
        "nodegroupName": str,
    },
)

DescribeNodegroupResponseTypeDef = TypedDict(
    "DescribeNodegroupResponseTypeDef",
    {
        "nodegroup": "NodegroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeUpdateRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeUpdateRequestRequestTypeDef",
    {
        "name": str,
        "updateId": str,
    },
)
_OptionalDescribeUpdateRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeUpdateRequestRequestTypeDef",
    {
        "nodegroupName": str,
        "addonName": str,
    },
    total=False,
)

class DescribeUpdateRequestRequestTypeDef(
    _RequiredDescribeUpdateRequestRequestTypeDef, _OptionalDescribeUpdateRequestRequestTypeDef
):
    pass

DescribeUpdateResponseTypeDef = TypedDict(
    "DescribeUpdateResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateIdentityProviderConfigRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateIdentityProviderConfigRequestRequestTypeDef",
    {
        "clusterName": str,
        "identityProviderConfig": "IdentityProviderConfigTypeDef",
    },
)
_OptionalDisassociateIdentityProviderConfigRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateIdentityProviderConfigRequestRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)

class DisassociateIdentityProviderConfigRequestRequestTypeDef(
    _RequiredDisassociateIdentityProviderConfigRequestRequestTypeDef,
    _OptionalDisassociateIdentityProviderConfigRequestRequestTypeDef,
):
    pass

DisassociateIdentityProviderConfigResponseTypeDef = TypedDict(
    "DisassociateIdentityProviderConfigResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef",
    {
        "resources": List[str],
        "provider": "ProviderTypeDef",
    },
    total=False,
)

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "errorCode": ErrorCodeType,
        "errorMessage": str,
        "resourceIds": List[str],
    },
    total=False,
)

FargateProfileSelectorTypeDef = TypedDict(
    "FargateProfileSelectorTypeDef",
    {
        "namespace": str,
        "labels": Dict[str, str],
    },
    total=False,
)

FargateProfileTypeDef = TypedDict(
    "FargateProfileTypeDef",
    {
        "fargateProfileName": str,
        "fargateProfileArn": str,
        "clusterName": str,
        "createdAt": datetime,
        "podExecutionRoleArn": str,
        "subnets": List[str],
        "selectors": List["FargateProfileSelectorTypeDef"],
        "status": FargateProfileStatusType,
        "tags": Dict[str, str],
    },
    total=False,
)

IdentityProviderConfigResponseTypeDef = TypedDict(
    "IdentityProviderConfigResponseTypeDef",
    {
        "oidc": "OidcIdentityProviderConfigTypeDef",
    },
    total=False,
)

IdentityProviderConfigTypeDef = TypedDict(
    "IdentityProviderConfigTypeDef",
    {
        "type": str,
        "name": str,
    },
)

IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "oidc": "OIDCTypeDef",
    },
    total=False,
)

IssueTypeDef = TypedDict(
    "IssueTypeDef",
    {
        "code": NodegroupIssueCodeType,
        "message": str,
        "resourceIds": List[str],
    },
    total=False,
)

KubernetesNetworkConfigRequestTypeDef = TypedDict(
    "KubernetesNetworkConfigRequestTypeDef",
    {
        "serviceIpv4Cidr": str,
    },
    total=False,
)

KubernetesNetworkConfigResponseTypeDef = TypedDict(
    "KubernetesNetworkConfigResponseTypeDef",
    {
        "serviceIpv4Cidr": str,
    },
    total=False,
)

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {
        "name": str,
        "version": str,
        "id": str,
    },
    total=False,
)

_RequiredListAddonsRequestRequestTypeDef = TypedDict(
    "_RequiredListAddonsRequestRequestTypeDef",
    {
        "clusterName": str,
    },
)
_OptionalListAddonsRequestRequestTypeDef = TypedDict(
    "_OptionalListAddonsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAddonsRequestRequestTypeDef(
    _RequiredListAddonsRequestRequestTypeDef, _OptionalListAddonsRequestRequestTypeDef
):
    pass

ListAddonsResponseTypeDef = TypedDict(
    "ListAddonsResponseTypeDef",
    {
        "addons": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListClustersRequestRequestTypeDef = TypedDict(
    "ListClustersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListClustersResponseTypeDef = TypedDict(
    "ListClustersResponseTypeDef",
    {
        "clusters": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFargateProfilesRequestRequestTypeDef = TypedDict(
    "_RequiredListFargateProfilesRequestRequestTypeDef",
    {
        "clusterName": str,
    },
)
_OptionalListFargateProfilesRequestRequestTypeDef = TypedDict(
    "_OptionalListFargateProfilesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListFargateProfilesRequestRequestTypeDef(
    _RequiredListFargateProfilesRequestRequestTypeDef,
    _OptionalListFargateProfilesRequestRequestTypeDef,
):
    pass

ListFargateProfilesResponseTypeDef = TypedDict(
    "ListFargateProfilesResponseTypeDef",
    {
        "fargateProfileNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIdentityProviderConfigsRequestRequestTypeDef = TypedDict(
    "_RequiredListIdentityProviderConfigsRequestRequestTypeDef",
    {
        "clusterName": str,
    },
)
_OptionalListIdentityProviderConfigsRequestRequestTypeDef = TypedDict(
    "_OptionalListIdentityProviderConfigsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListIdentityProviderConfigsRequestRequestTypeDef(
    _RequiredListIdentityProviderConfigsRequestRequestTypeDef,
    _OptionalListIdentityProviderConfigsRequestRequestTypeDef,
):
    pass

ListIdentityProviderConfigsResponseTypeDef = TypedDict(
    "ListIdentityProviderConfigsResponseTypeDef",
    {
        "identityProviderConfigs": List["IdentityProviderConfigTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListNodegroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListNodegroupsRequestRequestTypeDef",
    {
        "clusterName": str,
    },
)
_OptionalListNodegroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListNodegroupsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListNodegroupsRequestRequestTypeDef(
    _RequiredListNodegroupsRequestRequestTypeDef, _OptionalListNodegroupsRequestRequestTypeDef
):
    pass

ListNodegroupsResponseTypeDef = TypedDict(
    "ListNodegroupsResponseTypeDef",
    {
        "nodegroups": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUpdatesRequestRequestTypeDef = TypedDict(
    "_RequiredListUpdatesRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalListUpdatesRequestRequestTypeDef = TypedDict(
    "_OptionalListUpdatesRequestRequestTypeDef",
    {
        "nodegroupName": str,
        "addonName": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListUpdatesRequestRequestTypeDef(
    _RequiredListUpdatesRequestRequestTypeDef, _OptionalListUpdatesRequestRequestTypeDef
):
    pass

ListUpdatesResponseTypeDef = TypedDict(
    "ListUpdatesResponseTypeDef",
    {
        "updateIds": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogSetupTypeDef = TypedDict(
    "LogSetupTypeDef",
    {
        "types": List[LogTypeType],
        "enabled": bool,
    },
    total=False,
)

LoggingTypeDef = TypedDict(
    "LoggingTypeDef",
    {
        "clusterLogging": List["LogSetupTypeDef"],
    },
    total=False,
)

NodegroupHealthTypeDef = TypedDict(
    "NodegroupHealthTypeDef",
    {
        "issues": List["IssueTypeDef"],
    },
    total=False,
)

NodegroupResourcesTypeDef = TypedDict(
    "NodegroupResourcesTypeDef",
    {
        "autoScalingGroups": List["AutoScalingGroupTypeDef"],
        "remoteAccessSecurityGroup": str,
    },
    total=False,
)

NodegroupScalingConfigTypeDef = TypedDict(
    "NodegroupScalingConfigTypeDef",
    {
        "minSize": int,
        "maxSize": int,
        "desiredSize": int,
    },
    total=False,
)

NodegroupTypeDef = TypedDict(
    "NodegroupTypeDef",
    {
        "nodegroupName": str,
        "nodegroupArn": str,
        "clusterName": str,
        "version": str,
        "releaseVersion": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "status": NodegroupStatusType,
        "capacityType": CapacityTypesType,
        "scalingConfig": "NodegroupScalingConfigTypeDef",
        "instanceTypes": List[str],
        "subnets": List[str],
        "remoteAccess": "RemoteAccessConfigTypeDef",
        "amiType": AMITypesType,
        "nodeRole": str,
        "labels": Dict[str, str],
        "taints": List["TaintTypeDef"],
        "resources": "NodegroupResourcesTypeDef",
        "diskSize": int,
        "health": "NodegroupHealthTypeDef",
        "updateConfig": "NodegroupUpdateConfigTypeDef",
        "launchTemplate": "LaunchTemplateSpecificationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

NodegroupUpdateConfigTypeDef = TypedDict(
    "NodegroupUpdateConfigTypeDef",
    {
        "maxUnavailable": int,
        "maxUnavailablePercentage": int,
    },
    total=False,
)

OIDCTypeDef = TypedDict(
    "OIDCTypeDef",
    {
        "issuer": str,
    },
    total=False,
)

_RequiredOidcIdentityProviderConfigRequestTypeDef = TypedDict(
    "_RequiredOidcIdentityProviderConfigRequestTypeDef",
    {
        "identityProviderConfigName": str,
        "issuerUrl": str,
        "clientId": str,
    },
)
_OptionalOidcIdentityProviderConfigRequestTypeDef = TypedDict(
    "_OptionalOidcIdentityProviderConfigRequestTypeDef",
    {
        "usernameClaim": str,
        "usernamePrefix": str,
        "groupsClaim": str,
        "groupsPrefix": str,
        "requiredClaims": Dict[str, str],
    },
    total=False,
)

class OidcIdentityProviderConfigRequestTypeDef(
    _RequiredOidcIdentityProviderConfigRequestTypeDef,
    _OptionalOidcIdentityProviderConfigRequestTypeDef,
):
    pass

OidcIdentityProviderConfigTypeDef = TypedDict(
    "OidcIdentityProviderConfigTypeDef",
    {
        "identityProviderConfigName": str,
        "identityProviderConfigArn": str,
        "clusterName": str,
        "issuerUrl": str,
        "clientId": str,
        "usernameClaim": str,
        "usernamePrefix": str,
        "groupsClaim": str,
        "groupsPrefix": str,
        "requiredClaims": Dict[str, str],
        "tags": Dict[str, str],
        "status": configStatusType,
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

ProviderTypeDef = TypedDict(
    "ProviderTypeDef",
    {
        "keyArn": str,
    },
    total=False,
)

RemoteAccessConfigTypeDef = TypedDict(
    "RemoteAccessConfigTypeDef",
    {
        "ec2SshKey": str,
        "sourceSecurityGroups": List[str],
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

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TaintTypeDef = TypedDict(
    "TaintTypeDef",
    {
        "key": str,
        "value": str,
        "effect": TaintEffectType,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateAddonRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAddonRequestRequestTypeDef",
    {
        "clusterName": str,
        "addonName": str,
    },
)
_OptionalUpdateAddonRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAddonRequestRequestTypeDef",
    {
        "addonVersion": str,
        "serviceAccountRoleArn": str,
        "resolveConflicts": ResolveConflictsType,
        "clientRequestToken": str,
    },
    total=False,
)

class UpdateAddonRequestRequestTypeDef(
    _RequiredUpdateAddonRequestRequestTypeDef, _OptionalUpdateAddonRequestRequestTypeDef
):
    pass

UpdateAddonResponseTypeDef = TypedDict(
    "UpdateAddonResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateClusterConfigRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateClusterConfigRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateClusterConfigRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateClusterConfigRequestRequestTypeDef",
    {
        "resourcesVpcConfig": "VpcConfigRequestTypeDef",
        "logging": "LoggingTypeDef",
        "clientRequestToken": str,
    },
    total=False,
)

class UpdateClusterConfigRequestRequestTypeDef(
    _RequiredUpdateClusterConfigRequestRequestTypeDef,
    _OptionalUpdateClusterConfigRequestRequestTypeDef,
):
    pass

UpdateClusterConfigResponseTypeDef = TypedDict(
    "UpdateClusterConfigResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateClusterVersionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateClusterVersionRequestRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)
_OptionalUpdateClusterVersionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateClusterVersionRequestRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)

class UpdateClusterVersionRequestRequestTypeDef(
    _RequiredUpdateClusterVersionRequestRequestTypeDef,
    _OptionalUpdateClusterVersionRequestRequestTypeDef,
):
    pass

UpdateClusterVersionResponseTypeDef = TypedDict(
    "UpdateClusterVersionResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateLabelsPayloadTypeDef = TypedDict(
    "UpdateLabelsPayloadTypeDef",
    {
        "addOrUpdateLabels": Dict[str, str],
        "removeLabels": List[str],
    },
    total=False,
)

_RequiredUpdateNodegroupConfigRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateNodegroupConfigRequestRequestTypeDef",
    {
        "clusterName": str,
        "nodegroupName": str,
    },
)
_OptionalUpdateNodegroupConfigRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateNodegroupConfigRequestRequestTypeDef",
    {
        "labels": "UpdateLabelsPayloadTypeDef",
        "taints": "UpdateTaintsPayloadTypeDef",
        "scalingConfig": "NodegroupScalingConfigTypeDef",
        "updateConfig": "NodegroupUpdateConfigTypeDef",
        "clientRequestToken": str,
    },
    total=False,
)

class UpdateNodegroupConfigRequestRequestTypeDef(
    _RequiredUpdateNodegroupConfigRequestRequestTypeDef,
    _OptionalUpdateNodegroupConfigRequestRequestTypeDef,
):
    pass

UpdateNodegroupConfigResponseTypeDef = TypedDict(
    "UpdateNodegroupConfigResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateNodegroupVersionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateNodegroupVersionRequestRequestTypeDef",
    {
        "clusterName": str,
        "nodegroupName": str,
    },
)
_OptionalUpdateNodegroupVersionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateNodegroupVersionRequestRequestTypeDef",
    {
        "version": str,
        "releaseVersion": str,
        "launchTemplate": "LaunchTemplateSpecificationTypeDef",
        "force": bool,
        "clientRequestToken": str,
    },
    total=False,
)

class UpdateNodegroupVersionRequestRequestTypeDef(
    _RequiredUpdateNodegroupVersionRequestRequestTypeDef,
    _OptionalUpdateNodegroupVersionRequestRequestTypeDef,
):
    pass

UpdateNodegroupVersionResponseTypeDef = TypedDict(
    "UpdateNodegroupVersionResponseTypeDef",
    {
        "update": "UpdateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateParamTypeDef = TypedDict(
    "UpdateParamTypeDef",
    {
        "type": UpdateParamTypeType,
        "value": str,
    },
    total=False,
)

UpdateTaintsPayloadTypeDef = TypedDict(
    "UpdateTaintsPayloadTypeDef",
    {
        "addOrUpdateTaints": List["TaintTypeDef"],
        "removeTaints": List["TaintTypeDef"],
    },
    total=False,
)

UpdateTypeDef = TypedDict(
    "UpdateTypeDef",
    {
        "id": str,
        "status": UpdateStatusType,
        "type": UpdateTypeType,
        "params": List["UpdateParamTypeDef"],
        "createdAt": datetime,
        "errors": List["ErrorDetailTypeDef"],
    },
    total=False,
)

VpcConfigRequestTypeDef = TypedDict(
    "VpcConfigRequestTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
        "publicAccessCidrs": List[str],
    },
    total=False,
)

VpcConfigResponseTypeDef = TypedDict(
    "VpcConfigResponseTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "clusterSecurityGroupId": str,
        "vpcId": str,
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
        "publicAccessCidrs": List[str],
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
