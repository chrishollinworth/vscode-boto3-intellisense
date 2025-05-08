"""
Type annotations for opensearchserverless service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_opensearchserverless.client import OpenSearchServiceServerlessClient

    session = Session()
    client: OpenSearchServiceServerlessClient = session.client("opensearchserverless")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    BatchGetCollectionRequestTypeDef,
    BatchGetCollectionResponseTypeDef,
    BatchGetEffectiveLifecyclePolicyRequestTypeDef,
    BatchGetEffectiveLifecyclePolicyResponseTypeDef,
    BatchGetLifecyclePolicyRequestTypeDef,
    BatchGetLifecyclePolicyResponseTypeDef,
    BatchGetVpcEndpointRequestTypeDef,
    BatchGetVpcEndpointResponseTypeDef,
    CreateAccessPolicyRequestTypeDef,
    CreateAccessPolicyResponseTypeDef,
    CreateCollectionRequestTypeDef,
    CreateCollectionResponseTypeDef,
    CreateLifecyclePolicyRequestTypeDef,
    CreateLifecyclePolicyResponseTypeDef,
    CreateSecurityConfigRequestTypeDef,
    CreateSecurityConfigResponseTypeDef,
    CreateSecurityPolicyRequestTypeDef,
    CreateSecurityPolicyResponseTypeDef,
    CreateVpcEndpointRequestTypeDef,
    CreateVpcEndpointResponseTypeDef,
    DeleteAccessPolicyRequestTypeDef,
    DeleteCollectionRequestTypeDef,
    DeleteCollectionResponseTypeDef,
    DeleteLifecyclePolicyRequestTypeDef,
    DeleteSecurityConfigRequestTypeDef,
    DeleteSecurityPolicyRequestTypeDef,
    DeleteVpcEndpointRequestTypeDef,
    DeleteVpcEndpointResponseTypeDef,
    GetAccessPolicyRequestTypeDef,
    GetAccessPolicyResponseTypeDef,
    GetAccountSettingsResponseTypeDef,
    GetPoliciesStatsResponseTypeDef,
    GetSecurityConfigRequestTypeDef,
    GetSecurityConfigResponseTypeDef,
    GetSecurityPolicyRequestTypeDef,
    GetSecurityPolicyResponseTypeDef,
    ListAccessPoliciesRequestTypeDef,
    ListAccessPoliciesResponseTypeDef,
    ListCollectionsRequestTypeDef,
    ListCollectionsResponseTypeDef,
    ListLifecyclePoliciesRequestTypeDef,
    ListLifecyclePoliciesResponseTypeDef,
    ListSecurityConfigsRequestTypeDef,
    ListSecurityConfigsResponseTypeDef,
    ListSecurityPoliciesRequestTypeDef,
    ListSecurityPoliciesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListVpcEndpointsRequestTypeDef,
    ListVpcEndpointsResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAccessPolicyRequestTypeDef,
    UpdateAccessPolicyResponseTypeDef,
    UpdateAccountSettingsRequestTypeDef,
    UpdateAccountSettingsResponseTypeDef,
    UpdateCollectionRequestTypeDef,
    UpdateCollectionResponseTypeDef,
    UpdateLifecyclePolicyRequestTypeDef,
    UpdateLifecyclePolicyResponseTypeDef,
    UpdateSecurityConfigRequestTypeDef,
    UpdateSecurityConfigResponseTypeDef,
    UpdateSecurityPolicyRequestTypeDef,
    UpdateSecurityPolicyResponseTypeDef,
    UpdateVpcEndpointRequestTypeDef,
    UpdateVpcEndpointResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("OpenSearchServiceServerlessClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    OcuLimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class OpenSearchServiceServerlessClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        OpenSearchServiceServerlessClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#generate_presigned_url)
        """

    def batch_get_collection(
        self, **kwargs: Unpack[BatchGetCollectionRequestTypeDef]
    ) -> BatchGetCollectionResponseTypeDef:
        """
        Returns attributes for one or more collections, including the collection
        endpoint and the OpenSearch Dashboards endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/batch_get_collection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#batch_get_collection)
        """

    def batch_get_effective_lifecycle_policy(
        self, **kwargs: Unpack[BatchGetEffectiveLifecyclePolicyRequestTypeDef]
    ) -> BatchGetEffectiveLifecyclePolicyResponseTypeDef:
        """
        Returns a list of successful and failed retrievals for the OpenSearch
        Serverless indexes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/batch_get_effective_lifecycle_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#batch_get_effective_lifecycle_policy)
        """

    def batch_get_lifecycle_policy(
        self, **kwargs: Unpack[BatchGetLifecyclePolicyRequestTypeDef]
    ) -> BatchGetLifecyclePolicyResponseTypeDef:
        """
        Returns one or more configured OpenSearch Serverless lifecycle policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/batch_get_lifecycle_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#batch_get_lifecycle_policy)
        """

    def batch_get_vpc_endpoint(
        self, **kwargs: Unpack[BatchGetVpcEndpointRequestTypeDef]
    ) -> BatchGetVpcEndpointResponseTypeDef:
        """
        Returns attributes for one or more VPC endpoints associated with the current
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/batch_get_vpc_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#batch_get_vpc_endpoint)
        """

    def create_access_policy(
        self, **kwargs: Unpack[CreateAccessPolicyRequestTypeDef]
    ) -> CreateAccessPolicyResponseTypeDef:
        """
        Creates a data access policy for OpenSearch Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/create_access_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#create_access_policy)
        """

    def create_collection(
        self, **kwargs: Unpack[CreateCollectionRequestTypeDef]
    ) -> CreateCollectionResponseTypeDef:
        """
        Creates a new OpenSearch Serverless collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/create_collection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#create_collection)
        """

    def create_lifecycle_policy(
        self, **kwargs: Unpack[CreateLifecyclePolicyRequestTypeDef]
    ) -> CreateLifecyclePolicyResponseTypeDef:
        """
        Creates a lifecyle policy to be applied to OpenSearch Serverless indexes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/create_lifecycle_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#create_lifecycle_policy)
        """

    def create_security_config(
        self, **kwargs: Unpack[CreateSecurityConfigRequestTypeDef]
    ) -> CreateSecurityConfigResponseTypeDef:
        """
        Specifies a security configuration for OpenSearch Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/create_security_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#create_security_config)
        """

    def create_security_policy(
        self, **kwargs: Unpack[CreateSecurityPolicyRequestTypeDef]
    ) -> CreateSecurityPolicyResponseTypeDef:
        """
        Creates a security policy to be used by one or more OpenSearch Serverless
        collections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/create_security_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#create_security_policy)
        """

    def create_vpc_endpoint(
        self, **kwargs: Unpack[CreateVpcEndpointRequestTypeDef]
    ) -> CreateVpcEndpointResponseTypeDef:
        """
        Creates an OpenSearch Serverless-managed interface VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/create_vpc_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#create_vpc_endpoint)
        """

    def delete_access_policy(
        self, **kwargs: Unpack[DeleteAccessPolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an OpenSearch Serverless access policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/delete_access_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#delete_access_policy)
        """

    def delete_collection(
        self, **kwargs: Unpack[DeleteCollectionRequestTypeDef]
    ) -> DeleteCollectionResponseTypeDef:
        """
        Deletes an OpenSearch Serverless collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/delete_collection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#delete_collection)
        """

    def delete_lifecycle_policy(
        self, **kwargs: Unpack[DeleteLifecyclePolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an OpenSearch Serverless lifecycle policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/delete_lifecycle_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#delete_lifecycle_policy)
        """

    def delete_security_config(
        self, **kwargs: Unpack[DeleteSecurityConfigRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a security configuration for OpenSearch Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/delete_security_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#delete_security_config)
        """

    def delete_security_policy(
        self, **kwargs: Unpack[DeleteSecurityPolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an OpenSearch Serverless security policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/delete_security_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#delete_security_policy)
        """

    def delete_vpc_endpoint(
        self, **kwargs: Unpack[DeleteVpcEndpointRequestTypeDef]
    ) -> DeleteVpcEndpointResponseTypeDef:
        """
        Deletes an OpenSearch Serverless-managed interface endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/delete_vpc_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#delete_vpc_endpoint)
        """

    def get_access_policy(
        self, **kwargs: Unpack[GetAccessPolicyRequestTypeDef]
    ) -> GetAccessPolicyResponseTypeDef:
        """
        Returns an OpenSearch Serverless access policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/get_access_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#get_access_policy)
        """

    def get_account_settings(self) -> GetAccountSettingsResponseTypeDef:
        """
        Returns account-level settings related to OpenSearch Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/get_account_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#get_account_settings)
        """

    def get_policies_stats(self) -> GetPoliciesStatsResponseTypeDef:
        """
        Returns statistical information about your OpenSearch Serverless access
        policies, security configurations, and security policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/get_policies_stats.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#get_policies_stats)
        """

    def get_security_config(
        self, **kwargs: Unpack[GetSecurityConfigRequestTypeDef]
    ) -> GetSecurityConfigResponseTypeDef:
        """
        Returns information about an OpenSearch Serverless security configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/get_security_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#get_security_config)
        """

    def get_security_policy(
        self, **kwargs: Unpack[GetSecurityPolicyRequestTypeDef]
    ) -> GetSecurityPolicyResponseTypeDef:
        """
        Returns information about a configured OpenSearch Serverless security policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/get_security_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#get_security_policy)
        """

    def list_access_policies(
        self, **kwargs: Unpack[ListAccessPoliciesRequestTypeDef]
    ) -> ListAccessPoliciesResponseTypeDef:
        """
        Returns information about a list of OpenSearch Serverless access policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/list_access_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#list_access_policies)
        """

    def list_collections(
        self, **kwargs: Unpack[ListCollectionsRequestTypeDef]
    ) -> ListCollectionsResponseTypeDef:
        """
        Lists all OpenSearch Serverless collections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/list_collections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#list_collections)
        """

    def list_lifecycle_policies(
        self, **kwargs: Unpack[ListLifecyclePoliciesRequestTypeDef]
    ) -> ListLifecyclePoliciesResponseTypeDef:
        """
        Returns a list of OpenSearch Serverless lifecycle policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/list_lifecycle_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#list_lifecycle_policies)
        """

    def list_security_configs(
        self, **kwargs: Unpack[ListSecurityConfigsRequestTypeDef]
    ) -> ListSecurityConfigsResponseTypeDef:
        """
        Returns information about configured OpenSearch Serverless security
        configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/list_security_configs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#list_security_configs)
        """

    def list_security_policies(
        self, **kwargs: Unpack[ListSecurityPoliciesRequestTypeDef]
    ) -> ListSecurityPoliciesResponseTypeDef:
        """
        Returns information about configured OpenSearch Serverless security policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/list_security_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#list_security_policies)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns the tags for an OpenSearch Serverless resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#list_tags_for_resource)
        """

    def list_vpc_endpoints(
        self, **kwargs: Unpack[ListVpcEndpointsRequestTypeDef]
    ) -> ListVpcEndpointsResponseTypeDef:
        """
        Returns the OpenSearch Serverless-managed interface VPC endpoints associated
        with the current account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/list_vpc_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#list_vpc_endpoints)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Associates tags with an OpenSearch Serverless resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a tag or set of tags from an OpenSearch Serverless resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#untag_resource)
        """

    def update_access_policy(
        self, **kwargs: Unpack[UpdateAccessPolicyRequestTypeDef]
    ) -> UpdateAccessPolicyResponseTypeDef:
        """
        Updates an OpenSearch Serverless access policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/update_access_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#update_access_policy)
        """

    def update_account_settings(
        self, **kwargs: Unpack[UpdateAccountSettingsRequestTypeDef]
    ) -> UpdateAccountSettingsResponseTypeDef:
        """
        Update the OpenSearch Serverless settings for the current Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/update_account_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#update_account_settings)
        """

    def update_collection(
        self, **kwargs: Unpack[UpdateCollectionRequestTypeDef]
    ) -> UpdateCollectionResponseTypeDef:
        """
        Updates an OpenSearch Serverless collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/update_collection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#update_collection)
        """

    def update_lifecycle_policy(
        self, **kwargs: Unpack[UpdateLifecyclePolicyRequestTypeDef]
    ) -> UpdateLifecyclePolicyResponseTypeDef:
        """
        Updates an OpenSearch Serverless access policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/update_lifecycle_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#update_lifecycle_policy)
        """

    def update_security_config(
        self, **kwargs: Unpack[UpdateSecurityConfigRequestTypeDef]
    ) -> UpdateSecurityConfigResponseTypeDef:
        """
        Updates a security configuration for OpenSearch Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/update_security_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#update_security_config)
        """

    def update_security_policy(
        self, **kwargs: Unpack[UpdateSecurityPolicyRequestTypeDef]
    ) -> UpdateSecurityPolicyResponseTypeDef:
        """
        Updates an OpenSearch Serverless security policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/update_security_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#update_security_policy)
        """

    def update_vpc_endpoint(
        self, **kwargs: Unpack[UpdateVpcEndpointRequestTypeDef]
    ) -> UpdateVpcEndpointResponseTypeDef:
        """
        Updates an OpenSearch Serverless-managed interface endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless/client/update_vpc_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client/#update_vpc_endpoint)
        """
