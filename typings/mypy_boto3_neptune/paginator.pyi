"""
Type annotations for neptune service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_neptune.client import NeptuneClient
    from mypy_boto3_neptune.paginator import (
        DescribeDBClusterEndpointsPaginator,
        DescribeDBClusterParameterGroupsPaginator,
        DescribeDBClusterParametersPaginator,
        DescribeDBClusterSnapshotsPaginator,
        DescribeDBClustersPaginator,
        DescribeDBEngineVersionsPaginator,
        DescribeDBInstancesPaginator,
        DescribeDBParameterGroupsPaginator,
        DescribeDBParametersPaginator,
        DescribeDBSubnetGroupsPaginator,
        DescribeEngineDefaultParametersPaginator,
        DescribeEventSubscriptionsPaginator,
        DescribeEventsPaginator,
        DescribeGlobalClustersPaginator,
        DescribeOrderableDBInstanceOptionsPaginator,
        DescribePendingMaintenanceActionsPaginator,
    )

    session = Session()
    client: NeptuneClient = session.client("neptune")

    describe_db_cluster_endpoints_paginator: DescribeDBClusterEndpointsPaginator = client.get_paginator("describe_db_cluster_endpoints")
    describe_db_cluster_parameter_groups_paginator: DescribeDBClusterParameterGroupsPaginator = client.get_paginator("describe_db_cluster_parameter_groups")
    describe_db_cluster_parameters_paginator: DescribeDBClusterParametersPaginator = client.get_paginator("describe_db_cluster_parameters")
    describe_db_cluster_snapshots_paginator: DescribeDBClusterSnapshotsPaginator = client.get_paginator("describe_db_cluster_snapshots")
    describe_db_clusters_paginator: DescribeDBClustersPaginator = client.get_paginator("describe_db_clusters")
    describe_db_engine_versions_paginator: DescribeDBEngineVersionsPaginator = client.get_paginator("describe_db_engine_versions")
    describe_db_instances_paginator: DescribeDBInstancesPaginator = client.get_paginator("describe_db_instances")
    describe_db_parameter_groups_paginator: DescribeDBParameterGroupsPaginator = client.get_paginator("describe_db_parameter_groups")
    describe_db_parameters_paginator: DescribeDBParametersPaginator = client.get_paginator("describe_db_parameters")
    describe_db_subnet_groups_paginator: DescribeDBSubnetGroupsPaginator = client.get_paginator("describe_db_subnet_groups")
    describe_engine_default_parameters_paginator: DescribeEngineDefaultParametersPaginator = client.get_paginator("describe_engine_default_parameters")
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
    DBClusterEndpointMessageTypeDef,
    DBClusterMessageTypeDef,
    DBClusterParameterGroupDetailsTypeDef,
    DBClusterParameterGroupsMessageTypeDef,
    DBClusterSnapshotMessageTypeDef,
    DBEngineVersionMessageTypeDef,
    DBInstanceMessageTypeDef,
    DBParameterGroupDetailsTypeDef,
    DBParameterGroupsMessageTypeDef,
    DBSubnetGroupMessageTypeDef,
    DescribeDBClusterEndpointsMessagePaginateTypeDef,
    DescribeDBClusterParameterGroupsMessagePaginateTypeDef,
    DescribeDBClusterParametersMessagePaginateTypeDef,
    DescribeDBClustersMessagePaginateTypeDef,
    DescribeDBClusterSnapshotsMessagePaginateTypeDef,
    DescribeDBEngineVersionsMessagePaginateTypeDef,
    DescribeDBInstancesMessagePaginateTypeDef,
    DescribeDBParameterGroupsMessagePaginateTypeDef,
    DescribeDBParametersMessagePaginateTypeDef,
    DescribeDBSubnetGroupsMessagePaginateTypeDef,
    DescribeEngineDefaultParametersMessagePaginateTypeDef,
    DescribeEngineDefaultParametersResultTypeDef,
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
    "DescribeDBClusterEndpointsPaginator",
    "DescribeDBClusterParameterGroupsPaginator",
    "DescribeDBClusterParametersPaginator",
    "DescribeDBClusterSnapshotsPaginator",
    "DescribeDBClustersPaginator",
    "DescribeDBEngineVersionsPaginator",
    "DescribeDBInstancesPaginator",
    "DescribeDBParameterGroupsPaginator",
    "DescribeDBParametersPaginator",
    "DescribeDBSubnetGroupsPaginator",
    "DescribeEngineDefaultParametersPaginator",
    "DescribeEventSubscriptionsPaginator",
    "DescribeEventsPaginator",
    "DescribeGlobalClustersPaginator",
    "DescribeOrderableDBInstanceOptionsPaginator",
    "DescribePendingMaintenanceActionsPaginator",
)

if TYPE_CHECKING:
    _DescribeDBClusterEndpointsPaginatorBase = Paginator[DBClusterEndpointMessageTypeDef]
else:
    _DescribeDBClusterEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBClusterEndpointsPaginator(_DescribeDBClusterEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeDBClusterEndpoints.html#Neptune.Paginator.DescribeDBClusterEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describedbclusterendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBClusterEndpointsMessagePaginateTypeDef]
    ) -> PageIterator[DBClusterEndpointMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeDBClusterEndpoints.html#Neptune.Paginator.DescribeDBClusterEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describedbclusterendpointspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBClusterParameterGroupsPaginatorBase = Paginator[
        DBClusterParameterGroupsMessageTypeDef
    ]
else:
    _DescribeDBClusterParameterGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBClusterParameterGroupsPaginator(_DescribeDBClusterParameterGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeDBClusterParameterGroups.html#Neptune.Paginator.DescribeDBClusterParameterGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describedbclusterparametergroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBClusterParameterGroupsMessagePaginateTypeDef]
    ) -> PageIterator[DBClusterParameterGroupsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeDBClusterParameterGroups.html#Neptune.Paginator.DescribeDBClusterParameterGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describedbclusterparametergroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBClusterParametersPaginatorBase = Paginator[DBClusterParameterGroupDetailsTypeDef]
else:
    _DescribeDBClusterParametersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBClusterParametersPaginator(_DescribeDBClusterParametersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeDBClusterParameters.html#Neptune.Paginator.DescribeDBClusterParameters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describedbclusterparameterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBClusterParametersMessagePaginateTypeDef]
    ) -> PageIterator[DBClusterParameterGroupDetailsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeDBClusterParameters.html#Neptune.Paginator.DescribeDBClusterParameters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describedbclusterparameterspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBClusterSnapshotsPaginatorBase = Paginator[DBClusterSnapshotMessageTypeDef]
else:
    _DescribeDBClusterSnapshotsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBClusterSnapshotsPaginator(_DescribeDBClusterSnapshotsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeDBClusterSnapshots.html#Neptune.Paginator.DescribeDBClusterSnapshots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describedbclustersnapshotspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBClusterSnapshotsMessagePaginateTypeDef]
    ) -> PageIterator[DBClusterSnapshotMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeDBClusterSnapshots.html#Neptune.Paginator.DescribeDBClusterSnapshots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describedbclustersnapshotspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBClustersPaginatorBase = Paginator[DBClusterMessageTypeDef]
else:
    _DescribeDBClustersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBClustersPaginator(_DescribeDBClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeDBClusters.html#Neptune.Paginator.DescribeDBClusters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describedbclusterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBClustersMessagePaginateTypeDef]
    ) -> PageIterator[DBClusterMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeDBClusters.html#Neptune.Paginator.DescribeDBClusters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describedbclusterspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBEngineVersionsPaginatorBase = Paginator[DBEngineVersionMessageTypeDef]
else:
    _DescribeDBEngineVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBEngineVersionsPaginator(_DescribeDBEngineVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeDBEngineVersions.html#Neptune.Paginator.DescribeDBEngineVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describedbengineversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBEngineVersionsMessagePaginateTypeDef]
    ) -> PageIterator[DBEngineVersionMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeDBEngineVersions.html#Neptune.Paginator.DescribeDBEngineVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describedbengineversionspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBInstancesPaginatorBase = Paginator[DBInstanceMessageTypeDef]
else:
    _DescribeDBInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBInstancesPaginator(_DescribeDBInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeDBInstances.html#Neptune.Paginator.DescribeDBInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describedbinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBInstancesMessagePaginateTypeDef]
    ) -> PageIterator[DBInstanceMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeDBInstances.html#Neptune.Paginator.DescribeDBInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describedbinstancespaginator)
        """

