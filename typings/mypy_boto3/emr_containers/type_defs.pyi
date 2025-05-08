"""
Type annotations for emr-containers service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_emr_containers.type_defs import CancelJobRunRequestTypeDef

    data: CancelJobRunRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    AllowAWSToRetainLogsType,
    EndpointStateType,
    FailureReasonType,
    JobRunStateType,
    PersistentAppUIType,
    TemplateParameterDataTypeType,
    VirtualClusterStateType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AuthorizationConfigurationTypeDef",
    "CancelJobRunRequestTypeDef",
    "CancelJobRunResponseTypeDef",
    "CertificateTypeDef",
    "CloudWatchMonitoringConfigurationTypeDef",
    "ConfigurationOutputTypeDef",
    "ConfigurationOverridesOutputTypeDef",
    "ConfigurationOverridesPaginatorTypeDef",
    "ConfigurationOverridesTypeDef",
    "ConfigurationOverridesUnionTypeDef",
    "ConfigurationPaginatorTypeDef",
    "ConfigurationTypeDef",
    "ContainerInfoTypeDef",
    "ContainerLogRotationConfigurationTypeDef",
    "ContainerProviderTypeDef",
    "CreateJobTemplateRequestTypeDef",
    "CreateJobTemplateResponseTypeDef",
    "CreateManagedEndpointRequestTypeDef",
    "CreateManagedEndpointResponseTypeDef",
    "CreateSecurityConfigurationRequestTypeDef",
    "CreateSecurityConfigurationResponseTypeDef",
    "CreateVirtualClusterRequestTypeDef",
    "CreateVirtualClusterResponseTypeDef",
    "CredentialsTypeDef",
    "DeleteJobTemplateRequestTypeDef",
    "DeleteJobTemplateResponseTypeDef",
    "DeleteManagedEndpointRequestTypeDef",
    "DeleteManagedEndpointResponseTypeDef",
    "DeleteVirtualClusterRequestTypeDef",
    "DeleteVirtualClusterResponseTypeDef",
    "DescribeJobRunRequestTypeDef",
    "DescribeJobRunResponseTypeDef",
    "DescribeJobTemplateRequestTypeDef",
    "DescribeJobTemplateResponseTypeDef",
    "DescribeManagedEndpointRequestTypeDef",
    "DescribeManagedEndpointResponseTypeDef",
    "DescribeSecurityConfigurationRequestTypeDef",
    "DescribeSecurityConfigurationResponseTypeDef",
    "DescribeVirtualClusterRequestTypeDef",
    "DescribeVirtualClusterResponseTypeDef",
    "EksInfoTypeDef",
    "EncryptionConfigurationTypeDef",
    "EndpointPaginatorTypeDef",
    "EndpointTypeDef",
    "GetManagedEndpointSessionCredentialsRequestTypeDef",
    "GetManagedEndpointSessionCredentialsResponseTypeDef",
    "InTransitEncryptionConfigurationTypeDef",
    "JobDriverOutputTypeDef",
    "JobDriverTypeDef",
    "JobDriverUnionTypeDef",
    "JobRunPaginatorTypeDef",
    "JobRunTypeDef",
    "JobTemplateDataOutputTypeDef",
    "JobTemplateDataPaginatorTypeDef",
    "JobTemplateDataTypeDef",
    "JobTemplateDataUnionTypeDef",
    "JobTemplatePaginatorTypeDef",
    "JobTemplateTypeDef",
    "LakeFormationConfigurationTypeDef",
    "ListJobRunsRequestPaginateTypeDef",
    "ListJobRunsRequestTypeDef",
    "ListJobRunsResponsePaginatorTypeDef",
    "ListJobRunsResponseTypeDef",
    "ListJobTemplatesRequestPaginateTypeDef",
    "ListJobTemplatesRequestTypeDef",
    "ListJobTemplatesResponsePaginatorTypeDef",
    "ListJobTemplatesResponseTypeDef",
    "ListManagedEndpointsRequestPaginateTypeDef",
    "ListManagedEndpointsRequestTypeDef",
    "ListManagedEndpointsResponsePaginatorTypeDef",
    "ListManagedEndpointsResponseTypeDef",
    "ListSecurityConfigurationsRequestPaginateTypeDef",
    "ListSecurityConfigurationsRequestTypeDef",
    "ListSecurityConfigurationsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVirtualClustersRequestPaginateTypeDef",
    "ListVirtualClustersRequestTypeDef",
    "ListVirtualClustersResponseTypeDef",
    "ManagedLogsTypeDef",
    "MonitoringConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ParametricCloudWatchMonitoringConfigurationTypeDef",
    "ParametricConfigurationOverridesOutputTypeDef",
    "ParametricConfigurationOverridesPaginatorTypeDef",
    "ParametricConfigurationOverridesTypeDef",
    "ParametricMonitoringConfigurationTypeDef",
    "ParametricS3MonitoringConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "RetryPolicyConfigurationTypeDef",
    "RetryPolicyExecutionTypeDef",
    "S3MonitoringConfigurationTypeDef",
    "SecureNamespaceInfoTypeDef",
    "SecurityConfigurationDataTypeDef",
    "SecurityConfigurationTypeDef",
    "SparkSqlJobDriverTypeDef",
    "SparkSubmitJobDriverOutputTypeDef",
    "SparkSubmitJobDriverTypeDef",
    "StartJobRunRequestTypeDef",
    "StartJobRunResponseTypeDef",
    "TLSCertificateConfigurationTypeDef",
    "TagResourceRequestTypeDef",
    "TemplateParameterConfigurationTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "VirtualClusterTypeDef",
)

CancelJobRunRequestTypeDef = TypedDict(
    "CancelJobRunRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
    },
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CertificateTypeDef(TypedDict):
    certificateArn: NotRequired[str]
    certificateData: NotRequired[str]

class CloudWatchMonitoringConfigurationTypeDef(TypedDict):
    logGroupName: str
    logStreamNamePrefix: NotRequired[str]

class ConfigurationOutputTypeDef(TypedDict):
    classification: str
    properties: NotRequired[Dict[str, str]]
    configurations: NotRequired[List[Dict[str, Any]]]

class ConfigurationPaginatorTypeDef(TypedDict):
    classification: str
    properties: NotRequired[Dict[str, str]]
    configurations: NotRequired[List[Dict[str, Any]]]

class ConfigurationTypeDef(TypedDict):
    classification: str
    properties: NotRequired[Mapping[str, str]]
    configurations: NotRequired[Sequence[Mapping[str, Any]]]

class EksInfoTypeDef(TypedDict):
    namespace: NotRequired[str]

class ContainerLogRotationConfigurationTypeDef(TypedDict):
    rotationSize: str
    maxFilesToKeep: int

class CredentialsTypeDef(TypedDict):
    token: NotRequired[str]

DeleteJobTemplateRequestTypeDef = TypedDict(
    "DeleteJobTemplateRequestTypeDef",
    {
        "id": str,
    },
)
DeleteManagedEndpointRequestTypeDef = TypedDict(
    "DeleteManagedEndpointRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
    },
)
DeleteVirtualClusterRequestTypeDef = TypedDict(
    "DeleteVirtualClusterRequestTypeDef",
    {
        "id": str,
    },
)
DescribeJobRunRequestTypeDef = TypedDict(
    "DescribeJobRunRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
    },
)
DescribeJobTemplateRequestTypeDef = TypedDict(
    "DescribeJobTemplateRequestTypeDef",
    {
        "id": str,
    },
)
DescribeManagedEndpointRequestTypeDef = TypedDict(
    "DescribeManagedEndpointRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
    },
)
DescribeSecurityConfigurationRequestTypeDef = TypedDict(
    "DescribeSecurityConfigurationRequestTypeDef",
    {
        "id": str,
    },
)
DescribeVirtualClusterRequestTypeDef = TypedDict(
    "DescribeVirtualClusterRequestTypeDef",
    {
        "id": str,
    },
)

class GetManagedEndpointSessionCredentialsRequestTypeDef(TypedDict):
    endpointIdentifier: str
    virtualClusterIdentifier: str
    executionRoleArn: str
    credentialType: str
    durationInSeconds: NotRequired[int]
    logContext: NotRequired[str]
    clientToken: NotRequired[str]

class TLSCertificateConfigurationTypeDef(TypedDict):
    certificateProviderType: NotRequired[Literal["PEM"]]
    publicCertificateSecretArn: NotRequired[str]
    privateCertificateSecretArn: NotRequired[str]

class SparkSqlJobDriverTypeDef(TypedDict):
    entryPoint: NotRequired[str]
    sparkSqlParameters: NotRequired[str]

class SparkSubmitJobDriverOutputTypeDef(TypedDict):
    entryPoint: str
    entryPointArguments: NotRequired[List[str]]
    sparkSubmitParameters: NotRequired[str]

class SparkSubmitJobDriverTypeDef(TypedDict):
    entryPoint: str
    entryPointArguments: NotRequired[Sequence[str]]
    sparkSubmitParameters: NotRequired[str]

class RetryPolicyConfigurationTypeDef(TypedDict):
    maxAttempts: int

class RetryPolicyExecutionTypeDef(TypedDict):
    currentAttemptCount: int

TemplateParameterConfigurationTypeDef = TypedDict(
    "TemplateParameterConfigurationTypeDef",
    {
        "type": NotRequired[TemplateParameterDataTypeType],
        "defaultValue": NotRequired[str],
    },
)

class SecureNamespaceInfoTypeDef(TypedDict):
    clusterId: NotRequired[str]
    namespace: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ManagedLogsTypeDef(TypedDict):
    allowAWSToRetainLogs: NotRequired[AllowAWSToRetainLogsType]
    encryptionKeyArn: NotRequired[str]

class S3MonitoringConfigurationTypeDef(TypedDict):
    logUri: str

class ParametricCloudWatchMonitoringConfigurationTypeDef(TypedDict):
    logGroupName: NotRequired[str]
    logStreamNamePrefix: NotRequired[str]

class ParametricS3MonitoringConfigurationTypeDef(TypedDict):
    logUri: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

CancelJobRunResponseTypeDef = TypedDict(
    "CancelJobRunResponseTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateJobTemplateResponseTypeDef = TypedDict(
    "CreateJobTemplateResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateManagedEndpointResponseTypeDef = TypedDict(
    "CreateManagedEndpointResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "virtualClusterId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSecurityConfigurationResponseTypeDef = TypedDict(
    "CreateSecurityConfigurationResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVirtualClusterResponseTypeDef = TypedDict(
    "CreateVirtualClusterResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteJobTemplateResponseTypeDef = TypedDict(
    "DeleteJobTemplateResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteManagedEndpointResponseTypeDef = TypedDict(
    "DeleteManagedEndpointResponseTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVirtualClusterResponseTypeDef = TypedDict(
    "DeleteVirtualClusterResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

StartJobRunResponseTypeDef = TypedDict(
    "StartJobRunResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "virtualClusterId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ContainerInfoTypeDef(TypedDict):
    eksInfo: NotRequired[EksInfoTypeDef]

GetManagedEndpointSessionCredentialsResponseTypeDef = TypedDict(
    "GetManagedEndpointSessionCredentialsResponseTypeDef",
    {
        "id": str,
        "credentials": CredentialsTypeDef,
        "expiresAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class InTransitEncryptionConfigurationTypeDef(TypedDict):
    tlsCertificateConfiguration: NotRequired[TLSCertificateConfigurationTypeDef]

class JobDriverOutputTypeDef(TypedDict):
    sparkSubmitJobDriver: NotRequired[SparkSubmitJobDriverOutputTypeDef]
    sparkSqlJobDriver: NotRequired[SparkSqlJobDriverTypeDef]

class JobDriverTypeDef(TypedDict):
    sparkSubmitJobDriver: NotRequired[SparkSubmitJobDriverTypeDef]
    sparkSqlJobDriver: NotRequired[SparkSqlJobDriverTypeDef]

class LakeFormationConfigurationTypeDef(TypedDict):
    authorizedSessionTagValue: NotRequired[str]
    secureNamespaceInfo: NotRequired[SecureNamespaceInfoTypeDef]
    queryEngineRoleArn: NotRequired[str]

class ListJobRunsRequestPaginateTypeDef(TypedDict):
    virtualClusterId: str
    createdBefore: NotRequired[TimestampTypeDef]
    createdAfter: NotRequired[TimestampTypeDef]
    name: NotRequired[str]
    states: NotRequired[Sequence[JobRunStateType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListJobRunsRequestTypeDef(TypedDict):
    virtualClusterId: str
    createdBefore: NotRequired[TimestampTypeDef]
    createdAfter: NotRequired[TimestampTypeDef]
    name: NotRequired[str]
    states: NotRequired[Sequence[JobRunStateType]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListJobTemplatesRequestPaginateTypeDef(TypedDict):
    createdAfter: NotRequired[TimestampTypeDef]
    createdBefore: NotRequired[TimestampTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListJobTemplatesRequestTypeDef(TypedDict):
    createdAfter: NotRequired[TimestampTypeDef]
    createdBefore: NotRequired[TimestampTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

ListManagedEndpointsRequestPaginateTypeDef = TypedDict(
    "ListManagedEndpointsRequestPaginateTypeDef",
    {
        "virtualClusterId": str,
        "createdBefore": NotRequired[TimestampTypeDef],
        "createdAfter": NotRequired[TimestampTypeDef],
        "types": NotRequired[Sequence[str]],
        "states": NotRequired[Sequence[EndpointStateType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListManagedEndpointsRequestTypeDef = TypedDict(
    "ListManagedEndpointsRequestTypeDef",
    {
        "virtualClusterId": str,
        "createdBefore": NotRequired[TimestampTypeDef],
        "createdAfter": NotRequired[TimestampTypeDef],
        "types": NotRequired[Sequence[str]],
        "states": NotRequired[Sequence[EndpointStateType]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

class ListSecurityConfigurationsRequestPaginateTypeDef(TypedDict):
    createdAfter: NotRequired[TimestampTypeDef]
    createdBefore: NotRequired[TimestampTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSecurityConfigurationsRequestTypeDef(TypedDict):
    createdAfter: NotRequired[TimestampTypeDef]
    createdBefore: NotRequired[TimestampTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListVirtualClustersRequestPaginateTypeDef(TypedDict):
    containerProviderId: NotRequired[str]
    containerProviderType: NotRequired[Literal["EKS"]]
    createdAfter: NotRequired[TimestampTypeDef]
    createdBefore: NotRequired[TimestampTypeDef]
    states: NotRequired[Sequence[VirtualClusterStateType]]
    eksAccessEntryIntegrated: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListVirtualClustersRequestTypeDef(TypedDict):
    containerProviderId: NotRequired[str]
    containerProviderType: NotRequired[Literal["EKS"]]
    createdAfter: NotRequired[TimestampTypeDef]
    createdBefore: NotRequired[TimestampTypeDef]
    states: NotRequired[Sequence[VirtualClusterStateType]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    eksAccessEntryIntegrated: NotRequired[bool]

class MonitoringConfigurationTypeDef(TypedDict):
    managedLogs: NotRequired[ManagedLogsTypeDef]
    persistentAppUI: NotRequired[PersistentAppUIType]
    cloudWatchMonitoringConfiguration: NotRequired[CloudWatchMonitoringConfigurationTypeDef]
    s3MonitoringConfiguration: NotRequired[S3MonitoringConfigurationTypeDef]
    containerLogRotationConfiguration: NotRequired[ContainerLogRotationConfigurationTypeDef]

class ParametricMonitoringConfigurationTypeDef(TypedDict):
    persistentAppUI: NotRequired[str]
    cloudWatchMonitoringConfiguration: NotRequired[
        ParametricCloudWatchMonitoringConfigurationTypeDef
    ]
    s3MonitoringConfiguration: NotRequired[ParametricS3MonitoringConfigurationTypeDef]

ContainerProviderTypeDef = TypedDict(
    "ContainerProviderTypeDef",
    {
        "type": Literal["EKS"],
        "id": str,
        "info": NotRequired[ContainerInfoTypeDef],
    },
)

class EncryptionConfigurationTypeDef(TypedDict):
    inTransitEncryptionConfiguration: NotRequired[InTransitEncryptionConfigurationTypeDef]

JobDriverUnionTypeDef = Union[JobDriverTypeDef, JobDriverOutputTypeDef]

class ConfigurationOverridesOutputTypeDef(TypedDict):
    applicationConfiguration: NotRequired[List[ConfigurationOutputTypeDef]]
    monitoringConfiguration: NotRequired[MonitoringConfigurationTypeDef]

class ConfigurationOverridesPaginatorTypeDef(TypedDict):
    applicationConfiguration: NotRequired[List[ConfigurationPaginatorTypeDef]]
    monitoringConfiguration: NotRequired[MonitoringConfigurationTypeDef]

class ConfigurationOverridesTypeDef(TypedDict):
    applicationConfiguration: NotRequired[Sequence[ConfigurationTypeDef]]
    monitoringConfiguration: NotRequired[MonitoringConfigurationTypeDef]

class ParametricConfigurationOverridesOutputTypeDef(TypedDict):
    applicationConfiguration: NotRequired[List[ConfigurationOutputTypeDef]]
    monitoringConfiguration: NotRequired[ParametricMonitoringConfigurationTypeDef]

class ParametricConfigurationOverridesPaginatorTypeDef(TypedDict):
    applicationConfiguration: NotRequired[List[ConfigurationPaginatorTypeDef]]
    monitoringConfiguration: NotRequired[ParametricMonitoringConfigurationTypeDef]

class ParametricConfigurationOverridesTypeDef(TypedDict):
    applicationConfiguration: NotRequired[Sequence[ConfigurationTypeDef]]
    monitoringConfiguration: NotRequired[ParametricMonitoringConfigurationTypeDef]

class CreateVirtualClusterRequestTypeDef(TypedDict):
    name: str
    containerProvider: ContainerProviderTypeDef
    clientToken: str
    tags: NotRequired[Mapping[str, str]]
    securityConfigurationId: NotRequired[str]

VirtualClusterTypeDef = TypedDict(
    "VirtualClusterTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "state": NotRequired[VirtualClusterStateType],
        "containerProvider": NotRequired[ContainerProviderTypeDef],
        "createdAt": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
        "securityConfigurationId": NotRequired[str],
    },
)

class AuthorizationConfigurationTypeDef(TypedDict):
    lakeFormationConfiguration: NotRequired[LakeFormationConfigurationTypeDef]
    encryptionConfiguration: NotRequired[EncryptionConfigurationTypeDef]

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "virtualClusterId": NotRequired[str],
        "type": NotRequired[str],
        "state": NotRequired[EndpointStateType],
        "releaseLabel": NotRequired[str],
        "executionRoleArn": NotRequired[str],
        "certificateArn": NotRequired[str],
        "certificateAuthority": NotRequired[CertificateTypeDef],
        "configurationOverrides": NotRequired[ConfigurationOverridesOutputTypeDef],
        "serverUrl": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "securityGroup": NotRequired[str],
        "subnetIds": NotRequired[List[str]],
        "stateDetails": NotRequired[str],
        "failureReason": NotRequired[FailureReasonType],
        "tags": NotRequired[Dict[str, str]],
    },
)
JobRunTypeDef = TypedDict(
    "JobRunTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "virtualClusterId": NotRequired[str],
        "arn": NotRequired[str],
        "state": NotRequired[JobRunStateType],
        "clientToken": NotRequired[str],
        "executionRoleArn": NotRequired[str],
        "releaseLabel": NotRequired[str],
        "configurationOverrides": NotRequired[ConfigurationOverridesOutputTypeDef],
        "jobDriver": NotRequired[JobDriverOutputTypeDef],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "finishedAt": NotRequired[datetime],
        "stateDetails": NotRequired[str],
        "failureReason": NotRequired[FailureReasonType],
        "tags": NotRequired[Dict[str, str]],
        "retryPolicyConfiguration": NotRequired[RetryPolicyConfigurationTypeDef],
        "retryPolicyExecution": NotRequired[RetryPolicyExecutionTypeDef],
    },
)
EndpointPaginatorTypeDef = TypedDict(
    "EndpointPaginatorTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "virtualClusterId": NotRequired[str],
        "type": NotRequired[str],
        "state": NotRequired[EndpointStateType],
        "releaseLabel": NotRequired[str],
        "executionRoleArn": NotRequired[str],
        "certificateArn": NotRequired[str],
        "certificateAuthority": NotRequired[CertificateTypeDef],
        "configurationOverrides": NotRequired[ConfigurationOverridesPaginatorTypeDef],
        "serverUrl": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "securityGroup": NotRequired[str],
        "subnetIds": NotRequired[List[str]],
        "stateDetails": NotRequired[str],
        "failureReason": NotRequired[FailureReasonType],
        "tags": NotRequired[Dict[str, str]],
    },
)
JobRunPaginatorTypeDef = TypedDict(
    "JobRunPaginatorTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "virtualClusterId": NotRequired[str],
        "arn": NotRequired[str],
        "state": NotRequired[JobRunStateType],
        "clientToken": NotRequired[str],
        "executionRoleArn": NotRequired[str],
        "releaseLabel": NotRequired[str],
        "configurationOverrides": NotRequired[ConfigurationOverridesPaginatorTypeDef],
        "jobDriver": NotRequired[JobDriverOutputTypeDef],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "finishedAt": NotRequired[datetime],
        "stateDetails": NotRequired[str],
        "failureReason": NotRequired[FailureReasonType],
        "tags": NotRequired[Dict[str, str]],
        "retryPolicyConfiguration": NotRequired[RetryPolicyConfigurationTypeDef],
        "retryPolicyExecution": NotRequired[RetryPolicyExecutionTypeDef],
    },
)
ConfigurationOverridesUnionTypeDef = Union[
    ConfigurationOverridesTypeDef, ConfigurationOverridesOutputTypeDef
]

class JobTemplateDataOutputTypeDef(TypedDict):
    executionRoleArn: str
    releaseLabel: str
    jobDriver: JobDriverOutputTypeDef
    configurationOverrides: NotRequired[ParametricConfigurationOverridesOutputTypeDef]
    parameterConfiguration: NotRequired[Dict[str, TemplateParameterConfigurationTypeDef]]
    jobTags: NotRequired[Dict[str, str]]

class JobTemplateDataPaginatorTypeDef(TypedDict):
    executionRoleArn: str
    releaseLabel: str
    jobDriver: JobDriverOutputTypeDef
    configurationOverrides: NotRequired[ParametricConfigurationOverridesPaginatorTypeDef]
    parameterConfiguration: NotRequired[Dict[str, TemplateParameterConfigurationTypeDef]]
    jobTags: NotRequired[Dict[str, str]]

class JobTemplateDataTypeDef(TypedDict):
    executionRoleArn: str
    releaseLabel: str
    jobDriver: JobDriverTypeDef
    configurationOverrides: NotRequired[ParametricConfigurationOverridesTypeDef]
    parameterConfiguration: NotRequired[Mapping[str, TemplateParameterConfigurationTypeDef]]
    jobTags: NotRequired[Mapping[str, str]]

class DescribeVirtualClusterResponseTypeDef(TypedDict):
    virtualCluster: VirtualClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVirtualClustersResponseTypeDef(TypedDict):
    virtualClusters: List[VirtualClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SecurityConfigurationDataTypeDef(TypedDict):
    authorizationConfiguration: NotRequired[AuthorizationConfigurationTypeDef]

class DescribeManagedEndpointResponseTypeDef(TypedDict):
    endpoint: EndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListManagedEndpointsResponseTypeDef(TypedDict):
    endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeJobRunResponseTypeDef(TypedDict):
    jobRun: JobRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobRunsResponseTypeDef(TypedDict):
    jobRuns: List[JobRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListManagedEndpointsResponsePaginatorTypeDef(TypedDict):
    endpoints: List[EndpointPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListJobRunsResponsePaginatorTypeDef(TypedDict):
    jobRuns: List[JobRunPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

CreateManagedEndpointRequestTypeDef = TypedDict(
    "CreateManagedEndpointRequestTypeDef",
    {
        "name": str,
        "virtualClusterId": str,
        "type": str,
        "releaseLabel": str,
        "executionRoleArn": str,
        "clientToken": str,
        "certificateArn": NotRequired[str],
        "configurationOverrides": NotRequired[ConfigurationOverridesUnionTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)

class StartJobRunRequestTypeDef(TypedDict):
    virtualClusterId: str
    clientToken: str
    name: NotRequired[str]
    executionRoleArn: NotRequired[str]
    releaseLabel: NotRequired[str]
    jobDriver: NotRequired[JobDriverUnionTypeDef]
    configurationOverrides: NotRequired[ConfigurationOverridesUnionTypeDef]
    tags: NotRequired[Mapping[str, str]]
    jobTemplateId: NotRequired[str]
    jobTemplateParameters: NotRequired[Mapping[str, str]]
    retryPolicyConfiguration: NotRequired[RetryPolicyConfigurationTypeDef]

JobTemplateTypeDef = TypedDict(
    "JobTemplateTypeDef",
    {
        "jobTemplateData": JobTemplateDataOutputTypeDef,
        "name": NotRequired[str],
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "kmsKeyArn": NotRequired[str],
        "decryptionError": NotRequired[str],
    },
)
JobTemplatePaginatorTypeDef = TypedDict(
    "JobTemplatePaginatorTypeDef",
    {
        "jobTemplateData": JobTemplateDataPaginatorTypeDef,
        "name": NotRequired[str],
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "kmsKeyArn": NotRequired[str],
        "decryptionError": NotRequired[str],
    },
)
JobTemplateDataUnionTypeDef = Union[JobTemplateDataTypeDef, JobTemplateDataOutputTypeDef]

class CreateSecurityConfigurationRequestTypeDef(TypedDict):
    clientToken: str
    name: str
    securityConfigurationData: SecurityConfigurationDataTypeDef
    tags: NotRequired[Mapping[str, str]]

SecurityConfigurationTypeDef = TypedDict(
    "SecurityConfigurationTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "securityConfigurationData": NotRequired[SecurityConfigurationDataTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)

class DescribeJobTemplateResponseTypeDef(TypedDict):
    jobTemplate: JobTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobTemplatesResponseTypeDef(TypedDict):
    templates: List[JobTemplateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListJobTemplatesResponsePaginatorTypeDef(TypedDict):
    templates: List[JobTemplatePaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateJobTemplateRequestTypeDef(TypedDict):
    name: str
    clientToken: str
    jobTemplateData: JobTemplateDataUnionTypeDef
    tags: NotRequired[Mapping[str, str]]
    kmsKeyArn: NotRequired[str]

class DescribeSecurityConfigurationResponseTypeDef(TypedDict):
    securityConfiguration: SecurityConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSecurityConfigurationsResponseTypeDef(TypedDict):
    securityConfigurations: List[SecurityConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
