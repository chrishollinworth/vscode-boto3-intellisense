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

from .literals import AMITypesType, CapacityTypesType, ResolveConflictsType
from .paginator import (
    DescribeAddonVersionsPaginator,
    ListAddonsPaginator,
    ListClustersPaginator,
    ListFargateProfilesPaginator,
    ListIdentityProviderConfigsPaginator,
    ListNodegroupsPaginator,
    ListUpdatesPaginator,
)
from .type_defs import (
    AssociateEncryptionConfigResponseTypeDef,
    AssociateIdentityProviderConfigResponseTypeDef,
    CreateAddonResponseTypeDef,
    CreateClusterResponseTypeDef,
    CreateFargateProfileResponseTypeDef,
    CreateNodegroupResponseTypeDef,
    DeleteAddonResponseTypeDef,
    DeleteClusterResponseTypeDef,
    DeleteFargateProfileResponseTypeDef,
    DeleteNodegroupResponseTypeDef,
    DescribeAddonResponseTypeDef,
    DescribeAddonVersionsResponseTypeDef,
    DescribeClusterResponseTypeDef,
    DescribeFargateProfileResponseTypeDef,
    DescribeIdentityProviderConfigResponseTypeDef,
    DescribeNodegroupResponseTypeDef,
    DescribeUpdateResponseTypeDef,
    DisassociateIdentityProviderConfigResponseTypeDef,
    EncryptionConfigTypeDef,
    FargateProfileSelectorTypeDef,
    IdentityProviderConfigTypeDef,
    KubernetesNetworkConfigRequestTypeDef,
    LaunchTemplateSpecificationTypeDef,
    ListAddonsResponseTypeDef,
    ListClustersResponseTypeDef,
    ListFargateProfilesResponseTypeDef,
    ListIdentityProviderConfigsResponseTypeDef,
    ListNodegroupsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUpdatesResponseTypeDef,
    LoggingTypeDef,
    NodegroupScalingConfigTypeDef,
    NodegroupUpdateConfigTypeDef,
    OidcIdentityProviderConfigRequestTypeDef,
    RemoteAccessConfigTypeDef,
    TaintTypeDef,
    UpdateAddonResponseTypeDef,
    UpdateClusterConfigResponseTypeDef,
    UpdateClusterVersionResponseTypeDef,
    UpdateLabelsPayloadTypeDef,
    UpdateNodegroupConfigResponseTypeDef,
    UpdateNodegroupVersionResponseTypeDef,
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
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClientException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServerException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    UnsupportedAvailabilityZoneException: Type[BotocoreClientError]

class EKSClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        EKSClient exceptions.
        """
    def associate_encryption_config(
        self,
        *,
        clusterName: str,
        encryptionConfig: List["EncryptionConfigTypeDef"],
        clientRequestToken: str = None
    ) -> AssociateEncryptionConfigResponseTypeDef:
        """
        Associate encryption configuration to an existing cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.associate_encryption_config)
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
        Associate an identity provider configuration to a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.associate_identity_provider_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#associate_identity_provider_config)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#can_paginate)
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
        tags: Dict[str, str] = None
    ) -> CreateAddonResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.create_addon)
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
        encryptionConfig: List["EncryptionConfigTypeDef"] = None
    ) -> CreateClusterResponseTypeDef:
        """
        Creates an Amazon EKS control plane.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.create_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#create_cluster)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.create_fargate_profile)
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
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.create_nodegroup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#create_nodegroup)
        """
    def delete_addon(self, *, clusterName: str, addonName: str) -> DeleteAddonResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.delete_addon)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#delete_addon)
        """
    def delete_cluster(self, *, name: str) -> DeleteClusterResponseTypeDef:
        """
        Deletes the Amazon EKS cluster control plane.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.delete_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#delete_cluster)
        """
    def delete_fargate_profile(
        self, *, clusterName: str, fargateProfileName: str
    ) -> DeleteFargateProfileResponseTypeDef:
        """
        Deletes an Fargate profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.delete_fargate_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#delete_fargate_profile)
        """
    def delete_nodegroup(
        self, *, clusterName: str, nodegroupName: str
    ) -> DeleteNodegroupResponseTypeDef:
        """
        Deletes an Amazon EKS node group for a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.delete_nodegroup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#delete_nodegroup)
        """
    def describe_addon(self, *, clusterName: str, addonName: str) -> DescribeAddonResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.describe_addon)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#describe_addon)
        """
    def describe_addon_versions(
        self,
        *,
        kubernetesVersion: str = None,
        maxResults: int = None,
        nextToken: str = None,
        addonName: str = None
    ) -> DescribeAddonVersionsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.describe_addon_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#describe_addon_versions)
        """
    def describe_cluster(self, *, name: str) -> DescribeClusterResponseTypeDef:
        """
        Returns descriptive information about an Amazon EKS cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.describe_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#describe_cluster)
        """
    def describe_fargate_profile(
        self, *, clusterName: str, fargateProfileName: str
    ) -> DescribeFargateProfileResponseTypeDef:
        """
        Returns descriptive information about an Fargate profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.describe_fargate_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#describe_fargate_profile)
        """
    def describe_identity_provider_config(
        self, *, clusterName: str, identityProviderConfig: "IdentityProviderConfigTypeDef"
    ) -> DescribeIdentityProviderConfigResponseTypeDef:
        """
        Returns descriptive information about an identity provider configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.describe_identity_provider_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#describe_identity_provider_config)
        """
    def describe_nodegroup(
        self, *, clusterName: str, nodegroupName: str
    ) -> DescribeNodegroupResponseTypeDef:
        """
        Returns descriptive information about an Amazon EKS node group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.describe_nodegroup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#describe_nodegroup)
        """
    def describe_update(
        self, *, name: str, updateId: str, nodegroupName: str = None, addonName: str = None
    ) -> DescribeUpdateResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.describe_update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#describe_update)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.disassociate_identity_provider_config)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#generate_presigned_url)
        """
    def list_addons(
        self, *, clusterName: str, maxResults: int = None, nextToken: str = None
    ) -> ListAddonsResponseTypeDef:
        """
        Lists the available add-ons.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.list_addons)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#list_addons)
        """
    def list_clusters(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListClustersResponseTypeDef:
        """
        Lists the Amazon EKS clusters in your Amazon Web Services account in the
        specified Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.list_clusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#list_clusters)
        """
    def list_fargate_profiles(
        self, *, clusterName: str, maxResults: int = None, nextToken: str = None
    ) -> ListFargateProfilesResponseTypeDef:
        """
        Lists the Fargate profiles associated with the specified cluster in your Amazon
        Web Services account in the specified Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.list_fargate_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#list_fargate_profiles)
        """
    def list_identity_provider_configs(
        self, *, clusterName: str, maxResults: int = None, nextToken: str = None
    ) -> ListIdentityProviderConfigsResponseTypeDef:
        """
        A list of identity provider configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.list_identity_provider_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#list_identity_provider_configs)
        """
    def list_nodegroups(
        self, *, clusterName: str, maxResults: int = None, nextToken: str = None
    ) -> ListNodegroupsResponseTypeDef:
        """
        Lists the Amazon EKS managed node groups associated with the specified cluster
        in your Amazon Web Services account in the specified Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.list_nodegroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#list_nodegroups)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        List the tags for an Amazon EKS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.list_tags_for_resource)
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
        Lists the updates associated with an Amazon EKS cluster or managed node group in
        your Amazon Web Services account, in the specified Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.list_updates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#list_updates)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Associates the specified tags to a resource with the specified `resourceArn`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Deletes specified tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#untag_resource)
        """
    def update_addon(
        self,
        *,
        clusterName: str,
        addonName: str,
        addonVersion: str = None,
        serviceAccountRoleArn: str = None,
        resolveConflicts: ResolveConflictsType = None,
        clientRequestToken: str = None
    ) -> UpdateAddonResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.update_addon)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#update_addon)
        """
    def update_cluster_config(
        self,
        *,
        name: str,
        resourcesVpcConfig: "VpcConfigRequestTypeDef" = None,
        logging: "LoggingTypeDef" = None,
        clientRequestToken: str = None
    ) -> UpdateClusterConfigResponseTypeDef:
        """
        Updates an Amazon EKS cluster configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.update_cluster_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#update_cluster_config)
        """
    def update_cluster_version(
        self, *, name: str, version: str, clientRequestToken: str = None
    ) -> UpdateClusterVersionResponseTypeDef:
        """
        Updates an Amazon EKS cluster to the specified Kubernetes version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.update_cluster_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#update_cluster_version)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.update_nodegroup_config)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Client.update_nodegroup_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/client.html#update_nodegroup_version)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_addon_versions"]
    ) -> DescribeAddonVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Paginator.DescribeAddonVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#describeaddonversionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_addons"]) -> ListAddonsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Paginator.ListAddons)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listaddonspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_clusters"]) -> ListClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Paginator.ListClusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listclusterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_fargate_profiles"]
    ) -> ListFargateProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Paginator.ListFargateProfiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listfargateprofilespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_identity_provider_configs"]
    ) -> ListIdentityProviderConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Paginator.ListIdentityProviderConfigs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listidentityproviderconfigspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_nodegroups"]) -> ListNodegroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Paginator.ListNodegroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listnodegroupspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_updates"]) -> ListUpdatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Paginator.ListUpdates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/paginators.html#listupdatespaginator)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["addon_active"]) -> AddonActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Waiter.AddonActive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#addonactivewaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["addon_deleted"]) -> AddonDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Waiter.AddonDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#addondeletedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["cluster_active"]) -> ClusterActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Waiter.ClusterActive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#clusteractivewaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["cluster_deleted"]) -> ClusterDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Waiter.ClusterDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#clusterdeletedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["fargate_profile_active"]
    ) -> FargateProfileActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Waiter.FargateProfileActive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#fargateprofileactivewaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["fargate_profile_deleted"]
    ) -> FargateProfileDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Waiter.FargateProfileDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#fargateprofiledeletedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["nodegroup_active"]) -> NodegroupActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Waiter.NodegroupActive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#nodegroupactivewaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["nodegroup_deleted"]) -> NodegroupDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/eks.html#EKS.Waiter.NodegroupDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/waiters.html#nodegroupdeletedwaiter)
        """
