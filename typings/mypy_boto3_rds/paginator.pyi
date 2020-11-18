# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for rds service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_rds import RDSClient
    from mypy_boto3_rds.paginator import (
        DescribeCertificatesPaginator,
        DescribeCustomAvailabilityZonesPaginator,
        DescribeDBClusterBacktracksPaginator,
        DescribeDBClusterEndpointsPaginator,
        DescribeDBClusterParameterGroupsPaginator,
        DescribeDBClusterParametersPaginator,
        DescribeDBClusterSnapshotsPaginator,
        DescribeDBClustersPaginator,
        DescribeDBEngineVersionsPaginator,
        DescribeDBInstanceAutomatedBackupsPaginator,
        DescribeDBInstancesPaginator,
        DescribeDBLogFilesPaginator,
        DescribeDBParameterGroupsPaginator,
        DescribeDBParametersPaginator,
        DescribeDBProxiesPaginator,
        DescribeDBProxyTargetGroupsPaginator,
        DescribeDBProxyTargetsPaginator,
        DescribeDBSecurityGroupsPaginator,
        DescribeDBSnapshotsPaginator,
        DescribeDBSubnetGroupsPaginator,
        DescribeEngineDefaultClusterParametersPaginator,
        DescribeEngineDefaultParametersPaginator,
        DescribeEventSubscriptionsPaginator,
        DescribeEventsPaginator,
        DescribeExportTasksPaginator,
        DescribeGlobalClustersPaginator,
        DescribeInstallationMediaPaginator,
        DescribeOptionGroupOptionsPaginator,
        DescribeOptionGroupsPaginator,
        DescribeOrderableDBInstanceOptionsPaginator,
        DescribePendingMaintenanceActionsPaginator,
        DescribeReservedDBInstancesPaginator,
        DescribeReservedDBInstancesOfferingsPaginator,
        DescribeSourceRegionsPaginator,
        DownloadDBLogFilePortionPaginator,
    )

    client: RDSClient = boto3.client("rds")

    describe_certificates_paginator: DescribeCertificatesPaginator = client.get_paginator("describe_certificates")
    describe_custom_availability_zones_paginator: DescribeCustomAvailabilityZonesPaginator = client.get_paginator("describe_custom_availability_zones")
    describe_db_cluster_backtracks_paginator: DescribeDBClusterBacktracksPaginator = client.get_paginator("describe_db_cluster_backtracks")
    describe_db_cluster_endpoints_paginator: DescribeDBClusterEndpointsPaginator = client.get_paginator("describe_db_cluster_endpoints")
    describe_db_cluster_parameter_groups_paginator: DescribeDBClusterParameterGroupsPaginator = client.get_paginator("describe_db_cluster_parameter_groups")
    describe_db_cluster_parameters_paginator: DescribeDBClusterParametersPaginator = client.get_paginator("describe_db_cluster_parameters")
    describe_db_cluster_snapshots_paginator: DescribeDBClusterSnapshotsPaginator = client.get_paginator("describe_db_cluster_snapshots")
    describe_db_clusters_paginator: DescribeDBClustersPaginator = client.get_paginator("describe_db_clusters")
    describe_db_engine_versions_paginator: DescribeDBEngineVersionsPaginator = client.get_paginator("describe_db_engine_versions")
    describe_db_instance_automated_backups_paginator: DescribeDBInstanceAutomatedBackupsPaginator = client.get_paginator("describe_db_instance_automated_backups")
    describe_db_instances_paginator: DescribeDBInstancesPaginator = client.get_paginator("describe_db_instances")
    describe_db_log_files_paginator: DescribeDBLogFilesPaginator = client.get_paginator("describe_db_log_files")
    describe_db_parameter_groups_paginator: DescribeDBParameterGroupsPaginator = client.get_paginator("describe_db_parameter_groups")
    describe_db_parameters_paginator: DescribeDBParametersPaginator = client.get_paginator("describe_db_parameters")
    describe_db_proxies_paginator: DescribeDBProxiesPaginator = client.get_paginator("describe_db_proxies")
    describe_db_proxy_target_groups_paginator: DescribeDBProxyTargetGroupsPaginator = client.get_paginator("describe_db_proxy_target_groups")
    describe_db_proxy_targets_paginator: DescribeDBProxyTargetsPaginator = client.get_paginator("describe_db_proxy_targets")
    describe_db_security_groups_paginator: DescribeDBSecurityGroupsPaginator = client.get_paginator("describe_db_security_groups")
    describe_db_snapshots_paginator: DescribeDBSnapshotsPaginator = client.get_paginator("describe_db_snapshots")
    describe_db_subnet_groups_paginator: DescribeDBSubnetGroupsPaginator = client.get_paginator("describe_db_subnet_groups")
    describe_engine_default_cluster_parameters_paginator: DescribeEngineDefaultClusterParametersPaginator = client.get_paginator("describe_engine_default_cluster_parameters")
    describe_engine_default_parameters_paginator: DescribeEngineDefaultParametersPaginator = client.get_paginator("describe_engine_default_parameters")
    describe_event_subscriptions_paginator: DescribeEventSubscriptionsPaginator = client.get_paginator("describe_event_subscriptions")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_export_tasks_paginator: DescribeExportTasksPaginator = client.get_paginator("describe_export_tasks")
    describe_global_clusters_paginator: DescribeGlobalClustersPaginator = client.get_paginator("describe_global_clusters")
    describe_installation_media_paginator: DescribeInstallationMediaPaginator = client.get_paginator("describe_installation_media")
    describe_option_group_options_paginator: DescribeOptionGroupOptionsPaginator = client.get_paginator("describe_option_group_options")
    describe_option_groups_paginator: DescribeOptionGroupsPaginator = client.get_paginator("describe_option_groups")
    describe_orderable_db_instance_options_paginator: DescribeOrderableDBInstanceOptionsPaginator = client.get_paginator("describe_orderable_db_instance_options")
    describe_pending_maintenance_actions_paginator: DescribePendingMaintenanceActionsPaginator = client.get_paginator("describe_pending_maintenance_actions")
    describe_reserved_db_instances_paginator: DescribeReservedDBInstancesPaginator = client.get_paginator("describe_reserved_db_instances")
    describe_reserved_db_instances_offerings_paginator: DescribeReservedDBInstancesOfferingsPaginator = client.get_paginator("describe_reserved_db_instances_offerings")
    describe_source_regions_paginator: DescribeSourceRegionsPaginator = client.get_paginator("describe_source_regions")
    download_db_log_file_portion_paginator: DownloadDBLogFilePortionPaginator = client.get_paginator("download_db_log_file_portion")
    ```
"""
import sys
from datetime import datetime
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_rds.type_defs import (
    CertificateMessageTypeDef,
    CustomAvailabilityZoneMessageTypeDef,
    DBClusterBacktrackMessageTypeDef,
    DBClusterEndpointMessageTypeDef,
    DBClusterMessageTypeDef,
    DBClusterParameterGroupDetailsTypeDef,
    DBClusterParameterGroupsMessageTypeDef,
    DBClusterSnapshotMessageTypeDef,
    DBEngineVersionMessageTypeDef,
    DBInstanceAutomatedBackupMessageTypeDef,
    DBInstanceMessageTypeDef,
    DBParameterGroupDetailsTypeDef,
    DBParameterGroupsMessageTypeDef,
    DBSecurityGroupMessageTypeDef,
    DBSnapshotMessageTypeDef,
    DBSubnetGroupMessageTypeDef,
    DescribeDBLogFilesResponseTypeDef,
    DescribeDBProxiesResponseTypeDef,
    DescribeDBProxyTargetGroupsResponseTypeDef,
    DescribeDBProxyTargetsResponseTypeDef,
    DescribeEngineDefaultClusterParametersResultTypeDef,
    DescribeEngineDefaultParametersResultTypeDef,
    DownloadDBLogFilePortionDetailsTypeDef,
    EventsMessageTypeDef,
    EventSubscriptionsMessageTypeDef,
    ExportTasksMessageTypeDef,
    FilterTypeDef,
    GlobalClustersMessageTypeDef,
    InstallationMediaMessageTypeDef,
    OptionGroupOptionsMessageTypeDef,
    OptionGroupsTypeDef,
    OrderableDBInstanceOptionsMessageTypeDef,
    PaginatorConfigTypeDef,
    PendingMaintenanceActionsMessageTypeDef,
    ReservedDBInstanceMessageTypeDef,
    ReservedDBInstancesOfferingMessageTypeDef,
    SourceRegionMessageTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeCertificatesPaginator",
    "DescribeCustomAvailabilityZonesPaginator",
    "DescribeDBClusterBacktracksPaginator",
    "DescribeDBClusterEndpointsPaginator",
    "DescribeDBClusterParameterGroupsPaginator",
    "DescribeDBClusterParametersPaginator",
    "DescribeDBClusterSnapshotsPaginator",
    "DescribeDBClustersPaginator",
    "DescribeDBEngineVersionsPaginator",
    "DescribeDBInstanceAutomatedBackupsPaginator",
    "DescribeDBInstancesPaginator",
    "DescribeDBLogFilesPaginator",
    "DescribeDBParameterGroupsPaginator",
    "DescribeDBParametersPaginator",
    "DescribeDBProxiesPaginator",
    "DescribeDBProxyTargetGroupsPaginator",
    "DescribeDBProxyTargetsPaginator",
    "DescribeDBSecurityGroupsPaginator",
    "DescribeDBSnapshotsPaginator",
    "DescribeDBSubnetGroupsPaginator",
    "DescribeEngineDefaultClusterParametersPaginator",
    "DescribeEngineDefaultParametersPaginator",
    "DescribeEventSubscriptionsPaginator",
    "DescribeEventsPaginator",
    "DescribeExportTasksPaginator",
    "DescribeGlobalClustersPaginator",
    "DescribeInstallationMediaPaginator",
    "DescribeOptionGroupOptionsPaginator",
    "DescribeOptionGroupsPaginator",
    "DescribeOrderableDBInstanceOptionsPaginator",
    "DescribePendingMaintenanceActionsPaginator",
    "DescribeReservedDBInstancesPaginator",
    "DescribeReservedDBInstancesOfferingsPaginator",
    "DescribeSourceRegionsPaginator",
    "DownloadDBLogFilePortionPaginator",
)


class DescribeCertificatesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeCertificates)
    """

    def paginate(
        self,
        CertificateIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[CertificateMessageTypeDef]:
        """
        [DescribeCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeCertificates.paginate)
        """


class DescribeCustomAvailabilityZonesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCustomAvailabilityZones documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeCustomAvailabilityZones)
    """

    def paginate(
        self,
        CustomAvailabilityZoneId: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[CustomAvailabilityZoneMessageTypeDef]:
        """
        [DescribeCustomAvailabilityZones.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeCustomAvailabilityZones.paginate)
        """


class DescribeDBClusterBacktracksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBClusterBacktracks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBClusterBacktracks)
    """

    def paginate(
        self,
        DBClusterIdentifier: str,
        BacktrackIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DBClusterBacktrackMessageTypeDef]:
        """
        [DescribeDBClusterBacktracks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBClusterBacktracks.paginate)
        """


class DescribeDBClusterEndpointsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBClusterEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBClusterEndpoints)
    """

    def paginate(
        self,
        DBClusterIdentifier: str = None,
        DBClusterEndpointIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DBClusterEndpointMessageTypeDef]:
        """
        [DescribeDBClusterEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBClusterEndpoints.paginate)
        """


class DescribeDBClusterParameterGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBClusterParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBClusterParameterGroups)
    """

    def paginate(
        self,
        DBClusterParameterGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DBClusterParameterGroupsMessageTypeDef]:
        """
        [DescribeDBClusterParameterGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBClusterParameterGroups.paginate)
        """


class DescribeDBClusterParametersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBClusterParameters)
    """

    def paginate(
        self,
        DBClusterParameterGroupName: str,
        Source: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DBClusterParameterGroupDetailsTypeDef]:
        """
        [DescribeDBClusterParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBClusterParameters.paginate)
        """


class DescribeDBClusterSnapshotsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBClusterSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBClusterSnapshots)
    """

    def paginate(
        self,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DBClusterSnapshotMessageTypeDef]:
        """
        [DescribeDBClusterSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBClusterSnapshots.paginate)
        """


class DescribeDBClustersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBClusters)
    """

    def paginate(
        self,
        DBClusterIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        IncludeShared: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DBClusterMessageTypeDef]:
        """
        [DescribeDBClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBClusters.paginate)
        """


class DescribeDBEngineVersionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBEngineVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBEngineVersions)
    """

    def paginate(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        DBParameterGroupFamily: str = None,
        Filters: List[FilterTypeDef] = None,
        DefaultOnly: bool = None,
        ListSupportedCharacterSets: bool = None,
        ListSupportedTimezones: bool = None,
        IncludeAll: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DBEngineVersionMessageTypeDef]:
        """
        [DescribeDBEngineVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBEngineVersions.paginate)
        """


class DescribeDBInstanceAutomatedBackupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBInstanceAutomatedBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBInstanceAutomatedBackups)
    """

    def paginate(
        self,
        DbiResourceId: str = None,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DBInstanceAutomatedBackupMessageTypeDef]:
        """
        [DescribeDBInstanceAutomatedBackups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBInstanceAutomatedBackups.paginate)
        """


class DescribeDBInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBInstances)
    """

    def paginate(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DBInstanceMessageTypeDef]:
        """
        [DescribeDBInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBInstances.paginate)
        """


class DescribeDBLogFilesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBLogFiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBLogFiles)
    """

    def paginate(
        self,
        DBInstanceIdentifier: str,
        FilenameContains: str = None,
        FileLastWritten: int = None,
        FileSize: int = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeDBLogFilesResponseTypeDef]:
        """
        [DescribeDBLogFiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBLogFiles.paginate)
        """


class DescribeDBParameterGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBParameterGroups)
    """

    def paginate(
        self,
        DBParameterGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DBParameterGroupsMessageTypeDef]:
        """
        [DescribeDBParameterGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBParameterGroups.paginate)
        """


class DescribeDBParametersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBParameters)
    """

    def paginate(
        self,
        DBParameterGroupName: str,
        Source: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DBParameterGroupDetailsTypeDef]:
        """
        [DescribeDBParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBParameters.paginate)
        """


class DescribeDBProxiesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBProxies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBProxies)
    """

    def paginate(
        self,
        DBProxyName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeDBProxiesResponseTypeDef]:
        """
        [DescribeDBProxies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBProxies.paginate)
        """


class DescribeDBProxyTargetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBProxyTargetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBProxyTargetGroups)
    """

    def paginate(
        self,
        DBProxyName: str,
        TargetGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeDBProxyTargetGroupsResponseTypeDef]:
        """
        [DescribeDBProxyTargetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBProxyTargetGroups.paginate)
        """


class DescribeDBProxyTargetsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBProxyTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBProxyTargets)
    """

    def paginate(
        self,
        DBProxyName: str,
        TargetGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeDBProxyTargetsResponseTypeDef]:
        """
        [DescribeDBProxyTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBProxyTargets.paginate)
        """


class DescribeDBSecurityGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBSecurityGroups)
    """

    def paginate(
        self,
        DBSecurityGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DBSecurityGroupMessageTypeDef]:
        """
        [DescribeDBSecurityGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBSecurityGroups.paginate)
        """


class DescribeDBSnapshotsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBSnapshots)
    """

    def paginate(
        self,
        DBInstanceIdentifier: str = None,
        DBSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        DbiResourceId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DBSnapshotMessageTypeDef]:
        """
        [DescribeDBSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBSnapshots.paginate)
        """


class DescribeDBSubnetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDBSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBSubnetGroups)
    """

    def paginate(
        self,
        DBSubnetGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DBSubnetGroupMessageTypeDef]:
        """
        [DescribeDBSubnetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeDBSubnetGroups.paginate)
        """


class DescribeEngineDefaultClusterParametersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEngineDefaultClusterParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeEngineDefaultClusterParameters)
    """

    def paginate(
        self,
        DBParameterGroupFamily: str,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeEngineDefaultClusterParametersResultTypeDef]:
        """
        [DescribeEngineDefaultClusterParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeEngineDefaultClusterParameters.paginate)
        """


class DescribeEngineDefaultParametersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEngineDefaultParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeEngineDefaultParameters)
    """

    def paginate(
        self,
        DBParameterGroupFamily: str,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeEngineDefaultParametersResultTypeDef]:
        """
        [DescribeEngineDefaultParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeEngineDefaultParameters.paginate)
        """


class DescribeEventSubscriptionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeEventSubscriptions)
    """

    def paginate(
        self,
        SubscriptionName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[EventSubscriptionsMessageTypeDef]:
        """
        [DescribeEventSubscriptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeEventSubscriptions.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeEvents)
    """

    def paginate(
        self,
        SourceIdentifier: str = None,
        SourceType: Literal[
            "db-instance",
            "db-parameter-group",
            "db-security-group",
            "db-snapshot",
            "db-cluster",
            "db-cluster-snapshot",
        ] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[EventsMessageTypeDef]:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeEvents.paginate)
        """


class DescribeExportTasksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeExportTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeExportTasks)
    """

    def paginate(
        self,
        ExportTaskIdentifier: str = None,
        SourceArn: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ExportTasksMessageTypeDef]:
        """
        [DescribeExportTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeExportTasks.paginate)
        """


class DescribeGlobalClustersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeGlobalClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeGlobalClusters)
    """

    def paginate(
        self,
        GlobalClusterIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GlobalClustersMessageTypeDef]:
        """
        [DescribeGlobalClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeGlobalClusters.paginate)
        """


class DescribeInstallationMediaPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInstallationMedia documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeInstallationMedia)
    """

    def paginate(
        self,
        InstallationMediaId: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[InstallationMediaMessageTypeDef]:
        """
        [DescribeInstallationMedia.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeInstallationMedia.paginate)
        """


class DescribeOptionGroupOptionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeOptionGroupOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeOptionGroupOptions)
    """

    def paginate(
        self,
        EngineName: str,
        MajorEngineVersion: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[OptionGroupOptionsMessageTypeDef]:
        """
        [DescribeOptionGroupOptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeOptionGroupOptions.paginate)
        """


class DescribeOptionGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeOptionGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeOptionGroups)
    """

    def paginate(
        self,
        OptionGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        EngineName: str = None,
        MajorEngineVersion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[OptionGroupsTypeDef]:
        """
        [DescribeOptionGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeOptionGroups.paginate)
        """


class DescribeOrderableDBInstanceOptionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeOrderableDBInstanceOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeOrderableDBInstanceOptions)
    """

    def paginate(
        self,
        Engine: str,
        EngineVersion: str = None,
        DBInstanceClass: str = None,
        LicenseModel: str = None,
        AvailabilityZoneGroup: str = None,
        Vpc: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[OrderableDBInstanceOptionsMessageTypeDef]:
        """
        [DescribeOrderableDBInstanceOptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeOrderableDBInstanceOptions.paginate)
        """


class DescribePendingMaintenanceActionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribePendingMaintenanceActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribePendingMaintenanceActions)
    """

    def paginate(
        self,
        ResourceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[PendingMaintenanceActionsMessageTypeDef]:
        """
        [DescribePendingMaintenanceActions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribePendingMaintenanceActions.paginate)
        """


class DescribeReservedDBInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReservedDBInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeReservedDBInstances)
    """

    def paginate(
        self,
        ReservedDBInstanceId: str = None,
        ReservedDBInstancesOfferingId: str = None,
        DBInstanceClass: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MultiAZ: bool = None,
        LeaseId: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ReservedDBInstanceMessageTypeDef]:
        """
        [DescribeReservedDBInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeReservedDBInstances.paginate)
        """


class DescribeReservedDBInstancesOfferingsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReservedDBInstancesOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeReservedDBInstancesOfferings)
    """

    def paginate(
        self,
        ReservedDBInstancesOfferingId: str = None,
        DBInstanceClass: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        MultiAZ: bool = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ReservedDBInstancesOfferingMessageTypeDef]:
        """
        [DescribeReservedDBInstancesOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeReservedDBInstancesOfferings.paginate)
        """


class DescribeSourceRegionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSourceRegions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeSourceRegions)
    """

    def paginate(
        self,
        RegionName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[SourceRegionMessageTypeDef]:
        """
        [DescribeSourceRegions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DescribeSourceRegions.paginate)
        """


class DownloadDBLogFilePortionPaginator(Boto3Paginator):
    """
    [Paginator.DownloadDBLogFilePortion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DownloadDBLogFilePortion)
    """

    def paginate(
        self,
        DBInstanceIdentifier: str,
        LogFileName: str,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DownloadDBLogFilePortionDetailsTypeDef]:
        """
        [DownloadDBLogFilePortion.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds.html#RDS.Paginator.DownloadDBLogFilePortion.paginate)
        """
