"""
Type annotations for lightsail service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_lightsail.client import LightsailClient
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

    session = Session()
    client: LightsailClient = session.client("lightsail")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetActiveNamesRequestPaginateTypeDef,
    GetActiveNamesResultTypeDef,
    GetBlueprintsRequestPaginateTypeDef,
    GetBlueprintsResultTypeDef,
    GetBundlesRequestPaginateTypeDef,
    GetBundlesResultTypeDef,
    GetCloudFormationStackRecordsRequestPaginateTypeDef,
    GetCloudFormationStackRecordsResultTypeDef,
    GetDiskSnapshotsRequestPaginateTypeDef,
    GetDiskSnapshotsResultTypeDef,
    GetDisksRequestPaginateTypeDef,
    GetDisksResultTypeDef,
    GetDomainsRequestPaginateTypeDef,
    GetDomainsResultTypeDef,
    GetExportSnapshotRecordsRequestPaginateTypeDef,
    GetExportSnapshotRecordsResultTypeDef,
    GetInstanceSnapshotsRequestPaginateTypeDef,
    GetInstanceSnapshotsResultTypeDef,
    GetInstancesRequestPaginateTypeDef,
    GetInstancesResultTypeDef,
    GetKeyPairsRequestPaginateTypeDef,
    GetKeyPairsResultTypeDef,
    GetLoadBalancersRequestPaginateTypeDef,
    GetLoadBalancersResultTypeDef,
    GetOperationsRequestPaginateTypeDef,
    GetOperationsResultTypeDef,
    GetRelationalDatabaseBlueprintsRequestPaginateTypeDef,
    GetRelationalDatabaseBlueprintsResultTypeDef,
    GetRelationalDatabaseBundlesRequestPaginateTypeDef,
    GetRelationalDatabaseBundlesResultTypeDef,
    GetRelationalDatabaseEventsRequestPaginateTypeDef,
    GetRelationalDatabaseEventsResultTypeDef,
    GetRelationalDatabaseParametersRequestPaginateTypeDef,
    GetRelationalDatabaseParametersResultTypeDef,
    GetRelationalDatabaseSnapshotsRequestPaginateTypeDef,
    GetRelationalDatabaseSnapshotsResultTypeDef,
    GetRelationalDatabasesRequestPaginateTypeDef,
    GetRelationalDatabasesResultTypeDef,
    GetStaticIpsRequestPaginateTypeDef,
    GetStaticIpsResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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

if TYPE_CHECKING:
    _GetActiveNamesPaginatorBase = Paginator[GetActiveNamesResultTypeDef]
else:
    _GetActiveNamesPaginatorBase = Paginator  # type: ignore[assignment]

class GetActiveNamesPaginator(_GetActiveNamesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetActiveNames.html#Lightsail.Paginator.GetActiveNames)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getactivenamespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetActiveNamesRequestPaginateTypeDef]
    ) -> PageIterator[GetActiveNamesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetActiveNames.html#Lightsail.Paginator.GetActiveNames.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getactivenamespaginator)
        """

if TYPE_CHECKING:
    _GetBlueprintsPaginatorBase = Paginator[GetBlueprintsResultTypeDef]
else:
    _GetBlueprintsPaginatorBase = Paginator  # type: ignore[assignment]

