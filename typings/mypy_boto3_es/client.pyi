# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for es service client

Usage::

    ```python
    import boto3
    from mypy_boto3_es import ElasticsearchServiceClient

    client: ElasticsearchServiceClient = boto3.client("es")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_es.paginator import (
    DescribeReservedElasticsearchInstanceOfferingsPaginator,
    DescribeReservedElasticsearchInstancesPaginator,
    GetUpgradeHistoryPaginator,
    ListElasticsearchInstanceTypesPaginator,
    ListElasticsearchVersionsPaginator,
)
from mypy_boto3_es.type_defs import (
    AcceptInboundCrossClusterSearchConnectionResponseTypeDef,
    AdvancedSecurityOptionsInputTypeDef,
    AssociatePackageResponseTypeDef,
    CancelElasticsearchServiceSoftwareUpdateResponseTypeDef,
    CognitoOptionsTypeDef,
    CreateElasticsearchDomainResponseTypeDef,
    CreateOutboundCrossClusterSearchConnectionResponseTypeDef,
    CreatePackageResponseTypeDef,
    DeleteElasticsearchDomainResponseTypeDef,
    DeleteInboundCrossClusterSearchConnectionResponseTypeDef,
    DeleteOutboundCrossClusterSearchConnectionResponseTypeDef,
    DeletePackageResponseTypeDef,
    DescribeElasticsearchDomainConfigResponseTypeDef,
    DescribeElasticsearchDomainResponseTypeDef,
    DescribeElasticsearchDomainsResponseTypeDef,
    DescribeElasticsearchInstanceTypeLimitsResponseTypeDef,
    DescribeInboundCrossClusterSearchConnectionsResponseTypeDef,
    DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef,
    DescribePackagesFilterTypeDef,
    DescribePackagesResponseTypeDef,
    DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef,
    DescribeReservedElasticsearchInstancesResponseTypeDef,
    DissociatePackageResponseTypeDef,
    DomainEndpointOptionsTypeDef,
    DomainInformationTypeDef,
    EBSOptionsTypeDef,
    ElasticsearchClusterConfigTypeDef,
    EncryptionAtRestOptionsTypeDef,
    FilterTypeDef,
    GetCompatibleElasticsearchVersionsResponseTypeDef,
    GetUpgradeHistoryResponseTypeDef,
    GetUpgradeStatusResponseTypeDef,
    ListDomainNamesResponseTypeDef,
    ListDomainsForPackageResponseTypeDef,
    ListElasticsearchInstanceTypesResponseTypeDef,
    ListElasticsearchVersionsResponseTypeDef,
    ListPackagesForDomainResponseTypeDef,
    ListTagsResponseTypeDef,
    LogPublishingOptionTypeDef,
    NodeToNodeEncryptionOptionsTypeDef,
    PackageSourceTypeDef,
    PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef,
    RejectInboundCrossClusterSearchConnectionResponseTypeDef,
    SnapshotOptionsTypeDef,
    StartElasticsearchServiceSoftwareUpdateResponseTypeDef,
    TagTypeDef,
    UpdateElasticsearchDomainConfigResponseTypeDef,
    UpgradeElasticsearchDomainResponseTypeDef,
    VPCOptionsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ElasticsearchServiceClient",)


class Exceptions:
    AccessDeniedException: Type[Boto3ClientError]
    BaseException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    ConflictException: Type[Boto3ClientError]
    DisabledOperationException: Type[Boto3ClientError]
    InternalException: Type[Boto3ClientError]
    InvalidPaginationTokenException: Type[Boto3ClientError]
    InvalidTypeException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    ResourceAlreadyExistsException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    ValidationException: Type[Boto3ClientError]


class ElasticsearchServiceClient:
    """
    [ElasticsearchService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client)
    """

    exceptions: Exceptions

    def accept_inbound_cross_cluster_search_connection(
        self, CrossClusterSearchConnectionId: str
    ) -> AcceptInboundCrossClusterSearchConnectionResponseTypeDef:
        """
        [Client.accept_inbound_cross_cluster_search_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.accept_inbound_cross_cluster_search_connection)
        """

    def add_tags(self, ARN: str, TagList: List["TagTypeDef"]) -> None:
        """
        [Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.add_tags)
        """

    def associate_package(self, PackageID: str, DomainName: str) -> AssociatePackageResponseTypeDef:
        """
        [Client.associate_package documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.associate_package)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.can_paginate)
        """

    def cancel_elasticsearch_service_software_update(
        self, DomainName: str
    ) -> CancelElasticsearchServiceSoftwareUpdateResponseTypeDef:
        """
        [Client.cancel_elasticsearch_service_software_update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.cancel_elasticsearch_service_software_update)
        """

    def create_elasticsearch_domain(
        self,
        DomainName: str,
        ElasticsearchVersion: str = None,
        ElasticsearchClusterConfig: "ElasticsearchClusterConfigTypeDef" = None,
        EBSOptions: "EBSOptionsTypeDef" = None,
        AccessPolicies: str = None,
        SnapshotOptions: "SnapshotOptionsTypeDef" = None,
        VPCOptions: VPCOptionsTypeDef = None,
        CognitoOptions: "CognitoOptionsTypeDef" = None,
        EncryptionAtRestOptions: "EncryptionAtRestOptionsTypeDef" = None,
        NodeToNodeEncryptionOptions: "NodeToNodeEncryptionOptionsTypeDef" = None,
        AdvancedOptions: Dict[str, str] = None,
        LogPublishingOptions: Dict[
            Literal["INDEX_SLOW_LOGS", "SEARCH_SLOW_LOGS", "ES_APPLICATION_LOGS"],
            "LogPublishingOptionTypeDef",
        ] = None,
        DomainEndpointOptions: "DomainEndpointOptionsTypeDef" = None,
        AdvancedSecurityOptions: AdvancedSecurityOptionsInputTypeDef = None,
    ) -> CreateElasticsearchDomainResponseTypeDef:
        """
        [Client.create_elasticsearch_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.create_elasticsearch_domain)
        """

    def create_outbound_cross_cluster_search_connection(
        self,
        SourceDomainInfo: "DomainInformationTypeDef",
        DestinationDomainInfo: "DomainInformationTypeDef",
        ConnectionAlias: str,
    ) -> CreateOutboundCrossClusterSearchConnectionResponseTypeDef:
        """
        [Client.create_outbound_cross_cluster_search_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.create_outbound_cross_cluster_search_connection)
        """

    def create_package(
        self,
        PackageName: str,
        PackageType: Literal["TXT-DICTIONARY"],
        PackageSource: PackageSourceTypeDef,
        PackageDescription: str = None,
    ) -> CreatePackageResponseTypeDef:
        """
        [Client.create_package documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.create_package)
        """

    def delete_elasticsearch_domain(
        self, DomainName: str
    ) -> DeleteElasticsearchDomainResponseTypeDef:
        """
        [Client.delete_elasticsearch_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.delete_elasticsearch_domain)
        """

    def delete_elasticsearch_service_role(self) -> None:
        """
        [Client.delete_elasticsearch_service_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.delete_elasticsearch_service_role)
        """

    def delete_inbound_cross_cluster_search_connection(
        self, CrossClusterSearchConnectionId: str
    ) -> DeleteInboundCrossClusterSearchConnectionResponseTypeDef:
        """
        [Client.delete_inbound_cross_cluster_search_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.delete_inbound_cross_cluster_search_connection)
        """

    def delete_outbound_cross_cluster_search_connection(
        self, CrossClusterSearchConnectionId: str
    ) -> DeleteOutboundCrossClusterSearchConnectionResponseTypeDef:
        """
        [Client.delete_outbound_cross_cluster_search_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.delete_outbound_cross_cluster_search_connection)
        """

    def delete_package(self, PackageID: str) -> DeletePackageResponseTypeDef:
        """
        [Client.delete_package documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.delete_package)
        """

    def describe_elasticsearch_domain(
        self, DomainName: str
    ) -> DescribeElasticsearchDomainResponseTypeDef:
        """
        [Client.describe_elasticsearch_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_domain)
        """

    def describe_elasticsearch_domain_config(
        self, DomainName: str
    ) -> DescribeElasticsearchDomainConfigResponseTypeDef:
        """
        [Client.describe_elasticsearch_domain_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_domain_config)
        """

    def describe_elasticsearch_domains(
        self, DomainNames: List[str]
    ) -> DescribeElasticsearchDomainsResponseTypeDef:
        """
        [Client.describe_elasticsearch_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_domains)
        """

    def describe_elasticsearch_instance_type_limits(
        self,
        InstanceType: Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "ultrawarm1.medium.elasticsearch",
            "ultrawarm1.large.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        ElasticsearchVersion: str,
        DomainName: str = None,
    ) -> DescribeElasticsearchInstanceTypeLimitsResponseTypeDef:
        """
        [Client.describe_elasticsearch_instance_type_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_instance_type_limits)
        """

    def describe_inbound_cross_cluster_search_connections(
        self, Filters: List[FilterTypeDef] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeInboundCrossClusterSearchConnectionsResponseTypeDef:
        """
        [Client.describe_inbound_cross_cluster_search_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.describe_inbound_cross_cluster_search_connections)
        """

    def describe_outbound_cross_cluster_search_connections(
        self, Filters: List[FilterTypeDef] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef:
        """
        [Client.describe_outbound_cross_cluster_search_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.describe_outbound_cross_cluster_search_connections)
        """

    def describe_packages(
        self,
        Filters: List[DescribePackagesFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribePackagesResponseTypeDef:
        """
        [Client.describe_packages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.describe_packages)
        """

    def describe_reserved_elasticsearch_instance_offerings(
        self,
        ReservedElasticsearchInstanceOfferingId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef:
        """
        [Client.describe_reserved_elasticsearch_instance_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.describe_reserved_elasticsearch_instance_offerings)
        """

    def describe_reserved_elasticsearch_instances(
        self,
        ReservedElasticsearchInstanceId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeReservedElasticsearchInstancesResponseTypeDef:
        """
        [Client.describe_reserved_elasticsearch_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.describe_reserved_elasticsearch_instances)
        """

    def dissociate_package(
        self, PackageID: str, DomainName: str
    ) -> DissociatePackageResponseTypeDef:
        """
        [Client.dissociate_package documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.dissociate_package)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.generate_presigned_url)
        """

    def get_compatible_elasticsearch_versions(
        self, DomainName: str = None
    ) -> GetCompatibleElasticsearchVersionsResponseTypeDef:
        """
        [Client.get_compatible_elasticsearch_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.get_compatible_elasticsearch_versions)
        """

    def get_upgrade_history(
        self, DomainName: str, MaxResults: int = None, NextToken: str = None
    ) -> GetUpgradeHistoryResponseTypeDef:
        """
        [Client.get_upgrade_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.get_upgrade_history)
        """

    def get_upgrade_status(self, DomainName: str) -> GetUpgradeStatusResponseTypeDef:
        """
        [Client.get_upgrade_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.get_upgrade_status)
        """

    def list_domain_names(self) -> ListDomainNamesResponseTypeDef:
        """
        [Client.list_domain_names documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.list_domain_names)
        """

    def list_domains_for_package(
        self, PackageID: str, MaxResults: int = None, NextToken: str = None
    ) -> ListDomainsForPackageResponseTypeDef:
        """
        [Client.list_domains_for_package documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.list_domains_for_package)
        """

    def list_elasticsearch_instance_types(
        self,
        ElasticsearchVersion: str,
        DomainName: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListElasticsearchInstanceTypesResponseTypeDef:
        """
        [Client.list_elasticsearch_instance_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.list_elasticsearch_instance_types)
        """

    def list_elasticsearch_versions(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListElasticsearchVersionsResponseTypeDef:
        """
        [Client.list_elasticsearch_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.list_elasticsearch_versions)
        """

    def list_packages_for_domain(
        self, DomainName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListPackagesForDomainResponseTypeDef:
        """
        [Client.list_packages_for_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.list_packages_for_domain)
        """

    def list_tags(self, ARN: str) -> ListTagsResponseTypeDef:
        """
        [Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.list_tags)
        """

    def purchase_reserved_elasticsearch_instance_offering(
        self,
        ReservedElasticsearchInstanceOfferingId: str,
        ReservationName: str,
        InstanceCount: int = None,
    ) -> PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef:
        """
        [Client.purchase_reserved_elasticsearch_instance_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.purchase_reserved_elasticsearch_instance_offering)
        """

    def reject_inbound_cross_cluster_search_connection(
        self, CrossClusterSearchConnectionId: str
    ) -> RejectInboundCrossClusterSearchConnectionResponseTypeDef:
        """
        [Client.reject_inbound_cross_cluster_search_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.reject_inbound_cross_cluster_search_connection)
        """

    def remove_tags(self, ARN: str, TagKeys: List[str]) -> None:
        """
        [Client.remove_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.remove_tags)
        """

    def start_elasticsearch_service_software_update(
        self, DomainName: str
    ) -> StartElasticsearchServiceSoftwareUpdateResponseTypeDef:
        """
        [Client.start_elasticsearch_service_software_update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.start_elasticsearch_service_software_update)
        """

    def update_elasticsearch_domain_config(
        self,
        DomainName: str,
        ElasticsearchClusterConfig: "ElasticsearchClusterConfigTypeDef" = None,
        EBSOptions: "EBSOptionsTypeDef" = None,
        SnapshotOptions: "SnapshotOptionsTypeDef" = None,
        VPCOptions: VPCOptionsTypeDef = None,
        CognitoOptions: "CognitoOptionsTypeDef" = None,
        AdvancedOptions: Dict[str, str] = None,
        AccessPolicies: str = None,
        LogPublishingOptions: Dict[
            Literal["INDEX_SLOW_LOGS", "SEARCH_SLOW_LOGS", "ES_APPLICATION_LOGS"],
            "LogPublishingOptionTypeDef",
        ] = None,
        DomainEndpointOptions: "DomainEndpointOptionsTypeDef" = None,
        AdvancedSecurityOptions: AdvancedSecurityOptionsInputTypeDef = None,
    ) -> UpdateElasticsearchDomainConfigResponseTypeDef:
        """
        [Client.update_elasticsearch_domain_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.update_elasticsearch_domain_config)
        """

    def upgrade_elasticsearch_domain(
        self, DomainName: str, TargetVersion: str, PerformCheckOnly: bool = None
    ) -> UpgradeElasticsearchDomainResponseTypeDef:
        """
        [Client.upgrade_elasticsearch_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Client.upgrade_elasticsearch_domain)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_elasticsearch_instance_offerings"]
    ) -> DescribeReservedElasticsearchInstanceOfferingsPaginator:
        """
        [Paginator.DescribeReservedElasticsearchInstanceOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstanceOfferings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_elasticsearch_instances"]
    ) -> DescribeReservedElasticsearchInstancesPaginator:
        """
        [Paginator.DescribeReservedElasticsearchInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_upgrade_history"]
    ) -> GetUpgradeHistoryPaginator:
        """
        [Paginator.GetUpgradeHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Paginator.GetUpgradeHistory)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_elasticsearch_instance_types"]
    ) -> ListElasticsearchInstanceTypesPaginator:
        """
        [Paginator.ListElasticsearchInstanceTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchInstanceTypes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_elasticsearch_versions"]
    ) -> ListElasticsearchVersionsPaginator:
        """
        [Paginator.ListElasticsearchVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchVersions)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
