"""
Type annotations for es service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_es.client import ElasticsearchServiceClient

    session = Session()
    client: ElasticsearchServiceClient = session.client("es")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeReservedElasticsearchInstanceOfferingsPaginator,
    DescribeReservedElasticsearchInstancesPaginator,
    GetUpgradeHistoryPaginator,
    ListElasticsearchInstanceTypesPaginator,
    ListElasticsearchVersionsPaginator,
)
from .type_defs import (
    AcceptInboundCrossClusterSearchConnectionRequestTypeDef,
    AcceptInboundCrossClusterSearchConnectionResponseTypeDef,
    AddTagsRequestTypeDef,
    AssociatePackageRequestTypeDef,
    AssociatePackageResponseTypeDef,
    AuthorizeVpcEndpointAccessRequestTypeDef,
    AuthorizeVpcEndpointAccessResponseTypeDef,
    CancelDomainConfigChangeRequestTypeDef,
    CancelDomainConfigChangeResponseTypeDef,
    CancelElasticsearchServiceSoftwareUpdateRequestTypeDef,
    CancelElasticsearchServiceSoftwareUpdateResponseTypeDef,
    CreateElasticsearchDomainRequestTypeDef,
    CreateElasticsearchDomainResponseTypeDef,
    CreateOutboundCrossClusterSearchConnectionRequestTypeDef,
    CreateOutboundCrossClusterSearchConnectionResponseTypeDef,
    CreatePackageRequestTypeDef,
    CreatePackageResponseTypeDef,
    CreateVpcEndpointRequestTypeDef,
    CreateVpcEndpointResponseTypeDef,
    DeleteElasticsearchDomainRequestTypeDef,
    DeleteElasticsearchDomainResponseTypeDef,
    DeleteInboundCrossClusterSearchConnectionRequestTypeDef,
    DeleteInboundCrossClusterSearchConnectionResponseTypeDef,
    DeleteOutboundCrossClusterSearchConnectionRequestTypeDef,
    DeleteOutboundCrossClusterSearchConnectionResponseTypeDef,
    DeletePackageRequestTypeDef,
    DeletePackageResponseTypeDef,
    DeleteVpcEndpointRequestTypeDef,
    DeleteVpcEndpointResponseTypeDef,
    DescribeDomainAutoTunesRequestTypeDef,
    DescribeDomainAutoTunesResponseTypeDef,
    DescribeDomainChangeProgressRequestTypeDef,
    DescribeDomainChangeProgressResponseTypeDef,
    DescribeElasticsearchDomainConfigRequestTypeDef,
    DescribeElasticsearchDomainConfigResponseTypeDef,
    DescribeElasticsearchDomainRequestTypeDef,
    DescribeElasticsearchDomainResponseTypeDef,
    DescribeElasticsearchDomainsRequestTypeDef,
    DescribeElasticsearchDomainsResponseTypeDef,
    DescribeElasticsearchInstanceTypeLimitsRequestTypeDef,
    DescribeElasticsearchInstanceTypeLimitsResponseTypeDef,
    DescribeInboundCrossClusterSearchConnectionsRequestTypeDef,
    DescribeInboundCrossClusterSearchConnectionsResponseTypeDef,
    DescribeOutboundCrossClusterSearchConnectionsRequestTypeDef,
    DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef,
    DescribePackagesRequestTypeDef,
    DescribePackagesResponseTypeDef,
    DescribeReservedElasticsearchInstanceOfferingsRequestTypeDef,
    DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef,
    DescribeReservedElasticsearchInstancesRequestTypeDef,
    DescribeReservedElasticsearchInstancesResponseTypeDef,
    DescribeVpcEndpointsRequestTypeDef,
    DescribeVpcEndpointsResponseTypeDef,
    DissociatePackageRequestTypeDef,
    DissociatePackageResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetCompatibleElasticsearchVersionsRequestTypeDef,
    GetCompatibleElasticsearchVersionsResponseTypeDef,
    GetPackageVersionHistoryRequestTypeDef,
    GetPackageVersionHistoryResponseTypeDef,
    GetUpgradeHistoryRequestTypeDef,
    GetUpgradeHistoryResponseTypeDef,
    GetUpgradeStatusRequestTypeDef,
    GetUpgradeStatusResponseTypeDef,
    ListDomainNamesRequestTypeDef,
    ListDomainNamesResponseTypeDef,
    ListDomainsForPackageRequestTypeDef,
    ListDomainsForPackageResponseTypeDef,
    ListElasticsearchInstanceTypesRequestTypeDef,
    ListElasticsearchInstanceTypesResponseTypeDef,
    ListElasticsearchVersionsRequestTypeDef,
    ListElasticsearchVersionsResponseTypeDef,
    ListPackagesForDomainRequestTypeDef,
    ListPackagesForDomainResponseTypeDef,
    ListTagsRequestTypeDef,
    ListTagsResponseTypeDef,
    ListVpcEndpointAccessRequestTypeDef,
    ListVpcEndpointAccessResponseTypeDef,
    ListVpcEndpointsForDomainRequestTypeDef,
    ListVpcEndpointsForDomainResponseTypeDef,
    ListVpcEndpointsRequestTypeDef,
    ListVpcEndpointsResponseTypeDef,
    PurchaseReservedElasticsearchInstanceOfferingRequestTypeDef,
    PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef,
    RejectInboundCrossClusterSearchConnectionRequestTypeDef,
    RejectInboundCrossClusterSearchConnectionResponseTypeDef,
    RemoveTagsRequestTypeDef,
    RevokeVpcEndpointAccessRequestTypeDef,
    StartElasticsearchServiceSoftwareUpdateRequestTypeDef,
    StartElasticsearchServiceSoftwareUpdateResponseTypeDef,
    UpdateElasticsearchDomainConfigRequestTypeDef,
    UpdateElasticsearchDomainConfigResponseTypeDef,
    UpdatePackageRequestTypeDef,
    UpdatePackageResponseTypeDef,
    UpdateVpcEndpointRequestTypeDef,
    UpdateVpcEndpointResponseTypeDef,
    UpgradeElasticsearchDomainRequestTypeDef,
    UpgradeElasticsearchDomainResponseTypeDef,
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

__all__ = ("ElasticsearchServiceClient",)

class Exceptions(BaseClientExceptions):
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

class ElasticsearchServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ElasticsearchServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#generate_presigned_url)
        """

    def accept_inbound_cross_cluster_search_connection(
        self, **kwargs: Unpack[AcceptInboundCrossClusterSearchConnectionRequestTypeDef]
    ) -> AcceptInboundCrossClusterSearchConnectionResponseTypeDef:
        """
        Allows the destination domain owner to accept an inbound cross-cluster search
        connection request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/accept_inbound_cross_cluster_search_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#accept_inbound_cross_cluster_search_connection)
        """

    def add_tags(self, **kwargs: Unpack[AddTagsRequestTypeDef]) -> EmptyResponseMetadataTypeDef:
        """
        Attaches tags to an existing Elasticsearch domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/add_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#add_tags)
        """

    def associate_package(
        self, **kwargs: Unpack[AssociatePackageRequestTypeDef]
    ) -> AssociatePackageResponseTypeDef:
        """
        Associates a package with an Amazon ES domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/associate_package.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#associate_package)
        """

    def authorize_vpc_endpoint_access(
        self, **kwargs: Unpack[AuthorizeVpcEndpointAccessRequestTypeDef]
    ) -> AuthorizeVpcEndpointAccessResponseTypeDef:
        """
        Provides access to an Amazon OpenSearch Service domain through the use of an
        interface VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/authorize_vpc_endpoint_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#authorize_vpc_endpoint_access)
        """

    def cancel_domain_config_change(
        self, **kwargs: Unpack[CancelDomainConfigChangeRequestTypeDef]
    ) -> CancelDomainConfigChangeResponseTypeDef:
        """
        Cancels a pending configuration change on an Amazon OpenSearch Service domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/cancel_domain_config_change.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#cancel_domain_config_change)
        """

    def cancel_elasticsearch_service_software_update(
        self, **kwargs: Unpack[CancelElasticsearchServiceSoftwareUpdateRequestTypeDef]
    ) -> CancelElasticsearchServiceSoftwareUpdateResponseTypeDef:
        """
        Cancels a scheduled service software update for an Amazon ES domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/cancel_elasticsearch_service_software_update.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#cancel_elasticsearch_service_software_update)
        """

    def create_elasticsearch_domain(
        self, **kwargs: Unpack[CreateElasticsearchDomainRequestTypeDef]
    ) -> CreateElasticsearchDomainResponseTypeDef:
        """
        Creates a new Elasticsearch domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/create_elasticsearch_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#create_elasticsearch_domain)
        """

    def create_outbound_cross_cluster_search_connection(
        self, **kwargs: Unpack[CreateOutboundCrossClusterSearchConnectionRequestTypeDef]
    ) -> CreateOutboundCrossClusterSearchConnectionResponseTypeDef:
        """
        Creates a new cross-cluster search connection from a source domain to a
        destination domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/create_outbound_cross_cluster_search_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#create_outbound_cross_cluster_search_connection)
        """

    def create_package(
        self, **kwargs: Unpack[CreatePackageRequestTypeDef]
    ) -> CreatePackageResponseTypeDef:
        """
        Create a package for use with Amazon ES domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/create_package.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#create_package)
        """

    def create_vpc_endpoint(
        self, **kwargs: Unpack[CreateVpcEndpointRequestTypeDef]
    ) -> CreateVpcEndpointResponseTypeDef:
        """
        Creates an Amazon OpenSearch Service-managed VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/create_vpc_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#create_vpc_endpoint)
        """

    def delete_elasticsearch_domain(
        self, **kwargs: Unpack[DeleteElasticsearchDomainRequestTypeDef]
    ) -> DeleteElasticsearchDomainResponseTypeDef:
        """
        Permanently deletes the specified Elasticsearch domain and all of its data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/delete_elasticsearch_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#delete_elasticsearch_domain)
        """

    def delete_elasticsearch_service_role(self) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the service-linked role that Elasticsearch Service uses to manage and
        maintain VPC domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/delete_elasticsearch_service_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#delete_elasticsearch_service_role)
        """

    def delete_inbound_cross_cluster_search_connection(
        self, **kwargs: Unpack[DeleteInboundCrossClusterSearchConnectionRequestTypeDef]
    ) -> DeleteInboundCrossClusterSearchConnectionResponseTypeDef:
        """
        Allows the destination domain owner to delete an existing inbound cross-cluster
        search connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/delete_inbound_cross_cluster_search_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#delete_inbound_cross_cluster_search_connection)
        """

    def delete_outbound_cross_cluster_search_connection(
        self, **kwargs: Unpack[DeleteOutboundCrossClusterSearchConnectionRequestTypeDef]
    ) -> DeleteOutboundCrossClusterSearchConnectionResponseTypeDef:
        """
        Allows the source domain owner to delete an existing outbound cross-cluster
        search connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/delete_outbound_cross_cluster_search_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#delete_outbound_cross_cluster_search_connection)
        """

    def delete_package(
        self, **kwargs: Unpack[DeletePackageRequestTypeDef]
    ) -> DeletePackageResponseTypeDef:
        """
        Delete the package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/delete_package.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#delete_package)
        """

    def delete_vpc_endpoint(
        self, **kwargs: Unpack[DeleteVpcEndpointRequestTypeDef]
    ) -> DeleteVpcEndpointResponseTypeDef:
        """
        Deletes an Amazon OpenSearch Service-managed interface VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/delete_vpc_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#delete_vpc_endpoint)
        """

    def describe_domain_auto_tunes(
        self, **kwargs: Unpack[DescribeDomainAutoTunesRequestTypeDef]
    ) -> DescribeDomainAutoTunesResponseTypeDef:
        """
        Provides scheduled Auto-Tune action details for the Elasticsearch domain, such
        as Auto-Tune action type, description, severity, and scheduled date.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/describe_domain_auto_tunes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#describe_domain_auto_tunes)
        """

    def describe_domain_change_progress(
        self, **kwargs: Unpack[DescribeDomainChangeProgressRequestTypeDef]
    ) -> DescribeDomainChangeProgressResponseTypeDef:
        """
        Returns information about the current blue/green deployment happening on a
        domain, including a change ID, status, and progress stages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/describe_domain_change_progress.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#describe_domain_change_progress)
        """

    def describe_elasticsearch_domain(
        self, **kwargs: Unpack[DescribeElasticsearchDomainRequestTypeDef]
    ) -> DescribeElasticsearchDomainResponseTypeDef:
        """
        Returns domain configuration information about the specified Elasticsearch
        domain, including the domain ID, domain endpoint, and domain ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/describe_elasticsearch_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#describe_elasticsearch_domain)
        """

    def describe_elasticsearch_domain_config(
        self, **kwargs: Unpack[DescribeElasticsearchDomainConfigRequestTypeDef]
    ) -> DescribeElasticsearchDomainConfigResponseTypeDef:
        """
        Provides cluster configuration information about the specified Elasticsearch
        domain, such as the state, creation date, update version, and update date for
        cluster options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/describe_elasticsearch_domain_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#describe_elasticsearch_domain_config)
        """

    def describe_elasticsearch_domains(
        self, **kwargs: Unpack[DescribeElasticsearchDomainsRequestTypeDef]
    ) -> DescribeElasticsearchDomainsResponseTypeDef:
        """
        Returns domain configuration information about the specified Elasticsearch
        domains, including the domain ID, domain endpoint, and domain ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/describe_elasticsearch_domains.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#describe_elasticsearch_domains)
        """

    def describe_elasticsearch_instance_type_limits(
        self, **kwargs: Unpack[DescribeElasticsearchInstanceTypeLimitsRequestTypeDef]
    ) -> DescribeElasticsearchInstanceTypeLimitsResponseTypeDef:
        """
        Describe Elasticsearch Limits for a given InstanceType and ElasticsearchVersion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/describe_elasticsearch_instance_type_limits.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#describe_elasticsearch_instance_type_limits)
        """

    def describe_inbound_cross_cluster_search_connections(
        self, **kwargs: Unpack[DescribeInboundCrossClusterSearchConnectionsRequestTypeDef]
    ) -> DescribeInboundCrossClusterSearchConnectionsResponseTypeDef:
        """
        Lists all the inbound cross-cluster search connections for a destination domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/describe_inbound_cross_cluster_search_connections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#describe_inbound_cross_cluster_search_connections)
        """

    def describe_outbound_cross_cluster_search_connections(
        self, **kwargs: Unpack[DescribeOutboundCrossClusterSearchConnectionsRequestTypeDef]
    ) -> DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef:
        """
        Lists all the outbound cross-cluster search connections for a source domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/describe_outbound_cross_cluster_search_connections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#describe_outbound_cross_cluster_search_connections)
        """

    def describe_packages(
        self, **kwargs: Unpack[DescribePackagesRequestTypeDef]
    ) -> DescribePackagesResponseTypeDef:
        """
        Describes all packages available to Amazon ES.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/describe_packages.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#describe_packages)
        """

    def describe_reserved_elasticsearch_instance_offerings(
        self, **kwargs: Unpack[DescribeReservedElasticsearchInstanceOfferingsRequestTypeDef]
    ) -> DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef:
        """
        Lists available reserved Elasticsearch instance offerings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/describe_reserved_elasticsearch_instance_offerings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#describe_reserved_elasticsearch_instance_offerings)
        """

    def describe_reserved_elasticsearch_instances(
        self, **kwargs: Unpack[DescribeReservedElasticsearchInstancesRequestTypeDef]
    ) -> DescribeReservedElasticsearchInstancesResponseTypeDef:
        """
        Returns information about reserved Elasticsearch instances for this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/describe_reserved_elasticsearch_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#describe_reserved_elasticsearch_instances)
        """

    def describe_vpc_endpoints(
        self, **kwargs: Unpack[DescribeVpcEndpointsRequestTypeDef]
    ) -> DescribeVpcEndpointsResponseTypeDef:
        """
        Describes one or more Amazon OpenSearch Service-managed VPC endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/describe_vpc_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#describe_vpc_endpoints)
        """

    def dissociate_package(
        self, **kwargs: Unpack[DissociatePackageRequestTypeDef]
    ) -> DissociatePackageResponseTypeDef:
        """
        Dissociates a package from the Amazon ES domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/dissociate_package.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#dissociate_package)
        """

    def get_compatible_elasticsearch_versions(
        self, **kwargs: Unpack[GetCompatibleElasticsearchVersionsRequestTypeDef]
    ) -> GetCompatibleElasticsearchVersionsResponseTypeDef:
        """
        Returns a list of upgrade compatible Elastisearch versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/get_compatible_elasticsearch_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#get_compatible_elasticsearch_versions)
        """

    def get_package_version_history(
        self, **kwargs: Unpack[GetPackageVersionHistoryRequestTypeDef]
    ) -> GetPackageVersionHistoryResponseTypeDef:
        """
        Returns a list of versions of the package, along with their creation time and
        commit message.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/get_package_version_history.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#get_package_version_history)
        """

    def get_upgrade_history(
        self, **kwargs: Unpack[GetUpgradeHistoryRequestTypeDef]
    ) -> GetUpgradeHistoryResponseTypeDef:
        """
        Retrieves the complete history of the last 10 upgrades that were performed on
        the domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/get_upgrade_history.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#get_upgrade_history)
        """

    def get_upgrade_status(
        self, **kwargs: Unpack[GetUpgradeStatusRequestTypeDef]
    ) -> GetUpgradeStatusResponseTypeDef:
        """
        Retrieves the latest status of the last upgrade or upgrade eligibility check
        that was performed on the domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/get_upgrade_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#get_upgrade_status)
        """

    def list_domain_names(
        self, **kwargs: Unpack[ListDomainNamesRequestTypeDef]
    ) -> ListDomainNamesResponseTypeDef:
        """
        Returns the name of all Elasticsearch domains owned by the current user's
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/list_domain_names.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#list_domain_names)
        """

    def list_domains_for_package(
        self, **kwargs: Unpack[ListDomainsForPackageRequestTypeDef]
    ) -> ListDomainsForPackageResponseTypeDef:
        """
        Lists all Amazon ES domains associated with the package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/list_domains_for_package.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#list_domains_for_package)
        """

    def list_elasticsearch_instance_types(
        self, **kwargs: Unpack[ListElasticsearchInstanceTypesRequestTypeDef]
    ) -> ListElasticsearchInstanceTypesResponseTypeDef:
        """
        List all Elasticsearch instance types that are supported for given
        ElasticsearchVersion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/list_elasticsearch_instance_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#list_elasticsearch_instance_types)
        """

    def list_elasticsearch_versions(
        self, **kwargs: Unpack[ListElasticsearchVersionsRequestTypeDef]
    ) -> ListElasticsearchVersionsResponseTypeDef:
        """
        List all supported Elasticsearch versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/list_elasticsearch_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#list_elasticsearch_versions)
        """

    def list_packages_for_domain(
        self, **kwargs: Unpack[ListPackagesForDomainRequestTypeDef]
    ) -> ListPackagesForDomainResponseTypeDef:
        """
        Lists all packages associated with the Amazon ES domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/list_packages_for_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#list_packages_for_domain)
        """

    def list_tags(self, **kwargs: Unpack[ListTagsRequestTypeDef]) -> ListTagsResponseTypeDef:
        """
        Returns all tags for the given Elasticsearch domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/list_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#list_tags)
        """

    def list_vpc_endpoint_access(
        self, **kwargs: Unpack[ListVpcEndpointAccessRequestTypeDef]
    ) -> ListVpcEndpointAccessResponseTypeDef:
        """
        Retrieves information about each principal that is allowed to access a given
        Amazon OpenSearch Service domain through the use of an interface VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/list_vpc_endpoint_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#list_vpc_endpoint_access)
        """

    def list_vpc_endpoints(
        self, **kwargs: Unpack[ListVpcEndpointsRequestTypeDef]
    ) -> ListVpcEndpointsResponseTypeDef:
        """
        Retrieves all Amazon OpenSearch Service-managed VPC endpoints in the current
        account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/list_vpc_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#list_vpc_endpoints)
        """

    def list_vpc_endpoints_for_domain(
        self, **kwargs: Unpack[ListVpcEndpointsForDomainRequestTypeDef]
    ) -> ListVpcEndpointsForDomainResponseTypeDef:
        """
        Retrieves all Amazon OpenSearch Service-managed VPC endpoints associated with a
        particular domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/list_vpc_endpoints_for_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#list_vpc_endpoints_for_domain)
        """

    def purchase_reserved_elasticsearch_instance_offering(
        self, **kwargs: Unpack[PurchaseReservedElasticsearchInstanceOfferingRequestTypeDef]
    ) -> PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef:
        """
        Allows you to purchase reserved Elasticsearch instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/purchase_reserved_elasticsearch_instance_offering.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#purchase_reserved_elasticsearch_instance_offering)
        """

    def reject_inbound_cross_cluster_search_connection(
        self, **kwargs: Unpack[RejectInboundCrossClusterSearchConnectionRequestTypeDef]
    ) -> RejectInboundCrossClusterSearchConnectionResponseTypeDef:
        """
        Allows the destination domain owner to reject an inbound cross-cluster search
        connection request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/reject_inbound_cross_cluster_search_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#reject_inbound_cross_cluster_search_connection)
        """

    def remove_tags(
        self, **kwargs: Unpack[RemoveTagsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified set of tags from the specified Elasticsearch domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/remove_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#remove_tags)
        """

    def revoke_vpc_endpoint_access(
        self, **kwargs: Unpack[RevokeVpcEndpointAccessRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Revokes access to an Amazon OpenSearch Service domain that was provided through
        an interface VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/revoke_vpc_endpoint_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#revoke_vpc_endpoint_access)
        """

    def start_elasticsearch_service_software_update(
        self, **kwargs: Unpack[StartElasticsearchServiceSoftwareUpdateRequestTypeDef]
    ) -> StartElasticsearchServiceSoftwareUpdateResponseTypeDef:
        """
        Schedules a service software update for an Amazon ES domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/start_elasticsearch_service_software_update.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#start_elasticsearch_service_software_update)
        """

    def update_elasticsearch_domain_config(
        self, **kwargs: Unpack[UpdateElasticsearchDomainConfigRequestTypeDef]
    ) -> UpdateElasticsearchDomainConfigResponseTypeDef:
        """
        Modifies the cluster configuration of the specified Elasticsearch domain,
        setting as setting the instance type and the number of instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/update_elasticsearch_domain_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#update_elasticsearch_domain_config)
        """

    def update_package(
        self, **kwargs: Unpack[UpdatePackageRequestTypeDef]
    ) -> UpdatePackageResponseTypeDef:
        """
        Updates a package for use with Amazon ES domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/update_package.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#update_package)
        """

    def update_vpc_endpoint(
        self, **kwargs: Unpack[UpdateVpcEndpointRequestTypeDef]
    ) -> UpdateVpcEndpointResponseTypeDef:
        """
        Modifies an Amazon OpenSearch Service-managed interface VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/update_vpc_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#update_vpc_endpoint)
        """

    def upgrade_elasticsearch_domain(
        self, **kwargs: Unpack[UpgradeElasticsearchDomainRequestTypeDef]
    ) -> UpgradeElasticsearchDomainResponseTypeDef:
        """
        Allows you to either upgrade your domain or perform an Upgrade eligibility
        check to a compatible Elasticsearch version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/upgrade_elasticsearch_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#upgrade_elasticsearch_domain)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_reserved_elasticsearch_instance_offerings"]
    ) -> DescribeReservedElasticsearchInstanceOfferingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_reserved_elasticsearch_instances"]
    ) -> DescribeReservedElasticsearchInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_upgrade_history"]
    ) -> GetUpgradeHistoryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_elasticsearch_instance_types"]
    ) -> ListElasticsearchInstanceTypesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_elasticsearch_versions"]
    ) -> ListElasticsearchVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/client/#get_paginator)
        """
