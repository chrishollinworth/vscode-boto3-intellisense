"""
Type annotations for drs service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_drs import drsClient
    from mypy_boto3_drs.paginator import (
        DescribeJobLogItemsPaginator,
        DescribeJobsPaginator,
        DescribeLaunchConfigurationTemplatesPaginator,
        DescribeRecoveryInstancesPaginator,
        DescribeRecoverySnapshotsPaginator,
        DescribeReplicationConfigurationTemplatesPaginator,
        DescribeSourceNetworksPaginator,
        DescribeSourceServersPaginator,
        ListExtensibleSourceServersPaginator,
        ListLaunchActionsPaginator,
        ListStagingAccountsPaginator,
    )

    client: drsClient = boto3.client("drs")

    describe_job_log_items_paginator: DescribeJobLogItemsPaginator = client.get_paginator("describe_job_log_items")
    describe_jobs_paginator: DescribeJobsPaginator = client.get_paginator("describe_jobs")
    describe_launch_configuration_templates_paginator: DescribeLaunchConfigurationTemplatesPaginator = client.get_paginator("describe_launch_configuration_templates")
    describe_recovery_instances_paginator: DescribeRecoveryInstancesPaginator = client.get_paginator("describe_recovery_instances")
    describe_recovery_snapshots_paginator: DescribeRecoverySnapshotsPaginator = client.get_paginator("describe_recovery_snapshots")
    describe_replication_configuration_templates_paginator: DescribeReplicationConfigurationTemplatesPaginator = client.get_paginator("describe_replication_configuration_templates")
    describe_source_networks_paginator: DescribeSourceNetworksPaginator = client.get_paginator("describe_source_networks")
    describe_source_servers_paginator: DescribeSourceServersPaginator = client.get_paginator("describe_source_servers")
    list_extensible_source_servers_paginator: ListExtensibleSourceServersPaginator = client.get_paginator("list_extensible_source_servers")
    list_launch_actions_paginator: ListLaunchActionsPaginator = client.get_paginator("list_launch_actions")
    list_staging_accounts_paginator: ListStagingAccountsPaginator = client.get_paginator("list_staging_accounts")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import RecoverySnapshotsOrderType
from .type_defs import (
    DescribeJobLogItemsResponseTypeDef,
    DescribeJobsRequestFiltersTypeDef,
    DescribeJobsResponseTypeDef,
    DescribeLaunchConfigurationTemplatesResponseTypeDef,
    DescribeRecoveryInstancesRequestFiltersTypeDef,
    DescribeRecoveryInstancesResponseTypeDef,
    DescribeRecoverySnapshotsRequestFiltersTypeDef,
    DescribeRecoverySnapshotsResponseTypeDef,
    DescribeReplicationConfigurationTemplatesResponseTypeDef,
    DescribeSourceNetworksRequestFiltersTypeDef,
    DescribeSourceNetworksResponseTypeDef,
    DescribeSourceServersRequestFiltersTypeDef,
    DescribeSourceServersResponseTypeDef,
    LaunchActionsRequestFiltersTypeDef,
    ListExtensibleSourceServersResponseTypeDef,
    ListLaunchActionsResponseTypeDef,
    ListStagingAccountsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeJobLogItemsPaginator",
    "DescribeJobsPaginator",
    "DescribeLaunchConfigurationTemplatesPaginator",
    "DescribeRecoveryInstancesPaginator",
    "DescribeRecoverySnapshotsPaginator",
    "DescribeReplicationConfigurationTemplatesPaginator",
    "DescribeSourceNetworksPaginator",
    "DescribeSourceServersPaginator",
    "ListExtensibleSourceServersPaginator",
    "ListLaunchActionsPaginator",
    "ListStagingAccountsPaginator",
)

class DescribeJobLogItemsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/drs.html#drs.Paginator.DescribeJobLogItems)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators.html#describejoblogitemspaginator)
    """

    def paginate(
        self, *, jobID: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeJobLogItemsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/drs.html#drs.Paginator.DescribeJobLogItems.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators.html#describejoblogitemspaginator)
        """

class DescribeJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/drs.html#drs.Paginator.DescribeJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators.html#describejobspaginator)
    """

    def paginate(
        self,
        *,
        filters: "DescribeJobsRequestFiltersTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/drs.html#drs.Paginator.DescribeJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators.html#describejobspaginator)
        """

class DescribeLaunchConfigurationTemplatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/drs.html#drs.Paginator.DescribeLaunchConfigurationTemplates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators.html#describelaunchconfigurationtemplatespaginator)
    """

    def paginate(
        self,
        *,
        launchConfigurationTemplateIDs: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLaunchConfigurationTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/drs.html#drs.Paginator.DescribeLaunchConfigurationTemplates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators.html#describelaunchconfigurationtemplatespaginator)
        """

class DescribeRecoveryInstancesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/drs.html#drs.Paginator.DescribeRecoveryInstances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators.html#describerecoveryinstancespaginator)
    """

    def paginate(
        self,
        *,
        filters: "DescribeRecoveryInstancesRequestFiltersTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeRecoveryInstancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/drs.html#drs.Paginator.DescribeRecoveryInstances.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators.html#describerecoveryinstancespaginator)
        """

class DescribeRecoverySnapshotsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/drs.html#drs.Paginator.DescribeRecoverySnapshots)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators.html#describerecoverysnapshotspaginator)
    """

    def paginate(
        self,
        *,
        sourceServerID: str,
        filters: "DescribeRecoverySnapshotsRequestFiltersTypeDef" = None,
        order: RecoverySnapshotsOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeRecoverySnapshotsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/drs.html#drs.Paginator.DescribeRecoverySnapshots.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators.html#describerecoverysnapshotspaginator)
        """

class DescribeReplicationConfigurationTemplatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/drs.html#drs.Paginator.DescribeReplicationConfigurationTemplates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators.html#describereplicationconfigurationtemplatespaginator)
    """

    def paginate(
        self,
        *,
        replicationConfigurationTemplateIDs: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeReplicationConfigurationTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/drs.html#drs.Paginator.DescribeReplicationConfigurationTemplates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators.html#describereplicationconfigurationtemplatespaginator)
        """

class DescribeSourceNetworksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/drs.html#drs.Paginator.DescribeSourceNetworks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators.html#describesourcenetworkspaginator)
    """

    def paginate(
        self,
        *,
        filters: "DescribeSourceNetworksRequestFiltersTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSourceNetworksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/drs.html#drs.Paginator.DescribeSourceNetworks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators.html#describesourcenetworkspaginator)
        """

class DescribeSourceServersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/drs.html#drs.Paginator.DescribeSourceServers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators.html#describesourceserverspaginator)
    """

    def paginate(
        self,
        *,
        filters: "DescribeSourceServersRequestFiltersTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSourceServersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/drs.html#drs.Paginator.DescribeSourceServers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators.html#describesourceserverspaginator)
        """

class ListExtensibleSourceServersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/drs.html#drs.Paginator.ListExtensibleSourceServers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators.html#listextensiblesourceserverspaginator)
    """

    def paginate(
        self, *, stagingAccountID: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListExtensibleSourceServersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/drs.html#drs.Paginator.ListExtensibleSourceServers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators.html#listextensiblesourceserverspaginator)
        """

class ListLaunchActionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/drs.html#drs.Paginator.ListLaunchActions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators.html#listlaunchactionspaginator)
    """

    def paginate(
        self,
        *,
        resourceId: str,
        filters: "LaunchActionsRequestFiltersTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLaunchActionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/drs.html#drs.Paginator.ListLaunchActions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators.html#listlaunchactionspaginator)
        """

class ListStagingAccountsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/drs.html#drs.Paginator.ListStagingAccounts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators.html#liststagingaccountspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStagingAccountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/drs.html#drs.Paginator.ListStagingAccounts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators.html#liststagingaccountspaginator)
        """
