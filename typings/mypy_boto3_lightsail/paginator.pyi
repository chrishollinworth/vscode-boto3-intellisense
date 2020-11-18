# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for lightsail service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_lightsail import LightsailClient
    from mypy_boto3_lightsail.paginator import (
        GetActiveNamesPaginator,
        GetBlueprintsPaginator,
        GetBundlesPaginator,
        GetCloudFormationStackRecordsPaginator,
        GetDiskSnapshotsPaginator,
        GetDisksPaginator,
        GetDomainsPaginator,
        GetExportSnapshotRecordsPaginator,
        GetInstanceSnapshotsPaginator,
        GetInstancesPaginator,
        GetKeyPairsPaginator,
        GetLoadBalancersPaginator,
        GetOperationsPaginator,
        GetRelationalDatabaseBlueprintsPaginator,
        GetRelationalDatabaseBundlesPaginator,
        GetRelationalDatabaseEventsPaginator,
        GetRelationalDatabaseParametersPaginator,
        GetRelationalDatabaseSnapshotsPaginator,
        GetRelationalDatabasesPaginator,
        GetStaticIpsPaginator,
    )

    client: LightsailClient = boto3.client("lightsail")

    get_active_names_paginator: GetActiveNamesPaginator = client.get_paginator("get_active_names")
    get_blueprints_paginator: GetBlueprintsPaginator = client.get_paginator("get_blueprints")
    get_bundles_paginator: GetBundlesPaginator = client.get_paginator("get_bundles")
    get_cloud_formation_stack_records_paginator: GetCloudFormationStackRecordsPaginator = client.get_paginator("get_cloud_formation_stack_records")
    get_disk_snapshots_paginator: GetDiskSnapshotsPaginator = client.get_paginator("get_disk_snapshots")
    get_disks_paginator: GetDisksPaginator = client.get_paginator("get_disks")
    get_domains_paginator: GetDomainsPaginator = client.get_paginator("get_domains")
    get_export_snapshot_records_paginator: GetExportSnapshotRecordsPaginator = client.get_paginator("get_export_snapshot_records")
    get_instance_snapshots_paginator: GetInstanceSnapshotsPaginator = client.get_paginator("get_instance_snapshots")
    get_instances_paginator: GetInstancesPaginator = client.get_paginator("get_instances")
    get_key_pairs_paginator: GetKeyPairsPaginator = client.get_paginator("get_key_pairs")
    get_load_balancers_paginator: GetLoadBalancersPaginator = client.get_paginator("get_load_balancers")
    get_operations_paginator: GetOperationsPaginator = client.get_paginator("get_operations")
    get_relational_database_blueprints_paginator: GetRelationalDatabaseBlueprintsPaginator = client.get_paginator("get_relational_database_blueprints")
    get_relational_database_bundles_paginator: GetRelationalDatabaseBundlesPaginator = client.get_paginator("get_relational_database_bundles")
    get_relational_database_events_paginator: GetRelationalDatabaseEventsPaginator = client.get_paginator("get_relational_database_events")
    get_relational_database_parameters_paginator: GetRelationalDatabaseParametersPaginator = client.get_paginator("get_relational_database_parameters")
    get_relational_database_snapshots_paginator: GetRelationalDatabaseSnapshotsPaginator = client.get_paginator("get_relational_database_snapshots")
    get_relational_databases_paginator: GetRelationalDatabasesPaginator = client.get_paginator("get_relational_databases")
    get_static_ips_paginator: GetStaticIpsPaginator = client.get_paginator("get_static_ips")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_lightsail.type_defs import (
    GetActiveNamesResultTypeDef,
    GetBlueprintsResultTypeDef,
    GetBundlesResultTypeDef,
    GetCloudFormationStackRecordsResultTypeDef,
    GetDiskSnapshotsResultTypeDef,
    GetDisksResultTypeDef,
    GetDomainsResultTypeDef,
    GetExportSnapshotRecordsResultTypeDef,
    GetInstanceSnapshotsResultTypeDef,
    GetInstancesResultTypeDef,
    GetKeyPairsResultTypeDef,
    GetLoadBalancersResultTypeDef,
    GetOperationsResultTypeDef,
    GetRelationalDatabaseBlueprintsResultTypeDef,
    GetRelationalDatabaseBundlesResultTypeDef,
    GetRelationalDatabaseEventsResultTypeDef,
    GetRelationalDatabaseParametersResultTypeDef,
    GetRelationalDatabaseSnapshotsResultTypeDef,
    GetRelationalDatabasesResultTypeDef,
    GetStaticIpsResultTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "GetActiveNamesPaginator",
    "GetBlueprintsPaginator",
    "GetBundlesPaginator",
    "GetCloudFormationStackRecordsPaginator",
    "GetDiskSnapshotsPaginator",
    "GetDisksPaginator",
    "GetDomainsPaginator",
    "GetExportSnapshotRecordsPaginator",
    "GetInstanceSnapshotsPaginator",
    "GetInstancesPaginator",
    "GetKeyPairsPaginator",
    "GetLoadBalancersPaginator",
    "GetOperationsPaginator",
    "GetRelationalDatabaseBlueprintsPaginator",
    "GetRelationalDatabaseBundlesPaginator",
    "GetRelationalDatabaseEventsPaginator",
    "GetRelationalDatabaseParametersPaginator",
    "GetRelationalDatabaseSnapshotsPaginator",
    "GetRelationalDatabasesPaginator",
    "GetStaticIpsPaginator",
)


