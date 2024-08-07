"""
Type annotations for eks service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/type_defs.html)

Usage::

    ```python
    from mypy_boto3_eks.type_defs import AccessConfigResponseTypeDef

    data: AccessConfigResponseTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AccessScopeTypeType,
    AddonIssueCodeType,
    AddonStatusType,
    AMITypesType,
    AuthenticationModeType,
    CapacityTypesType,
    ClusterIssueCodeType,
    ClusterStatusType,
    ConnectorConfigProviderType,
    EksAnywhereSubscriptionStatusType,
    ErrorCodeType,
    FargateProfileIssueCodeType,
    FargateProfileStatusType,
    InsightStatusValueType,
    IpFamilyType,
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
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccessConfigResponseTypeDef",
    "AccessEntryTypeDef",
    "AccessPolicyTypeDef",
    "AccessScopeTypeDef",
    "AddonHealthTypeDef",
    "AddonInfoTypeDef",
    "AddonIssueTypeDef",
    "AddonPodIdentityAssociationsTypeDef",
    "AddonPodIdentityConfigurationTypeDef",
    "AddonTypeDef",
    "AddonVersionInfoTypeDef",
    "AssociateAccessPolicyRequestRequestTypeDef",
    "AssociateAccessPolicyResponseTypeDef",
    "AssociateEncryptionConfigRequestRequestTypeDef",
    "AssociateEncryptionConfigResponseTypeDef",
    "AssociateIdentityProviderConfigRequestRequestTypeDef",
    "AssociateIdentityProviderConfigResponseTypeDef",
    "AssociatedAccessPolicyTypeDef",
    "AutoScalingGroupTypeDef",
    "CertificateTypeDef",
    "ClientStatTypeDef",
    "ClusterHealthTypeDef",
    "ClusterIssueTypeDef",
    "ClusterTypeDef",
    "CompatibilityTypeDef",
    "ConnectorConfigRequestTypeDef",
    "ConnectorConfigResponseTypeDef",
    "ControlPlanePlacementRequestTypeDef",
    "ControlPlanePlacementResponseTypeDef",
    "CreateAccessConfigRequestTypeDef",
    "CreateAccessEntryRequestRequestTypeDef",
    "CreateAccessEntryResponseTypeDef",
    "CreateAddonRequestRequestTypeDef",
    "CreateAddonResponseTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateEksAnywhereSubscriptionRequestRequestTypeDef",
    "CreateEksAnywhereSubscriptionResponseTypeDef",
    "CreateFargateProfileRequestRequestTypeDef",
    "CreateFargateProfileResponseTypeDef",
    "CreateNodegroupRequestRequestTypeDef",
    "CreateNodegroupResponseTypeDef",
    "CreatePodIdentityAssociationRequestRequestTypeDef",
    "CreatePodIdentityAssociationResponseTypeDef",
    "DeleteAccessEntryRequestRequestTypeDef",
    "DeleteAddonRequestRequestTypeDef",
    "DeleteAddonResponseTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteEksAnywhereSubscriptionRequestRequestTypeDef",
    "DeleteEksAnywhereSubscriptionResponseTypeDef",
    "DeleteFargateProfileRequestRequestTypeDef",
    "DeleteFargateProfileResponseTypeDef",
    "DeleteNodegroupRequestRequestTypeDef",
    "DeleteNodegroupResponseTypeDef",
    "DeletePodIdentityAssociationRequestRequestTypeDef",
    "DeletePodIdentityAssociationResponseTypeDef",
    "DeprecationDetailTypeDef",
    "DeregisterClusterRequestRequestTypeDef",
    "DeregisterClusterResponseTypeDef",
    "DescribeAccessEntryRequestRequestTypeDef",
    "DescribeAccessEntryResponseTypeDef",
    "DescribeAddonConfigurationRequestRequestTypeDef",
    "DescribeAddonConfigurationResponseTypeDef",
    "DescribeAddonRequestRequestTypeDef",
    "DescribeAddonResponseTypeDef",
    "DescribeAddonVersionsRequestRequestTypeDef",
    "DescribeAddonVersionsResponseTypeDef",
    "DescribeClusterRequestRequestTypeDef",
    "DescribeClusterResponseTypeDef",
    "DescribeEksAnywhereSubscriptionRequestRequestTypeDef",
    "DescribeEksAnywhereSubscriptionResponseTypeDef",
    "DescribeFargateProfileRequestRequestTypeDef",
    "DescribeFargateProfileResponseTypeDef",
    "DescribeIdentityProviderConfigRequestRequestTypeDef",
    "DescribeIdentityProviderConfigResponseTypeDef",
    "DescribeInsightRequestRequestTypeDef",
    "DescribeInsightResponseTypeDef",
    "DescribeNodegroupRequestRequestTypeDef",
    "DescribeNodegroupResponseTypeDef",
    "DescribePodIdentityAssociationRequestRequestTypeDef",
    "DescribePodIdentityAssociationResponseTypeDef",
    "DescribeUpdateRequestRequestTypeDef",
    "DescribeUpdateResponseTypeDef",
    "DisassociateAccessPolicyRequestRequestTypeDef",
    "DisassociateIdentityProviderConfigRequestRequestTypeDef",
    "DisassociateIdentityProviderConfigResponseTypeDef",
    "EksAnywhereSubscriptionTermTypeDef",
    "EksAnywhereSubscriptionTypeDef",
    "EncryptionConfigTypeDef",
    "ErrorDetailTypeDef",
    "FargateProfileHealthTypeDef",
    "FargateProfileIssueTypeDef",
    "FargateProfileSelectorTypeDef",
    "FargateProfileTypeDef",
    "IdentityProviderConfigResponseTypeDef",
    "IdentityProviderConfigTypeDef",
    "IdentityTypeDef",
    "InsightCategorySpecificSummaryTypeDef",
    "InsightResourceDetailTypeDef",
    "InsightStatusTypeDef",
    "InsightSummaryTypeDef",
    "InsightTypeDef",
    "InsightsFilterTypeDef",
    "IssueTypeDef",
    "KubernetesNetworkConfigRequestTypeDef",
    "KubernetesNetworkConfigResponseTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "ListAccessEntriesRequestRequestTypeDef",
    "ListAccessEntriesResponseTypeDef",
    "ListAccessPoliciesRequestRequestTypeDef",
    "ListAccessPoliciesResponseTypeDef",
    "ListAddonsRequestRequestTypeDef",
    "ListAddonsResponseTypeDef",
    "ListAssociatedAccessPoliciesRequestRequestTypeDef",
    "ListAssociatedAccessPoliciesResponseTypeDef",
    "ListClustersRequestRequestTypeDef",
    "ListClustersResponseTypeDef",
    "ListEksAnywhereSubscriptionsRequestRequestTypeDef",
    "ListEksAnywhereSubscriptionsResponseTypeDef",
    "ListFargateProfilesRequestRequestTypeDef",
    "ListFargateProfilesResponseTypeDef",
    "ListIdentityProviderConfigsRequestRequestTypeDef",
    "ListIdentityProviderConfigsResponseTypeDef",
    "ListInsightsRequestRequestTypeDef",
    "ListInsightsResponseTypeDef",
    "ListNodegroupsRequestRequestTypeDef",
    "ListNodegroupsResponseTypeDef",
    "ListPodIdentityAssociationsRequestRequestTypeDef",
    "ListPodIdentityAssociationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUpdatesRequestRequestTypeDef",
    "ListUpdatesResponseTypeDef",
    "LogSetupTypeDef",
    "LoggingTypeDef",
    "MarketplaceInformationTypeDef",
    "NodegroupHealthTypeDef",
    "NodegroupResourcesTypeDef",
    "NodegroupScalingConfigTypeDef",
    "NodegroupTypeDef",
    "NodegroupUpdateConfigTypeDef",
    "OIDCTypeDef",
    "OidcIdentityProviderConfigRequestTypeDef",
    "OidcIdentityProviderConfigTypeDef",
    "OutpostConfigRequestTypeDef",
    "OutpostConfigResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PodIdentityAssociationSummaryTypeDef",
    "PodIdentityAssociationTypeDef",
    "ProviderTypeDef",
    "RegisterClusterRequestRequestTypeDef",
    "RegisterClusterResponseTypeDef",
    "RemoteAccessConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TaintTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccessConfigRequestTypeDef",
    "UpdateAccessEntryRequestRequestTypeDef",
    "UpdateAccessEntryResponseTypeDef",
    "UpdateAddonRequestRequestTypeDef",
    "UpdateAddonResponseTypeDef",
    "UpdateClusterConfigRequestRequestTypeDef",
    "UpdateClusterConfigResponseTypeDef",
    "UpdateClusterVersionRequestRequestTypeDef",
    "UpdateClusterVersionResponseTypeDef",
    "UpdateEksAnywhereSubscriptionRequestRequestTypeDef",
    "UpdateEksAnywhereSubscriptionResponseTypeDef",
    "UpdateLabelsPayloadTypeDef",
    "UpdateNodegroupConfigRequestRequestTypeDef",
    "UpdateNodegroupConfigResponseTypeDef",
    "UpdateNodegroupVersionRequestRequestTypeDef",
    "UpdateNodegroupVersionResponseTypeDef",
    "UpdateParamTypeDef",
    "UpdatePodIdentityAssociationRequestRequestTypeDef",
    "UpdatePodIdentityAssociationResponseTypeDef",
    "UpdateTaintsPayloadTypeDef",
    "UpdateTypeDef",
    "VpcConfigRequestTypeDef",
    "VpcConfigResponseTypeDef",
    "WaiterConfigTypeDef",
)

AccessConfigResponseTypeDef = TypedDict(
    "AccessConfigResponseTypeDef",
    {
        "bootstrapClusterCreatorAdminPermissions": bool,
        "authenticationMode": AuthenticationModeType,
    },
    total=False,
)

AccessEntryTypeDef = TypedDict(
    "AccessEntryTypeDef",
    {
        "clusterName": str,
        "principalArn": str,
        "kubernetesGroups": List[str],
        "accessEntryArn": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "tags": Dict[str, str],
        "username": str,
        "type": str,
    },
    total=False,
)

AccessPolicyTypeDef = TypedDict(
    "AccessPolicyTypeDef",
    {
        "name": str,
        "arn": str,
    },
    total=False,
)

AccessScopeTypeDef = TypedDict(
    "AccessScopeTypeDef",
    {
        "type": AccessScopeTypeType,
        "namespaces": List[str],
    },
    total=False,
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
        "publisher": str,
        "owner": str,
        "marketplaceInformation": "MarketplaceInformationTypeDef",
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

AddonPodIdentityAssociationsTypeDef = TypedDict(
    "AddonPodIdentityAssociationsTypeDef",
    {
        "serviceAccount": str,
        "roleArn": str,
    },
)

AddonPodIdentityConfigurationTypeDef = TypedDict(
    "AddonPodIdentityConfigurationTypeDef",
    {
        "serviceAccount": str,
        "recommendedManagedPolicies": List[str],
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
        "publisher": str,
        "owner": str,
        "marketplaceInformation": "MarketplaceInformationTypeDef",
        "configurationValues": str,
        "podIdentityAssociations": List[str],
    },
    total=False,
)

AddonVersionInfoTypeDef = TypedDict(
    "AddonVersionInfoTypeDef",
    {
        "addonVersion": str,
        "architecture": List[str],
        "compatibilities": List["CompatibilityTypeDef"],
        "requiresConfiguration": bool,
        "requiresIamPermissions": bool,
    },
    total=False,
)

AssociateAccessPolicyRequestRequestTypeDef = TypedDict(
    "AssociateAccessPolicyRequestRequestTypeDef",
    {
        "clusterName": str,
        "principalArn": str,
        "policyArn": str,
        "accessScope": "AccessScopeTypeDef",
    },
)

AssociateAccessPolicyResponseTypeDef = TypedDict(
    "AssociateAccessPolicyResponseTypeDef",
    {
        "clusterName": str,
        "principalArn": str,
        "associatedAccessPolicy": "AssociatedAccessPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

AssociatedAccessPolicyTypeDef = TypedDict(
    "AssociatedAccessPolicyTypeDef",
    {
        "policyArn": str,
        "accessScope": "AccessScopeTypeDef",
        "associatedAt": datetime,
        "modifiedAt": datetime,
    },
    total=False,
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

ClientStatTypeDef = TypedDict(
    "ClientStatTypeDef",
    {
        "userAgent": str,
        "numberOfRequestsLast30Days": int,
        "lastRequestTime": datetime,
    },
    total=False,
)

ClusterHealthTypeDef = TypedDict(
    "ClusterHealthTypeDef",
    {
        "issues": List["ClusterIssueTypeDef"],
    },
    total=False,
)

ClusterIssueTypeDef = TypedDict(
    "ClusterIssueTypeDef",
    {
        "code": ClusterIssueCodeType,
        "message": str,
        "resourceIds": List[str],
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
        "connectorConfig": "ConnectorConfigResponseTypeDef",
        "id": str,
        "health": "ClusterHealthTypeDef",
        "outpostConfig": "OutpostConfigResponseTypeDef",
        "accessConfig": "AccessConfigResponseTypeDef",
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

ConnectorConfigRequestTypeDef = TypedDict(
    "ConnectorConfigRequestTypeDef",
    {
        "roleArn": str,
        "provider": ConnectorConfigProviderType,
    },
)

ConnectorConfigResponseTypeDef = TypedDict(
    "ConnectorConfigResponseTypeDef",
    {
        "activationId": str,
        "activationCode": str,
        "activationExpiry": datetime,
        "provider": str,
        "roleArn": str,
    },
    total=False,
)

ControlPlanePlacementRequestTypeDef = TypedDict(
    "ControlPlanePlacementRequestTypeDef",
    {
        "groupName": str,
    },
    total=False,
)

ControlPlanePlacementResponseTypeDef = TypedDict(
    "ControlPlanePlacementResponseTypeDef",
    {
        "groupName": str,
    },
    total=False,
)

CreateAccessConfigRequestTypeDef = TypedDict(
    "CreateAccessConfigRequestTypeDef",
    {
        "bootstrapClusterCreatorAdminPermissions": bool,
        "authenticationMode": AuthenticationModeType,
    },
    total=False,
)

_RequiredCreateAccessEntryRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAccessEntryRequestRequestTypeDef",
    {
        "clusterName": str,
        "principalArn": str,
    },
)
_OptionalCreateAccessEntryRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAccessEntryRequestRequestTypeDef",
    {
        "kubernetesGroups": List[str],
        "tags": Dict[str, str],
        "clientRequestToken": str,
        "username": str,
        "type": str,
    },
    total=False,
)

class CreateAccessEntryRequestRequestTypeDef(
    _RequiredCreateAccessEntryRequestRequestTypeDef, _OptionalCreateAccessEntryRequestRequestTypeDef
):
    pass

CreateAccessEntryResponseTypeDef = TypedDict(
    "CreateAccessEntryResponseTypeDef",
    {
        "accessEntry": "AccessEntryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "configurationValues": str,
        "podIdentityAssociations": List["AddonPodIdentityAssociationsTypeDef"],
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
        "outpostConfig": "OutpostConfigRequestTypeDef",
        "accessConfig": "CreateAccessConfigRequestTypeDef",
        "bootstrapSelfManagedAddons": bool,
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

_RequiredCreateEksAnywhereSubscriptionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEksAnywhereSubscriptionRequestRequestTypeDef",
    {
        "name": str,
        "term": "EksAnywhereSubscriptionTermTypeDef",
    },
)
_OptionalCreateEksAnywhereSubscriptionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEksAnywhereSubscriptionRequestRequestTypeDef",
    {
        "licenseQuantity": int,
        "licenseType": Literal["Cluster"],
        "autoRenew": bool,
        "clientRequestToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateEksAnywhereSubscriptionRequestRequestTypeDef(
    _RequiredCreateEksAnywhereSubscriptionRequestRequestTypeDef,
    _OptionalCreateEksAnywhereSubscriptionRequestRequestTypeDef,
):
    pass

CreateEksAnywhereSubscriptionResponseTypeDef = TypedDict(
    "CreateEksAnywhereSubscriptionResponseTypeDef",
    {
        "subscription": "EksAnywhereSubscriptionTypeDef",
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

_RequiredCreatePodIdentityAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePodIdentityAssociationRequestRequestTypeDef",
    {
        "clusterName": str,
        "namespace": str,
        "serviceAccount": str,
        "roleArn": str,
    },
)
_OptionalCreatePodIdentityAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePodIdentityAssociationRequestRequestTypeDef",
    {
        "clientRequestToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreatePodIdentityAssociationRequestRequestTypeDef(
    _RequiredCreatePodIdentityAssociationRequestRequestTypeDef,
    _OptionalCreatePodIdentityAssociationRequestRequestTypeDef,
):
    pass

CreatePodIdentityAssociationResponseTypeDef = TypedDict(
    "CreatePodIdentityAssociationResponseTypeDef",
    {
        "association": "PodIdentityAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAccessEntryRequestRequestTypeDef = TypedDict(
    "DeleteAccessEntryRequestRequestTypeDef",
    {
        "clusterName": str,
        "principalArn": str,
    },
)

_RequiredDeleteAddonRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAddonRequestRequestTypeDef",
    {
        "clusterName": str,
        "addonName": str,
    },
)
_OptionalDeleteAddonRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAddonRequestRequestTypeDef",
    {
        "preserve": bool,
    },
    total=False,
)

class DeleteAddonRequestRequestTypeDef(
    _RequiredDeleteAddonRequestRequestTypeDef, _OptionalDeleteAddonRequestRequestTypeDef
):
    pass

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

DeleteEksAnywhereSubscriptionRequestRequestTypeDef = TypedDict(
    "DeleteEksAnywhereSubscriptionRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteEksAnywhereSubscriptionResponseTypeDef = TypedDict(
    "DeleteEksAnywhereSubscriptionResponseTypeDef",
    {
        "subscription": "EksAnywhereSubscriptionTypeDef",
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

DeletePodIdentityAssociationRequestRequestTypeDef = TypedDict(
    "DeletePodIdentityAssociationRequestRequestTypeDef",
    {
        "clusterName": str,
        "associationId": str,
    },
)

DeletePodIdentityAssociationResponseTypeDef = TypedDict(
    "DeletePodIdentityAssociationResponseTypeDef",
    {
        "association": "PodIdentityAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeprecationDetailTypeDef = TypedDict(
    "DeprecationDetailTypeDef",
    {
        "usage": str,
        "replacedWith": str,
        "stopServingVersion": str,
        "startServingReplacementVersion": str,
        "clientStats": List["ClientStatTypeDef"],
    },
    total=False,
)

DeregisterClusterRequestRequestTypeDef = TypedDict(
    "DeregisterClusterRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeregisterClusterResponseTypeDef = TypedDict(
    "DeregisterClusterResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccessEntryRequestRequestTypeDef = TypedDict(
    "DescribeAccessEntryRequestRequestTypeDef",
    {
        "clusterName": str,
        "principalArn": str,
    },
)

DescribeAccessEntryResponseTypeDef = TypedDict(
    "DescribeAccessEntryResponseTypeDef",
    {
        "accessEntry": "AccessEntryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAddonConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeAddonConfigurationRequestRequestTypeDef",
    {
        "addonName": str,
        "addonVersion": str,
    },
)

DescribeAddonConfigurationResponseTypeDef = TypedDict(
    "DescribeAddonConfigurationResponseTypeDef",
    {
        "addonName": str,
        "addonVersion": str,
        "configurationSchema": str,
        "podIdentityConfiguration": List["AddonPodIdentityConfigurationTypeDef"],
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
        "types": List[str],
        "publishers": List[str],
        "owners": List[str],
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

DescribeEksAnywhereSubscriptionRequestRequestTypeDef = TypedDict(
    "DescribeEksAnywhereSubscriptionRequestRequestTypeDef",
    {
        "id": str,
    },
)

DescribeEksAnywhereSubscriptionResponseTypeDef = TypedDict(
    "DescribeEksAnywhereSubscriptionResponseTypeDef",
    {
        "subscription": "EksAnywhereSubscriptionTypeDef",
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

DescribeInsightRequestRequestTypeDef = TypedDict(
    "DescribeInsightRequestRequestTypeDef",
    {
        "clusterName": str,
        "id": str,
    },
)

DescribeInsightResponseTypeDef = TypedDict(
    "DescribeInsightResponseTypeDef",
    {
        "insight": "InsightTypeDef",
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

DescribePodIdentityAssociationRequestRequestTypeDef = TypedDict(
    "DescribePodIdentityAssociationRequestRequestTypeDef",
    {
        "clusterName": str,
        "associationId": str,
    },
)

DescribePodIdentityAssociationResponseTypeDef = TypedDict(
    "DescribePodIdentityAssociationResponseTypeDef",
    {
        "association": "PodIdentityAssociationTypeDef",
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

DisassociateAccessPolicyRequestRequestTypeDef = TypedDict(
    "DisassociateAccessPolicyRequestRequestTypeDef",
    {
        "clusterName": str,
        "principalArn": str,
        "policyArn": str,
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

EksAnywhereSubscriptionTermTypeDef = TypedDict(
    "EksAnywhereSubscriptionTermTypeDef",
    {
        "duration": int,
        "unit": Literal["MONTHS"],
    },
    total=False,
)

EksAnywhereSubscriptionTypeDef = TypedDict(
    "EksAnywhereSubscriptionTypeDef",
    {
        "id": str,
        "arn": str,
        "createdAt": datetime,
        "effectiveDate": datetime,
        "expirationDate": datetime,
        "licenseQuantity": int,
        "licenseType": Literal["Cluster"],
        "term": "EksAnywhereSubscriptionTermTypeDef",
        "status": str,
        "autoRenew": bool,
        "licenseArns": List[str],
        "tags": Dict[str, str],
    },
    total=False,
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

FargateProfileHealthTypeDef = TypedDict(
    "FargateProfileHealthTypeDef",
    {
        "issues": List["FargateProfileIssueTypeDef"],
    },
    total=False,
)

FargateProfileIssueTypeDef = TypedDict(
    "FargateProfileIssueTypeDef",
    {
        "code": FargateProfileIssueCodeType,
        "message": str,
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
        "health": "FargateProfileHealthTypeDef",
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

InsightCategorySpecificSummaryTypeDef = TypedDict(
    "InsightCategorySpecificSummaryTypeDef",
    {
        "deprecationDetails": List["DeprecationDetailTypeDef"],
    },
    total=False,
)

InsightResourceDetailTypeDef = TypedDict(
    "InsightResourceDetailTypeDef",
    {
        "insightStatus": "InsightStatusTypeDef",
        "kubernetesResourceUri": str,
        "arn": str,
    },
    total=False,
)

InsightStatusTypeDef = TypedDict(
    "InsightStatusTypeDef",
    {
        "status": InsightStatusValueType,
        "reason": str,
    },
    total=False,
)

InsightSummaryTypeDef = TypedDict(
    "InsightSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "category": Literal["UPGRADE_READINESS"],
        "kubernetesVersion": str,
        "lastRefreshTime": datetime,
        "lastTransitionTime": datetime,
        "description": str,
        "insightStatus": "InsightStatusTypeDef",
    },
    total=False,
)

InsightTypeDef = TypedDict(
    "InsightTypeDef",
    {
        "id": str,
        "name": str,
        "category": Literal["UPGRADE_READINESS"],
        "kubernetesVersion": str,
        "lastRefreshTime": datetime,
        "lastTransitionTime": datetime,
        "description": str,
        "insightStatus": "InsightStatusTypeDef",
        "recommendation": str,
        "additionalInfo": Dict[str, str],
        "resources": List["InsightResourceDetailTypeDef"],
        "categorySpecificSummary": "InsightCategorySpecificSummaryTypeDef",
    },
    total=False,
)

InsightsFilterTypeDef = TypedDict(
    "InsightsFilterTypeDef",
    {
        "categories": List[Literal["UPGRADE_READINESS"]],
        "kubernetesVersions": List[str],
        "statuses": List[InsightStatusValueType],
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
        "ipFamily": IpFamilyType,
    },
    total=False,
)

KubernetesNetworkConfigResponseTypeDef = TypedDict(
    "KubernetesNetworkConfigResponseTypeDef",
    {
        "serviceIpv4Cidr": str,
        "serviceIpv6Cidr": str,
        "ipFamily": IpFamilyType,
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

_RequiredListAccessEntriesRequestRequestTypeDef = TypedDict(
    "_RequiredListAccessEntriesRequestRequestTypeDef",
    {
        "clusterName": str,
    },
)
_OptionalListAccessEntriesRequestRequestTypeDef = TypedDict(
    "_OptionalListAccessEntriesRequestRequestTypeDef",
    {
        "associatedPolicyArn": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAccessEntriesRequestRequestTypeDef(
    _RequiredListAccessEntriesRequestRequestTypeDef, _OptionalListAccessEntriesRequestRequestTypeDef
):
    pass

ListAccessEntriesResponseTypeDef = TypedDict(
    "ListAccessEntriesResponseTypeDef",
    {
        "accessEntries": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAccessPoliciesRequestRequestTypeDef = TypedDict(
    "ListAccessPoliciesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListAccessPoliciesResponseTypeDef = TypedDict(
    "ListAccessPoliciesResponseTypeDef",
    {
        "accessPolicies": List["AccessPolicyTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredListAssociatedAccessPoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredListAssociatedAccessPoliciesRequestRequestTypeDef",
    {
        "clusterName": str,
        "principalArn": str,
    },
)
_OptionalListAssociatedAccessPoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalListAssociatedAccessPoliciesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAssociatedAccessPoliciesRequestRequestTypeDef(
    _RequiredListAssociatedAccessPoliciesRequestRequestTypeDef,
    _OptionalListAssociatedAccessPoliciesRequestRequestTypeDef,
):
    pass

ListAssociatedAccessPoliciesResponseTypeDef = TypedDict(
    "ListAssociatedAccessPoliciesResponseTypeDef",
    {
        "clusterName": str,
        "principalArn": str,
        "nextToken": str,
        "associatedAccessPolicies": List["AssociatedAccessPolicyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListClustersRequestRequestTypeDef = TypedDict(
    "ListClustersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "include": List[str],
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

ListEksAnywhereSubscriptionsRequestRequestTypeDef = TypedDict(
    "ListEksAnywhereSubscriptionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "includeStatus": List[EksAnywhereSubscriptionStatusType],
    },
    total=False,
)

ListEksAnywhereSubscriptionsResponseTypeDef = TypedDict(
    "ListEksAnywhereSubscriptionsResponseTypeDef",
    {
        "subscriptions": List["EksAnywhereSubscriptionTypeDef"],
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

_RequiredListInsightsRequestRequestTypeDef = TypedDict(
    "_RequiredListInsightsRequestRequestTypeDef",
    {
        "clusterName": str,
    },
)
_OptionalListInsightsRequestRequestTypeDef = TypedDict(
    "_OptionalListInsightsRequestRequestTypeDef",
    {
        "filter": "InsightsFilterTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListInsightsRequestRequestTypeDef(
    _RequiredListInsightsRequestRequestTypeDef, _OptionalListInsightsRequestRequestTypeDef
):
    pass

ListInsightsResponseTypeDef = TypedDict(
    "ListInsightsResponseTypeDef",
    {
        "insights": List["InsightSummaryTypeDef"],
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

_RequiredListPodIdentityAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredListPodIdentityAssociationsRequestRequestTypeDef",
    {
        "clusterName": str,
    },
)
_OptionalListPodIdentityAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalListPodIdentityAssociationsRequestRequestTypeDef",
    {
        "namespace": str,
        "serviceAccount": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListPodIdentityAssociationsRequestRequestTypeDef(
    _RequiredListPodIdentityAssociationsRequestRequestTypeDef,
    _OptionalListPodIdentityAssociationsRequestRequestTypeDef,
):
    pass

ListPodIdentityAssociationsResponseTypeDef = TypedDict(
    "ListPodIdentityAssociationsResponseTypeDef",
    {
        "associations": List["PodIdentityAssociationSummaryTypeDef"],
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

MarketplaceInformationTypeDef = TypedDict(
    "MarketplaceInformationTypeDef",
    {
        "productId": str,
        "productUrl": str,
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

_RequiredOutpostConfigRequestTypeDef = TypedDict(
    "_RequiredOutpostConfigRequestTypeDef",
    {
        "outpostArns": List[str],
        "controlPlaneInstanceType": str,
    },
)
_OptionalOutpostConfigRequestTypeDef = TypedDict(
    "_OptionalOutpostConfigRequestTypeDef",
    {
        "controlPlanePlacement": "ControlPlanePlacementRequestTypeDef",
    },
    total=False,
)

class OutpostConfigRequestTypeDef(
    _RequiredOutpostConfigRequestTypeDef, _OptionalOutpostConfigRequestTypeDef
):
    pass

_RequiredOutpostConfigResponseTypeDef = TypedDict(
    "_RequiredOutpostConfigResponseTypeDef",
    {
        "outpostArns": List[str],
        "controlPlaneInstanceType": str,
    },
)
_OptionalOutpostConfigResponseTypeDef = TypedDict(
    "_OptionalOutpostConfigResponseTypeDef",
    {
        "controlPlanePlacement": "ControlPlanePlacementResponseTypeDef",
    },
    total=False,
)

class OutpostConfigResponseTypeDef(
    _RequiredOutpostConfigResponseTypeDef, _OptionalOutpostConfigResponseTypeDef
):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PodIdentityAssociationSummaryTypeDef = TypedDict(
    "PodIdentityAssociationSummaryTypeDef",
    {
        "clusterName": str,
        "namespace": str,
        "serviceAccount": str,
        "associationArn": str,
        "associationId": str,
        "ownerArn": str,
    },
    total=False,
)

PodIdentityAssociationTypeDef = TypedDict(
    "PodIdentityAssociationTypeDef",
    {
        "clusterName": str,
        "namespace": str,
        "serviceAccount": str,
        "roleArn": str,
        "associationArn": str,
        "associationId": str,
        "tags": Dict[str, str],
        "createdAt": datetime,
        "modifiedAt": datetime,
        "ownerArn": str,
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

_RequiredRegisterClusterRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterClusterRequestRequestTypeDef",
    {
        "name": str,
        "connectorConfig": "ConnectorConfigRequestTypeDef",
    },
)
_OptionalRegisterClusterRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterClusterRequestRequestTypeDef",
    {
        "clientRequestToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class RegisterClusterRequestRequestTypeDef(
    _RequiredRegisterClusterRequestRequestTypeDef, _OptionalRegisterClusterRequestRequestTypeDef
):
    pass

RegisterClusterResponseTypeDef = TypedDict(
    "RegisterClusterResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

UpdateAccessConfigRequestTypeDef = TypedDict(
    "UpdateAccessConfigRequestTypeDef",
    {
        "authenticationMode": AuthenticationModeType,
    },
    total=False,
)

_RequiredUpdateAccessEntryRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAccessEntryRequestRequestTypeDef",
    {
        "clusterName": str,
        "principalArn": str,
    },
)
_OptionalUpdateAccessEntryRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAccessEntryRequestRequestTypeDef",
    {
        "kubernetesGroups": List[str],
        "clientRequestToken": str,
        "username": str,
    },
    total=False,
)

class UpdateAccessEntryRequestRequestTypeDef(
    _RequiredUpdateAccessEntryRequestRequestTypeDef, _OptionalUpdateAccessEntryRequestRequestTypeDef
):
    pass

UpdateAccessEntryResponseTypeDef = TypedDict(
    "UpdateAccessEntryResponseTypeDef",
    {
        "accessEntry": "AccessEntryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
        "configurationValues": str,
        "podIdentityAssociations": List["AddonPodIdentityAssociationsTypeDef"],
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
        "accessConfig": "UpdateAccessConfigRequestTypeDef",
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

_RequiredUpdateEksAnywhereSubscriptionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEksAnywhereSubscriptionRequestRequestTypeDef",
    {
        "id": str,
        "autoRenew": bool,
    },
)
_OptionalUpdateEksAnywhereSubscriptionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEksAnywhereSubscriptionRequestRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)

class UpdateEksAnywhereSubscriptionRequestRequestTypeDef(
    _RequiredUpdateEksAnywhereSubscriptionRequestRequestTypeDef,
    _OptionalUpdateEksAnywhereSubscriptionRequestRequestTypeDef,
):
    pass

UpdateEksAnywhereSubscriptionResponseTypeDef = TypedDict(
    "UpdateEksAnywhereSubscriptionResponseTypeDef",
    {
        "subscription": "EksAnywhereSubscriptionTypeDef",
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

_RequiredUpdatePodIdentityAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePodIdentityAssociationRequestRequestTypeDef",
    {
        "clusterName": str,
        "associationId": str,
    },
)
_OptionalUpdatePodIdentityAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePodIdentityAssociationRequestRequestTypeDef",
    {
        "roleArn": str,
        "clientRequestToken": str,
    },
    total=False,
)

class UpdatePodIdentityAssociationRequestRequestTypeDef(
    _RequiredUpdatePodIdentityAssociationRequestRequestTypeDef,
    _OptionalUpdatePodIdentityAssociationRequestRequestTypeDef,
):
    pass

UpdatePodIdentityAssociationResponseTypeDef = TypedDict(
    "UpdatePodIdentityAssociationResponseTypeDef",
    {
        "association": "PodIdentityAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
