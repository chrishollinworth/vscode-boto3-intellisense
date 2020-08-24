# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for codebuild service client

Usage::

    ```python
    import boto3
    from mypy_boto3_codebuild import CodeBuildClient

    client: CodeBuildClient = boto3.client("codebuild")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

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
from mypy_boto3_codebuild.type_defs import (
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


class Exceptions:
    AccountLimitExceededException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    InvalidInputException: Type[Boto3ClientError]
    OAuthProviderException: Type[Boto3ClientError]
    ResourceAlreadyExistsException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]


class CodeBuildClient:
    """
    [CodeBuild.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client)
    """

    exceptions: Exceptions

    def batch_delete_builds(self, ids: List[str]) -> BatchDeleteBuildsOutputTypeDef:
        """
        [Client.batch_delete_builds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.batch_delete_builds)
        """

    def batch_get_build_batches(self, ids: List[str]) -> BatchGetBuildBatchesOutputTypeDef:
        """
        [Client.batch_get_build_batches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.batch_get_build_batches)
        """

    def batch_get_builds(self, ids: List[str]) -> BatchGetBuildsOutputTypeDef:
        """
        [Client.batch_get_builds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.batch_get_builds)
        """

    def batch_get_projects(self, names: List[str]) -> BatchGetProjectsOutputTypeDef:
        """
        [Client.batch_get_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.batch_get_projects)
        """

    def batch_get_report_groups(
        self, reportGroupArns: List[str]
    ) -> BatchGetReportGroupsOutputTypeDef:
        """
        [Client.batch_get_report_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.batch_get_report_groups)
        """

    def batch_get_reports(self, reportArns: List[str]) -> BatchGetReportsOutputTypeDef:
        """
        [Client.batch_get_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.batch_get_reports)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.can_paginate)
        """

    def create_project(
        self,
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
    ) -> CreateProjectOutputTypeDef:
        """
        [Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.create_project)
        """

    def create_report_group(
        self,
        name: str,
        type: Literal["TEST", "CODE_COVERAGE"],
        exportConfig: "ReportExportConfigTypeDef",
        tags: List["TagTypeDef"] = None,
    ) -> CreateReportGroupOutputTypeDef:
        """
        [Client.create_report_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.create_report_group)
        """

    def create_webhook(
        self,
        projectName: str,
        branchFilter: str = None,
        filterGroups: List[List["WebhookFilterTypeDef"]] = None,
        buildType: Literal["BUILD", "BUILD_BATCH"] = None,
    ) -> CreateWebhookOutputTypeDef:
        """
        [Client.create_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.create_webhook)
        """

    def delete_build_batch(self, id: str) -> DeleteBuildBatchOutputTypeDef:
        """
        [Client.delete_build_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.delete_build_batch)
        """

    def delete_project(self, name: str) -> Dict[str, Any]:
        """
        [Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.delete_project)
        """

    def delete_report(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.delete_report)
        """

    def delete_report_group(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_report_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.delete_report_group)
        """

    def delete_resource_policy(self, resourceArn: str) -> Dict[str, Any]:
        """
        [Client.delete_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.delete_resource_policy)
        """

    def delete_source_credentials(self, arn: str) -> DeleteSourceCredentialsOutputTypeDef:
        """
        [Client.delete_source_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.delete_source_credentials)
        """

    def delete_webhook(self, projectName: str) -> Dict[str, Any]:
        """
        [Client.delete_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.delete_webhook)
        """

    def describe_code_coverages(
        self,
        reportArn: str,
        nextToken: str = None,
        maxResults: int = None,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        sortBy: Literal["LINE_COVERAGE_PERCENTAGE", "FILE_PATH"] = None,
        minLineCoveragePercentage: float = None,
        maxLineCoveragePercentage: float = None,
    ) -> DescribeCodeCoveragesOutputTypeDef:
        """
        [Client.describe_code_coverages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.describe_code_coverages)
        """

    def describe_test_cases(
        self,
        reportArn: str,
        nextToken: str = None,
        maxResults: int = None,
        filter: TestCaseFilterTypeDef = None,
    ) -> DescribeTestCasesOutputTypeDef:
        """
        [Client.describe_test_cases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.describe_test_cases)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.generate_presigned_url)
        """

    def get_resource_policy(self, resourceArn: str) -> GetResourcePolicyOutputTypeDef:
        """
        [Client.get_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.get_resource_policy)
        """

    def import_source_credentials(
        self,
        token: str,
        serverType: Literal["GITHUB", "BITBUCKET", "GITHUB_ENTERPRISE"],
        authType: Literal["OAUTH", "BASIC_AUTH", "PERSONAL_ACCESS_TOKEN"],
        username: str = None,
        shouldOverwrite: bool = None,
    ) -> ImportSourceCredentialsOutputTypeDef:
        """
        [Client.import_source_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.import_source_credentials)
        """

    def invalidate_project_cache(self, projectName: str) -> Dict[str, Any]:
        """
        [Client.invalidate_project_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.invalidate_project_cache)
        """

    def list_build_batches(
        self,
        filter: BuildBatchFilterTypeDef = None,
        maxResults: int = None,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        nextToken: str = None,
    ) -> ListBuildBatchesOutputTypeDef:
        """
        [Client.list_build_batches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.list_build_batches)
        """

    def list_build_batches_for_project(
        self,
        projectName: str = None,
        filter: BuildBatchFilterTypeDef = None,
        maxResults: int = None,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        nextToken: str = None,
    ) -> ListBuildBatchesForProjectOutputTypeDef:
        """
        [Client.list_build_batches_for_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.list_build_batches_for_project)
        """

    def list_builds(
        self, sortOrder: Literal["ASCENDING", "DESCENDING"] = None, nextToken: str = None
    ) -> ListBuildsOutputTypeDef:
        """
        [Client.list_builds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.list_builds)
        """

    def list_builds_for_project(
        self,
        projectName: str,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        nextToken: str = None,
    ) -> ListBuildsForProjectOutputTypeDef:
        """
        [Client.list_builds_for_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.list_builds_for_project)
        """

    def list_curated_environment_images(self) -> ListCuratedEnvironmentImagesOutputTypeDef:
        """
        [Client.list_curated_environment_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.list_curated_environment_images)
        """

    def list_projects(
        self,
        sortBy: Literal["NAME", "CREATED_TIME", "LAST_MODIFIED_TIME"] = None,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        nextToken: str = None,
    ) -> ListProjectsOutputTypeDef:
        """
        [Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.list_projects)
        """

    def list_report_groups(
        self,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        sortBy: Literal["NAME", "CREATED_TIME", "LAST_MODIFIED_TIME"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListReportGroupsOutputTypeDef:
        """
        [Client.list_report_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.list_report_groups)
        """

    def list_reports(
        self,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: ReportFilterTypeDef = None,
    ) -> ListReportsOutputTypeDef:
        """
        [Client.list_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.list_reports)
        """

    def list_reports_for_report_group(
        self,
        reportGroupArn: str,
        nextToken: str = None,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        maxResults: int = None,
        filter: ReportFilterTypeDef = None,
    ) -> ListReportsForReportGroupOutputTypeDef:
        """
        [Client.list_reports_for_report_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.list_reports_for_report_group)
        """

    def list_shared_projects(
        self,
        sortBy: Literal["ARN", "MODIFIED_TIME"] = None,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListSharedProjectsOutputTypeDef:
        """
        [Client.list_shared_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.list_shared_projects)
        """

    def list_shared_report_groups(
        self,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        sortBy: Literal["ARN", "MODIFIED_TIME"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListSharedReportGroupsOutputTypeDef:
        """
        [Client.list_shared_report_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.list_shared_report_groups)
        """

    def list_source_credentials(self) -> ListSourceCredentialsOutputTypeDef:
        """
        [Client.list_source_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.list_source_credentials)
        """

    def put_resource_policy(self, policy: str, resourceArn: str) -> PutResourcePolicyOutputTypeDef:
        """
        [Client.put_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.put_resource_policy)
        """

    def retry_build(self, id: str = None, idempotencyToken: str = None) -> RetryBuildOutputTypeDef:
        """
        [Client.retry_build documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.retry_build)
        """

    def retry_build_batch(
        self,
        id: str = None,
        idempotencyToken: str = None,
        retryType: Literal["RETRY_ALL_BUILDS", "RETRY_FAILED_BUILDS"] = None,
    ) -> RetryBuildBatchOutputTypeDef:
        """
        [Client.retry_build_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.retry_build_batch)
        """

    def start_build(
        self,
        projectName: str,
        secondarySourcesOverride: List["ProjectSourceTypeDef"] = None,
        secondarySourcesVersionOverride: List["ProjectSourceVersionTypeDef"] = None,
        sourceVersion: str = None,
        artifactsOverride: "ProjectArtifactsTypeDef" = None,
        secondaryArtifactsOverride: List["ProjectArtifactsTypeDef"] = None,
        environmentVariablesOverride: List["EnvironmentVariableTypeDef"] = None,
        sourceTypeOverride: Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ] = None,
        sourceLocationOverride: str = None,
        sourceAuthOverride: "SourceAuthTypeDef" = None,
        gitCloneDepthOverride: int = None,
        gitSubmodulesConfigOverride: "GitSubmodulesConfigTypeDef" = None,
        buildspecOverride: str = None,
        insecureSslOverride: bool = None,
        reportBuildStatusOverride: bool = None,
        buildStatusConfigOverride: "BuildStatusConfigTypeDef" = None,
        environmentTypeOverride: Literal[
            "WINDOWS_CONTAINER",
            "LINUX_CONTAINER",
            "LINUX_GPU_CONTAINER",
            "ARM_CONTAINER",
            "WINDOWS_SERVER_2019_CONTAINER",
        ] = None,
        imageOverride: str = None,
        computeTypeOverride: Literal[
            "BUILD_GENERAL1_SMALL",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_2XLARGE",
        ] = None,
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
        imagePullCredentialsTypeOverride: Literal["CODEBUILD", "SERVICE_ROLE"] = None,
        debugSessionEnabled: bool = None,
    ) -> StartBuildOutputTypeDef:
        """
        [Client.start_build documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.start_build)
        """

    def start_build_batch(
        self,
        projectName: str,
        secondarySourcesOverride: List["ProjectSourceTypeDef"] = None,
        secondarySourcesVersionOverride: List["ProjectSourceVersionTypeDef"] = None,
        sourceVersion: str = None,
        artifactsOverride: "ProjectArtifactsTypeDef" = None,
        secondaryArtifactsOverride: List["ProjectArtifactsTypeDef"] = None,
        environmentVariablesOverride: List["EnvironmentVariableTypeDef"] = None,
        sourceTypeOverride: Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ] = None,
        sourceLocationOverride: str = None,
        sourceAuthOverride: "SourceAuthTypeDef" = None,
        gitCloneDepthOverride: int = None,
        gitSubmodulesConfigOverride: "GitSubmodulesConfigTypeDef" = None,
        buildspecOverride: str = None,
        insecureSslOverride: bool = None,
        reportBuildBatchStatusOverride: bool = None,
        environmentTypeOverride: Literal[
            "WINDOWS_CONTAINER",
            "LINUX_CONTAINER",
            "LINUX_GPU_CONTAINER",
            "ARM_CONTAINER",
            "WINDOWS_SERVER_2019_CONTAINER",
        ] = None,
        imageOverride: str = None,
        computeTypeOverride: Literal[
            "BUILD_GENERAL1_SMALL",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_2XLARGE",
        ] = None,
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
        imagePullCredentialsTypeOverride: Literal["CODEBUILD", "SERVICE_ROLE"] = None,
        buildBatchConfigOverride: "ProjectBuildBatchConfigTypeDef" = None,
    ) -> StartBuildBatchOutputTypeDef:
        """
        [Client.start_build_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.start_build_batch)
        """

    def stop_build(self, id: str) -> StopBuildOutputTypeDef:
        """
        [Client.stop_build documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.stop_build)
        """

    def stop_build_batch(self, id: str) -> StopBuildBatchOutputTypeDef:
        """
        [Client.stop_build_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.stop_build_batch)
        """

    def update_project(
        self,
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
    ) -> UpdateProjectOutputTypeDef:
        """
        [Client.update_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.update_project)
        """

    def update_report_group(
        self,
        arn: str,
        exportConfig: "ReportExportConfigTypeDef" = None,
        tags: List["TagTypeDef"] = None,
    ) -> UpdateReportGroupOutputTypeDef:
        """
        [Client.update_report_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.update_report_group)
        """

    def update_webhook(
        self,
        projectName: str,
        branchFilter: str = None,
        rotateSecret: bool = None,
        filterGroups: List[List["WebhookFilterTypeDef"]] = None,
        buildType: Literal["BUILD", "BUILD_BATCH"] = None,
    ) -> UpdateWebhookOutputTypeDef:
        """
        [Client.update_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Client.update_webhook)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_code_coverages"]
    ) -> DescribeCodeCoveragesPaginator:
        """
        [Paginator.DescribeCodeCoverages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Paginator.DescribeCodeCoverages)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_test_cases"]
    ) -> DescribeTestCasesPaginator:
        """
        [Paginator.DescribeTestCases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Paginator.DescribeTestCases)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_build_batches"]
    ) -> ListBuildBatchesPaginator:
        """
        [Paginator.ListBuildBatches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildBatches)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_build_batches_for_project"]
    ) -> ListBuildBatchesForProjectPaginator:
        """
        [Paginator.ListBuildBatchesForProject documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildBatchesForProject)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_builds"]) -> ListBuildsPaginator:
        """
        [Paginator.ListBuilds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Paginator.ListBuilds)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_builds_for_project"]
    ) -> ListBuildsForProjectPaginator:
        """
        [Paginator.ListBuildsForProject documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildsForProject)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Paginator.ListProjects)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_report_groups"]
    ) -> ListReportGroupsPaginator:
        """
        [Paginator.ListReportGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Paginator.ListReportGroups)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_reports"]) -> ListReportsPaginator:
        """
        [Paginator.ListReports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Paginator.ListReports)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_reports_for_report_group"]
    ) -> ListReportsForReportGroupPaginator:
        """
        [Paginator.ListReportsForReportGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Paginator.ListReportsForReportGroup)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_shared_projects"]
    ) -> ListSharedProjectsPaginator:
        """
        [Paginator.ListSharedProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Paginator.ListSharedProjects)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_shared_report_groups"]
    ) -> ListSharedReportGroupsPaginator:
        """
        [Paginator.ListSharedReportGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codebuild.html#CodeBuild.Paginator.ListSharedReportGroups)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
