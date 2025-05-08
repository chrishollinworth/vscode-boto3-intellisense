"""
Type annotations for dms service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_dms.client import DatabaseMigrationServiceClient
    from mypy_boto3_dms.paginator import (
        DescribeCertificatesPaginator,
        DescribeConnectionsPaginator,
        DescribeDataMigrationsPaginator,
        DescribeEndpointTypesPaginator,
        DescribeEndpointsPaginator,
        DescribeEventSubscriptionsPaginator,
        DescribeEventsPaginator,
        DescribeOrderableReplicationInstancesPaginator,
        DescribeReplicationInstancesPaginator,
        DescribeReplicationSubnetGroupsPaginator,
        DescribeReplicationTaskAssessmentResultsPaginator,
        DescribeReplicationTasksPaginator,
        DescribeSchemasPaginator,
        DescribeTableStatisticsPaginator,
    )

    session = Session()
    client: DatabaseMigrationServiceClient = session.client("dms")

    describe_certificates_paginator: DescribeCertificatesPaginator = client.get_paginator("describe_certificates")
    describe_connections_paginator: DescribeConnectionsPaginator = client.get_paginator("describe_connections")
    describe_data_migrations_paginator: DescribeDataMigrationsPaginator = client.get_paginator("describe_data_migrations")
    describe_endpoint_types_paginator: DescribeEndpointTypesPaginator = client.get_paginator("describe_endpoint_types")
    describe_endpoints_paginator: DescribeEndpointsPaginator = client.get_paginator("describe_endpoints")
    describe_event_subscriptions_paginator: DescribeEventSubscriptionsPaginator = client.get_paginator("describe_event_subscriptions")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_orderable_replication_instances_paginator: DescribeOrderableReplicationInstancesPaginator = client.get_paginator("describe_orderable_replication_instances")
    describe_replication_instances_paginator: DescribeReplicationInstancesPaginator = client.get_paginator("describe_replication_instances")
    describe_replication_subnet_groups_paginator: DescribeReplicationSubnetGroupsPaginator = client.get_paginator("describe_replication_subnet_groups")
    describe_replication_task_assessment_results_paginator: DescribeReplicationTaskAssessmentResultsPaginator = client.get_paginator("describe_replication_task_assessment_results")
    describe_replication_tasks_paginator: DescribeReplicationTasksPaginator = client.get_paginator("describe_replication_tasks")
    describe_schemas_paginator: DescribeSchemasPaginator = client.get_paginator("describe_schemas")
    describe_table_statistics_paginator: DescribeTableStatisticsPaginator = client.get_paginator("describe_table_statistics")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeCertificatesMessagePaginateTypeDef,
    DescribeCertificatesResponseTypeDef,
    DescribeConnectionsMessagePaginateTypeDef,
    DescribeConnectionsResponseTypeDef,
    DescribeDataMigrationsMessagePaginateTypeDef,
    DescribeDataMigrationsResponseTypeDef,
    DescribeEndpointsMessagePaginateTypeDef,
    DescribeEndpointsResponseTypeDef,
    DescribeEndpointTypesMessagePaginateTypeDef,
    DescribeEndpointTypesResponseTypeDef,
    DescribeEventsMessagePaginateTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeEventSubscriptionsMessagePaginateTypeDef,
    DescribeEventSubscriptionsResponseTypeDef,
    DescribeOrderableReplicationInstancesMessagePaginateTypeDef,
    DescribeOrderableReplicationInstancesResponseTypeDef,
    DescribeReplicationInstancesMessagePaginateTypeDef,
    DescribeReplicationInstancesResponseTypeDef,
    DescribeReplicationSubnetGroupsMessagePaginateTypeDef,
    DescribeReplicationSubnetGroupsResponseTypeDef,
    DescribeReplicationTaskAssessmentResultsMessagePaginateTypeDef,
    DescribeReplicationTaskAssessmentResultsResponseTypeDef,
    DescribeReplicationTasksMessagePaginateTypeDef,
    DescribeReplicationTasksResponseTypeDef,
    DescribeSchemasMessagePaginateTypeDef,
    DescribeSchemasResponseTypeDef,
    DescribeTableStatisticsMessagePaginateTypeDef,
    DescribeTableStatisticsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeCertificatesPaginator",
    "DescribeConnectionsPaginator",
    "DescribeDataMigrationsPaginator",
    "DescribeEndpointTypesPaginator",
    "DescribeEndpointsPaginator",
    "DescribeEventSubscriptionsPaginator",
    "DescribeEventsPaginator",
    "DescribeOrderableReplicationInstancesPaginator",
    "DescribeReplicationInstancesPaginator",
    "DescribeReplicationSubnetGroupsPaginator",
    "DescribeReplicationTaskAssessmentResultsPaginator",
    "DescribeReplicationTasksPaginator",
    "DescribeSchemasPaginator",
    "DescribeTableStatisticsPaginator",
)

if TYPE_CHECKING:
    _DescribeCertificatesPaginatorBase = Paginator[DescribeCertificatesResponseTypeDef]
else:
    _DescribeCertificatesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeCertificatesPaginator(_DescribeCertificatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeCertificates.html#DatabaseMigrationService.Paginator.DescribeCertificates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describecertificatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCertificatesMessagePaginateTypeDef]
    ) -> PageIterator[DescribeCertificatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeCertificates.html#DatabaseMigrationService.Paginator.DescribeCertificates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describecertificatespaginator)
        """

