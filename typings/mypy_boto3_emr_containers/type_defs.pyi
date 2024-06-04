"""
Type annotations for emr-containers service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/type_defs.html)

Usage::

    ```python
    from mypy_boto3_emr_containers.type_defs import AuthorizationConfigurationTypeDef

    data: AuthorizationConfigurationTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    EndpointStateType,
    FailureReasonType,
    JobRunStateType,
    PersistentAppUIType,
    TemplateParameterDataTypeType,
    VirtualClusterStateType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AuthorizationConfigurationTypeDef",
    "CancelJobRunRequestRequestTypeDef",
    "CancelJobRunResponseTypeDef",
    "CertificateTypeDef",
    "CloudWatchMonitoringConfigurationTypeDef",
    "ConfigurationOverridesTypeDef",
    "ConfigurationTypeDef",
    "ContainerInfoTypeDef",
    "ContainerLogRotationConfigurationTypeDef",
    "ContainerProviderTypeDef",
    "CreateJobTemplateRequestRequestTypeDef",
    "CreateJobTemplateResponseTypeDef",
    "CreateManagedEndpointRequestRequestTypeDef",
    "CreateManagedEndpointResponseTypeDef",
    "CreateSecurityConfigurationRequestRequestTypeDef",
    "CreateSecurityConfigurationResponseTypeDef",
    "CreateVirtualClusterRequestRequestTypeDef",
    "CreateVirtualClusterResponseTypeDef",
    "CredentialsTypeDef",
    "DeleteJobTemplateRequestRequestTypeDef",
    "DeleteJobTemplateResponseTypeDef",
    "DeleteManagedEndpointRequestRequestTypeDef",
    "DeleteManagedEndpointResponseTypeDef",
    "DeleteVirtualClusterRequestRequestTypeDef",
    "DeleteVirtualClusterResponseTypeDef",
    "DescribeJobRunRequestRequestTypeDef",
    "DescribeJobRunResponseTypeDef",
    "DescribeJobTemplateRequestRequestTypeDef",
    "DescribeJobTemplateResponseTypeDef",
    "DescribeManagedEndpointRequestRequestTypeDef",
    "DescribeManagedEndpointResponseTypeDef",
    "DescribeSecurityConfigurationRequestRequestTypeDef",
    "DescribeSecurityConfigurationResponseTypeDef",
    "DescribeVirtualClusterRequestRequestTypeDef",
    "DescribeVirtualClusterResponseTypeDef",
    "EksInfoTypeDef",
    "EncryptionConfigurationTypeDef",
    "EndpointTypeDef",
    "GetManagedEndpointSessionCredentialsRequestRequestTypeDef",
    "GetManagedEndpointSessionCredentialsResponseTypeDef",
    "InTransitEncryptionConfigurationTypeDef",
    "JobDriverTypeDef",
    "JobRunTypeDef",
    "JobTemplateDataTypeDef",
    "JobTemplateTypeDef",
    "LakeFormationConfigurationTypeDef",
    "ListJobRunsRequestRequestTypeDef",
    "ListJobRunsResponseTypeDef",
    "ListJobTemplatesRequestRequestTypeDef",
    "ListJobTemplatesResponseTypeDef",
    "ListManagedEndpointsRequestRequestTypeDef",
    "ListManagedEndpointsResponseTypeDef",
    "ListSecurityConfigurationsRequestRequestTypeDef",
    "ListSecurityConfigurationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVirtualClustersRequestRequestTypeDef",
    "ListVirtualClustersResponseTypeDef",
    "MonitoringConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ParametricCloudWatchMonitoringConfigurationTypeDef",
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
    "SparkSubmitJobDriverTypeDef",
    "StartJobRunRequestRequestTypeDef",
    "StartJobRunResponseTypeDef",
    "TLSCertificateConfigurationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TemplateParameterConfigurationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "VirtualClusterTypeDef",
)

AuthorizationConfigurationTypeDef = TypedDict(
    "AuthorizationConfigurationTypeDef",
    {
        "lakeFormationConfiguration": "LakeFormationConfigurationTypeDef",
        "encryptionConfiguration": "EncryptionConfigurationTypeDef",
    },
    total=False,
)

CancelJobRunRequestRequestTypeDef = TypedDict(
    "CancelJobRunRequestRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
    },
)

CancelJobRunResponseTypeDef = TypedDict(
    "CancelJobRunResponseTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "certificateArn": str,
        "certificateData": str,
    },
    total=False,
)

_RequiredCloudWatchMonitoringConfigurationTypeDef = TypedDict(
    "_RequiredCloudWatchMonitoringConfigurationTypeDef",
    {
        "logGroupName": str,
    },
)
_OptionalCloudWatchMonitoringConfigurationTypeDef = TypedDict(
    "_OptionalCloudWatchMonitoringConfigurationTypeDef",
    {
        "logStreamNamePrefix": str,
    },
    total=False,
)

class CloudWatchMonitoringConfigurationTypeDef(
    _RequiredCloudWatchMonitoringConfigurationTypeDef,
    _OptionalCloudWatchMonitoringConfigurationTypeDef,
):
    pass

ConfigurationOverridesTypeDef = TypedDict(
    "ConfigurationOverridesTypeDef",
    {
        "applicationConfiguration": List["ConfigurationTypeDef"],
        "monitoringConfiguration": "MonitoringConfigurationTypeDef",
    },
    total=False,
)

_RequiredConfigurationTypeDef = TypedDict(
    "_RequiredConfigurationTypeDef",
    {
        "classification": str,
    },
)
_OptionalConfigurationTypeDef = TypedDict(
    "_OptionalConfigurationTypeDef",
    {
        "properties": Dict[str, str],
        "configurations": List[Dict[str, Any]],
    },
    total=False,
)

class ConfigurationTypeDef(_RequiredConfigurationTypeDef, _OptionalConfigurationTypeDef):
    pass

ContainerInfoTypeDef = TypedDict(
    "ContainerInfoTypeDef",
    {
        "eksInfo": "EksInfoTypeDef",
    },
    total=False,
)

ContainerLogRotationConfigurationTypeDef = TypedDict(
    "ContainerLogRotationConfigurationTypeDef",
    {
        "rotationSize": str,
        "maxFilesToKeep": int,
    },
)

_RequiredContainerProviderTypeDef = TypedDict(
    "_RequiredContainerProviderTypeDef",
    {
        "type": Literal["EKS"],
        "id": str,
    },
)
_OptionalContainerProviderTypeDef = TypedDict(
    "_OptionalContainerProviderTypeDef",
    {
        "info": "ContainerInfoTypeDef",
    },
    total=False,
)

class ContainerProviderTypeDef(
    _RequiredContainerProviderTypeDef, _OptionalContainerProviderTypeDef
):
    pass

_RequiredCreateJobTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateJobTemplateRequestRequestTypeDef",
    {
        "name": str,
        "clientToken": str,
        "jobTemplateData": "JobTemplateDataTypeDef",
    },
)
_OptionalCreateJobTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateJobTemplateRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
        "kmsKeyArn": str,
    },
    total=False,
)

class CreateJobTemplateRequestRequestTypeDef(
    _RequiredCreateJobTemplateRequestRequestTypeDef, _OptionalCreateJobTemplateRequestRequestTypeDef
):
    pass

CreateJobTemplateResponseTypeDef = TypedDict(
    "CreateJobTemplateResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateManagedEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredCreateManagedEndpointRequestRequestTypeDef",
    {
        "name": str,
        "virtualClusterId": str,
        "type": str,
        "releaseLabel": str,
        "executionRoleArn": str,
        "clientToken": str,
    },
)
_OptionalCreateManagedEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalCreateManagedEndpointRequestRequestTypeDef",
    {
        "certificateArn": str,
        "configurationOverrides": "ConfigurationOverridesTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateManagedEndpointRequestRequestTypeDef(
    _RequiredCreateManagedEndpointRequestRequestTypeDef,
    _OptionalCreateManagedEndpointRequestRequestTypeDef,
):
    pass

CreateManagedEndpointResponseTypeDef = TypedDict(
    "CreateManagedEndpointResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "virtualClusterId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSecurityConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSecurityConfigurationRequestRequestTypeDef",
    {
        "clientToken": str,
        "name": str,
        "securityConfigurationData": "SecurityConfigurationDataTypeDef",
    },
)
_OptionalCreateSecurityConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSecurityConfigurationRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateSecurityConfigurationRequestRequestTypeDef(
    _RequiredCreateSecurityConfigurationRequestRequestTypeDef,
    _OptionalCreateSecurityConfigurationRequestRequestTypeDef,
):
    pass

CreateSecurityConfigurationResponseTypeDef = TypedDict(
    "CreateSecurityConfigurationResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVirtualClusterRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVirtualClusterRequestRequestTypeDef",
    {
        "name": str,
        "containerProvider": "ContainerProviderTypeDef",
        "clientToken": str,
    },
)
_OptionalCreateVirtualClusterRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVirtualClusterRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
        "securityConfigurationId": str,
    },
    total=False,
)

class CreateVirtualClusterRequestRequestTypeDef(
    _RequiredCreateVirtualClusterRequestRequestTypeDef,
    _OptionalCreateVirtualClusterRequestRequestTypeDef,
):
    pass

CreateVirtualClusterResponseTypeDef = TypedDict(
    "CreateVirtualClusterResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "token": str,
    },
    total=False,
)

DeleteJobTemplateRequestRequestTypeDef = TypedDict(
    "DeleteJobTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteJobTemplateResponseTypeDef = TypedDict(
    "DeleteJobTemplateResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteManagedEndpointRequestRequestTypeDef = TypedDict(
    "DeleteManagedEndpointRequestRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
    },
)

DeleteManagedEndpointResponseTypeDef = TypedDict(
    "DeleteManagedEndpointResponseTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVirtualClusterRequestRequestTypeDef = TypedDict(
    "DeleteVirtualClusterRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteVirtualClusterResponseTypeDef = TypedDict(
    "DeleteVirtualClusterResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobRunRequestRequestTypeDef = TypedDict(
    "DescribeJobRunRequestRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
    },
)

DescribeJobRunResponseTypeDef = TypedDict(
    "DescribeJobRunResponseTypeDef",
    {
        "jobRun": "JobRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobTemplateRequestRequestTypeDef = TypedDict(
    "DescribeJobTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)

DescribeJobTemplateResponseTypeDef = TypedDict(
    "DescribeJobTemplateResponseTypeDef",
    {
        "jobTemplate": "JobTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeManagedEndpointRequestRequestTypeDef = TypedDict(
    "DescribeManagedEndpointRequestRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
    },
)

DescribeManagedEndpointResponseTypeDef = TypedDict(
    "DescribeManagedEndpointResponseTypeDef",
    {
        "endpoint": "EndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSecurityConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeSecurityConfigurationRequestRequestTypeDef",
    {
        "id": str,
    },
)

DescribeSecurityConfigurationResponseTypeDef = TypedDict(
    "DescribeSecurityConfigurationResponseTypeDef",
    {
        "securityConfiguration": "SecurityConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVirtualClusterRequestRequestTypeDef = TypedDict(
    "DescribeVirtualClusterRequestRequestTypeDef",
    {
        "id": str,
    },
)

DescribeVirtualClusterResponseTypeDef = TypedDict(
    "DescribeVirtualClusterResponseTypeDef",
    {
        "virtualCluster": "VirtualClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EksInfoTypeDef = TypedDict(
    "EksInfoTypeDef",
    {
        "namespace": str,
    },
    total=False,
)

EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "inTransitEncryptionConfiguration": "InTransitEncryptionConfigurationTypeDef",
    },
    total=False,
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "virtualClusterId": str,
        "type": str,
        "state": EndpointStateType,
        "releaseLabel": str,
        "executionRoleArn": str,
        "certificateArn": str,
        "certificateAuthority": "CertificateTypeDef",
        "configurationOverrides": "ConfigurationOverridesTypeDef",
        "serverUrl": str,
        "createdAt": datetime,
        "securityGroup": str,
        "subnetIds": List[str],
        "stateDetails": str,
        "failureReason": FailureReasonType,
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredGetManagedEndpointSessionCredentialsRequestRequestTypeDef = TypedDict(
    "_RequiredGetManagedEndpointSessionCredentialsRequestRequestTypeDef",
    {
        "endpointIdentifier": str,
        "virtualClusterIdentifier": str,
        "executionRoleArn": str,
        "credentialType": str,
    },
)
_OptionalGetManagedEndpointSessionCredentialsRequestRequestTypeDef = TypedDict(
    "_OptionalGetManagedEndpointSessionCredentialsRequestRequestTypeDef",
    {
        "durationInSeconds": int,
        "logContext": str,
        "clientToken": str,
    },
    total=False,
)

class GetManagedEndpointSessionCredentialsRequestRequestTypeDef(
    _RequiredGetManagedEndpointSessionCredentialsRequestRequestTypeDef,
    _OptionalGetManagedEndpointSessionCredentialsRequestRequestTypeDef,
):
    pass

GetManagedEndpointSessionCredentialsResponseTypeDef = TypedDict(
    "GetManagedEndpointSessionCredentialsResponseTypeDef",
    {
        "id": str,
        "credentials": "CredentialsTypeDef",
        "expiresAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InTransitEncryptionConfigurationTypeDef = TypedDict(
    "InTransitEncryptionConfigurationTypeDef",
    {
        "tlsCertificateConfiguration": "TLSCertificateConfigurationTypeDef",
    },
    total=False,
)

JobDriverTypeDef = TypedDict(
    "JobDriverTypeDef",
    {
        "sparkSubmitJobDriver": "SparkSubmitJobDriverTypeDef",
        "sparkSqlJobDriver": "SparkSqlJobDriverTypeDef",
    },
    total=False,
)

JobRunTypeDef = TypedDict(
    "JobRunTypeDef",
    {
        "id": str,
        "name": str,
        "virtualClusterId": str,
        "arn": str,
        "state": JobRunStateType,
        "clientToken": str,
        "executionRoleArn": str,
        "releaseLabel": str,
        "configurationOverrides": "ConfigurationOverridesTypeDef",
        "jobDriver": "JobDriverTypeDef",
        "createdAt": datetime,
        "createdBy": str,
        "finishedAt": datetime,
        "stateDetails": str,
        "failureReason": FailureReasonType,
        "tags": Dict[str, str],
        "retryPolicyConfiguration": "RetryPolicyConfigurationTypeDef",
        "retryPolicyExecution": "RetryPolicyExecutionTypeDef",
    },
    total=False,
)

_RequiredJobTemplateDataTypeDef = TypedDict(
    "_RequiredJobTemplateDataTypeDef",
    {
        "executionRoleArn": str,
        "releaseLabel": str,
        "jobDriver": "JobDriverTypeDef",
    },
)
_OptionalJobTemplateDataTypeDef = TypedDict(
    "_OptionalJobTemplateDataTypeDef",
    {
        "configurationOverrides": "ParametricConfigurationOverridesTypeDef",
        "parameterConfiguration": Dict[str, "TemplateParameterConfigurationTypeDef"],
        "jobTags": Dict[str, str],
    },
    total=False,
)

class JobTemplateDataTypeDef(_RequiredJobTemplateDataTypeDef, _OptionalJobTemplateDataTypeDef):
    pass

_RequiredJobTemplateTypeDef = TypedDict(
    "_RequiredJobTemplateTypeDef",
    {
        "jobTemplateData": "JobTemplateDataTypeDef",
    },
)
_OptionalJobTemplateTypeDef = TypedDict(
    "_OptionalJobTemplateTypeDef",
    {
        "name": str,
        "id": str,
        "arn": str,
        "createdAt": datetime,
        "createdBy": str,
        "tags": Dict[str, str],
        "kmsKeyArn": str,
        "decryptionError": str,
    },
    total=False,
)

class JobTemplateTypeDef(_RequiredJobTemplateTypeDef, _OptionalJobTemplateTypeDef):
    pass

LakeFormationConfigurationTypeDef = TypedDict(
    "LakeFormationConfigurationTypeDef",
    {
        "authorizedSessionTagValue": str,
        "secureNamespaceInfo": "SecureNamespaceInfoTypeDef",
        "queryEngineRoleArn": str,
    },
    total=False,
)

_RequiredListJobRunsRequestRequestTypeDef = TypedDict(
    "_RequiredListJobRunsRequestRequestTypeDef",
    {
        "virtualClusterId": str,
    },
)
_OptionalListJobRunsRequestRequestTypeDef = TypedDict(
    "_OptionalListJobRunsRequestRequestTypeDef",
    {
        "createdBefore": Union[datetime, str],
        "createdAfter": Union[datetime, str],
        "name": str,
        "states": List[JobRunStateType],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListJobRunsRequestRequestTypeDef(
    _RequiredListJobRunsRequestRequestTypeDef, _OptionalListJobRunsRequestRequestTypeDef
):
    pass

ListJobRunsResponseTypeDef = TypedDict(
    "ListJobRunsResponseTypeDef",
    {
        "jobRuns": List["JobRunTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobTemplatesRequestRequestTypeDef = TypedDict(
    "ListJobTemplatesRequestRequestTypeDef",
    {
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListJobTemplatesResponseTypeDef = TypedDict(
    "ListJobTemplatesResponseTypeDef",
    {
        "templates": List["JobTemplateTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListManagedEndpointsRequestRequestTypeDef = TypedDict(
    "_RequiredListManagedEndpointsRequestRequestTypeDef",
    {
        "virtualClusterId": str,
    },
)
_OptionalListManagedEndpointsRequestRequestTypeDef = TypedDict(
    "_OptionalListManagedEndpointsRequestRequestTypeDef",
    {
        "createdBefore": Union[datetime, str],
        "createdAfter": Union[datetime, str],
        "types": List[str],
        "states": List[EndpointStateType],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListManagedEndpointsRequestRequestTypeDef(
    _RequiredListManagedEndpointsRequestRequestTypeDef,
    _OptionalListManagedEndpointsRequestRequestTypeDef,
):
    pass

ListManagedEndpointsResponseTypeDef = TypedDict(
    "ListManagedEndpointsResponseTypeDef",
    {
        "endpoints": List["EndpointTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSecurityConfigurationsRequestRequestTypeDef = TypedDict(
    "ListSecurityConfigurationsRequestRequestTypeDef",
    {
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListSecurityConfigurationsResponseTypeDef = TypedDict(
    "ListSecurityConfigurationsResponseTypeDef",
    {
        "securityConfigurations": List["SecurityConfigurationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVirtualClustersRequestRequestTypeDef = TypedDict(
    "ListVirtualClustersRequestRequestTypeDef",
    {
        "containerProviderId": str,
        "containerProviderType": Literal["EKS"],
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
        "states": List[VirtualClusterStateType],
        "maxResults": int,
        "nextToken": str,
        "eksAccessEntryIntegrated": bool,
    },
    total=False,
)

ListVirtualClustersResponseTypeDef = TypedDict(
    "ListVirtualClustersResponseTypeDef",
    {
        "virtualClusters": List["VirtualClusterTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MonitoringConfigurationTypeDef = TypedDict(
    "MonitoringConfigurationTypeDef",
    {
        "persistentAppUI": PersistentAppUIType,
        "cloudWatchMonitoringConfiguration": "CloudWatchMonitoringConfigurationTypeDef",
        "s3MonitoringConfiguration": "S3MonitoringConfigurationTypeDef",
        "containerLogRotationConfiguration": "ContainerLogRotationConfigurationTypeDef",
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ParametricCloudWatchMonitoringConfigurationTypeDef = TypedDict(
    "ParametricCloudWatchMonitoringConfigurationTypeDef",
    {
        "logGroupName": str,
        "logStreamNamePrefix": str,
    },
    total=False,
)

ParametricConfigurationOverridesTypeDef = TypedDict(
    "ParametricConfigurationOverridesTypeDef",
    {
        "applicationConfiguration": List["ConfigurationTypeDef"],
        "monitoringConfiguration": "ParametricMonitoringConfigurationTypeDef",
    },
    total=False,
)

ParametricMonitoringConfigurationTypeDef = TypedDict(
    "ParametricMonitoringConfigurationTypeDef",
    {
        "persistentAppUI": str,
        "cloudWatchMonitoringConfiguration": "ParametricCloudWatchMonitoringConfigurationTypeDef",
        "s3MonitoringConfiguration": "ParametricS3MonitoringConfigurationTypeDef",
    },
    total=False,
)

ParametricS3MonitoringConfigurationTypeDef = TypedDict(
    "ParametricS3MonitoringConfigurationTypeDef",
    {
        "logUri": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

RetryPolicyConfigurationTypeDef = TypedDict(
    "RetryPolicyConfigurationTypeDef",
    {
        "maxAttempts": int,
    },
)

RetryPolicyExecutionTypeDef = TypedDict(
    "RetryPolicyExecutionTypeDef",
    {
        "currentAttemptCount": int,
    },
)

S3MonitoringConfigurationTypeDef = TypedDict(
    "S3MonitoringConfigurationTypeDef",
    {
        "logUri": str,
    },
)

SecureNamespaceInfoTypeDef = TypedDict(
    "SecureNamespaceInfoTypeDef",
    {
        "clusterId": str,
        "namespace": str,
    },
    total=False,
)

SecurityConfigurationDataTypeDef = TypedDict(
    "SecurityConfigurationDataTypeDef",
    {
        "authorizationConfiguration": "AuthorizationConfigurationTypeDef",
    },
    total=False,
)

SecurityConfigurationTypeDef = TypedDict(
    "SecurityConfigurationTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "createdBy": str,
        "securityConfigurationData": "SecurityConfigurationDataTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

SparkSqlJobDriverTypeDef = TypedDict(
    "SparkSqlJobDriverTypeDef",
    {
        "entryPoint": str,
        "sparkSqlParameters": str,
    },
    total=False,
)

_RequiredSparkSubmitJobDriverTypeDef = TypedDict(
    "_RequiredSparkSubmitJobDriverTypeDef",
    {
        "entryPoint": str,
    },
)
_OptionalSparkSubmitJobDriverTypeDef = TypedDict(
    "_OptionalSparkSubmitJobDriverTypeDef",
    {
        "entryPointArguments": List[str],
        "sparkSubmitParameters": str,
    },
    total=False,
)

class SparkSubmitJobDriverTypeDef(
    _RequiredSparkSubmitJobDriverTypeDef, _OptionalSparkSubmitJobDriverTypeDef
):
    pass

_RequiredStartJobRunRequestRequestTypeDef = TypedDict(
    "_RequiredStartJobRunRequestRequestTypeDef",
    {
        "virtualClusterId": str,
        "clientToken": str,
    },
)
_OptionalStartJobRunRequestRequestTypeDef = TypedDict(
    "_OptionalStartJobRunRequestRequestTypeDef",
    {
        "name": str,
        "executionRoleArn": str,
        "releaseLabel": str,
        "jobDriver": "JobDriverTypeDef",
        "configurationOverrides": "ConfigurationOverridesTypeDef",
        "tags": Dict[str, str],
        "jobTemplateId": str,
        "jobTemplateParameters": Dict[str, str],
        "retryPolicyConfiguration": "RetryPolicyConfigurationTypeDef",
    },
    total=False,
)

class StartJobRunRequestRequestTypeDef(
    _RequiredStartJobRunRequestRequestTypeDef, _OptionalStartJobRunRequestRequestTypeDef
):
    pass

StartJobRunResponseTypeDef = TypedDict(
    "StartJobRunResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "virtualClusterId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TLSCertificateConfigurationTypeDef = TypedDict(
    "TLSCertificateConfigurationTypeDef",
    {
        "certificateProviderType": Literal["PEM"],
        "publicCertificateSecretArn": str,
        "privateCertificateSecretArn": str,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TemplateParameterConfigurationTypeDef = TypedDict(
    "TemplateParameterConfigurationTypeDef",
    {
        "type": TemplateParameterDataTypeType,
        "defaultValue": str,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

VirtualClusterTypeDef = TypedDict(
    "VirtualClusterTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "state": VirtualClusterStateType,
        "containerProvider": "ContainerProviderTypeDef",
        "createdAt": datetime,
        "tags": Dict[str, str],
        "securityConfigurationId": str,
    },
    total=False,
)
