"""
Main interface for codebuild service.

Usage::

    ```python
    import boto3
    from mypy_boto3_codebuild import (
        Client,
        CodeBuildClient,
        DescribeCodeCoveragesPaginator,
        DescribeTestCasesPaginator,
        ListBuildBatchesForProjectPaginator,
        ListBuildBatchesPaginator,
        ListBuildsForProjectPaginator,
        ListBuildsPaginator,
        ListProjectsPaginator,
        ListReportGroupsPaginator,
        ListReportsForReportGroupPaginator,
        ListReportsPaginator,
        ListSharedProjectsPaginator,
        ListSharedReportGroupsPaginator,
    )

    session = boto3.Session()

    client: CodeBuildClient = boto3.client("codebuild")
    session_client: CodeBuildClient = session.client("codebuild")

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
from mypy_boto3_codebuild.client import CodeBuildClient
from mypy_boto3_codebuild.paginator import (
    DescribeCodeCoveragesPaginator,
    DescribeTestCasesPaginator,
    ListBuildBatchesForProjectPaginator,
    ListBuildBatchesPaginator,
    ListBuildsForProjectPaginator,
    ListBuildsPaginator,
    ListProjectsPaginator,
    ListReportGroupsPaginator,
    ListReportsForReportGroupPaginator,
    ListReportsPaginator,
    ListSharedProjectsPaginator,
    ListSharedReportGroupsPaginator,
)

Client = CodeBuildClient


__all__ = (
    "Client",
    "CodeBuildClient",
    "DescribeCodeCoveragesPaginator",
    "DescribeTestCasesPaginator",
    "ListBuildBatchesForProjectPaginator",
    "ListBuildBatchesPaginator",
    "ListBuildsForProjectPaginator",
    "ListBuildsPaginator",
    "ListProjectsPaginator",
    "ListReportGroupsPaginator",
    "ListReportsForReportGroupPaginator",
    "ListReportsPaginator",
    "ListSharedProjectsPaginator",
    "ListSharedReportGroupsPaginator",
)
