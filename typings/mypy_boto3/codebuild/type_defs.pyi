"""
Type annotations for codebuild service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codebuild/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_codebuild.type_defs import AutoRetryConfigTypeDef

    data: AutoRetryConfigTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ArtifactNamespaceType,
    ArtifactPackagingType,
    ArtifactsTypeType,
    AuthTypeType,
    BatchReportModeTypeType,
    BucketOwnerAccessType,
    BuildBatchPhaseTypeType,
    BuildPhaseTypeType,
    CacheModeType,
    CacheTypeType,
    ComputeTypeType,
    EnvironmentTypeType,
    EnvironmentVariableTypeType,
    FleetContextCodeType,
    FleetOverflowBehaviorType,
    FleetProxyRuleBehaviorType,
    FleetProxyRuleEffectTypeType,
    FleetProxyRuleTypeType,
    FleetSortByTypeType,
    FleetStatusCodeType,
    ImagePullCredentialsTypeType,
    LanguageTypeType,
    LogsConfigStatusTypeType,
    MachineTypeType,
    PlatformTypeType,
    ProjectSortByTypeType,
    ProjectVisibilityTypeType,
    PullRequestBuildApproverRoleType,
    PullRequestBuildCommentApprovalType,
    ReportCodeCoverageSortByTypeType,
    ReportExportConfigTypeType,
    ReportGroupSortByTypeType,
    ReportGroupStatusTypeType,
    ReportGroupTrendFieldTypeType,
    ReportPackagingTypeType,
    ReportStatusTypeType,
    ReportTypeType,
    RetryBuildBatchTypeType,
    ServerTypeType,
    SharedResourceSortByTypeType,
    SortOrderTypeType,
    SourceAuthTypeType,
    SourceTypeType,
    StatusTypeType,
    WebhookBuildTypeType,
    WebhookFilterTypeType,
    WebhookScopeTypeType,
    WebhookStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AutoRetryConfigTypeDef",
    "BatchDeleteBuildsInputTypeDef",
    "BatchDeleteBuildsOutputTypeDef",
    "BatchGetBuildBatchesInputTypeDef",
    "BatchGetBuildBatchesOutputTypeDef",
    "BatchGetBuildsInputTypeDef",
    "BatchGetBuildsOutputTypeDef",
    "BatchGetCommandExecutionsInputTypeDef",
    "BatchGetCommandExecutionsOutputTypeDef",
    "BatchGetFleetsInputTypeDef",
    "BatchGetFleetsOutputTypeDef",
    "BatchGetProjectsInputTypeDef",
    "BatchGetProjectsOutputTypeDef",
    "BatchGetReportGroupsInputTypeDef",
    "BatchGetReportGroupsOutputTypeDef",
    "BatchGetReportsInputTypeDef",
    "BatchGetReportsOutputTypeDef",
    "BatchGetSandboxesInputTypeDef",
    "BatchGetSandboxesOutputTypeDef",
    "BatchRestrictionsOutputTypeDef",
    "BatchRestrictionsTypeDef",
    "BuildArtifactsTypeDef",
    "BuildBatchFilterTypeDef",
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
    "CommandExecutionTypeDef",
    "ComputeConfigurationTypeDef",
    "CreateFleetInputTypeDef",
    "CreateFleetOutputTypeDef",
    "CreateProjectInputTypeDef",
    "CreateProjectOutputTypeDef",
    "CreateReportGroupInputTypeDef",
    "CreateReportGroupOutputTypeDef",
    "CreateWebhookInputTypeDef",
    "CreateWebhookOutputTypeDef",
    "DebugSessionTypeDef",
    "DeleteBuildBatchInputTypeDef",
    "DeleteBuildBatchOutputTypeDef",
    "DeleteFleetInputTypeDef",
    "DeleteProjectInputTypeDef",
    "DeleteReportGroupInputTypeDef",
    "DeleteReportInputTypeDef",
    "DeleteResourcePolicyInputTypeDef",
    "DeleteSourceCredentialsInputTypeDef",
    "DeleteSourceCredentialsOutputTypeDef",
    "DeleteWebhookInputTypeDef",
    "DescribeCodeCoveragesInputPaginateTypeDef",
    "DescribeCodeCoveragesInputTypeDef",
    "DescribeCodeCoveragesOutputTypeDef",
    "DescribeTestCasesInputPaginateTypeDef",
    "DescribeTestCasesInputTypeDef",
    "DescribeTestCasesOutputTypeDef",
    "DockerServerOutputTypeDef",
    "DockerServerStatusTypeDef",
    "DockerServerTypeDef",
    "EnvironmentImageTypeDef",
    "EnvironmentLanguageTypeDef",
    "EnvironmentPlatformTypeDef",
    "EnvironmentVariableTypeDef",
    "ExportedEnvironmentVariableTypeDef",
    "FleetProxyRuleOutputTypeDef",
    "FleetProxyRuleTypeDef",
    "FleetStatusTypeDef",
    "FleetTypeDef",
    "GetReportGroupTrendInputTypeDef",
    "GetReportGroupTrendOutputTypeDef",
    "GetResourcePolicyInputTypeDef",
    "GetResourcePolicyOutputTypeDef",
    "GitSubmodulesConfigTypeDef",
    "ImportSourceCredentialsInputTypeDef",
    "ImportSourceCredentialsOutputTypeDef",
    "InvalidateProjectCacheInputTypeDef",
    "ListBuildBatchesForProjectInputPaginateTypeDef",
    "ListBuildBatchesForProjectInputTypeDef",
    "ListBuildBatchesForProjectOutputTypeDef",
    "ListBuildBatchesInputPaginateTypeDef",
    "ListBuildBatchesInputTypeDef",
    "ListBuildBatchesOutputTypeDef",
    "ListBuildsForProjectInputPaginateTypeDef",
    "ListBuildsForProjectInputTypeDef",
    "ListBuildsForProjectOutputTypeDef",
    "ListBuildsInputPaginateTypeDef",
    "ListBuildsInputTypeDef",
    "ListBuildsOutputTypeDef",
    "ListCommandExecutionsForSandboxInputPaginateTypeDef",
    "ListCommandExecutionsForSandboxInputTypeDef",
    "ListCommandExecutionsForSandboxOutputTypeDef",
    "ListCuratedEnvironmentImagesOutputTypeDef",
    "ListFleetsInputTypeDef",
    "ListFleetsOutputTypeDef",
    "ListProjectsInputPaginateTypeDef",
    "ListProjectsInputTypeDef",
    "ListProjectsOutputTypeDef",
    "ListReportGroupsInputPaginateTypeDef",
    "ListReportGroupsInputTypeDef",
    "ListReportGroupsOutputTypeDef",
    "ListReportsForReportGroupInputPaginateTypeDef",
    "ListReportsForReportGroupInputTypeDef",
    "ListReportsForReportGroupOutputTypeDef",
    "ListReportsInputPaginateTypeDef",
    "ListReportsInputTypeDef",
    "ListReportsOutputTypeDef",
    "ListSandboxesForProjectInputPaginateTypeDef",
    "ListSandboxesForProjectInputTypeDef",
    "ListSandboxesForProjectOutputTypeDef",
    "ListSandboxesInputPaginateTypeDef",
    "ListSandboxesInputTypeDef",
    "ListSandboxesOutputTypeDef",
    "ListSharedProjectsInputPaginateTypeDef",
    "ListSharedProjectsInputTypeDef",
    "ListSharedProjectsOutputTypeDef",
    "ListSharedReportGroupsInputPaginateTypeDef",
    "ListSharedReportGroupsInputTypeDef",
    "ListSharedReportGroupsOutputTypeDef",
    "ListSourceCredentialsOutputTypeDef",
    "LogsConfigTypeDef",
    "LogsLocationTypeDef",
    "NetworkInterfaceTypeDef",
    "PaginatorConfigTypeDef",
    "PhaseContextTypeDef",
    "ProjectArtifactsTypeDef",
    "ProjectBadgeTypeDef",
    "ProjectBuildBatchConfigOutputTypeDef",
    "ProjectBuildBatchConfigTypeDef",
    "ProjectBuildBatchConfigUnionTypeDef",
    "ProjectCacheOutputTypeDef",
    "ProjectCacheTypeDef",
    "ProjectCacheUnionTypeDef",
    "ProjectEnvironmentOutputTypeDef",
    "ProjectEnvironmentTypeDef",
    "ProjectEnvironmentUnionTypeDef",
    "ProjectFileSystemLocationTypeDef",
    "ProjectFleetTypeDef",
    "ProjectSourceTypeDef",
    "ProjectSourceVersionTypeDef",
    "ProjectTypeDef",
    "ProxyConfigurationOutputTypeDef",
    "ProxyConfigurationTypeDef",
    "ProxyConfigurationUnionTypeDef",
    "PullRequestBuildPolicyOutputTypeDef",
    "PullRequestBuildPolicyTypeDef",
    "PullRequestBuildPolicyUnionTypeDef",
    "PutResourcePolicyInputTypeDef",
    "PutResourcePolicyOutputTypeDef",
    "RegistryCredentialTypeDef",
    "ReportExportConfigTypeDef",
    "ReportFilterTypeDef",
    "ReportGroupTrendStatsTypeDef",
    "ReportGroupTypeDef",
    "ReportTypeDef",
    "ReportWithRawDataTypeDef",
    "ResolvedArtifactTypeDef",
    "ResponseMetadataTypeDef",
    "RetryBuildBatchInputTypeDef",
    "RetryBuildBatchOutputTypeDef",
    "RetryBuildInputTypeDef",
    "RetryBuildOutputTypeDef",
    "S3LogsConfigTypeDef",
    "S3ReportExportConfigTypeDef",
    "SSMSessionTypeDef",
    "SandboxSessionPhaseTypeDef",
    "SandboxSessionTypeDef",
    "SandboxTypeDef",
    "ScalingConfigurationInputTypeDef",
    "ScalingConfigurationOutputTypeDef",
    "ScopeConfigurationTypeDef",
    "SourceAuthTypeDef",
    "SourceCredentialsInfoTypeDef",
    "StartBuildBatchInputTypeDef",
    "StartBuildBatchOutputTypeDef",
    "StartBuildInputTypeDef",
    "StartBuildOutputTypeDef",
    "StartCommandExecutionInputTypeDef",
    "StartCommandExecutionOutputTypeDef",
    "StartSandboxConnectionInputTypeDef",
    "StartSandboxConnectionOutputTypeDef",
    "StartSandboxInputTypeDef",
    "StartSandboxOutputTypeDef",
    "StopBuildBatchInputTypeDef",
    "StopBuildBatchOutputTypeDef",
    "StopBuildInputTypeDef",
    "StopBuildOutputTypeDef",
    "StopSandboxInputTypeDef",
    "StopSandboxOutputTypeDef",
    "TagTypeDef",
    "TargetTrackingScalingConfigurationTypeDef",
    "TestCaseFilterTypeDef",
    "TestCaseTypeDef",
    "TestReportSummaryTypeDef",
    "UpdateFleetInputTypeDef",
    "UpdateFleetOutputTypeDef",
    "UpdateProjectInputTypeDef",
    "UpdateProjectOutputTypeDef",
    "UpdateProjectVisibilityInputTypeDef",
    "UpdateProjectVisibilityOutputTypeDef",
    "UpdateReportGroupInputTypeDef",
    "UpdateReportGroupOutputTypeDef",
    "UpdateWebhookInputTypeDef",
    "UpdateWebhookOutputTypeDef",
    "VpcConfigOutputTypeDef",
    "VpcConfigTypeDef",
    "VpcConfigUnionTypeDef",
    "WebhookFilterTypeDef",
    "WebhookTypeDef",
)

class AutoRetryConfigTypeDef(TypedDict):
    autoRetryLimit: NotRequired[int]
    autoRetryNumber: NotRequired[int]
    nextAutoRetry: NotRequired[str]
    previousAutoRetry: NotRequired[str]

class BatchDeleteBuildsInputTypeDef(TypedDict):
    ids: Sequence[str]

BuildNotDeletedTypeDef = TypedDict(
    "BuildNotDeletedTypeDef",
    {
        "id": NotRequired[str],
        "statusCode": NotRequired[str],
    },
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class BatchGetBuildBatchesInputTypeDef(TypedDict):
    ids: Sequence[str]

class BatchGetBuildsInputTypeDef(TypedDict):
    ids: Sequence[str]

class BatchGetCommandExecutionsInputTypeDef(TypedDict):
    sandboxId: str
    commandExecutionIds: Sequence[str]

class BatchGetFleetsInputTypeDef(TypedDict):
    names: Sequence[str]

class BatchGetProjectsInputTypeDef(TypedDict):
    names: Sequence[str]

class BatchGetReportGroupsInputTypeDef(TypedDict):
    reportGroupArns: Sequence[str]

class BatchGetReportsInputTypeDef(TypedDict):
    reportArns: Sequence[str]

class BatchGetSandboxesInputTypeDef(TypedDict):
    ids: Sequence[str]

class BatchRestrictionsOutputTypeDef(TypedDict):
    maximumBuildsAllowed: NotRequired[int]
    computeTypesAllowed: NotRequired[List[str]]
    fleetsAllowed: NotRequired[List[str]]

class BatchRestrictionsTypeDef(TypedDict):
    maximumBuildsAllowed: NotRequired[int]
    computeTypesAllowed: NotRequired[Sequence[str]]
    fleetsAllowed: NotRequired[Sequence[str]]

class BuildArtifactsTypeDef(TypedDict):
    location: NotRequired[str]
    sha256sum: NotRequired[str]
    md5sum: NotRequired[str]
    overrideArtifactName: NotRequired[bool]
    encryptionDisabled: NotRequired[bool]
    artifactIdentifier: NotRequired[str]
    bucketOwnerAccess: NotRequired[BucketOwnerAccessType]

class BuildBatchFilterTypeDef(TypedDict):
    status: NotRequired[StatusTypeType]

class PhaseContextTypeDef(TypedDict):
    statusCode: NotRequired[str]
    message: NotRequired[str]

ProjectCacheOutputTypeDef = TypedDict(
    "ProjectCacheOutputTypeDef",
    {
        "type": CacheTypeType,
        "location": NotRequired[str],
        "modes": NotRequired[List[CacheModeType]],
        "cacheNamespace": NotRequired[str],
    },
)
ProjectFileSystemLocationTypeDef = TypedDict(
    "ProjectFileSystemLocationTypeDef",
    {
        "type": NotRequired[Literal["EFS"]],
        "location": NotRequired[str],
        "mountPoint": NotRequired[str],
        "identifier": NotRequired[str],
        "mountOptions": NotRequired[str],
    },
)

class ProjectSourceVersionTypeDef(TypedDict):
    sourceIdentifier: str
    sourceVersion: str

class VpcConfigOutputTypeDef(TypedDict):
    vpcId: NotRequired[str]
    subnets: NotRequired[List[str]]
    securityGroupIds: NotRequired[List[str]]

class BuildStatusConfigTypeDef(TypedDict):
    context: NotRequired[str]
    targetUrl: NotRequired[str]

ResolvedArtifactTypeDef = TypedDict(
    "ResolvedArtifactTypeDef",
    {
        "type": NotRequired[ArtifactsTypeType],
        "location": NotRequired[str],
        "identifier": NotRequired[str],
    },
)

class DebugSessionTypeDef(TypedDict):
    sessionEnabled: NotRequired[bool]
    sessionTarget: NotRequired[str]

class ExportedEnvironmentVariableTypeDef(TypedDict):
    name: NotRequired[str]
    value: NotRequired[str]

class NetworkInterfaceTypeDef(TypedDict):
    subnetId: NotRequired[str]
    networkInterfaceId: NotRequired[str]

class CloudWatchLogsConfigTypeDef(TypedDict):
    status: LogsConfigStatusTypeType
    groupName: NotRequired[str]
    streamName: NotRequired[str]

class CodeCoverageReportSummaryTypeDef(TypedDict):
    lineCoveragePercentage: NotRequired[float]
    linesCovered: NotRequired[int]
    linesMissed: NotRequired[int]
    branchCoveragePercentage: NotRequired[float]
    branchesCovered: NotRequired[int]
    branchesMissed: NotRequired[int]

CodeCoverageTypeDef = TypedDict(
    "CodeCoverageTypeDef",
    {
        "id": NotRequired[str],
        "reportARN": NotRequired[str],
        "filePath": NotRequired[str],
        "lineCoveragePercentage": NotRequired[float],
        "linesCovered": NotRequired[int],
        "linesMissed": NotRequired[int],
        "branchCoveragePercentage": NotRequired[float],
        "branchesCovered": NotRequired[int],
        "branchesMissed": NotRequired[int],
        "expired": NotRequired[datetime],
    },
)

class ComputeConfigurationTypeDef(TypedDict):
    vCpu: NotRequired[int]
    memory: NotRequired[int]
    disk: NotRequired[int]
    machineType: NotRequired[MachineTypeType]
    instanceType: NotRequired[str]

class TagTypeDef(TypedDict):
    key: NotRequired[str]
    value: NotRequired[str]

ProjectArtifactsTypeDef = TypedDict(
    "ProjectArtifactsTypeDef",
    {
        "type": ArtifactsTypeType,
        "location": NotRequired[str],
        "path": NotRequired[str],
        "namespaceType": NotRequired[ArtifactNamespaceType],
        "name": NotRequired[str],
        "packaging": NotRequired[ArtifactPackagingType],
        "overrideArtifactName": NotRequired[bool],
        "encryptionDisabled": NotRequired[bool],
        "artifactIdentifier": NotRequired[str],
        "bucketOwnerAccess": NotRequired[BucketOwnerAccessType],
    },
)

class ScopeConfigurationTypeDef(TypedDict):
    name: str
    scope: WebhookScopeTypeType
    domain: NotRequired[str]

WebhookFilterTypeDef = TypedDict(
    "WebhookFilterTypeDef",
    {
        "type": WebhookFilterTypeType,
        "pattern": str,
        "excludeMatchedPattern": NotRequired[bool],
    },
)
DeleteBuildBatchInputTypeDef = TypedDict(
    "DeleteBuildBatchInputTypeDef",
    {
        "id": str,
    },
)

class DeleteFleetInputTypeDef(TypedDict):
    arn: str

class DeleteProjectInputTypeDef(TypedDict):
    name: str

class DeleteReportGroupInputTypeDef(TypedDict):
    arn: str
    deleteReports: NotRequired[bool]

class DeleteReportInputTypeDef(TypedDict):
    arn: str

class DeleteResourcePolicyInputTypeDef(TypedDict):
    resourceArn: str

class DeleteSourceCredentialsInputTypeDef(TypedDict):
    arn: str

class DeleteWebhookInputTypeDef(TypedDict):
    projectName: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeCodeCoveragesInputTypeDef(TypedDict):
    reportArn: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    sortOrder: NotRequired[SortOrderTypeType]
    sortBy: NotRequired[ReportCodeCoverageSortByTypeType]
    minLineCoveragePercentage: NotRequired[float]
    maxLineCoveragePercentage: NotRequired[float]

class TestCaseFilterTypeDef(TypedDict):
    status: NotRequired[str]
    keyword: NotRequired[str]

class TestCaseTypeDef(TypedDict):
    reportArn: NotRequired[str]
    testRawDataPath: NotRequired[str]
    prefix: NotRequired[str]
    name: NotRequired[str]
    status: NotRequired[str]
    durationInNanoSeconds: NotRequired[int]
    message: NotRequired[str]
    expired: NotRequired[datetime]
    testSuiteName: NotRequired[str]

class DockerServerStatusTypeDef(TypedDict):
    status: NotRequired[str]
    message: NotRequired[str]

class EnvironmentImageTypeDef(TypedDict):
    name: NotRequired[str]
    description: NotRequired[str]
    versions: NotRequired[List[str]]

EnvironmentVariableTypeDef = TypedDict(
    "EnvironmentVariableTypeDef",
    {
        "name": str,
        "value": str,
        "type": NotRequired[EnvironmentVariableTypeType],
    },
)
FleetProxyRuleOutputTypeDef = TypedDict(
    "FleetProxyRuleOutputTypeDef",
    {
        "type": FleetProxyRuleTypeType,
        "effect": FleetProxyRuleEffectTypeType,
        "entities": List[str],
    },
)
FleetProxyRuleTypeDef = TypedDict(
    "FleetProxyRuleTypeDef",
    {
        "type": FleetProxyRuleTypeType,
        "effect": FleetProxyRuleEffectTypeType,
        "entities": Sequence[str],
    },
)

class FleetStatusTypeDef(TypedDict):
    statusCode: NotRequired[FleetStatusCodeType]
    context: NotRequired[FleetContextCodeType]
    message: NotRequired[str]

class GetReportGroupTrendInputTypeDef(TypedDict):
    reportGroupArn: str
    trendField: ReportGroupTrendFieldTypeType
    numOfReports: NotRequired[int]

ReportGroupTrendStatsTypeDef = TypedDict(
    "ReportGroupTrendStatsTypeDef",
    {
        "average": NotRequired[str],
        "max": NotRequired[str],
        "min": NotRequired[str],
    },
)

class ReportWithRawDataTypeDef(TypedDict):
    reportArn: NotRequired[str]
    data: NotRequired[str]

class GetResourcePolicyInputTypeDef(TypedDict):
    resourceArn: str

class GitSubmodulesConfigTypeDef(TypedDict):
    fetchSubmodules: bool

class ImportSourceCredentialsInputTypeDef(TypedDict):
    token: str
    serverType: ServerTypeType
    authType: AuthTypeType
    username: NotRequired[str]
    shouldOverwrite: NotRequired[bool]

class InvalidateProjectCacheInputTypeDef(TypedDict):
    projectName: str

class ListBuildsForProjectInputTypeDef(TypedDict):
    projectName: str
    sortOrder: NotRequired[SortOrderTypeType]
    nextToken: NotRequired[str]

class ListBuildsInputTypeDef(TypedDict):
    sortOrder: NotRequired[SortOrderTypeType]
    nextToken: NotRequired[str]

class ListCommandExecutionsForSandboxInputTypeDef(TypedDict):
    sandboxId: str
    maxResults: NotRequired[int]
    sortOrder: NotRequired[SortOrderTypeType]
    nextToken: NotRequired[str]

class ListFleetsInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    sortOrder: NotRequired[SortOrderTypeType]
    sortBy: NotRequired[FleetSortByTypeType]

class ListProjectsInputTypeDef(TypedDict):
    sortBy: NotRequired[ProjectSortByTypeType]
    sortOrder: NotRequired[SortOrderTypeType]
    nextToken: NotRequired[str]

class ListReportGroupsInputTypeDef(TypedDict):
    sortOrder: NotRequired[SortOrderTypeType]
    sortBy: NotRequired[ReportGroupSortByTypeType]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ReportFilterTypeDef(TypedDict):
    status: NotRequired[ReportStatusTypeType]

class ListSandboxesForProjectInputTypeDef(TypedDict):
    projectName: str
    maxResults: NotRequired[int]
    sortOrder: NotRequired[SortOrderTypeType]
    nextToken: NotRequired[str]

class ListSandboxesInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    sortOrder: NotRequired[SortOrderTypeType]
    nextToken: NotRequired[str]

class ListSharedProjectsInputTypeDef(TypedDict):
    sortBy: NotRequired[SharedResourceSortByTypeType]
    sortOrder: NotRequired[SortOrderTypeType]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListSharedReportGroupsInputTypeDef(TypedDict):
    sortOrder: NotRequired[SortOrderTypeType]
    sortBy: NotRequired[SharedResourceSortByTypeType]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class SourceCredentialsInfoTypeDef(TypedDict):
    arn: NotRequired[str]
    serverType: NotRequired[ServerTypeType]
    authType: NotRequired[AuthTypeType]
    resource: NotRequired[str]

class S3LogsConfigTypeDef(TypedDict):
    status: LogsConfigStatusTypeType
    location: NotRequired[str]
    encryptionDisabled: NotRequired[bool]
    bucketOwnerAccess: NotRequired[BucketOwnerAccessType]

class ProjectBadgeTypeDef(TypedDict):
    badgeEnabled: NotRequired[bool]
    badgeRequestUrl: NotRequired[str]

ProjectCacheTypeDef = TypedDict(
    "ProjectCacheTypeDef",
    {
        "type": CacheTypeType,
        "location": NotRequired[str],
        "modes": NotRequired[Sequence[CacheModeType]],
        "cacheNamespace": NotRequired[str],
    },
)

class ProjectFleetTypeDef(TypedDict):
    fleetArn: NotRequired[str]

class RegistryCredentialTypeDef(TypedDict):
    credential: str
    credentialProvider: Literal["SECRETS_MANAGER"]

SourceAuthTypeDef = TypedDict(
    "SourceAuthTypeDef",
    {
        "type": SourceAuthTypeType,
        "resource": NotRequired[str],
    },
)

class PullRequestBuildPolicyOutputTypeDef(TypedDict):
    requiresCommentApproval: PullRequestBuildCommentApprovalType
    approverRoles: NotRequired[List[PullRequestBuildApproverRoleType]]

class PullRequestBuildPolicyTypeDef(TypedDict):
    requiresCommentApproval: PullRequestBuildCommentApprovalType
    approverRoles: NotRequired[Sequence[PullRequestBuildApproverRoleType]]

class PutResourcePolicyInputTypeDef(TypedDict):
    policy: str
    resourceArn: str

class S3ReportExportConfigTypeDef(TypedDict):
    bucket: NotRequired[str]
    bucketOwner: NotRequired[str]
    path: NotRequired[str]
    packaging: NotRequired[ReportPackagingTypeType]
    encryptionKey: NotRequired[str]
    encryptionDisabled: NotRequired[bool]

class TestReportSummaryTypeDef(TypedDict):
    total: int
    statusCounts: Dict[str, int]
    durationInNanoSeconds: int

RetryBuildBatchInputTypeDef = TypedDict(
    "RetryBuildBatchInputTypeDef",
    {
        "id": NotRequired[str],
        "idempotencyToken": NotRequired[str],
        "retryType": NotRequired[RetryBuildBatchTypeType],
    },
)
RetryBuildInputTypeDef = TypedDict(
    "RetryBuildInputTypeDef",
    {
        "id": NotRequired[str],
        "idempotencyToken": NotRequired[str],
    },
)

class SSMSessionTypeDef(TypedDict):
    sessionId: NotRequired[str]
    tokenValue: NotRequired[str]
    streamUrl: NotRequired[str]

class TargetTrackingScalingConfigurationTypeDef(TypedDict):
    metricType: NotRequired[Literal["FLEET_UTILIZATION_RATE"]]
    targetValue: NotRequired[float]

StartCommandExecutionInputTypeDef = TypedDict(
    "StartCommandExecutionInputTypeDef",
    {
        "sandboxId": str,
        "command": str,
        "type": NotRequired[Literal["SHELL"]],
    },
)

class StartSandboxConnectionInputTypeDef(TypedDict):
    sandboxId: str

class StartSandboxInputTypeDef(TypedDict):
    projectName: NotRequired[str]
    idempotencyToken: NotRequired[str]

StopBuildBatchInputTypeDef = TypedDict(
    "StopBuildBatchInputTypeDef",
    {
        "id": str,
    },
)
StopBuildInputTypeDef = TypedDict(
    "StopBuildInputTypeDef",
    {
        "id": str,
    },
)
StopSandboxInputTypeDef = TypedDict(
    "StopSandboxInputTypeDef",
    {
        "id": str,
    },
)

class UpdateProjectVisibilityInputTypeDef(TypedDict):
    projectArn: str
    projectVisibility: ProjectVisibilityTypeType
    resourceAccessRole: NotRequired[str]

class VpcConfigTypeDef(TypedDict):
    vpcId: NotRequired[str]
    subnets: NotRequired[Sequence[str]]
    securityGroupIds: NotRequired[Sequence[str]]

class BatchDeleteBuildsOutputTypeDef(TypedDict):
    buildsDeleted: List[str]
    buildsNotDeleted: List[BuildNotDeletedTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBuildBatchOutputTypeDef(TypedDict):
    statusCode: str
    buildsDeleted: List[str]
    buildsNotDeleted: List[BuildNotDeletedTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSourceCredentialsOutputTypeDef(TypedDict):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyOutputTypeDef(TypedDict):
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportSourceCredentialsOutputTypeDef(TypedDict):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBuildBatchesForProjectOutputTypeDef(TypedDict):
    ids: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListBuildBatchesOutputTypeDef(TypedDict):
    ids: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListBuildsForProjectOutputTypeDef(TypedDict):
    ids: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListBuildsOutputTypeDef(TypedDict):
    ids: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListFleetsOutputTypeDef(TypedDict):
    fleets: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListProjectsOutputTypeDef(TypedDict):
    projects: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListReportGroupsOutputTypeDef(TypedDict):
    reportGroups: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListReportsForReportGroupOutputTypeDef(TypedDict):
    reports: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListReportsOutputTypeDef(TypedDict):
    reports: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSandboxesForProjectOutputTypeDef(TypedDict):
    ids: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSandboxesOutputTypeDef(TypedDict):
    ids: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSharedProjectsOutputTypeDef(TypedDict):
    projects: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSharedReportGroupsOutputTypeDef(TypedDict):
    reportGroups: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class PutResourcePolicyOutputTypeDef(TypedDict):
    resourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProjectVisibilityOutputTypeDef(TypedDict):
    projectArn: str
    publicProjectAlias: str
    projectVisibility: ProjectVisibilityTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class ProjectBuildBatchConfigOutputTypeDef(TypedDict):
    serviceRole: NotRequired[str]
    combineArtifacts: NotRequired[bool]
    restrictions: NotRequired[BatchRestrictionsOutputTypeDef]
    timeoutInMins: NotRequired[int]
    batchReportMode: NotRequired[BatchReportModeTypeType]

class ProjectBuildBatchConfigTypeDef(TypedDict):
    serviceRole: NotRequired[str]
    combineArtifacts: NotRequired[bool]
    restrictions: NotRequired[BatchRestrictionsTypeDef]
    timeoutInMins: NotRequired[int]
    batchReportMode: NotRequired[BatchReportModeTypeType]

ListBuildBatchesForProjectInputTypeDef = TypedDict(
    "ListBuildBatchesForProjectInputTypeDef",
    {
        "projectName": NotRequired[str],
        "filter": NotRequired[BuildBatchFilterTypeDef],
        "maxResults": NotRequired[int],
        "sortOrder": NotRequired[SortOrderTypeType],
        "nextToken": NotRequired[str],
    },
)
ListBuildBatchesInputTypeDef = TypedDict(
    "ListBuildBatchesInputTypeDef",
    {
        "filter": NotRequired[BuildBatchFilterTypeDef],
        "maxResults": NotRequired[int],
        "sortOrder": NotRequired[SortOrderTypeType],
        "nextToken": NotRequired[str],
    },
)

class BuildBatchPhaseTypeDef(TypedDict):
    phaseType: NotRequired[BuildBatchPhaseTypeType]
    phaseStatus: NotRequired[StatusTypeType]
    startTime: NotRequired[datetime]
    endTime: NotRequired[datetime]
    durationInSeconds: NotRequired[int]
    contexts: NotRequired[List[PhaseContextTypeDef]]

class BuildPhaseTypeDef(TypedDict):
    phaseType: NotRequired[BuildPhaseTypeType]
    phaseStatus: NotRequired[StatusTypeType]
    startTime: NotRequired[datetime]
    endTime: NotRequired[datetime]
    durationInSeconds: NotRequired[int]
    contexts: NotRequired[List[PhaseContextTypeDef]]

class SandboxSessionPhaseTypeDef(TypedDict):
    phaseType: NotRequired[str]
    phaseStatus: NotRequired[StatusTypeType]
    startTime: NotRequired[datetime]
    endTime: NotRequired[datetime]
    durationInSeconds: NotRequired[int]
    contexts: NotRequired[List[PhaseContextTypeDef]]

class BuildSummaryTypeDef(TypedDict):
    arn: NotRequired[str]
    requestedOn: NotRequired[datetime]
    buildStatus: NotRequired[StatusTypeType]
    primaryArtifact: NotRequired[ResolvedArtifactTypeDef]
    secondaryArtifacts: NotRequired[List[ResolvedArtifactTypeDef]]

class DescribeCodeCoveragesOutputTypeDef(TypedDict):
    codeCoverages: List[CodeCoverageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeCodeCoveragesInputPaginateTypeDef(TypedDict):
    reportArn: str
    sortOrder: NotRequired[SortOrderTypeType]
    sortBy: NotRequired[ReportCodeCoverageSortByTypeType]
    minLineCoveragePercentage: NotRequired[float]
    maxLineCoveragePercentage: NotRequired[float]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListBuildBatchesForProjectInputPaginateTypeDef = TypedDict(
    "ListBuildBatchesForProjectInputPaginateTypeDef",
    {
        "projectName": NotRequired[str],
        "filter": NotRequired[BuildBatchFilterTypeDef],
        "sortOrder": NotRequired[SortOrderTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListBuildBatchesInputPaginateTypeDef = TypedDict(
    "ListBuildBatchesInputPaginateTypeDef",
    {
        "filter": NotRequired[BuildBatchFilterTypeDef],
        "sortOrder": NotRequired[SortOrderTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListBuildsForProjectInputPaginateTypeDef(TypedDict):
    projectName: str
    sortOrder: NotRequired[SortOrderTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListBuildsInputPaginateTypeDef(TypedDict):
    sortOrder: NotRequired[SortOrderTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCommandExecutionsForSandboxInputPaginateTypeDef(TypedDict):
    sandboxId: str
    sortOrder: NotRequired[SortOrderTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProjectsInputPaginateTypeDef(TypedDict):
    sortBy: NotRequired[ProjectSortByTypeType]
    sortOrder: NotRequired[SortOrderTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListReportGroupsInputPaginateTypeDef(TypedDict):
    sortOrder: NotRequired[SortOrderTypeType]
    sortBy: NotRequired[ReportGroupSortByTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSandboxesForProjectInputPaginateTypeDef(TypedDict):
    projectName: str
    sortOrder: NotRequired[SortOrderTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSandboxesInputPaginateTypeDef(TypedDict):
    sortOrder: NotRequired[SortOrderTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSharedProjectsInputPaginateTypeDef(TypedDict):
    sortBy: NotRequired[SharedResourceSortByTypeType]
    sortOrder: NotRequired[SortOrderTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSharedReportGroupsInputPaginateTypeDef(TypedDict):
    sortOrder: NotRequired[SortOrderTypeType]
    sortBy: NotRequired[SharedResourceSortByTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

DescribeTestCasesInputPaginateTypeDef = TypedDict(
    "DescribeTestCasesInputPaginateTypeDef",
    {
        "reportArn": str,
        "filter": NotRequired[TestCaseFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeTestCasesInputTypeDef = TypedDict(
    "DescribeTestCasesInputTypeDef",
    {
        "reportArn": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filter": NotRequired[TestCaseFilterTypeDef],
    },
)

class DescribeTestCasesOutputTypeDef(TypedDict):
    testCases: List[TestCaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DockerServerOutputTypeDef(TypedDict):
    computeType: ComputeTypeType
    securityGroupIds: NotRequired[List[str]]
    status: NotRequired[DockerServerStatusTypeDef]

class DockerServerTypeDef(TypedDict):
    computeType: ComputeTypeType
    securityGroupIds: NotRequired[Sequence[str]]
    status: NotRequired[DockerServerStatusTypeDef]

class EnvironmentLanguageTypeDef(TypedDict):
    language: NotRequired[LanguageTypeType]
    images: NotRequired[List[EnvironmentImageTypeDef]]

class ProxyConfigurationOutputTypeDef(TypedDict):
    defaultBehavior: NotRequired[FleetProxyRuleBehaviorType]
    orderedProxyRules: NotRequired[List[FleetProxyRuleOutputTypeDef]]

class ProxyConfigurationTypeDef(TypedDict):
    defaultBehavior: NotRequired[FleetProxyRuleBehaviorType]
    orderedProxyRules: NotRequired[Sequence[FleetProxyRuleTypeDef]]

class GetReportGroupTrendOutputTypeDef(TypedDict):
    stats: ReportGroupTrendStatsTypeDef
    rawData: List[ReportWithRawDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

ListReportsForReportGroupInputPaginateTypeDef = TypedDict(
    "ListReportsForReportGroupInputPaginateTypeDef",
    {
        "reportGroupArn": str,
        "sortOrder": NotRequired[SortOrderTypeType],
        "filter": NotRequired[ReportFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReportsForReportGroupInputTypeDef = TypedDict(
    "ListReportsForReportGroupInputTypeDef",
    {
        "reportGroupArn": str,
        "nextToken": NotRequired[str],
        "sortOrder": NotRequired[SortOrderTypeType],
        "maxResults": NotRequired[int],
        "filter": NotRequired[ReportFilterTypeDef],
    },
)
ListReportsInputPaginateTypeDef = TypedDict(
    "ListReportsInputPaginateTypeDef",
    {
        "sortOrder": NotRequired[SortOrderTypeType],
        "filter": NotRequired[ReportFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReportsInputTypeDef = TypedDict(
    "ListReportsInputTypeDef",
    {
        "sortOrder": NotRequired[SortOrderTypeType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filter": NotRequired[ReportFilterTypeDef],
    },
)

class ListSourceCredentialsOutputTypeDef(TypedDict):
    sourceCredentialsInfos: List[SourceCredentialsInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LogsConfigTypeDef(TypedDict):
    cloudWatchLogs: NotRequired[CloudWatchLogsConfigTypeDef]
    s3Logs: NotRequired[S3LogsConfigTypeDef]

class LogsLocationTypeDef(TypedDict):
    groupName: NotRequired[str]
    streamName: NotRequired[str]
    deepLink: NotRequired[str]
    s3DeepLink: NotRequired[str]
    cloudWatchLogsArn: NotRequired[str]
    s3LogsArn: NotRequired[str]
    cloudWatchLogs: NotRequired[CloudWatchLogsConfigTypeDef]
    s3Logs: NotRequired[S3LogsConfigTypeDef]

ProjectCacheUnionTypeDef = Union[ProjectCacheTypeDef, ProjectCacheOutputTypeDef]
ProjectSourceTypeDef = TypedDict(
    "ProjectSourceTypeDef",
    {
        "type": SourceTypeType,
        "location": NotRequired[str],
        "gitCloneDepth": NotRequired[int],
        "gitSubmodulesConfig": NotRequired[GitSubmodulesConfigTypeDef],
        "buildspec": NotRequired[str],
        "auth": NotRequired[SourceAuthTypeDef],
        "reportBuildStatus": NotRequired[bool],
        "buildStatusConfig": NotRequired[BuildStatusConfigTypeDef],
        "insecureSsl": NotRequired[bool],
        "sourceIdentifier": NotRequired[str],
    },
)

class WebhookTypeDef(TypedDict):
    url: NotRequired[str]
    payloadUrl: NotRequired[str]
    secret: NotRequired[str]
    branchFilter: NotRequired[str]
    filterGroups: NotRequired[List[List[WebhookFilterTypeDef]]]
    buildType: NotRequired[WebhookBuildTypeType]
    manualCreation: NotRequired[bool]
    lastModifiedSecret: NotRequired[datetime]
    scopeConfiguration: NotRequired[ScopeConfigurationTypeDef]
    status: NotRequired[WebhookStatusType]
    statusMessage: NotRequired[str]
    pullRequestBuildPolicy: NotRequired[PullRequestBuildPolicyOutputTypeDef]

PullRequestBuildPolicyUnionTypeDef = Union[
    PullRequestBuildPolicyTypeDef, PullRequestBuildPolicyOutputTypeDef
]

class ReportExportConfigTypeDef(TypedDict):
    exportConfigType: NotRequired[ReportExportConfigTypeType]
    s3Destination: NotRequired[S3ReportExportConfigTypeDef]

class StartSandboxConnectionOutputTypeDef(TypedDict):
    ssmSession: SSMSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ScalingConfigurationInputTypeDef(TypedDict):
    scalingType: NotRequired[Literal["TARGET_TRACKING_SCALING"]]
    targetTrackingScalingConfigs: NotRequired[Sequence[TargetTrackingScalingConfigurationTypeDef]]
    maxCapacity: NotRequired[int]

class ScalingConfigurationOutputTypeDef(TypedDict):
    scalingType: NotRequired[Literal["TARGET_TRACKING_SCALING"]]
    targetTrackingScalingConfigs: NotRequired[List[TargetTrackingScalingConfigurationTypeDef]]
    maxCapacity: NotRequired[int]
    desiredCapacity: NotRequired[int]

VpcConfigUnionTypeDef = Union[VpcConfigTypeDef, VpcConfigOutputTypeDef]
ProjectBuildBatchConfigUnionTypeDef = Union[
    ProjectBuildBatchConfigTypeDef, ProjectBuildBatchConfigOutputTypeDef
]

class BuildGroupTypeDef(TypedDict):
    identifier: NotRequired[str]
    dependsOn: NotRequired[List[str]]
    ignoreFailure: NotRequired[bool]
    currentBuildSummary: NotRequired[BuildSummaryTypeDef]
    priorBuildSummaryList: NotRequired[List[BuildSummaryTypeDef]]

ProjectEnvironmentOutputTypeDef = TypedDict(
    "ProjectEnvironmentOutputTypeDef",
    {
        "type": EnvironmentTypeType,
        "image": str,
        "computeType": ComputeTypeType,
        "computeConfiguration": NotRequired[ComputeConfigurationTypeDef],
        "fleet": NotRequired[ProjectFleetTypeDef],
        "environmentVariables": NotRequired[List[EnvironmentVariableTypeDef]],
        "privilegedMode": NotRequired[bool],
        "certificate": NotRequired[str],
        "registryCredential": NotRequired[RegistryCredentialTypeDef],
        "imagePullCredentialsType": NotRequired[ImagePullCredentialsTypeType],
        "dockerServer": NotRequired[DockerServerOutputTypeDef],
    },
)
ProjectEnvironmentTypeDef = TypedDict(
    "ProjectEnvironmentTypeDef",
    {
        "type": EnvironmentTypeType,
        "image": str,
        "computeType": ComputeTypeType,
        "computeConfiguration": NotRequired[ComputeConfigurationTypeDef],
        "fleet": NotRequired[ProjectFleetTypeDef],
        "environmentVariables": NotRequired[Sequence[EnvironmentVariableTypeDef]],
        "privilegedMode": NotRequired[bool],
        "certificate": NotRequired[str],
        "registryCredential": NotRequired[RegistryCredentialTypeDef],
        "imagePullCredentialsType": NotRequired[ImagePullCredentialsTypeType],
        "dockerServer": NotRequired[DockerServerTypeDef],
    },
)

class EnvironmentPlatformTypeDef(TypedDict):
    platform: NotRequired[PlatformTypeType]
    languages: NotRequired[List[EnvironmentLanguageTypeDef]]

ProxyConfigurationUnionTypeDef = Union[ProxyConfigurationTypeDef, ProxyConfigurationOutputTypeDef]
CommandExecutionTypeDef = TypedDict(
    "CommandExecutionTypeDef",
    {
        "id": NotRequired[str],
        "sandboxId": NotRequired[str],
        "submitTime": NotRequired[datetime],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "status": NotRequired[str],
        "command": NotRequired[str],
        "type": NotRequired[Literal["SHELL"]],
        "exitCode": NotRequired[str],
        "standardOutputContent": NotRequired[str],
        "standardErrContent": NotRequired[str],
        "logs": NotRequired[LogsLocationTypeDef],
        "sandboxArn": NotRequired[str],
    },
)
SandboxSessionTypeDef = TypedDict(
    "SandboxSessionTypeDef",
    {
        "id": NotRequired[str],
        "status": NotRequired[str],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "currentPhase": NotRequired[str],
        "phases": NotRequired[List[SandboxSessionPhaseTypeDef]],
        "resolvedSourceVersion": NotRequired[str],
        "logs": NotRequired[LogsLocationTypeDef],
        "networkInterface": NotRequired[NetworkInterfaceTypeDef],
    },
)

class StartBuildInputTypeDef(TypedDict):
    projectName: str
    secondarySourcesOverride: NotRequired[Sequence[ProjectSourceTypeDef]]
    secondarySourcesVersionOverride: NotRequired[Sequence[ProjectSourceVersionTypeDef]]
    sourceVersion: NotRequired[str]
    artifactsOverride: NotRequired[ProjectArtifactsTypeDef]
    secondaryArtifactsOverride: NotRequired[Sequence[ProjectArtifactsTypeDef]]
    environmentVariablesOverride: NotRequired[Sequence[EnvironmentVariableTypeDef]]
    sourceTypeOverride: NotRequired[SourceTypeType]
    sourceLocationOverride: NotRequired[str]
    sourceAuthOverride: NotRequired[SourceAuthTypeDef]
    gitCloneDepthOverride: NotRequired[int]
    gitSubmodulesConfigOverride: NotRequired[GitSubmodulesConfigTypeDef]
    buildspecOverride: NotRequired[str]
    insecureSslOverride: NotRequired[bool]
    reportBuildStatusOverride: NotRequired[bool]
    buildStatusConfigOverride: NotRequired[BuildStatusConfigTypeDef]
    environmentTypeOverride: NotRequired[EnvironmentTypeType]
    imageOverride: NotRequired[str]
    computeTypeOverride: NotRequired[ComputeTypeType]
    certificateOverride: NotRequired[str]
    cacheOverride: NotRequired[ProjectCacheUnionTypeDef]
    serviceRoleOverride: NotRequired[str]
    privilegedModeOverride: NotRequired[bool]
    timeoutInMinutesOverride: NotRequired[int]
    queuedTimeoutInMinutesOverride: NotRequired[int]
    encryptionKeyOverride: NotRequired[str]
    idempotencyToken: NotRequired[str]
    logsConfigOverride: NotRequired[LogsConfigTypeDef]
    registryCredentialOverride: NotRequired[RegistryCredentialTypeDef]
    imagePullCredentialsTypeOverride: NotRequired[ImagePullCredentialsTypeType]
    debugSessionEnabled: NotRequired[bool]
    fleetOverride: NotRequired[ProjectFleetTypeDef]
    autoRetryLimitOverride: NotRequired[int]

class CreateWebhookOutputTypeDef(TypedDict):
    webhook: WebhookTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWebhookOutputTypeDef(TypedDict):
    webhook: WebhookTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWebhookInputTypeDef(TypedDict):
    projectName: str
    branchFilter: NotRequired[str]
    filterGroups: NotRequired[Sequence[Sequence[WebhookFilterTypeDef]]]
    buildType: NotRequired[WebhookBuildTypeType]
    manualCreation: NotRequired[bool]
    scopeConfiguration: NotRequired[ScopeConfigurationTypeDef]
    pullRequestBuildPolicy: NotRequired[PullRequestBuildPolicyUnionTypeDef]

class UpdateWebhookInputTypeDef(TypedDict):
    projectName: str
    branchFilter: NotRequired[str]
    rotateSecret: NotRequired[bool]
    filterGroups: NotRequired[Sequence[Sequence[WebhookFilterTypeDef]]]
    buildType: NotRequired[WebhookBuildTypeType]
    pullRequestBuildPolicy: NotRequired[PullRequestBuildPolicyUnionTypeDef]

CreateReportGroupInputTypeDef = TypedDict(
    "CreateReportGroupInputTypeDef",
    {
        "name": str,
        "type": ReportTypeType,
        "exportConfig": ReportExportConfigTypeDef,
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ReportGroupTypeDef = TypedDict(
    "ReportGroupTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[ReportTypeType],
        "exportConfig": NotRequired[ReportExportConfigTypeDef],
        "created": NotRequired[datetime],
        "lastModified": NotRequired[datetime],
        "tags": NotRequired[List[TagTypeDef]],
        "status": NotRequired[ReportGroupStatusTypeType],
    },
)
ReportTypeDef = TypedDict(
    "ReportTypeDef",
    {
        "arn": NotRequired[str],
        "type": NotRequired[ReportTypeType],
        "name": NotRequired[str],
        "reportGroupArn": NotRequired[str],
        "executionId": NotRequired[str],
        "status": NotRequired[ReportStatusTypeType],
        "created": NotRequired[datetime],
        "expired": NotRequired[datetime],
        "exportConfig": NotRequired[ReportExportConfigTypeDef],
        "truncated": NotRequired[bool],
        "testSummary": NotRequired[TestReportSummaryTypeDef],
        "codeCoverageSummary": NotRequired[CodeCoverageReportSummaryTypeDef],
    },
)

class UpdateReportGroupInputTypeDef(TypedDict):
    arn: str
    exportConfig: NotRequired[ReportExportConfigTypeDef]
    tags: NotRequired[Sequence[TagTypeDef]]

FleetTypeDef = TypedDict(
    "FleetTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "id": NotRequired[str],
        "created": NotRequired[datetime],
        "lastModified": NotRequired[datetime],
        "status": NotRequired[FleetStatusTypeDef],
        "baseCapacity": NotRequired[int],
        "environmentType": NotRequired[EnvironmentTypeType],
        "computeType": NotRequired[ComputeTypeType],
        "computeConfiguration": NotRequired[ComputeConfigurationTypeDef],
        "scalingConfiguration": NotRequired[ScalingConfigurationOutputTypeDef],
        "overflowBehavior": NotRequired[FleetOverflowBehaviorType],
        "vpcConfig": NotRequired[VpcConfigOutputTypeDef],
        "proxyConfiguration": NotRequired[ProxyConfigurationOutputTypeDef],
        "imageId": NotRequired[str],
        "fleetServiceRole": NotRequired[str],
        "tags": NotRequired[List[TagTypeDef]],
    },
)

class StartBuildBatchInputTypeDef(TypedDict):
    projectName: str
    secondarySourcesOverride: NotRequired[Sequence[ProjectSourceTypeDef]]
    secondarySourcesVersionOverride: NotRequired[Sequence[ProjectSourceVersionTypeDef]]
    sourceVersion: NotRequired[str]
    artifactsOverride: NotRequired[ProjectArtifactsTypeDef]
    secondaryArtifactsOverride: NotRequired[Sequence[ProjectArtifactsTypeDef]]
    environmentVariablesOverride: NotRequired[Sequence[EnvironmentVariableTypeDef]]
    sourceTypeOverride: NotRequired[SourceTypeType]
    sourceLocationOverride: NotRequired[str]
    sourceAuthOverride: NotRequired[SourceAuthTypeDef]
    gitCloneDepthOverride: NotRequired[int]
    gitSubmodulesConfigOverride: NotRequired[GitSubmodulesConfigTypeDef]
    buildspecOverride: NotRequired[str]
    insecureSslOverride: NotRequired[bool]
    reportBuildBatchStatusOverride: NotRequired[bool]
    environmentTypeOverride: NotRequired[EnvironmentTypeType]
    imageOverride: NotRequired[str]
    computeTypeOverride: NotRequired[ComputeTypeType]
    certificateOverride: NotRequired[str]
    cacheOverride: NotRequired[ProjectCacheUnionTypeDef]
    serviceRoleOverride: NotRequired[str]
    privilegedModeOverride: NotRequired[bool]
    buildTimeoutInMinutesOverride: NotRequired[int]
    queuedTimeoutInMinutesOverride: NotRequired[int]
    encryptionKeyOverride: NotRequired[str]
    idempotencyToken: NotRequired[str]
    logsConfigOverride: NotRequired[LogsConfigTypeDef]
    registryCredentialOverride: NotRequired[RegistryCredentialTypeDef]
    imagePullCredentialsTypeOverride: NotRequired[ImagePullCredentialsTypeType]
    buildBatchConfigOverride: NotRequired[ProjectBuildBatchConfigUnionTypeDef]
    debugSessionEnabled: NotRequired[bool]

BuildBatchTypeDef = TypedDict(
    "BuildBatchTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "currentPhase": NotRequired[str],
        "buildBatchStatus": NotRequired[StatusTypeType],
        "sourceVersion": NotRequired[str],
        "resolvedSourceVersion": NotRequired[str],
        "projectName": NotRequired[str],
        "phases": NotRequired[List[BuildBatchPhaseTypeDef]],
        "source": NotRequired[ProjectSourceTypeDef],
        "secondarySources": NotRequired[List[ProjectSourceTypeDef]],
        "secondarySourceVersions": NotRequired[List[ProjectSourceVersionTypeDef]],
        "artifacts": NotRequired[BuildArtifactsTypeDef],
        "secondaryArtifacts": NotRequired[List[BuildArtifactsTypeDef]],
        "cache": NotRequired[ProjectCacheOutputTypeDef],
        "environment": NotRequired[ProjectEnvironmentOutputTypeDef],
        "serviceRole": NotRequired[str],
        "logConfig": NotRequired[LogsConfigTypeDef],
        "buildTimeoutInMinutes": NotRequired[int],
        "queuedTimeoutInMinutes": NotRequired[int],
        "complete": NotRequired[bool],
        "initiator": NotRequired[str],
        "vpcConfig": NotRequired[VpcConfigOutputTypeDef],
        "encryptionKey": NotRequired[str],
        "buildBatchNumber": NotRequired[int],
        "fileSystemLocations": NotRequired[List[ProjectFileSystemLocationTypeDef]],
        "buildBatchConfig": NotRequired[ProjectBuildBatchConfigOutputTypeDef],
        "buildGroups": NotRequired[List[BuildGroupTypeDef]],
        "debugSessionEnabled": NotRequired[bool],
        "reportArns": NotRequired[List[str]],
    },
)
BuildTypeDef = TypedDict(
    "BuildTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "buildNumber": NotRequired[int],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "currentPhase": NotRequired[str],
        "buildStatus": NotRequired[StatusTypeType],
        "sourceVersion": NotRequired[str],
        "resolvedSourceVersion": NotRequired[str],
        "projectName": NotRequired[str],
        "phases": NotRequired[List[BuildPhaseTypeDef]],
        "source": NotRequired[ProjectSourceTypeDef],
        "secondarySources": NotRequired[List[ProjectSourceTypeDef]],
        "secondarySourceVersions": NotRequired[List[ProjectSourceVersionTypeDef]],
        "artifacts": NotRequired[BuildArtifactsTypeDef],
        "secondaryArtifacts": NotRequired[List[BuildArtifactsTypeDef]],
        "cache": NotRequired[ProjectCacheOutputTypeDef],
        "environment": NotRequired[ProjectEnvironmentOutputTypeDef],
        "serviceRole": NotRequired[str],
        "logs": NotRequired[LogsLocationTypeDef],
        "timeoutInMinutes": NotRequired[int],
        "queuedTimeoutInMinutes": NotRequired[int],
        "buildComplete": NotRequired[bool],
        "initiator": NotRequired[str],
        "vpcConfig": NotRequired[VpcConfigOutputTypeDef],
        "networkInterface": NotRequired[NetworkInterfaceTypeDef],
        "encryptionKey": NotRequired[str],
        "exportedEnvironmentVariables": NotRequired[List[ExportedEnvironmentVariableTypeDef]],
        "reportArns": NotRequired[List[str]],
        "fileSystemLocations": NotRequired[List[ProjectFileSystemLocationTypeDef]],
        "debugSession": NotRequired[DebugSessionTypeDef],
        "buildBatchArn": NotRequired[str],
        "autoRetryConfig": NotRequired[AutoRetryConfigTypeDef],
    },
)

class ProjectTypeDef(TypedDict):
    name: NotRequired[str]
    arn: NotRequired[str]
    description: NotRequired[str]
    source: NotRequired[ProjectSourceTypeDef]
    secondarySources: NotRequired[List[ProjectSourceTypeDef]]
    sourceVersion: NotRequired[str]
    secondarySourceVersions: NotRequired[List[ProjectSourceVersionTypeDef]]
    artifacts: NotRequired[ProjectArtifactsTypeDef]
    secondaryArtifacts: NotRequired[List[ProjectArtifactsTypeDef]]
    cache: NotRequired[ProjectCacheOutputTypeDef]
    environment: NotRequired[ProjectEnvironmentOutputTypeDef]
    serviceRole: NotRequired[str]
    timeoutInMinutes: NotRequired[int]
    queuedTimeoutInMinutes: NotRequired[int]
    encryptionKey: NotRequired[str]
    tags: NotRequired[List[TagTypeDef]]
    created: NotRequired[datetime]
    lastModified: NotRequired[datetime]
    webhook: NotRequired[WebhookTypeDef]
    vpcConfig: NotRequired[VpcConfigOutputTypeDef]
    badge: NotRequired[ProjectBadgeTypeDef]
    logsConfig: NotRequired[LogsConfigTypeDef]
    fileSystemLocations: NotRequired[List[ProjectFileSystemLocationTypeDef]]
    buildBatchConfig: NotRequired[ProjectBuildBatchConfigOutputTypeDef]
    concurrentBuildLimit: NotRequired[int]
    projectVisibility: NotRequired[ProjectVisibilityTypeType]
    publicProjectAlias: NotRequired[str]
    resourceAccessRole: NotRequired[str]
    autoRetryLimit: NotRequired[int]

ProjectEnvironmentUnionTypeDef = Union[ProjectEnvironmentTypeDef, ProjectEnvironmentOutputTypeDef]

class ListCuratedEnvironmentImagesOutputTypeDef(TypedDict):
    platforms: List[EnvironmentPlatformTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFleetInputTypeDef(TypedDict):
    name: str
    baseCapacity: int
    environmentType: EnvironmentTypeType
    computeType: ComputeTypeType
    computeConfiguration: NotRequired[ComputeConfigurationTypeDef]
    scalingConfiguration: NotRequired[ScalingConfigurationInputTypeDef]
    overflowBehavior: NotRequired[FleetOverflowBehaviorType]
    vpcConfig: NotRequired[VpcConfigUnionTypeDef]
    proxyConfiguration: NotRequired[ProxyConfigurationUnionTypeDef]
    imageId: NotRequired[str]
    fleetServiceRole: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class UpdateFleetInputTypeDef(TypedDict):
    arn: str
    baseCapacity: NotRequired[int]
    environmentType: NotRequired[EnvironmentTypeType]
    computeType: NotRequired[ComputeTypeType]
    computeConfiguration: NotRequired[ComputeConfigurationTypeDef]
    scalingConfiguration: NotRequired[ScalingConfigurationInputTypeDef]
    overflowBehavior: NotRequired[FleetOverflowBehaviorType]
    vpcConfig: NotRequired[VpcConfigUnionTypeDef]
    proxyConfiguration: NotRequired[ProxyConfigurationUnionTypeDef]
    imageId: NotRequired[str]
    fleetServiceRole: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class BatchGetCommandExecutionsOutputTypeDef(TypedDict):
    commandExecutions: List[CommandExecutionTypeDef]
    commandExecutionsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCommandExecutionsForSandboxOutputTypeDef(TypedDict):
    commandExecutions: List[CommandExecutionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StartCommandExecutionOutputTypeDef(TypedDict):
    commandExecution: CommandExecutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

SandboxTypeDef = TypedDict(
    "SandboxTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "projectName": NotRequired[str],
        "requestTime": NotRequired[datetime],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "status": NotRequired[str],
        "source": NotRequired[ProjectSourceTypeDef],
        "sourceVersion": NotRequired[str],
        "secondarySources": NotRequired[List[ProjectSourceTypeDef]],
        "secondarySourceVersions": NotRequired[List[ProjectSourceVersionTypeDef]],
        "environment": NotRequired[ProjectEnvironmentOutputTypeDef],
        "fileSystemLocations": NotRequired[List[ProjectFileSystemLocationTypeDef]],
        "timeoutInMinutes": NotRequired[int],
        "queuedTimeoutInMinutes": NotRequired[int],
        "vpcConfig": NotRequired[VpcConfigOutputTypeDef],
        "logConfig": NotRequired[LogsConfigTypeDef],
        "encryptionKey": NotRequired[str],
        "serviceRole": NotRequired[str],
        "currentSession": NotRequired[SandboxSessionTypeDef],
    },
)

class BatchGetReportGroupsOutputTypeDef(TypedDict):
    reportGroups: List[ReportGroupTypeDef]
    reportGroupsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReportGroupOutputTypeDef(TypedDict):
    reportGroup: ReportGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReportGroupOutputTypeDef(TypedDict):
    reportGroup: ReportGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetReportsOutputTypeDef(TypedDict):
    reports: List[ReportTypeDef]
    reportsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetFleetsOutputTypeDef(TypedDict):
    fleets: List[FleetTypeDef]
    fleetsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFleetOutputTypeDef(TypedDict):
    fleet: FleetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFleetOutputTypeDef(TypedDict):
    fleet: FleetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetBuildBatchesOutputTypeDef(TypedDict):
    buildBatches: List[BuildBatchTypeDef]
    buildBatchesNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class RetryBuildBatchOutputTypeDef(TypedDict):
    buildBatch: BuildBatchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartBuildBatchOutputTypeDef(TypedDict):
    buildBatch: BuildBatchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopBuildBatchOutputTypeDef(TypedDict):
    buildBatch: BuildBatchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetBuildsOutputTypeDef(TypedDict):
    builds: List[BuildTypeDef]
    buildsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class RetryBuildOutputTypeDef(TypedDict):
    build: BuildTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartBuildOutputTypeDef(TypedDict):
    build: BuildTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopBuildOutputTypeDef(TypedDict):
    build: BuildTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetProjectsOutputTypeDef(TypedDict):
    projects: List[ProjectTypeDef]
    projectsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectOutputTypeDef(TypedDict):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProjectOutputTypeDef(TypedDict):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectInputTypeDef(TypedDict):
    name: str
    source: ProjectSourceTypeDef
    artifacts: ProjectArtifactsTypeDef
    environment: ProjectEnvironmentUnionTypeDef
    serviceRole: str
    description: NotRequired[str]
    secondarySources: NotRequired[Sequence[ProjectSourceTypeDef]]
    sourceVersion: NotRequired[str]
    secondarySourceVersions: NotRequired[Sequence[ProjectSourceVersionTypeDef]]
    secondaryArtifacts: NotRequired[Sequence[ProjectArtifactsTypeDef]]
    cache: NotRequired[ProjectCacheUnionTypeDef]
    timeoutInMinutes: NotRequired[int]
    queuedTimeoutInMinutes: NotRequired[int]
    encryptionKey: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]
    vpcConfig: NotRequired[VpcConfigUnionTypeDef]
    badgeEnabled: NotRequired[bool]
    logsConfig: NotRequired[LogsConfigTypeDef]
    fileSystemLocations: NotRequired[Sequence[ProjectFileSystemLocationTypeDef]]
    buildBatchConfig: NotRequired[ProjectBuildBatchConfigUnionTypeDef]
    concurrentBuildLimit: NotRequired[int]
    autoRetryLimit: NotRequired[int]

class UpdateProjectInputTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    source: NotRequired[ProjectSourceTypeDef]
    secondarySources: NotRequired[Sequence[ProjectSourceTypeDef]]
    sourceVersion: NotRequired[str]
    secondarySourceVersions: NotRequired[Sequence[ProjectSourceVersionTypeDef]]
    artifacts: NotRequired[ProjectArtifactsTypeDef]
    secondaryArtifacts: NotRequired[Sequence[ProjectArtifactsTypeDef]]
    cache: NotRequired[ProjectCacheUnionTypeDef]
    environment: NotRequired[ProjectEnvironmentUnionTypeDef]
    serviceRole: NotRequired[str]
    timeoutInMinutes: NotRequired[int]
    queuedTimeoutInMinutes: NotRequired[int]
    encryptionKey: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]
    vpcConfig: NotRequired[VpcConfigUnionTypeDef]
    badgeEnabled: NotRequired[bool]
    logsConfig: NotRequired[LogsConfigTypeDef]
    fileSystemLocations: NotRequired[Sequence[ProjectFileSystemLocationTypeDef]]
    buildBatchConfig: NotRequired[ProjectBuildBatchConfigUnionTypeDef]
    concurrentBuildLimit: NotRequired[int]
    autoRetryLimit: NotRequired[int]

class BatchGetSandboxesOutputTypeDef(TypedDict):
    sandboxes: List[SandboxTypeDef]
    sandboxesNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartSandboxOutputTypeDef(TypedDict):
    sandbox: SandboxTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopSandboxOutputTypeDef(TypedDict):
    sandbox: SandboxTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