if TYPE_CHECKING:
    _DescribeDBParameterGroupsPaginatorBase = Paginator[DBParameterGroupsMessageTypeDef]
else:
    _DescribeDBParameterGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBParameterGroupsPaginator(_DescribeDBParameterGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeDBParameterGroups.html#Neptune.Paginator.DescribeDBParameterGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describedbparametergroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBParameterGroupsMessagePaginateTypeDef]
    ) -> PageIterator[DBParameterGroupsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeDBParameterGroups.html#Neptune.Paginator.DescribeDBParameterGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describedbparametergroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBParametersPaginatorBase = Paginator[DBParameterGroupDetailsTypeDef]
else:
    _DescribeDBParametersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBParametersPaginator(_DescribeDBParametersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeDBParameters.html#Neptune.Paginator.DescribeDBParameters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describedbparameterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBParametersMessagePaginateTypeDef]
    ) -> PageIterator[DBParameterGroupDetailsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeDBParameters.html#Neptune.Paginator.DescribeDBParameters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describedbparameterspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBSubnetGroupsPaginatorBase = Paginator[DBSubnetGroupMessageTypeDef]
else:
    _DescribeDBSubnetGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBSubnetGroupsPaginator(_DescribeDBSubnetGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeDBSubnetGroups.html#Neptune.Paginator.DescribeDBSubnetGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describedbsubnetgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBSubnetGroupsMessagePaginateTypeDef]
    ) -> PageIterator[DBSubnetGroupMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeDBSubnetGroups.html#Neptune.Paginator.DescribeDBSubnetGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describedbsubnetgroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeEngineDefaultParametersPaginatorBase = Paginator[
        DescribeEngineDefaultParametersResultTypeDef
    ]
else:
    _DescribeEngineDefaultParametersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEngineDefaultParametersPaginator(_DescribeEngineDefaultParametersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeEngineDefaultParameters.html#Neptune.Paginator.DescribeEngineDefaultParameters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describeenginedefaultparameterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEngineDefaultParametersMessagePaginateTypeDef]
    ) -> PageIterator[DescribeEngineDefaultParametersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeEngineDefaultParameters.html#Neptune.Paginator.DescribeEngineDefaultParameters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describeenginedefaultparameterspaginator)
        """

if TYPE_CHECKING:
    _DescribeEventSubscriptionsPaginatorBase = Paginator[EventSubscriptionsMessageTypeDef]
else:
    _DescribeEventSubscriptionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEventSubscriptionsPaginator(_DescribeEventSubscriptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeEventSubscriptions.html#Neptune.Paginator.DescribeEventSubscriptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describeeventsubscriptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEventSubscriptionsMessagePaginateTypeDef]
    ) -> PageIterator[EventSubscriptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeEventSubscriptions.html#Neptune.Paginator.DescribeEventSubscriptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describeeventsubscriptionspaginator)
        """

if TYPE_CHECKING:
    _DescribeEventsPaginatorBase = Paginator[EventsMessageTypeDef]
else:
    _DescribeEventsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEventsPaginator(_DescribeEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeEvents.html#Neptune.Paginator.DescribeEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describeeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEventsMessagePaginateTypeDef]
    ) -> PageIterator[EventsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeEvents.html#Neptune.Paginator.DescribeEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describeeventspaginator)
        """

if TYPE_CHECKING:
    _DescribeGlobalClustersPaginatorBase = Paginator[GlobalClustersMessageTypeDef]
else:
    _DescribeGlobalClustersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeGlobalClustersPaginator(_DescribeGlobalClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeGlobalClusters.html#Neptune.Paginator.DescribeGlobalClusters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describeglobalclusterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeGlobalClustersMessagePaginateTypeDef]
    ) -> PageIterator[GlobalClustersMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeGlobalClusters.html#Neptune.Paginator.DescribeGlobalClusters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describeglobalclusterspaginator)
        """

if TYPE_CHECKING:
    _DescribeOrderableDBInstanceOptionsPaginatorBase = Paginator[
        OrderableDBInstanceOptionsMessageTypeDef
    ]
else:
    _DescribeOrderableDBInstanceOptionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeOrderableDBInstanceOptionsPaginator(_DescribeOrderableDBInstanceOptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeOrderableDBInstanceOptions.html#Neptune.Paginator.DescribeOrderableDBInstanceOptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describeorderabledbinstanceoptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeOrderableDBInstanceOptionsMessagePaginateTypeDef]
    ) -> PageIterator[OrderableDBInstanceOptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribeOrderableDBInstanceOptions.html#Neptune.Paginator.DescribeOrderableDBInstanceOptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describeorderabledbinstanceoptionspaginator)
        """

if TYPE_CHECKING:
    _DescribePendingMaintenanceActionsPaginatorBase = Paginator[
        PendingMaintenanceActionsMessageTypeDef
    ]
else:
    _DescribePendingMaintenanceActionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribePendingMaintenanceActionsPaginator(_DescribePendingMaintenanceActionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribePendingMaintenanceActions.html#Neptune.Paginator.DescribePendingMaintenanceActions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describependingmaintenanceactionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribePendingMaintenanceActionsMessagePaginateTypeDef]
    ) -> PageIterator[PendingMaintenanceActionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune/paginator/DescribePendingMaintenanceActions.html#Neptune.Paginator.DescribePendingMaintenanceActions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators/#describependingmaintenanceactionspaginator)
        """
