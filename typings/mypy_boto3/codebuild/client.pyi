"""
Type annotations for codebuild service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_codebuild import CodeBuildClient

    client: CodeBuildClient = boto3.client("codebuild")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AuthTypeType,
    ComputeTypeType,
    EnvironmentTypeType,
    ImagePullCredentialsTypeType,
    ProjectSortByTypeType,
    ProjectVisibilityTypeType,
    ReportCodeCoverageSortByTypeType,
    ReportGroupSortByTypeType,
    ReportGroupTrendFieldTypeType,
    ReportTypeType,
    RetryBuildBatchTypeType,
    ServerTypeType,
    SharedResourceSortByTypeType,
    SortOrderTypeType,
    SourceTypeType,
    WebhookBuildTypeType,
)
from .paginator import (
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
from .type_defs import (
    BatchDeleteBuildsOutputTypeDef,
    BatchGetBuildBatchesOutputTypeDef,
    BatchGetBuildsOutputTypeDef,
    BatchGetProjectsOutputTypeDef,
    BatchGetReportGroupsOutputTypeDef,
    BatchGetReportsOutputTypeDef,
    BuildBatchFilterTypeDef,
    BuildStatusConfigTypeDef,
    CreateProjectOutputTypeDef,
    CreateReportGroupOutputTypeDef,
    CreateWebhookOutputTypeDef,
    DeleteBuildBatchOutputTypeDef,
    DeleteSourceCredentialsOutputTypeDef,
    DescribeCodeCoveragesOutputTypeDef,
    DescribeTestCasesOutputTypeDef,
    EnvironmentVariableTypeDef,
    GetReportGroupTrendOutputTypeDef,
    GetResourcePolicyOutputTypeDef,
    GitSubmodulesConfigTypeDef,
    ImportSourceCredentialsOutputTypeDef,
    ListBuildBatchesForProjectOutputTypeDef,
    ListBuildBatchesOutputTypeDef,
    ListBuildsForProjectOutputTypeDef,
    ListBuildsOutputTypeDef,
    ListCuratedEnvironmentImagesOutputTypeDef,
    ListProjectsOutputTypeDef,
    ListReportGroupsOutputTypeDef,
    ListReportsForReportGroupOutputTypeDef,
    ListReportsOutputTypeDef,
    ListSharedProjectsOutputTypeDef,
    ListSharedReportGroupsOutputTypeDef,
    ListSourceCredentialsOutputTypeDef,
    LogsConfigTypeDef,
    ProjectArtifactsTypeDef,
    ProjectBuildBatchConfigTypeDef,
    ProjectCacheTypeDef,
    ProjectEnvironmentTypeDef,
    ProjectFileSystemLocationTypeDef,
    ProjectSourceTypeDef,
    ProjectSourceVersionTypeDef,
    PutResourcePolicyOutputTypeDef,
    RegistryCredentialTypeDef,
    ReportExportConfigTypeDef,
    ReportFilterTypeDef,
    RetryBuildBatchOutputTypeDef,
    RetryBuildOutputTypeDef,
    SourceAuthTypeDef,
    StartBuildBatchOutputTypeDef,
    StartBuildOutputTypeDef,
    StopBuildBatchOutputTypeDef,
    StopBuildOutputTypeDef,
    TagTypeDef,
    TestCaseFilterTypeDef,
    UpdateProjectOutputTypeDef,
    UpdateProjectVisibilityOutputTypeDef,
    UpdateReportGroupOutputTypeDef,
    UpdateWebhookOutputTypeDef,
    VpcConfigTypeDef,
    WebhookFilterTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CodeBuildClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccountLimitExceededException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    OAuthProviderException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class CodeBuildClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        CodeBuildClient exceptions.
        """
    def batch_delete_builds(self, *, ids: List[str]) -> BatchDeleteBuildsOutputTypeDef:
        """
        Deletes one or more builds.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.batch_delete_builds)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#batch_delete_builds)
        """
    def batch_get_build_batches(self, *, ids: List[str]) -> BatchGetBuildBatchesOutputTypeDef:
        """
        Retrieves information about one or more batch builds.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.batch_get_build_batches)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#batch_get_build_batches)
        """
    def batch_get_builds(self, *, ids: List[str]) -> BatchGetBuildsOutputTypeDef:
        """
        Gets information about one or more builds.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.batch_get_builds)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#batch_get_builds)
        """
    def batch_get_projects(self, *, names: List[str]) -> BatchGetProjectsOutputTypeDef:
        """
        Gets information about one or more build projects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.batch_get_projects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#batch_get_projects)
        """
    def batch_get_report_groups(
        self, *, reportGroupArns: List[str]
    ) -> BatchGetReportGroupsOutputTypeDef:
        """
        Returns an array of report groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.batch_get_report_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#batch_get_report_groups)
        """
    def batch_get_reports(self, *, reportArns: List[str]) -> BatchGetReportsOutputTypeDef:
        """
        Returns an array of reports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.batch_get_reports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#batch_get_reports)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#can_paginate)
        """
    def create_project(
        self,
        *,
        name: str,
        source: "ProjectSourceTypeDef",
        artifacts: "ProjectArtifactsTypeDef",
        environment: "ProjectEnvironmentTypeDef",
        serviceRole: str,
        description: str = None,
        secondarySources: List["ProjectSourceTypeDef"] = None,
        sourceVersion: str = None,
        secondarySourceVersions: List["ProjectSourceVersionTypeDef"] = None,
        secondaryArtifacts: List["ProjectArtifactsTypeDef"] = None,
        cache: "ProjectCacheTypeDef" = None,
        timeoutInMinutes: int = None,
        queuedTimeoutInMinutes: int = None,
        encryptionKey: str = None,
        tags: List["TagTypeDef"] = None,
        vpcConfig: "VpcConfigTypeDef" = None,
        badgeEnabled: bool = None,
        logsConfig: "LogsConfigTypeDef" = None,
        fileSystemLocations: List["ProjectFileSystemLocationTypeDef"] = None,
        buildBatchConfig: "ProjectBuildBatchConfigTypeDef" = None,
        concurrentBuildLimit: int = None
    ) -> CreateProjectOutputTypeDef:
        """
        Creates a build project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.create_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#create_project)
        """
    def create_report_group(
        self,
        *,
        name: str,
        type: ReportTypeType,
        exportConfig: "ReportExportConfigTypeDef",
        tags: List["TagTypeDef"] = None
    ) -> CreateReportGroupOutputTypeDef:
        """
        Creates a report group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.create_report_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#create_report_group)
        """
    def create_webhook(
        self,
        *,
        projectName: str,
        branchFilter: str = None,
        filterGroups: List[List["WebhookFilterTypeDef"]] = None,
        buildType: WebhookBuildTypeType = None
    ) -> CreateWebhookOutputTypeDef:
        """
        For an existing CodeBuild build project that has its source code stored in a
        GitHub or Bitbucket repository, enables CodeBuild to start rebuilding the source
        code every time a code change is pushed to the repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.create_webhook)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#create_webhook)
        """
    def delete_build_batch(self, *, id: str) -> DeleteBuildBatchOutputTypeDef:
        """
        Deletes a batch build.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.delete_build_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#delete_build_batch)
        """
    def delete_project(self, *, name: str) -> Dict[str, Any]:
        """
        Deletes a build project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.delete_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#delete_project)
        """
    def delete_report(self, *, arn: str) -> Dict[str, Any]:
        """
        Deletes a report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.delete_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#delete_report)
        """
    def delete_report_group(self, *, arn: str, deleteReports: bool = None) -> Dict[str, Any]:
        """
        Deletes a report group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.delete_report_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#delete_report_group)
        """
    def delete_resource_policy(self, *, resourceArn: str) -> Dict[str, Any]:
        """
        Deletes a resource policy that is identified by its resource ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#delete_resource_policy)
        """
    def delete_source_credentials(self, *, arn: str) -> DeleteSourceCredentialsOutputTypeDef:
        """
        Deletes a set of GitHub, GitHub Enterprise, or Bitbucket source credentials.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.delete_source_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#delete_source_credentials)
        """
    def delete_webhook(self, *, projectName: str) -> Dict[str, Any]:
        """
        For an existing CodeBuild build project that has its source code stored in a
        GitHub or Bitbucket repository, stops CodeBuild from rebuilding the source code
        every time a code change is pushed to the repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.delete_webhook)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#delete_webhook)
        """
    def describe_code_coverages(
        self,
        *,
        reportArn: str,
        nextToken: str = None,
        maxResults: int = None,
        sortOrder: SortOrderTypeType = None,
        sortBy: ReportCodeCoverageSortByTypeType = None,
        minLineCoveragePercentage: float = None,
        maxLineCoveragePercentage: float = None
    ) -> DescribeCodeCoveragesOutputTypeDef:
        """
        Retrieves one or more code coverage reports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.describe_code_coverages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#describe_code_coverages)
        """
    def describe_test_cases(
        self,
        *,
        reportArn: str,
        nextToken: str = None,
        maxResults: int = None,
        filter: "TestCaseFilterTypeDef" = None
    ) -> DescribeTestCasesOutputTypeDef:
        """
        Returns a list of details about test cases for a report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.describe_test_cases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#describe_test_cases)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#generate_presigned_url)
        """
    def get_report_group_trend(
        self,
        *,
        reportGroupArn: str,
        trendField: ReportGroupTrendFieldTypeType,
        numOfReports: int = None
    ) -> GetReportGroupTrendOutputTypeDef:
        """
        Analyzes and accumulates test report values for the specified test reports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.get_report_group_trend)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#get_report_group_trend)
        """
    def get_resource_policy(self, *, resourceArn: str) -> GetResourcePolicyOutputTypeDef:
        """
        Gets a resource policy that is identified by its resource ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.get_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#get_resource_policy)
        """
    def import_source_credentials(
        self,
        *,
        token: str,
        serverType: ServerTypeType,
        authType: AuthTypeType,
        username: str = None,
        shouldOverwrite: bool = None
    ) -> ImportSourceCredentialsOutputTypeDef:
        """
        Imports the source repository credentials for an CodeBuild project that has its
        source code stored in a GitHub, GitHub Enterprise, or Bitbucket repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.import_source_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#import_source_credentials)
        """
    def invalidate_project_cache(self, *, projectName: str) -> Dict[str, Any]:
        """
        Resets the cache for a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.invalidate_project_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#invalidate_project_cache)
        """
    def list_build_batches(
        self,
        *,
        filter: "BuildBatchFilterTypeDef" = None,
        maxResults: int = None,
        sortOrder: SortOrderTypeType = None,
        nextToken: str = None
    ) -> ListBuildBatchesOutputTypeDef:
        """
        Retrieves the identifiers of your build batches in the current region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.list_build_batches)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list_build_batches)
        """
    def list_build_batches_for_project(
        self,
        *,
        projectName: str = None,
        filter: "BuildBatchFilterTypeDef" = None,
        maxResults: int = None,
        sortOrder: SortOrderTypeType = None,
        nextToken: str = None
    ) -> ListBuildBatchesForProjectOutputTypeDef:
        """
        Retrieves the identifiers of the build batches for a specific project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.list_build_batches_for_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list_build_batches_for_project)
        """
    def list_builds(
        self, *, sortOrder: SortOrderTypeType = None, nextToken: str = None
    ) -> ListBuildsOutputTypeDef:
        """
        Gets a list of build IDs, with each build ID representing a single build.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.list_builds)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list_builds)
        """
    def list_builds_for_project(
        self, *, projectName: str, sortOrder: SortOrderTypeType = None, nextToken: str = None
    ) -> ListBuildsForProjectOutputTypeDef:
        """
        Gets a list of build identifiers for the specified build project, with each
        build identifier representing a single build.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.list_builds_for_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list_builds_for_project)
        """
    def list_curated_environment_images(self) -> ListCuratedEnvironmentImagesOutputTypeDef:
        """
        Gets information about Docker images that are managed by CodeBuild.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.list_curated_environment_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list_curated_environment_images)
        """
    def list_projects(
        self,
        *,
        sortBy: ProjectSortByTypeType = None,
        sortOrder: SortOrderTypeType = None,
        nextToken: str = None
    ) -> ListProjectsOutputTypeDef:
        """
        Gets a list of build project names, with each build project name representing a
        single build project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.list_projects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list_projects)
        """
    def list_report_groups(
        self,
        *,
        sortOrder: SortOrderTypeType = None,
        sortBy: ReportGroupSortByTypeType = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListReportGroupsOutputTypeDef:
        """
        Gets a list ARNs for the report groups in the current Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.list_report_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list_report_groups)
        """
    def list_reports(
        self,
        *,
        sortOrder: SortOrderTypeType = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: "ReportFilterTypeDef" = None
    ) -> ListReportsOutputTypeDef:
        """
        Returns a list of ARNs for the reports in the current Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.list_reports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list_reports)
        """
    def list_reports_for_report_group(
        self,
        *,
        reportGroupArn: str,
        nextToken: str = None,
        sortOrder: SortOrderTypeType = None,
        maxResults: int = None,
        filter: "ReportFilterTypeDef" = None
    ) -> ListReportsForReportGroupOutputTypeDef:
        """
        Returns a list of ARNs for the reports that belong to a `ReportGroup` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.list_reports_for_report_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list_reports_for_report_group)
        """
    def list_shared_projects(
        self,
        *,
        sortBy: SharedResourceSortByTypeType = None,
        sortOrder: SortOrderTypeType = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListSharedProjectsOutputTypeDef:
        """
        Gets a list of projects that are shared with other Amazon Web Services accounts
        or users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.list_shared_projects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list_shared_projects)
        """
    def list_shared_report_groups(
        self,
        *,
        sortOrder: SortOrderTypeType = None,
        sortBy: SharedResourceSortByTypeType = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListSharedReportGroupsOutputTypeDef:
        """
        Gets a list of report groups that are shared with other Amazon Web Services
        accounts or users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.list_shared_report_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list_shared_report_groups)
        """
    def list_source_credentials(self) -> ListSourceCredentialsOutputTypeDef:
        """
        Returns a list of `SourceCredentialsInfo` objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.list_source_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list_source_credentials)
        """
    def put_resource_policy(
        self, *, policy: str, resourceArn: str
    ) -> PutResourcePolicyOutputTypeDef:
        """
        Stores a resource policy for the ARN of a `Project` or `ReportGroup` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#put_resource_policy)
        """
    def retry_build(
        self, *, id: str = None, idempotencyToken: str = None
    ) -> RetryBuildOutputTypeDef:
        """
        Restarts a build.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.retry_build)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#retry_build)
        """
    def retry_build_batch(
        self,
        *,
        id: str = None,
        idempotencyToken: str = None,
        retryType: RetryBuildBatchTypeType = None
    ) -> RetryBuildBatchOutputTypeDef:
        """
        Restarts a failed batch build.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.retry_build_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#retry_build_batch)
        """
    def start_build(
        self,
        *,
        projectName: str,
        secondarySourcesOverride: List["ProjectSourceTypeDef"] = None,
        secondarySourcesVersionOverride: List["ProjectSourceVersionTypeDef"] = None,
        sourceVersion: str = None,
        artifactsOverride: "ProjectArtifactsTypeDef" = None,
        secondaryArtifactsOverride: List["ProjectArtifactsTypeDef"] = None,
        environmentVariablesOverride: List["EnvironmentVariableTypeDef"] = None,
        sourceTypeOverride: SourceTypeType = None,
        sourceLocationOverride: str = None,
        sourceAuthOverride: "SourceAuthTypeDef" = None,
        gitCloneDepthOverride: int = None,
        gitSubmodulesConfigOverride: "GitSubmodulesConfigTypeDef" = None,
        buildspecOverride: str = None,
        insecureSslOverride: bool = None,
        reportBuildStatusOverride: bool = None,
        buildStatusConfigOverride: "BuildStatusConfigTypeDef" = None,
        environmentTypeOverride: EnvironmentTypeType = None,
        imageOverride: str = None,
        computeTypeOverride: ComputeTypeType = None,
        certificateOverride: str = None,
        cacheOverride: "ProjectCacheTypeDef" = None,
        serviceRoleOverride: str = None,
        privilegedModeOverride: bool = None,
        timeoutInMinutesOverride: int = None,
        queuedTimeoutInMinutesOverride: int = None,
        encryptionKeyOverride: str = None,
        idempotencyToken: str = None,
        logsConfigOverride: "LogsConfigTypeDef" = None,
        registryCredentialOverride: "RegistryCredentialTypeDef" = None,
        imagePullCredentialsTypeOverride: ImagePullCredentialsTypeType = None,
        debugSessionEnabled: bool = None
    ) -> StartBuildOutputTypeDef:
        """
        Starts running a build.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.start_build)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#start_build)
        """
    def start_build_batch(
        self,
        *,
        projectName: str,
        secondarySourcesOverride: List["ProjectSourceTypeDef"] = None,
        secondarySourcesVersionOverride: List["ProjectSourceVersionTypeDef"] = None,
        sourceVersion: str = None,
        artifactsOverride: "ProjectArtifactsTypeDef" = None,
        secondaryArtifactsOverride: List["ProjectArtifactsTypeDef"] = None,
        environmentVariablesOverride: List["EnvironmentVariableTypeDef"] = None,
        sourceTypeOverride: SourceTypeType = None,
        sourceLocationOverride: str = None,
        sourceAuthOverride: "SourceAuthTypeDef" = None,
        gitCloneDepthOverride: int = None,
        gitSubmodulesConfigOverride: "GitSubmodulesConfigTypeDef" = None,
        buildspecOverride: str = None,
        insecureSslOverride: bool = None,
        reportBuildBatchStatusOverride: bool = None,
        environmentTypeOverride: EnvironmentTypeType = None,
        imageOverride: str = None,
        computeTypeOverride: ComputeTypeType = None,
        certificateOverride: str = None,
        cacheOverride: "ProjectCacheTypeDef" = None,
        serviceRoleOverride: str = None,
        privilegedModeOverride: bool = None,
        buildTimeoutInMinutesOverride: int = None,
        queuedTimeoutInMinutesOverride: int = None,
        encryptionKeyOverride: str = None,
        idempotencyToken: str = None,
        logsConfigOverride: "LogsConfigTypeDef" = None,
        registryCredentialOverride: "RegistryCredentialTypeDef" = None,
        imagePullCredentialsTypeOverride: ImagePullCredentialsTypeType = None,
        buildBatchConfigOverride: "ProjectBuildBatchConfigTypeDef" = None,
        debugSessionEnabled: bool = None
    ) -> StartBuildBatchOutputTypeDef:
        """
        Starts a batch build for a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.start_build_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#start_build_batch)
        """
    def stop_build(self, *, id: str) -> StopBuildOutputTypeDef:
        """
        Attempts to stop running a build.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.stop_build)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#stop_build)
        """
    def stop_build_batch(self, *, id: str) -> StopBuildBatchOutputTypeDef:
        """
        Stops a running batch build.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.stop_build_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#stop_build_batch)
        """
    def update_project(
        self,
        *,
        name: str,
        description: str = None,
        source: "ProjectSourceTypeDef" = None,
        secondarySources: List["ProjectSourceTypeDef"] = None,
        sourceVersion: str = None,
        secondarySourceVersions: List["ProjectSourceVersionTypeDef"] = None,
        artifacts: "ProjectArtifactsTypeDef" = None,
        secondaryArtifacts: List["ProjectArtifactsTypeDef"] = None,
        cache: "ProjectCacheTypeDef" = None,
        environment: "ProjectEnvironmentTypeDef" = None,
        serviceRole: str = None,
        timeoutInMinutes: int = None,
        queuedTimeoutInMinutes: int = None,
        encryptionKey: str = None,
        tags: List["TagTypeDef"] = None,
        vpcConfig: "VpcConfigTypeDef" = None,
        badgeEnabled: bool = None,
        logsConfig: "LogsConfigTypeDef" = None,
        fileSystemLocations: List["ProjectFileSystemLocationTypeDef"] = None,
        buildBatchConfig: "ProjectBuildBatchConfigTypeDef" = None,
        concurrentBuildLimit: int = None
    ) -> UpdateProjectOutputTypeDef:
        """
        Changes the settings of a build project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.update_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#update_project)
        """
    def update_project_visibility(
        self,
        *,
        projectArn: str,
        projectVisibility: ProjectVisibilityTypeType,
        resourceAccessRole: str = None
    ) -> UpdateProjectVisibilityOutputTypeDef:
        """
        Changes the public visibility for a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.update_project_visibility)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#update_project_visibility)
        """
    def update_report_group(
        self,
        *,
        arn: str,
        exportConfig: "ReportExportConfigTypeDef" = None,
        tags: List["TagTypeDef"] = None
    ) -> UpdateReportGroupOutputTypeDef:
        """
        Updates a report group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.update_report_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#update_report_group)
        """
    def update_webhook(
        self,
        *,
        projectName: str,
        branchFilter: str = None,
        rotateSecret: bool = None,
        filterGroups: List[List["WebhookFilterTypeDef"]] = None,
        buildType: WebhookBuildTypeType = None
    ) -> UpdateWebhookOutputTypeDef:
        """
        Updates the webhook associated with an CodeBuild build project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Client.update_webhook)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#update_webhook)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_code_coverages"]
    ) -> DescribeCodeCoveragesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Paginator.DescribeCodeCoverages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#describecodecoveragespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_test_cases"]
    ) -> DescribeTestCasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Paginator.DescribeTestCases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#describetestcasespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_build_batches"]
    ) -> ListBuildBatchesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildBatches)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listbuildbatchespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_build_batches_for_project"]
    ) -> ListBuildBatchesForProjectPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildBatchesForProject)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listbuildbatchesforprojectpaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_builds"]) -> ListBuildsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Paginator.ListBuilds)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listbuildspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_builds_for_project"]
    ) -> ListBuildsForProjectPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildsForProject)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listbuildsforprojectpaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Paginator.ListProjects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listprojectspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_report_groups"]
    ) -> ListReportGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Paginator.ListReportGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listreportgroupspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_reports"]) -> ListReportsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Paginator.ListReports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listreportspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_reports_for_report_group"]
    ) -> ListReportsForReportGroupPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Paginator.ListReportsForReportGroup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listreportsforreportgrouppaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_shared_projects"]
    ) -> ListSharedProjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Paginator.ListSharedProjects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listsharedprojectspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_shared_report_groups"]
    ) -> ListSharedReportGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/codebuild.html#CodeBuild.Paginator.ListSharedReportGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listsharedreportgroupspaginator)
        """
