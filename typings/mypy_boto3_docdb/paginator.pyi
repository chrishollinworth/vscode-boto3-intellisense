"""
Type annotations for docdb service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_docdb.client import DocDBClient
    from mypy_boto3_docdb.paginator import (
        DescribeCertificatesPaginator,
        DescribeDBClusterParameterGroupsPaginator,
        DescribeDBClusterParametersPaginator,
        DescribeDBClusterSnapshotsPaginator,
        DescribeDBClustersPaginator,
        DescribeDBEngineVersionsPaginator,
        DescribeDBInstancesPaginator,
        DescribeDBSubnetGroupsPaginator,
        DescribeEventSubscriptionsPaginator,
        DescribeEventsPaginator,
        DescribeGlobalClustersPaginator,
        DescribeOrderableDBInstanceOptionsPaginator,
        DescribePendingMaintenanceActionsPaginator,
    )

    session = Session()
    client: DocDBClient = session.client("docdb")

    describe_certificates_paginator: DescribeCertificatesPaginator = client.get_paginator("describe_certificates")
    describe_db_cluster_parameter_groups_paginator: DescribeDBClusterParameterGroupsPaginator = client.get_paginator("describe_db_cluster_parameter_groups")
    describe_db_cluster_parameters_paginator: DescribeDBClusterParametersPaginator = client.get_paginator("describe_db_cluster_parameters")
    describe_db_cluster_snapshots_paginator: DescribeDBClusterSnapshotsPaginator = client.get_paginator("describe_db_cluster_snapshots")
    describe_db_clusters_paginator: DescribeDBClustersPaginator = client.get_paginator("describe_db_clusters")
    describe_db_engine_versions_paginator: DescribeDBEngineVersionsPaginator = client.get_paginator("describe_db_engine_versions")
    describe_db_instances_paginator: DescribeDBInstancesPaginator = client.get_paginator("describe_db_instances")
    describe_db_subnet_groups_paginator: DescribeDBSubnetGroupsPaginator = client.get_paginator("describe_db_subnet_groups")
    describe_event_subscriptions_paginator: DescribeEventSubscriptionsPaginator = client.get_paginator("describe_event_subscriptions")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_global_clusters_paginator: DescribeGlobalClustersPaginator = client.get_paginator("describe_global_clusters")
    describe_orderable_db_instance_options_paginator: DescribeOrderableDBInstanceOptionsPaginator = client.get_paginator("describe_orderable_db_instance_options")
    describe_pending_maintenance_actions_paginator: DescribePendingMaintenanceActionsPaginator = client.get_paginator("describe_pending_maintenance_actions")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    CertificateMessageTypeDef,
    DBClusterMessageTypeDef,
    DBClusterParameterGroupDetailsTypeDef,
    DBClusterParameterGroupsMessageTypeDef,
    DBClusterSnapshotMessageTypeDef,
    DBEngineVersionMessageTypeDef,
    DBInstanceMessageTypeDef,
    DBSubnetGroupMessageTypeDef,
    DescribeCertificatesMessagePaginateTypeDef,
    DescribeDBClusterParameterGroupsMessagePaginateTypeDef,
    DescribeDBClusterParametersMessagePaginateTypeDef,
    DescribeDBClustersMessagePaginateTypeDef,
    DescribeDBClusterSnapshotsMessagePaginateTypeDef,
    DescribeDBEngineVersionsMessagePaginateTypeDef,
    DescribeDBInstancesMessagePaginateTypeDef,
    DescribeDBSubnetGroupsMessagePaginateTypeDef,
    DescribeEventsMessagePaginateTypeDef,
    DescribeEventSubscriptionsMessagePaginateTypeDef,
    DescribeGlobalClustersMessagePaginateTypeDef,
    DescribeOrderableDBInstanceOptionsMessagePaginateTypeDef,
    DescribePendingMaintenanceActionsMessagePaginateTypeDef,
    EventsMessageTypeDef,
    EventSubscriptionsMessageTypeDef,
    GlobalClustersMessageTypeDef,
    OrderableDBInstanceOptionsMessageTypeDef,
    PendingMaintenanceActionsMessageTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeCertificatesPaginator",
    "DescribeDBClusterParameterGroupsPaginator",
    "DescribeDBClusterParametersPaginator",
    "DescribeDBClusterSnapshotsPaginator",
    "DescribeDBClustersPaginator",
    "DescribeDBEngineVersionsPaginator",
    "DescribeDBInstancesPaginator",
    "DescribeDBSubnetGroupsPaginator",
    "DescribeEventSubscriptionsPaginator",
    "DescribeEventsPaginator",
    "DescribeGlobalClustersPaginator",
    "DescribeOrderableDBInstanceOptionsPaginator",
    "DescribePendingMaintenanceActionsPaginator",
)

if TYPE_CHECKING:
    _DescribeCertificatesPaginatorBase = Paginator[CertificateMessageTypeDef]
else:
    _DescribeCertificatesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeCertificatesPaginator(_DescribeCertificatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeCertificates.html#DocDB.Paginator.DescribeCertificates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describecertificatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCertificatesMessagePaginateTypeDef]
    ) -> PageIterator[CertificateMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeCertificates.html#DocDB.Paginator.DescribeCertificates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describecertificatespaginator)
        """

