# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for redshift service client paginators.

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
        DescribeDefaultClusterParametersPaginator,
        DescribeEventSubscriptionsPaginator,
        DescribeEventsPaginator,
        DescribeHsmClientCertificatesPaginator,
        DescribeHsmConfigurationsPaginator,
        DescribeNodeConfigurationOptionsPaginator,
        DescribeOrderableClusterOptionsPaginator,
        DescribeReservedNodeOfferingsPaginator,
        DescribeReservedNodesPaginator,
        DescribeScheduledActionsPaginator,
        DescribeSnapshotCopyGrantsPaginator,
        DescribeSnapshotSchedulesPaginator,
        DescribeTableRestoreStatusPaginator,
        DescribeTagsPaginator,
        DescribeUsageLimitsPaginator,
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
    describe_default_cluster_parameters_paginator: DescribeDefaultClusterParametersPaginator = client.get_paginator("describe_default_cluster_parameters")
    describe_event_subscriptions_paginator: DescribeEventSubscriptionsPaginator = client.get_paginator("describe_event_subscriptions")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_hsm_client_certificates_paginator: DescribeHsmClientCertificatesPaginator = client.get_paginator("describe_hsm_client_certificates")
    describe_hsm_configurations_paginator: DescribeHsmConfigurationsPaginator = client.get_paginator("describe_hsm_configurations")
    describe_node_configuration_options_paginator: DescribeNodeConfigurationOptionsPaginator = client.get_paginator("describe_node_configuration_options")
    describe_orderable_cluster_options_paginator: DescribeOrderableClusterOptionsPaginator = client.get_paginator("describe_orderable_cluster_options")
    describe_reserved_node_offerings_paginator: DescribeReservedNodeOfferingsPaginator = client.get_paginator("describe_reserved_node_offerings")
    describe_reserved_nodes_paginator: DescribeReservedNodesPaginator = client.get_paginator("describe_reserved_nodes")
    describe_scheduled_actions_paginator: DescribeScheduledActionsPaginator = client.get_paginator("describe_scheduled_actions")
    describe_snapshot_copy_grants_paginator: DescribeSnapshotCopyGrantsPaginator = client.get_paginator("describe_snapshot_copy_grants")
    describe_snapshot_schedules_paginator: DescribeSnapshotSchedulesPaginator = client.get_paginator("describe_snapshot_schedules")
    describe_table_restore_status_paginator: DescribeTableRestoreStatusPaginator = client.get_paginator("describe_table_restore_status")
    describe_tags_paginator: DescribeTagsPaginator = client.get_paginator("describe_tags")
    describe_usage_limits_paginator: DescribeUsageLimitsPaginator = client.get_paginator("describe_usage_limits")
    get_reserved_node_exchange_offerings_paginator: GetReservedNodeExchangeOfferingsPaginator = client.get_paginator("get_reserved_node_exchange_offerings")
    ```
"""
import sys
from datetime import datetime
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_redshift.type_defs import (
    ClusterDbRevisionsMessageTypeDef,
    ClusterParameterGroupDetailsTypeDef,
    ClusterParameterGroupsMessageTypeDef,
    ClusterSecurityGroupMessageTypeDef,
    ClustersMessageTypeDef,
    ClusterSubnetGroupMessageTypeDef,
    ClusterVersionsMessageTypeDef,
    DescribeDefaultClusterParametersResultTypeDef,
    DescribeSnapshotSchedulesOutputMessageTypeDef,
    EventsMessageTypeDef,
    EventSubscriptionsMessageTypeDef,
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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


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
    "DescribeDefaultClusterParametersPaginator",
    "DescribeEventSubscriptionsPaginator",
    "DescribeEventsPaginator",
    "DescribeHsmClientCertificatesPaginator",
    "DescribeHsmConfigurationsPaginator",
    "DescribeNodeConfigurationOptionsPaginator",
    "DescribeOrderableClusterOptionsPaginator",
    "DescribeReservedNodeOfferingsPaginator",
    "DescribeReservedNodesPaginator",
    "DescribeScheduledActionsPaginator",
    "DescribeSnapshotCopyGrantsPaginator",
    "DescribeSnapshotSchedulesPaginator",
    "DescribeTableRestoreStatusPaginator",
    "DescribeTagsPaginator",
    "DescribeUsageLimitsPaginator",
    "GetReservedNodeExchangeOfferingsPaginator",
)


class DescribeClusterDbRevisionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClusterDbRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeClusterDbRevisions)
    """

    def paginate(
        self, ClusterIdentifier: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ClusterDbRevisionsMessageTypeDef]:
        """
        [DescribeClusterDbRevisions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeClusterDbRevisions.paginate)
        """


class DescribeClusterParameterGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClusterParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeClusterParameterGroups)
    """

    def paginate(
        self,
        ParameterGroupName: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ClusterParameterGroupsMessageTypeDef]:
        """
        [DescribeClusterParameterGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeClusterParameterGroups.paginate)
        """


class DescribeClusterParametersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeClusterParameters)
    """

    def paginate(
        self,
        ParameterGroupName: str,
        Source: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ClusterParameterGroupDetailsTypeDef]:
        """
        [DescribeClusterParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeClusterParameters.paginate)
        """


class DescribeClusterSecurityGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClusterSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSecurityGroups)
    """

    def paginate(
        self,
        ClusterSecurityGroupName: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ClusterSecurityGroupMessageTypeDef]:
        """
        [DescribeClusterSecurityGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSecurityGroups.paginate)
        """


class DescribeClusterSnapshotsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClusterSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSnapshots)
    """

    def paginate(
        self,
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        SnapshotType: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        OwnerAccount: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        ClusterExists: bool = None,
        SortingEntities: List[SnapshotSortingEntityTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[SnapshotMessageTypeDef]:
        """
        [DescribeClusterSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSnapshots.paginate)
        """


class DescribeClusterSubnetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClusterSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSubnetGroups)
    """

    def paginate(
        self,
        ClusterSubnetGroupName: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ClusterSubnetGroupMessageTypeDef]:
        """
        [DescribeClusterSubnetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSubnetGroups.paginate)
        """


class DescribeClusterTracksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClusterTracks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeClusterTracks)
    """

    def paginate(
        self, MaintenanceTrackName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[TrackListMessageTypeDef]:
        """
        [DescribeClusterTracks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeClusterTracks.paginate)
        """


class DescribeClusterVersionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClusterVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeClusterVersions)
    """

    def paginate(
        self,
        ClusterVersion: str = None,
        ClusterParameterGroupFamily: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ClusterVersionsMessageTypeDef]:
        """
        [DescribeClusterVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeClusterVersions.paginate)
        """


class DescribeClustersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeClusters)
    """

    def paginate(
        self,
        ClusterIdentifier: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ClustersMessageTypeDef]:
        """
        [DescribeClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeClusters.paginate)
        """


class DescribeDefaultClusterParametersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDefaultClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeDefaultClusterParameters)
    """

    def paginate(
        self, ParameterGroupFamily: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDefaultClusterParametersResultTypeDef]:
        """
        [DescribeDefaultClusterParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeDefaultClusterParameters.paginate)
        """


class DescribeEventSubscriptionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeEventSubscriptions)
    """

    def paginate(
        self,
        SubscriptionName: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[EventSubscriptionsMessageTypeDef]:
        """
        [DescribeEventSubscriptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeEventSubscriptions.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeEvents)
    """

    def paginate(
        self,
        SourceIdentifier: str = None,
        SourceType: Literal[
            "cluster",
            "cluster-parameter-group",
            "cluster-security-group",
            "cluster-snapshot",
            "scheduled-action",
        ] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[EventsMessageTypeDef]:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeEvents.paginate)
        """


class DescribeHsmClientCertificatesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeHsmClientCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeHsmClientCertificates)
    """

    def paginate(
        self,
        HsmClientCertificateIdentifier: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[HsmClientCertificateMessageTypeDef]:
        """
        [DescribeHsmClientCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeHsmClientCertificates.paginate)
        """


class DescribeHsmConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeHsmConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeHsmConfigurations)
    """

    def paginate(
        self,
        HsmConfigurationIdentifier: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[HsmConfigurationMessageTypeDef]:
        """
        [DescribeHsmConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeHsmConfigurations.paginate)
        """


class DescribeNodeConfigurationOptionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeNodeConfigurationOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeNodeConfigurationOptions)
    """

    def paginate(
        self,
        ActionType: Literal["restore-cluster", "recommend-node-config", "resize-cluster"],
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        OwnerAccount: str = None,
        Filters: List[NodeConfigurationOptionsFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[NodeConfigurationOptionsMessageTypeDef]:
        """
        [DescribeNodeConfigurationOptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeNodeConfigurationOptions.paginate)
        """


class DescribeOrderableClusterOptionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeOrderableClusterOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeOrderableClusterOptions)
    """

    def paginate(
        self,
        ClusterVersion: str = None,
        NodeType: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[OrderableClusterOptionsMessageTypeDef]:
        """
        [DescribeOrderableClusterOptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeOrderableClusterOptions.paginate)
        """


class DescribeReservedNodeOfferingsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReservedNodeOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodeOfferings)
    """

    def paginate(
        self, ReservedNodeOfferingId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ReservedNodeOfferingsMessageTypeDef]:
        """
        [DescribeReservedNodeOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodeOfferings.paginate)
        """


class DescribeReservedNodesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReservedNodes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodes)
    """

    def paginate(
        self, ReservedNodeId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ReservedNodesMessageTypeDef]:
        """
        [DescribeReservedNodes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodes.paginate)
        """


class DescribeScheduledActionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeScheduledActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeScheduledActions)
    """

    def paginate(
        self,
        ScheduledActionName: str = None,
        TargetActionType: Literal["ResizeCluster", "PauseCluster", "ResumeCluster"] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Active: bool = None,
        Filters: List[ScheduledActionFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ScheduledActionsMessageTypeDef]:
        """
        [DescribeScheduledActions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeScheduledActions.paginate)
        """


class DescribeSnapshotCopyGrantsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSnapshotCopyGrants documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeSnapshotCopyGrants)
    """

    def paginate(
        self,
        SnapshotCopyGrantName: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[SnapshotCopyGrantMessageTypeDef]:
        """
        [DescribeSnapshotCopyGrants.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeSnapshotCopyGrants.paginate)
        """


class DescribeSnapshotSchedulesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSnapshotSchedules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeSnapshotSchedules)
    """

    def paginate(
        self,
        ClusterIdentifier: str = None,
        ScheduleIdentifier: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeSnapshotSchedulesOutputMessageTypeDef]:
        """
        [DescribeSnapshotSchedules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeSnapshotSchedules.paginate)
        """


class DescribeTableRestoreStatusPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTableRestoreStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeTableRestoreStatus)
    """

    def paginate(
        self,
        ClusterIdentifier: str = None,
        TableRestoreRequestId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[TableRestoreStatusMessageTypeDef]:
        """
        [DescribeTableRestoreStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeTableRestoreStatus.paginate)
        """


class DescribeTagsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeTags)
    """

    def paginate(
        self,
        ResourceName: str = None,
        ResourceType: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[TaggedResourceListMessageTypeDef]:
        """
        [DescribeTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeTags.paginate)
        """


class DescribeUsageLimitsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeUsageLimits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeUsageLimits)
    """

    def paginate(
        self,
        UsageLimitId: str = None,
        ClusterIdentifier: str = None,
        FeatureType: Literal["spectrum", "concurrency-scaling"] = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[UsageLimitListTypeDef]:
        """
        [DescribeUsageLimits.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.DescribeUsageLimits.paginate)
        """


class GetReservedNodeExchangeOfferingsPaginator(Boto3Paginator):
    """
    [Paginator.GetReservedNodeExchangeOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.GetReservedNodeExchangeOfferings)
    """

    def paginate(
        self, ReservedNodeId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetReservedNodeExchangeOfferingsOutputMessageTypeDef]:
        """
        [GetReservedNodeExchangeOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift.html#Redshift.Paginator.GetReservedNodeExchangeOfferings.paginate)
        """
