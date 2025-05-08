"""
Type annotations for redshift service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_redshift.client import RedshiftClient
    from mypy_boto3_redshift.paginator import (
        DescribeClusterDbRevisionsPaginator,
        DescribeClusterParameterGroupsPaginator,
        DescribeClusterParametersPaginator,
        DescribeClusterSecurityGroupsPaginator,
        DescribeClusterSnapshotsPaginator,
        DescribeClusterSubnetGroupsPaginator,
        DescribeClusterTracksPaginator,
        DescribeClusterVersionsPaginator,
        DescribeClustersPaginator,
        DescribeCustomDomainAssociationsPaginator,
        DescribeDataSharesForConsumerPaginator,
        DescribeDataSharesForProducerPaginator,
        DescribeDataSharesPaginator,
        DescribeDefaultClusterParametersPaginator,
        DescribeEndpointAccessPaginator,
        DescribeEndpointAuthorizationPaginator,
        DescribeEventSubscriptionsPaginator,
        DescribeEventsPaginator,
        DescribeHsmClientCertificatesPaginator,
        DescribeHsmConfigurationsPaginator,
        DescribeInboundIntegrationsPaginator,
        DescribeIntegrationsPaginator,
        DescribeNodeConfigurationOptionsPaginator,
        DescribeOrderableClusterOptionsPaginator,
        DescribeRedshiftIdcApplicationsPaginator,
        DescribeReservedNodeExchangeStatusPaginator,
        DescribeReservedNodeOfferingsPaginator,
        DescribeReservedNodesPaginator,
        DescribeScheduledActionsPaginator,
        DescribeSnapshotCopyGrantsPaginator,
        DescribeSnapshotSchedulesPaginator,
        DescribeTableRestoreStatusPaginator,
        DescribeTagsPaginator,
        DescribeUsageLimitsPaginator,
        GetReservedNodeExchangeConfigurationOptionsPaginator,
        GetReservedNodeExchangeOfferingsPaginator,
        ListRecommendationsPaginator,
    )

    session = Session()
    client: RedshiftClient = session.client("redshift")

    describe_cluster_db_revisions_paginator: DescribeClusterDbRevisionsPaginator = client.get_paginator("describe_cluster_db_revisions")
    describe_cluster_parameter_groups_paginator: DescribeClusterParameterGroupsPaginator = client.get_paginator("describe_cluster_parameter_groups")
    describe_cluster_parameters_paginator: DescribeClusterParametersPaginator = client.get_paginator("describe_cluster_parameters")
    describe_cluster_security_groups_paginator: DescribeClusterSecurityGroupsPaginator = client.get_paginator("describe_cluster_security_groups")
    describe_cluster_snapshots_paginator: DescribeClusterSnapshotsPaginator = client.get_paginator("describe_cluster_snapshots")
    describe_cluster_subnet_groups_paginator: DescribeClusterSubnetGroupsPaginator = client.get_paginator("describe_cluster_subnet_groups")
    describe_cluster_tracks_paginator: DescribeClusterTracksPaginator = client.get_paginator("describe_cluster_tracks")
    describe_cluster_versions_paginator: DescribeClusterVersionsPaginator = client.get_paginator("describe_cluster_versions")
    describe_clusters_paginator: DescribeClustersPaginator = client.get_paginator("describe_clusters")
    describe_custom_domain_associations_paginator: DescribeCustomDomainAssociationsPaginator = client.get_paginator("describe_custom_domain_associations")
    describe_data_shares_for_consumer_paginator: DescribeDataSharesForConsumerPaginator = client.get_paginator("describe_data_shares_for_consumer")
    describe_data_shares_for_producer_paginator: DescribeDataSharesForProducerPaginator = client.get_paginator("describe_data_shares_for_producer")
    describe_data_shares_paginator: DescribeDataSharesPaginator = client.get_paginator("describe_data_shares")
    describe_default_cluster_parameters_paginator: DescribeDefaultClusterParametersPaginator = client.get_paginator("describe_default_cluster_parameters")
    describe_endpoint_access_paginator: DescribeEndpointAccessPaginator = client.get_paginator("describe_endpoint_access")
    describe_endpoint_authorization_paginator: DescribeEndpointAuthorizationPaginator = client.get_paginator("describe_endpoint_authorization")
    describe_event_subscriptions_paginator: DescribeEventSubscriptionsPaginator = client.get_paginator("describe_event_subscriptions")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_hsm_client_certificates_paginator: DescribeHsmClientCertificatesPaginator = client.get_paginator("describe_hsm_client_certificates")
    describe_hsm_configurations_paginator: DescribeHsmConfigurationsPaginator = client.get_paginator("describe_hsm_configurations")
    describe_inbound_integrations_paginator: DescribeInboundIntegrationsPaginator = client.get_paginator("describe_inbound_integrations")
    describe_integrations_paginator: DescribeIntegrationsPaginator = client.get_paginator("describe_integrations")
    describe_node_configuration_options_paginator: DescribeNodeConfigurationOptionsPaginator = client.get_paginator("describe_node_configuration_options")
    describe_orderable_cluster_options_paginator: DescribeOrderableClusterOptionsPaginator = client.get_paginator("describe_orderable_cluster_options")
    describe_redshift_idc_applications_paginator: DescribeRedshiftIdcApplicationsPaginator = client.get_paginator("describe_redshift_idc_applications")
    describe_reserved_node_exchange_status_paginator: DescribeReservedNodeExchangeStatusPaginator = client.get_paginator("describe_reserved_node_exchange_status")
    describe_reserved_node_offerings_paginator: DescribeReservedNodeOfferingsPaginator = client.get_paginator("describe_reserved_node_offerings")
    describe_reserved_nodes_paginator: DescribeReservedNodesPaginator = client.get_paginator("describe_reserved_nodes")
    describe_scheduled_actions_paginator: DescribeScheduledActionsPaginator = client.get_paginator("describe_scheduled_actions")
    describe_snapshot_copy_grants_paginator: DescribeSnapshotCopyGrantsPaginator = client.get_paginator("describe_snapshot_copy_grants")
    describe_snapshot_schedules_paginator: DescribeSnapshotSchedulesPaginator = client.get_paginator("describe_snapshot_schedules")
    describe_table_restore_status_paginator: DescribeTableRestoreStatusPaginator = client.get_paginator("describe_table_restore_status")
    describe_tags_paginator: DescribeTagsPaginator = client.get_paginator("describe_tags")
    describe_usage_limits_paginator: DescribeUsageLimitsPaginator = client.get_paginator("describe_usage_limits")
    get_reserved_node_exchange_configuration_options_paginator: GetReservedNodeExchangeConfigurationOptionsPaginator = client.get_paginator("get_reserved_node_exchange_configuration_options")
    get_reserved_node_exchange_offerings_paginator: GetReservedNodeExchangeOfferingsPaginator = client.get_paginator("get_reserved_node_exchange_offerings")
    list_recommendations_paginator: ListRecommendationsPaginator = client.get_paginator("list_recommendations")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ClusterDbRevisionsMessageTypeDef,
    ClusterParameterGroupDetailsTypeDef,
    ClusterParameterGroupsMessageTypeDef,
    ClusterSecurityGroupMessageTypeDef,
    ClustersMessageTypeDef,
    ClusterSubnetGroupMessageTypeDef,
    ClusterVersionsMessageTypeDef,
    CustomDomainAssociationsMessageTypeDef,
    DescribeClusterDbRevisionsMessagePaginateTypeDef,
    DescribeClusterParameterGroupsMessagePaginateTypeDef,
    DescribeClusterParametersMessagePaginateTypeDef,
    DescribeClusterSecurityGroupsMessagePaginateTypeDef,
    DescribeClustersMessagePaginateTypeDef,
    DescribeClusterSnapshotsMessagePaginateTypeDef,
    DescribeClusterSubnetGroupsMessagePaginateTypeDef,
    DescribeClusterTracksMessagePaginateTypeDef,
    DescribeClusterVersionsMessagePaginateTypeDef,
    DescribeCustomDomainAssociationsMessagePaginateTypeDef,
    DescribeDataSharesForConsumerMessagePaginateTypeDef,
    DescribeDataSharesForConsumerResultTypeDef,
    DescribeDataSharesForProducerMessagePaginateTypeDef,
    DescribeDataSharesForProducerResultTypeDef,
    DescribeDataSharesMessagePaginateTypeDef,
    DescribeDataSharesResultTypeDef,
    DescribeDefaultClusterParametersMessagePaginateTypeDef,
    DescribeDefaultClusterParametersResultTypeDef,
    DescribeEndpointAccessMessagePaginateTypeDef,
    DescribeEndpointAuthorizationMessagePaginateTypeDef,
    DescribeEventsMessagePaginateTypeDef,
    DescribeEventSubscriptionsMessagePaginateTypeDef,
    DescribeHsmClientCertificatesMessagePaginateTypeDef,
    DescribeHsmConfigurationsMessagePaginateTypeDef,
    DescribeInboundIntegrationsMessagePaginateTypeDef,
    DescribeIntegrationsMessagePaginateTypeDef,
    DescribeNodeConfigurationOptionsMessagePaginateTypeDef,
    DescribeOrderableClusterOptionsMessagePaginateTypeDef,
    DescribeRedshiftIdcApplicationsMessagePaginateTypeDef,
    DescribeRedshiftIdcApplicationsResultTypeDef,
    DescribeReservedNodeExchangeStatusInputMessagePaginateTypeDef,
    DescribeReservedNodeExchangeStatusOutputMessageTypeDef,
    DescribeReservedNodeOfferingsMessagePaginateTypeDef,
    DescribeReservedNodesMessagePaginateTypeDef,
    DescribeScheduledActionsMessagePaginateTypeDef,
    DescribeSnapshotCopyGrantsMessagePaginateTypeDef,
    DescribeSnapshotSchedulesMessagePaginateTypeDef,
    DescribeSnapshotSchedulesOutputMessageTypeDef,
    DescribeTableRestoreStatusMessagePaginateTypeDef,
    DescribeTagsMessagePaginateTypeDef,
    DescribeUsageLimitsMessagePaginateTypeDef,
    EndpointAccessListTypeDef,
    EndpointAuthorizationListTypeDef,
    EventsMessageTypeDef,
    EventSubscriptionsMessageTypeDef,
    GetReservedNodeExchangeConfigurationOptionsInputMessagePaginateTypeDef,
    GetReservedNodeExchangeConfigurationOptionsOutputMessageTypeDef,
    GetReservedNodeExchangeOfferingsInputMessagePaginateTypeDef,
    GetReservedNodeExchangeOfferingsOutputMessageTypeDef,
    HsmClientCertificateMessageTypeDef,
    HsmConfigurationMessageTypeDef,
    InboundIntegrationsMessageTypeDef,
    IntegrationsMessageTypeDef,
    ListRecommendationsMessagePaginateTypeDef,
    ListRecommendationsResultTypeDef,
    NodeConfigurationOptionsMessageTypeDef,
    OrderableClusterOptionsMessageTypeDef,
    ReservedNodeOfferingsMessageTypeDef,
    ReservedNodesMessageTypeDef,
    ScheduledActionsMessageTypeDef,
    SnapshotCopyGrantMessageTypeDef,
    SnapshotMessageTypeDef,
    TableRestoreStatusMessageTypeDef,
    TaggedResourceListMessageTypeDef,
    TrackListMessageTypeDef,
    UsageLimitListTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeClusterDbRevisionsPaginator",
    "DescribeClusterParameterGroupsPaginator",
    "DescribeClusterParametersPaginator",
    "DescribeClusterSecurityGroupsPaginator",
    "DescribeClusterSnapshotsPaginator",
    "DescribeClusterSubnetGroupsPaginator",
    "DescribeClusterTracksPaginator",
    "DescribeClusterVersionsPaginator",
    "DescribeClustersPaginator",
    "DescribeCustomDomainAssociationsPaginator",
    "DescribeDataSharesForConsumerPaginator",
    "DescribeDataSharesForProducerPaginator",
    "DescribeDataSharesPaginator",
    "DescribeDefaultClusterParametersPaginator",
    "DescribeEndpointAccessPaginator",
    "DescribeEndpointAuthorizationPaginator",
    "DescribeEventSubscriptionsPaginator",
    "DescribeEventsPaginator",
    "DescribeHsmClientCertificatesPaginator",
    "DescribeHsmConfigurationsPaginator",
    "DescribeInboundIntegrationsPaginator",
    "DescribeIntegrationsPaginator",
    "DescribeNodeConfigurationOptionsPaginator",
    "DescribeOrderableClusterOptionsPaginator",
    "DescribeRedshiftIdcApplicationsPaginator",
    "DescribeReservedNodeExchangeStatusPaginator",
    "DescribeReservedNodeOfferingsPaginator",
    "DescribeReservedNodesPaginator",
    "DescribeScheduledActionsPaginator",
    "DescribeSnapshotCopyGrantsPaginator",
    "DescribeSnapshotSchedulesPaginator",
    "DescribeTableRestoreStatusPaginator",
    "DescribeTagsPaginator",
    "DescribeUsageLimitsPaginator",
    "GetReservedNodeExchangeConfigurationOptionsPaginator",
    "GetReservedNodeExchangeOfferingsPaginator",
    "ListRecommendationsPaginator",
)

if TYPE_CHECKING:
    _DescribeClusterDbRevisionsPaginatorBase = Paginator[ClusterDbRevisionsMessageTypeDef]
else:
    _DescribeClusterDbRevisionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeClusterDbRevisionsPaginator(_DescribeClusterDbRevisionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeClusterDbRevisions.html#Redshift.Paginator.DescribeClusterDbRevisions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeclusterdbrevisionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClusterDbRevisionsMessagePaginateTypeDef]
    ) -> PageIterator[ClusterDbRevisionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeClusterDbRevisions.html#Redshift.Paginator.DescribeClusterDbRevisions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeclusterdbrevisionspaginator)
        """

