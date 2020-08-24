"""
Main interface for codebuild service type definitions.

Usage::

    ```python
    from mypy_boto3_codebuild.type_defs import BatchRestrictionsTypeDef

    data: BatchRestrictionsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchRestrictionsTypeDef",
    "BuildArtifactsTypeDef",
    "BuildBatchPhaseTypeDef",
    "BuildBatchTypeDef",
    "BuildGroupTypeDef",
    "BuildNotDeletedTypeDef",
    "BuildPhaseTypeDef",
    "BuildStatusConfigTypeDef",
    "BuildSummaryTypeDef",
    "BuildTypeDef",
    "CloudWatchLogsConfigTypeDef",
    "CodeCoverageReportSummaryTypeDef",
    "CodeCoverageTypeDef",
    "DebugSessionTypeDef",
    "EnvironmentImageTypeDef",
    "EnvironmentLanguageTypeDef",
    "EnvironmentPlatformTypeDef",
    "EnvironmentVariableTypeDef",
    "ExportedEnvironmentVariableTypeDef",
    "GitSubmodulesConfigTypeDef",
    "LogsConfigTypeDef",
    "LogsLocationTypeDef",
    "NetworkInterfaceTypeDef",
    "PhaseContextTypeDef",
    "ProjectArtifactsTypeDef",
    "ProjectBadgeTypeDef",
    "ProjectBuildBatchConfigTypeDef",
    "ProjectCacheTypeDef",
    "ProjectEnvironmentTypeDef",
    "ProjectFileSystemLocationTypeDef",
    "ProjectSourceTypeDef",
    "ProjectSourceVersionTypeDef",
    "ProjectTypeDef",
    "RegistryCredentialTypeDef",
    "ReportExportConfigTypeDef",
    "ReportGroupTypeDef",
    "ReportTypeDef",
    "ResolvedArtifactTypeDef",
    "S3LogsConfigTypeDef",
    "S3ReportExportConfigTypeDef",
    "SourceAuthTypeDef",
    "SourceCredentialsInfoTypeDef",
    "TagTypeDef",
    "TestCaseTypeDef",
    "TestReportSummaryTypeDef",
    "VpcConfigTypeDef",
    "WebhookFilterTypeDef",
    "WebhookTypeDef",
    "BatchDeleteBuildsOutputTypeDef",
    "BatchGetBuildBatchesOutputTypeDef",
    "BatchGetBuildsOutputTypeDef",
    "BatchGetProjectsOutputTypeDef",
    "BatchGetReportGroupsOutputTypeDef",
    "BatchGetReportsOutputTypeDef",
    "BuildBatchFilterTypeDef",
    "CreateProjectOutputTypeDef",
    "CreateReportGroupOutputTypeDef",
    "CreateWebhookOutputTypeDef",
    "DeleteBuildBatchOutputTypeDef",
    "DeleteSourceCredentialsOutputTypeDef",
    "DescribeCodeCoveragesOutputTypeDef",
    "DescribeTestCasesOutputTypeDef",
    "GetResourcePolicyOutputTypeDef",
    "ImportSourceCredentialsOutputTypeDef",
    "ListBuildBatchesForProjectOutputTypeDef",
    "ListBuildBatchesOutputTypeDef",
    "ListBuildsForProjectOutputTypeDef",
    "ListBuildsOutputTypeDef",
    "ListCuratedEnvironmentImagesOutputTypeDef",
    "ListProjectsOutputTypeDef",
    "ListReportGroupsOutputTypeDef",
    "ListReportsForReportGroupOutputTypeDef",
    "ListReportsOutputTypeDef",
    "ListSharedProjectsOutputTypeDef",
    "ListSharedReportGroupsOutputTypeDef",
    "ListSourceCredentialsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PutResourcePolicyOutputTypeDef",
    "ReportFilterTypeDef",
    "RetryBuildBatchOutputTypeDef",
    "RetryBuildOutputTypeDef",
    "StartBuildBatchOutputTypeDef",
    "StartBuildOutputTypeDef",
    "StopBuildBatchOutputTypeDef",
    "StopBuildOutputTypeDef",
    "TestCaseFilterTypeDef",
    "UpdateProjectOutputTypeDef",
    "UpdateReportGroupOutputTypeDef",
    "UpdateWebhookOutputTypeDef",
)

BatchRestrictionsTypeDef = TypedDict(
    "BatchRestrictionsTypeDef",
    {"maximumBuildsAllowed": int, "computeTypesAllowed": List[str]},
    total=False,
)

BuildArtifactsTypeDef = TypedDict(
    "BuildArtifactsTypeDef",
    {
        "location": str,
        "sha256sum": str,
        "md5sum": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)

BuildBatchPhaseTypeDef = TypedDict(
    "BuildBatchPhaseTypeDef",
    {
        "phaseType": Literal[
            "SUBMITTED",
            "DOWNLOAD_BATCHSPEC",
            "IN_PROGRESS",
            "COMBINE_ARTIFACTS",
            "SUCCEEDED",
            "FAILED",
            "STOPPED",
        ],
        "phaseStatus": Literal[
            "SUCCEEDED", "FAILED", "FAULT", "TIMED_OUT", "IN_PROGRESS", "STOPPED"
        ],
        "startTime": datetime,
        "endTime": datetime,
        "durationInSeconds": int,
        "contexts": List["PhaseContextTypeDef"],
    },
    total=False,
)

BuildBatchTypeDef = TypedDict(
    "BuildBatchTypeDef",
    {
        "id": str,
        "arn": str,
        "startTime": datetime,
        "endTime": datetime,
        "currentPhase": str,
        "buildBatchStatus": Literal[
            "SUCCEEDED", "FAILED", "FAULT", "TIMED_OUT", "IN_PROGRESS", "STOPPED"
        ],
        "sourceVersion": str,
        "resolvedSourceVersion": str,
        "projectName": str,
        "phases": List["BuildBatchPhaseTypeDef"],
        "source": "ProjectSourceTypeDef",
        "secondarySources": List["ProjectSourceTypeDef"],
        "secondarySourceVersions": List["ProjectSourceVersionTypeDef"],
        "artifacts": "BuildArtifactsTypeDef",
        "secondaryArtifacts": List["BuildArtifactsTypeDef"],
        "cache": "ProjectCacheTypeDef",
        "environment": "ProjectEnvironmentTypeDef",
        "serviceRole": str,
        "logConfig": "LogsConfigTypeDef",
        "buildTimeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "complete": bool,
        "initiator": str,
        "vpcConfig": "VpcConfigTypeDef",
        "encryptionKey": str,
        "buildBatchNumber": int,
        "fileSystemLocations": List["ProjectFileSystemLocationTypeDef"],
        "buildBatchConfig": "ProjectBuildBatchConfigTypeDef",
        "buildGroups": List["BuildGroupTypeDef"],
    },
    total=False,
)

BuildGroupTypeDef = TypedDict(
    "BuildGroupTypeDef",
    {
        "identifier": str,
        "dependsOn": List[str],
        "ignoreFailure": bool,
        "currentBuildSummary": "BuildSummaryTypeDef",
        "priorBuildSummaryList": List["BuildSummaryTypeDef"],
    },
    total=False,
)

BuildNotDeletedTypeDef = TypedDict(
    "BuildNotDeletedTypeDef", {"id": str, "statusCode": str}, total=False
)

BuildPhaseTypeDef = TypedDict(
    "BuildPhaseTypeDef",
    {
        "phaseType": Literal[
            "SUBMITTED",
            "QUEUED",
            "PROVISIONING",
            "DOWNLOAD_SOURCE",
            "INSTALL",
            "PRE_BUILD",
            "BUILD",
            "POST_BUILD",
            "UPLOAD_ARTIFACTS",
            "FINALIZING",
            "COMPLETED",
        ],
        "phaseStatus": Literal[
            "SUCCEEDED", "FAILED", "FAULT", "TIMED_OUT", "IN_PROGRESS", "STOPPED"
        ],
        "startTime": datetime,
        "endTime": datetime,
        "durationInSeconds": int,
        "contexts": List["PhaseContextTypeDef"],
    },
    total=False,
)

BuildStatusConfigTypeDef = TypedDict(
    "BuildStatusConfigTypeDef", {"context": str, "targetUrl": str}, total=False
)

BuildSummaryTypeDef = TypedDict(
    "BuildSummaryTypeDef",
    {
        "arn": str,
        "requestedOn": datetime,
        "buildStatus": Literal[
            "SUCCEEDED", "FAILED", "FAULT", "TIMED_OUT", "IN_PROGRESS", "STOPPED"
        ],
        "primaryArtifact": "ResolvedArtifactTypeDef",
        "secondaryArtifacts": List["ResolvedArtifactTypeDef"],
    },
    total=False,
)

BuildTypeDef = TypedDict(
    "BuildTypeDef",
    {
        "id": str,
        "arn": str,
        "buildNumber": int,
        "startTime": datetime,
        "endTime": datetime,
        "currentPhase": str,
        "buildStatus": Literal[
            "SUCCEEDED", "FAILED", "FAULT", "TIMED_OUT", "IN_PROGRESS", "STOPPED"
        ],
        "sourceVersion": str,
        "resolvedSourceVersion": str,
        "projectName": str,
        "phases": List["BuildPhaseTypeDef"],
        "source": "ProjectSourceTypeDef",
        "secondarySources": List["ProjectSourceTypeDef"],
        "secondarySourceVersions": List["ProjectSourceVersionTypeDef"],
        "artifacts": "BuildArtifactsTypeDef",
        "secondaryArtifacts": List["BuildArtifactsTypeDef"],
        "cache": "ProjectCacheTypeDef",
        "environment": "ProjectEnvironmentTypeDef",
        "serviceRole": str,
        "logs": "LogsLocationTypeDef",
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "buildComplete": bool,
        "initiator": str,
        "vpcConfig": "VpcConfigTypeDef",
        "networkInterface": "NetworkInterfaceTypeDef",
        "encryptionKey": str,
        "exportedEnvironmentVariables": List["ExportedEnvironmentVariableTypeDef"],
        "reportArns": List[str],
        "fileSystemLocations": List["ProjectFileSystemLocationTypeDef"],
        "debugSession": "DebugSessionTypeDef",
        "buildBatchArn": str,
    },
    total=False,
)

_RequiredCloudWatchLogsConfigTypeDef = TypedDict(
    "_RequiredCloudWatchLogsConfigTypeDef", {"status": Literal["ENABLED", "DISABLED"]}
)
_OptionalCloudWatchLogsConfigTypeDef = TypedDict(
    "_OptionalCloudWatchLogsConfigTypeDef", {"groupName": str, "streamName": str}, total=False
)


class CloudWatchLogsConfigTypeDef(
    _RequiredCloudWatchLogsConfigTypeDef, _OptionalCloudWatchLogsConfigTypeDef
):
    pass


CodeCoverageReportSummaryTypeDef = TypedDict(
    "CodeCoverageReportSummaryTypeDef",
    {
        "lineCoveragePercentage": float,
        "linesCovered": int,
        "linesMissed": int,
        "branchCoveragePercentage": float,
        "branchesCovered": int,
        "branchesMissed": int,
    },
    total=False,
)

CodeCoverageTypeDef = TypedDict(
    "CodeCoverageTypeDef",
    {
        "id": str,
        "reportARN": str,
        "filePath": str,
        "lineCoveragePercentage": float,
        "linesCovered": int,
        "linesMissed": int,
        "branchCoveragePercentage": float,
        "branchesCovered": int,
        "branchesMissed": int,
        "expired": datetime,
    },
    total=False,
)

DebugSessionTypeDef = TypedDict(
    "DebugSessionTypeDef", {"sessionEnabled": bool, "sessionTarget": str}, total=False
)

EnvironmentImageTypeDef = TypedDict(
    "EnvironmentImageTypeDef", {"name": str, "description": str, "versions": List[str]}, total=False
)

EnvironmentLanguageTypeDef = TypedDict(
    "EnvironmentLanguageTypeDef",
    {
        "language": Literal[
            "JAVA",
            "PYTHON",
            "NODE_JS",
            "RUBY",
            "GOLANG",
            "DOCKER",
            "ANDROID",
            "DOTNET",
            "BASE",
            "PHP",
        ],
        "images": List["EnvironmentImageTypeDef"],
    },
    total=False,
)

EnvironmentPlatformTypeDef = TypedDict(
    "EnvironmentPlatformTypeDef",
    {
        "platform": Literal["DEBIAN", "AMAZON_LINUX", "UBUNTU", "WINDOWS_SERVER"],
        "languages": List["EnvironmentLanguageTypeDef"],
    },
    total=False,
)

_RequiredEnvironmentVariableTypeDef = TypedDict(
    "_RequiredEnvironmentVariableTypeDef", {"name": str, "value": str}
)
_OptionalEnvironmentVariableTypeDef = TypedDict(
    "_OptionalEnvironmentVariableTypeDef",
    {"type": Literal["PLAINTEXT", "PARAMETER_STORE", "SECRETS_MANAGER"]},
    total=False,
)


class EnvironmentVariableTypeDef(
    _RequiredEnvironmentVariableTypeDef, _OptionalEnvironmentVariableTypeDef
):
    pass


ExportedEnvironmentVariableTypeDef = TypedDict(
    "ExportedEnvironmentVariableTypeDef", {"name": str, "value": str}, total=False
)

GitSubmodulesConfigTypeDef = TypedDict("GitSubmodulesConfigTypeDef", {"fetchSubmodules": bool})

LogsConfigTypeDef = TypedDict(
    "LogsConfigTypeDef",
    {"cloudWatchLogs": "CloudWatchLogsConfigTypeDef", "s3Logs": "S3LogsConfigTypeDef"},
    total=False,
)

LogsLocationTypeDef = TypedDict(
    "LogsLocationTypeDef",
    {
        "groupName": str,
        "streamName": str,
        "deepLink": str,
        "s3DeepLink": str,
        "cloudWatchLogsArn": str,
        "s3LogsArn": str,
        "cloudWatchLogs": "CloudWatchLogsConfigTypeDef",
        "s3Logs": "S3LogsConfigTypeDef",
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef", {"subnetId": str, "networkInterfaceId": str}, total=False
)

PhaseContextTypeDef = TypedDict(
    "PhaseContextTypeDef", {"statusCode": str, "message": str}, total=False
)

_RequiredProjectArtifactsTypeDef = TypedDict(
    "_RequiredProjectArtifactsTypeDef", {"type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"]}
)
_OptionalProjectArtifactsTypeDef = TypedDict(
    "_OptionalProjectArtifactsTypeDef",
    {
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ProjectArtifactsTypeDef(_RequiredProjectArtifactsTypeDef, _OptionalProjectArtifactsTypeDef):
    pass


ProjectBadgeTypeDef = TypedDict(
    "ProjectBadgeTypeDef", {"badgeEnabled": bool, "badgeRequestUrl": str}, total=False
)

ProjectBuildBatchConfigTypeDef = TypedDict(
    "ProjectBuildBatchConfigTypeDef",
    {
        "serviceRole": str,
        "combineArtifacts": bool,
        "restrictions": "BatchRestrictionsTypeDef",
        "timeoutInMins": int,
    },
    total=False,
)

_RequiredProjectCacheTypeDef = TypedDict(
    "_RequiredProjectCacheTypeDef", {"type": Literal["NO_CACHE", "S3", "LOCAL"]}
)
_OptionalProjectCacheTypeDef = TypedDict(
    "_OptionalProjectCacheTypeDef",
    {
        "location": str,
        "modes": List[
            Literal["LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE", "LOCAL_CUSTOM_CACHE"]
        ],
    },
    total=False,
)


class ProjectCacheTypeDef(_RequiredProjectCacheTypeDef, _OptionalProjectCacheTypeDef):
    pass


_RequiredProjectEnvironmentTypeDef = TypedDict(
    "_RequiredProjectEnvironmentTypeDef",
    {
        "type": Literal[
            "WINDOWS_CONTAINER",
            "LINUX_CONTAINER",
            "LINUX_GPU_CONTAINER",
            "ARM_CONTAINER",
            "WINDOWS_SERVER_2019_CONTAINER",
        ],
        "image": str,
        "computeType": Literal[
            "BUILD_GENERAL1_SMALL",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_2XLARGE",
        ],
    },
)
_OptionalProjectEnvironmentTypeDef = TypedDict(
    "_OptionalProjectEnvironmentTypeDef",
    {
        "environmentVariables": List["EnvironmentVariableTypeDef"],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": "RegistryCredentialTypeDef",
        "imagePullCredentialsType": Literal["CODEBUILD", "SERVICE_ROLE"],
    },
    total=False,
)


class ProjectEnvironmentTypeDef(
    _RequiredProjectEnvironmentTypeDef, _OptionalProjectEnvironmentTypeDef
):
    pass


ProjectFileSystemLocationTypeDef = TypedDict(
    "ProjectFileSystemLocationTypeDef",
    {
        "type": Literal["EFS"],
        "location": str,
        "mountPoint": str,
        "identifier": str,
        "mountOptions": str,
    },
    total=False,
)

_RequiredProjectSourceTypeDef = TypedDict(
    "_RequiredProjectSourceTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ]
    },
)
_OptionalProjectSourceTypeDef = TypedDict(
    "_OptionalProjectSourceTypeDef",
    {
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": "GitSubmodulesConfigTypeDef",
        "buildspec": str,
        "auth": "SourceAuthTypeDef",
        "reportBuildStatus": bool,
        "buildStatusConfig": "BuildStatusConfigTypeDef",
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ProjectSourceTypeDef(_RequiredProjectSourceTypeDef, _OptionalProjectSourceTypeDef):
    pass


ProjectSourceVersionTypeDef = TypedDict(
    "ProjectSourceVersionTypeDef", {"sourceIdentifier": str, "sourceVersion": str}
)

ProjectTypeDef = TypedDict(
    "ProjectTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "source": "ProjectSourceTypeDef",
        "secondarySources": List["ProjectSourceTypeDef"],
        "sourceVersion": str,
        "secondarySourceVersions": List["ProjectSourceVersionTypeDef"],
        "artifacts": "ProjectArtifactsTypeDef",
        "secondaryArtifacts": List["ProjectArtifactsTypeDef"],
        "cache": "ProjectCacheTypeDef",
        "environment": "ProjectEnvironmentTypeDef",
        "serviceRole": str,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "encryptionKey": str,
        "tags": List["TagTypeDef"],
        "created": datetime,
        "lastModified": datetime,
        "webhook": "WebhookTypeDef",
        "vpcConfig": "VpcConfigTypeDef",
        "badge": "ProjectBadgeTypeDef",
        "logsConfig": "LogsConfigTypeDef",
        "fileSystemLocations": List["ProjectFileSystemLocationTypeDef"],
        "buildBatchConfig": "ProjectBuildBatchConfigTypeDef",
    },
    total=False,
)

RegistryCredentialTypeDef = TypedDict(
    "RegistryCredentialTypeDef",
    {"credential": str, "credentialProvider": Literal["SECRETS_MANAGER"]},
)

ReportExportConfigTypeDef = TypedDict(
    "ReportExportConfigTypeDef",
    {
        "exportConfigType": Literal["S3", "NO_EXPORT"],
        "s3Destination": "S3ReportExportConfigTypeDef",
    },
    total=False,
)

ReportGroupTypeDef = TypedDict(
    "ReportGroupTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal["TEST", "CODE_COVERAGE"],
        "exportConfig": "ReportExportConfigTypeDef",
        "created": datetime,
        "lastModified": datetime,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

ReportTypeDef = TypedDict(
    "ReportTypeDef",
    {
        "arn": str,
        "type": Literal["TEST", "CODE_COVERAGE"],
        "name": str,
        "reportGroupArn": str,
        "executionId": str,
        "status": Literal["GENERATING", "SUCCEEDED", "FAILED", "INCOMPLETE", "DELETING"],
        "created": datetime,
        "expired": datetime,
        "exportConfig": "ReportExportConfigTypeDef",
        "truncated": bool,
        "testSummary": "TestReportSummaryTypeDef",
        "codeCoverageSummary": "CodeCoverageReportSummaryTypeDef",
    },
    total=False,
)

ResolvedArtifactTypeDef = TypedDict(
    "ResolvedArtifactTypeDef",
    {"type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"], "location": str, "identifier": str},
    total=False,
)

_RequiredS3LogsConfigTypeDef = TypedDict(
    "_RequiredS3LogsConfigTypeDef", {"status": Literal["ENABLED", "DISABLED"]}
)
_OptionalS3LogsConfigTypeDef = TypedDict(
    "_OptionalS3LogsConfigTypeDef", {"location": str, "encryptionDisabled": bool}, total=False
)


class S3LogsConfigTypeDef(_RequiredS3LogsConfigTypeDef, _OptionalS3LogsConfigTypeDef):
    pass


S3ReportExportConfigTypeDef = TypedDict(
    "S3ReportExportConfigTypeDef",
    {
        "bucket": str,
        "path": str,
        "packaging": Literal["ZIP", "NONE"],
        "encryptionKey": str,
        "encryptionDisabled": bool,
    },
    total=False,
)

_RequiredSourceAuthTypeDef = TypedDict("_RequiredSourceAuthTypeDef", {"type": Literal["OAUTH"]})
_OptionalSourceAuthTypeDef = TypedDict("_OptionalSourceAuthTypeDef", {"resource": str}, total=False)


class SourceAuthTypeDef(_RequiredSourceAuthTypeDef, _OptionalSourceAuthTypeDef):
    pass


SourceCredentialsInfoTypeDef = TypedDict(
    "SourceCredentialsInfoTypeDef",
    {
        "arn": str,
        "serverType": Literal["GITHUB", "BITBUCKET", "GITHUB_ENTERPRISE"],
        "authType": Literal["OAUTH", "BASIC_AUTH", "PERSONAL_ACCESS_TOKEN"],
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"key": str, "value": str}, total=False)

TestCaseTypeDef = TypedDict(
    "TestCaseTypeDef",
    {
        "reportArn": str,
        "testRawDataPath": str,
        "prefix": str,
        "name": str,
        "status": str,
        "durationInNanoSeconds": int,
        "message": str,
        "expired": datetime,
    },
    total=False,
)

TestReportSummaryTypeDef = TypedDict(
    "TestReportSummaryTypeDef",
    {"total": int, "statusCounts": Dict[str, int], "durationInNanoSeconds": int},
)

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)

_RequiredWebhookFilterTypeDef = TypedDict(
    "_RequiredWebhookFilterTypeDef",
    {
        "type": Literal[
            "EVENT", "BASE_REF", "HEAD_REF", "ACTOR_ACCOUNT_ID", "FILE_PATH", "COMMIT_MESSAGE"
        ],
        "pattern": str,
    },
)
_OptionalWebhookFilterTypeDef = TypedDict(
    "_OptionalWebhookFilterTypeDef", {"excludeMatchedPattern": bool}, total=False
)


class WebhookFilterTypeDef(_RequiredWebhookFilterTypeDef, _OptionalWebhookFilterTypeDef):
    pass


WebhookTypeDef = TypedDict(
    "WebhookTypeDef",
    {
        "url": str,
        "payloadUrl": str,
        "secret": str,
        "branchFilter": str,
        "filterGroups": List[List["WebhookFilterTypeDef"]],
        "buildType": Literal["BUILD", "BUILD_BATCH"],
        "lastModifiedSecret": datetime,
    },
    total=False,
)

BatchDeleteBuildsOutputTypeDef = TypedDict(
    "BatchDeleteBuildsOutputTypeDef",
    {"buildsDeleted": List[str], "buildsNotDeleted": List["BuildNotDeletedTypeDef"]},
    total=False,
)

BatchGetBuildBatchesOutputTypeDef = TypedDict(
    "BatchGetBuildBatchesOutputTypeDef",
    {"buildBatches": List["BuildBatchTypeDef"], "buildBatchesNotFound": List[str]},
    total=False,
)

BatchGetBuildsOutputTypeDef = TypedDict(
    "BatchGetBuildsOutputTypeDef",
    {"builds": List["BuildTypeDef"], "buildsNotFound": List[str]},
    total=False,
)

BatchGetProjectsOutputTypeDef = TypedDict(
    "BatchGetProjectsOutputTypeDef",
    {"projects": List["ProjectTypeDef"], "projectsNotFound": List[str]},
    total=False,
)

BatchGetReportGroupsOutputTypeDef = TypedDict(
    "BatchGetReportGroupsOutputTypeDef",
    {"reportGroups": List["ReportGroupTypeDef"], "reportGroupsNotFound": List[str]},
    total=False,
)

BatchGetReportsOutputTypeDef = TypedDict(
    "BatchGetReportsOutputTypeDef",
    {"reports": List["ReportTypeDef"], "reportsNotFound": List[str]},
    total=False,
)

BuildBatchFilterTypeDef = TypedDict(
    "BuildBatchFilterTypeDef",
    {"status": Literal["SUCCEEDED", "FAILED", "FAULT", "TIMED_OUT", "IN_PROGRESS", "STOPPED"]},
    total=False,
)

CreateProjectOutputTypeDef = TypedDict(
    "CreateProjectOutputTypeDef", {"project": "ProjectTypeDef"}, total=False
)

CreateReportGroupOutputTypeDef = TypedDict(
    "CreateReportGroupOutputTypeDef", {"reportGroup": "ReportGroupTypeDef"}, total=False
)

CreateWebhookOutputTypeDef = TypedDict(
    "CreateWebhookOutputTypeDef", {"webhook": "WebhookTypeDef"}, total=False
)

DeleteBuildBatchOutputTypeDef = TypedDict(
    "DeleteBuildBatchOutputTypeDef",
    {
        "statusCode": str,
        "buildsDeleted": List[str],
        "buildsNotDeleted": List["BuildNotDeletedTypeDef"],
    },
    total=False,
)

DeleteSourceCredentialsOutputTypeDef = TypedDict(
    "DeleteSourceCredentialsOutputTypeDef", {"arn": str}, total=False
)

DescribeCodeCoveragesOutputTypeDef = TypedDict(
    "DescribeCodeCoveragesOutputTypeDef",
    {"nextToken": str, "codeCoverages": List["CodeCoverageTypeDef"]},
    total=False,
)

DescribeTestCasesOutputTypeDef = TypedDict(
    "DescribeTestCasesOutputTypeDef",
    {"nextToken": str, "testCases": List["TestCaseTypeDef"]},
    total=False,
)

GetResourcePolicyOutputTypeDef = TypedDict(
    "GetResourcePolicyOutputTypeDef", {"policy": str}, total=False
)

ImportSourceCredentialsOutputTypeDef = TypedDict(
    "ImportSourceCredentialsOutputTypeDef", {"arn": str}, total=False
)

ListBuildBatchesForProjectOutputTypeDef = TypedDict(
    "ListBuildBatchesForProjectOutputTypeDef", {"ids": List[str], "nextToken": str}, total=False
)

ListBuildBatchesOutputTypeDef = TypedDict(
    "ListBuildBatchesOutputTypeDef", {"ids": List[str], "nextToken": str}, total=False
)

ListBuildsForProjectOutputTypeDef = TypedDict(
    "ListBuildsForProjectOutputTypeDef", {"ids": List[str], "nextToken": str}, total=False
)

ListBuildsOutputTypeDef = TypedDict(
    "ListBuildsOutputTypeDef", {"ids": List[str], "nextToken": str}, total=False
)

ListCuratedEnvironmentImagesOutputTypeDef = TypedDict(
    "ListCuratedEnvironmentImagesOutputTypeDef",
    {"platforms": List["EnvironmentPlatformTypeDef"]},
    total=False,
)

ListProjectsOutputTypeDef = TypedDict(
    "ListProjectsOutputTypeDef", {"nextToken": str, "projects": List[str]}, total=False
)

ListReportGroupsOutputTypeDef = TypedDict(
    "ListReportGroupsOutputTypeDef", {"nextToken": str, "reportGroups": List[str]}, total=False
)

ListReportsForReportGroupOutputTypeDef = TypedDict(
    "ListReportsForReportGroupOutputTypeDef", {"nextToken": str, "reports": List[str]}, total=False
)

ListReportsOutputTypeDef = TypedDict(
    "ListReportsOutputTypeDef", {"nextToken": str, "reports": List[str]}, total=False
)

ListSharedProjectsOutputTypeDef = TypedDict(
    "ListSharedProjectsOutputTypeDef", {"nextToken": str, "projects": List[str]}, total=False
)

ListSharedReportGroupsOutputTypeDef = TypedDict(
    "ListSharedReportGroupsOutputTypeDef",
    {"nextToken": str, "reportGroups": List[str]},
    total=False,
)

ListSourceCredentialsOutputTypeDef = TypedDict(
    "ListSourceCredentialsOutputTypeDef",
    {"sourceCredentialsInfos": List["SourceCredentialsInfoTypeDef"]},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutResourcePolicyOutputTypeDef = TypedDict(
    "PutResourcePolicyOutputTypeDef", {"resourceArn": str}, total=False
)

ReportFilterTypeDef = TypedDict(
    "ReportFilterTypeDef",
    {"status": Literal["GENERATING", "SUCCEEDED", "FAILED", "INCOMPLETE", "DELETING"]},
    total=False,
)

RetryBuildBatchOutputTypeDef = TypedDict(
    "RetryBuildBatchOutputTypeDef", {"buildBatch": "BuildBatchTypeDef"}, total=False
)

RetryBuildOutputTypeDef = TypedDict(
    "RetryBuildOutputTypeDef", {"build": "BuildTypeDef"}, total=False
)

StartBuildBatchOutputTypeDef = TypedDict(
    "StartBuildBatchOutputTypeDef", {"buildBatch": "BuildBatchTypeDef"}, total=False
)

StartBuildOutputTypeDef = TypedDict(
    "StartBuildOutputTypeDef", {"build": "BuildTypeDef"}, total=False
)

StopBuildBatchOutputTypeDef = TypedDict(
    "StopBuildBatchOutputTypeDef", {"buildBatch": "BuildBatchTypeDef"}, total=False
)

StopBuildOutputTypeDef = TypedDict("StopBuildOutputTypeDef", {"build": "BuildTypeDef"}, total=False)

TestCaseFilterTypeDef = TypedDict("TestCaseFilterTypeDef", {"status": str}, total=False)

UpdateProjectOutputTypeDef = TypedDict(
    "UpdateProjectOutputTypeDef", {"project": "ProjectTypeDef"}, total=False
)

UpdateReportGroupOutputTypeDef = TypedDict(
    "UpdateReportGroupOutputTypeDef", {"reportGroup": "ReportGroupTypeDef"}, total=False
)

UpdateWebhookOutputTypeDef = TypedDict(
    "UpdateWebhookOutputTypeDef", {"webhook": "WebhookTypeDef"}, total=False
)
