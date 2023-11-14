"""
Type annotations for opensearchserverless service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_opensearchserverless import OpenSearchServiceServerlessClient

    client: OpenSearchServiceServerlessClient = boto3.client("opensearchserverless")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import CollectionTypeType, SecurityPolicyTypeType
from .type_defs import (
    BatchGetCollectionResponseTypeDef,
    BatchGetEffectiveLifecyclePolicyResponseTypeDef,
    BatchGetLifecyclePolicyResponseTypeDef,
    BatchGetVpcEndpointResponseTypeDef,
    CapacityLimitsTypeDef,
    CollectionFiltersTypeDef,
    CreateAccessPolicyResponseTypeDef,
    CreateCollectionResponseTypeDef,
    CreateLifecyclePolicyResponseTypeDef,
    CreateSecurityConfigResponseTypeDef,
    CreateSecurityPolicyResponseTypeDef,
    CreateVpcEndpointResponseTypeDef,
    DeleteCollectionResponseTypeDef,
    DeleteVpcEndpointResponseTypeDef,
    GetAccessPolicyResponseTypeDef,
    GetAccountSettingsResponseTypeDef,
    GetPoliciesStatsResponseTypeDef,
    GetSecurityConfigResponseTypeDef,
    GetSecurityPolicyResponseTypeDef,
    LifecyclePolicyIdentifierTypeDef,
    LifecyclePolicyResourceIdentifierTypeDef,
    ListAccessPoliciesResponseTypeDef,
    ListCollectionsResponseTypeDef,
    ListLifecyclePoliciesResponseTypeDef,
    ListSecurityConfigsResponseTypeDef,
    ListSecurityPoliciesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListVpcEndpointsResponseTypeDef,
    SamlConfigOptionsTypeDef,
    TagTypeDef,
    UpdateAccessPolicyResponseTypeDef,
    UpdateAccountSettingsResponseTypeDef,
    UpdateCollectionResponseTypeDef,
    UpdateLifecyclePolicyResponseTypeDef,
    UpdateSecurityConfigResponseTypeDef,
    UpdateSecurityPolicyResponseTypeDef,
    UpdateVpcEndpointResponseTypeDef,
    VpcEndpointFiltersTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("OpenSearchServiceServerlessClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    OcuLimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class OpenSearchServiceServerlessClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        OpenSearchServiceServerlessClient exceptions.
        """
    def batch_get_collection(
        self, *, ids: List[str] = None, names: List[str] = None
    ) -> BatchGetCollectionResponseTypeDef:
        """
        Returns attributes for one or more collections, including the collection
        endpoint and the OpenSearch Dashboards endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.batch_get_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#batch_get_collection)
        """
    def batch_get_effective_lifecycle_policy(
        self, *, resourceIdentifiers: List["LifecyclePolicyResourceIdentifierTypeDef"]
    ) -> BatchGetEffectiveLifecyclePolicyResponseTypeDef:
        """
        Returns a list of successful and failed retrievals for the OpenSearch Serverless
        indexes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.batch_get_effective_lifecycle_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#batch_get_effective_lifecycle_policy)
        """
    def batch_get_lifecycle_policy(
        self, *, identifiers: List["LifecyclePolicyIdentifierTypeDef"]
    ) -> BatchGetLifecyclePolicyResponseTypeDef:
        """
        Returns one or more configured OpenSearch Serverless lifecycle policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.batch_get_lifecycle_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#batch_get_lifecycle_policy)
        """
    def batch_get_vpc_endpoint(self, *, ids: List[str]) -> BatchGetVpcEndpointResponseTypeDef:
        """
        Returns attributes for one or more VPC endpoints associated with the current
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.batch_get_vpc_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#batch_get_vpc_endpoint)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#close)
        """
    def create_access_policy(
        self,
        *,
        name: str,
        policy: str,
        type: Literal["data"],
        clientToken: str = None,
        description: str = None
    ) -> CreateAccessPolicyResponseTypeDef:
        """
        Creates a data access policy for OpenSearch Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.create_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#create_access_policy)
        """
    def create_collection(
        self,
        *,
        name: str,
        clientToken: str = None,
        description: str = None,
        tags: List["TagTypeDef"] = None,
        type: CollectionTypeType = None
    ) -> CreateCollectionResponseTypeDef:
        """
        Creates a new OpenSearch Serverless collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.create_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#create_collection)
        """
    def create_lifecycle_policy(
        self,
        *,
        name: str,
        policy: str,
        type: Literal["retention"],
        clientToken: str = None,
        description: str = None
    ) -> CreateLifecyclePolicyResponseTypeDef:
        """
        Creates a lifecyle policy to be applied to OpenSearch Serverless indexes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.create_lifecycle_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#create_lifecycle_policy)
        """
    def create_security_config(
        self,
        *,
        name: str,
        type: Literal["saml"],
        clientToken: str = None,
        description: str = None,
        samlOptions: "SamlConfigOptionsTypeDef" = None
    ) -> CreateSecurityConfigResponseTypeDef:
        """
        Specifies a security configuration for OpenSearch Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.create_security_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#create_security_config)
        """
    def create_security_policy(
        self,
        *,
        name: str,
        policy: str,
        type: SecurityPolicyTypeType,
        clientToken: str = None,
        description: str = None
    ) -> CreateSecurityPolicyResponseTypeDef:
        """
        Creates a security policy to be used by one or more OpenSearch Serverless
        collections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.create_security_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#create_security_policy)
        """
    def create_vpc_endpoint(
        self,
        *,
        name: str,
        subnetIds: List[str],
        vpcId: str,
        clientToken: str = None,
        securityGroupIds: List[str] = None
    ) -> CreateVpcEndpointResponseTypeDef:
        """
        Creates an OpenSearch Serverless-managed interface VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.create_vpc_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#create_vpc_endpoint)
        """
    def delete_access_policy(
        self, *, name: str, type: Literal["data"], clientToken: str = None
    ) -> Dict[str, Any]:
        """
        Deletes an OpenSearch Serverless access policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.delete_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#delete_access_policy)
        """
    def delete_collection(
        self, *, id: str, clientToken: str = None
    ) -> DeleteCollectionResponseTypeDef:
        """
        Deletes an OpenSearch Serverless collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.delete_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#delete_collection)
        """
    def delete_lifecycle_policy(
        self, *, name: str, type: Literal["retention"], clientToken: str = None
    ) -> Dict[str, Any]:
        """
        Deletes an OpenSearch Serverless lifecycle policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.delete_lifecycle_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#delete_lifecycle_policy)
        """
    def delete_security_config(self, *, id: str, clientToken: str = None) -> Dict[str, Any]:
        """
        Deletes a security configuration for OpenSearch Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.delete_security_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#delete_security_config)
        """
    def delete_security_policy(
        self, *, name: str, type: SecurityPolicyTypeType, clientToken: str = None
    ) -> Dict[str, Any]:
        """
        Deletes an OpenSearch Serverless security policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.delete_security_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#delete_security_policy)
        """
    def delete_vpc_endpoint(
        self, *, id: str, clientToken: str = None
    ) -> DeleteVpcEndpointResponseTypeDef:
        """
        Deletes an OpenSearch Serverless-managed interface endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.delete_vpc_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#delete_vpc_endpoint)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#generate_presigned_url)
        """
    def get_access_policy(
        self, *, name: str, type: Literal["data"]
    ) -> GetAccessPolicyResponseTypeDef:
        """
        Returns an OpenSearch Serverless access policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.get_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#get_access_policy)
        """
    def get_account_settings(self) -> GetAccountSettingsResponseTypeDef:
        """
        Returns account-level settings related to OpenSearch Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.get_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#get_account_settings)
        """
    def get_policies_stats(self) -> GetPoliciesStatsResponseTypeDef:
        """
        Returns statistical information about your OpenSearch Serverless access
        policies, security configurations, and security policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.get_policies_stats)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#get_policies_stats)
        """
    def get_security_config(self, *, id: str) -> GetSecurityConfigResponseTypeDef:
        """
        Returns information about an OpenSearch Serverless security configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.get_security_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#get_security_config)
        """
    def get_security_policy(
        self, *, name: str, type: SecurityPolicyTypeType
    ) -> GetSecurityPolicyResponseTypeDef:
        """
        Returns information about a configured OpenSearch Serverless security policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.get_security_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#get_security_policy)
        """
    def list_access_policies(
        self,
        *,
        type: Literal["data"],
        maxResults: int = None,
        nextToken: str = None,
        resource: List[str] = None
    ) -> ListAccessPoliciesResponseTypeDef:
        """
        Returns information about a list of OpenSearch Serverless access policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.list_access_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#list_access_policies)
        """
    def list_collections(
        self,
        *,
        collectionFilters: "CollectionFiltersTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListCollectionsResponseTypeDef:
        """
        Lists all OpenSearch Serverless collections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.list_collections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#list_collections)
        """
    def list_lifecycle_policies(
        self,
        *,
        type: Literal["retention"],
        maxResults: int = None,
        nextToken: str = None,
        resources: List[str] = None
    ) -> ListLifecyclePoliciesResponseTypeDef:
        """
        Returns a list of OpenSearch Serverless lifecycle policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.list_lifecycle_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#list_lifecycle_policies)
        """
    def list_security_configs(
        self, *, type: Literal["saml"], maxResults: int = None, nextToken: str = None
    ) -> ListSecurityConfigsResponseTypeDef:
        """
        Returns information about configured OpenSearch Serverless security
        configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.list_security_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#list_security_configs)
        """
    def list_security_policies(
        self,
        *,
        type: SecurityPolicyTypeType,
        maxResults: int = None,
        nextToken: str = None,
        resource: List[str] = None
    ) -> ListSecurityPoliciesResponseTypeDef:
        """
        Returns information about configured OpenSearch Serverless security policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.list_security_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#list_security_policies)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns the tags for an OpenSearch Serverless resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#list_tags_for_resource)
        """
    def list_vpc_endpoints(
        self,
        *,
        maxResults: int = None,
        nextToken: str = None,
        vpcEndpointFilters: "VpcEndpointFiltersTypeDef" = None
    ) -> ListVpcEndpointsResponseTypeDef:
        """
        Returns the OpenSearch Serverless-managed interface VPC endpoints associated
        with the current account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.list_vpc_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#list_vpc_endpoints)
        """
    def tag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Associates tags with an OpenSearch Serverless resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag or set of tags from an OpenSearch Serverless resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#untag_resource)
        """
    def update_access_policy(
        self,
        *,
        name: str,
        policyVersion: str,
        type: Literal["data"],
        clientToken: str = None,
        description: str = None,
        policy: str = None
    ) -> UpdateAccessPolicyResponseTypeDef:
        """
        Updates an OpenSearch Serverless access policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.update_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#update_access_policy)
        """
    def update_account_settings(
        self, *, capacityLimits: "CapacityLimitsTypeDef" = None
    ) -> UpdateAccountSettingsResponseTypeDef:
        """
        Update the OpenSearch Serverless settings for the current Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.update_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#update_account_settings)
        """
    def update_collection(
        self, *, id: str, clientToken: str = None, description: str = None
    ) -> UpdateCollectionResponseTypeDef:
        """
        Updates an OpenSearch Serverless collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.update_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#update_collection)
        """
    def update_lifecycle_policy(
        self,
        *,
        name: str,
        policyVersion: str,
        type: Literal["retention"],
        clientToken: str = None,
        description: str = None,
        policy: str = None
    ) -> UpdateLifecyclePolicyResponseTypeDef:
        """
        Updates an OpenSearch Serverless access policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.update_lifecycle_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#update_lifecycle_policy)
        """
    def update_security_config(
        self,
        *,
        configVersion: str,
        id: str,
        clientToken: str = None,
        description: str = None,
        samlOptions: "SamlConfigOptionsTypeDef" = None
    ) -> UpdateSecurityConfigResponseTypeDef:
        """
        Updates a security configuration for OpenSearch Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.update_security_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#update_security_config)
        """
    def update_security_policy(
        self,
        *,
        name: str,
        policyVersion: str,
        type: SecurityPolicyTypeType,
        clientToken: str = None,
        description: str = None,
        policy: str = None
    ) -> UpdateSecurityPolicyResponseTypeDef:
        """
        Updates an OpenSearch Serverless security policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.update_security_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#update_security_policy)
        """
    def update_vpc_endpoint(
        self,
        *,
        id: str,
        addSecurityGroupIds: List[str] = None,
        addSubnetIds: List[str] = None,
        clientToken: str = None,
        removeSecurityGroupIds: List[str] = None,
        removeSubnetIds: List[str] = None
    ) -> UpdateVpcEndpointResponseTypeDef:
        """
        Updates an OpenSearch Serverless-managed interface endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/opensearchserverless.html#OpenSearchServiceServerless.Client.update_vpc_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/client.html#update_vpc_endpoint)
        """
