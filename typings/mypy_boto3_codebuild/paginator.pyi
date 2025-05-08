"""
Type annotations for codebuild service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_codebuild.client import CodeBuildClient
    from mypy_boto3_codebuild.paginator import (
        DescribeCodeCoveragesPaginator,
        DescribeTestCasesPaginator,
        ListBuildBatchesForProjectPaginator,
        ListBuildBatchesPaginator,
        ListBuildsForProjectPaginator,
        ListBuildsPaginator,
        ListCommandExecutionsForSandboxPaginator,
        ListProjectsPaginator,
        ListReportGroupsPaginator,
        ListReportsForReportGroupPaginator,
        ListReportsPaginator,
        ListSandboxesForProjectPaginator,
        ListSandboxesPaginator,
        ListSharedProjectsPaginator,
        ListSharedReportGroupsPaginator,
    )

    session = Session()
    client: CodeBuildClient = session.client("codebuild")

    describe_code_coverages_paginator: DescribeCodeCoveragesPaginator = client.get_paginator("describe_code_coverages")
    describe_test_cases_paginator: DescribeTestCasesPaginator = client.get_paginator("describe_test_cases")
    list_build_batches_for_project_paginator: ListBuildBatchesForProjectPaginator = client.get_paginator("list_build_batches_for_project")
    list_build_batches_paginator: ListBuildBatchesPaginator = client.get_paginator("list_build_batches")
    list_builds_for_project_paginator: ListBuildsForProjectPaginator = client.get_paginator("list_builds_for_project")
    list_builds_paginator: ListBuildsPaginator = client.get_paginator("list_builds")
    list_command_executions_for_sandbox_paginator: ListCommandExecutionsForSandboxPaginator = client.get_paginator("list_command_executions_for_sandbox")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    list_report_groups_paginator: ListReportGroupsPaginator = client.get_paginator("list_report_groups")
    list_reports_for_report_group_paginator: ListReportsForReportGroupPaginator = client.get_paginator("list_reports_for_report_group")
    list_reports_paginator: ListReportsPaginator = client.get_paginator("list_reports")
    list_sandboxes_for_project_paginator: ListSandboxesForProjectPaginator = client.get_paginator("list_sandboxes_for_project")
    list_sandboxes_paginator: ListSandboxesPaginator = client.get_paginator("list_sandboxes")
    list_shared_projects_paginator: ListSharedProjectsPaginator = client.get_paginator("list_shared_projects")
    list_shared_report_groups_paginator: ListSharedReportGroupsPaginator = client.get_paginator("list_shared_report_groups")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeCodeCoveragesInputPaginateTypeDef,
    DescribeCodeCoveragesOutputTypeDef,
    DescribeTestCasesInputPaginateTypeDef,
    DescribeTestCasesOutputTypeDef,
    ListBuildBatchesForProjectInputPaginateTypeDef,
    ListBuildBatchesForProjectOutputTypeDef,
    ListBuildBatchesInputPaginateTypeDef,
    ListBuildBatchesOutputTypeDef,
    ListBuildsForProjectInputPaginateTypeDef,
    ListBuildsForProjectOutputTypeDef,
    ListBuildsInputPaginateTypeDef,
    ListBuildsOutputTypeDef,
    ListCommandExecutionsForSandboxInputPaginateTypeDef,
    ListCommandExecutionsForSandboxOutputTypeDef,
    ListProjectsInputPaginateTypeDef,
    ListProjectsOutputTypeDef,
    ListReportGroupsInputPaginateTypeDef,
    ListReportGroupsOutputTypeDef,
    ListReportsForReportGroupInputPaginateTypeDef,
    ListReportsForReportGroupOutputTypeDef,
    ListReportsInputPaginateTypeDef,
    ListReportsOutputTypeDef,
    ListSandboxesForProjectInputPaginateTypeDef,
    ListSandboxesForProjectOutputTypeDef,
    ListSandboxesInputPaginateTypeDef,
    ListSandboxesOutputTypeDef,
    ListSharedProjectsInputPaginateTypeDef,
    ListSharedProjectsOutputTypeDef,
    ListSharedReportGroupsInputPaginateTypeDef,
    ListSharedReportGroupsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeCodeCoveragesPaginator",
    "DescribeTestCasesPaginator",
    "ListBuildBatchesForProjectPaginator",
    "ListBuildBatchesPaginator",
    "ListBuildsForProjectPaginator",
    "ListBuildsPaginator",
    "ListCommandExecutionsForSandboxPaginator",
    "ListProjectsPaginator",
    "ListReportGroupsPaginator",
    "ListReportsForReportGroupPaginator",
    "ListReportsPaginator",
    "ListSandboxesForProjectPaginator",
    "ListSandboxesPaginator",
    "ListSharedProjectsPaginator",
    "ListSharedReportGroupsPaginator",
)

if TYPE_CHECKING:
    _DescribeCodeCoveragesPaginatorBase = Paginator[DescribeCodeCoveragesOutputTypeDef]
else:
    _DescribeCodeCoveragesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeCodeCoveragesPaginator(_DescribeCodeCoveragesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/DescribeCodeCoverages.html#CodeBuild.Paginator.DescribeCodeCoverages)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#describecodecoveragespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCodeCoveragesInputPaginateTypeDef]
    ) -> PageIterator[DescribeCodeCoveragesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/DescribeCodeCoverages.html#CodeBuild.Paginator.DescribeCodeCoverages.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#describecodecoveragespaginator)
        """

