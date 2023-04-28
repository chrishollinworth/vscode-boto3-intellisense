"""
Type annotations for lightsail service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html)

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
import sys
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetActiveNames)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getactivenamespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetActiveNamesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetActiveNames.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getactivenamespaginator)
        """

class GetBlueprintsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetBlueprints)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getblueprintspaginator)
    """

    def paginate(
        self,
        *,
        includeInactive: bool = None,
        appCategory: Literal["LfR"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetBlueprintsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetBlueprints.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getblueprintspaginator)
        """

class GetBundlesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetBundles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getbundlespaginator)
    """

    def paginate(
        self,
        *,
        includeInactive: bool = None,
        appCategory: Literal["LfR"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetBundlesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetBundles.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getbundlespaginator)
        """

class GetCloudFormationStackRecordsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetCloudFormationStackRecords)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getcloudformationstackrecordspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetCloudFormationStackRecordsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetCloudFormationStackRecords.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getcloudformationstackrecordspaginator)
        """

class GetDiskSnapshotsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetDiskSnapshots)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getdisksnapshotspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetDiskSnapshotsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetDiskSnapshots.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getdisksnapshotspaginator)
        """

class GetDisksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetDisks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getdiskspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetDisksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetDisks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getdiskspaginator)
        """

class GetDomainsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetDomains)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getdomainspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetDomainsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetDomains.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getdomainspaginator)
        """

class GetExportSnapshotRecordsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetExportSnapshotRecords)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getexportsnapshotrecordspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetExportSnapshotRecordsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetExportSnapshotRecords.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getexportsnapshotrecordspaginator)
        """

class GetInstanceSnapshotsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetInstanceSnapshots)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getinstancesnapshotspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetInstanceSnapshotsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetInstanceSnapshots.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getinstancesnapshotspaginator)
        """

class GetInstancesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetInstances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getinstancespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetInstancesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetInstances.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getinstancespaginator)
        """

class GetKeyPairsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetKeyPairs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getkeypairspaginator)
    """

    def paginate(
        self, *, includeDefaultKeyPair: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetKeyPairsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetKeyPairs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getkeypairspaginator)
        """

class GetLoadBalancersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetLoadBalancers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getloadbalancerspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetLoadBalancersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetLoadBalancers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getloadbalancerspaginator)
        """

class GetOperationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetOperations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getoperationspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetOperationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetOperations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getoperationspaginator)
        """

class GetRelationalDatabaseBlueprintsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBlueprints)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabaseblueprintspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetRelationalDatabaseBlueprintsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBlueprints.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabaseblueprintspaginator)
        """

class GetRelationalDatabaseBundlesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBundles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabasebundlespaginator)
    """

    def paginate(
        self, *, includeInactive: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetRelationalDatabaseBundlesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBundles.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabasebundlespaginator)
        """

class GetRelationalDatabaseEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseEvents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabaseeventspaginator)
    """

    def paginate(
        self,
        *,
        relationalDatabaseName: str,
        durationInMinutes: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetRelationalDatabaseEventsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseEvents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabaseeventspaginator)
        """

class GetRelationalDatabaseParametersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseParameters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabaseparameterspaginator)
    """

    def paginate(
        self, *, relationalDatabaseName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetRelationalDatabaseParametersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseParameters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabaseparameterspaginator)
        """

class GetRelationalDatabaseSnapshotsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseSnapshots)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabasesnapshotspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetRelationalDatabaseSnapshotsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseSnapshots.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabasesnapshotspaginator)
        """

class GetRelationalDatabasesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabases)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabasespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetRelationalDatabasesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabases.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabasespaginator)
        """

class GetStaticIpsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetStaticIps)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getstaticipspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetStaticIpsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/lightsail.html#Lightsail.Paginator.GetStaticIps.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getstaticipspaginator)
        """
