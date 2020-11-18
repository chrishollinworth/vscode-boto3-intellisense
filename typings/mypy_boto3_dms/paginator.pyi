# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for dms service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_dms import DatabaseMigrationServiceClient
    from mypy_boto3_dms.paginator import (
        DescribeCertificatesPaginator,
        DescribeConnectionsPaginator,
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

    client: DatabaseMigrationServiceClient = boto3.client("dms")

    describe_certificates_paginator: DescribeCertificatesPaginator = client.get_paginator("describe_certificates")
    describe_connections_paginator: DescribeConnectionsPaginator = client.get_paginator("describe_connections")
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
import sys
from datetime import datetime
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_dms.type_defs import (
    DescribeCertificatesResponseTypeDef,
    DescribeConnectionsResponseTypeDef,
    DescribeEndpointsResponseTypeDef,
    DescribeEndpointTypesResponseTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeEventSubscriptionsResponseTypeDef,
    DescribeOrderableReplicationInstancesResponseTypeDef,
    DescribeReplicationInstancesResponseTypeDef,
    DescribeReplicationSubnetGroupsResponseTypeDef,
    DescribeReplicationTaskAssessmentResultsResponseTypeDef,
    DescribeReplicationTasksResponseTypeDef,
    DescribeSchemasResponseTypeDef,
    DescribeTableStatisticsResponseTypeDef,
    FilterTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeCertificatesPaginator",
    "DescribeConnectionsPaginator",
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


class DescribeCertificatesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeCertificates)
    """

    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeCertificatesResponseTypeDef]:
        """
        [DescribeCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeCertificates.paginate)
        """


class DescribeConnectionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeConnections)
    """

    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeConnectionsResponseTypeDef]:
        """
        [DescribeConnections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeConnections.paginate)
        """


class DescribeEndpointTypesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEndpointTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpointTypes)
    """

    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEndpointTypesResponseTypeDef]:
        """
        [DescribeEndpointTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpointTypes.paginate)
        """


class DescribeEndpointsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpoints)
    """

    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEndpointsResponseTypeDef]:
        """
        [DescribeEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpoints.paginate)
        """


class DescribeEventSubscriptionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEventSubscriptions)
    """

    def paginate(
        self,
        SubscriptionName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeEventSubscriptionsResponseTypeDef]:
        """
        [DescribeEventSubscriptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEventSubscriptions.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEvents)
    """

    def paginate(
        self,
        SourceIdentifier: str = None,
        SourceType: Literal["replication-instance"] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeEventsResponseTypeDef]:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEvents.paginate)
        """


class DescribeOrderableReplicationInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeOrderableReplicationInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeOrderableReplicationInstances)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeOrderableReplicationInstancesResponseTypeDef]:
        """
        [DescribeOrderableReplicationInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeOrderableReplicationInstances.paginate)
        """


class DescribeReplicationInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReplicationInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationInstances)
    """

    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeReplicationInstancesResponseTypeDef]:
        """
        [DescribeReplicationInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationInstances.paginate)
        """


class DescribeReplicationSubnetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReplicationSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationSubnetGroups)
    """

    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeReplicationSubnetGroupsResponseTypeDef]:
        """
        [DescribeReplicationSubnetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationSubnetGroups.paginate)
        """


class DescribeReplicationTaskAssessmentResultsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReplicationTaskAssessmentResults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTaskAssessmentResults)
    """

    def paginate(
        self, ReplicationTaskArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeReplicationTaskAssessmentResultsResponseTypeDef]:
        """
        [DescribeReplicationTaskAssessmentResults.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTaskAssessmentResults.paginate)
        """


class DescribeReplicationTasksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReplicationTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTasks)
    """

    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        WithoutSettings: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeReplicationTasksResponseTypeDef]:
        """
        [DescribeReplicationTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTasks.paginate)
        """


class DescribeSchemasPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeSchemas)
    """

    def paginate(
        self, EndpointArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSchemasResponseTypeDef]:
        """
        [DescribeSchemas.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeSchemas.paginate)
        """


class DescribeTableStatisticsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTableStatistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeTableStatistics)
    """

    def paginate(
        self,
        ReplicationTaskArn: str,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeTableStatisticsResponseTypeDef]:
        """
        [DescribeTableStatistics.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeTableStatistics.paginate)
        """
