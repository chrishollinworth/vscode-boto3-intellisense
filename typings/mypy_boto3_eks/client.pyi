# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for eks service client

Usage::

    ```python
    import boto3
    from mypy_boto3_eks import EKSClient

    client: EKSClient = boto3.client("eks")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_eks.paginator import (
    ListClustersPaginator,
    ListFargateProfilesPaginator,
    ListNodegroupsPaginator,
    ListUpdatesPaginator,
)
from mypy_boto3_eks.type_defs import (
    CreateClusterResponseTypeDef,
    CreateFargateProfileResponseTypeDef,
    CreateNodegroupResponseTypeDef,
    DeleteClusterResponseTypeDef,
    DeleteFargateProfileResponseTypeDef,
    DeleteNodegroupResponseTypeDef,
    DescribeClusterResponseTypeDef,
    DescribeFargateProfileResponseTypeDef,
    DescribeNodegroupResponseTypeDef,
    DescribeUpdateResponseTypeDef,
    EncryptionConfigTypeDef,
    FargateProfileSelectorTypeDef,
    KubernetesNetworkConfigRequestTypeDef,
    LaunchTemplateSpecificationTypeDef,
    ListClustersResponseTypeDef,
    ListFargateProfilesResponseTypeDef,
    ListNodegroupsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUpdatesResponseTypeDef,
    LoggingTypeDef,
    NodegroupScalingConfigTypeDef,
    RemoteAccessConfigTypeDef,
    UpdateClusterConfigResponseTypeDef,
    UpdateClusterVersionResponseTypeDef,
    UpdateLabelsPayloadTypeDef,
    UpdateNodegroupConfigResponseTypeDef,
    UpdateNodegroupVersionResponseTypeDef,
    VpcConfigRequestTypeDef,
)
from mypy_boto3_eks.waiter import (
    ClusterActiveWaiter,
    ClusterDeletedWaiter,
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


class EKSClient:
    """
    [EKS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client.can_paginate)
        """

    def create_cluster(
        self,
        name: str,
        roleArn: str,
        resourcesVpcConfig: VpcConfigRequestTypeDef,
        version: str = None,
        kubernetesNetworkConfig: KubernetesNetworkConfigRequestTypeDef = None,
        logging: "LoggingTypeDef" = None,
        clientRequestToken: str = None,
        tags: Dict[str, str] = None,
        encryptionConfig: List["EncryptionConfigTypeDef"] = None,
    ) -> CreateClusterResponseTypeDef:
        """
        [Client.create_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client.create_cluster)
        """

    def create_fargate_profile(
        self,
        fargateProfileName: str,
        clusterName: str,
        podExecutionRoleArn: str,
        subnets: List[str] = None,
        selectors: List["FargateProfileSelectorTypeDef"] = None,
        clientRequestToken: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateFargateProfileResponseTypeDef:
        """
        [Client.create_fargate_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client.create_fargate_profile)
        """

    def create_nodegroup(
        self,
        clusterName: str,
        nodegroupName: str,
        subnets: List[str],
        nodeRole: str,
        scalingConfig: "NodegroupScalingConfigTypeDef" = None,
        diskSize: int = None,
        instanceTypes: List[str] = None,
        amiType: Literal["AL2_x86_64", "AL2_x86_64_GPU", "AL2_ARM_64"] = None,
        remoteAccess: "RemoteAccessConfigTypeDef" = None,
        labels: Dict[str, str] = None,
        tags: Dict[str, str] = None,
        clientRequestToken: str = None,
        launchTemplate: "LaunchTemplateSpecificationTypeDef" = None,
        version: str = None,
        releaseVersion: str = None,
    ) -> CreateNodegroupResponseTypeDef:
        """
        [Client.create_nodegroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client.create_nodegroup)
        """

    def delete_cluster(self, name: str) -> DeleteClusterResponseTypeDef:
        """
        [Client.delete_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client.delete_cluster)
        """

    def delete_fargate_profile(
        self, clusterName: str, fargateProfileName: str
    ) -> DeleteFargateProfileResponseTypeDef:
        """
        [Client.delete_fargate_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client.delete_fargate_profile)
        """

    def delete_nodegroup(
        self, clusterName: str, nodegroupName: str
    ) -> DeleteNodegroupResponseTypeDef:
        """
        [Client.delete_nodegroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client.delete_nodegroup)
        """

    def describe_cluster(self, name: str) -> DescribeClusterResponseTypeDef:
        """
        [Client.describe_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client.describe_cluster)
        """

    def describe_fargate_profile(
        self, clusterName: str, fargateProfileName: str
    ) -> DescribeFargateProfileResponseTypeDef:
        """
        [Client.describe_fargate_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client.describe_fargate_profile)
        """

    def describe_nodegroup(
        self, clusterName: str, nodegroupName: str
    ) -> DescribeNodegroupResponseTypeDef:
        """
        [Client.describe_nodegroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client.describe_nodegroup)
        """

    def describe_update(
        self, name: str, updateId: str, nodegroupName: str = None
    ) -> DescribeUpdateResponseTypeDef:
        """
        [Client.describe_update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client.describe_update)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client.generate_presigned_url)
        """

    def list_clusters(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListClustersResponseTypeDef:
        """
        [Client.list_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client.list_clusters)
        """

    def list_fargate_profiles(
        self, clusterName: str, maxResults: int = None, nextToken: str = None
    ) -> ListFargateProfilesResponseTypeDef:
        """
        [Client.list_fargate_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client.list_fargate_profiles)
        """

    def list_nodegroups(
        self, clusterName: str, maxResults: int = None, nextToken: str = None
    ) -> ListNodegroupsResponseTypeDef:
        """
        [Client.list_nodegroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client.list_nodegroups)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client.list_tags_for_resource)
        """

    def list_updates(
        self, name: str, nodegroupName: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListUpdatesResponseTypeDef:
        """
        [Client.list_updates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client.list_updates)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client.untag_resource)
        """

    def update_cluster_config(
        self,
        name: str,
        resourcesVpcConfig: VpcConfigRequestTypeDef = None,
        logging: "LoggingTypeDef" = None,
        clientRequestToken: str = None,
    ) -> UpdateClusterConfigResponseTypeDef:
        """
        [Client.update_cluster_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client.update_cluster_config)
        """

    def update_cluster_version(
        self, name: str, version: str, clientRequestToken: str = None
    ) -> UpdateClusterVersionResponseTypeDef:
        """
        [Client.update_cluster_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client.update_cluster_version)
        """

    def update_nodegroup_config(
        self,
        clusterName: str,
        nodegroupName: str,
        labels: UpdateLabelsPayloadTypeDef = None,
        scalingConfig: "NodegroupScalingConfigTypeDef" = None,
        clientRequestToken: str = None,
    ) -> UpdateNodegroupConfigResponseTypeDef:
        """
        [Client.update_nodegroup_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client.update_nodegroup_config)
        """

    def update_nodegroup_version(
        self,
        clusterName: str,
        nodegroupName: str,
        version: str = None,
        releaseVersion: str = None,
        launchTemplate: "LaunchTemplateSpecificationTypeDef" = None,
        force: bool = None,
        clientRequestToken: str = None,
    ) -> UpdateNodegroupVersionResponseTypeDef:
        """
        [Client.update_nodegroup_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Client.update_nodegroup_version)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_clusters"]) -> ListClustersPaginator:
        """
        [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Paginator.ListClusters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_fargate_profiles"]
    ) -> ListFargateProfilesPaginator:
        """
        [Paginator.ListFargateProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Paginator.ListFargateProfiles)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_nodegroups"]) -> ListNodegroupsPaginator:
        """
        [Paginator.ListNodegroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Paginator.ListNodegroups)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_updates"]) -> ListUpdatesPaginator:
        """
        [Paginator.ListUpdates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Paginator.ListUpdates)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["cluster_active"]) -> ClusterActiveWaiter:
        """
        [Waiter.ClusterActive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Waiter.ClusterActive)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["cluster_deleted"]) -> ClusterDeletedWaiter:
        """
        [Waiter.ClusterDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Waiter.ClusterDeleted)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["nodegroup_active"]) -> NodegroupActiveWaiter:
        """
        [Waiter.NodegroupActive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Waiter.NodegroupActive)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["nodegroup_deleted"]) -> NodegroupDeletedWaiter:
        """
        [Waiter.NodegroupDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/eks.html#EKS.Waiter.NodegroupDeleted)
        """
