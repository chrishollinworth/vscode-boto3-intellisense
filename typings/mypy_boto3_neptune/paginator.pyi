"""
Type annotations for neptune service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_neptune import NeptuneClient
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

    client: NeptuneClient = boto3.client("neptune")

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

from datetime import datetime
from typing import Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import SourceTypeType
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
    DescribeEngineDefaultParametersResultTypeDef,
    EventsMessageTypeDef,
    EventSubscriptionsMessageTypeDef,
    FilterTypeDef,
    GlobalClustersMessageTypeDef,
    OrderableDBInstanceOptionsMessageTypeDef,
    PaginatorConfigTypeDef,
    PendingMaintenanceActionsMessageTypeDef,
)

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

class DescribeDBClusterEndpointsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterEndpoints)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describedbclusterendpointspaginator)
    """

    def paginate(
        self,
        *,
        DBClusterIdentifier: str = None,
        DBClusterEndpointIdentifier: str = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DBClusterEndpointMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterEndpoints.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describedbclusterendpointspaginator)
        """

class DescribeDBClusterParameterGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterParameterGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describedbclusterparametergroupspaginator)
    """

    def paginate(
        self,
        *,
        DBClusterParameterGroupName: str = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DBClusterParameterGroupsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterParameterGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describedbclusterparametergroupspaginator)
        """

class DescribeDBClusterParametersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterParameters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describedbclusterparameterspaginator)
    """

    def paginate(
        self,
        *,
        DBClusterParameterGroupName: str,
        Source: str = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DBClusterParameterGroupDetailsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterParameters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describedbclusterparameterspaginator)
        """

class DescribeDBClusterSnapshotsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterSnapshots)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describedbclustersnapshotspaginator)
    """

    def paginate(
        self,
        *,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List["FilterTypeDef"] = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DBClusterSnapshotMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusterSnapshots.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describedbclustersnapshotspaginator)
        """

class DescribeDBClustersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describedbclusterspaginator)
    """

    def paginate(
        self,
        *,
        DBClusterIdentifier: str = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DBClusterMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeDBClusters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describedbclusterspaginator)
        """

class DescribeDBEngineVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeDBEngineVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describedbengineversionspaginator)
    """

    def paginate(
        self,
        *,
        Engine: str = None,
        EngineVersion: str = None,
        DBParameterGroupFamily: str = None,
        Filters: List["FilterTypeDef"] = None,
        DefaultOnly: bool = None,
        ListSupportedCharacterSets: bool = None,
        ListSupportedTimezones: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DBEngineVersionMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeDBEngineVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describedbengineversionspaginator)
        """

class DescribeDBInstancesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeDBInstances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describedbinstancespaginator)
    """

    def paginate(
        self,
        *,
        DBInstanceIdentifier: str = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DBInstanceMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeDBInstances.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describedbinstancespaginator)
        """

class DescribeDBParameterGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeDBParameterGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describedbparametergroupspaginator)
    """

    def paginate(
        self,
        *,
        DBParameterGroupName: str = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DBParameterGroupsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeDBParameterGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describedbparametergroupspaginator)
        """

class DescribeDBParametersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeDBParameters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describedbparameterspaginator)
    """

    def paginate(
        self,
        *,
        DBParameterGroupName: str,
        Source: str = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DBParameterGroupDetailsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeDBParameters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describedbparameterspaginator)
        """

class DescribeDBSubnetGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeDBSubnetGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describedbsubnetgroupspaginator)
    """

    def paginate(
        self,
        *,
        DBSubnetGroupName: str = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DBSubnetGroupMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeDBSubnetGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describedbsubnetgroupspaginator)
        """

class DescribeEngineDefaultParametersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeEngineDefaultParameters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describeenginedefaultparameterspaginator)
    """

    def paginate(
        self,
        *,
        DBParameterGroupFamily: str,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEngineDefaultParametersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeEngineDefaultParameters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describeenginedefaultparameterspaginator)
        """

class DescribeEventSubscriptionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeEventSubscriptions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describeeventsubscriptionspaginator)
    """

    def paginate(
        self,
        *,
        SubscriptionName: str = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[EventSubscriptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeEventSubscriptions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describeeventsubscriptionspaginator)
        """

class DescribeEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeEvents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describeeventspaginator)
    """

    def paginate(
        self,
        *,
        SourceIdentifier: str = None,
        SourceType: SourceTypeType = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[EventsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeEvents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describeeventspaginator)
        """

class DescribeGlobalClustersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeGlobalClusters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describeglobalclusterspaginator)
    """

    def paginate(
        self,
        *,
        GlobalClusterIdentifier: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GlobalClustersMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeGlobalClusters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describeglobalclusterspaginator)
        """

class DescribeOrderableDBInstanceOptionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeOrderableDBInstanceOptions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describeorderabledbinstanceoptionspaginator)
    """

    def paginate(
        self,
        *,
        Engine: str,
        EngineVersion: str = None,
        DBInstanceClass: str = None,
        LicenseModel: str = None,
        Vpc: bool = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[OrderableDBInstanceOptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribeOrderableDBInstanceOptions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describeorderabledbinstanceoptionspaginator)
        """

class DescribePendingMaintenanceActionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribePendingMaintenanceActions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describependingmaintenanceactionspaginator)
    """

    def paginate(
        self,
        *,
        ResourceIdentifier: str = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[PendingMaintenanceActionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune.html#Neptune.Paginator.DescribePendingMaintenanceActions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/paginators.html#describependingmaintenanceactionspaginator)
        """
