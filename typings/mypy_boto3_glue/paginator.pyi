"""
Type annotations for glue service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_glue.client import GlueClient
    from mypy_boto3_glue.paginator import (
        DescribeEntityPaginator,
        GetClassifiersPaginator,
        GetConnectionsPaginator,
        GetCrawlerMetricsPaginator,
        GetCrawlersPaginator,
        GetDatabasesPaginator,
        GetDevEndpointsPaginator,
        GetJobRunsPaginator,
        GetJobsPaginator,
        GetPartitionIndexesPaginator,
        GetPartitionsPaginator,
        GetResourcePoliciesPaginator,
        GetSecurityConfigurationsPaginator,
        GetTableVersionsPaginator,
        GetTablesPaginator,
        GetTriggersPaginator,
        GetUserDefinedFunctionsPaginator,
        GetWorkflowRunsPaginator,
        ListBlueprintsPaginator,
        ListConnectionTypesPaginator,
        ListEntitiesPaginator,
        ListJobsPaginator,
        ListRegistriesPaginator,
        ListSchemaVersionsPaginator,
        ListSchemasPaginator,
        ListTableOptimizerRunsPaginator,
        ListTriggersPaginator,
        ListUsageProfilesPaginator,
        ListWorkflowsPaginator,
    )

    session = Session()
    client: GlueClient = session.client("glue")

    describe_entity_paginator: DescribeEntityPaginator = client.get_paginator("describe_entity")
    get_classifiers_paginator: GetClassifiersPaginator = client.get_paginator("get_classifiers")
    get_connections_paginator: GetConnectionsPaginator = client.get_paginator("get_connections")
    get_crawler_metrics_paginator: GetCrawlerMetricsPaginator = client.get_paginator("get_crawler_metrics")
    get_crawlers_paginator: GetCrawlersPaginator = client.get_paginator("get_crawlers")
    get_databases_paginator: GetDatabasesPaginator = client.get_paginator("get_databases")
    get_dev_endpoints_paginator: GetDevEndpointsPaginator = client.get_paginator("get_dev_endpoints")
    get_job_runs_paginator: GetJobRunsPaginator = client.get_paginator("get_job_runs")
    get_jobs_paginator: GetJobsPaginator = client.get_paginator("get_jobs")
    get_partition_indexes_paginator: GetPartitionIndexesPaginator = client.get_paginator("get_partition_indexes")
    get_partitions_paginator: GetPartitionsPaginator = client.get_paginator("get_partitions")
    get_resource_policies_paginator: GetResourcePoliciesPaginator = client.get_paginator("get_resource_policies")
    get_security_configurations_paginator: GetSecurityConfigurationsPaginator = client.get_paginator("get_security_configurations")
    get_table_versions_paginator: GetTableVersionsPaginator = client.get_paginator("get_table_versions")
    get_tables_paginator: GetTablesPaginator = client.get_paginator("get_tables")
    get_triggers_paginator: GetTriggersPaginator = client.get_paginator("get_triggers")
    get_user_defined_functions_paginator: GetUserDefinedFunctionsPaginator = client.get_paginator("get_user_defined_functions")
    get_workflow_runs_paginator: GetWorkflowRunsPaginator = client.get_paginator("get_workflow_runs")
    list_blueprints_paginator: ListBlueprintsPaginator = client.get_paginator("list_blueprints")
    list_connection_types_paginator: ListConnectionTypesPaginator = client.get_paginator("list_connection_types")
    list_entities_paginator: ListEntitiesPaginator = client.get_paginator("list_entities")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    list_registries_paginator: ListRegistriesPaginator = client.get_paginator("list_registries")
    list_schema_versions_paginator: ListSchemaVersionsPaginator = client.get_paginator("list_schema_versions")
    list_schemas_paginator: ListSchemasPaginator = client.get_paginator("list_schemas")
    list_table_optimizer_runs_paginator: ListTableOptimizerRunsPaginator = client.get_paginator("list_table_optimizer_runs")
    list_triggers_paginator: ListTriggersPaginator = client.get_paginator("list_triggers")
    list_usage_profiles_paginator: ListUsageProfilesPaginator = client.get_paginator("list_usage_profiles")
    list_workflows_paginator: ListWorkflowsPaginator = client.get_paginator("list_workflows")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeEntityRequestPaginateTypeDef,
    DescribeEntityResponseTypeDef,
    GetClassifiersRequestPaginateTypeDef,
    GetClassifiersResponseTypeDef,
    GetConnectionsRequestPaginateTypeDef,
    GetConnectionsResponseTypeDef,
    GetCrawlerMetricsRequestPaginateTypeDef,
    GetCrawlerMetricsResponseTypeDef,
    GetCrawlersRequestPaginateTypeDef,
    GetCrawlersResponseTypeDef,
    GetDatabasesRequestPaginateTypeDef,
    GetDatabasesResponseTypeDef,
    GetDevEndpointsRequestPaginateTypeDef,
    GetDevEndpointsResponseTypeDef,
    GetJobRunsRequestPaginateTypeDef,
    GetJobRunsResponseTypeDef,
    GetJobsRequestPaginateTypeDef,
    GetJobsResponsePaginatorTypeDef,
    GetPartitionIndexesRequestPaginateTypeDef,
    GetPartitionIndexesResponseTypeDef,
    GetPartitionsRequestPaginateTypeDef,
    GetPartitionsResponseTypeDef,
    GetResourcePoliciesRequestPaginateTypeDef,
    GetResourcePoliciesResponseTypeDef,
    GetSecurityConfigurationsRequestPaginateTypeDef,
    GetSecurityConfigurationsResponseTypeDef,
    GetTablesRequestPaginateTypeDef,
    GetTablesResponsePaginatorTypeDef,
    GetTableVersionsRequestPaginateTypeDef,
    GetTableVersionsResponsePaginatorTypeDef,
    GetTriggersRequestPaginateTypeDef,
    GetTriggersResponseTypeDef,
    GetUserDefinedFunctionsRequestPaginateTypeDef,
    GetUserDefinedFunctionsResponseTypeDef,
    GetWorkflowRunsRequestPaginateTypeDef,
    GetWorkflowRunsResponseTypeDef,
    ListBlueprintsRequestPaginateTypeDef,
    ListBlueprintsResponseTypeDef,
    ListConnectionTypesRequestPaginateTypeDef,
    ListConnectionTypesResponseTypeDef,
    ListEntitiesRequestPaginateTypeDef,
    ListEntitiesResponseTypeDef,
    ListJobsRequestPaginateTypeDef,
    ListJobsResponseTypeDef,
    ListRegistriesInputPaginateTypeDef,
    ListRegistriesResponseTypeDef,
    ListSchemasInputPaginateTypeDef,
    ListSchemasResponseTypeDef,
    ListSchemaVersionsInputPaginateTypeDef,
    ListSchemaVersionsResponseTypeDef,
    ListTableOptimizerRunsRequestPaginateTypeDef,
    ListTableOptimizerRunsResponseTypeDef,
    ListTriggersRequestPaginateTypeDef,
    ListTriggersResponseTypeDef,
    ListUsageProfilesRequestPaginateTypeDef,
    ListUsageProfilesResponseTypeDef,
    ListWorkflowsRequestPaginateTypeDef,
    ListWorkflowsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeEntityPaginator",
    "GetClassifiersPaginator",
    "GetConnectionsPaginator",
    "GetCrawlerMetricsPaginator",
    "GetCrawlersPaginator",
    "GetDatabasesPaginator",
    "GetDevEndpointsPaginator",
    "GetJobRunsPaginator",
    "GetJobsPaginator",
    "GetPartitionIndexesPaginator",
    "GetPartitionsPaginator",
    "GetResourcePoliciesPaginator",
    "GetSecurityConfigurationsPaginator",
    "GetTableVersionsPaginator",
    "GetTablesPaginator",
    "GetTriggersPaginator",
    "GetUserDefinedFunctionsPaginator",
    "GetWorkflowRunsPaginator",
    "ListBlueprintsPaginator",
    "ListConnectionTypesPaginator",
    "ListEntitiesPaginator",
    "ListJobsPaginator",
    "ListRegistriesPaginator",
    "ListSchemaVersionsPaginator",
    "ListSchemasPaginator",
    "ListTableOptimizerRunsPaginator",
    "ListTriggersPaginator",
    "ListUsageProfilesPaginator",
    "ListWorkflowsPaginator",
)

if TYPE_CHECKING:
    _DescribeEntityPaginatorBase = Paginator[DescribeEntityResponseTypeDef]
else:
    _DescribeEntityPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEntityPaginator(_DescribeEntityPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/DescribeEntity.html#Glue.Paginator.DescribeEntity)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#describeentitypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEntityRequestPaginateTypeDef]
    ) -> PageIterator[DescribeEntityResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/DescribeEntity.html#Glue.Paginator.DescribeEntity.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#describeentitypaginator)
        """

