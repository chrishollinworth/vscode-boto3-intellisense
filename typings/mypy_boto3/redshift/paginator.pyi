"""
Type annotations for redshift service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_redshift import RedshiftClient
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
        DescribeDataSharesPaginator,
        DescribeDataSharesForConsumerPaginator,
        DescribeDataSharesForProducerPaginator,
        DescribeDefaultClusterParametersPaginator,
        DescribeEndpointAccessPaginator,
        DescribeEndpointAuthorizationPaginator,
        DescribeEventSubscriptionsPaginator,
        DescribeEventsPaginator,
        DescribeHsmClientCertificatesPaginator,
        DescribeHsmConfigurationsPaginator,
        DescribeNodeConfigurationOptionsPaginator,
        DescribeOrderableClusterOptionsPaginator,
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
    )

    client: RedshiftClient = boto3.client("redshift")

    describe_cluster_db_revisions_paginator: DescribeClusterDbRevisionsPaginator = client.get_paginator("describe_cluster_db_revisions")
    describe_cluster_parameter_groups_paginator: DescribeClusterParameterGroupsPaginator = client.get_paginator("describe_cluster_parameter_groups")
    describe_cluster_parameters_paginator: DescribeClusterParametersPaginator = client.get_paginator("describe_cluster_parameters")
    describe_cluster_security_groups_paginator: DescribeClusterSecurityGroupsPaginator = client.get_paginator("describe_cluster_security_groups")
    describe_cluster_snapshots_paginator: DescribeClusterSnapshotsPaginator = client.get_paginator("describe_cluster_snapshots")
    describe_cluster_subnet_groups_paginator: DescribeClusterSubnetGroupsPaginator = client.get_paginator("describe_cluster_subnet_groups")
    describe_cluster_tracks_paginator: DescribeClusterTracksPaginator = client.get_paginator("describe_cluster_tracks")
    describe_cluster_versions_paginator: DescribeClusterVersionsPaginator = client.get_paginator("describe_cluster_versions")
    describe_clusters_paginator: DescribeClustersPaginator = client.get_paginator("describe_clusters")
    describe_data_shares_paginator: DescribeDataSharesPaginator = client.get_paginator("describe_data_shares")
    describe_data_shares_for_consumer_paginator: DescribeDataSharesForConsumerPaginator = client.get_paginator("describe_data_shares_for_consumer")
    describe_data_shares_for_producer_paginator: DescribeDataSharesForProducerPaginator = client.get_paginator("describe_data_shares_for_producer")
    describe_default_cluster_parameters_paginator: DescribeDefaultClusterParametersPaginator = client.get_paginator("describe_default_cluster_parameters")
    describe_endpoint_access_paginator: DescribeEndpointAccessPaginator = client.get_paginator("describe_endpoint_access")
    describe_endpoint_authorization_paginator: DescribeEndpointAuthorizationPaginator = client.get_paginator("describe_endpoint_authorization")
    describe_event_subscriptions_paginator: DescribeEventSubscriptionsPaginator = client.get_paginator("describe_event_subscriptions")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_hsm_client_certificates_paginator: DescribeHsmClientCertificatesPaginator = client.get_paginator("describe_hsm_client_certificates")
    describe_hsm_configurations_paginator: DescribeHsmConfigurationsPaginator = client.get_paginator("describe_hsm_configurations")
    describe_node_configuration_options_paginator: DescribeNodeConfigurationOptionsPaginator = client.get_paginator("describe_node_configuration_options")
    describe_orderable_cluster_options_paginator: DescribeOrderableClusterOptionsPaginator = client.get_paginator("describe_orderable_cluster_options")
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
    ```
"""
from datetime import datetime
from typing import Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    ActionTypeType,
    DataShareStatusForConsumerType,
    DataShareStatusForProducerType,
    ReservedNodeExchangeActionTypeType,
    ScheduledActionTypeValuesType,
    SourceTypeType,
    UsageLimitFeatureTypeType,
)
from .type_defs import (
    ClusterDbRevisionsMessageTypeDef,
    ClusterParameterGroupDetailsTypeDef,
    ClusterParameterGroupsMessageTypeDef,
    ClusterSecurityGroupMessageTypeDef,
    ClustersMessageTypeDef,
    ClusterSubnetGroupMessageTypeDef,
    ClusterVersionsMessageTypeDef,
    DescribeDataSharesForConsumerResultTypeDef,
    DescribeDataSharesForProducerResultTypeDef,
    DescribeDataSharesResultTypeDef,
    DescribeDefaultClusterParametersResultTypeDef,
    DescribeReservedNodeExchangeStatusOutputMessageTypeDef,
    DescribeSnapshotSchedulesOutputMessageTypeDef,
    EndpointAccessListTypeDef,
    EndpointAuthorizationListTypeDef,
    EventsMessageTypeDef,
    EventSubscriptionsMessageTypeDef,
    GetReservedNodeExchangeConfigurationOptionsOutputMessageTypeDef,
    GetReservedNodeExchangeOfferingsOutputMessageTypeDef,
    HsmClientCertificateMessageTypeDef,
    HsmConfigurationMessageTypeDef,
    NodeConfigurationOptionsFilterTypeDef,
    NodeConfigurationOptionsMessageTypeDef,
    OrderableClusterOptionsMessageTypeDef,
    PaginatorConfigTypeDef,
    ReservedNodeOfferingsMessageTypeDef,
    ReservedNodesMessageTypeDef,
    ScheduledActionFilterTypeDef,
    ScheduledActionsMessageTypeDef,
    SnapshotCopyGrantMessageTypeDef,
    SnapshotMessageTypeDef,
    SnapshotSortingEntityTypeDef,
    TableRestoreStatusMessageTypeDef,
    TaggedResourceListMessageTypeDef,
    TrackListMessageTypeDef,
    UsageLimitListTypeDef,
)

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
    "DescribeDataSharesPaginator",
    "DescribeDataSharesForConsumerPaginator",
    "DescribeDataSharesForProducerPaginator",
    "DescribeDefaultClusterParametersPaginator",
    "DescribeEndpointAccessPaginator",
    "DescribeEndpointAuthorizationPaginator",
    "DescribeEventSubscriptionsPaginator",
    "DescribeEventsPaginator",
    "DescribeHsmClientCertificatesPaginator",
    "DescribeHsmConfigurationsPaginator",
    "DescribeNodeConfigurationOptionsPaginator",
    "DescribeOrderableClusterOptionsPaginator",
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
)

class DescribeClusterDbRevisionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeClusterDbRevisions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclusterdbrevisionspaginator)
    """

    def paginate(
        self, *, ClusterIdentifier: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ClusterDbRevisionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeClusterDbRevisions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclusterdbrevisionspaginator)
        """

class DescribeClusterParameterGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeClusterParameterGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclusterparametergroupspaginator)
    """

    def paginate(
        self,
        *,
        ParameterGroupName: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ClusterParameterGroupsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeClusterParameterGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclusterparametergroupspaginator)
        """

class DescribeClusterParametersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeClusterParameters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclusterparameterspaginator)
    """

    def paginate(
        self,
        *,
        ParameterGroupName: str,
        Source: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ClusterParameterGroupDetailsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeClusterParameters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclusterparameterspaginator)
        """

class DescribeClusterSecurityGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSecurityGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclustersecuritygroupspaginator)
    """

    def paginate(
        self,
        *,
        ClusterSecurityGroupName: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ClusterSecurityGroupMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSecurityGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclustersecuritygroupspaginator)
        """

class DescribeClusterSnapshotsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSnapshots)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclustersnapshotspaginator)
    """

    def paginate(
        self,
        *,
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        SnapshotArn: str = None,
        SnapshotType: str = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        OwnerAccount: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        ClusterExists: bool = None,
        SortingEntities: List["SnapshotSortingEntityTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SnapshotMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSnapshots.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclustersnapshotspaginator)
        """

class DescribeClusterSubnetGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSubnetGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclustersubnetgroupspaginator)
    """

    def paginate(
        self,
        *,
        ClusterSubnetGroupName: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ClusterSubnetGroupMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSubnetGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclustersubnetgroupspaginator)
        """

class DescribeClusterTracksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeClusterTracks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclustertrackspaginator)
    """

    def paginate(
        self, *, MaintenanceTrackName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[TrackListMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeClusterTracks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclustertrackspaginator)
        """

class DescribeClusterVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeClusterVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclusterversionspaginator)
    """

    def paginate(
        self,
        *,
        ClusterVersion: str = None,
        ClusterParameterGroupFamily: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ClusterVersionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeClusterVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclusterversionspaginator)
        """

class DescribeClustersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeClusters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclusterspaginator)
    """

    def paginate(
        self,
        *,
        ClusterIdentifier: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ClustersMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeClusters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclusterspaginator)
        """

class DescribeDataSharesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeDataShares)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describedatasharespaginator)
    """

    def paginate(
        self, *, DataShareArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDataSharesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeDataShares.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describedatasharespaginator)
        """

class DescribeDataSharesForConsumerPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeDataSharesForConsumer)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describedatasharesforconsumerpaginator)
    """

    def paginate(
        self,
        *,
        ConsumerArn: str = None,
        Status: DataShareStatusForConsumerType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDataSharesForConsumerResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeDataSharesForConsumer.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describedatasharesforconsumerpaginator)
        """

class DescribeDataSharesForProducerPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeDataSharesForProducer)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describedatasharesforproducerpaginator)
    """

    def paginate(
        self,
        *,
        ProducerArn: str = None,
        Status: DataShareStatusForProducerType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDataSharesForProducerResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeDataSharesForProducer.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describedatasharesforproducerpaginator)
        """

class DescribeDefaultClusterParametersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeDefaultClusterParameters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describedefaultclusterparameterspaginator)
    """

    def paginate(
        self, *, ParameterGroupFamily: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDefaultClusterParametersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeDefaultClusterParameters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describedefaultclusterparameterspaginator)
        """

class DescribeEndpointAccessPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeEndpointAccess)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeendpointaccesspaginator)
    """

    def paginate(
        self,
        *,
        ClusterIdentifier: str = None,
        ResourceOwner: str = None,
        EndpointName: str = None,
        VpcId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[EndpointAccessListTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeEndpointAccess.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeendpointaccesspaginator)
        """

class DescribeEndpointAuthorizationPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeEndpointAuthorization)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeendpointauthorizationpaginator)
    """

    def paginate(
        self,
        *,
        ClusterIdentifier: str = None,
        Account: str = None,
        Grantee: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[EndpointAuthorizationListTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeEndpointAuthorization.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeendpointauthorizationpaginator)
        """

class DescribeEventSubscriptionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeEventSubscriptions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeeventsubscriptionspaginator)
    """

    def paginate(
        self,
        *,
        SubscriptionName: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[EventSubscriptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeEventSubscriptions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeeventsubscriptionspaginator)
        """

class DescribeEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeEvents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeeventspaginator)
    """

    def paginate(
        self,
        *,
        SourceIdentifier: str = None,
        SourceType: SourceTypeType = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        Duration: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[EventsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeEvents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeeventspaginator)
        """

class DescribeHsmClientCertificatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeHsmClientCertificates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describehsmclientcertificatespaginator)
    """

    def paginate(
        self,
        *,
        HsmClientCertificateIdentifier: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[HsmClientCertificateMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeHsmClientCertificates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describehsmclientcertificatespaginator)
        """

class DescribeHsmConfigurationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeHsmConfigurations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describehsmconfigurationspaginator)
    """

    def paginate(
        self,
        *,
        HsmConfigurationIdentifier: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[HsmConfigurationMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeHsmConfigurations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describehsmconfigurationspaginator)
        """

class DescribeNodeConfigurationOptionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeNodeConfigurationOptions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describenodeconfigurationoptionspaginator)
    """

    def paginate(
        self,
        *,
        ActionType: ActionTypeType,
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        SnapshotArn: str = None,
        OwnerAccount: str = None,
        Filters: List["NodeConfigurationOptionsFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[NodeConfigurationOptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeNodeConfigurationOptions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describenodeconfigurationoptionspaginator)
        """

class DescribeOrderableClusterOptionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeOrderableClusterOptions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeorderableclusteroptionspaginator)
    """

    def paginate(
        self,
        *,
        ClusterVersion: str = None,
        NodeType: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[OrderableClusterOptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeOrderableClusterOptions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeorderableclusteroptionspaginator)
        """

class DescribeReservedNodeExchangeStatusPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodeExchangeStatus)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describereservednodeexchangestatuspaginator)
    """

    def paginate(
        self,
        *,
        ReservedNodeId: str = None,
        ReservedNodeExchangeRequestId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeReservedNodeExchangeStatusOutputMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodeExchangeStatus.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describereservednodeexchangestatuspaginator)
        """

class DescribeReservedNodeOfferingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodeOfferings)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describereservednodeofferingspaginator)
    """

    def paginate(
        self, *, ReservedNodeOfferingId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ReservedNodeOfferingsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodeOfferings.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describereservednodeofferingspaginator)
        """

class DescribeReservedNodesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describereservednodespaginator)
    """

    def paginate(
        self, *, ReservedNodeId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ReservedNodesMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describereservednodespaginator)
        """

class DescribeScheduledActionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeScheduledActions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describescheduledactionspaginator)
    """

    def paginate(
        self,
        *,
        ScheduledActionName: str = None,
        TargetActionType: ScheduledActionTypeValuesType = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        Active: bool = None,
        Filters: List["ScheduledActionFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ScheduledActionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeScheduledActions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describescheduledactionspaginator)
        """

class DescribeSnapshotCopyGrantsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeSnapshotCopyGrants)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describesnapshotcopygrantspaginator)
    """

    def paginate(
        self,
        *,
        SnapshotCopyGrantName: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SnapshotCopyGrantMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeSnapshotCopyGrants.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describesnapshotcopygrantspaginator)
        """

class DescribeSnapshotSchedulesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeSnapshotSchedules)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describesnapshotschedulespaginator)
    """

    def paginate(
        self,
        *,
        ClusterIdentifier: str = None,
        ScheduleIdentifier: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSnapshotSchedulesOutputMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeSnapshotSchedules.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describesnapshotschedulespaginator)
        """

class DescribeTableRestoreStatusPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeTableRestoreStatus)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describetablerestorestatuspaginator)
    """

    def paginate(
        self,
        *,
        ClusterIdentifier: str = None,
        TableRestoreRequestId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[TableRestoreStatusMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeTableRestoreStatus.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describetablerestorestatuspaginator)
        """

class DescribeTagsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeTags)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describetagspaginator)
    """

    def paginate(
        self,
        *,
        ResourceName: str = None,
        ResourceType: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[TaggedResourceListMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeTags.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describetagspaginator)
        """

class DescribeUsageLimitsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeUsageLimits)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeusagelimitspaginator)
    """

    def paginate(
        self,
        *,
        UsageLimitId: str = None,
        ClusterIdentifier: str = None,
        FeatureType: UsageLimitFeatureTypeType = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[UsageLimitListTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.DescribeUsageLimits.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeusagelimitspaginator)
        """

class GetReservedNodeExchangeConfigurationOptionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.GetReservedNodeExchangeConfigurationOptions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#getreservednodeexchangeconfigurationoptionspaginator)
    """

    def paginate(
        self,
        *,
        ActionType: ReservedNodeExchangeActionTypeType,
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetReservedNodeExchangeConfigurationOptionsOutputMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.GetReservedNodeExchangeConfigurationOptions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#getreservednodeexchangeconfigurationoptionspaginator)
        """

class GetReservedNodeExchangeOfferingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.GetReservedNodeExchangeOfferings)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#getreservednodeexchangeofferingspaginator)
    """

    def paginate(
        self, *, ReservedNodeId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetReservedNodeExchangeOfferingsOutputMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/redshift.html#Redshift.Paginator.GetReservedNodeExchangeOfferings.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#getreservednodeexchangeofferingspaginator)
        """
