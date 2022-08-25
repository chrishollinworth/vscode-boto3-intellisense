"""
Type annotations for cloudformation service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html)

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
        ListTypesPaginator,
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
    list_types_paginator: ListTypesPaginator = client.get_paginator("list_types")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    CallAsType,
    DeprecatedStatusType,
    ProvisioningTypeType,
    RegistryTypeType,
    StackSetStatusType,
    StackStatusType,
    VisibilityType,
)
from .type_defs import (
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
    ListTypesOutputTypeDef,
    PaginatorConfigTypeDef,
    StackInstanceFilterTypeDef,
    TypeFiltersTypeDef,
)

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
    "ListTypesPaginator",
)

class DescribeAccountLimitsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeAccountLimits)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#describeaccountlimitspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAccountLimitsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeAccountLimits.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#describeaccountlimitspaginator)
        """

class DescribeChangeSetPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeChangeSet)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#describechangesetpaginator)
    """

    def paginate(
        self,
        *,
        ChangeSetName: str,
        StackName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeChangeSetOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeChangeSet.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#describechangesetpaginator)
        """

class DescribeStackEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStackEvents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#describestackeventspaginator)
    """

    def paginate(
        self, *, StackName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeStackEventsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStackEvents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#describestackeventspaginator)
        """

class DescribeStacksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStacks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#describestackspaginator)
    """

    def paginate(
        self, *, StackName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeStacksOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStacks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#describestackspaginator)
        """

class ListChangeSetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.ListChangeSets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#listchangesetspaginator)
    """

    def paginate(
        self, *, StackName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListChangeSetsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.ListChangeSets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#listchangesetspaginator)
        """

class ListExportsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.ListExports)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#listexportspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListExportsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.ListExports.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#listexportspaginator)
        """

class ListImportsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.ListImports)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#listimportspaginator)
    """

    def paginate(
        self, *, ExportName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListImportsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.ListImports.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#listimportspaginator)
        """

class ListStackInstancesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackInstances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#liststackinstancespaginator)
    """

    def paginate(
        self,
        *,
        StackSetName: str,
        Filters: List["StackInstanceFilterTypeDef"] = None,
        StackInstanceAccount: str = None,
        StackInstanceRegion: str = None,
        CallAs: CallAsType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStackInstancesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackInstances.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#liststackinstancespaginator)
        """

class ListStackResourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackResources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#liststackresourcespaginator)
    """

    def paginate(
        self, *, StackName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStackResourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackResources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#liststackresourcespaginator)
        """

class ListStackSetOperationResultsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperationResults)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#liststacksetoperationresultspaginator)
    """

    def paginate(
        self,
        *,
        StackSetName: str,
        OperationId: str,
        CallAs: CallAsType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStackSetOperationResultsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperationResults.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#liststacksetoperationresultspaginator)
        """

class ListStackSetOperationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#liststacksetoperationspaginator)
    """

    def paginate(
        self,
        *,
        StackSetName: str,
        CallAs: CallAsType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStackSetOperationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#liststacksetoperationspaginator)
        """

class ListStackSetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#liststacksetspaginator)
    """

    def paginate(
        self,
        *,
        Status: StackSetStatusType = None,
        CallAs: CallAsType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStackSetsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#liststacksetspaginator)
        """

class ListStacksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.ListStacks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#liststackspaginator)
    """

    def paginate(
        self,
        *,
        StackStatusFilter: List[StackStatusType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStacksOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.ListStacks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#liststackspaginator)
        """

class ListTypesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.ListTypes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#listtypespaginator)
    """

    def paginate(
        self,
        *,
        Visibility: VisibilityType = None,
        ProvisioningType: ProvisioningTypeType = None,
        DeprecatedStatus: DeprecatedStatusType = None,
        Type: RegistryTypeType = None,
        Filters: "TypeFiltersTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTypesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/cloudformation.html#CloudFormation.Paginator.ListTypes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators.html#listtypespaginator)
        """