if TYPE_CHECKING:
    _GetClassifiersPaginatorBase = Paginator[GetClassifiersResponseTypeDef]
else:
    _GetClassifiersPaginatorBase = Paginator  # type: ignore[assignment]

class GetClassifiersPaginator(_GetClassifiersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetClassifiers.html#Glue.Paginator.GetClassifiers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getclassifierspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetClassifiersRequestPaginateTypeDef]
    ) -> PageIterator[GetClassifiersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetClassifiers.html#Glue.Paginator.GetClassifiers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getclassifierspaginator)
        """

if TYPE_CHECKING:
    _GetConnectionsPaginatorBase = Paginator[GetConnectionsResponseTypeDef]
else:
    _GetConnectionsPaginatorBase = Paginator  # type: ignore[assignment]

class GetConnectionsPaginator(_GetConnectionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetConnections.html#Glue.Paginator.GetConnections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getconnectionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetConnectionsRequestPaginateTypeDef]
    ) -> PageIterator[GetConnectionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetConnections.html#Glue.Paginator.GetConnections.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getconnectionspaginator)
        """

if TYPE_CHECKING:
    _GetCrawlerMetricsPaginatorBase = Paginator[GetCrawlerMetricsResponseTypeDef]
else:
    _GetCrawlerMetricsPaginatorBase = Paginator  # type: ignore[assignment]

class GetCrawlerMetricsPaginator(_GetCrawlerMetricsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetCrawlerMetrics.html#Glue.Paginator.GetCrawlerMetrics)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getcrawlermetricspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetCrawlerMetricsRequestPaginateTypeDef]
    ) -> PageIterator[GetCrawlerMetricsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetCrawlerMetrics.html#Glue.Paginator.GetCrawlerMetrics.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getcrawlermetricspaginator)
        """

if TYPE_CHECKING:
    _GetCrawlersPaginatorBase = Paginator[GetCrawlersResponseTypeDef]
else:
    _GetCrawlersPaginatorBase = Paginator  # type: ignore[assignment]

class GetCrawlersPaginator(_GetCrawlersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetCrawlers.html#Glue.Paginator.GetCrawlers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getcrawlerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetCrawlersRequestPaginateTypeDef]
    ) -> PageIterator[GetCrawlersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetCrawlers.html#Glue.Paginator.GetCrawlers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getcrawlerspaginator)
        """

if TYPE_CHECKING:
    _GetDatabasesPaginatorBase = Paginator[GetDatabasesResponseTypeDef]
else:
    _GetDatabasesPaginatorBase = Paginator  # type: ignore[assignment]

class GetDatabasesPaginator(_GetDatabasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetDatabases.html#Glue.Paginator.GetDatabases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getdatabasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetDatabasesRequestPaginateTypeDef]
    ) -> PageIterator[GetDatabasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetDatabases.html#Glue.Paginator.GetDatabases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getdatabasespaginator)
        """

if TYPE_CHECKING:
    _GetDevEndpointsPaginatorBase = Paginator[GetDevEndpointsResponseTypeDef]
else:
    _GetDevEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class GetDevEndpointsPaginator(_GetDevEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetDevEndpoints.html#Glue.Paginator.GetDevEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getdevendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetDevEndpointsRequestPaginateTypeDef]
    ) -> PageIterator[GetDevEndpointsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetDevEndpoints.html#Glue.Paginator.GetDevEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getdevendpointspaginator)
        """

if TYPE_CHECKING:
    _GetJobRunsPaginatorBase = Paginator[GetJobRunsResponseTypeDef]
else:
    _GetJobRunsPaginatorBase = Paginator  # type: ignore[assignment]

class GetJobRunsPaginator(_GetJobRunsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetJobRuns.html#Glue.Paginator.GetJobRuns)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getjobrunspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetJobRunsRequestPaginateTypeDef]
    ) -> PageIterator[GetJobRunsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetJobRuns.html#Glue.Paginator.GetJobRuns.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getjobrunspaginator)
        """

if TYPE_CHECKING:
    _GetJobsPaginatorBase = Paginator[GetJobsResponsePaginatorTypeDef]
else:
    _GetJobsPaginatorBase = Paginator  # type: ignore[assignment]

class GetJobsPaginator(_GetJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetJobs.html#Glue.Paginator.GetJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetJobsRequestPaginateTypeDef]
    ) -> PageIterator[GetJobsResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetJobs.html#Glue.Paginator.GetJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getjobspaginator)
        """

if TYPE_CHECKING:
    _GetPartitionIndexesPaginatorBase = Paginator[GetPartitionIndexesResponseTypeDef]
else:
    _GetPartitionIndexesPaginatorBase = Paginator  # type: ignore[assignment]

class GetPartitionIndexesPaginator(_GetPartitionIndexesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetPartitionIndexes.html#Glue.Paginator.GetPartitionIndexes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getpartitionindexespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetPartitionIndexesRequestPaginateTypeDef]
    ) -> PageIterator[GetPartitionIndexesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetPartitionIndexes.html#Glue.Paginator.GetPartitionIndexes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getpartitionindexespaginator)
        """

if TYPE_CHECKING:
    _GetPartitionsPaginatorBase = Paginator[GetPartitionsResponseTypeDef]
else:
    _GetPartitionsPaginatorBase = Paginator  # type: ignore[assignment]

class GetPartitionsPaginator(_GetPartitionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetPartitions.html#Glue.Paginator.GetPartitions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getpartitionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetPartitionsRequestPaginateTypeDef]
    ) -> PageIterator[GetPartitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetPartitions.html#Glue.Paginator.GetPartitions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getpartitionspaginator)
        """

if TYPE_CHECKING:
    _GetResourcePoliciesPaginatorBase = Paginator[GetResourcePoliciesResponseTypeDef]
else:
    _GetResourcePoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class GetResourcePoliciesPaginator(_GetResourcePoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetResourcePolicies.html#Glue.Paginator.GetResourcePolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getresourcepoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetResourcePoliciesRequestPaginateTypeDef]
    ) -> PageIterator[GetResourcePoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetResourcePolicies.html#Glue.Paginator.GetResourcePolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getresourcepoliciespaginator)
        """

if TYPE_CHECKING:
    _GetSecurityConfigurationsPaginatorBase = Paginator[GetSecurityConfigurationsResponseTypeDef]
else:
    _GetSecurityConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class GetSecurityConfigurationsPaginator(_GetSecurityConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetSecurityConfigurations.html#Glue.Paginator.GetSecurityConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getsecurityconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetSecurityConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[GetSecurityConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetSecurityConfigurations.html#Glue.Paginator.GetSecurityConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getsecurityconfigurationspaginator)
        """

if TYPE_CHECKING:
    _GetTableVersionsPaginatorBase = Paginator[GetTableVersionsResponsePaginatorTypeDef]
else:
    _GetTableVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class GetTableVersionsPaginator(_GetTableVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetTableVersions.html#Glue.Paginator.GetTableVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#gettableversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetTableVersionsRequestPaginateTypeDef]
    ) -> PageIterator[GetTableVersionsResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetTableVersions.html#Glue.Paginator.GetTableVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#gettableversionspaginator)
        """

if TYPE_CHECKING:
    _GetTablesPaginatorBase = Paginator[GetTablesResponsePaginatorTypeDef]
else:
    _GetTablesPaginatorBase = Paginator  # type: ignore[assignment]

class GetTablesPaginator(_GetTablesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetTables.html#Glue.Paginator.GetTables)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#gettablespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetTablesRequestPaginateTypeDef]
    ) -> PageIterator[GetTablesResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetTables.html#Glue.Paginator.GetTables.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#gettablespaginator)
        """

if TYPE_CHECKING:
    _GetTriggersPaginatorBase = Paginator[GetTriggersResponseTypeDef]
else:
    _GetTriggersPaginatorBase = Paginator  # type: ignore[assignment]

class GetTriggersPaginator(_GetTriggersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetTriggers.html#Glue.Paginator.GetTriggers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#gettriggerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetTriggersRequestPaginateTypeDef]
    ) -> PageIterator[GetTriggersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetTriggers.html#Glue.Paginator.GetTriggers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#gettriggerspaginator)
        """

if TYPE_CHECKING:
    _GetUserDefinedFunctionsPaginatorBase = Paginator[GetUserDefinedFunctionsResponseTypeDef]
else:
    _GetUserDefinedFunctionsPaginatorBase = Paginator  # type: ignore[assignment]

class GetUserDefinedFunctionsPaginator(_GetUserDefinedFunctionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetUserDefinedFunctions.html#Glue.Paginator.GetUserDefinedFunctions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getuserdefinedfunctionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetUserDefinedFunctionsRequestPaginateTypeDef]
    ) -> PageIterator[GetUserDefinedFunctionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetUserDefinedFunctions.html#Glue.Paginator.GetUserDefinedFunctions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getuserdefinedfunctionspaginator)
        """

if TYPE_CHECKING:
    _GetWorkflowRunsPaginatorBase = Paginator[GetWorkflowRunsResponseTypeDef]
else:
    _GetWorkflowRunsPaginatorBase = Paginator  # type: ignore[assignment]

class GetWorkflowRunsPaginator(_GetWorkflowRunsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetWorkflowRuns.html#Glue.Paginator.GetWorkflowRuns)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getworkflowrunspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetWorkflowRunsRequestPaginateTypeDef]
    ) -> PageIterator[GetWorkflowRunsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/GetWorkflowRuns.html#Glue.Paginator.GetWorkflowRuns.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#getworkflowrunspaginator)
        """

if TYPE_CHECKING:
    _ListBlueprintsPaginatorBase = Paginator[ListBlueprintsResponseTypeDef]
else:
    _ListBlueprintsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBlueprintsPaginator(_ListBlueprintsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/ListBlueprints.html#Glue.Paginator.ListBlueprints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#listblueprintspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBlueprintsRequestPaginateTypeDef]
    ) -> PageIterator[ListBlueprintsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/ListBlueprints.html#Glue.Paginator.ListBlueprints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#listblueprintspaginator)
        """

if TYPE_CHECKING:
    _ListConnectionTypesPaginatorBase = Paginator[ListConnectionTypesResponseTypeDef]
else:
    _ListConnectionTypesPaginatorBase = Paginator  # type: ignore[assignment]

class ListConnectionTypesPaginator(_ListConnectionTypesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/ListConnectionTypes.html#Glue.Paginator.ListConnectionTypes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#listconnectiontypespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConnectionTypesRequestPaginateTypeDef]
    ) -> PageIterator[ListConnectionTypesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/ListConnectionTypes.html#Glue.Paginator.ListConnectionTypes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#listconnectiontypespaginator)
        """

if TYPE_CHECKING:
    _ListEntitiesPaginatorBase = Paginator[ListEntitiesResponseTypeDef]
else:
    _ListEntitiesPaginatorBase = Paginator  # type: ignore[assignment]

class ListEntitiesPaginator(_ListEntitiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/ListEntities.html#Glue.Paginator.ListEntities)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#listentitiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEntitiesRequestPaginateTypeDef]
    ) -> PageIterator[ListEntitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/ListEntities.html#Glue.Paginator.ListEntities.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#listentitiespaginator)
        """

if TYPE_CHECKING:
    _ListJobsPaginatorBase = Paginator[ListJobsResponseTypeDef]
else:
    _ListJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListJobsPaginator(_ListJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/ListJobs.html#Glue.Paginator.ListJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#listjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/ListJobs.html#Glue.Paginator.ListJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#listjobspaginator)
        """

if TYPE_CHECKING:
    _ListRegistriesPaginatorBase = Paginator[ListRegistriesResponseTypeDef]
else:
    _ListRegistriesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRegistriesPaginator(_ListRegistriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/ListRegistries.html#Glue.Paginator.ListRegistries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#listregistriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRegistriesInputPaginateTypeDef]
    ) -> PageIterator[ListRegistriesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/ListRegistries.html#Glue.Paginator.ListRegistries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#listregistriespaginator)
        """

if TYPE_CHECKING:
    _ListSchemaVersionsPaginatorBase = Paginator[ListSchemaVersionsResponseTypeDef]
else:
    _ListSchemaVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSchemaVersionsPaginator(_ListSchemaVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/ListSchemaVersions.html#Glue.Paginator.ListSchemaVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#listschemaversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSchemaVersionsInputPaginateTypeDef]
    ) -> PageIterator[ListSchemaVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/ListSchemaVersions.html#Glue.Paginator.ListSchemaVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#listschemaversionspaginator)
        """

if TYPE_CHECKING:
    _ListSchemasPaginatorBase = Paginator[ListSchemasResponseTypeDef]
else:
    _ListSchemasPaginatorBase = Paginator  # type: ignore[assignment]

class ListSchemasPaginator(_ListSchemasPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/ListSchemas.html#Glue.Paginator.ListSchemas)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#listschemaspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSchemasInputPaginateTypeDef]
    ) -> PageIterator[ListSchemasResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/ListSchemas.html#Glue.Paginator.ListSchemas.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#listschemaspaginator)
        """

if TYPE_CHECKING:
    _ListTableOptimizerRunsPaginatorBase = Paginator[ListTableOptimizerRunsResponseTypeDef]
else:
    _ListTableOptimizerRunsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTableOptimizerRunsPaginator(_ListTableOptimizerRunsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/ListTableOptimizerRuns.html#Glue.Paginator.ListTableOptimizerRuns)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#listtableoptimizerrunspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTableOptimizerRunsRequestPaginateTypeDef]
    ) -> PageIterator[ListTableOptimizerRunsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/ListTableOptimizerRuns.html#Glue.Paginator.ListTableOptimizerRuns.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#listtableoptimizerrunspaginator)
        """

if TYPE_CHECKING:
    _ListTriggersPaginatorBase = Paginator[ListTriggersResponseTypeDef]
else:
    _ListTriggersPaginatorBase = Paginator  # type: ignore[assignment]

class ListTriggersPaginator(_ListTriggersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/ListTriggers.html#Glue.Paginator.ListTriggers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#listtriggerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTriggersRequestPaginateTypeDef]
    ) -> PageIterator[ListTriggersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/ListTriggers.html#Glue.Paginator.ListTriggers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#listtriggerspaginator)
        """

if TYPE_CHECKING:
    _ListUsageProfilesPaginatorBase = Paginator[ListUsageProfilesResponseTypeDef]
else:
    _ListUsageProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class ListUsageProfilesPaginator(_ListUsageProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/ListUsageProfiles.html#Glue.Paginator.ListUsageProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#listusageprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUsageProfilesRequestPaginateTypeDef]
    ) -> PageIterator[ListUsageProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/ListUsageProfiles.html#Glue.Paginator.ListUsageProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#listusageprofilespaginator)
        """

if TYPE_CHECKING:
    _ListWorkflowsPaginatorBase = Paginator[ListWorkflowsResponseTypeDef]
else:
    _ListWorkflowsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkflowsPaginator(_ListWorkflowsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/ListWorkflows.html#Glue.Paginator.ListWorkflows)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#listworkflowspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkflowsRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkflowsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/paginator/ListWorkflows.html#Glue.Paginator.ListWorkflows.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators/#listworkflowspaginator)
        """
