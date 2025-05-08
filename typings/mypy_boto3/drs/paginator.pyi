"""
Type annotations for drs service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_drs.client import DrsClient
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

    session = Session()
    client: DrsClient = session.client("drs")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeJobLogItemsRequestPaginateTypeDef,
    DescribeJobLogItemsResponseTypeDef,
    DescribeJobsRequestPaginateTypeDef,
    DescribeJobsResponseTypeDef,
    DescribeLaunchConfigurationTemplatesRequestPaginateTypeDef,
    DescribeLaunchConfigurationTemplatesResponseTypeDef,
    DescribeRecoveryInstancesRequestPaginateTypeDef,
    DescribeRecoveryInstancesResponseTypeDef,
    DescribeRecoverySnapshotsRequestPaginateTypeDef,
    DescribeRecoverySnapshotsResponseTypeDef,
    DescribeReplicationConfigurationTemplatesRequestPaginateTypeDef,
    DescribeReplicationConfigurationTemplatesResponseTypeDef,
    DescribeSourceNetworksRequestPaginateTypeDef,
    DescribeSourceNetworksResponseTypeDef,
    DescribeSourceServersRequestPaginateTypeDef,
    DescribeSourceServersResponseTypeDef,
    ListExtensibleSourceServersRequestPaginateTypeDef,
    ListExtensibleSourceServersResponseTypeDef,
    ListLaunchActionsRequestPaginateTypeDef,
    ListLaunchActionsResponseTypeDef,
    ListStagingAccountsRequestPaginateTypeDef,
    ListStagingAccountsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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

if TYPE_CHECKING:
    _DescribeJobLogItemsPaginatorBase = Paginator[DescribeJobLogItemsResponseTypeDef]
else:
    _DescribeJobLogItemsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeJobLogItemsPaginator(_DescribeJobLogItemsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/paginator/DescribeJobLogItems.html#Drs.Paginator.DescribeJobLogItems)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators/#describejoblogitemspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeJobLogItemsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeJobLogItemsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/paginator/DescribeJobLogItems.html#Drs.Paginator.DescribeJobLogItems.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators/#describejoblogitemspaginator)
        """

if TYPE_CHECKING:
    _DescribeJobsPaginatorBase = Paginator[DescribeJobsResponseTypeDef]
