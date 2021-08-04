"""
Type annotations for codebuild service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/literals.html)

Usage::

    ```python
    from mypy_boto3_codebuild.literals import ArtifactNamespaceType

    data: ArtifactNamespaceType = "BUILD_ID"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ArtifactNamespaceType",
    "ArtifactPackagingType",
    "ArtifactsTypeType",
    "AuthTypeType",
    "BucketOwnerAccessType",
    "BuildBatchPhaseTypeType",
    "BuildPhaseTypeType",
    "CacheModeType",
    "CacheTypeType",
    "ComputeTypeType",
    "CredentialProviderTypeType",
    "DescribeCodeCoveragesPaginatorName",
    "DescribeTestCasesPaginatorName",
    "EnvironmentTypeType",
    "EnvironmentVariableTypeType",
    "FileSystemTypeType",
    "ImagePullCredentialsTypeType",
    "LanguageTypeType",
    "ListBuildBatchesForProjectPaginatorName",
    "ListBuildBatchesPaginatorName",
    "ListBuildsForProjectPaginatorName",
    "ListBuildsPaginatorName",
    "ListProjectsPaginatorName",
    "ListReportGroupsPaginatorName",
    "ListReportsForReportGroupPaginatorName",
    "ListReportsPaginatorName",
    "ListSharedProjectsPaginatorName",
    "ListSharedReportGroupsPaginatorName",
    "LogsConfigStatusTypeType",
    "PlatformTypeType",
    "ProjectSortByTypeType",
    "ReportCodeCoverageSortByTypeType",
    "ReportExportConfigTypeType",
    "ReportGroupSortByTypeType",
    "ReportGroupStatusTypeType",
    "ReportGroupTrendFieldTypeType",
    "ReportPackagingTypeType",
    "ReportStatusTypeType",
    "ReportTypeType",
    "RetryBuildBatchTypeType",
    "ServerTypeType",
    "SharedResourceSortByTypeType",
    "SortOrderTypeType",
    "SourceAuthTypeType",
    "SourceTypeType",
    "StatusTypeType",
    "WebhookBuildTypeType",
    "WebhookFilterTypeType",
)

ArtifactNamespaceType = Literal["BUILD_ID", "NONE"]
ArtifactPackagingType = Literal["NONE", "ZIP"]
ArtifactsTypeType = Literal["CODEPIPELINE", "NO_ARTIFACTS", "S3"]
AuthTypeType = Literal["BASIC_AUTH", "OAUTH", "PERSONAL_ACCESS_TOKEN"]
BucketOwnerAccessType = Literal["FULL", "NONE", "READ_ONLY"]
BuildBatchPhaseTypeType = Literal[
    "COMBINE_ARTIFACTS",
    "DOWNLOAD_BATCHSPEC",
    "FAILED",
    "IN_PROGRESS",
    "STOPPED",
    "SUBMITTED",
    "SUCCEEDED",
]
BuildPhaseTypeType = Literal[
    "BUILD",
    "COMPLETED",
    "DOWNLOAD_SOURCE",
    "FINALIZING",
    "INSTALL",
    "POST_BUILD",
    "PRE_BUILD",
    "PROVISIONING",
    "QUEUED",
    "SUBMITTED",
    "UPLOAD_ARTIFACTS",
]
CacheModeType = Literal["LOCAL_CUSTOM_CACHE", "LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE"]
CacheTypeType = Literal["LOCAL", "NO_CACHE", "S3"]
ComputeTypeType = Literal[
    "BUILD_GENERAL1_2XLARGE",
    "BUILD_GENERAL1_LARGE",
    "BUILD_GENERAL1_MEDIUM",
    "BUILD_GENERAL1_SMALL",
]
CredentialProviderTypeType = Literal["SECRETS_MANAGER"]
DescribeCodeCoveragesPaginatorName = Literal["describe_code_coverages"]
DescribeTestCasesPaginatorName = Literal["describe_test_cases"]
EnvironmentTypeType = Literal[
    "ARM_CONTAINER",
    "LINUX_CONTAINER",
    "LINUX_GPU_CONTAINER",
    "WINDOWS_CONTAINER",
    "WINDOWS_SERVER_2019_CONTAINER",
]
EnvironmentVariableTypeType = Literal["PARAMETER_STORE", "PLAINTEXT", "SECRETS_MANAGER"]
FileSystemTypeType = Literal["EFS"]
ImagePullCredentialsTypeType = Literal["CODEBUILD", "SERVICE_ROLE"]
LanguageTypeType = Literal[
    "ANDROID", "BASE", "DOCKER", "DOTNET", "GOLANG", "JAVA", "NODE_JS", "PHP", "PYTHON", "RUBY"
]
ListBuildBatchesForProjectPaginatorName = Literal["list_build_batches_for_project"]
ListBuildBatchesPaginatorName = Literal["list_build_batches"]
ListBuildsForProjectPaginatorName = Literal["list_builds_for_project"]
ListBuildsPaginatorName = Literal["list_builds"]
ListProjectsPaginatorName = Literal["list_projects"]
ListReportGroupsPaginatorName = Literal["list_report_groups"]
ListReportsForReportGroupPaginatorName = Literal["list_reports_for_report_group"]
ListReportsPaginatorName = Literal["list_reports"]
ListSharedProjectsPaginatorName = Literal["list_shared_projects"]
ListSharedReportGroupsPaginatorName = Literal["list_shared_report_groups"]
LogsConfigStatusTypeType = Literal["DISABLED", "ENABLED"]
PlatformTypeType = Literal["AMAZON_LINUX", "DEBIAN", "UBUNTU", "WINDOWS_SERVER"]
ProjectSortByTypeType = Literal["CREATED_TIME", "LAST_MODIFIED_TIME", "NAME"]
ReportCodeCoverageSortByTypeType = Literal["FILE_PATH", "LINE_COVERAGE_PERCENTAGE"]
ReportExportConfigTypeType = Literal["NO_EXPORT", "S3"]
ReportGroupSortByTypeType = Literal["CREATED_TIME", "LAST_MODIFIED_TIME", "NAME"]
ReportGroupStatusTypeType = Literal["ACTIVE", "DELETING"]
ReportGroupTrendFieldTypeType = Literal[
    "BRANCHES_COVERED",
    "BRANCHES_MISSED",
    "BRANCH_COVERAGE",
    "DURATION",
    "LINES_COVERED",
    "LINES_MISSED",
    "LINE_COVERAGE",
    "PASS_RATE",
    "TOTAL",
]
ReportPackagingTypeType = Literal["NONE", "ZIP"]
ReportStatusTypeType = Literal["DELETING", "FAILED", "GENERATING", "INCOMPLETE", "SUCCEEDED"]
ReportTypeType = Literal["CODE_COVERAGE", "TEST"]
RetryBuildBatchTypeType = Literal["RETRY_ALL_BUILDS", "RETRY_FAILED_BUILDS"]
ServerTypeType = Literal["BITBUCKET", "GITHUB", "GITHUB_ENTERPRISE"]
SharedResourceSortByTypeType = Literal["ARN", "MODIFIED_TIME"]
SortOrderTypeType = Literal["ASCENDING", "DESCENDING"]
SourceAuthTypeType = Literal["OAUTH"]
SourceTypeType = Literal[
    "BITBUCKET", "CODECOMMIT", "CODEPIPELINE", "GITHUB", "GITHUB_ENTERPRISE", "NO_SOURCE", "S3"
]
StatusTypeType = Literal["FAILED", "FAULT", "IN_PROGRESS", "STOPPED", "SUCCEEDED", "TIMED_OUT"]
WebhookBuildTypeType = Literal["BUILD", "BUILD_BATCH"]
WebhookFilterTypeType = Literal[
    "ACTOR_ACCOUNT_ID", "BASE_REF", "COMMIT_MESSAGE", "EVENT", "FILE_PATH", "HEAD_REF"
]