if TYPE_CHECKING:
    _DescribeConnectionsPaginatorBase = Paginator[DescribeConnectionsResponseTypeDef]
else:
    _DescribeConnectionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeConnectionsPaginator(_DescribeConnectionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeConnections.html#DatabaseMigrationService.Paginator.DescribeConnections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describeconnectionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeConnectionsMessagePaginateTypeDef]
    ) -> PageIterator[DescribeConnectionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeConnections.html#DatabaseMigrationService.Paginator.DescribeConnections.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describeconnectionspaginator)
        """

if TYPE_CHECKING:
    _DescribeDataMigrationsPaginatorBase = Paginator[DescribeDataMigrationsResponseTypeDef]
else:
    _DescribeDataMigrationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDataMigrationsPaginator(_DescribeDataMigrationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeDataMigrations.html#DatabaseMigrationService.Paginator.DescribeDataMigrations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describedatamigrationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDataMigrationsMessagePaginateTypeDef]
    ) -> PageIterator[DescribeDataMigrationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeDataMigrations.html#DatabaseMigrationService.Paginator.DescribeDataMigrations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describedatamigrationspaginator)
        """

if TYPE_CHECKING:
    _DescribeEndpointTypesPaginatorBase = Paginator[DescribeEndpointTypesResponseTypeDef]
else:
    _DescribeEndpointTypesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEndpointTypesPaginator(_DescribeEndpointTypesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeEndpointTypes.html#DatabaseMigrationService.Paginator.DescribeEndpointTypes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describeendpointtypespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEndpointTypesMessagePaginateTypeDef]
    ) -> PageIterator[DescribeEndpointTypesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeEndpointTypes.html#DatabaseMigrationService.Paginator.DescribeEndpointTypes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describeendpointtypespaginator)
        """

if TYPE_CHECKING:
    _DescribeEndpointsPaginatorBase = Paginator[DescribeEndpointsResponseTypeDef]
else:
    _DescribeEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEndpointsPaginator(_DescribeEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeEndpoints.html#DatabaseMigrationService.Paginator.DescribeEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describeendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEndpointsMessagePaginateTypeDef]
    ) -> PageIterator[DescribeEndpointsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeEndpoints.html#DatabaseMigrationService.Paginator.DescribeEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describeendpointspaginator)
        """

if TYPE_CHECKING:
    _DescribeEventSubscriptionsPaginatorBase = Paginator[DescribeEventSubscriptionsResponseTypeDef]
else:
    _DescribeEventSubscriptionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEventSubscriptionsPaginator(_DescribeEventSubscriptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeEventSubscriptions.html#DatabaseMigrationService.Paginator.DescribeEventSubscriptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describeeventsubscriptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEventSubscriptionsMessagePaginateTypeDef]
    ) -> PageIterator[DescribeEventSubscriptionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeEventSubscriptions.html#DatabaseMigrationService.Paginator.DescribeEventSubscriptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describeeventsubscriptionspaginator)
        """

if TYPE_CHECKING:
    _DescribeEventsPaginatorBase = Paginator[DescribeEventsResponseTypeDef]
else:
    _DescribeEventsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEventsPaginator(_DescribeEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeEvents.html#DatabaseMigrationService.Paginator.DescribeEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describeeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEventsMessagePaginateTypeDef]
    ) -> PageIterator[DescribeEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeEvents.html#DatabaseMigrationService.Paginator.DescribeEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describeeventspaginator)
        """

if TYPE_CHECKING:
    _DescribeOrderableReplicationInstancesPaginatorBase = Paginator[
        DescribeOrderableReplicationInstancesResponseTypeDef
    ]
else:
    _DescribeOrderableReplicationInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeOrderableReplicationInstancesPaginator(
    _DescribeOrderableReplicationInstancesPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeOrderableReplicationInstances.html#DatabaseMigrationService.Paginator.DescribeOrderableReplicationInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describeorderablereplicationinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeOrderableReplicationInstancesMessagePaginateTypeDef]
    ) -> PageIterator[DescribeOrderableReplicationInstancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeOrderableReplicationInstances.html#DatabaseMigrationService.Paginator.DescribeOrderableReplicationInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describeorderablereplicationinstancespaginator)
        """

if TYPE_CHECKING:
    _DescribeReplicationInstancesPaginatorBase = Paginator[
        DescribeReplicationInstancesResponseTypeDef
    ]
else:
    _DescribeReplicationInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeReplicationInstancesPaginator(_DescribeReplicationInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeReplicationInstances.html#DatabaseMigrationService.Paginator.DescribeReplicationInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describereplicationinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReplicationInstancesMessagePaginateTypeDef]
    ) -> PageIterator[DescribeReplicationInstancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeReplicationInstances.html#DatabaseMigrationService.Paginator.DescribeReplicationInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describereplicationinstancespaginator)
        """

if TYPE_CHECKING:
    _DescribeReplicationSubnetGroupsPaginatorBase = Paginator[
        DescribeReplicationSubnetGroupsResponseTypeDef
    ]
else:
    _DescribeReplicationSubnetGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeReplicationSubnetGroupsPaginator(_DescribeReplicationSubnetGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeReplicationSubnetGroups.html#DatabaseMigrationService.Paginator.DescribeReplicationSubnetGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describereplicationsubnetgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReplicationSubnetGroupsMessagePaginateTypeDef]
    ) -> PageIterator[DescribeReplicationSubnetGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeReplicationSubnetGroups.html#DatabaseMigrationService.Paginator.DescribeReplicationSubnetGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describereplicationsubnetgroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeReplicationTaskAssessmentResultsPaginatorBase = Paginator[
        DescribeReplicationTaskAssessmentResultsResponseTypeDef
    ]
else:
    _DescribeReplicationTaskAssessmentResultsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeReplicationTaskAssessmentResultsPaginator(
    _DescribeReplicationTaskAssessmentResultsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeReplicationTaskAssessmentResults.html#DatabaseMigrationService.Paginator.DescribeReplicationTaskAssessmentResults)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describereplicationtaskassessmentresultspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReplicationTaskAssessmentResultsMessagePaginateTypeDef]
    ) -> PageIterator[DescribeReplicationTaskAssessmentResultsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeReplicationTaskAssessmentResults.html#DatabaseMigrationService.Paginator.DescribeReplicationTaskAssessmentResults.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describereplicationtaskassessmentresultspaginator)
        """

if TYPE_CHECKING:
    _DescribeReplicationTasksPaginatorBase = Paginator[DescribeReplicationTasksResponseTypeDef]
else:
    _DescribeReplicationTasksPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeReplicationTasksPaginator(_DescribeReplicationTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeReplicationTasks.html#DatabaseMigrationService.Paginator.DescribeReplicationTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describereplicationtaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReplicationTasksMessagePaginateTypeDef]
    ) -> PageIterator[DescribeReplicationTasksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeReplicationTasks.html#DatabaseMigrationService.Paginator.DescribeReplicationTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describereplicationtaskspaginator)
        """

if TYPE_CHECKING:
    _DescribeSchemasPaginatorBase = Paginator[DescribeSchemasResponseTypeDef]
else:
    _DescribeSchemasPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSchemasPaginator(_DescribeSchemasPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeSchemas.html#DatabaseMigrationService.Paginator.DescribeSchemas)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describeschemaspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSchemasMessagePaginateTypeDef]
    ) -> PageIterator[DescribeSchemasResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeSchemas.html#DatabaseMigrationService.Paginator.DescribeSchemas.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describeschemaspaginator)
        """

if TYPE_CHECKING:
    _DescribeTableStatisticsPaginatorBase = Paginator[DescribeTableStatisticsResponseTypeDef]
else:
    _DescribeTableStatisticsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTableStatisticsPaginator(_DescribeTableStatisticsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeTableStatistics.html#DatabaseMigrationService.Paginator.DescribeTableStatistics)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describetablestatisticspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTableStatisticsMessagePaginateTypeDef]
    ) -> PageIterator[DescribeTableStatisticsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/paginator/DescribeTableStatistics.html#DatabaseMigrationService.Paginator.DescribeTableStatistics.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators/#describetablestatisticspaginator)
        """