else:
    _DescribeJobsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeJobsPaginator(_DescribeJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/paginator/DescribeJobs.html#Drs.Paginator.DescribeJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators/#describejobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeJobsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/paginator/DescribeJobs.html#Drs.Paginator.DescribeJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators/#describejobspaginator)
        """

if TYPE_CHECKING:
    _DescribeLaunchConfigurationTemplatesPaginatorBase = Paginator[
        DescribeLaunchConfigurationTemplatesResponseTypeDef
    ]
else:
    _DescribeLaunchConfigurationTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeLaunchConfigurationTemplatesPaginator(
    _DescribeLaunchConfigurationTemplatesPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/paginator/DescribeLaunchConfigurationTemplates.html#Drs.Paginator.DescribeLaunchConfigurationTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators/#describelaunchconfigurationtemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeLaunchConfigurationTemplatesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeLaunchConfigurationTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/paginator/DescribeLaunchConfigurationTemplates.html#Drs.Paginator.DescribeLaunchConfigurationTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators/#describelaunchconfigurationtemplatespaginator)
        """

if TYPE_CHECKING:
    _DescribeRecoveryInstancesPaginatorBase = Paginator[DescribeRecoveryInstancesResponseTypeDef]
else:
    _DescribeRecoveryInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeRecoveryInstancesPaginator(_DescribeRecoveryInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/paginator/DescribeRecoveryInstances.html#Drs.Paginator.DescribeRecoveryInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators/#describerecoveryinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeRecoveryInstancesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeRecoveryInstancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/paginator/DescribeRecoveryInstances.html#Drs.Paginator.DescribeRecoveryInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators/#describerecoveryinstancespaginator)
        """

if TYPE_CHECKING:
    _DescribeRecoverySnapshotsPaginatorBase = Paginator[DescribeRecoverySnapshotsResponseTypeDef]
else:
    _DescribeRecoverySnapshotsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeRecoverySnapshotsPaginator(_DescribeRecoverySnapshotsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/paginator/DescribeRecoverySnapshots.html#Drs.Paginator.DescribeRecoverySnapshots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators/#describerecoverysnapshotspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeRecoverySnapshotsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeRecoverySnapshotsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/paginator/DescribeRecoverySnapshots.html#Drs.Paginator.DescribeRecoverySnapshots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators/#describerecoverysnapshotspaginator)
        """

if TYPE_CHECKING:
    _DescribeReplicationConfigurationTemplatesPaginatorBase = Paginator[
        DescribeReplicationConfigurationTemplatesResponseTypeDef
    ]
else:
    _DescribeReplicationConfigurationTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeReplicationConfigurationTemplatesPaginator(
    _DescribeReplicationConfigurationTemplatesPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/paginator/DescribeReplicationConfigurationTemplates.html#Drs.Paginator.DescribeReplicationConfigurationTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators/#describereplicationconfigurationtemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReplicationConfigurationTemplatesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeReplicationConfigurationTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/paginator/DescribeReplicationConfigurationTemplates.html#Drs.Paginator.DescribeReplicationConfigurationTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators/#describereplicationconfigurationtemplatespaginator)
        """

if TYPE_CHECKING:
    _DescribeSourceNetworksPaginatorBase = Paginator[DescribeSourceNetworksResponseTypeDef]
else:
    _DescribeSourceNetworksPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSourceNetworksPaginator(_DescribeSourceNetworksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/paginator/DescribeSourceNetworks.html#Drs.Paginator.DescribeSourceNetworks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators/#describesourcenetworkspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSourceNetworksRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSourceNetworksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/paginator/DescribeSourceNetworks.html#Drs.Paginator.DescribeSourceNetworks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators/#describesourcenetworkspaginator)
        """

if TYPE_CHECKING:
    _DescribeSourceServersPaginatorBase = Paginator[DescribeSourceServersResponseTypeDef]
else:
    _DescribeSourceServersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSourceServersPaginator(_DescribeSourceServersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/paginator/DescribeSourceServers.html#Drs.Paginator.DescribeSourceServers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators/#describesourceserverspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSourceServersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSourceServersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/paginator/DescribeSourceServers.html#Drs.Paginator.DescribeSourceServers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators/#describesourceserverspaginator)
        """

if TYPE_CHECKING:
    _ListExtensibleSourceServersPaginatorBase = Paginator[
        ListExtensibleSourceServersResponseTypeDef
    ]
else:
    _ListExtensibleSourceServersPaginatorBase = Paginator  # type: ignore[assignment]

class ListExtensibleSourceServersPaginator(_ListExtensibleSourceServersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/paginator/ListExtensibleSourceServers.html#Drs.Paginator.ListExtensibleSourceServers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators/#listextensiblesourceserverspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListExtensibleSourceServersRequestPaginateTypeDef]
    ) -> PageIterator[ListExtensibleSourceServersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/paginator/ListExtensibleSourceServers.html#Drs.Paginator.ListExtensibleSourceServers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators/#listextensiblesourceserverspaginator)
        """

if TYPE_CHECKING:
    _ListLaunchActionsPaginatorBase = Paginator[ListLaunchActionsResponseTypeDef]
else:
    _ListLaunchActionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListLaunchActionsPaginator(_ListLaunchActionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/paginator/ListLaunchActions.html#Drs.Paginator.ListLaunchActions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators/#listlaunchactionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLaunchActionsRequestPaginateTypeDef]
    ) -> PageIterator[ListLaunchActionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/paginator/ListLaunchActions.html#Drs.Paginator.ListLaunchActions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators/#listlaunchactionspaginator)
        """

if TYPE_CHECKING:
    _ListStagingAccountsPaginatorBase = Paginator[ListStagingAccountsResponseTypeDef]
else:
    _ListStagingAccountsPaginatorBase = Paginator  # type: ignore[assignment]

class ListStagingAccountsPaginator(_ListStagingAccountsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/paginator/ListStagingAccounts.html#Drs.Paginator.ListStagingAccounts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators/#liststagingaccountspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStagingAccountsRequestPaginateTypeDef]
    ) -> PageIterator[ListStagingAccountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs/paginator/ListStagingAccounts.html#Drs.Paginator.ListStagingAccounts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_drs/paginators/#liststagingaccountspaginator)
        """
