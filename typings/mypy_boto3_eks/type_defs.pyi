"""
Type annotations for eks service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_eks.type_defs import AccessConfigResponseTypeDef

    data: AccessConfigResponseTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AccessScopeTypeType,
    AddonIssueCodeType,
    AddonStatusType,
    AMITypesType,
    ArgoCdRoleType,
    AuthenticationModeType,
    CapabilityIssueCodeType,
    CapabilityStatusType,
    CapabilityTypeType,
    CapacityTypesType,
    CategoryType,
    ClusterIssueCodeType,
    ClusterStatusType,
    ClusterVersionStatusType,
    ConfigStatusType,
    ConnectorConfigProviderType,
    EksAnywhereSubscriptionStatusType,
    ErrorCodeType,
    FargateProfileIssueCodeType,
    FargateProfileStatusType,
    InsightsRefreshStatusType,
    InsightStatusValueType,
    IpFamilyType,
    LogTypeType,
    NodegroupIssueCodeType,
    NodegroupStatusType,
    NodegroupUpdateStrategiesType,
    ProvisionedControlPlaneTierType,
    RepairActionType,
    ResolveConflictsType,
    SsoIdentityTypeType,
    SupportTypeType,
    TaintEffectType,
    UpdateParamTypeType,
    UpdateStatusType,
    UpdateTypeType,
    VersionStatusType,
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
    "AccessConfigResponseTypeDef",
    "AccessEntryTypeDef",
    "AccessPolicyTypeDef",
    "AccessScopeOutputTypeDef",
    "AccessScopeTypeDef",
    "AccessScopeUnionTypeDef",
    "AddonCompatibilityDetailTypeDef",
    "AddonHealthTypeDef",
    "AddonInfoTypeDef",
    "AddonIssueTypeDef",
    "AddonNamespaceConfigRequestTypeDef",
    "AddonNamespaceConfigResponseTypeDef",
    "AddonPodIdentityAssociationsTypeDef",
    "AddonPodIdentityConfigurationTypeDef",
    "AddonTypeDef",
    "AddonVersionInfoTypeDef",
    "ArgoCdAwsIdcConfigRequestTypeDef",
    "ArgoCdAwsIdcConfigResponseTypeDef",
    "ArgoCdConfigRequestTypeDef",
    "ArgoCdConfigResponseTypeDef",
    "ArgoCdNetworkAccessConfigRequestTypeDef",
    "ArgoCdNetworkAccessConfigResponseTypeDef",
    "ArgoCdRoleMappingOutputTypeDef",
    "ArgoCdRoleMappingTypeDef",
    "ArgoCdRoleMappingUnionTypeDef",
    "AssociateAccessPolicyRequestTypeDef",
    "AssociateAccessPolicyResponseTypeDef",
    "AssociateEncryptionConfigRequestTypeDef",
    "AssociateEncryptionConfigResponseTypeDef",
    "AssociateIdentityProviderConfigRequestTypeDef",
    "AssociateIdentityProviderConfigResponseTypeDef",
    "AssociatedAccessPolicyTypeDef",
    "AutoScalingGroupTypeDef",
    "BlockStorageTypeDef",
    "CapabilityConfigurationRequestTypeDef",
    "CapabilityConfigurationResponseTypeDef",
    "CapabilityHealthTypeDef",
    "CapabilityIssueTypeDef",
    "CapabilitySummaryTypeDef",
    "CapabilityTypeDef",
    "CertificateTypeDef",
    "ClientStatTypeDef",
    "ClusterHealthTypeDef",
    "ClusterIssueTypeDef",
    "ClusterTypeDef",
    "ClusterVersionInformationTypeDef",
    "CompatibilityTypeDef",
    "ComputeConfigRequestTypeDef",
    "ComputeConfigResponseTypeDef",
    "ConnectorConfigRequestTypeDef",
    "ConnectorConfigResponseTypeDef",
    "ControlPlanePlacementRequestTypeDef",
    "ControlPlanePlacementResponseTypeDef",
    "ControlPlaneScalingConfigTypeDef",
    "CreateAccessConfigRequestTypeDef",
    "CreateAccessEntryRequestTypeDef",
    "CreateAccessEntryResponseTypeDef",
    "CreateAddonRequestTypeDef",
    "CreateAddonResponseTypeDef",
    "CreateCapabilityRequestTypeDef",
    "CreateCapabilityResponseTypeDef",
    "CreateClusterRequestTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateEksAnywhereSubscriptionRequestTypeDef",
    "CreateEksAnywhereSubscriptionResponseTypeDef",
    "CreateFargateProfileRequestTypeDef",
    "CreateFargateProfileResponseTypeDef",
    "CreateNodegroupRequestTypeDef",
    "CreateNodegroupResponseTypeDef",
    "CreatePodIdentityAssociationRequestTypeDef",
    "CreatePodIdentityAssociationResponseTypeDef",
    "DeleteAccessEntryRequestTypeDef",
    "DeleteAddonRequestTypeDef",
    "DeleteAddonResponseTypeDef",
    "DeleteCapabilityRequestTypeDef",
    "DeleteCapabilityResponseTypeDef",
    "DeleteClusterRequestTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteEksAnywhereSubscriptionRequestTypeDef",
    "DeleteEksAnywhereSubscriptionResponseTypeDef",
    "DeleteFargateProfileRequestTypeDef",
    "DeleteFargateProfileResponseTypeDef",
    "DeleteNodegroupRequestTypeDef",
    "DeleteNodegroupResponseTypeDef",
    "DeletePodIdentityAssociationRequestTypeDef",
    "DeletePodIdentityAssociationResponseTypeDef",
    "DeprecationDetailTypeDef",
    "DeregisterClusterRequestTypeDef",
    "DeregisterClusterResponseTypeDef",
    "DescribeAccessEntryRequestTypeDef",
    "DescribeAccessEntryResponseTypeDef",
    "DescribeAddonConfigurationRequestTypeDef",
    "DescribeAddonConfigurationResponseTypeDef",
    "DescribeAddonRequestTypeDef",
    "DescribeAddonRequestWaitExtraTypeDef",
    "DescribeAddonRequestWaitTypeDef",
    "DescribeAddonResponseTypeDef",
    "DescribeAddonVersionsRequestPaginateTypeDef",
    "DescribeAddonVersionsRequestTypeDef",
    "DescribeAddonVersionsResponseTypeDef",
    "DescribeCapabilityRequestTypeDef",
    "DescribeCapabilityResponseTypeDef",
    "DescribeClusterRequestTypeDef",
    "DescribeClusterRequestWaitExtraTypeDef",
    "DescribeClusterRequestWaitTypeDef",
    "DescribeClusterResponseTypeDef",
    "DescribeClusterVersionsRequestPaginateTypeDef",
    "DescribeClusterVersionsRequestTypeDef",
    "DescribeClusterVersionsResponseTypeDef",
    "DescribeEksAnywhereSubscriptionRequestTypeDef",
    "DescribeEksAnywhereSubscriptionResponseTypeDef",
    "DescribeFargateProfileRequestTypeDef",
    "DescribeFargateProfileRequestWaitExtraTypeDef",
    "DescribeFargateProfileRequestWaitTypeDef",
    "DescribeFargateProfileResponseTypeDef",
    "DescribeIdentityProviderConfigRequestTypeDef",
    "DescribeIdentityProviderConfigResponseTypeDef",
    "DescribeInsightRequestTypeDef",
    "DescribeInsightResponseTypeDef",
    "DescribeInsightsRefreshRequestTypeDef",
    "DescribeInsightsRefreshResponseTypeDef",
    "DescribeNodegroupRequestTypeDef",
    "DescribeNodegroupRequestWaitExtraTypeDef",
    "DescribeNodegroupRequestWaitTypeDef",
    "DescribeNodegroupResponseTypeDef",
    "DescribePodIdentityAssociationRequestTypeDef",
    "DescribePodIdentityAssociationResponseTypeDef",
    "DescribeUpdateRequestTypeDef",
    "DescribeUpdateResponseTypeDef",
    "DisassociateAccessPolicyRequestTypeDef",
    "DisassociateIdentityProviderConfigRequestTypeDef",
    "DisassociateIdentityProviderConfigResponseTypeDef",
    "EksAnywhereSubscriptionTermTypeDef",
    "EksAnywhereSubscriptionTypeDef",
    "ElasticLoadBalancingTypeDef",
    "EncryptionConfigOutputTypeDef",
    "EncryptionConfigTypeDef",
    "EncryptionConfigUnionTypeDef",
    "ErrorDetailTypeDef",
    "FargateProfileHealthTypeDef",
    "FargateProfileIssueTypeDef",
    "FargateProfileSelectorOutputTypeDef",
    "FargateProfileSelectorTypeDef",
    "FargateProfileSelectorUnionTypeDef",
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
    "LicenseTypeDef",
    "ListAccessEntriesRequestPaginateTypeDef",
    "ListAccessEntriesRequestTypeDef",
    "ListAccessEntriesResponseTypeDef",
    "ListAccessPoliciesRequestPaginateTypeDef",
    "ListAccessPoliciesRequestTypeDef",
    "ListAccessPoliciesResponseTypeDef",
    "ListAddonsRequestPaginateTypeDef",
    "ListAddonsRequestTypeDef",
    "ListAddonsResponseTypeDef",
    "ListAssociatedAccessPoliciesRequestPaginateTypeDef",
    "ListAssociatedAccessPoliciesRequestTypeDef",
    "ListAssociatedAccessPoliciesResponseTypeDef",
    "ListCapabilitiesRequestPaginateTypeDef",
    "ListCapabilitiesRequestTypeDef",
    "ListCapabilitiesResponseTypeDef",
    "ListClustersRequestPaginateTypeDef",
    "ListClustersRequestTypeDef",
    "ListClustersResponseTypeDef",
    "ListEksAnywhereSubscriptionsRequestPaginateTypeDef",
    "ListEksAnywhereSubscriptionsRequestTypeDef",
    "ListEksAnywhereSubscriptionsResponseTypeDef",
    "ListFargateProfilesRequestPaginateTypeDef",
    "ListFargateProfilesRequestTypeDef",
    "ListFargateProfilesResponseTypeDef",
    "ListIdentityProviderConfigsRequestPaginateTypeDef",
    "ListIdentityProviderConfigsRequestTypeDef",
    "ListIdentityProviderConfigsResponseTypeDef",
    "ListInsightsRequestPaginateTypeDef",
    "ListInsightsRequestTypeDef",
    "ListInsightsResponseTypeDef",
    "ListNodegroupsRequestPaginateTypeDef",
    "ListNodegroupsRequestTypeDef",
    "ListNodegroupsResponseTypeDef",
    "ListPodIdentityAssociationsRequestPaginateTypeDef",
    "ListPodIdentityAssociationsRequestTypeDef",
    "ListPodIdentityAssociationsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUpdatesRequestPaginateTypeDef",
    "ListUpdatesRequestTypeDef",
    "ListUpdatesResponseTypeDef",
    "LogSetupOutputTypeDef",
    "LogSetupTypeDef",
    "LoggingOutputTypeDef",
    "LoggingTypeDef",
    "LoggingUnionTypeDef",
    "MarketplaceInformationTypeDef",
    "NodeRepairConfigOutputTypeDef",
    "NodeRepairConfigOverridesTypeDef",
    "NodeRepairConfigTypeDef",
    "NodeRepairConfigUnionTypeDef",
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
    "RegisterClusterRequestTypeDef",
    "RegisterClusterResponseTypeDef",
    "RemoteAccessConfigOutputTypeDef",
    "RemoteAccessConfigTypeDef",
    "RemoteAccessConfigUnionTypeDef",
    "RemoteNetworkConfigRequestTypeDef",
    "RemoteNetworkConfigResponseTypeDef",
    "RemoteNodeNetworkOutputTypeDef",
    "RemoteNodeNetworkTypeDef",
    "RemoteNodeNetworkUnionTypeDef",
    "RemotePodNetworkOutputTypeDef",
    "RemotePodNetworkTypeDef",
    "RemotePodNetworkUnionTypeDef",
    "ResponseMetadataTypeDef",
    "SsoIdentityTypeDef",
    "StartInsightsRefreshRequestTypeDef",
    "StartInsightsRefreshResponseTypeDef",
    "StorageConfigRequestTypeDef",
    "StorageConfigResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TaintTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAccessConfigRequestTypeDef",
    "UpdateAccessEntryRequestTypeDef",
    "UpdateAccessEntryResponseTypeDef",
    "UpdateAddonRequestTypeDef",
    "UpdateAddonResponseTypeDef",
    "UpdateArgoCdConfigTypeDef",
    "UpdateCapabilityConfigurationTypeDef",
    "UpdateCapabilityRequestTypeDef",
    "UpdateCapabilityResponseTypeDef",
    "UpdateClusterConfigRequestTypeDef",
    "UpdateClusterConfigResponseTypeDef",
    "UpdateClusterVersionRequestTypeDef",
    "UpdateClusterVersionResponseTypeDef",
    "UpdateEksAnywhereSubscriptionRequestTypeDef",
    "UpdateEksAnywhereSubscriptionResponseTypeDef",
    "UpdateLabelsPayloadTypeDef",
    "UpdateNodegroupConfigRequestTypeDef",
    "UpdateNodegroupConfigResponseTypeDef",
    "UpdateNodegroupVersionRequestTypeDef",
    "UpdateNodegroupVersionResponseTypeDef",
    "UpdateParamTypeDef",
    "UpdatePodIdentityAssociationRequestTypeDef",
    "UpdatePodIdentityAssociationResponseTypeDef",
    "UpdateRoleMappingsTypeDef",
    "UpdateTaintsPayloadTypeDef",
    "UpdateTypeDef",
    "UpgradePolicyRequestTypeDef",
    "UpgradePolicyResponseTypeDef",
    "VpcConfigRequestTypeDef",
    "VpcConfigResponseTypeDef",
    "WaiterConfigTypeDef",
    "ZonalShiftConfigRequestTypeDef",
    "ZonalShiftConfigResponseTypeDef",
)

class AccessConfigResponseTypeDef(TypedDict):
    bootstrapClusterCreatorAdminPermissions: NotRequired[bool]
    authenticationMode: NotRequired[AuthenticationModeType]

AccessEntryTypeDef = TypedDict(
    "AccessEntryTypeDef",
    {
        "clusterName": NotRequired[str],
        "principalArn": NotRequired[str],
        "kubernetesGroups": NotRequired[List[str]],
        "accessEntryArn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "modifiedAt": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
        "username": NotRequired[str],
        "type": NotRequired[str],
    },
)

class AccessPolicyTypeDef(TypedDict):
    name: NotRequired[str]
    arn: NotRequired[str]

AccessScopeOutputTypeDef = TypedDict(
    "AccessScopeOutputTypeDef",
    {
        "type": NotRequired[AccessScopeTypeType],
        "namespaces": NotRequired[List[str]],
    },
)
AccessScopeTypeDef = TypedDict(
    "AccessScopeTypeDef",
    {
        "type": NotRequired[AccessScopeTypeType],
        "namespaces": NotRequired[Sequence[str]],
    },
)

class AddonCompatibilityDetailTypeDef(TypedDict):
    name: NotRequired[str]
    compatibleVersions: NotRequired[List[str]]

class AddonIssueTypeDef(TypedDict):
    code: NotRequired[AddonIssueCodeType]
    message: NotRequired[str]
    resourceIds: NotRequired[List[str]]

class MarketplaceInformationTypeDef(TypedDict):
    productId: NotRequired[str]
    productUrl: NotRequired[str]

class AddonNamespaceConfigRequestTypeDef(TypedDict):
    namespace: NotRequired[str]

class AddonNamespaceConfigResponseTypeDef(TypedDict):
    namespace: NotRequired[str]

class AddonPodIdentityAssociationsTypeDef(TypedDict):
    serviceAccount: str
    roleArn: str

class AddonPodIdentityConfigurationTypeDef(TypedDict):
    serviceAccount: NotRequired[str]
    recommendedManagedPolicies: NotRequired[List[str]]

class CompatibilityTypeDef(TypedDict):
    clusterVersion: NotRequired[str]
    platformVersions: NotRequired[List[str]]
    defaultVersion: NotRequired[bool]

class ArgoCdAwsIdcConfigRequestTypeDef(TypedDict):
    idcInstanceArn: str
    idcRegion: NotRequired[str]

class ArgoCdAwsIdcConfigResponseTypeDef(TypedDict):
    idcInstanceArn: NotRequired[str]
    idcRegion: NotRequired[str]
    idcManagedApplicationArn: NotRequired[str]

class ArgoCdNetworkAccessConfigRequestTypeDef(TypedDict):
    vpceIds: NotRequired[Sequence[str]]

class ArgoCdNetworkAccessConfigResponseTypeDef(TypedDict):
    vpceIds: NotRequired[List[str]]

SsoIdentityTypeDef = TypedDict(
    "SsoIdentityTypeDef",
    {
        "id": str,
        "type": SsoIdentityTypeType,
    },
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class OidcIdentityProviderConfigRequestTypeDef(TypedDict):
    identityProviderConfigName: str
    issuerUrl: str
    clientId: str
    usernameClaim: NotRequired[str]
    usernamePrefix: NotRequired[str]
    groupsClaim: NotRequired[str]
    groupsPrefix: NotRequired[str]
    requiredClaims: NotRequired[Mapping[str, str]]

class AutoScalingGroupTypeDef(TypedDict):
    name: NotRequired[str]

class BlockStorageTypeDef(TypedDict):
    enabled: NotRequired[bool]

class CapabilityIssueTypeDef(TypedDict):
    code: NotRequired[CapabilityIssueCodeType]
    message: NotRequired[str]

CapabilitySummaryTypeDef = TypedDict(
    "CapabilitySummaryTypeDef",
    {
        "capabilityName": NotRequired[str],
        "arn": NotRequired[str],
        "type": NotRequired[CapabilityTypeType],
        "status": NotRequired[CapabilityStatusType],
        "version": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "modifiedAt": NotRequired[datetime],
    },
)

class CertificateTypeDef(TypedDict):
    data: NotRequired[str]

class ClientStatTypeDef(TypedDict):
    userAgent: NotRequired[str]
    numberOfRequestsLast30Days: NotRequired[int]
    lastRequestTime: NotRequired[datetime]

class ClusterIssueTypeDef(TypedDict):
    code: NotRequired[ClusterIssueCodeType]
    message: NotRequired[str]
    resourceIds: NotRequired[List[str]]

class ComputeConfigResponseTypeDef(TypedDict):
    enabled: NotRequired[bool]
    nodePools: NotRequired[List[str]]
    nodeRoleArn: NotRequired[str]

class ConnectorConfigResponseTypeDef(TypedDict):
    activationId: NotRequired[str]
    activationCode: NotRequired[str]
    activationExpiry: NotRequired[datetime]
    provider: NotRequired[str]
    roleArn: NotRequired[str]

class ControlPlaneScalingConfigTypeDef(TypedDict):
    tier: NotRequired[ProvisionedControlPlaneTierType]

class UpgradePolicyResponseTypeDef(TypedDict):
    supportType: NotRequired[SupportTypeType]

class VpcConfigResponseTypeDef(TypedDict):
    subnetIds: NotRequired[List[str]]
    securityGroupIds: NotRequired[List[str]]
    clusterSecurityGroupId: NotRequired[str]
    vpcId: NotRequired[str]
    endpointPublicAccess: NotRequired[bool]
    endpointPrivateAccess: NotRequired[bool]
    publicAccessCidrs: NotRequired[List[str]]

class ZonalShiftConfigResponseTypeDef(TypedDict):
    enabled: NotRequired[bool]

class ClusterVersionInformationTypeDef(TypedDict):
    clusterVersion: NotRequired[str]
    clusterType: NotRequired[str]
    defaultPlatformVersion: NotRequired[str]
    defaultVersion: NotRequired[bool]
    releaseDate: NotRequired[datetime]
    endOfStandardSupportDate: NotRequired[datetime]
    endOfExtendedSupportDate: NotRequired[datetime]
    status: NotRequired[ClusterVersionStatusType]
    versionStatus: NotRequired[VersionStatusType]
    kubernetesPatchVersion: NotRequired[str]

class ComputeConfigRequestTypeDef(TypedDict):
    enabled: NotRequired[bool]
    nodePools: NotRequired[Sequence[str]]
    nodeRoleArn: NotRequired[str]

class ConnectorConfigRequestTypeDef(TypedDict):
    roleArn: str
    provider: ConnectorConfigProviderType

class ControlPlanePlacementRequestTypeDef(TypedDict):
    groupName: NotRequired[str]

class ControlPlanePlacementResponseTypeDef(TypedDict):
    groupName: NotRequired[str]

class CreateAccessConfigRequestTypeDef(TypedDict):
    bootstrapClusterCreatorAdminPermissions: NotRequired[bool]
    authenticationMode: NotRequired[AuthenticationModeType]

CreateAccessEntryRequestTypeDef = TypedDict(
    "CreateAccessEntryRequestTypeDef",
    {
        "clusterName": str,
        "principalArn": str,
        "kubernetesGroups": NotRequired[Sequence[str]],
        "tags": NotRequired[Mapping[str, str]],
        "clientRequestToken": NotRequired[str],
        "username": NotRequired[str],
        "type": NotRequired[str],
    },
)

class UpgradePolicyRequestTypeDef(TypedDict):
    supportType: NotRequired[SupportTypeType]

class VpcConfigRequestTypeDef(TypedDict):
    subnetIds: NotRequired[Sequence[str]]
    securityGroupIds: NotRequired[Sequence[str]]
    endpointPublicAccess: NotRequired[bool]
    endpointPrivateAccess: NotRequired[bool]
    publicAccessCidrs: NotRequired[Sequence[str]]

class ZonalShiftConfigRequestTypeDef(TypedDict):
    enabled: NotRequired[bool]

class EksAnywhereSubscriptionTermTypeDef(TypedDict):
    duration: NotRequired[int]
    unit: NotRequired[Literal["MONTHS"]]

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {
        "name": NotRequired[str],
        "version": NotRequired[str],
        "id": NotRequired[str],
    },
)

class NodegroupScalingConfigTypeDef(TypedDict):
    minSize: NotRequired[int]
    maxSize: NotRequired[int]
    desiredSize: NotRequired[int]

class NodegroupUpdateConfigTypeDef(TypedDict):
    maxUnavailable: NotRequired[int]
    maxUnavailablePercentage: NotRequired[int]
    updateStrategy: NotRequired[NodegroupUpdateStrategiesType]

class TaintTypeDef(TypedDict):
    key: NotRequired[str]
    value: NotRequired[str]
    effect: NotRequired[TaintEffectType]

class CreatePodIdentityAssociationRequestTypeDef(TypedDict):
    clusterName: str
    namespace: str
    serviceAccount: str
    roleArn: str
    clientRequestToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    disableSessionTags: NotRequired[bool]
    targetRoleArn: NotRequired[str]

class PodIdentityAssociationTypeDef(TypedDict):
    clusterName: NotRequired[str]
    namespace: NotRequired[str]
    serviceAccount: NotRequired[str]
    roleArn: NotRequired[str]
    associationArn: NotRequired[str]
    associationId: NotRequired[str]
    tags: NotRequired[Dict[str, str]]
    createdAt: NotRequired[datetime]
    modifiedAt: NotRequired[datetime]
    ownerArn: NotRequired[str]
    disableSessionTags: NotRequired[bool]
    targetRoleArn: NotRequired[str]
    externalId: NotRequired[str]

class DeleteAccessEntryRequestTypeDef(TypedDict):
    clusterName: str
    principalArn: str

class DeleteAddonRequestTypeDef(TypedDict):
    clusterName: str
    addonName: str
    preserve: NotRequired[bool]

class DeleteCapabilityRequestTypeDef(TypedDict):
    clusterName: str
    capabilityName: str

class DeleteClusterRequestTypeDef(TypedDict):
    name: str

DeleteEksAnywhereSubscriptionRequestTypeDef = TypedDict(
    "DeleteEksAnywhereSubscriptionRequestTypeDef",
    {
        "id": str,
    },
)

class DeleteFargateProfileRequestTypeDef(TypedDict):
    clusterName: str
    fargateProfileName: str

class DeleteNodegroupRequestTypeDef(TypedDict):
    clusterName: str
    nodegroupName: str

class DeletePodIdentityAssociationRequestTypeDef(TypedDict):
    clusterName: str
    associationId: str

class DeregisterClusterRequestTypeDef(TypedDict):
    name: str

class DescribeAccessEntryRequestTypeDef(TypedDict):
    clusterName: str
    principalArn: str

class DescribeAddonConfigurationRequestTypeDef(TypedDict):
    addonName: str
    addonVersion: str

class DescribeAddonRequestTypeDef(TypedDict):
    clusterName: str
    addonName: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

DescribeAddonVersionsRequestTypeDef = TypedDict(
    "DescribeAddonVersionsRequestTypeDef",
    {
        "kubernetesVersion": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "addonName": NotRequired[str],
        "types": NotRequired[Sequence[str]],
        "publishers": NotRequired[Sequence[str]],
        "owners": NotRequired[Sequence[str]],
    },
)

class DescribeCapabilityRequestTypeDef(TypedDict):
    clusterName: str
    capabilityName: str

class DescribeClusterRequestTypeDef(TypedDict):
    name: str

class DescribeClusterVersionsRequestTypeDef(TypedDict):
    clusterType: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    defaultOnly: NotRequired[bool]
    includeAll: NotRequired[bool]
    clusterVersions: NotRequired[Sequence[str]]
    status: NotRequired[ClusterVersionStatusType]
    versionStatus: NotRequired[VersionStatusType]

DescribeEksAnywhereSubscriptionRequestTypeDef = TypedDict(
    "DescribeEksAnywhereSubscriptionRequestTypeDef",
    {
        "id": str,
    },
)

class DescribeFargateProfileRequestTypeDef(TypedDict):
    clusterName: str
    fargateProfileName: str

IdentityProviderConfigTypeDef = TypedDict(
    "IdentityProviderConfigTypeDef",
    {
        "type": str,
        "name": str,
    },
)
DescribeInsightRequestTypeDef = TypedDict(
    "DescribeInsightRequestTypeDef",
    {
        "clusterName": str,
        "id": str,
    },
)

class DescribeInsightsRefreshRequestTypeDef(TypedDict):
    clusterName: str

class DescribeNodegroupRequestTypeDef(TypedDict):
    clusterName: str
    nodegroupName: str

class DescribePodIdentityAssociationRequestTypeDef(TypedDict):
    clusterName: str
    associationId: str

class DescribeUpdateRequestTypeDef(TypedDict):
    name: str
    updateId: str
    nodegroupName: NotRequired[str]
    addonName: NotRequired[str]
    capabilityName: NotRequired[str]

class DisassociateAccessPolicyRequestTypeDef(TypedDict):
    clusterName: str
    principalArn: str
    policyArn: str

LicenseTypeDef = TypedDict(
    "LicenseTypeDef",
    {
        "id": NotRequired[str],
        "token": NotRequired[str],
    },
)

class ElasticLoadBalancingTypeDef(TypedDict):
    enabled: NotRequired[bool]

class ProviderTypeDef(TypedDict):
    keyArn: NotRequired[str]

class ErrorDetailTypeDef(TypedDict):
    errorCode: NotRequired[ErrorCodeType]
    errorMessage: NotRequired[str]
    resourceIds: NotRequired[List[str]]

class FargateProfileIssueTypeDef(TypedDict):
    code: NotRequired[FargateProfileIssueCodeType]
    message: NotRequired[str]
    resourceIds: NotRequired[List[str]]

class FargateProfileSelectorOutputTypeDef(TypedDict):
    namespace: NotRequired[str]
    labels: NotRequired[Dict[str, str]]

class FargateProfileSelectorTypeDef(TypedDict):
    namespace: NotRequired[str]
    labels: NotRequired[Mapping[str, str]]

class OidcIdentityProviderConfigTypeDef(TypedDict):
    identityProviderConfigName: NotRequired[str]
    identityProviderConfigArn: NotRequired[str]
    clusterName: NotRequired[str]
    issuerUrl: NotRequired[str]
    clientId: NotRequired[str]
    usernameClaim: NotRequired[str]
    usernamePrefix: NotRequired[str]
    groupsClaim: NotRequired[str]
    groupsPrefix: NotRequired[str]
    requiredClaims: NotRequired[Dict[str, str]]
    tags: NotRequired[Dict[str, str]]
    status: NotRequired[ConfigStatusType]

class OIDCTypeDef(TypedDict):
    issuer: NotRequired[str]

class InsightStatusTypeDef(TypedDict):
    status: NotRequired[InsightStatusValueType]
    reason: NotRequired[str]

class InsightsFilterTypeDef(TypedDict):
    categories: NotRequired[Sequence[CategoryType]]
    kubernetesVersions: NotRequired[Sequence[str]]
    statuses: NotRequired[Sequence[InsightStatusValueType]]

class IssueTypeDef(TypedDict):
    code: NotRequired[NodegroupIssueCodeType]
    message: NotRequired[str]
    resourceIds: NotRequired[List[str]]

class ListAccessEntriesRequestTypeDef(TypedDict):
    clusterName: str
    associatedPolicyArn: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListAccessPoliciesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListAddonsRequestTypeDef(TypedDict):
    clusterName: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListAssociatedAccessPoliciesRequestTypeDef(TypedDict):
    clusterName: str
    principalArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListCapabilitiesRequestTypeDef(TypedDict):
    clusterName: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListClustersRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    include: NotRequired[Sequence[str]]

class ListEksAnywhereSubscriptionsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    includeStatus: NotRequired[Sequence[EksAnywhereSubscriptionStatusType]]

class ListFargateProfilesRequestTypeDef(TypedDict):
    clusterName: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListIdentityProviderConfigsRequestTypeDef(TypedDict):
    clusterName: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListNodegroupsRequestTypeDef(TypedDict):
    clusterName: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListPodIdentityAssociationsRequestTypeDef(TypedDict):
    clusterName: str
    namespace: NotRequired[str]
    serviceAccount: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class PodIdentityAssociationSummaryTypeDef(TypedDict):
    clusterName: NotRequired[str]
    namespace: NotRequired[str]
    serviceAccount: NotRequired[str]
    associationArn: NotRequired[str]
    associationId: NotRequired[str]
    ownerArn: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ListUpdatesRequestTypeDef(TypedDict):
    name: str
    nodegroupName: NotRequired[str]
    addonName: NotRequired[str]
    capabilityName: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

LogSetupOutputTypeDef = TypedDict(
    "LogSetupOutputTypeDef",
    {
        "types": NotRequired[List[LogTypeType]],
        "enabled": NotRequired[bool],
    },
)
LogSetupTypeDef = TypedDict(
    "LogSetupTypeDef",
    {
        "types": NotRequired[Sequence[LogTypeType]],
        "enabled": NotRequired[bool],
    },
)

class NodeRepairConfigOverridesTypeDef(TypedDict):
    nodeMonitoringCondition: NotRequired[str]
    nodeUnhealthyReason: NotRequired[str]
    minRepairWaitTimeMins: NotRequired[int]
    repairAction: NotRequired[RepairActionType]

class RemoteAccessConfigOutputTypeDef(TypedDict):
    ec2SshKey: NotRequired[str]
    sourceSecurityGroups: NotRequired[List[str]]

class RemoteAccessConfigTypeDef(TypedDict):
    ec2SshKey: NotRequired[str]
    sourceSecurityGroups: NotRequired[Sequence[str]]

class RemoteNodeNetworkOutputTypeDef(TypedDict):
    cidrs: NotRequired[List[str]]

class RemotePodNetworkOutputTypeDef(TypedDict):
    cidrs: NotRequired[List[str]]

class RemoteNodeNetworkTypeDef(TypedDict):
    cidrs: NotRequired[Sequence[str]]

class RemotePodNetworkTypeDef(TypedDict):
    cidrs: NotRequired[Sequence[str]]

class StartInsightsRefreshRequestTypeDef(TypedDict):
    clusterName: str

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAccessConfigRequestTypeDef(TypedDict):
    authenticationMode: NotRequired[AuthenticationModeType]

class UpdateAccessEntryRequestTypeDef(TypedDict):
    clusterName: str
    principalArn: str
    kubernetesGroups: NotRequired[Sequence[str]]
    clientRequestToken: NotRequired[str]
    username: NotRequired[str]

class UpdateClusterVersionRequestTypeDef(TypedDict):
    name: str
    version: str
    clientRequestToken: NotRequired[str]
    force: NotRequired[bool]

UpdateEksAnywhereSubscriptionRequestTypeDef = TypedDict(
    "UpdateEksAnywhereSubscriptionRequestTypeDef",
    {
        "id": str,
        "autoRenew": bool,
        "clientRequestToken": NotRequired[str],
    },
)

class UpdateLabelsPayloadTypeDef(TypedDict):
    addOrUpdateLabels: NotRequired[Mapping[str, str]]
    removeLabels: NotRequired[Sequence[str]]

UpdateParamTypeDef = TypedDict(
    "UpdateParamTypeDef",
    {
        "type": NotRequired[UpdateParamTypeType],
        "value": NotRequired[str],
    },
)

class UpdatePodIdentityAssociationRequestTypeDef(TypedDict):
    clusterName: str
    associationId: str
    roleArn: NotRequired[str]
    clientRequestToken: NotRequired[str]
    disableSessionTags: NotRequired[bool]
    targetRoleArn: NotRequired[str]

class AssociatedAccessPolicyTypeDef(TypedDict):
    policyArn: NotRequired[str]
    accessScope: NotRequired[AccessScopeOutputTypeDef]
    associatedAt: NotRequired[datetime]
    modifiedAt: NotRequired[datetime]

AccessScopeUnionTypeDef = Union[AccessScopeTypeDef, AccessScopeOutputTypeDef]

class AddonHealthTypeDef(TypedDict):
    issues: NotRequired[List[AddonIssueTypeDef]]

class CreateAddonRequestTypeDef(TypedDict):
    clusterName: str
    addonName: str
    addonVersion: NotRequired[str]
    serviceAccountRoleArn: NotRequired[str]
    resolveConflicts: NotRequired[ResolveConflictsType]
    clientRequestToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    configurationValues: NotRequired[str]
    podIdentityAssociations: NotRequired[Sequence[AddonPodIdentityAssociationsTypeDef]]
    namespaceConfig: NotRequired[AddonNamespaceConfigRequestTypeDef]

class UpdateAddonRequestTypeDef(TypedDict):
    clusterName: str
    addonName: str
    addonVersion: NotRequired[str]
    serviceAccountRoleArn: NotRequired[str]
    resolveConflicts: NotRequired[ResolveConflictsType]
    clientRequestToken: NotRequired[str]
    configurationValues: NotRequired[str]
    podIdentityAssociations: NotRequired[Sequence[AddonPodIdentityAssociationsTypeDef]]

class AddonVersionInfoTypeDef(TypedDict):
    addonVersion: NotRequired[str]
    architecture: NotRequired[List[str]]
    computeTypes: NotRequired[List[str]]
    compatibilities: NotRequired[List[CompatibilityTypeDef]]
    requiresConfiguration: NotRequired[bool]
    requiresIamPermissions: NotRequired[bool]

class ArgoCdRoleMappingOutputTypeDef(TypedDict):
    role: ArgoCdRoleType
    identities: List[SsoIdentityTypeDef]

class ArgoCdRoleMappingTypeDef(TypedDict):
    role: ArgoCdRoleType
    identities: Sequence[SsoIdentityTypeDef]

class CreateAccessEntryResponseTypeDef(TypedDict):
    accessEntry: AccessEntryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccessEntryResponseTypeDef(TypedDict):
    accessEntry: AccessEntryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAddonConfigurationResponseTypeDef(TypedDict):
    addonName: str
    addonVersion: str
    configurationSchema: str
    podIdentityConfiguration: List[AddonPodIdentityConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInsightsRefreshResponseTypeDef(TypedDict):
    message: str
    status: InsightsRefreshStatusType
    startedAt: datetime
    endedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessEntriesResponseTypeDef(TypedDict):
    accessEntries: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAccessPoliciesResponseTypeDef(TypedDict):
    accessPolicies: List[AccessPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAddonsResponseTypeDef(TypedDict):
    addons: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListClustersResponseTypeDef(TypedDict):
    clusters: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListFargateProfilesResponseTypeDef(TypedDict):
    fargateProfileNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListNodegroupsResponseTypeDef(TypedDict):
    nodegroups: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListUpdatesResponseTypeDef(TypedDict):
    updateIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StartInsightsRefreshResponseTypeDef(TypedDict):
    message: str
    status: InsightsRefreshStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccessEntryResponseTypeDef(TypedDict):
    accessEntry: AccessEntryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateIdentityProviderConfigRequestTypeDef(TypedDict):
    clusterName: str
    oidc: OidcIdentityProviderConfigRequestTypeDef
    tags: NotRequired[Mapping[str, str]]
    clientRequestToken: NotRequired[str]

class NodegroupResourcesTypeDef(TypedDict):
    autoScalingGroups: NotRequired[List[AutoScalingGroupTypeDef]]
    remoteAccessSecurityGroup: NotRequired[str]

class StorageConfigRequestTypeDef(TypedDict):
    blockStorage: NotRequired[BlockStorageTypeDef]

class StorageConfigResponseTypeDef(TypedDict):
    blockStorage: NotRequired[BlockStorageTypeDef]

class CapabilityHealthTypeDef(TypedDict):
    issues: NotRequired[List[CapabilityIssueTypeDef]]

class ListCapabilitiesResponseTypeDef(TypedDict):
    capabilities: List[CapabilitySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DeprecationDetailTypeDef(TypedDict):
    usage: NotRequired[str]
    replacedWith: NotRequired[str]
    stopServingVersion: NotRequired[str]
    startServingReplacementVersion: NotRequired[str]
    clientStats: NotRequired[List[ClientStatTypeDef]]

class ClusterHealthTypeDef(TypedDict):
    issues: NotRequired[List[ClusterIssueTypeDef]]

class DescribeClusterVersionsResponseTypeDef(TypedDict):
    clusterVersions: List[ClusterVersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class RegisterClusterRequestTypeDef(TypedDict):
    name: str
    connectorConfig: ConnectorConfigRequestTypeDef
    clientRequestToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class OutpostConfigRequestTypeDef(TypedDict):
    outpostArns: Sequence[str]
    controlPlaneInstanceType: str
    controlPlanePlacement: NotRequired[ControlPlanePlacementRequestTypeDef]

class OutpostConfigResponseTypeDef(TypedDict):
    outpostArns: List[str]
    controlPlaneInstanceType: str
    controlPlanePlacement: NotRequired[ControlPlanePlacementResponseTypeDef]

class CreateEksAnywhereSubscriptionRequestTypeDef(TypedDict):
    name: str
    term: EksAnywhereSubscriptionTermTypeDef
    licenseQuantity: NotRequired[int]
    licenseType: NotRequired[Literal["Cluster"]]
    autoRenew: NotRequired[bool]
    clientRequestToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class UpdateNodegroupVersionRequestTypeDef(TypedDict):
    clusterName: str
    nodegroupName: str
    version: NotRequired[str]
    releaseVersion: NotRequired[str]
    launchTemplate: NotRequired[LaunchTemplateSpecificationTypeDef]
    force: NotRequired[bool]
    clientRequestToken: NotRequired[str]

class UpdateTaintsPayloadTypeDef(TypedDict):
    addOrUpdateTaints: NotRequired[Sequence[TaintTypeDef]]
    removeTaints: NotRequired[Sequence[TaintTypeDef]]

class CreatePodIdentityAssociationResponseTypeDef(TypedDict):
    association: PodIdentityAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePodIdentityAssociationResponseTypeDef(TypedDict):
    association: PodIdentityAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePodIdentityAssociationResponseTypeDef(TypedDict):
    association: PodIdentityAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePodIdentityAssociationResponseTypeDef(TypedDict):
    association: PodIdentityAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAddonRequestWaitExtraTypeDef(TypedDict):
    clusterName: str
    addonName: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeAddonRequestWaitTypeDef(TypedDict):
    clusterName: str
    addonName: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeClusterRequestWaitExtraTypeDef(TypedDict):
    name: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeClusterRequestWaitTypeDef(TypedDict):
    name: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeFargateProfileRequestWaitExtraTypeDef(TypedDict):
    clusterName: str
    fargateProfileName: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeFargateProfileRequestWaitTypeDef(TypedDict):
    clusterName: str
    fargateProfileName: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeNodegroupRequestWaitExtraTypeDef(TypedDict):
    clusterName: str
    nodegroupName: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeNodegroupRequestWaitTypeDef(TypedDict):
    clusterName: str
    nodegroupName: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

DescribeAddonVersionsRequestPaginateTypeDef = TypedDict(
    "DescribeAddonVersionsRequestPaginateTypeDef",
    {
        "kubernetesVersion": NotRequired[str],
        "addonName": NotRequired[str],
        "types": NotRequired[Sequence[str]],
        "publishers": NotRequired[Sequence[str]],
        "owners": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class DescribeClusterVersionsRequestPaginateTypeDef(TypedDict):
    clusterType: NotRequired[str]
    defaultOnly: NotRequired[bool]
    includeAll: NotRequired[bool]
    clusterVersions: NotRequired[Sequence[str]]
    status: NotRequired[ClusterVersionStatusType]
    versionStatus: NotRequired[VersionStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAccessEntriesRequestPaginateTypeDef(TypedDict):
    clusterName: str
    associatedPolicyArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAccessPoliciesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAddonsRequestPaginateTypeDef(TypedDict):
    clusterName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAssociatedAccessPoliciesRequestPaginateTypeDef(TypedDict):
    clusterName: str
    principalArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCapabilitiesRequestPaginateTypeDef(TypedDict):
    clusterName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListClustersRequestPaginateTypeDef(TypedDict):
    include: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEksAnywhereSubscriptionsRequestPaginateTypeDef(TypedDict):
    includeStatus: NotRequired[Sequence[EksAnywhereSubscriptionStatusType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFargateProfilesRequestPaginateTypeDef(TypedDict):
    clusterName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListIdentityProviderConfigsRequestPaginateTypeDef(TypedDict):
    clusterName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListNodegroupsRequestPaginateTypeDef(TypedDict):
    clusterName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPodIdentityAssociationsRequestPaginateTypeDef(TypedDict):
    clusterName: str
    namespace: NotRequired[str]
    serviceAccount: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListUpdatesRequestPaginateTypeDef(TypedDict):
    name: str
    nodegroupName: NotRequired[str]
    addonName: NotRequired[str]
    capabilityName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeIdentityProviderConfigRequestTypeDef(TypedDict):
    clusterName: str
    identityProviderConfig: IdentityProviderConfigTypeDef

class DisassociateIdentityProviderConfigRequestTypeDef(TypedDict):
    clusterName: str
    identityProviderConfig: IdentityProviderConfigTypeDef
    clientRequestToken: NotRequired[str]

class ListIdentityProviderConfigsResponseTypeDef(TypedDict):
    identityProviderConfigs: List[IdentityProviderConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

EksAnywhereSubscriptionTypeDef = TypedDict(
    "EksAnywhereSubscriptionTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "effectiveDate": NotRequired[datetime],
        "expirationDate": NotRequired[datetime],
        "licenseQuantity": NotRequired[int],
        "licenseType": NotRequired[Literal["Cluster"]],
        "term": NotRequired[EksAnywhereSubscriptionTermTypeDef],
        "status": NotRequired[str],
        "autoRenew": NotRequired[bool],
        "licenseArns": NotRequired[List[str]],
        "licenses": NotRequired[List[LicenseTypeDef]],
        "tags": NotRequired[Dict[str, str]],
    },
)

class KubernetesNetworkConfigRequestTypeDef(TypedDict):
    serviceIpv4Cidr: NotRequired[str]
    ipFamily: NotRequired[IpFamilyType]
    elasticLoadBalancing: NotRequired[ElasticLoadBalancingTypeDef]

class KubernetesNetworkConfigResponseTypeDef(TypedDict):
    serviceIpv4Cidr: NotRequired[str]
    serviceIpv6Cidr: NotRequired[str]
    ipFamily: NotRequired[IpFamilyType]
    elasticLoadBalancing: NotRequired[ElasticLoadBalancingTypeDef]

class EncryptionConfigOutputTypeDef(TypedDict):
    resources: NotRequired[List[str]]
    provider: NotRequired[ProviderTypeDef]

class EncryptionConfigTypeDef(TypedDict):
    resources: NotRequired[Sequence[str]]
    provider: NotRequired[ProviderTypeDef]

class FargateProfileHealthTypeDef(TypedDict):
    issues: NotRequired[List[FargateProfileIssueTypeDef]]

FargateProfileSelectorUnionTypeDef = Union[
    FargateProfileSelectorTypeDef, FargateProfileSelectorOutputTypeDef
]

class IdentityProviderConfigResponseTypeDef(TypedDict):
    oidc: NotRequired[OidcIdentityProviderConfigTypeDef]

class IdentityTypeDef(TypedDict):
    oidc: NotRequired[OIDCTypeDef]

class InsightResourceDetailTypeDef(TypedDict):
    insightStatus: NotRequired[InsightStatusTypeDef]
    kubernetesResourceUri: NotRequired[str]
    arn: NotRequired[str]

InsightSummaryTypeDef = TypedDict(
    "InsightSummaryTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "category": NotRequired[CategoryType],
        "kubernetesVersion": NotRequired[str],
        "lastRefreshTime": NotRequired[datetime],
        "lastTransitionTime": NotRequired[datetime],
        "description": NotRequired[str],
        "insightStatus": NotRequired[InsightStatusTypeDef],
    },
)
ListInsightsRequestPaginateTypeDef = TypedDict(
    "ListInsightsRequestPaginateTypeDef",
    {
        "clusterName": str,
        "filter": NotRequired[InsightsFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListInsightsRequestTypeDef = TypedDict(
    "ListInsightsRequestTypeDef",
    {
        "clusterName": str,
        "filter": NotRequired[InsightsFilterTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

class NodegroupHealthTypeDef(TypedDict):
    issues: NotRequired[List[IssueTypeDef]]

class ListPodIdentityAssociationsResponseTypeDef(TypedDict):
    associations: List[PodIdentityAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class LoggingOutputTypeDef(TypedDict):
    clusterLogging: NotRequired[List[LogSetupOutputTypeDef]]

class LoggingTypeDef(TypedDict):
    clusterLogging: NotRequired[Sequence[LogSetupTypeDef]]

class NodeRepairConfigOutputTypeDef(TypedDict):
    enabled: NotRequired[bool]
    maxUnhealthyNodeThresholdCount: NotRequired[int]
    maxUnhealthyNodeThresholdPercentage: NotRequired[int]
    maxParallelNodesRepairedCount: NotRequired[int]
    maxParallelNodesRepairedPercentage: NotRequired[int]
    nodeRepairConfigOverrides: NotRequired[List[NodeRepairConfigOverridesTypeDef]]

class NodeRepairConfigTypeDef(TypedDict):
    enabled: NotRequired[bool]
    maxUnhealthyNodeThresholdCount: NotRequired[int]
    maxUnhealthyNodeThresholdPercentage: NotRequired[int]
    maxParallelNodesRepairedCount: NotRequired[int]
    maxParallelNodesRepairedPercentage: NotRequired[int]
    nodeRepairConfigOverrides: NotRequired[Sequence[NodeRepairConfigOverridesTypeDef]]

RemoteAccessConfigUnionTypeDef = Union[RemoteAccessConfigTypeDef, RemoteAccessConfigOutputTypeDef]

class RemoteNetworkConfigResponseTypeDef(TypedDict):
    remoteNodeNetworks: NotRequired[List[RemoteNodeNetworkOutputTypeDef]]
    remotePodNetworks: NotRequired[List[RemotePodNetworkOutputTypeDef]]

RemoteNodeNetworkUnionTypeDef = Union[RemoteNodeNetworkTypeDef, RemoteNodeNetworkOutputTypeDef]
RemotePodNetworkUnionTypeDef = Union[RemotePodNetworkTypeDef, RemotePodNetworkOutputTypeDef]
UpdateTypeDef = TypedDict(
    "UpdateTypeDef",
    {
        "id": NotRequired[str],
        "status": NotRequired[UpdateStatusType],
        "type": NotRequired[UpdateTypeType],
        "params": NotRequired[List[UpdateParamTypeDef]],
        "createdAt": NotRequired[datetime],
        "errors": NotRequired[List[ErrorDetailTypeDef]],
    },
)

class AssociateAccessPolicyResponseTypeDef(TypedDict):
    clusterName: str
    principalArn: str
    associatedAccessPolicy: AssociatedAccessPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssociatedAccessPoliciesResponseTypeDef(TypedDict):
    clusterName: str
    principalArn: str
    associatedAccessPolicies: List[AssociatedAccessPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class AssociateAccessPolicyRequestTypeDef(TypedDict):
    clusterName: str
    principalArn: str
    policyArn: str
    accessScope: AccessScopeUnionTypeDef

class AddonTypeDef(TypedDict):
    addonName: NotRequired[str]
    clusterName: NotRequired[str]
    status: NotRequired[AddonStatusType]
    addonVersion: NotRequired[str]
    health: NotRequired[AddonHealthTypeDef]
    addonArn: NotRequired[str]
    createdAt: NotRequired[datetime]
    modifiedAt: NotRequired[datetime]
    serviceAccountRoleArn: NotRequired[str]
    tags: NotRequired[Dict[str, str]]
    publisher: NotRequired[str]
    owner: NotRequired[str]
    marketplaceInformation: NotRequired[MarketplaceInformationTypeDef]
    configurationValues: NotRequired[str]
    podIdentityAssociations: NotRequired[List[str]]
    namespaceConfig: NotRequired[AddonNamespaceConfigResponseTypeDef]

AddonInfoTypeDef = TypedDict(
    "AddonInfoTypeDef",
    {
        "addonName": NotRequired[str],
        "type": NotRequired[str],
        "addonVersions": NotRequired[List[AddonVersionInfoTypeDef]],
        "publisher": NotRequired[str],
        "owner": NotRequired[str],
        "marketplaceInformation": NotRequired[MarketplaceInformationTypeDef],
        "defaultNamespace": NotRequired[str],
    },
)

class ArgoCdConfigResponseTypeDef(TypedDict):
    namespace: NotRequired[str]
    awsIdc: NotRequired[ArgoCdAwsIdcConfigResponseTypeDef]
    rbacRoleMappings: NotRequired[List[ArgoCdRoleMappingOutputTypeDef]]
    networkAccess: NotRequired[ArgoCdNetworkAccessConfigResponseTypeDef]
    serverUrl: NotRequired[str]

ArgoCdRoleMappingUnionTypeDef = Union[ArgoCdRoleMappingTypeDef, ArgoCdRoleMappingOutputTypeDef]

class InsightCategorySpecificSummaryTypeDef(TypedDict):
    deprecationDetails: NotRequired[List[DeprecationDetailTypeDef]]
    addonCompatibilityDetails: NotRequired[List[AddonCompatibilityDetailTypeDef]]

class CreateEksAnywhereSubscriptionResponseTypeDef(TypedDict):
    subscription: EksAnywhereSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEksAnywhereSubscriptionResponseTypeDef(TypedDict):
    subscription: EksAnywhereSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEksAnywhereSubscriptionResponseTypeDef(TypedDict):
    subscription: EksAnywhereSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEksAnywhereSubscriptionsResponseTypeDef(TypedDict):
    subscriptions: List[EksAnywhereSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateEksAnywhereSubscriptionResponseTypeDef(TypedDict):
    subscription: EksAnywhereSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

EncryptionConfigUnionTypeDef = Union[EncryptionConfigTypeDef, EncryptionConfigOutputTypeDef]

class FargateProfileTypeDef(TypedDict):
    fargateProfileName: NotRequired[str]
    fargateProfileArn: NotRequired[str]
    clusterName: NotRequired[str]
    createdAt: NotRequired[datetime]
    podExecutionRoleArn: NotRequired[str]
    subnets: NotRequired[List[str]]
    selectors: NotRequired[List[FargateProfileSelectorOutputTypeDef]]
    status: NotRequired[FargateProfileStatusType]
    tags: NotRequired[Dict[str, str]]
    health: NotRequired[FargateProfileHealthTypeDef]

class CreateFargateProfileRequestTypeDef(TypedDict):
    fargateProfileName: str
    clusterName: str
    podExecutionRoleArn: str
    subnets: NotRequired[Sequence[str]]
    selectors: NotRequired[Sequence[FargateProfileSelectorUnionTypeDef]]
    clientRequestToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class DescribeIdentityProviderConfigResponseTypeDef(TypedDict):
    identityProviderConfig: IdentityProviderConfigResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInsightsResponseTypeDef(TypedDict):
    insights: List[InsightSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

LoggingUnionTypeDef = Union[LoggingTypeDef, LoggingOutputTypeDef]

class NodegroupTypeDef(TypedDict):
    nodegroupName: NotRequired[str]
    nodegroupArn: NotRequired[str]
    clusterName: NotRequired[str]
    version: NotRequired[str]
    releaseVersion: NotRequired[str]
    createdAt: NotRequired[datetime]
    modifiedAt: NotRequired[datetime]
    status: NotRequired[NodegroupStatusType]
    capacityType: NotRequired[CapacityTypesType]
    scalingConfig: NotRequired[NodegroupScalingConfigTypeDef]
    instanceTypes: NotRequired[List[str]]
    subnets: NotRequired[List[str]]
    remoteAccess: NotRequired[RemoteAccessConfigOutputTypeDef]
    amiType: NotRequired[AMITypesType]
    nodeRole: NotRequired[str]
    labels: NotRequired[Dict[str, str]]
    taints: NotRequired[List[TaintTypeDef]]
    resources: NotRequired[NodegroupResourcesTypeDef]
    diskSize: NotRequired[int]
    health: NotRequired[NodegroupHealthTypeDef]
    updateConfig: NotRequired[NodegroupUpdateConfigTypeDef]
    nodeRepairConfig: NotRequired[NodeRepairConfigOutputTypeDef]
    launchTemplate: NotRequired[LaunchTemplateSpecificationTypeDef]
    tags: NotRequired[Dict[str, str]]

NodeRepairConfigUnionTypeDef = Union[NodeRepairConfigTypeDef, NodeRepairConfigOutputTypeDef]
ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "version": NotRequired[str],
        "endpoint": NotRequired[str],
        "roleArn": NotRequired[str],
        "resourcesVpcConfig": NotRequired[VpcConfigResponseTypeDef],
        "kubernetesNetworkConfig": NotRequired[KubernetesNetworkConfigResponseTypeDef],
        "logging": NotRequired[LoggingOutputTypeDef],
        "identity": NotRequired[IdentityTypeDef],
        "status": NotRequired[ClusterStatusType],
        "certificateAuthority": NotRequired[CertificateTypeDef],
        "clientRequestToken": NotRequired[str],
        "platformVersion": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "encryptionConfig": NotRequired[List[EncryptionConfigOutputTypeDef]],
        "connectorConfig": NotRequired[ConnectorConfigResponseTypeDef],
        "id": NotRequired[str],
        "health": NotRequired[ClusterHealthTypeDef],
        "outpostConfig": NotRequired[OutpostConfigResponseTypeDef],
        "accessConfig": NotRequired[AccessConfigResponseTypeDef],
        "upgradePolicy": NotRequired[UpgradePolicyResponseTypeDef],
        "zonalShiftConfig": NotRequired[ZonalShiftConfigResponseTypeDef],
        "remoteNetworkConfig": NotRequired[RemoteNetworkConfigResponseTypeDef],
        "computeConfig": NotRequired[ComputeConfigResponseTypeDef],
        "storageConfig": NotRequired[StorageConfigResponseTypeDef],
        "deletionProtection": NotRequired[bool],
        "controlPlaneScalingConfig": NotRequired[ControlPlaneScalingConfigTypeDef],
    },
)

class RemoteNetworkConfigRequestTypeDef(TypedDict):
    remoteNodeNetworks: NotRequired[Sequence[RemoteNodeNetworkUnionTypeDef]]
    remotePodNetworks: NotRequired[Sequence[RemotePodNetworkUnionTypeDef]]

class AssociateEncryptionConfigResponseTypeDef(TypedDict):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateIdentityProviderConfigResponseTypeDef(TypedDict):
    update: UpdateTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUpdateResponseTypeDef(TypedDict):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateIdentityProviderConfigResponseTypeDef(TypedDict):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAddonResponseTypeDef(TypedDict):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCapabilityResponseTypeDef(TypedDict):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterConfigResponseTypeDef(TypedDict):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterVersionResponseTypeDef(TypedDict):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNodegroupConfigResponseTypeDef(TypedDict):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNodegroupVersionResponseTypeDef(TypedDict):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAddonResponseTypeDef(TypedDict):
    addon: AddonTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAddonResponseTypeDef(TypedDict):
    addon: AddonTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAddonResponseTypeDef(TypedDict):
    addon: AddonTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAddonVersionsResponseTypeDef(TypedDict):
    addons: List[AddonInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CapabilityConfigurationResponseTypeDef(TypedDict):
    argoCd: NotRequired[ArgoCdConfigResponseTypeDef]

class ArgoCdConfigRequestTypeDef(TypedDict):
    awsIdc: ArgoCdAwsIdcConfigRequestTypeDef
    namespace: NotRequired[str]
    rbacRoleMappings: NotRequired[Sequence[ArgoCdRoleMappingUnionTypeDef]]
    networkAccess: NotRequired[ArgoCdNetworkAccessConfigRequestTypeDef]

class UpdateRoleMappingsTypeDef(TypedDict):
    addOrUpdateRoleMappings: NotRequired[Sequence[ArgoCdRoleMappingUnionTypeDef]]
    removeRoleMappings: NotRequired[Sequence[ArgoCdRoleMappingTypeDef]]

InsightTypeDef = TypedDict(
    "InsightTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "category": NotRequired[CategoryType],
        "kubernetesVersion": NotRequired[str],
        "lastRefreshTime": NotRequired[datetime],
        "lastTransitionTime": NotRequired[datetime],
        "description": NotRequired[str],
        "insightStatus": NotRequired[InsightStatusTypeDef],
        "recommendation": NotRequired[str],
        "additionalInfo": NotRequired[Dict[str, str]],
        "resources": NotRequired[List[InsightResourceDetailTypeDef]],
        "categorySpecificSummary": NotRequired[InsightCategorySpecificSummaryTypeDef],
    },
)

class AssociateEncryptionConfigRequestTypeDef(TypedDict):
    clusterName: str
    encryptionConfig: Sequence[EncryptionConfigUnionTypeDef]
    clientRequestToken: NotRequired[str]

class CreateFargateProfileResponseTypeDef(TypedDict):
    fargateProfile: FargateProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFargateProfileResponseTypeDef(TypedDict):
    fargateProfile: FargateProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFargateProfileResponseTypeDef(TypedDict):
    fargateProfile: FargateProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNodegroupResponseTypeDef(TypedDict):
    nodegroup: NodegroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNodegroupResponseTypeDef(TypedDict):
    nodegroup: NodegroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNodegroupResponseTypeDef(TypedDict):
    nodegroup: NodegroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNodegroupRequestTypeDef(TypedDict):
    clusterName: str
    nodegroupName: str
    subnets: Sequence[str]
    nodeRole: str
    scalingConfig: NotRequired[NodegroupScalingConfigTypeDef]
    diskSize: NotRequired[int]
    instanceTypes: NotRequired[Sequence[str]]
    amiType: NotRequired[AMITypesType]
    remoteAccess: NotRequired[RemoteAccessConfigUnionTypeDef]
    labels: NotRequired[Mapping[str, str]]
    taints: NotRequired[Sequence[TaintTypeDef]]
    tags: NotRequired[Mapping[str, str]]
    clientRequestToken: NotRequired[str]
    launchTemplate: NotRequired[LaunchTemplateSpecificationTypeDef]
    updateConfig: NotRequired[NodegroupUpdateConfigTypeDef]
    nodeRepairConfig: NotRequired[NodeRepairConfigUnionTypeDef]
    capacityType: NotRequired[CapacityTypesType]
    version: NotRequired[str]
    releaseVersion: NotRequired[str]

class UpdateNodegroupConfigRequestTypeDef(TypedDict):
    clusterName: str
    nodegroupName: str
    labels: NotRequired[UpdateLabelsPayloadTypeDef]
    taints: NotRequired[UpdateTaintsPayloadTypeDef]
    scalingConfig: NotRequired[NodegroupScalingConfigTypeDef]
    updateConfig: NotRequired[NodegroupUpdateConfigTypeDef]
    nodeRepairConfig: NotRequired[NodeRepairConfigUnionTypeDef]
    clientRequestToken: NotRequired[str]

class CreateClusterResponseTypeDef(TypedDict):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterResponseTypeDef(TypedDict):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterClusterResponseTypeDef(TypedDict):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeClusterResponseTypeDef(TypedDict):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterClusterResponseTypeDef(TypedDict):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterRequestTypeDef(TypedDict):
    name: str
    roleArn: str
    resourcesVpcConfig: VpcConfigRequestTypeDef
    version: NotRequired[str]
    kubernetesNetworkConfig: NotRequired[KubernetesNetworkConfigRequestTypeDef]
    logging: NotRequired[LoggingUnionTypeDef]
    clientRequestToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    encryptionConfig: NotRequired[Sequence[EncryptionConfigUnionTypeDef]]
    outpostConfig: NotRequired[OutpostConfigRequestTypeDef]
    accessConfig: NotRequired[CreateAccessConfigRequestTypeDef]
    bootstrapSelfManagedAddons: NotRequired[bool]
    upgradePolicy: NotRequired[UpgradePolicyRequestTypeDef]
    zonalShiftConfig: NotRequired[ZonalShiftConfigRequestTypeDef]
    remoteNetworkConfig: NotRequired[RemoteNetworkConfigRequestTypeDef]
    computeConfig: NotRequired[ComputeConfigRequestTypeDef]
    storageConfig: NotRequired[StorageConfigRequestTypeDef]
    deletionProtection: NotRequired[bool]
    controlPlaneScalingConfig: NotRequired[ControlPlaneScalingConfigTypeDef]

class UpdateClusterConfigRequestTypeDef(TypedDict):
    name: str
    resourcesVpcConfig: NotRequired[VpcConfigRequestTypeDef]
    logging: NotRequired[LoggingUnionTypeDef]
    clientRequestToken: NotRequired[str]
    accessConfig: NotRequired[UpdateAccessConfigRequestTypeDef]
    upgradePolicy: NotRequired[UpgradePolicyRequestTypeDef]
    zonalShiftConfig: NotRequired[ZonalShiftConfigRequestTypeDef]
    computeConfig: NotRequired[ComputeConfigRequestTypeDef]
    kubernetesNetworkConfig: NotRequired[KubernetesNetworkConfigRequestTypeDef]
    storageConfig: NotRequired[StorageConfigRequestTypeDef]
    remoteNetworkConfig: NotRequired[RemoteNetworkConfigRequestTypeDef]
    deletionProtection: NotRequired[bool]
    controlPlaneScalingConfig: NotRequired[ControlPlaneScalingConfigTypeDef]

CapabilityTypeDef = TypedDict(
    "CapabilityTypeDef",
    {
        "capabilityName": NotRequired[str],
        "arn": NotRequired[str],
        "clusterName": NotRequired[str],
        "type": NotRequired[CapabilityTypeType],
        "roleArn": NotRequired[str],
        "status": NotRequired[CapabilityStatusType],
        "version": NotRequired[str],
        "configuration": NotRequired[CapabilityConfigurationResponseTypeDef],
        "tags": NotRequired[Dict[str, str]],
        "health": NotRequired[CapabilityHealthTypeDef],
        "createdAt": NotRequired[datetime],
        "modifiedAt": NotRequired[datetime],
        "deletePropagationPolicy": NotRequired[Literal["RETAIN"]],
    },
)

class CapabilityConfigurationRequestTypeDef(TypedDict):
    argoCd: NotRequired[ArgoCdConfigRequestTypeDef]

class UpdateArgoCdConfigTypeDef(TypedDict):
    rbacRoleMappings: NotRequired[UpdateRoleMappingsTypeDef]
    networkAccess: NotRequired[ArgoCdNetworkAccessConfigRequestTypeDef]

class DescribeInsightResponseTypeDef(TypedDict):
    insight: InsightTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCapabilityResponseTypeDef(TypedDict):
    capability: CapabilityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCapabilityResponseTypeDef(TypedDict):
    capability: CapabilityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCapabilityResponseTypeDef(TypedDict):
    capability: CapabilityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

CreateCapabilityRequestTypeDef = TypedDict(
    "CreateCapabilityRequestTypeDef",
    {
        "capabilityName": str,
        "clusterName": str,
        "type": CapabilityTypeType,
        "roleArn": str,
        "deletePropagationPolicy": Literal["RETAIN"],
        "clientRequestToken": NotRequired[str],
        "configuration": NotRequired[CapabilityConfigurationRequestTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)

class UpdateCapabilityConfigurationTypeDef(TypedDict):
    argoCd: NotRequired[UpdateArgoCdConfigTypeDef]

class UpdateCapabilityRequestTypeDef(TypedDict):
    clusterName: str
    capabilityName: str
    roleArn: NotRequired[str]
    configuration: NotRequired[UpdateCapabilityConfigurationTypeDef]
    clientRequestToken: NotRequired[str]
    deletePropagationPolicy: NotRequired[Literal["RETAIN"]]
