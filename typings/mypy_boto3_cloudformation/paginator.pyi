"""
Type annotations for cloudformation service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_cloudformation.client import CloudFormationClient
    from mypy_boto3_cloudformation.paginator import (
        DescribeAccountLimitsPaginator,
        DescribeChangeSetPaginator,
        DescribeStackEventsPaginator,
        DescribeStacksPaginator,
        ListChangeSetsPaginator,
        ListExportsPaginator,
        ListGeneratedTemplatesPaginator,
        ListImportsPaginator,
        ListResourceScanRelatedResourcesPaginator,
        ListResourceScanResourcesPaginator,
        ListResourceScansPaginator,
        ListStackInstancesPaginator,
        ListStackRefactorActionsPaginator,
        ListStackRefactorsPaginator,
        ListStackResourcesPaginator,
        ListStackSetOperationResultsPaginator,
        ListStackSetOperationsPaginator,
        ListStackSetsPaginator,
        ListStacksPaginator,
        ListTypesPaginator,
    )

    session = Session()
    client: CloudFormationClient = session.client("cloudformation")

    describe_account_limits_paginator: DescribeAccountLimitsPaginator = client.get_paginator("describe_account_limits")
    describe_change_set_paginator: DescribeChangeSetPaginator = client.get_paginator("describe_change_set")
    describe_stack_events_paginator: DescribeStackEventsPaginator = client.get_paginator("describe_stack_events")
    describe_stacks_paginator: DescribeStacksPaginator = client.get_paginator("describe_stacks")
    list_change_sets_paginator: ListChangeSetsPaginator = client.get_paginator("list_change_sets")
    list_exports_paginator: ListExportsPaginator = client.get_paginator("list_exports")
    list_generated_templates_paginator: ListGeneratedTemplatesPaginator = client.get_paginator("list_generated_templates")
    list_imports_paginator: ListImportsPaginator = client.get_paginator("list_imports")
    list_resource_scan_related_resources_paginator: ListResourceScanRelatedResourcesPaginator = client.get_paginator("list_resource_scan_related_resources")
    list_resource_scan_resources_paginator: ListResourceScanResourcesPaginator = client.get_paginator("list_resource_scan_resources")
    list_resource_scans_paginator: ListResourceScansPaginator = client.get_paginator("list_resource_scans")
    list_stack_instances_paginator: ListStackInstancesPaginator = client.get_paginator("list_stack_instances")
    list_stack_refactor_actions_paginator: ListStackRefactorActionsPaginator = client.get_paginator("list_stack_refactor_actions")
    list_stack_refactors_paginator: ListStackRefactorsPaginator = client.get_paginator("list_stack_refactors")
    list_stack_resources_paginator: ListStackResourcesPaginator = client.get_paginator("list_stack_resources")
    list_stack_set_operation_results_paginator: ListStackSetOperationResultsPaginator = client.get_paginator("list_stack_set_operation_results")
    list_stack_set_operations_paginator: ListStackSetOperationsPaginator = client.get_paginator("list_stack_set_operations")
    list_stack_sets_paginator: ListStackSetsPaginator = client.get_paginator("list_stack_sets")
    list_stacks_paginator: ListStacksPaginator = client.get_paginator("list_stacks")
    list_types_paginator: ListTypesPaginator = client.get_paginator("list_types")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeAccountLimitsInputPaginateTypeDef,
    DescribeAccountLimitsOutputTypeDef,
    DescribeChangeSetInputPaginateTypeDef,
    DescribeChangeSetOutputTypeDef,
    DescribeStackEventsInputPaginateTypeDef,
    DescribeStackEventsOutputTypeDef,
    DescribeStacksInputPaginateTypeDef,
    DescribeStacksOutputTypeDef,
    ListChangeSetsInputPaginateTypeDef,
    ListChangeSetsOutputTypeDef,
    ListExportsInputPaginateTypeDef,
    ListExportsOutputTypeDef,
    ListGeneratedTemplatesInputPaginateTypeDef,
    ListGeneratedTemplatesOutputTypeDef,
    ListImportsInputPaginateTypeDef,
    ListImportsOutputTypeDef,
    ListResourceScanRelatedResourcesInputPaginateTypeDef,
    ListResourceScanRelatedResourcesOutputTypeDef,
    ListResourceScanResourcesInputPaginateTypeDef,
    ListResourceScanResourcesOutputTypeDef,
    ListResourceScansInputPaginateTypeDef,
    ListResourceScansOutputTypeDef,
    ListStackInstancesInputPaginateTypeDef,
    ListStackInstancesOutputTypeDef,
    ListStackRefactorActionsInputPaginateTypeDef,
    ListStackRefactorActionsOutputTypeDef,
    ListStackRefactorsInputPaginateTypeDef,
    ListStackRefactorsOutputTypeDef,
    ListStackResourcesInputPaginateTypeDef,
    ListStackResourcesOutputTypeDef,
    ListStackSetOperationResultsInputPaginateTypeDef,
    ListStackSetOperationResultsOutputTypeDef,
    ListStackSetOperationsInputPaginateTypeDef,
    ListStackSetOperationsOutputTypeDef,
    ListStackSetsInputPaginateTypeDef,
    ListStackSetsOutputTypeDef,
    ListStacksInputPaginateTypeDef,
    ListStacksOutputTypeDef,
    ListTypesInputPaginateTypeDef,
    ListTypesOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeAccountLimitsPaginator",
    "DescribeChangeSetPaginator",
    "DescribeStackEventsPaginator",
    "DescribeStacksPaginator",
    "ListChangeSetsPaginator",
    "ListExportsPaginator",
    "ListGeneratedTemplatesPaginator",
    "ListImportsPaginator",
    "ListResourceScanRelatedResourcesPaginator",
    "ListResourceScanResourcesPaginator",
    "ListResourceScansPaginator",
    "ListStackInstancesPaginator",
    "ListStackRefactorActionsPaginator",
    "ListStackRefactorsPaginator",
    "ListStackResourcesPaginator",
    "ListStackSetOperationResultsPaginator",
    "ListStackSetOperationsPaginator",
    "ListStackSetsPaginator",
    "ListStacksPaginator",
    "ListTypesPaginator",
)

if TYPE_CHECKING:
    _DescribeAccountLimitsPaginatorBase = Paginator[DescribeAccountLimitsOutputTypeDef]
else:
    _DescribeAccountLimitsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeAccountLimitsPaginator(_DescribeAccountLimitsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/DescribeAccountLimits.html#CloudFormation.Paginator.DescribeAccountLimits)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#describeaccountlimitspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAccountLimitsInputPaginateTypeDef]
    ) -> PageIterator[DescribeAccountLimitsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/DescribeAccountLimits.html#CloudFormation.Paginator.DescribeAccountLimits.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#describeaccountlimitspaginator)
        """