class GetBlueprintsPaginator(_GetBlueprintsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetBlueprints.html#Lightsail.Paginator.GetBlueprints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getblueprintspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetBlueprintsRequestPaginateTypeDef]
    ) -> PageIterator[GetBlueprintsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetBlueprints.html#Lightsail.Paginator.GetBlueprints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getblueprintspaginator)
        """

if TYPE_CHECKING:
    _GetBundlesPaginatorBase = Paginator[GetBundlesResultTypeDef]
else:
    _GetBundlesPaginatorBase = Paginator  # type: ignore[assignment]

class GetBundlesPaginator(_GetBundlesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetBundles.html#Lightsail.Paginator.GetBundles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getbundlespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetBundlesRequestPaginateTypeDef]
    ) -> PageIterator[GetBundlesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetBundles.html#Lightsail.Paginator.GetBundles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getbundlespaginator)
        """

if TYPE_CHECKING:
    _GetCloudFormationStackRecordsPaginatorBase = Paginator[
        GetCloudFormationStackRecordsResultTypeDef
    ]
else:
    _GetCloudFormationStackRecordsPaginatorBase = Paginator  # type: ignore[assignment]

class GetCloudFormationStackRecordsPaginator(_GetCloudFormationStackRecordsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetCloudFormationStackRecords.html#Lightsail.Paginator.GetCloudFormationStackRecords)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getcloudformationstackrecordspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetCloudFormationStackRecordsRequestPaginateTypeDef]
    ) -> PageIterator[GetCloudFormationStackRecordsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetCloudFormationStackRecords.html#Lightsail.Paginator.GetCloudFormationStackRecords.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getcloudformationstackrecordspaginator)
        """

if TYPE_CHECKING:
    _GetDiskSnapshotsPaginatorBase = Paginator[GetDiskSnapshotsResultTypeDef]
else:
    _GetDiskSnapshotsPaginatorBase = Paginator  # type: ignore[assignment]

class GetDiskSnapshotsPaginator(_GetDiskSnapshotsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetDiskSnapshots.html#Lightsail.Paginator.GetDiskSnapshots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getdisksnapshotspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetDiskSnapshotsRequestPaginateTypeDef]
    ) -> PageIterator[GetDiskSnapshotsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetDiskSnapshots.html#Lightsail.Paginator.GetDiskSnapshots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getdisksnapshotspaginator)
        """

if TYPE_CHECKING:
    _GetDisksPaginatorBase = Paginator[GetDisksResultTypeDef]
else:
    _GetDisksPaginatorBase = Paginator  # type: ignore[assignment]

class GetDisksPaginator(_GetDisksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetDisks.html#Lightsail.Paginator.GetDisks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getdiskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetDisksRequestPaginateTypeDef]
    ) -> PageIterator[GetDisksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetDisks.html#Lightsail.Paginator.GetDisks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getdiskspaginator)
        """

if TYPE_CHECKING:
    _GetDomainsPaginatorBase = Paginator[GetDomainsResultTypeDef]
else:
    _GetDomainsPaginatorBase = Paginator  # type: ignore[assignment]

class GetDomainsPaginator(_GetDomainsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetDomains.html#Lightsail.Paginator.GetDomains)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getdomainspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetDomainsRequestPaginateTypeDef]
    ) -> PageIterator[GetDomainsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetDomains.html#Lightsail.Paginator.GetDomains.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getdomainspaginator)
        """

if TYPE_CHECKING:
    _GetExportSnapshotRecordsPaginatorBase = Paginator[GetExportSnapshotRecordsResultTypeDef]
else:
    _GetExportSnapshotRecordsPaginatorBase = Paginator  # type: ignore[assignment]

class GetExportSnapshotRecordsPaginator(_GetExportSnapshotRecordsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetExportSnapshotRecords.html#Lightsail.Paginator.GetExportSnapshotRecords)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getexportsnapshotrecordspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetExportSnapshotRecordsRequestPaginateTypeDef]
    ) -> PageIterator[GetExportSnapshotRecordsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetExportSnapshotRecords.html#Lightsail.Paginator.GetExportSnapshotRecords.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getexportsnapshotrecordspaginator)
        """

if TYPE_CHECKING:
    _GetInstanceSnapshotsPaginatorBase = Paginator[GetInstanceSnapshotsResultTypeDef]
else:
    _GetInstanceSnapshotsPaginatorBase = Paginator  # type: ignore[assignment]

class GetInstanceSnapshotsPaginator(_GetInstanceSnapshotsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetInstanceSnapshots.html#Lightsail.Paginator.GetInstanceSnapshots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getinstancesnapshotspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetInstanceSnapshotsRequestPaginateTypeDef]
    ) -> PageIterator[GetInstanceSnapshotsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetInstanceSnapshots.html#Lightsail.Paginator.GetInstanceSnapshots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getinstancesnapshotspaginator)
        """

if TYPE_CHECKING:
    _GetInstancesPaginatorBase = Paginator[GetInstancesResultTypeDef]
else:
    _GetInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class GetInstancesPaginator(_GetInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetInstances.html#Lightsail.Paginator.GetInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetInstancesRequestPaginateTypeDef]
    ) -> PageIterator[GetInstancesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetInstances.html#Lightsail.Paginator.GetInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getinstancespaginator)
        """

if TYPE_CHECKING:
    _GetKeyPairsPaginatorBase = Paginator[GetKeyPairsResultTypeDef]
else:
    _GetKeyPairsPaginatorBase = Paginator  # type: ignore[assignment]

class GetKeyPairsPaginator(_GetKeyPairsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetKeyPairs.html#Lightsail.Paginator.GetKeyPairs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getkeypairspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetKeyPairsRequestPaginateTypeDef]
    ) -> PageIterator[GetKeyPairsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetKeyPairs.html#Lightsail.Paginator.GetKeyPairs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getkeypairspaginator)
        """

if TYPE_CHECKING:
    _GetLoadBalancersPaginatorBase = Paginator[GetLoadBalancersResultTypeDef]
else:
    _GetLoadBalancersPaginatorBase = Paginator  # type: ignore[assignment]

class GetLoadBalancersPaginator(_GetLoadBalancersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetLoadBalancers.html#Lightsail.Paginator.GetLoadBalancers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getloadbalancerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetLoadBalancersRequestPaginateTypeDef]
    ) -> PageIterator[GetLoadBalancersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetLoadBalancers.html#Lightsail.Paginator.GetLoadBalancers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getloadbalancerspaginator)
        """

if TYPE_CHECKING:
    _GetOperationsPaginatorBase = Paginator[GetOperationsResultTypeDef]
else:
    _GetOperationsPaginatorBase = Paginator  # type: ignore[assignment]

class GetOperationsPaginator(_GetOperationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetOperations.html#Lightsail.Paginator.GetOperations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getoperationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetOperationsRequestPaginateTypeDef]
    ) -> PageIterator[GetOperationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetOperations.html#Lightsail.Paginator.GetOperations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getoperationspaginator)
        """

if TYPE_CHECKING:
    _GetRelationalDatabaseBlueprintsPaginatorBase = Paginator[
        GetRelationalDatabaseBlueprintsResultTypeDef
    ]
else:
    _GetRelationalDatabaseBlueprintsPaginatorBase = Paginator  # type: ignore[assignment]

class GetRelationalDatabaseBlueprintsPaginator(_GetRelationalDatabaseBlueprintsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetRelationalDatabaseBlueprints.html#Lightsail.Paginator.GetRelationalDatabaseBlueprints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getrelationaldatabaseblueprintspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetRelationalDatabaseBlueprintsRequestPaginateTypeDef]
    ) -> PageIterator[GetRelationalDatabaseBlueprintsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetRelationalDatabaseBlueprints.html#Lightsail.Paginator.GetRelationalDatabaseBlueprints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getrelationaldatabaseblueprintspaginator)
        """

if TYPE_CHECKING:
    _GetRelationalDatabaseBundlesPaginatorBase = Paginator[
        GetRelationalDatabaseBundlesResultTypeDef
    ]
else:
    _GetRelationalDatabaseBundlesPaginatorBase = Paginator  # type: ignore[assignment]

class GetRelationalDatabaseBundlesPaginator(_GetRelationalDatabaseBundlesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetRelationalDatabaseBundles.html#Lightsail.Paginator.GetRelationalDatabaseBundles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getrelationaldatabasebundlespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetRelationalDatabaseBundlesRequestPaginateTypeDef]
    ) -> PageIterator[GetRelationalDatabaseBundlesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetRelationalDatabaseBundles.html#Lightsail.Paginator.GetRelationalDatabaseBundles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getrelationaldatabasebundlespaginator)
        """

if TYPE_CHECKING:
    _GetRelationalDatabaseEventsPaginatorBase = Paginator[GetRelationalDatabaseEventsResultTypeDef]
else:
    _GetRelationalDatabaseEventsPaginatorBase = Paginator  # type: ignore[assignment]

class GetRelationalDatabaseEventsPaginator(_GetRelationalDatabaseEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetRelationalDatabaseEvents.html#Lightsail.Paginator.GetRelationalDatabaseEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getrelationaldatabaseeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetRelationalDatabaseEventsRequestPaginateTypeDef]
    ) -> PageIterator[GetRelationalDatabaseEventsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetRelationalDatabaseEvents.html#Lightsail.Paginator.GetRelationalDatabaseEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getrelationaldatabaseeventspaginator)
        """

if TYPE_CHECKING:
    _GetRelationalDatabaseParametersPaginatorBase = Paginator[
        GetRelationalDatabaseParametersResultTypeDef
    ]
else:
    _GetRelationalDatabaseParametersPaginatorBase = Paginator  # type: ignore[assignment]

class GetRelationalDatabaseParametersPaginator(_GetRelationalDatabaseParametersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetRelationalDatabaseParameters.html#Lightsail.Paginator.GetRelationalDatabaseParameters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getrelationaldatabaseparameterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetRelationalDatabaseParametersRequestPaginateTypeDef]
    ) -> PageIterator[GetRelationalDatabaseParametersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetRelationalDatabaseParameters.html#Lightsail.Paginator.GetRelationalDatabaseParameters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getrelationaldatabaseparameterspaginator)
        """

if TYPE_CHECKING:
    _GetRelationalDatabaseSnapshotsPaginatorBase = Paginator[
        GetRelationalDatabaseSnapshotsResultTypeDef
    ]
else:
    _GetRelationalDatabaseSnapshotsPaginatorBase = Paginator  # type: ignore[assignment]

class GetRelationalDatabaseSnapshotsPaginator(_GetRelationalDatabaseSnapshotsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetRelationalDatabaseSnapshots.html#Lightsail.Paginator.GetRelationalDatabaseSnapshots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getrelationaldatabasesnapshotspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetRelationalDatabaseSnapshotsRequestPaginateTypeDef]
    ) -> PageIterator[GetRelationalDatabaseSnapshotsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetRelationalDatabaseSnapshots.html#Lightsail.Paginator.GetRelationalDatabaseSnapshots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getrelationaldatabasesnapshotspaginator)
        """

if TYPE_CHECKING:
    _GetRelationalDatabasesPaginatorBase = Paginator[GetRelationalDatabasesResultTypeDef]
else:
    _GetRelationalDatabasesPaginatorBase = Paginator  # type: ignore[assignment]

class GetRelationalDatabasesPaginator(_GetRelationalDatabasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetRelationalDatabases.html#Lightsail.Paginator.GetRelationalDatabases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getrelationaldatabasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetRelationalDatabasesRequestPaginateTypeDef]
    ) -> PageIterator[GetRelationalDatabasesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetRelationalDatabases.html#Lightsail.Paginator.GetRelationalDatabases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getrelationaldatabasespaginator)
        """

if TYPE_CHECKING:
    _GetStaticIpsPaginatorBase = Paginator[GetStaticIpsResultTypeDef]
else:
    _GetStaticIpsPaginatorBase = Paginator  # type: ignore[assignment]

class GetStaticIpsPaginator(_GetStaticIpsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetStaticIps.html#Lightsail.Paginator.GetStaticIps)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getstaticipspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetStaticIpsRequestPaginateTypeDef]
    ) -> PageIterator[GetStaticIpsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail/paginator/GetStaticIps.html#Lightsail.Paginator.GetStaticIps.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators/#getstaticipspaginator)
        """