class GetActiveNamesPaginator(Boto3Paginator):
    """
    [Paginator.GetActiveNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetActiveNames)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetActiveNamesResultTypeDef]:
        """
        [GetActiveNames.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetActiveNames.paginate)
        """


class GetBlueprintsPaginator(Boto3Paginator):
    """
    [Paginator.GetBlueprints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetBlueprints)
    """

    def paginate(
        self, includeInactive: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetBlueprintsResultTypeDef]:
        """
        [GetBlueprints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetBlueprints.paginate)
        """


class GetBundlesPaginator(Boto3Paginator):
    """
    [Paginator.GetBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetBundles)
    """

    def paginate(
        self, includeInactive: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetBundlesResultTypeDef]:
        """
        [GetBundles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetBundles.paginate)
        """


class GetCloudFormationStackRecordsPaginator(Boto3Paginator):
    """
    [Paginator.GetCloudFormationStackRecords documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetCloudFormationStackRecords)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetCloudFormationStackRecordsResultTypeDef]:
        """
        [GetCloudFormationStackRecords.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetCloudFormationStackRecords.paginate)
        """


class GetDiskSnapshotsPaginator(Boto3Paginator):
    """
    [Paginator.GetDiskSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetDiskSnapshots)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetDiskSnapshotsResultTypeDef]:
        """
        [GetDiskSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetDiskSnapshots.paginate)
        """


class GetDisksPaginator(Boto3Paginator):
    """
    [Paginator.GetDisks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetDisks)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetDisksResultTypeDef]:
        """
        [GetDisks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetDisks.paginate)
        """


class GetDomainsPaginator(Boto3Paginator):
    """
    [Paginator.GetDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetDomains)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetDomainsResultTypeDef]:
        """
        [GetDomains.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetDomains.paginate)
        """


class GetExportSnapshotRecordsPaginator(Boto3Paginator):
    """
    [Paginator.GetExportSnapshotRecords documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetExportSnapshotRecords)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetExportSnapshotRecordsResultTypeDef]:
        """
        [GetExportSnapshotRecords.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetExportSnapshotRecords.paginate)
        """


class GetInstanceSnapshotsPaginator(Boto3Paginator):
    """
    [Paginator.GetInstanceSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetInstanceSnapshots)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetInstanceSnapshotsResultTypeDef]:
        """
        [GetInstanceSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetInstanceSnapshots.paginate)
        """


class GetInstancesPaginator(Boto3Paginator):
    """
    [Paginator.GetInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetInstances)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetInstancesResultTypeDef]:
        """
        [GetInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetInstances.paginate)
        """


class GetKeyPairsPaginator(Boto3Paginator):
    """
    [Paginator.GetKeyPairs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetKeyPairs)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetKeyPairsResultTypeDef]:
        """
        [GetKeyPairs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetKeyPairs.paginate)
        """


class GetLoadBalancersPaginator(Boto3Paginator):
    """
    [Paginator.GetLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetLoadBalancers)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetLoadBalancersResultTypeDef]:
        """
        [GetLoadBalancers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetLoadBalancers.paginate)
        """


class GetOperationsPaginator(Boto3Paginator):
    """
    [Paginator.GetOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetOperations)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetOperationsResultTypeDef]:
        """
        [GetOperations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetOperations.paginate)
        """


class GetRelationalDatabaseBlueprintsPaginator(Boto3Paginator):
    """
    [Paginator.GetRelationalDatabaseBlueprints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBlueprints)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetRelationalDatabaseBlueprintsResultTypeDef]:
        """
        [GetRelationalDatabaseBlueprints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBlueprints.paginate)
        """


class GetRelationalDatabaseBundlesPaginator(Boto3Paginator):
    """
    [Paginator.GetRelationalDatabaseBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBundles)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetRelationalDatabaseBundlesResultTypeDef]:
        """
        [GetRelationalDatabaseBundles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBundles.paginate)
        """


class GetRelationalDatabaseEventsPaginator(Boto3Paginator):
    """
    [Paginator.GetRelationalDatabaseEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseEvents)
    """

    def paginate(
        self,
        relationalDatabaseName: str,
        durationInMinutes: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetRelationalDatabaseEventsResultTypeDef]:
        """
        [GetRelationalDatabaseEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseEvents.paginate)
        """


class GetRelationalDatabaseParametersPaginator(Boto3Paginator):
    """
    [Paginator.GetRelationalDatabaseParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseParameters)
    """

    def paginate(
        self, relationalDatabaseName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetRelationalDatabaseParametersResultTypeDef]:
        """
        [GetRelationalDatabaseParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseParameters.paginate)
        """


class GetRelationalDatabaseSnapshotsPaginator(Boto3Paginator):
    """
    [Paginator.GetRelationalDatabaseSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseSnapshots)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetRelationalDatabaseSnapshotsResultTypeDef]:
        """
        [GetRelationalDatabaseSnapshots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseSnapshots.paginate)
        """


class GetRelationalDatabasesPaginator(Boto3Paginator):
    """
    [Paginator.GetRelationalDatabases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabases)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetRelationalDatabasesResultTypeDef]:
        """
        [GetRelationalDatabases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabases.paginate)
        """


class GetStaticIpsPaginator(Boto3Paginator):
    """
    [Paginator.GetStaticIps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetStaticIps)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetStaticIpsResultTypeDef]:
        """
        [GetStaticIps.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetStaticIps.paginate)
        """