if TYPE_CHECKING:
    _DescribeChangeSetPaginatorBase = Paginator[DescribeChangeSetOutputTypeDef]
else:
    _DescribeChangeSetPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeChangeSetPaginator(_DescribeChangeSetPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/DescribeChangeSet.html#CloudFormation.Paginator.DescribeChangeSet)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#describechangesetpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeChangeSetInputPaginateTypeDef]
    ) -> PageIterator[DescribeChangeSetOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/DescribeChangeSet.html#CloudFormation.Paginator.DescribeChangeSet.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#describechangesetpaginator)
        """

if TYPE_CHECKING:
    _DescribeStackEventsPaginatorBase = Paginator[DescribeStackEventsOutputTypeDef]
else:
    _DescribeStackEventsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeStackEventsPaginator(_DescribeStackEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/DescribeStackEvents.html#CloudFormation.Paginator.DescribeStackEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#describestackeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeStackEventsInputPaginateTypeDef]
    ) -> PageIterator[DescribeStackEventsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/DescribeStackEvents.html#CloudFormation.Paginator.DescribeStackEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#describestackeventspaginator)
        """

if TYPE_CHECKING:
    _DescribeStacksPaginatorBase = Paginator[DescribeStacksOutputTypeDef]
else:
    _DescribeStacksPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeStacksPaginator(_DescribeStacksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/DescribeStacks.html#CloudFormation.Paginator.DescribeStacks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#describestackspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeStacksInputPaginateTypeDef]
    ) -> PageIterator[DescribeStacksOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/DescribeStacks.html#CloudFormation.Paginator.DescribeStacks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#describestackspaginator)
        """

if TYPE_CHECKING:
    _ListChangeSetsPaginatorBase = Paginator[ListChangeSetsOutputTypeDef]
else:
    _ListChangeSetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListChangeSetsPaginator(_ListChangeSetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListChangeSets.html#CloudFormation.Paginator.ListChangeSets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#listchangesetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListChangeSetsInputPaginateTypeDef]
    ) -> PageIterator[ListChangeSetsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListChangeSets.html#CloudFormation.Paginator.ListChangeSets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#listchangesetspaginator)
        """

if TYPE_CHECKING:
    _ListExportsPaginatorBase = Paginator[ListExportsOutputTypeDef]
else:
    _ListExportsPaginatorBase = Paginator  # type: ignore[assignment]

class ListExportsPaginator(_ListExportsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListExports.html#CloudFormation.Paginator.ListExports)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#listexportspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListExportsInputPaginateTypeDef]
    ) -> PageIterator[ListExportsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListExports.html#CloudFormation.Paginator.ListExports.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#listexportspaginator)
        """

if TYPE_CHECKING:
    _ListGeneratedTemplatesPaginatorBase = Paginator[ListGeneratedTemplatesOutputTypeDef]
else:
    _ListGeneratedTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListGeneratedTemplatesPaginator(_ListGeneratedTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListGeneratedTemplates.html#CloudFormation.Paginator.ListGeneratedTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#listgeneratedtemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGeneratedTemplatesInputPaginateTypeDef]
    ) -> PageIterator[ListGeneratedTemplatesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListGeneratedTemplates.html#CloudFormation.Paginator.ListGeneratedTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#listgeneratedtemplatespaginator)
        """

if TYPE_CHECKING:
    _ListImportsPaginatorBase = Paginator[ListImportsOutputTypeDef]
else:
    _ListImportsPaginatorBase = Paginator  # type: ignore[assignment]

class ListImportsPaginator(_ListImportsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListImports.html#CloudFormation.Paginator.ListImports)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#listimportspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListImportsInputPaginateTypeDef]
    ) -> PageIterator[ListImportsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListImports.html#CloudFormation.Paginator.ListImports.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#listimportspaginator)
        """

if TYPE_CHECKING:
    _ListResourceScanRelatedResourcesPaginatorBase = Paginator[
        ListResourceScanRelatedResourcesOutputTypeDef
    ]
else:
    _ListResourceScanRelatedResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourceScanRelatedResourcesPaginator(_ListResourceScanRelatedResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListResourceScanRelatedResources.html#CloudFormation.Paginator.ListResourceScanRelatedResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#listresourcescanrelatedresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourceScanRelatedResourcesInputPaginateTypeDef]
    ) -> PageIterator[ListResourceScanRelatedResourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListResourceScanRelatedResources.html#CloudFormation.Paginator.ListResourceScanRelatedResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#listresourcescanrelatedresourcespaginator)
        """

if TYPE_CHECKING:
    _ListResourceScanResourcesPaginatorBase = Paginator[ListResourceScanResourcesOutputTypeDef]
else:
    _ListResourceScanResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourceScanResourcesPaginator(_ListResourceScanResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListResourceScanResources.html#CloudFormation.Paginator.ListResourceScanResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#listresourcescanresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourceScanResourcesInputPaginateTypeDef]
    ) -> PageIterator[ListResourceScanResourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListResourceScanResources.html#CloudFormation.Paginator.ListResourceScanResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#listresourcescanresourcespaginator)
        """

if TYPE_CHECKING:
    _ListResourceScansPaginatorBase = Paginator[ListResourceScansOutputTypeDef]
else:
    _ListResourceScansPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourceScansPaginator(_ListResourceScansPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListResourceScans.html#CloudFormation.Paginator.ListResourceScans)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#listresourcescanspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourceScansInputPaginateTypeDef]
    ) -> PageIterator[ListResourceScansOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListResourceScans.html#CloudFormation.Paginator.ListResourceScans.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#listresourcescanspaginator)
        """

if TYPE_CHECKING:
    _ListStackInstancesPaginatorBase = Paginator[ListStackInstancesOutputTypeDef]
else:
    _ListStackInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class ListStackInstancesPaginator(_ListStackInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListStackInstances.html#CloudFormation.Paginator.ListStackInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#liststackinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStackInstancesInputPaginateTypeDef]
    ) -> PageIterator[ListStackInstancesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListStackInstances.html#CloudFormation.Paginator.ListStackInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#liststackinstancespaginator)
        """

if TYPE_CHECKING:
    _ListStackRefactorActionsPaginatorBase = Paginator[ListStackRefactorActionsOutputTypeDef]
else:
    _ListStackRefactorActionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListStackRefactorActionsPaginator(_ListStackRefactorActionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListStackRefactorActions.html#CloudFormation.Paginator.ListStackRefactorActions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#liststackrefactoractionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStackRefactorActionsInputPaginateTypeDef]
    ) -> PageIterator[ListStackRefactorActionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListStackRefactorActions.html#CloudFormation.Paginator.ListStackRefactorActions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#liststackrefactoractionspaginator)
        """

if TYPE_CHECKING:
    _ListStackRefactorsPaginatorBase = Paginator[ListStackRefactorsOutputTypeDef]
else:
    _ListStackRefactorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListStackRefactorsPaginator(_ListStackRefactorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListStackRefactors.html#CloudFormation.Paginator.ListStackRefactors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#liststackrefactorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStackRefactorsInputPaginateTypeDef]
    ) -> PageIterator[ListStackRefactorsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListStackRefactors.html#CloudFormation.Paginator.ListStackRefactors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#liststackrefactorspaginator)
        """

if TYPE_CHECKING:
    _ListStackResourcesPaginatorBase = Paginator[ListStackResourcesOutputTypeDef]
else:
    _ListStackResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListStackResourcesPaginator(_ListStackResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListStackResources.html#CloudFormation.Paginator.ListStackResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#liststackresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStackResourcesInputPaginateTypeDef]
    ) -> PageIterator[ListStackResourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListStackResources.html#CloudFormation.Paginator.ListStackResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#liststackresourcespaginator)
        """

if TYPE_CHECKING:
    _ListStackSetOperationResultsPaginatorBase = Paginator[
        ListStackSetOperationResultsOutputTypeDef
    ]
else:
    _ListStackSetOperationResultsPaginatorBase = Paginator  # type: ignore[assignment]

class ListStackSetOperationResultsPaginator(_ListStackSetOperationResultsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListStackSetOperationResults.html#CloudFormation.Paginator.ListStackSetOperationResults)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#liststacksetoperationresultspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStackSetOperationResultsInputPaginateTypeDef]
    ) -> PageIterator[ListStackSetOperationResultsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListStackSetOperationResults.html#CloudFormation.Paginator.ListStackSetOperationResults.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#liststacksetoperationresultspaginator)
        """

if TYPE_CHECKING:
    _ListStackSetOperationsPaginatorBase = Paginator[ListStackSetOperationsOutputTypeDef]
else:
    _ListStackSetOperationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListStackSetOperationsPaginator(_ListStackSetOperationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListStackSetOperations.html#CloudFormation.Paginator.ListStackSetOperations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#liststacksetoperationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStackSetOperationsInputPaginateTypeDef]
    ) -> PageIterator[ListStackSetOperationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListStackSetOperations.html#CloudFormation.Paginator.ListStackSetOperations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#liststacksetoperationspaginator)
        """

if TYPE_CHECKING:
    _ListStackSetsPaginatorBase = Paginator[ListStackSetsOutputTypeDef]
else:
    _ListStackSetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListStackSetsPaginator(_ListStackSetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListStackSets.html#CloudFormation.Paginator.ListStackSets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#liststacksetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStackSetsInputPaginateTypeDef]
    ) -> PageIterator[ListStackSetsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListStackSets.html#CloudFormation.Paginator.ListStackSets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#liststacksetspaginator)
        """

if TYPE_CHECKING:
    _ListStacksPaginatorBase = Paginator[ListStacksOutputTypeDef]
else:
    _ListStacksPaginatorBase = Paginator  # type: ignore[assignment]

class ListStacksPaginator(_ListStacksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListStacks.html#CloudFormation.Paginator.ListStacks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#liststackspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStacksInputPaginateTypeDef]
    ) -> PageIterator[ListStacksOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListStacks.html#CloudFormation.Paginator.ListStacks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#liststackspaginator)
        """

if TYPE_CHECKING:
    _ListTypesPaginatorBase = Paginator[ListTypesOutputTypeDef]
else:
    _ListTypesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTypesPaginator(_ListTypesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListTypes.html#CloudFormation.Paginator.ListTypes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#listtypespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTypesInputPaginateTypeDef]
    ) -> PageIterator[ListTypesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/paginator/ListTypes.html#CloudFormation.Paginator.ListTypes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/paginators/#listtypespaginator)
        """