if TYPE_CHECKING:
    _DescribeTestCasesPaginatorBase = Paginator[DescribeTestCasesOutputTypeDef]
else:
    _DescribeTestCasesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTestCasesPaginator(_DescribeTestCasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/DescribeTestCases.html#CodeBuild.Paginator.DescribeTestCases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#describetestcasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTestCasesInputPaginateTypeDef]
    ) -> PageIterator[DescribeTestCasesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/DescribeTestCases.html#CodeBuild.Paginator.DescribeTestCases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#describetestcasespaginator)
        """

if TYPE_CHECKING:
    _ListBuildBatchesForProjectPaginatorBase = Paginator[ListBuildBatchesForProjectOutputTypeDef]
else:
    _ListBuildBatchesForProjectPaginatorBase = Paginator  # type: ignore[assignment]

class ListBuildBatchesForProjectPaginator(_ListBuildBatchesForProjectPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListBuildBatchesForProject.html#CodeBuild.Paginator.ListBuildBatchesForProject)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listbuildbatchesforprojectpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBuildBatchesForProjectInputPaginateTypeDef]
    ) -> PageIterator[ListBuildBatchesForProjectOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListBuildBatchesForProject.html#CodeBuild.Paginator.ListBuildBatchesForProject.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listbuildbatchesforprojectpaginator)
        """

if TYPE_CHECKING:
    _ListBuildBatchesPaginatorBase = Paginator[ListBuildBatchesOutputTypeDef]
else:
    _ListBuildBatchesPaginatorBase = Paginator  # type: ignore[assignment]

class ListBuildBatchesPaginator(_ListBuildBatchesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListBuildBatches.html#CodeBuild.Paginator.ListBuildBatches)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listbuildbatchespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBuildBatchesInputPaginateTypeDef]
    ) -> PageIterator[ListBuildBatchesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListBuildBatches.html#CodeBuild.Paginator.ListBuildBatches.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listbuildbatchespaginator)
        """

if TYPE_CHECKING:
    _ListBuildsForProjectPaginatorBase = Paginator[ListBuildsForProjectOutputTypeDef]
else:
    _ListBuildsForProjectPaginatorBase = Paginator  # type: ignore[assignment]

class ListBuildsForProjectPaginator(_ListBuildsForProjectPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListBuildsForProject.html#CodeBuild.Paginator.ListBuildsForProject)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listbuildsforprojectpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBuildsForProjectInputPaginateTypeDef]
    ) -> PageIterator[ListBuildsForProjectOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListBuildsForProject.html#CodeBuild.Paginator.ListBuildsForProject.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listbuildsforprojectpaginator)
        """

if TYPE_CHECKING:
    _ListBuildsPaginatorBase = Paginator[ListBuildsOutputTypeDef]
else:
    _ListBuildsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBuildsPaginator(_ListBuildsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListBuilds.html#CodeBuild.Paginator.ListBuilds)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listbuildspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBuildsInputPaginateTypeDef]
    ) -> PageIterator[ListBuildsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListBuilds.html#CodeBuild.Paginator.ListBuilds.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listbuildspaginator)
        """

if TYPE_CHECKING:
    _ListCommandExecutionsForSandboxPaginatorBase = Paginator[
        ListCommandExecutionsForSandboxOutputTypeDef
    ]
else:
    _ListCommandExecutionsForSandboxPaginatorBase = Paginator  # type: ignore[assignment]

class ListCommandExecutionsForSandboxPaginator(_ListCommandExecutionsForSandboxPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListCommandExecutionsForSandbox.html#CodeBuild.Paginator.ListCommandExecutionsForSandbox)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listcommandexecutionsforsandboxpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCommandExecutionsForSandboxInputPaginateTypeDef]
    ) -> PageIterator[ListCommandExecutionsForSandboxOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListCommandExecutionsForSandbox.html#CodeBuild.Paginator.ListCommandExecutionsForSandbox.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listcommandexecutionsforsandboxpaginator)
        """

if TYPE_CHECKING:
    _ListProjectsPaginatorBase = Paginator[ListProjectsOutputTypeDef]
else:
    _ListProjectsPaginatorBase = Paginator  # type: ignore[assignment]

class ListProjectsPaginator(_ListProjectsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListProjects.html#CodeBuild.Paginator.ListProjects)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listprojectspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProjectsInputPaginateTypeDef]
    ) -> PageIterator[ListProjectsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListProjects.html#CodeBuild.Paginator.ListProjects.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listprojectspaginator)
        """

if TYPE_CHECKING:
    _ListReportGroupsPaginatorBase = Paginator[ListReportGroupsOutputTypeDef]
else:
    _ListReportGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListReportGroupsPaginator(_ListReportGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListReportGroups.html#CodeBuild.Paginator.ListReportGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listreportgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListReportGroupsInputPaginateTypeDef]
    ) -> PageIterator[ListReportGroupsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListReportGroups.html#CodeBuild.Paginator.ListReportGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listreportgroupspaginator)
        """

if TYPE_CHECKING:
    _ListReportsForReportGroupPaginatorBase = Paginator[ListReportsForReportGroupOutputTypeDef]
else:
    _ListReportsForReportGroupPaginatorBase = Paginator  # type: ignore[assignment]

class ListReportsForReportGroupPaginator(_ListReportsForReportGroupPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListReportsForReportGroup.html#CodeBuild.Paginator.ListReportsForReportGroup)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listreportsforreportgrouppaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListReportsForReportGroupInputPaginateTypeDef]
    ) -> PageIterator[ListReportsForReportGroupOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListReportsForReportGroup.html#CodeBuild.Paginator.ListReportsForReportGroup.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listreportsforreportgrouppaginator)
        """

if TYPE_CHECKING:
    _ListReportsPaginatorBase = Paginator[ListReportsOutputTypeDef]
else:
    _ListReportsPaginatorBase = Paginator  # type: ignore[assignment]

class ListReportsPaginator(_ListReportsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListReports.html#CodeBuild.Paginator.ListReports)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listreportspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListReportsInputPaginateTypeDef]
    ) -> PageIterator[ListReportsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListReports.html#CodeBuild.Paginator.ListReports.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listreportspaginator)
        """

if TYPE_CHECKING:
    _ListSandboxesForProjectPaginatorBase = Paginator[ListSandboxesForProjectOutputTypeDef]
else:
    _ListSandboxesForProjectPaginatorBase = Paginator  # type: ignore[assignment]

class ListSandboxesForProjectPaginator(_ListSandboxesForProjectPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListSandboxesForProject.html#CodeBuild.Paginator.ListSandboxesForProject)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listsandboxesforprojectpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSandboxesForProjectInputPaginateTypeDef]
    ) -> PageIterator[ListSandboxesForProjectOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListSandboxesForProject.html#CodeBuild.Paginator.ListSandboxesForProject.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listsandboxesforprojectpaginator)
        """

if TYPE_CHECKING:
    _ListSandboxesPaginatorBase = Paginator[ListSandboxesOutputTypeDef]
else:
    _ListSandboxesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSandboxesPaginator(_ListSandboxesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListSandboxes.html#CodeBuild.Paginator.ListSandboxes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listsandboxespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSandboxesInputPaginateTypeDef]
    ) -> PageIterator[ListSandboxesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListSandboxes.html#CodeBuild.Paginator.ListSandboxes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listsandboxespaginator)
        """

if TYPE_CHECKING:
    _ListSharedProjectsPaginatorBase = Paginator[ListSharedProjectsOutputTypeDef]
else:
    _ListSharedProjectsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSharedProjectsPaginator(_ListSharedProjectsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListSharedProjects.html#CodeBuild.Paginator.ListSharedProjects)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listsharedprojectspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSharedProjectsInputPaginateTypeDef]
    ) -> PageIterator[ListSharedProjectsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListSharedProjects.html#CodeBuild.Paginator.ListSharedProjects.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listsharedprojectspaginator)
        """

if TYPE_CHECKING:
    _ListSharedReportGroupsPaginatorBase = Paginator[ListSharedReportGroupsOutputTypeDef]
else:
    _ListSharedReportGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSharedReportGroupsPaginator(_ListSharedReportGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListSharedReportGroups.html#CodeBuild.Paginator.ListSharedReportGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listsharedreportgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSharedReportGroupsInputPaginateTypeDef]
    ) -> PageIterator[ListSharedReportGroupsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild/paginator/ListSharedReportGroups.html#CodeBuild.Paginator.ListSharedReportGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators/#listsharedreportgroupspaginator)
        """
