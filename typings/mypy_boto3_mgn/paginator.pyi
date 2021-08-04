"""
Type annotations for mgn service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_mgn import mgnClient
    from mypy_boto3_mgn.paginator import (
        DescribeJobLogItemsPaginator,
        DescribeJobsPaginator,
        DescribeReplicationConfigurationTemplatesPaginator,
        DescribeSourceServersPaginator,
    )

    client: mgnClient = boto3.client("mgn")

    describe_job_log_items_paginator: DescribeJobLogItemsPaginator = client.get_paginator("describe_job_log_items")
    describe_jobs_paginator: DescribeJobsPaginator = client.get_paginator("describe_jobs")
    describe_replication_configuration_templates_paginator: DescribeReplicationConfigurationTemplatesPaginator = client.get_paginator("describe_replication_configuration_templates")
    describe_source_servers_paginator: DescribeSourceServersPaginator = client.get_paginator("describe_source_servers")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    DescribeJobLogItemsResponseTypeDef,
    DescribeJobsRequestFiltersTypeDef,
    DescribeJobsResponseTypeDef,
    DescribeReplicationConfigurationTemplatesResponseTypeDef,
    DescribeSourceServersRequestFiltersTypeDef,
    DescribeSourceServersResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeJobLogItemsPaginator",
    "DescribeJobsPaginator",
    "DescribeReplicationConfigurationTemplatesPaginator",
    "DescribeSourceServersPaginator",
)

class DescribeJobLogItemsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/mgn.html#mgn.Paginator.DescribeJobLogItems)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describejoblogitemspaginator)
    """

    def paginate(
        self, *, jobID: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeJobLogItemsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/mgn.html#mgn.Paginator.DescribeJobLogItems.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describejoblogitemspaginator)
        """

class DescribeJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/mgn.html#mgn.Paginator.DescribeJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describejobspaginator)
    """

    def paginate(
        self,
        *,
        filters: "DescribeJobsRequestFiltersTypeDef",
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/mgn.html#mgn.Paginator.DescribeJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describejobspaginator)
        """

class DescribeReplicationConfigurationTemplatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/mgn.html#mgn.Paginator.DescribeReplicationConfigurationTemplates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describereplicationconfigurationtemplatespaginator)
    """

    def paginate(
        self,
        *,
        replicationConfigurationTemplateIDs: List[str],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeReplicationConfigurationTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/mgn.html#mgn.Paginator.DescribeReplicationConfigurationTemplates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describereplicationconfigurationtemplatespaginator)
        """

class DescribeSourceServersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/mgn.html#mgn.Paginator.DescribeSourceServers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describesourceserverspaginator)
    """

    def paginate(
        self,
        *,
        filters: "DescribeSourceServersRequestFiltersTypeDef",
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSourceServersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/mgn.html#mgn.Paginator.DescribeSourceServers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describesourceserverspaginator)
        """
