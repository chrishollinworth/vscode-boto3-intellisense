"""
Type annotations for eks service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_eks import EKSClient

    client: EKSClient = boto3.client("eks")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AMITypesType,
    CapacityTypesType,
    EksAnywhereSubscriptionStatusType,
    ResolveConflictsType,
)
from .paginator import (
    DescribeAddonVersionsPaginator,
    ListAccessEntriesPaginator,
    ListAccessPoliciesPaginator,
    ListAddonsPaginator,
    ListAssociatedAccessPoliciesPaginator,
    ListClustersPaginator,
    ListEksAnywhereSubscriptionsPaginator,
    ListFargateProfilesPaginator,
    ListIdentityProviderConfigsPaginator,
    ListInsightsPaginator,
    ListNodegroupsPaginator,
    ListPodIdentityAssociationsPaginator,
    ListUpdatesPaginator,
)
from .type_defs import (
    AccessScopeTypeDef,
    AddonPodIdentityAssociationsTypeDef,
    AssociateAccessPolicyResponseTypeDef,
    AssociateEncryptionConfigResponseTypeDef,
    AssociateIdentityProviderConfigResponseTypeDef,
    ConnectorConfigRequestTypeDef,
    CreateAccessConfigRequestTypeDef,
    CreateAccessEntryResponseTypeDef,
    CreateAddonResponseTypeDef,
    CreateClusterResponseTypeDef,
    CreateEksAnywhereSubscriptionResponseTypeDef,
    CreateFargateProfileResponseTypeDef,
    CreateNodegroupResponseTypeDef,
    CreatePodIdentityAssociationResponseTypeDef,
    DeleteAddonResponseTypeDef,
    DeleteClusterResponseTypeDef,
    DeleteEksAnywhereSubscriptionResponseTypeDef,
    DeleteFargateProfileResponseTypeDef,
    DeleteNodegroupResponseTypeDef,
    DeletePodIdentityAssociationResponseTypeDef,
    DeregisterClusterResponseTypeDef,
    DescribeAccessEntryResponseTypeDef,
    DescribeAddonConfigurationResponseTypeDef,
    DescribeAddonResponseTypeDef,
    DescribeAddonVersionsResponseTypeDef,
    DescribeClusterResponseTypeDef,
    DescribeEksAnywhereSubscriptionResponseTypeDef,
    DescribeFargateProfileResponseTypeDef,
    DescribeIdentityProviderConfigResponseTypeDef,
    DescribeInsightResponseTypeDef,
    DescribeNodegroupResponseTypeDef,
    DescribePodIdentityAssociationResponseTypeDef,
    DescribeUpdateResponseTypeDef,
    DisassociateIdentityProviderConfigResponseTypeDef,
    EksAnywhereSubscriptionTermTypeDef,
    EncryptionConfigTypeDef,
    FargateProfileSelectorTypeDef,
    IdentityProviderConfigTypeDef,
    InsightsFilterTypeDef,
    KubernetesNetworkConfigRequestTypeDef,
    LaunchTemplateSpecificationTypeDef,
    ListAccessEntriesResponseTypeDef,
    ListAccessPoliciesResponseTypeDef,
    ListAddonsResponseTypeDef,
    ListAssociatedAccessPoliciesResponseTypeDef,
    ListClustersResponseTypeDef,
    ListEksAnywhereSubscriptionsResponseTypeDef,
    ListFargateProfilesResponseTypeDef,
    ListIdentityProviderConfigsResponseTypeDef,
    ListInsightsResponseTypeDef,
    ListNodegroupsResponseTypeDef,
    ListPodIdentityAssociationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUpdatesResponseTypeDef,
    LoggingTypeDef,
    NodegroupScalingConfigTypeDef,
    NodegroupUpdateConfigTypeDef,
    OidcIdentityProviderConfigRequestTypeDef,
    OutpostConfigRequestTypeDef,
    RegisterClusterResponseTypeDef,
    RemoteAccessConfigTypeDef,
    TaintTypeDef,
    UpdateAccessConfigRequestTypeDef,
    UpdateAccessEntryResponseTypeDef,
    UpdateAddonResponseTypeDef,
    UpdateClusterConfigResponseTypeDef,
    UpdateClusterVersionResponseTypeDef,
    UpdateEksAnywhereSubscriptionResponseTypeDef,
    UpdateLabelsPayloadTypeDef,
    UpdateNodegroupConfigResponseTypeDef,
    UpdateNodegroupVersionResponseTypeDef,
    UpdatePodIdentityAssociationResponseTypeDef,
    UpdateTaintsPayloadTypeDef,
    VpcConfigRequestTypeDef,
)
from .waiter import (
    AddonActiveWaiter,
    AddonDeletedWaiter,
    ClusterActiveWaiter,
    ClusterDeletedWaiter,
    FargateProfileActiveWaiter,
    FargateProfileDeletedWaiter,
    NodegroupActiveWaiter,
    NodegroupDeletedWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("EKSClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClientException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourcePropagationDelayException: Type[BotocoreClientError]
    ServerException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    UnsupportedAvailabilityZoneException: Type[BotocoreClientError]

class EKSClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        EKSClient exceptions.
        """

    def associate_access_policy(
        self,
        *,
        clusterName: str,
        principalArn: str,
        policyArn: str,
        accessScope: "AccessScopeTypeDef"
    ) -> AssociateAccessPolicyResponseTypeDef:
        """
        Associates an access policy and its scope to an access entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.associate_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#associate_access_policy)
        """

    def associate_encryption_config(
        self,
        *,
        clusterName: str,
        encryptionConfig: List["EncryptionConfigTypeDef"],
        clientRequestToken: str = None
    ) -> AssociateEncryptionConfigResponseTypeDef:
        """
        Associates an encryption configuration to an existing cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.associate_encryption_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#associate_encryption_config)
        """

    def associate_identity_provider_config(
        self,
        *,
        clusterName: str,
        oidc: "OidcIdentityProviderConfigRequestTypeDef",
        tags: Dict[str, str] = None,
        clientRequestToken: str = None
    ) -> AssociateIdentityProviderConfigResponseTypeDef:
        """
        Associates an identity provider configuration to a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.associate_identity_provider_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#associate_identity_provider_config)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#close)
        """

    def create_access_entry(
        self,
        *,
        clusterName: str,
        principalArn: str,
        kubernetesGroups: List[str] = None,
        tags: Dict[str, str] = None,
        clientRequestToken: str = None,
        username: str = None,
        type: str = None
    ) -> CreateAccessEntryResponseTypeDef:
        """
        Creates an access entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.create_access_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#create_access_entry)
        """

    def create_addon(
        self,
        *,
        clusterName: str,
        addonName: str,
        addonVersion: str = None,
        serviceAccountRoleArn: str = None,
        resolveConflicts: ResolveConflictsType = None,
        clientRequestToken: str = None,
        tags: Dict[str, str] = None,
        configurationValues: str = None,
        podIdentityAssociations: List["AddonPodIdentityAssociationsTypeDef"] = None
    ) -> CreateAddonResponseTypeDef:
        """
        Creates an Amazon EKS add-on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.create_addon)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#create_addon)
        """

    def create_cluster(
        self,
        *,
        name: str,
        roleArn: str,
        resourcesVpcConfig: "VpcConfigRequestTypeDef",
        version: str = None,
        kubernetesNetworkConfig: "KubernetesNetworkConfigRequestTypeDef" = None,
        logging: "LoggingTypeDef" = None,
        clientRequestToken: str = None,
        tags: Dict[str, str] = None,
        encryptionConfig: List["EncryptionConfigTypeDef"] = None,
        outpostConfig: "OutpostConfigRequestTypeDef" = None,
        accessConfig: "CreateAccessConfigRequestTypeDef" = None
    ) -> CreateClusterResponseTypeDef:
        """
        Creates an Amazon EKS control plane.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.create_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#create_cluster)
        """

    def create_eks_anywhere_subscription(
        self,
        *,
        name: str,
        term: "EksAnywhereSubscriptionTermTypeDef",
        licenseQuantity: int = None,
        licenseType: Literal["Cluster"] = None,
        autoRenew: bool = None,
        clientRequestToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreateEksAnywhereSubscriptionResponseTypeDef:
        """
        Creates an EKS Anywhere subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.create_eks_anywhere_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#create_eks_anywhere_subscription)
        """

    def create_fargate_profile(
        self,
        *,
        fargateProfileName: str,
        clusterName: str,
        podExecutionRoleArn: str,
        subnets: List[str] = None,
        selectors: List["FargateProfileSelectorTypeDef"] = None,
        clientRequestToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreateFargateProfileResponseTypeDef:
        """
        Creates an Fargate profile for your Amazon EKS cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.create_fargate_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#create_fargate_profile)
        """

    def create_nodegroup(
        self,
        *,
        clusterName: str,
        nodegroupName: str,
        subnets: List[str],
        nodeRole: str,
        scalingConfig: "NodegroupScalingConfigTypeDef" = None,
        diskSize: int = None,
        instanceTypes: List[str] = None,
        amiType: AMITypesType = None,
        remoteAccess: "RemoteAccessConfigTypeDef" = None,
        labels: Dict[str, str] = None,
        taints: List["TaintTypeDef"] = None,
        tags: Dict[str, str] = None,
        clientRequestToken: str = None,
        launchTemplate: "LaunchTemplateSpecificationTypeDef" = None,
        updateConfig: "NodegroupUpdateConfigTypeDef" = None,
        capacityType: CapacityTypesType = None,
        version: str = None,
        releaseVersion: str = None
    ) -> CreateNodegroupResponseTypeDef:
        """
        Creates a managed node group for an Amazon EKS cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.create_nodegroup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#create_nodegroup)
        """

    def create_pod_identity_association(
        self,
        *,
        clusterName: str,
        namespace: str,
        serviceAccount: str,
        roleArn: str,
        clientRequestToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreatePodIdentityAssociationResponseTypeDef:
        """
        Creates an EKS Pod Identity association between a service account in an Amazon
        EKS cluster and an IAM role with *EKS Pod Identity*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.create_pod_identity_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#create_pod_identity_association)
        """

    def delete_access_entry(self, *, clusterName: str, principalArn: str) -> Dict[str, Any]:
        """
        Deletes an access entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.delete_access_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#delete_access_entry)
        """

    def delete_addon(
        self, *, clusterName: str, addonName: str, preserve: bool = None
    ) -> DeleteAddonResponseTypeDef:
        """
        Deletes an Amazon EKS add-on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.delete_addon)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#delete_addon)
        """

    def delete_cluster(self, *, name: str) -> DeleteClusterResponseTypeDef:
        """
        Deletes an Amazon EKS cluster control plane.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.delete_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#delete_cluster)
        """

    def delete_eks_anywhere_subscription(
        self, *, id: str
    ) -> DeleteEksAnywhereSubscriptionResponseTypeDef:
        """
        Deletes an expired or inactive subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.delete_eks_anywhere_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#delete_eks_anywhere_subscription)
        """

    def delete_fargate_profile(
        self, *, clusterName: str, fargateProfileName: str
    ) -> DeleteFargateProfileResponseTypeDef:
        """
        Deletes an Fargate profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.delete_fargate_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#delete_fargate_profile)
        """

    def delete_nodegroup(
        self, *, clusterName: str, nodegroupName: str
    ) -> DeleteNodegroupResponseTypeDef:
        """
        Deletes a managed node group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.delete_nodegroup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#delete_nodegroup)
        """

    def delete_pod_identity_association(
        self, *, clusterName: str, associationId: str
    ) -> DeletePodIdentityAssociationResponseTypeDef:
        """
        Deletes a EKS Pod Identity association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.delete_pod_identity_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#delete_pod_identity_association)
        """

    def deregister_cluster(self, *, name: str) -> DeregisterClusterResponseTypeDef:
        """
        Deregisters a connected cluster to remove it from the Amazon EKS control plane.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.deregister_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#deregister_cluster)
        """

    def describe_access_entry(
        self, *, clusterName: str, principalArn: str
    ) -> DescribeAccessEntryResponseTypeDef:
        """
        Describes an access entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.describe_access_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#describe_access_entry)
        """

    def describe_addon(self, *, clusterName: str, addonName: str) -> DescribeAddonResponseTypeDef:
        """
        Describes an Amazon EKS add-on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.describe_addon)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#describe_addon)
        """

    def describe_addon_configuration(
        self, *, addonName: str, addonVersion: str
    ) -> DescribeAddonConfigurationResponseTypeDef:
        """
        Returns configuration options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.describe_addon_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#describe_addon_configuration)
        """

    def describe_addon_versions(
        self,
        *,
        kubernetesVersion: str = None,
        maxResults: int = None,
        nextToken: str = None,
        addonName: str = None,
        types: List[str] = None,
        publishers: List[str] = None,
        owners: List[str] = None
    ) -> DescribeAddonVersionsResponseTypeDef:
        """
        Describes the versions for an add-on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.describe_addon_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#describe_addon_versions)
        """

    def describe_cluster(self, *, name: str) -> DescribeClusterResponseTypeDef:
        """
        Describes an Amazon EKS cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.describe_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#describe_cluster)
        """

    def describe_eks_anywhere_subscription(
        self, *, id: str
    ) -> DescribeEksAnywhereSubscriptionResponseTypeDef:
        """
        Returns descriptive information about a subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.describe_eks_anywhere_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#describe_eks_anywhere_subscription)
        """

    def describe_fargate_profile(
        self, *, clusterName: str, fargateProfileName: str
    ) -> DescribeFargateProfileResponseTypeDef:
        """
        Describes an Fargate profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.describe_fargate_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#describe_fargate_profile)
        """

    def describe_identity_provider_config(
        self, *, clusterName: str, identityProviderConfig: "IdentityProviderConfigTypeDef"
    ) -> DescribeIdentityProviderConfigResponseTypeDef:
        """
        Describes an identity provider configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.describe_identity_provider_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#describe_identity_provider_config)
        """

    def describe_insight(self, *, clusterName: str, id: str) -> DescribeInsightResponseTypeDef:
        """
        Returns details about an insight that you specify using its ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.describe_insight)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#describe_insight)
        """

    def describe_nodegroup(
        self, *, clusterName: str, nodegroupName: str
    ) -> DescribeNodegroupResponseTypeDef:
        """
        Describes a managed node group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.describe_nodegroup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#describe_nodegroup)
        """

    def describe_pod_identity_association(
        self, *, clusterName: str, associationId: str
    ) -> DescribePodIdentityAssociationResponseTypeDef:
        """
        Returns descriptive information about an EKS Pod Identity association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.describe_pod_identity_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#describe_pod_identity_association)
        """

    def describe_update(
        self, *, name: str, updateId: str, nodegroupName: str = None, addonName: str = None
    ) -> DescribeUpdateResponseTypeDef:
        """
        Describes an update to an Amazon EKS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.describe_update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#describe_update)
        """

    def disassociate_access_policy(
        self, *, clusterName: str, principalArn: str, policyArn: str
    ) -> Dict[str, Any]:
        """
        Disassociates an access policy from an access entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.disassociate_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#disassociate_access_policy)
        """

    def disassociate_identity_provider_config(
        self,
        *,
        clusterName: str,
        identityProviderConfig: "IdentityProviderConfigTypeDef",
        clientRequestToken: str = None
    ) -> DisassociateIdentityProviderConfigResponseTypeDef:
        """
        Disassociates an identity provider configuration from a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.disassociate_identity_provider_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#disassociate_identity_provider_config)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#generate_presigned_url)
        """

    def list_access_entries(
        self,
        *,
        clusterName: str,
        associatedPolicyArn: str = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListAccessEntriesResponseTypeDef:
        """
        Lists the access entries for your cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.list_access_entries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#list_access_entries)
        """

    def list_access_policies(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListAccessPoliciesResponseTypeDef:
        """
        Lists the available access policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.list_access_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#list_access_policies)
        """

    def list_addons(
        self, *, clusterName: str, maxResults: int = None, nextToken: str = None
    ) -> ListAddonsResponseTypeDef:
        """
        Lists the installed add-ons.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.list_addons)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#list_addons)
        """

    def list_associated_access_policies(
        self, *, clusterName: str, principalArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListAssociatedAccessPoliciesResponseTypeDef:
        """
        Lists the access policies associated with an access entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.list_associated_access_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#list_associated_access_policies)
        """

    def list_clusters(
        self, *, maxResults: int = None, nextToken: str = None, include: List[str] = None
    ) -> ListClustersResponseTypeDef:
        """
        Lists the Amazon EKS clusters in your Amazon Web Services account in the
        specified Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.list_clusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#list_clusters)
        """

    def list_eks_anywhere_subscriptions(
        self,
        *,
        maxResults: int = None,
        nextToken: str = None,
        includeStatus: List[EksAnywhereSubscriptionStatusType] = None
    ) -> ListEksAnywhereSubscriptionsResponseTypeDef:
        """
        Displays the full description of the subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.list_eks_anywhere_subscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#list_eks_anywhere_subscriptions)
        """

    def list_fargate_profiles(
        self, *, clusterName: str, maxResults: int = None, nextToken: str = None
    ) -> ListFargateProfilesResponseTypeDef:
        """
        Lists the Fargate profiles associated with the specified cluster in your Amazon
        Web Services account in the specified Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.list_fargate_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#list_fargate_profiles)
        """

    def list_identity_provider_configs(
        self, *, clusterName: str, maxResults: int = None, nextToken: str = None
    ) -> ListIdentityProviderConfigsResponseTypeDef:
        """
        Lists the identity provider configurations for your cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.list_identity_provider_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#list_identity_provider_configs)
        """

    def list_insights(
        self,
        *,
        clusterName: str,
        filter: "InsightsFilterTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListInsightsResponseTypeDef:
        """
        Returns a list of all insights checked for against the specified cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.list_insights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#list_insights)
        """

    def list_nodegroups(
        self, *, clusterName: str, maxResults: int = None, nextToken: str = None
    ) -> ListNodegroupsResponseTypeDef:
        """
        Lists the managed node groups associated with the specified cluster in your
        Amazon Web Services account in the specified Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.list_nodegroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#list_nodegroups)
        """

    def list_pod_identity_associations(
        self,
        *,
        clusterName: str,
        namespace: str = None,
        serviceAccount: str = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListPodIdentityAssociationsResponseTypeDef:
        """
        List the EKS Pod Identity associations in a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.list_pod_identity_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#list_pod_identity_associations)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        List the tags for an Amazon EKS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#list_tags_for_resource)
        """

    def list_updates(
        self,
        *,
        name: str,
        nodegroupName: str = None,
        addonName: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListUpdatesResponseTypeDef:
        """
        Lists the updates associated with an Amazon EKS resource in your Amazon Web
        Services account, in the specified Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.list_updates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#list_updates)
        """

    def register_cluster(
        self,
        *,
        name: str,
        connectorConfig: "ConnectorConfigRequestTypeDef",
        clientRequestToken: str = None,
        tags: Dict[str, str] = None
    ) -> RegisterClusterResponseTypeDef:
        """
        Connects a Kubernetes cluster to the Amazon EKS control plane.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.register_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#register_cluster)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Associates the specified tags to an Amazon EKS resource with the specified
        `resourceArn`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Deletes specified tags from an Amazon EKS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#untag_resource)
        """

    def update_access_entry(
        self,
        *,
        clusterName: str,
        principalArn: str,
        kubernetesGroups: List[str] = None,
        clientRequestToken: str = None,
        username: str = None
    ) -> UpdateAccessEntryResponseTypeDef:
        """
        Updates an access entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.update_access_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#update_access_entry)
        """

    def update_addon(
        self,
        *,
        clusterName: str,
        addonName: str,
        addonVersion: str = None,
        serviceAccountRoleArn: str = None,
        resolveConflicts: ResolveConflictsType = None,
        clientRequestToken: str = None,
        configurationValues: str = None,
        podIdentityAssociations: List["AddonPodIdentityAssociationsTypeDef"] = None
    ) -> UpdateAddonResponseTypeDef:
        """
        Updates an Amazon EKS add-on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.update_addon)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#update_addon)
        """

    def update_cluster_config(
        self,
        *,
        name: str,
        resourcesVpcConfig: "VpcConfigRequestTypeDef" = None,
        logging: "LoggingTypeDef" = None,
        clientRequestToken: str = None,
        accessConfig: "UpdateAccessConfigRequestTypeDef" = None
    ) -> UpdateClusterConfigResponseTypeDef:
        """
        Updates an Amazon EKS cluster configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.update_cluster_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#update_cluster_config)
        """

    def update_cluster_version(
        self, *, name: str, version: str, clientRequestToken: str = None
    ) -> UpdateClusterVersionResponseTypeDef:
        """
        Updates an Amazon EKS cluster to the specified Kubernetes version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.update_cluster_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#update_cluster_version)
        """

    def update_eks_anywhere_subscription(
        self, *, id: str, autoRenew: bool, clientRequestToken: str = None
    ) -> UpdateEksAnywhereSubscriptionResponseTypeDef:
        """
        Update an EKS Anywhere Subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.update_eks_anywhere_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#update_eks_anywhere_subscription)
        """

    def update_nodegroup_config(
        self,
        *,
        clusterName: str,
        nodegroupName: str,
        labels: "UpdateLabelsPayloadTypeDef" = None,
        taints: "UpdateTaintsPayloadTypeDef" = None,
        scalingConfig: "NodegroupScalingConfigTypeDef" = None,
        updateConfig: "NodegroupUpdateConfigTypeDef" = None,
        clientRequestToken: str = None
    ) -> UpdateNodegroupConfigResponseTypeDef:
        """
        Updates an Amazon EKS managed node group configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.update_nodegroup_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#update_nodegroup_config)
        """

    def update_nodegroup_version(
        self,
        *,
        clusterName: str,
        nodegroupName: str,
        version: str = None,
        releaseVersion: str = None,
        launchTemplate: "LaunchTemplateSpecificationTypeDef" = None,
        force: bool = None,
        clientRequestToken: str = None
    ) -> UpdateNodegroupVersionResponseTypeDef:
        """
        Updates the Kubernetes version or AMI version of an Amazon EKS managed node
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.update_nodegroup_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#update_nodegroup_version)
        """

    def update_pod_identity_association(
        self,
        *,
        clusterName: str,
        associationId: str,
        roleArn: str = None,
        clientRequestToken: str = None
    ) -> UpdatePodIdentityAssociationResponseTypeDef:
        """
        Updates a EKS Pod Identity association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Client.update_pod_identity_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#update_pod_identity_association)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_addon_versions"]
    ) -> DescribeAddonVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Paginator.DescribeAddonVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#describeaddonversionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_access_entries"]
    ) -> ListAccessEntriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Paginator.ListAccessEntries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listaccessentriespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_access_policies"]
    ) -> ListAccessPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Paginator.ListAccessPolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listaccesspoliciespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_addons"]) -> ListAddonsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Paginator.ListAddons)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listaddonspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_associated_access_policies"]
    ) -> ListAssociatedAccessPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Paginator.ListAssociatedAccessPolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listassociatedaccesspoliciespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_clusters"]) -> ListClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Paginator.ListClusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listclusterspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_eks_anywhere_subscriptions"]
    ) -> ListEksAnywhereSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Paginator.ListEksAnywhereSubscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listeksanywheresubscriptionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_fargate_profiles"]
    ) -> ListFargateProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Paginator.ListFargateProfiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listfargateprofilespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_identity_provider_configs"]
    ) -> ListIdentityProviderConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Paginator.ListIdentityProviderConfigs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listidentityproviderconfigspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_insights"]) -> ListInsightsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Paginator.ListInsights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listinsightspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_nodegroups"]) -> ListNodegroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Paginator.ListNodegroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listnodegroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_pod_identity_associations"]
    ) -> ListPodIdentityAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Paginator.ListPodIdentityAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listpodidentityassociationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_updates"]) -> ListUpdatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Paginator.ListUpdates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listupdatespaginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["addon_active"]) -> AddonActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Waiter.AddonActive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#addonactivewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["addon_deleted"]) -> AddonDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Waiter.AddonDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#addondeletedwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["cluster_active"]) -> ClusterActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Waiter.ClusterActive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#clusteractivewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["cluster_deleted"]) -> ClusterDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Waiter.ClusterDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#clusterdeletedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["fargate_profile_active"]
    ) -> FargateProfileActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Waiter.FargateProfileActive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#fargateprofileactivewaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["fargate_profile_deleted"]
    ) -> FargateProfileDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Waiter.FargateProfileDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#fargateprofiledeletedwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["nodegroup_active"]) -> NodegroupActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Waiter.NodegroupActive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#nodegroupactivewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["nodegroup_deleted"]) -> NodegroupDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/eks.html#EKS.Waiter.NodegroupDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#nodegroupdeletedwaiter)
        """