if TYPE_CHECKING:
    _DescribeClusterParameterGroupsPaginatorBase = Paginator[ClusterParameterGroupsMessageTypeDef]
else:
    _DescribeClusterParameterGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeClusterParameterGroupsPaginator(_DescribeClusterParameterGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeClusterParameterGroups.html#Redshift.Paginator.DescribeClusterParameterGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeclusterparametergroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClusterParameterGroupsMessagePaginateTypeDef]
    ) -> PageIterator[ClusterParameterGroupsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeClusterParameterGroups.html#Redshift.Paginator.DescribeClusterParameterGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeclusterparametergroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeClusterParametersPaginatorBase = Paginator[ClusterParameterGroupDetailsTypeDef]
else:
    _DescribeClusterParametersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeClusterParametersPaginator(_DescribeClusterParametersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeClusterParameters.html#Redshift.Paginator.DescribeClusterParameters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeclusterparameterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClusterParametersMessagePaginateTypeDef]
    ) -> PageIterator[ClusterParameterGroupDetailsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeClusterParameters.html#Redshift.Paginator.DescribeClusterParameters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeclusterparameterspaginator)
        """

if TYPE_CHECKING:
    _DescribeClusterSecurityGroupsPaginatorBase = Paginator[ClusterSecurityGroupMessageTypeDef]
else:
    _DescribeClusterSecurityGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeClusterSecurityGroupsPaginator(_DescribeClusterSecurityGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeClusterSecurityGroups.html#Redshift.Paginator.DescribeClusterSecurityGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeclustersecuritygroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClusterSecurityGroupsMessagePaginateTypeDef]
    ) -> PageIterator[ClusterSecurityGroupMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeClusterSecurityGroups.html#Redshift.Paginator.DescribeClusterSecurityGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeclustersecuritygroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeClusterSnapshotsPaginatorBase = Paginator[SnapshotMessageTypeDef]
else:
    _DescribeClusterSnapshotsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeClusterSnapshotsPaginator(_DescribeClusterSnapshotsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeClusterSnapshots.html#Redshift.Paginator.DescribeClusterSnapshots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeclustersnapshotspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClusterSnapshotsMessagePaginateTypeDef]
    ) -> PageIterator[SnapshotMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeClusterSnapshots.html#Redshift.Paginator.DescribeClusterSnapshots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeclustersnapshotspaginator)
        """

if TYPE_CHECKING:
    _DescribeClusterSubnetGroupsPaginatorBase = Paginator[ClusterSubnetGroupMessageTypeDef]
else:
    _DescribeClusterSubnetGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeClusterSubnetGroupsPaginator(_DescribeClusterSubnetGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeClusterSubnetGroups.html#Redshift.Paginator.DescribeClusterSubnetGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeclustersubnetgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClusterSubnetGroupsMessagePaginateTypeDef]
    ) -> PageIterator[ClusterSubnetGroupMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeClusterSubnetGroups.html#Redshift.Paginator.DescribeClusterSubnetGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeclustersubnetgroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeClusterTracksPaginatorBase = Paginator[TrackListMessageTypeDef]
else:
    _DescribeClusterTracksPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeClusterTracksPaginator(_DescribeClusterTracksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeClusterTracks.html#Redshift.Paginator.DescribeClusterTracks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeclustertrackspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClusterTracksMessagePaginateTypeDef]
    ) -> PageIterator[TrackListMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeClusterTracks.html#Redshift.Paginator.DescribeClusterTracks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeclustertrackspaginator)
        """

if TYPE_CHECKING:
    _DescribeClusterVersionsPaginatorBase = Paginator[ClusterVersionsMessageTypeDef]
else:
    _DescribeClusterVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeClusterVersionsPaginator(_DescribeClusterVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeClusterVersions.html#Redshift.Paginator.DescribeClusterVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeclusterversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClusterVersionsMessagePaginateTypeDef]
    ) -> PageIterator[ClusterVersionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeClusterVersions.html#Redshift.Paginator.DescribeClusterVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeclusterversionspaginator)
        """

if TYPE_CHECKING:
    _DescribeClustersPaginatorBase = Paginator[ClustersMessageTypeDef]
else:
    _DescribeClustersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeClustersPaginator(_DescribeClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeClusters.html#Redshift.Paginator.DescribeClusters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeclusterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClustersMessagePaginateTypeDef]
    ) -> PageIterator[ClustersMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeClusters.html#Redshift.Paginator.DescribeClusters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeclusterspaginator)
        """

if TYPE_CHECKING:
    _DescribeCustomDomainAssociationsPaginatorBase = Paginator[
        CustomDomainAssociationsMessageTypeDef
    ]
else:
    _DescribeCustomDomainAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeCustomDomainAssociationsPaginator(_DescribeCustomDomainAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeCustomDomainAssociations.html#Redshift.Paginator.DescribeCustomDomainAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describecustomdomainassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCustomDomainAssociationsMessagePaginateTypeDef]
    ) -> PageIterator[CustomDomainAssociationsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeCustomDomainAssociations.html#Redshift.Paginator.DescribeCustomDomainAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describecustomdomainassociationspaginator)
        """

if TYPE_CHECKING:
    _DescribeDataSharesForConsumerPaginatorBase = Paginator[
        DescribeDataSharesForConsumerResultTypeDef
    ]
else:
    _DescribeDataSharesForConsumerPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDataSharesForConsumerPaginator(_DescribeDataSharesForConsumerPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeDataSharesForConsumer.html#Redshift.Paginator.DescribeDataSharesForConsumer)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describedatasharesforconsumerpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDataSharesForConsumerMessagePaginateTypeDef]
    ) -> PageIterator[DescribeDataSharesForConsumerResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeDataSharesForConsumer.html#Redshift.Paginator.DescribeDataSharesForConsumer.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describedatasharesforconsumerpaginator)
        """

if TYPE_CHECKING:
    _DescribeDataSharesForProducerPaginatorBase = Paginator[
        DescribeDataSharesForProducerResultTypeDef
    ]
else:
    _DescribeDataSharesForProducerPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDataSharesForProducerPaginator(_DescribeDataSharesForProducerPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeDataSharesForProducer.html#Redshift.Paginator.DescribeDataSharesForProducer)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describedatasharesforproducerpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDataSharesForProducerMessagePaginateTypeDef]
    ) -> PageIterator[DescribeDataSharesForProducerResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeDataSharesForProducer.html#Redshift.Paginator.DescribeDataSharesForProducer.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describedatasharesforproducerpaginator)
        """

if TYPE_CHECKING:
    _DescribeDataSharesPaginatorBase = Paginator[DescribeDataSharesResultTypeDef]
else:
    _DescribeDataSharesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDataSharesPaginator(_DescribeDataSharesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeDataShares.html#Redshift.Paginator.DescribeDataShares)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describedatasharespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDataSharesMessagePaginateTypeDef]
    ) -> PageIterator[DescribeDataSharesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeDataShares.html#Redshift.Paginator.DescribeDataShares.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describedatasharespaginator)
        """

if TYPE_CHECKING:
    _DescribeDefaultClusterParametersPaginatorBase = Paginator[
        DescribeDefaultClusterParametersResultTypeDef
    ]
else:
    _DescribeDefaultClusterParametersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDefaultClusterParametersPaginator(_DescribeDefaultClusterParametersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeDefaultClusterParameters.html#Redshift.Paginator.DescribeDefaultClusterParameters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describedefaultclusterparameterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDefaultClusterParametersMessagePaginateTypeDef]
    ) -> PageIterator[DescribeDefaultClusterParametersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeDefaultClusterParameters.html#Redshift.Paginator.DescribeDefaultClusterParameters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describedefaultclusterparameterspaginator)
        """

if TYPE_CHECKING:
    _DescribeEndpointAccessPaginatorBase = Paginator[EndpointAccessListTypeDef]
else:
    _DescribeEndpointAccessPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEndpointAccessPaginator(_DescribeEndpointAccessPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeEndpointAccess.html#Redshift.Paginator.DescribeEndpointAccess)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeendpointaccesspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEndpointAccessMessagePaginateTypeDef]
    ) -> PageIterator[EndpointAccessListTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeEndpointAccess.html#Redshift.Paginator.DescribeEndpointAccess.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeendpointaccesspaginator)
        """

if TYPE_CHECKING:
    _DescribeEndpointAuthorizationPaginatorBase = Paginator[EndpointAuthorizationListTypeDef]
else:
    _DescribeEndpointAuthorizationPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEndpointAuthorizationPaginator(_DescribeEndpointAuthorizationPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeEndpointAuthorization.html#Redshift.Paginator.DescribeEndpointAuthorization)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeendpointauthorizationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEndpointAuthorizationMessagePaginateTypeDef]
    ) -> PageIterator[EndpointAuthorizationListTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeEndpointAuthorization.html#Redshift.Paginator.DescribeEndpointAuthorization.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeendpointauthorizationpaginator)
        """

if TYPE_CHECKING:
    _DescribeEventSubscriptionsPaginatorBase = Paginator[EventSubscriptionsMessageTypeDef]
else:
    _DescribeEventSubscriptionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEventSubscriptionsPaginator(_DescribeEventSubscriptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeEventSubscriptions.html#Redshift.Paginator.DescribeEventSubscriptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeeventsubscriptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEventSubscriptionsMessagePaginateTypeDef]
    ) -> PageIterator[EventSubscriptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeEventSubscriptions.html#Redshift.Paginator.DescribeEventSubscriptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeeventsubscriptionspaginator)
        """

if TYPE_CHECKING:
    _DescribeEventsPaginatorBase = Paginator[EventsMessageTypeDef]
else:
    _DescribeEventsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEventsPaginator(_DescribeEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeEvents.html#Redshift.Paginator.DescribeEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEventsMessagePaginateTypeDef]
    ) -> PageIterator[EventsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeEvents.html#Redshift.Paginator.DescribeEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeeventspaginator)
        """

if TYPE_CHECKING:
    _DescribeHsmClientCertificatesPaginatorBase = Paginator[HsmClientCertificateMessageTypeDef]
else:
    _DescribeHsmClientCertificatesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeHsmClientCertificatesPaginator(_DescribeHsmClientCertificatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeHsmClientCertificates.html#Redshift.Paginator.DescribeHsmClientCertificates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describehsmclientcertificatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeHsmClientCertificatesMessagePaginateTypeDef]
    ) -> PageIterator[HsmClientCertificateMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeHsmClientCertificates.html#Redshift.Paginator.DescribeHsmClientCertificates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describehsmclientcertificatespaginator)
        """

if TYPE_CHECKING:
    _DescribeHsmConfigurationsPaginatorBase = Paginator[HsmConfigurationMessageTypeDef]
else:
    _DescribeHsmConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeHsmConfigurationsPaginator(_DescribeHsmConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeHsmConfigurations.html#Redshift.Paginator.DescribeHsmConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describehsmconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeHsmConfigurationsMessagePaginateTypeDef]
    ) -> PageIterator[HsmConfigurationMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeHsmConfigurations.html#Redshift.Paginator.DescribeHsmConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describehsmconfigurationspaginator)
        """

if TYPE_CHECKING:
    _DescribeInboundIntegrationsPaginatorBase = Paginator[InboundIntegrationsMessageTypeDef]
else:
    _DescribeInboundIntegrationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeInboundIntegrationsPaginator(_DescribeInboundIntegrationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeInboundIntegrations.html#Redshift.Paginator.DescribeInboundIntegrations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeinboundintegrationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInboundIntegrationsMessagePaginateTypeDef]
    ) -> PageIterator[InboundIntegrationsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeInboundIntegrations.html#Redshift.Paginator.DescribeInboundIntegrations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeinboundintegrationspaginator)
        """

if TYPE_CHECKING:
    _DescribeIntegrationsPaginatorBase = Paginator[IntegrationsMessageTypeDef]
else:
    _DescribeIntegrationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeIntegrationsPaginator(_DescribeIntegrationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeIntegrations.html#Redshift.Paginator.DescribeIntegrations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeintegrationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeIntegrationsMessagePaginateTypeDef]
    ) -> PageIterator[IntegrationsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeIntegrations.html#Redshift.Paginator.DescribeIntegrations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeintegrationspaginator)
        """

if TYPE_CHECKING:
    _DescribeNodeConfigurationOptionsPaginatorBase = Paginator[
        NodeConfigurationOptionsMessageTypeDef
    ]
else:
    _DescribeNodeConfigurationOptionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeNodeConfigurationOptionsPaginator(_DescribeNodeConfigurationOptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeNodeConfigurationOptions.html#Redshift.Paginator.DescribeNodeConfigurationOptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describenodeconfigurationoptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeNodeConfigurationOptionsMessagePaginateTypeDef]
    ) -> PageIterator[NodeConfigurationOptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeNodeConfigurationOptions.html#Redshift.Paginator.DescribeNodeConfigurationOptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describenodeconfigurationoptionspaginator)
        """

if TYPE_CHECKING:
    _DescribeOrderableClusterOptionsPaginatorBase = Paginator[OrderableClusterOptionsMessageTypeDef]
else:
    _DescribeOrderableClusterOptionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeOrderableClusterOptionsPaginator(_DescribeOrderableClusterOptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeOrderableClusterOptions.html#Redshift.Paginator.DescribeOrderableClusterOptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeorderableclusteroptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeOrderableClusterOptionsMessagePaginateTypeDef]
    ) -> PageIterator[OrderableClusterOptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeOrderableClusterOptions.html#Redshift.Paginator.DescribeOrderableClusterOptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeorderableclusteroptionspaginator)
        """

if TYPE_CHECKING:
    _DescribeRedshiftIdcApplicationsPaginatorBase = Paginator[
        DescribeRedshiftIdcApplicationsResultTypeDef
    ]
else:
    _DescribeRedshiftIdcApplicationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeRedshiftIdcApplicationsPaginator(_DescribeRedshiftIdcApplicationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeRedshiftIdcApplications.html#Redshift.Paginator.DescribeRedshiftIdcApplications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeredshiftidcapplicationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeRedshiftIdcApplicationsMessagePaginateTypeDef]
    ) -> PageIterator[DescribeRedshiftIdcApplicationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeRedshiftIdcApplications.html#Redshift.Paginator.DescribeRedshiftIdcApplications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeredshiftidcapplicationspaginator)
        """

if TYPE_CHECKING:
    _DescribeReservedNodeExchangeStatusPaginatorBase = Paginator[
        DescribeReservedNodeExchangeStatusOutputMessageTypeDef
    ]
else:
    _DescribeReservedNodeExchangeStatusPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeReservedNodeExchangeStatusPaginator(_DescribeReservedNodeExchangeStatusPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeReservedNodeExchangeStatus.html#Redshift.Paginator.DescribeReservedNodeExchangeStatus)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describereservednodeexchangestatuspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReservedNodeExchangeStatusInputMessagePaginateTypeDef]
    ) -> PageIterator[DescribeReservedNodeExchangeStatusOutputMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeReservedNodeExchangeStatus.html#Redshift.Paginator.DescribeReservedNodeExchangeStatus.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describereservednodeexchangestatuspaginator)
        """

if TYPE_CHECKING:
    _DescribeReservedNodeOfferingsPaginatorBase = Paginator[ReservedNodeOfferingsMessageTypeDef]
else:
    _DescribeReservedNodeOfferingsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeReservedNodeOfferingsPaginator(_DescribeReservedNodeOfferingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeReservedNodeOfferings.html#Redshift.Paginator.DescribeReservedNodeOfferings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describereservednodeofferingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReservedNodeOfferingsMessagePaginateTypeDef]
    ) -> PageIterator[ReservedNodeOfferingsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeReservedNodeOfferings.html#Redshift.Paginator.DescribeReservedNodeOfferings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describereservednodeofferingspaginator)
        """

if TYPE_CHECKING:
    _DescribeReservedNodesPaginatorBase = Paginator[ReservedNodesMessageTypeDef]
else:
    _DescribeReservedNodesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeReservedNodesPaginator(_DescribeReservedNodesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeReservedNodes.html#Redshift.Paginator.DescribeReservedNodes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describereservednodespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReservedNodesMessagePaginateTypeDef]
    ) -> PageIterator[ReservedNodesMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeReservedNodes.html#Redshift.Paginator.DescribeReservedNodes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describereservednodespaginator)
        """

if TYPE_CHECKING:
    _DescribeScheduledActionsPaginatorBase = Paginator[ScheduledActionsMessageTypeDef]
else:
    _DescribeScheduledActionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeScheduledActionsPaginator(_DescribeScheduledActionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeScheduledActions.html#Redshift.Paginator.DescribeScheduledActions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describescheduledactionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeScheduledActionsMessagePaginateTypeDef]
    ) -> PageIterator[ScheduledActionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeScheduledActions.html#Redshift.Paginator.DescribeScheduledActions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describescheduledactionspaginator)
        """

if TYPE_CHECKING:
    _DescribeSnapshotCopyGrantsPaginatorBase = Paginator[SnapshotCopyGrantMessageTypeDef]
else:
    _DescribeSnapshotCopyGrantsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSnapshotCopyGrantsPaginator(_DescribeSnapshotCopyGrantsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeSnapshotCopyGrants.html#Redshift.Paginator.DescribeSnapshotCopyGrants)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describesnapshotcopygrantspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSnapshotCopyGrantsMessagePaginateTypeDef]
    ) -> PageIterator[SnapshotCopyGrantMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeSnapshotCopyGrants.html#Redshift.Paginator.DescribeSnapshotCopyGrants.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describesnapshotcopygrantspaginator)
        """

if TYPE_CHECKING:
    _DescribeSnapshotSchedulesPaginatorBase = Paginator[
        DescribeSnapshotSchedulesOutputMessageTypeDef
    ]
else:
    _DescribeSnapshotSchedulesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSnapshotSchedulesPaginator(_DescribeSnapshotSchedulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeSnapshotSchedules.html#Redshift.Paginator.DescribeSnapshotSchedules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describesnapshotschedulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSnapshotSchedulesMessagePaginateTypeDef]
    ) -> PageIterator[DescribeSnapshotSchedulesOutputMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeSnapshotSchedules.html#Redshift.Paginator.DescribeSnapshotSchedules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describesnapshotschedulespaginator)
        """

if TYPE_CHECKING:
    _DescribeTableRestoreStatusPaginatorBase = Paginator[TableRestoreStatusMessageTypeDef]
else:
    _DescribeTableRestoreStatusPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTableRestoreStatusPaginator(_DescribeTableRestoreStatusPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeTableRestoreStatus.html#Redshift.Paginator.DescribeTableRestoreStatus)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describetablerestorestatuspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTableRestoreStatusMessagePaginateTypeDef]
    ) -> PageIterator[TableRestoreStatusMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeTableRestoreStatus.html#Redshift.Paginator.DescribeTableRestoreStatus.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describetablerestorestatuspaginator)
        """

if TYPE_CHECKING:
    _DescribeTagsPaginatorBase = Paginator[TaggedResourceListMessageTypeDef]
else:
    _DescribeTagsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTagsPaginator(_DescribeTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeTags.html#Redshift.Paginator.DescribeTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describetagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTagsMessagePaginateTypeDef]
    ) -> PageIterator[TaggedResourceListMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeTags.html#Redshift.Paginator.DescribeTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describetagspaginator)
        """

if TYPE_CHECKING:
    _DescribeUsageLimitsPaginatorBase = Paginator[UsageLimitListTypeDef]
else:
    _DescribeUsageLimitsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeUsageLimitsPaginator(_DescribeUsageLimitsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeUsageLimits.html#Redshift.Paginator.DescribeUsageLimits)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeusagelimitspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeUsageLimitsMessagePaginateTypeDef]
    ) -> PageIterator[UsageLimitListTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/DescribeUsageLimits.html#Redshift.Paginator.DescribeUsageLimits.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#describeusagelimitspaginator)
        """

if TYPE_CHECKING:
    _GetReservedNodeExchangeConfigurationOptionsPaginatorBase = Paginator[
        GetReservedNodeExchangeConfigurationOptionsOutputMessageTypeDef
    ]
else:
    _GetReservedNodeExchangeConfigurationOptionsPaginatorBase = Paginator  # type: ignore[assignment]

class GetReservedNodeExchangeConfigurationOptionsPaginator(
    _GetReservedNodeExchangeConfigurationOptionsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/GetReservedNodeExchangeConfigurationOptions.html#Redshift.Paginator.GetReservedNodeExchangeConfigurationOptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#getreservednodeexchangeconfigurationoptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self,
        **kwargs: Unpack[GetReservedNodeExchangeConfigurationOptionsInputMessagePaginateTypeDef],
    ) -> PageIterator[GetReservedNodeExchangeConfigurationOptionsOutputMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/GetReservedNodeExchangeConfigurationOptions.html#Redshift.Paginator.GetReservedNodeExchangeConfigurationOptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#getreservednodeexchangeconfigurationoptionspaginator)
        """

if TYPE_CHECKING:
    _GetReservedNodeExchangeOfferingsPaginatorBase = Paginator[
        GetReservedNodeExchangeOfferingsOutputMessageTypeDef
    ]
else:
    _GetReservedNodeExchangeOfferingsPaginatorBase = Paginator  # type: ignore[assignment]

class GetReservedNodeExchangeOfferingsPaginator(_GetReservedNodeExchangeOfferingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/GetReservedNodeExchangeOfferings.html#Redshift.Paginator.GetReservedNodeExchangeOfferings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#getreservednodeexchangeofferingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetReservedNodeExchangeOfferingsInputMessagePaginateTypeDef]
    ) -> PageIterator[GetReservedNodeExchangeOfferingsOutputMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/GetReservedNodeExchangeOfferings.html#Redshift.Paginator.GetReservedNodeExchangeOfferings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#getreservednodeexchangeofferingspaginator)
        """

if TYPE_CHECKING:
    _ListRecommendationsPaginatorBase = Paginator[ListRecommendationsResultTypeDef]
else:
    _ListRecommendationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRecommendationsPaginator(_ListRecommendationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/ListRecommendations.html#Redshift.Paginator.ListRecommendations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#listrecommendationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRecommendationsMessagePaginateTypeDef]
    ) -> PageIterator[ListRecommendationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift/paginator/ListRecommendations.html#Redshift.Paginator.ListRecommendations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators/#listrecommendationspaginator)
        """
