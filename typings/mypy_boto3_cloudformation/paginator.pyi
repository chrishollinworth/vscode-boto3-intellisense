# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for cloudformation service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_cloudformation import CloudFormationClient
    from mypy_boto3_cloudformation.paginator import (
        DescribeAccountLimitsPaginator,
        DescribeChangeSetPaginator,
        DescribeStackEventsPaginator,
        DescribeStacksPaginator,
        ListChangeSetsPaginator,
        ListExportsPaginator,
        ListImportsPaginator,
        ListStackInstancesPaginator,
        ListStackResourcesPaginator,
        ListStackSetOperationResultsPaginator,
        ListStackSetOperationsPaginator,
        ListStackSetsPaginator,
        ListStacksPaginator,
    )

    client: CloudFormationClient = boto3.client("cloudformation")

    describe_account_limits_paginator: DescribeAccountLimitsPaginator = client.get_paginator("describe_account_limits")
    describe_change_set_paginator: DescribeChangeSetPaginator = client.get_paginator("describe_change_set")
    describe_stack_events_paginator: DescribeStackEventsPaginator = client.get_paginator("describe_stack_events")
    describe_stacks_paginator: DescribeStacksPaginator = client.get_paginator("describe_stacks")
    list_change_sets_paginator: ListChangeSetsPaginator = client.get_paginator("list_change_sets")
    list_exports_paginator: ListExportsPaginator = client.get_paginator("list_exports")
    list_imports_paginator: ListImportsPaginator = client.get_paginator("list_imports")
    list_stack_instances_paginator: ListStackInstancesPaginator = client.get_paginator("list_stack_instances")
    list_stack_resources_paginator: ListStackResourcesPaginator = client.get_paginator("list_stack_resources")
    list_stack_set_operation_results_paginator: ListStackSetOperationResultsPaginator = client.get_paginator("list_stack_set_operation_results")
    list_stack_set_operations_paginator: ListStackSetOperationsPaginator = client.get_paginator("list_stack_set_operations")
    list_stack_sets_paginator: ListStackSetsPaginator = client.get_paginator("list_stack_sets")
    list_stacks_paginator: ListStacksPaginator = client.get_paginator("list_stacks")
    ```
"""
import sys
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_cloudformation.type_defs import (
    DescribeAccountLimitsOutputTypeDef,
    DescribeChangeSetOutputTypeDef,
    DescribeStackEventsOutputTypeDef,
    DescribeStacksOutputTypeDef,
    ListChangeSetsOutputTypeDef,
    ListExportsOutputTypeDef,
    ListImportsOutputTypeDef,
    ListStackInstancesOutputTypeDef,
    ListStackResourcesOutputTypeDef,
    ListStackSetOperationResultsOutputTypeDef,
    ListStackSetOperationsOutputTypeDef,
    ListStackSetsOutputTypeDef,
    ListStacksOutputTypeDef,
    PaginatorConfigTypeDef,
    StackInstanceFilterTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeAccountLimitsPaginator",
    "DescribeChangeSetPaginator",
    "DescribeStackEventsPaginator",
    "DescribeStacksPaginator",
    "ListChangeSetsPaginator",
    "ListExportsPaginator",
    "ListImportsPaginator",
    "ListStackInstancesPaginator",
    "ListStackResourcesPaginator",
    "ListStackSetOperationResultsPaginator",
    "ListStackSetOperationsPaginator",
    "ListStackSetsPaginator",
    "ListStacksPaginator",
)


class DescribeAccountLimitsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAccountLimits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeAccountLimits)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAccountLimitsOutputTypeDef]:
        """
        [DescribeAccountLimits.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeAccountLimits.paginate)
        """


class DescribeChangeSetPaginator(Boto3Paginator):
    """
    [Paginator.DescribeChangeSet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeChangeSet)
    """

    def paginate(
        self,
        ChangeSetName: str,
        StackName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeChangeSetOutputTypeDef]:
        """
        [DescribeChangeSet.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeChangeSet.paginate)
        """


class DescribeStackEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeStackEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStackEvents)
    """

    def paginate(
        self, StackName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeStackEventsOutputTypeDef]:
        """
        [DescribeStackEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStackEvents.paginate)
        """


class DescribeStacksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStacks)
    """

    def paginate(
        self, StackName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeStacksOutputTypeDef]:
        """
        [DescribeStacks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStacks.paginate)
        """


class ListChangeSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListChangeSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.ListChangeSets)
    """

    def paginate(
        self, StackName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListChangeSetsOutputTypeDef]:
        """
        [ListChangeSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.ListChangeSets.paginate)
        """


class ListExportsPaginator(Boto3Paginator):
    """
    [Paginator.ListExports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.ListExports)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListExportsOutputTypeDef]:
        """
        [ListExports.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.ListExports.paginate)
        """


class ListImportsPaginator(Boto3Paginator):
    """
    [Paginator.ListImports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.ListImports)
    """

    def paginate(
        self, ExportName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListImportsOutputTypeDef]:
        """
        [ListImports.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.ListImports.paginate)
        """


class ListStackInstancesPaginator(Boto3Paginator):
    """
    [Paginator.ListStackInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackInstances)
    """

    def paginate(
        self,
        StackSetName: str,
        Filters: List[StackInstanceFilterTypeDef] = None,
        StackInstanceAccount: str = None,
        StackInstanceRegion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListStackInstancesOutputTypeDef]:
        """
        [ListStackInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackInstances.paginate)
        """


class ListStackResourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListStackResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackResources)
    """

    def paginate(
        self, StackName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStackResourcesOutputTypeDef]:
        """
        [ListStackResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackResources.paginate)
        """


class ListStackSetOperationResultsPaginator(Boto3Paginator):
    """
    [Paginator.ListStackSetOperationResults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperationResults)
    """

    def paginate(
        self, StackSetName: str, OperationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStackSetOperationResultsOutputTypeDef]:
        """
        [ListStackSetOperationResults.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperationResults.paginate)
        """


class ListStackSetOperationsPaginator(Boto3Paginator):
    """
    [Paginator.ListStackSetOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperations)
    """

    def paginate(
        self, StackSetName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStackSetOperationsOutputTypeDef]:
        """
        [ListStackSetOperations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperations.paginate)
        """


class ListStackSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListStackSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSets)
    """

    def paginate(
        self,
        Status: Literal["ACTIVE", "DELETED"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListStackSetsOutputTypeDef]:
        """
        [ListStackSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSets.paginate)
        """


class ListStacksPaginator(Boto3Paginator):
    """
    [Paginator.ListStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.ListStacks)
    """

    def paginate(
        self,
        StackStatusFilter: List[
            Literal[
                "CREATE_IN_PROGRESS",
                "CREATE_FAILED",
                "CREATE_COMPLETE",
                "ROLLBACK_IN_PROGRESS",
                "ROLLBACK_FAILED",
                "ROLLBACK_COMPLETE",
                "DELETE_IN_PROGRESS",
                "DELETE_FAILED",
                "DELETE_COMPLETE",
                "UPDATE_IN_PROGRESS",
                "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS",
                "UPDATE_COMPLETE",
                "UPDATE_ROLLBACK_IN_PROGRESS",
                "UPDATE_ROLLBACK_FAILED",
                "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS",
                "UPDATE_ROLLBACK_COMPLETE",
                "REVIEW_IN_PROGRESS",
                "IMPORT_IN_PROGRESS",
                "IMPORT_COMPLETE",
                "IMPORT_ROLLBACK_IN_PROGRESS",
                "IMPORT_ROLLBACK_FAILED",
                "IMPORT_ROLLBACK_COMPLETE",
            ]
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListStacksOutputTypeDef]:
        """
        [ListStacks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudformation.html#CloudFormation.Paginator.ListStacks.paginate)
        """
