"""
Type annotations for codebuild service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_codebuild import CodeBuildClient
    from mypy_boto3_codebuild.paginator import (
        DescribeCodeCoveragesPaginator,
        DescribeTestCasesPaginator,
        ListBuildBatchesPaginator,
        ListBuildBatchesForProjectPaginator,
        ListBuildsPaginator,
        ListBuildsForProjectPaginator,
        ListProjectsPaginator,
        ListReportGroupsPaginator,
        ListReportsPaginator,
        ListReportsForReportGroupPaginator,
        ListSharedProjectsPaginator,
        ListSharedReportGroupsPaginator,
    )

    client: CodeBuildClient = boto3.client("codebuild")

    describe_code_coverages_paginator: DescribeCodeCoveragesPaginator = client.get_paginator("describe_code_coverages")
    describe_test_cases_paginator: DescribeTestCasesPaginator = client.get_paginator("describe_test_cases")
    list_build_batches_paginator: ListBuildBatchesPaginator = client.get_paginator("list_build_batches")
    list_build_batches_for_project_paginator: ListBuildBatchesForProjectPaginator = client.get_paginator("list_build_batches_for_project")
    list_builds_paginator: ListBuildsPaginator = client.get_paginator("list_builds")
    list_builds_for_project_paginator: ListBuildsForProjectPaginator = client.get_paginator("list_builds_for_project")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    list_report_groups_paginator: ListReportGroupsPaginator = client.get_paginator("list_report_groups")
    list_reports_paginator: ListReportsPaginator = client.get_paginator("list_reports")
    list_reports_for_report_group_paginator: ListReportsForReportGroupPaginator = client.get_paginator("list_reports_for_report_group")
    list_shared_projects_paginator: ListSharedProjectsPaginator = client.get_paginator("list_shared_projects")
    list_shared_report_groups_paginator: ListSharedReportGroupsPaginator = client.get_paginator("list_shared_report_groups")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    ProjectSortByTypeType,
    ReportCodeCoverageSortByTypeType,
    ReportGroupSortByTypeType,
    SharedResourceSortByTypeType,
    SortOrderTypeType,
)
from .type_defs import (
    BuildBatchFilterTypeDef,
    DescribeCodeCoveragesOutputTypeDef,
    DescribeTestCasesOutputTypeDef,
    ListBuildBatchesForProjectOutputTypeDef,
    ListBuildBatchesOutputTypeDef,
    ListBuildsForProjectOutputTypeDef,
    ListBuildsOutputTypeDef,
    ListProjectsOutputTypeDef,
    ListReportGroupsOutputTypeDef,
    ListReportsForReportGroupOutputTypeDef,
    ListReportsOutputTypeDef,
    ListSharedProjectsOutputTypeDef,
    ListSharedReportGroupsOutputTypeDef,
    PaginatorConfigTypeDef,
    ReportFilterTypeDef,
    TestCaseFilterTypeDef,
)

__all__ = (
    "DescribeCodeCoveragesPaginator",
    "DescribeTestCasesPaginator",
    "ListBuildBatchesPaginator",
    "ListBuildBatchesForProjectPaginator",
    "ListBuildsPaginator",
    "ListBuildsForProjectPaginator",
    "ListProjectsPaginator",
    "ListReportGroupsPaginator",
    "ListReportsPaginator",
    "ListReportsForReportGroupPaginator",
    "ListSharedProjectsPaginator",
    "ListSharedReportGroupsPaginator",
)

class DescribeCodeCoveragesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.DescribeCodeCoverages)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#describecodecoveragespaginator)
    """

    def paginate(
        self,
        *,
        reportArn: str,
        sortOrder: SortOrderTypeType = None,
        sortBy: ReportCodeCoverageSortByTypeType = None,
        minLineCoveragePercentage: float = None,
        maxLineCoveragePercentage: float = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeCodeCoveragesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.DescribeCodeCoverages.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#describecodecoveragespaginator)
        """

class DescribeTestCasesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.DescribeTestCases)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#describetestcasespaginator)
    """

    def paginate(
        self,
        *,
        reportArn: str,
        filter: "TestCaseFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTestCasesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.DescribeTestCases.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#describetestcasespaginator)
        """

class ListBuildBatchesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildBatches)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listbuildbatchespaginator)
    """

    def paginate(
        self,
        *,
        filter: "BuildBatchFilterTypeDef" = None,
        sortOrder: SortOrderTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBuildBatchesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildBatches.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listbuildbatchespaginator)
        """

class ListBuildBatchesForProjectPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildBatchesForProject)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listbuildbatchesforprojectpaginator)
    """

    def paginate(
        self,
        *,
        projectName: str = None,
        filter: "BuildBatchFilterTypeDef" = None,
        sortOrder: SortOrderTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBuildBatchesForProjectOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildBatchesForProject.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listbuildbatchesforprojectpaginator)
        """

class ListBuildsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.ListBuilds)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listbuildspaginator)
    """

    def paginate(
        self,
        *,
        sortOrder: SortOrderTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBuildsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.ListBuilds.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listbuildspaginator)
        """

class ListBuildsForProjectPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildsForProject)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listbuildsforprojectpaginator)
    """

    def paginate(
        self,
        *,
        projectName: str,
        sortOrder: SortOrderTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBuildsForProjectOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildsForProject.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listbuildsforprojectpaginator)
        """

class ListProjectsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.ListProjects)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listprojectspaginator)
    """

    def paginate(
        self,
        *,
        sortBy: ProjectSortByTypeType = None,
        sortOrder: SortOrderTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.ListProjects.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listprojectspaginator)
        """

class ListReportGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.ListReportGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listreportgroupspaginator)
    """

    def paginate(
        self,
        *,
        sortOrder: SortOrderTypeType = None,
        sortBy: ReportGroupSortByTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListReportGroupsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.ListReportGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listreportgroupspaginator)
        """

class ListReportsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.ListReports)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listreportspaginator)
    """

    def paginate(
        self,
        *,
        sortOrder: SortOrderTypeType = None,
        filter: "ReportFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListReportsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.ListReports.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listreportspaginator)
        """

class ListReportsForReportGroupPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.ListReportsForReportGroup)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listreportsforreportgrouppaginator)
    """

    def paginate(
        self,
        *,
        reportGroupArn: str,
        sortOrder: SortOrderTypeType = None,
        filter: "ReportFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListReportsForReportGroupOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.ListReportsForReportGroup.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listreportsforreportgrouppaginator)
        """

class ListSharedProjectsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.ListSharedProjects)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listsharedprojectspaginator)
    """

    def paginate(
        self,
        *,
        sortBy: SharedResourceSortByTypeType = None,
        sortOrder: SortOrderTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSharedProjectsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.ListSharedProjects.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listsharedprojectspaginator)
        """

class ListSharedReportGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.ListSharedReportGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listsharedreportgroupspaginator)
    """

    def paginate(
        self,
        *,
        sortOrder: SortOrderTypeType = None,
        sortBy: SharedResourceSortByTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSharedReportGroupsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/codebuild.html#CodeBuild.Paginator.ListSharedReportGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listsharedreportgroupspaginator)
        """