if TYPE_CHECKING:
    _DescribeDBClusterParameterGroupsPaginatorBase = Paginator[
        DBClusterParameterGroupsMessageTypeDef
    ]
else:
    _DescribeDBClusterParameterGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBClusterParameterGroupsPaginator(_DescribeDBClusterParameterGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeDBClusterParameterGroups.html#DocDB.Paginator.DescribeDBClusterParameterGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describedbclusterparametergroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBClusterParameterGroupsMessagePaginateTypeDef]
    ) -> PageIterator[DBClusterParameterGroupsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeDBClusterParameterGroups.html#DocDB.Paginator.DescribeDBClusterParameterGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describedbclusterparametergroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBClusterParametersPaginatorBase = Paginator[DBClusterParameterGroupDetailsTypeDef]
else:
    _DescribeDBClusterParametersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBClusterParametersPaginator(_DescribeDBClusterParametersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeDBClusterParameters.html#DocDB.Paginator.DescribeDBClusterParameters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describedbclusterparameterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBClusterParametersMessagePaginateTypeDef]
    ) -> PageIterator[DBClusterParameterGroupDetailsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeDBClusterParameters.html#DocDB.Paginator.DescribeDBClusterParameters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describedbclusterparameterspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBClusterSnapshotsPaginatorBase = Paginator[DBClusterSnapshotMessageTypeDef]
else:
    _DescribeDBClusterSnapshotsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBClusterSnapshotsPaginator(_DescribeDBClusterSnapshotsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeDBClusterSnapshots.html#DocDB.Paginator.DescribeDBClusterSnapshots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describedbclustersnapshotspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBClusterSnapshotsMessagePaginateTypeDef]
    ) -> PageIterator[DBClusterSnapshotMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeDBClusterSnapshots.html#DocDB.Paginator.DescribeDBClusterSnapshots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describedbclustersnapshotspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBClustersPaginatorBase = Paginator[DBClusterMessageTypeDef]
else:
    _DescribeDBClustersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBClustersPaginator(_DescribeDBClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeDBClusters.html#DocDB.Paginator.DescribeDBClusters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describedbclusterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBClustersMessagePaginateTypeDef]
    ) -> PageIterator[DBClusterMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeDBClusters.html#DocDB.Paginator.DescribeDBClusters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describedbclusterspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBEngineVersionsPaginatorBase = Paginator[DBEngineVersionMessageTypeDef]
else:
    _DescribeDBEngineVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBEngineVersionsPaginator(_DescribeDBEngineVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeDBEngineVersions.html#DocDB.Paginator.DescribeDBEngineVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describedbengineversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBEngineVersionsMessagePaginateTypeDef]
    ) -> PageIterator[DBEngineVersionMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeDBEngineVersions.html#DocDB.Paginator.DescribeDBEngineVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describedbengineversionspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBInstancesPaginatorBase = Paginator[DBInstanceMessageTypeDef]
else:
    _DescribeDBInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBInstancesPaginator(_DescribeDBInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeDBInstances.html#DocDB.Paginator.DescribeDBInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describedbinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBInstancesMessagePaginateTypeDef]
    ) -> PageIterator[DBInstanceMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeDBInstances.html#DocDB.Paginator.DescribeDBInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describedbinstancespaginator)
        """

if TYPE_CHECKING:
    _DescribeDBSubnetGroupsPaginatorBase = Paginator[DBSubnetGroupMessageTypeDef]
else:
    _DescribeDBSubnetGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBSubnetGroupsPaginator(_DescribeDBSubnetGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeDBSubnetGroups.html#DocDB.Paginator.DescribeDBSubnetGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describedbsubnetgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBSubnetGroupsMessagePaginateTypeDef]
    ) -> PageIterator[DBSubnetGroupMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeDBSubnetGroups.html#DocDB.Paginator.DescribeDBSubnetGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describedbsubnetgroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeEventSubscriptionsPaginatorBase = Paginator[EventSubscriptionsMessageTypeDef]
else:
    _DescribeEventSubscriptionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEventSubscriptionsPaginator(_DescribeEventSubscriptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeEventSubscriptions.html#DocDB.Paginator.DescribeEventSubscriptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describeeventsubscriptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEventSubscriptionsMessagePaginateTypeDef]
    ) -> PageIterator[EventSubscriptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeEventSubscriptions.html#DocDB.Paginator.DescribeEventSubscriptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describeeventsubscriptionspaginator)
        """

if TYPE_CHECKING:
    _DescribeEventsPaginatorBase = Paginator[EventsMessageTypeDef]
else:
    _DescribeEventsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEventsPaginator(_DescribeEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeEvents.html#DocDB.Paginator.DescribeEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describeeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEventsMessagePaginateTypeDef]
    ) -> PageIterator[EventsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeEvents.html#DocDB.Paginator.DescribeEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describeeventspaginator)
        """

if TYPE_CHECKING:
    _DescribeGlobalClustersPaginatorBase = Paginator[GlobalClustersMessageTypeDef]
else:
    _DescribeGlobalClustersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeGlobalClustersPaginator(_DescribeGlobalClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeGlobalClusters.html#DocDB.Paginator.DescribeGlobalClusters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describeglobalclusterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeGlobalClustersMessagePaginateTypeDef]
    ) -> PageIterator[GlobalClustersMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeGlobalClusters.html#DocDB.Paginator.DescribeGlobalClusters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describeglobalclusterspaginator)
        """

if TYPE_CHECKING:
    _DescribeOrderableDBInstanceOptionsPaginatorBase = Paginator[
        OrderableDBInstanceOptionsMessageTypeDef
    ]
else:
    _DescribeOrderableDBInstanceOptionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeOrderableDBInstanceOptionsPaginator(_DescribeOrderableDBInstanceOptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeOrderableDBInstanceOptions.html#DocDB.Paginator.DescribeOrderableDBInstanceOptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describeorderabledbinstanceoptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeOrderableDBInstanceOptionsMessagePaginateTypeDef]
    ) -> PageIterator[OrderableDBInstanceOptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribeOrderableDBInstanceOptions.html#DocDB.Paginator.DescribeOrderableDBInstanceOptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describeorderabledbinstanceoptionspaginator)
        """

if TYPE_CHECKING:
    _DescribePendingMaintenanceActionsPaginatorBase = Paginator[
        PendingMaintenanceActionsMessageTypeDef
    ]
else:
    _DescribePendingMaintenanceActionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribePendingMaintenanceActionsPaginator(_DescribePendingMaintenanceActionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribePendingMaintenanceActions.html#DocDB.Paginator.DescribePendingMaintenanceActions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describependingmaintenanceactionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribePendingMaintenanceActionsMessagePaginateTypeDef]
    ) -> PageIterator[PendingMaintenanceActionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb/paginator/DescribePendingMaintenanceActions.html#DocDB.Paginator.DescribePendingMaintenanceActions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/paginators/#describependingmaintenanceactionspaginator)
        """
