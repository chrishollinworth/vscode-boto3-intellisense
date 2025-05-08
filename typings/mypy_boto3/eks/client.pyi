"""
Type annotations for eks service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_eks.client import EKSClient

    session = Session()
    client: EKSClient = session.client("eks")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeAddonVersionsPaginator,
    DescribeClusterVersionsPaginator,
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
    AssociateAccessPolicyRequestTypeDef,
    AssociateAccessPolicyResponseTypeDef,
    AssociateEncryptionConfigRequestTypeDef,
    AssociateEncryptionConfigResponseTypeDef,
    AssociateIdentityProviderConfigRequestTypeDef,
    AssociateIdentityProviderConfigResponseTypeDef,
    CreateAccessEntryRequestTypeDef,
    CreateAccessEntryResponseTypeDef,
    CreateAddonRequestTypeDef,
    CreateAddonResponseTypeDef,
    CreateClusterRequestTypeDef,
    CreateClusterResponseTypeDef,
    CreateEksAnywhereSubscriptionRequestTypeDef,
    CreateEksAnywhereSubscriptionResponseTypeDef,
    CreateFargateProfileRequestTypeDef,
    CreateFargateProfileResponseTypeDef,
    CreateNodegroupRequestTypeDef,
    CreateNodegroupResponseTypeDef,
    CreatePodIdentityAssociationRequestTypeDef,
    CreatePodIdentityAssociationResponseTypeDef,
    DeleteAccessEntryRequestTypeDef,
    DeleteAddonRequestTypeDef,
    DeleteAddonResponseTypeDef,
    DeleteClusterRequestTypeDef,
    DeleteClusterResponseTypeDef,
    DeleteEksAnywhereSubscriptionRequestTypeDef,
    DeleteEksAnywhereSubscriptionResponseTypeDef,
    DeleteFargateProfileRequestTypeDef,
    DeleteFargateProfileResponseTypeDef,
    DeleteNodegroupRequestTypeDef,
    DeleteNodegroupResponseTypeDef,
    DeletePodIdentityAssociationRequestTypeDef,
    DeletePodIdentityAssociationResponseTypeDef,
    DeregisterClusterRequestTypeDef,
    DeregisterClusterResponseTypeDef,
    DescribeAccessEntryRequestTypeDef,
    DescribeAccessEntryResponseTypeDef,
    DescribeAddonConfigurationRequestTypeDef,
    DescribeAddonConfigurationResponseTypeDef,
    DescribeAddonRequestTypeDef,
    DescribeAddonResponseTypeDef,
    DescribeAddonVersionsRequestTypeDef,
    DescribeAddonVersionsResponseTypeDef,
    DescribeClusterRequestTypeDef,
    DescribeClusterResponseTypeDef,
    DescribeClusterVersionsRequestTypeDef,
    DescribeClusterVersionsResponseTypeDef,
    DescribeEksAnywhereSubscriptionRequestTypeDef,
    DescribeEksAnywhereSubscriptionResponseTypeDef,
    DescribeFargateProfileRequestTypeDef,
    DescribeFargateProfileResponseTypeDef,
    DescribeIdentityProviderConfigRequestTypeDef,
    DescribeIdentityProviderConfigResponseTypeDef,
    DescribeInsightRequestTypeDef,
    DescribeInsightResponseTypeDef,
    DescribeNodegroupRequestTypeDef,
    DescribeNodegroupResponseTypeDef,
    DescribePodIdentityAssociationRequestTypeDef,
    DescribePodIdentityAssociationResponseTypeDef,
    DescribeUpdateRequestTypeDef,
    DescribeUpdateResponseTypeDef,
    DisassociateAccessPolicyRequestTypeDef,
    DisassociateIdentityProviderConfigRequestTypeDef,
    DisassociateIdentityProviderConfigResponseTypeDef,
    ListAccessEntriesRequestTypeDef,
    ListAccessEntriesResponseTypeDef,
    ListAccessPoliciesRequestTypeDef,
    ListAccessPoliciesResponseTypeDef,
    ListAddonsRequestTypeDef,
    ListAddonsResponseTypeDef,
    ListAssociatedAccessPoliciesRequestTypeDef,
    ListAssociatedAccessPoliciesResponseTypeDef,
    ListClustersRequestTypeDef,
    ListClustersResponseTypeDef,
    ListEksAnywhereSubscriptionsRequestTypeDef,
    ListEksAnywhereSubscriptionsResponseTypeDef,
    ListFargateProfilesRequestTypeDef,
    ListFargateProfilesResponseTypeDef,
    ListIdentityProviderConfigsRequestTypeDef,
    ListIdentityProviderConfigsResponseTypeDef,
    ListInsightsRequestTypeDef,
    ListInsightsResponseTypeDef,
    ListNodegroupsRequestTypeDef,
    ListNodegroupsResponseTypeDef,
    ListPodIdentityAssociationsRequestTypeDef,
    ListPodIdentityAssociationsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUpdatesRequestTypeDef,
    ListUpdatesResponseTypeDef,
    RegisterClusterRequestTypeDef,
    RegisterClusterResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAccessEntryRequestTypeDef,
    UpdateAccessEntryResponseTypeDef,
    UpdateAddonRequestTypeDef,
    UpdateAddonResponseTypeDef,
    UpdateClusterConfigRequestTypeDef,
    UpdateClusterConfigResponseTypeDef,
    UpdateClusterVersionRequestTypeDef,
    UpdateClusterVersionResponseTypeDef,
    UpdateEksAnywhereSubscriptionRequestTypeDef,
    UpdateEksAnywhereSubscriptionResponseTypeDef,
    UpdateNodegroupConfigRequestTypeDef,
    UpdateNodegroupConfigResponseTypeDef,
    UpdateNodegroupVersionRequestTypeDef,
    UpdateNodegroupVersionResponseTypeDef,
    UpdatePodIdentityAssociationRequestTypeDef,
    UpdatePodIdentityAssociationResponseTypeDef,
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

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("EKSClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClientException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidStateException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourcePropagationDelayException: Type[BotocoreClientError]
    ServerException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnsupportedAvailabilityZoneException: Type[BotocoreClientError]

class EKSClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        EKSClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html#EKS.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#generate_presigned_url)
        """

    def associate_access_policy(
        self, **kwargs: Unpack[AssociateAccessPolicyRequestTypeDef]
    ) -> AssociateAccessPolicyResponseTypeDef:
        """
        Associates an access policy and its scope to an access entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/associate_access_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#associate_access_policy)
        """

    def associate_encryption_config(
        self, **kwargs: Unpack[AssociateEncryptionConfigRequestTypeDef]
    ) -> AssociateEncryptionConfigResponseTypeDef:
        """
        Associates an encryption configuration to an existing cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/associate_encryption_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#associate_encryption_config)
        """

    def associate_identity_provider_config(
        self, **kwargs: Unpack[AssociateIdentityProviderConfigRequestTypeDef]
    ) -> AssociateIdentityProviderConfigResponseTypeDef:
        """
        Associates an identity provider configuration to a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/associate_identity_provider_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#associate_identity_provider_config)
        """

    def create_access_entry(
        self, **kwargs: Unpack[CreateAccessEntryRequestTypeDef]
    ) -> CreateAccessEntryResponseTypeDef:
        """
        Creates an access entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/create_access_entry.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#create_access_entry)
        """

    def create_addon(
        self, **kwargs: Unpack[CreateAddonRequestTypeDef]
    ) -> CreateAddonResponseTypeDef:
        """
        Creates an Amazon EKS add-on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/create_addon.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#create_addon)
        """

    def create_cluster(
        self, **kwargs: Unpack[CreateClusterRequestTypeDef]
    ) -> CreateClusterResponseTypeDef:
        """
        Creates an Amazon EKS control plane.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/create_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#create_cluster)
        """

    def create_eks_anywhere_subscription(
        self, **kwargs: Unpack[CreateEksAnywhereSubscriptionRequestTypeDef]
    ) -> CreateEksAnywhereSubscriptionResponseTypeDef:
        """
        Creates an EKS Anywhere subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/create_eks_anywhere_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#create_eks_anywhere_subscription)
        """

    def create_fargate_profile(
        self, **kwargs: Unpack[CreateFargateProfileRequestTypeDef]
    ) -> CreateFargateProfileResponseTypeDef:
        """
        Creates an Fargate profile for your Amazon EKS cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/create_fargate_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#create_fargate_profile)
        """

    def create_nodegroup(
        self, **kwargs: Unpack[CreateNodegroupRequestTypeDef]
    ) -> CreateNodegroupResponseTypeDef:
        """
        Creates a managed node group for an Amazon EKS cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/create_nodegroup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#create_nodegroup)
        """

    def create_pod_identity_association(
        self, **kwargs: Unpack[CreatePodIdentityAssociationRequestTypeDef]
    ) -> CreatePodIdentityAssociationResponseTypeDef:
        """
        Creates an EKS Pod Identity association between a service account in an Amazon
        EKS cluster and an IAM role with <i>EKS Pod Identity</i>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/create_pod_identity_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#create_pod_identity_association)
        """

    def delete_access_entry(
        self, **kwargs: Unpack[DeleteAccessEntryRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an access entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/delete_access_entry.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#delete_access_entry)
        """

    def delete_addon(
        self, **kwargs: Unpack[DeleteAddonRequestTypeDef]
    ) -> DeleteAddonResponseTypeDef:
        """
        Deletes an Amazon EKS add-on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/delete_addon.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#delete_addon)
        """

    def delete_cluster(
        self, **kwargs: Unpack[DeleteClusterRequestTypeDef]
    ) -> DeleteClusterResponseTypeDef:
        """
        Deletes an Amazon EKS cluster control plane.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/delete_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#delete_cluster)
        """

    def delete_eks_anywhere_subscription(
        self, **kwargs: Unpack[DeleteEksAnywhereSubscriptionRequestTypeDef]
    ) -> DeleteEksAnywhereSubscriptionResponseTypeDef:
        """
        Deletes an expired or inactive subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/delete_eks_anywhere_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#delete_eks_anywhere_subscription)
        """

    def delete_fargate_profile(
        self, **kwargs: Unpack[DeleteFargateProfileRequestTypeDef]
    ) -> DeleteFargateProfileResponseTypeDef:
        """
        Deletes an Fargate profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/delete_fargate_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#delete_fargate_profile)
        """

    def delete_nodegroup(
        self, **kwargs: Unpack[DeleteNodegroupRequestTypeDef]
    ) -> DeleteNodegroupResponseTypeDef:
        """
        Deletes a managed node group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/delete_nodegroup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#delete_nodegroup)
        """

    def delete_pod_identity_association(
        self, **kwargs: Unpack[DeletePodIdentityAssociationRequestTypeDef]
    ) -> DeletePodIdentityAssociationResponseTypeDef:
        """
        Deletes a EKS Pod Identity association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/delete_pod_identity_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#delete_pod_identity_association)
        """

    def deregister_cluster(
        self, **kwargs: Unpack[DeregisterClusterRequestTypeDef]
    ) -> DeregisterClusterResponseTypeDef:
        """
        Deregisters a connected cluster to remove it from the Amazon EKS control plane.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/deregister_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#deregister_cluster)
        """

    def describe_access_entry(
        self, **kwargs: Unpack[DescribeAccessEntryRequestTypeDef]
    ) -> DescribeAccessEntryResponseTypeDef:
        """
        Describes an access entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/describe_access_entry.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#describe_access_entry)
        """

    def describe_addon(
        self, **kwargs: Unpack[DescribeAddonRequestTypeDef]
    ) -> DescribeAddonResponseTypeDef:
        """
        Describes an Amazon EKS add-on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/describe_addon.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#describe_addon)
        """

    def describe_addon_configuration(
        self, **kwargs: Unpack[DescribeAddonConfigurationRequestTypeDef]
    ) -> DescribeAddonConfigurationResponseTypeDef:
        """
        Returns configuration options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/describe_addon_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#describe_addon_configuration)
        """

    def describe_addon_versions(
        self, **kwargs: Unpack[DescribeAddonVersionsRequestTypeDef]
    ) -> DescribeAddonVersionsResponseTypeDef:
        """
        Describes the versions for an add-on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/describe_addon_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#describe_addon_versions)
        """

    def describe_cluster(
        self, **kwargs: Unpack[DescribeClusterRequestTypeDef]
    ) -> DescribeClusterResponseTypeDef:
        """
        Describes an Amazon EKS cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/describe_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#describe_cluster)
        """

    def describe_cluster_versions(
        self, **kwargs: Unpack[DescribeClusterVersionsRequestTypeDef]
    ) -> DescribeClusterVersionsResponseTypeDef:
        """
        Lists available Kubernetes versions for Amazon EKS clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/describe_cluster_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#describe_cluster_versions)
        """

    def describe_eks_anywhere_subscription(
        self, **kwargs: Unpack[DescribeEksAnywhereSubscriptionRequestTypeDef]
    ) -> DescribeEksAnywhereSubscriptionResponseTypeDef:
        """
        Returns descriptive information about a subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/describe_eks_anywhere_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#describe_eks_anywhere_subscription)
        """

    def describe_fargate_profile(
        self, **kwargs: Unpack[DescribeFargateProfileRequestTypeDef]
    ) -> DescribeFargateProfileResponseTypeDef:
        """
        Describes an Fargate profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/describe_fargate_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#describe_fargate_profile)
        """

    def describe_identity_provider_config(
        self, **kwargs: Unpack[DescribeIdentityProviderConfigRequestTypeDef]
    ) -> DescribeIdentityProviderConfigResponseTypeDef:
        """
        Describes an identity provider configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/describe_identity_provider_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#describe_identity_provider_config)
        """

    def describe_insight(
        self, **kwargs: Unpack[DescribeInsightRequestTypeDef]
    ) -> DescribeInsightResponseTypeDef:
        """
        Returns details about an insight that you specify using its ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/describe_insight.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#describe_insight)
        """

    def describe_nodegroup(
        self, **kwargs: Unpack[DescribeNodegroupRequestTypeDef]
    ) -> DescribeNodegroupResponseTypeDef:
        """
        Describes a managed node group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/describe_nodegroup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#describe_nodegroup)
        """

    def describe_pod_identity_association(
        self, **kwargs: Unpack[DescribePodIdentityAssociationRequestTypeDef]
    ) -> DescribePodIdentityAssociationResponseTypeDef:
        """
        Returns descriptive information about an EKS Pod Identity association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/describe_pod_identity_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#describe_pod_identity_association)
        """

    def describe_update(
        self, **kwargs: Unpack[DescribeUpdateRequestTypeDef]
    ) -> DescribeUpdateResponseTypeDef:
        """
        Describes an update to an Amazon EKS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/describe_update.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#describe_update)
        """

    def disassociate_access_policy(
        self, **kwargs: Unpack[DisassociateAccessPolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates an access policy from an access entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/disassociate_access_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#disassociate_access_policy)
        """

    def disassociate_identity_provider_config(
        self, **kwargs: Unpack[DisassociateIdentityProviderConfigRequestTypeDef]
    ) -> DisassociateIdentityProviderConfigResponseTypeDef:
        """
        Disassociates an identity provider configuration from a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/disassociate_identity_provider_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#disassociate_identity_provider_config)
        """

    def list_access_entries(
        self, **kwargs: Unpack[ListAccessEntriesRequestTypeDef]
    ) -> ListAccessEntriesResponseTypeDef:
        """
        Lists the access entries for your cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/list_access_entries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#list_access_entries)
        """

    def list_access_policies(
        self, **kwargs: Unpack[ListAccessPoliciesRequestTypeDef]
    ) -> ListAccessPoliciesResponseTypeDef:
        """
        Lists the available access policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/list_access_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#list_access_policies)
        """

    def list_addons(self, **kwargs: Unpack[ListAddonsRequestTypeDef]) -> ListAddonsResponseTypeDef:
        """
        Lists the installed add-ons.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/list_addons.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#list_addons)
        """

    def list_associated_access_policies(
        self, **kwargs: Unpack[ListAssociatedAccessPoliciesRequestTypeDef]
    ) -> ListAssociatedAccessPoliciesResponseTypeDef:
        """
        Lists the access policies associated with an access entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/list_associated_access_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#list_associated_access_policies)
        """

    def list_clusters(
        self, **kwargs: Unpack[ListClustersRequestTypeDef]
    ) -> ListClustersResponseTypeDef:
        """
        Lists the Amazon EKS clusters in your Amazon Web Services account in the
        specified Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/list_clusters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#list_clusters)
        """

    def list_eks_anywhere_subscriptions(
        self, **kwargs: Unpack[ListEksAnywhereSubscriptionsRequestTypeDef]
    ) -> ListEksAnywhereSubscriptionsResponseTypeDef:
        """
        Displays the full description of the subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/list_eks_anywhere_subscriptions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#list_eks_anywhere_subscriptions)
        """

    def list_fargate_profiles(
        self, **kwargs: Unpack[ListFargateProfilesRequestTypeDef]
    ) -> ListFargateProfilesResponseTypeDef:
        """
        Lists the Fargate profiles associated with the specified cluster in your Amazon
        Web Services account in the specified Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/list_fargate_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#list_fargate_profiles)
        """

    def list_identity_provider_configs(
        self, **kwargs: Unpack[ListIdentityProviderConfigsRequestTypeDef]
    ) -> ListIdentityProviderConfigsResponseTypeDef:
        """
        Lists the identity provider configurations for your cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/list_identity_provider_configs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#list_identity_provider_configs)
        """

    def list_insights(
        self, **kwargs: Unpack[ListInsightsRequestTypeDef]
    ) -> ListInsightsResponseTypeDef:
        """
        Returns a list of all insights checked for against the specified cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/list_insights.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#list_insights)
        """

    def list_nodegroups(
        self, **kwargs: Unpack[ListNodegroupsRequestTypeDef]
    ) -> ListNodegroupsResponseTypeDef:
        """
        Lists the managed node groups associated with the specified cluster in your
        Amazon Web Services account in the specified Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/list_nodegroups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#list_nodegroups)
        """

    def list_pod_identity_associations(
        self, **kwargs: Unpack[ListPodIdentityAssociationsRequestTypeDef]
    ) -> ListPodIdentityAssociationsResponseTypeDef:
        """
        List the EKS Pod Identity associations in a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/list_pod_identity_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#list_pod_identity_associations)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        List the tags for an Amazon EKS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#list_tags_for_resource)
        """

    def list_updates(
        self, **kwargs: Unpack[ListUpdatesRequestTypeDef]
    ) -> ListUpdatesResponseTypeDef:
        """
        Lists the updates associated with an Amazon EKS resource in your Amazon Web
        Services account, in the specified Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/list_updates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#list_updates)
        """

    def register_cluster(
        self, **kwargs: Unpack[RegisterClusterRequestTypeDef]
    ) -> RegisterClusterResponseTypeDef:
        """
        Connects a Kubernetes cluster to the Amazon EKS control plane.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/register_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#register_cluster)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Associates the specified tags to an Amazon EKS resource with the specified
        <code>resourceArn</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes specified tags from an Amazon EKS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#untag_resource)
        """

    def update_access_entry(
        self, **kwargs: Unpack[UpdateAccessEntryRequestTypeDef]
    ) -> UpdateAccessEntryResponseTypeDef:
        """
        Updates an access entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/update_access_entry.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#update_access_entry)
        """

    def update_addon(
        self, **kwargs: Unpack[UpdateAddonRequestTypeDef]
    ) -> UpdateAddonResponseTypeDef:
        """
        Updates an Amazon EKS add-on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/update_addon.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#update_addon)
        """

    def update_cluster_config(
        self, **kwargs: Unpack[UpdateClusterConfigRequestTypeDef]
    ) -> UpdateClusterConfigResponseTypeDef:
        """
        Updates an Amazon EKS cluster configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/update_cluster_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#update_cluster_config)
        """

    def update_cluster_version(
        self, **kwargs: Unpack[UpdateClusterVersionRequestTypeDef]
    ) -> UpdateClusterVersionResponseTypeDef:
        """
        Updates an Amazon EKS cluster to the specified Kubernetes version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/update_cluster_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#update_cluster_version)
        """

    def update_eks_anywhere_subscription(
        self, **kwargs: Unpack[UpdateEksAnywhereSubscriptionRequestTypeDef]
    ) -> UpdateEksAnywhereSubscriptionResponseTypeDef:
        """
        Update an EKS Anywhere Subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/update_eks_anywhere_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#update_eks_anywhere_subscription)
        """

    def update_nodegroup_config(
        self, **kwargs: Unpack[UpdateNodegroupConfigRequestTypeDef]
    ) -> UpdateNodegroupConfigResponseTypeDef:
        """
        Updates an Amazon EKS managed node group configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/update_nodegroup_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#update_nodegroup_config)
        """

    def update_nodegroup_version(
        self, **kwargs: Unpack[UpdateNodegroupVersionRequestTypeDef]
    ) -> UpdateNodegroupVersionResponseTypeDef:
        """
        Updates the Kubernetes version or AMI version of an Amazon EKS managed node
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/update_nodegroup_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#update_nodegroup_version)
        """

    def update_pod_identity_association(
        self, **kwargs: Unpack[UpdatePodIdentityAssociationRequestTypeDef]
    ) -> UpdatePodIdentityAssociationResponseTypeDef:
        """
        Updates a EKS Pod Identity association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/update_pod_identity_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#update_pod_identity_association)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_addon_versions"]
    ) -> DescribeAddonVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_cluster_versions"]
    ) -> DescribeClusterVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_access_entries"]
    ) -> ListAccessEntriesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_access_policies"]
    ) -> ListAccessPoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_addons"]
    ) -> ListAddonsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_associated_access_policies"]
    ) -> ListAssociatedAccessPoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_clusters"]
    ) -> ListClustersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_eks_anywhere_subscriptions"]
    ) -> ListEksAnywhereSubscriptionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_fargate_profiles"]
    ) -> ListFargateProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_identity_provider_configs"]
    ) -> ListIdentityProviderConfigsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_insights"]
    ) -> ListInsightsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_nodegroups"]
    ) -> ListNodegroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_pod_identity_associations"]
    ) -> ListPodIdentityAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_updates"]
    ) -> ListUpdatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["addon_active"]
    ) -> AddonActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["addon_deleted"]
    ) -> AddonDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["cluster_active"]
    ) -> ClusterActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["cluster_deleted"]
    ) -> ClusterDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["fargate_profile_active"]
    ) -> FargateProfileActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["fargate_profile_deleted"]
    ) -> FargateProfileDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["nodegroup_active"]
    ) -> NodegroupActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["nodegroup_deleted"]
    ) -> NodegroupDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks/client/#get_waiter)
        """
