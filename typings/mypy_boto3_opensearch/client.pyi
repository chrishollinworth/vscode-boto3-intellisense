"""
Type annotations for opensearch service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_opensearch import OpenSearchServiceClient

    client: OpenSearchServiceClient = boto3.client("opensearch")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import EngineTypeType, LogTypeType, OpenSearchPartitionInstanceTypeType
from .type_defs import (
    AcceptInboundConnectionResponseTypeDef,
    AdvancedSecurityOptionsInputTypeDef,
    AssociatePackageResponseTypeDef,
    AuthorizeVpcEndpointAccessResponseTypeDef,
    AutoTuneOptionsInputTypeDef,
    AutoTuneOptionsTypeDef,
    CancelServiceSoftwareUpdateResponseTypeDef,
    ClusterConfigTypeDef,
    CognitoOptionsTypeDef,
    CreateDomainResponseTypeDef,
    CreateOutboundConnectionResponseTypeDef,
    CreatePackageResponseTypeDef,
    CreateVpcEndpointResponseTypeDef,
    DeleteDomainResponseTypeDef,
    DeleteInboundConnectionResponseTypeDef,
    DeleteOutboundConnectionResponseTypeDef,
    DeletePackageResponseTypeDef,
    DeleteVpcEndpointResponseTypeDef,
    DescribeDomainAutoTunesResponseTypeDef,
    DescribeDomainChangeProgressResponseTypeDef,
    DescribeDomainConfigResponseTypeDef,
    DescribeDomainResponseTypeDef,
    DescribeDomainsResponseTypeDef,
    DescribeInboundConnectionsResponseTypeDef,
    DescribeInstanceTypeLimitsResponseTypeDef,
    DescribeOutboundConnectionsResponseTypeDef,
    DescribePackagesFilterTypeDef,
    DescribePackagesResponseTypeDef,
    DescribeReservedInstanceOfferingsResponseTypeDef,
    DescribeReservedInstancesResponseTypeDef,
    DescribeVpcEndpointsResponseTypeDef,
    DissociatePackageResponseTypeDef,
    DomainEndpointOptionsTypeDef,
    DomainInformationContainerTypeDef,
    EBSOptionsTypeDef,
    EncryptionAtRestOptionsTypeDef,
    FilterTypeDef,
    GetCompatibleVersionsResponseTypeDef,
    GetPackageVersionHistoryResponseTypeDef,
    GetUpgradeHistoryResponseTypeDef,
    GetUpgradeStatusResponseTypeDef,
    ListDomainNamesResponseTypeDef,
    ListDomainsForPackageResponseTypeDef,
    ListInstanceTypeDetailsResponseTypeDef,
    ListPackagesForDomainResponseTypeDef,
    ListTagsResponseTypeDef,
    ListVersionsResponseTypeDef,
    ListVpcEndpointAccessResponseTypeDef,
    ListVpcEndpointsForDomainResponseTypeDef,
    ListVpcEndpointsResponseTypeDef,
    LogPublishingOptionTypeDef,
    NodeToNodeEncryptionOptionsTypeDef,
    PackageSourceTypeDef,
    PurchaseReservedInstanceOfferingResponseTypeDef,
    RejectInboundConnectionResponseTypeDef,
    SnapshotOptionsTypeDef,
    StartServiceSoftwareUpdateResponseTypeDef,
    TagTypeDef,
    UpdateDomainConfigResponseTypeDef,
    UpdatePackageResponseTypeDef,
    UpdateVpcEndpointResponseTypeDef,
    UpgradeDomainResponseTypeDef,
    VPCOptionsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("OpenSearchServiceClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BaseException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DisabledOperationException: Type[BotocoreClientError]
    InternalException: Type[BotocoreClientError]
    InvalidPaginationTokenException: Type[BotocoreClientError]
    InvalidTypeException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class OpenSearchServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        OpenSearchServiceClient exceptions.
        """
    def accept_inbound_connection(
        self, *, ConnectionId: str
    ) -> AcceptInboundConnectionResponseTypeDef:
        """
        Allows the destination Amazon OpenSearch Service domain owner to accept an
        inbound cross-cluster search connection request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.accept_inbound_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#accept_inbound_connection)
        """
    def add_tags(self, *, ARN: str, TagList: List["TagTypeDef"]) -> None:
        """
        Attaches tags to an existing Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.add_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#add_tags)
        """
    def associate_package(
        self, *, PackageID: str, DomainName: str
    ) -> AssociatePackageResponseTypeDef:
        """
        Associates a package with an Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.associate_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#associate_package)
        """
    def authorize_vpc_endpoint_access(
        self, *, DomainName: str, Account: str
    ) -> AuthorizeVpcEndpointAccessResponseTypeDef:
        """
        Provides access to an Amazon OpenSearch Service domain through the use of an
        interface VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.authorize_vpc_endpoint_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#authorize_vpc_endpoint_access)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#can_paginate)
        """
    def cancel_service_software_update(
        self, *, DomainName: str
    ) -> CancelServiceSoftwareUpdateResponseTypeDef:
        """
        Cancels a scheduled service software update for an Amazon OpenSearch Service
        domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.cancel_service_software_update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#cancel_service_software_update)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#close)
        """
    def create_domain(
        self,
        *,
        DomainName: str,
        EngineVersion: str = None,
        ClusterConfig: "ClusterConfigTypeDef" = None,
        EBSOptions: "EBSOptionsTypeDef" = None,
        AccessPolicies: str = None,
        SnapshotOptions: "SnapshotOptionsTypeDef" = None,
        VPCOptions: "VPCOptionsTypeDef" = None,
        CognitoOptions: "CognitoOptionsTypeDef" = None,
        EncryptionAtRestOptions: "EncryptionAtRestOptionsTypeDef" = None,
        NodeToNodeEncryptionOptions: "NodeToNodeEncryptionOptionsTypeDef" = None,
        AdvancedOptions: Dict[str, str] = None,
        LogPublishingOptions: Dict[LogTypeType, "LogPublishingOptionTypeDef"] = None,
        DomainEndpointOptions: "DomainEndpointOptionsTypeDef" = None,
        AdvancedSecurityOptions: "AdvancedSecurityOptionsInputTypeDef" = None,
        TagList: List["TagTypeDef"] = None,
        AutoTuneOptions: "AutoTuneOptionsInputTypeDef" = None
    ) -> CreateDomainResponseTypeDef:
        """
        Creates an Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.create_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#create_domain)
        """
    def create_outbound_connection(
        self,
        *,
        LocalDomainInfo: "DomainInformationContainerTypeDef",
        RemoteDomainInfo: "DomainInformationContainerTypeDef",
        ConnectionAlias: str
    ) -> CreateOutboundConnectionResponseTypeDef:
        """
        Creates a new cross-cluster search connection from a source Amazon OpenSearch
        Service domain to a destination domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.create_outbound_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#create_outbound_connection)
        """
    def create_package(
        self,
        *,
        PackageName: str,
        PackageType: Literal["TXT-DICTIONARY"],
        PackageSource: "PackageSourceTypeDef",
        PackageDescription: str = None
    ) -> CreatePackageResponseTypeDef:
        """
        Creates a package for use with Amazon OpenSearch Service domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.create_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#create_package)
        """
    def create_vpc_endpoint(
        self, *, DomainArn: str, VpcOptions: "VPCOptionsTypeDef", ClientToken: str = None
    ) -> CreateVpcEndpointResponseTypeDef:
        """
        Creates an Amazon OpenSearch Service-managed VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.create_vpc_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#create_vpc_endpoint)
        """
    def delete_domain(self, *, DomainName: str) -> DeleteDomainResponseTypeDef:
        """
        Deletes an Amazon OpenSearch Service domain and all of its data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.delete_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#delete_domain)
        """
    def delete_inbound_connection(
        self, *, ConnectionId: str
    ) -> DeleteInboundConnectionResponseTypeDef:
        """
        Allows the destination Amazon OpenSearch Service domain owner to delete an
        existing inbound cross-cluster search connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.delete_inbound_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#delete_inbound_connection)
        """
    def delete_outbound_connection(
        self, *, ConnectionId: str
    ) -> DeleteOutboundConnectionResponseTypeDef:
        """
        Allows the source Amazon OpenSearch Service domain owner to delete an existing
        outbound cross-cluster search connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.delete_outbound_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#delete_outbound_connection)
        """
    def delete_package(self, *, PackageID: str) -> DeletePackageResponseTypeDef:
        """
        Deletes an Amazon OpenSearch Service package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.delete_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#delete_package)
        """
    def delete_vpc_endpoint(self, *, VpcEndpointId: str) -> DeleteVpcEndpointResponseTypeDef:
        """
        Deletes an Amazon OpenSearch Service-managed interface VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.delete_vpc_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#delete_vpc_endpoint)
        """
    def describe_domain(self, *, DomainName: str) -> DescribeDomainResponseTypeDef:
        """
        Describes the domain configuration for the specified Amazon OpenSearch Service
        domain, including the domain ID, domain service endpoint, and domain ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.describe_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#describe_domain)
        """
    def describe_domain_auto_tunes(
        self, *, DomainName: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeDomainAutoTunesResponseTypeDef:
        """
        Returns the list of optimizations that Auto-Tune has made to an Amazon
        OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.describe_domain_auto_tunes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#describe_domain_auto_tunes)
        """
    def describe_domain_change_progress(
        self, *, DomainName: str, ChangeId: str = None
    ) -> DescribeDomainChangeProgressResponseTypeDef:
        """
        Returns information about the current blue/green deployment happening on an
        Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.describe_domain_change_progress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#describe_domain_change_progress)
        """
    def describe_domain_config(self, *, DomainName: str) -> DescribeDomainConfigResponseTypeDef:
        """
        Returns the configuration of an Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.describe_domain_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#describe_domain_config)
        """
    def describe_domains(self, *, DomainNames: List[str]) -> DescribeDomainsResponseTypeDef:
        """
        Returns domain configuration information about the specified Amazon OpenSearch
        Service domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.describe_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#describe_domains)
        """
    def describe_inbound_connections(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeInboundConnectionsResponseTypeDef:
        """
        Lists all the inbound cross-cluster search connections for a destination
        (remote) Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.describe_inbound_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#describe_inbound_connections)
        """
    def describe_instance_type_limits(
        self,
        *,
        InstanceType: OpenSearchPartitionInstanceTypeType,
        EngineVersion: str,
        DomainName: str = None
    ) -> DescribeInstanceTypeLimitsResponseTypeDef:
        """
        Describes the instance count, storage, and master node limits for a given
        OpenSearch or Elasticsearch version and instance type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.describe_instance_type_limits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#describe_instance_type_limits)
        """
    def describe_outbound_connections(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeOutboundConnectionsResponseTypeDef:
        """
        Lists all the outbound cross-cluster connections for a local (source) Amazon
        OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.describe_outbound_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#describe_outbound_connections)
        """
    def describe_packages(
        self,
        *,
        Filters: List["DescribePackagesFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribePackagesResponseTypeDef:
        """
        Describes all packages available to OpenSearch Service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.describe_packages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#describe_packages)
        """
    def describe_reserved_instance_offerings(
        self,
        *,
        ReservedInstanceOfferingId: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeReservedInstanceOfferingsResponseTypeDef:
        """
        Describes the available Amazon OpenSearch Service Reserved Instance offerings
        for a given Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.describe_reserved_instance_offerings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#describe_reserved_instance_offerings)
        """
    def describe_reserved_instances(
        self, *, ReservedInstanceId: str = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeReservedInstancesResponseTypeDef:
        """
        Describes the Amazon OpenSearch Service instances that you have reserved in a
        given Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.describe_reserved_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#describe_reserved_instances)
        """
    def describe_vpc_endpoints(
        self, *, VpcEndpointIds: List[str]
    ) -> DescribeVpcEndpointsResponseTypeDef:
        """
        Describes one or more Amazon OpenSearch Service-managed VPC endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.describe_vpc_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#describe_vpc_endpoints)
        """
    def dissociate_package(
        self, *, PackageID: str, DomainName: str
    ) -> DissociatePackageResponseTypeDef:
        """
        Removes a package from the specified Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.dissociate_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#dissociate_package)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#generate_presigned_url)
        """
    def get_compatible_versions(
        self, *, DomainName: str = None
    ) -> GetCompatibleVersionsResponseTypeDef:
        """
        Returns a map of OpenSearch or Elasticsearch versions and the versions you can
        upgrade them to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.get_compatible_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#get_compatible_versions)
        """
    def get_package_version_history(
        self, *, PackageID: str, MaxResults: int = None, NextToken: str = None
    ) -> GetPackageVersionHistoryResponseTypeDef:
        """
        Returns a list of Amazon OpenSearch Service package versions, along with their
        creation time and commit message.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.get_package_version_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#get_package_version_history)
        """
    def get_upgrade_history(
        self, *, DomainName: str, MaxResults: int = None, NextToken: str = None
    ) -> GetUpgradeHistoryResponseTypeDef:
        """
        Retrieves the complete history of the last 10 upgrades performed on an Amazon
        OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.get_upgrade_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#get_upgrade_history)
        """
    def get_upgrade_status(self, *, DomainName: str) -> GetUpgradeStatusResponseTypeDef:
        """
        Returns the most recent status of the last upgrade or upgrade eligibility check
        performed on an Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.get_upgrade_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#get_upgrade_status)
        """
    def list_domain_names(
        self, *, EngineType: EngineTypeType = None
    ) -> ListDomainNamesResponseTypeDef:
        """
        Returns the names of all Amazon OpenSearch Service domains owned by the current
        user in the active Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.list_domain_names)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#list_domain_names)
        """
    def list_domains_for_package(
        self, *, PackageID: str, MaxResults: int = None, NextToken: str = None
    ) -> ListDomainsForPackageResponseTypeDef:
        """
        Lists all Amazon OpenSearch Service domains associated with a given package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.list_domains_for_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#list_domains_for_package)
        """
    def list_instance_type_details(
        self,
        *,
        EngineVersion: str,
        DomainName: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListInstanceTypeDetailsResponseTypeDef:
        """
        Lists all instance types and available features for a given OpenSearch or
        Elasticsearch version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.list_instance_type_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#list_instance_type_details)
        """
    def list_packages_for_domain(
        self, *, DomainName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListPackagesForDomainResponseTypeDef:
        """
        Lists all packages associated with an Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.list_packages_for_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#list_packages_for_domain)
        """
    def list_tags(self, *, ARN: str) -> ListTagsResponseTypeDef:
        """
        Returns all resource tags for an Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.list_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#list_tags)
        """
    def list_versions(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListVersionsResponseTypeDef:
        """
        Lists all versions of OpenSearch and Elasticsearch that Amazon OpenSearch
        Service supports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.list_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#list_versions)
        """
    def list_vpc_endpoint_access(
        self, *, DomainName: str, NextToken: str = None
    ) -> ListVpcEndpointAccessResponseTypeDef:
        """
        Retrieves information about each Amazon Web Services principal that is allowed
        to access a given Amazon OpenSearch Service domain through the use of an
        interface VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.list_vpc_endpoint_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#list_vpc_endpoint_access)
        """
    def list_vpc_endpoints(self, *, NextToken: str = None) -> ListVpcEndpointsResponseTypeDef:
        """
        Retrieves all Amazon OpenSearch Service-managed VPC endpoints in the current
        Amazon Web Services account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.list_vpc_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#list_vpc_endpoints)
        """
    def list_vpc_endpoints_for_domain(
        self, *, DomainName: str, NextToken: str = None
    ) -> ListVpcEndpointsForDomainResponseTypeDef:
        """
        Retrieves all Amazon OpenSearch Service-managed VPC endpoints associated with a
        particular domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.list_vpc_endpoints_for_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#list_vpc_endpoints_for_domain)
        """
    def purchase_reserved_instance_offering(
        self, *, ReservedInstanceOfferingId: str, ReservationName: str, InstanceCount: int = None
    ) -> PurchaseReservedInstanceOfferingResponseTypeDef:
        """
        Allows you to purchase Amazon OpenSearch Service Reserved Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.purchase_reserved_instance_offering)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#purchase_reserved_instance_offering)
        """
    def reject_inbound_connection(
        self, *, ConnectionId: str
    ) -> RejectInboundConnectionResponseTypeDef:
        """
        Allows the remote Amazon OpenSearch Service domain owner to reject an inbound
        cross-cluster connection request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.reject_inbound_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#reject_inbound_connection)
        """
    def remove_tags(self, *, ARN: str, TagKeys: List[str]) -> None:
        """
        Removes the specified set of tags from an Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.remove_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#remove_tags)
        """
    def revoke_vpc_endpoint_access(self, *, DomainName: str, Account: str) -> Dict[str, Any]:
        """
        Revokes access to an Amazon OpenSearch Service domain that was provided through
        an interface VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.revoke_vpc_endpoint_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#revoke_vpc_endpoint_access)
        """
    def start_service_software_update(
        self, *, DomainName: str
    ) -> StartServiceSoftwareUpdateResponseTypeDef:
        """
        Schedules a service software update for an Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.start_service_software_update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#start_service_software_update)
        """
    def update_domain_config(
        self,
        *,
        DomainName: str,
        ClusterConfig: "ClusterConfigTypeDef" = None,
        EBSOptions: "EBSOptionsTypeDef" = None,
        SnapshotOptions: "SnapshotOptionsTypeDef" = None,
        VPCOptions: "VPCOptionsTypeDef" = None,
        CognitoOptions: "CognitoOptionsTypeDef" = None,
        AdvancedOptions: Dict[str, str] = None,
        AccessPolicies: str = None,
        LogPublishingOptions: Dict[LogTypeType, "LogPublishingOptionTypeDef"] = None,
        EncryptionAtRestOptions: "EncryptionAtRestOptionsTypeDef" = None,
        DomainEndpointOptions: "DomainEndpointOptionsTypeDef" = None,
        NodeToNodeEncryptionOptions: "NodeToNodeEncryptionOptionsTypeDef" = None,
        AdvancedSecurityOptions: "AdvancedSecurityOptionsInputTypeDef" = None,
        AutoTuneOptions: "AutoTuneOptionsTypeDef" = None,
        DryRun: bool = None
    ) -> UpdateDomainConfigResponseTypeDef:
        """
        Modifies the cluster configuration of the specified Amazon OpenSearch Service
        domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.update_domain_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#update_domain_config)
        """
    def update_package(
        self,
        *,
        PackageID: str,
        PackageSource: "PackageSourceTypeDef",
        PackageDescription: str = None,
        CommitMessage: str = None
    ) -> UpdatePackageResponseTypeDef:
        """
        Updates a package for use with Amazon OpenSearch Service domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.update_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#update_package)
        """
    def update_vpc_endpoint(
        self, *, VpcEndpointId: str, VpcOptions: "VPCOptionsTypeDef"
    ) -> UpdateVpcEndpointResponseTypeDef:
        """
        Modifies an Amazon OpenSearch Service-managed interface VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.update_vpc_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#update_vpc_endpoint)
        """
    def upgrade_domain(
        self,
        *,
        DomainName: str,
        TargetVersion: str,
        PerformCheckOnly: bool = None,
        AdvancedOptions: Dict[str, str] = None
    ) -> UpgradeDomainResponseTypeDef:
        """
        Allows you to either upgrade your Amazon OpenSearch Service domain or perform an
        upgrade eligibility check to a compatible version of OpenSearch or
        Elasticsearch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/opensearch.html#OpenSearchService.Client.upgrade_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/client.html#upgrade_domain)
        """
