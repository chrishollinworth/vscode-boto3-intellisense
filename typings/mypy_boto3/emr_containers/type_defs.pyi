"""
Type annotations for emr-containers service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/type_defs.html)

Usage::

    ```python
    from mypy_boto3_emr_containers.type_defs import CancelJobRunRequestRequestTypeDef

    data: CancelJobRunRequestRequestTypeDef = {...}
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
    "CancelJobRunRequestRequestTypeDef",
    "CancelJobRunResponseTypeDef",
    "CloudWatchMonitoringConfigurationTypeDef",
    "ConfigurationOverridesTypeDef",
    "ConfigurationTypeDef",
    "ContainerInfoTypeDef",
    "ContainerProviderTypeDef",
    "CreateManagedEndpointRequestRequestTypeDef",
    "CreateManagedEndpointResponseTypeDef",
    "CreateVirtualClusterRequestRequestTypeDef",
    "CreateVirtualClusterResponseTypeDef",
    "DeleteManagedEndpointRequestRequestTypeDef",
    "DeleteManagedEndpointResponseTypeDef",
    "DeleteVirtualClusterRequestRequestTypeDef",
    "DeleteVirtualClusterResponseTypeDef",
    "DescribeJobRunRequestRequestTypeDef",
    "DescribeJobRunResponseTypeDef",
    "DescribeManagedEndpointRequestRequestTypeDef",
    "DescribeManagedEndpointResponseTypeDef",
    "DescribeVirtualClusterRequestRequestTypeDef",
    "DescribeVirtualClusterResponseTypeDef",
    "EksInfoTypeDef",
    "EndpointTypeDef",
    "JobDriverTypeDef",
    "JobRunTypeDef",
    "ListJobRunsRequestRequestTypeDef",
    "ListJobRunsResponseTypeDef",
    "ListManagedEndpointsRequestRequestTypeDef",
    "ListManagedEndpointsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVirtualClustersRequestRequestTypeDef",
    "ListVirtualClustersResponseTypeDef",
    "MonitoringConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "S3MonitoringConfigurationTypeDef",
    "SparkSubmitJobDriverTypeDef",
    "StartJobRunRequestRequestTypeDef",
    "StartJobRunResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "VirtualClusterTypeDef",
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

_RequiredCreateManagedEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredCreateManagedEndpointRequestRequestTypeDef",
    {
        "name": str,
        "virtualClusterId": str,
        "type": str,
        "releaseLabel": str,
        "executionRoleArn": str,
        "certificateArn": str,
        "clientToken": str,
    },
)
_OptionalCreateManagedEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalCreateManagedEndpointRequestRequestTypeDef",
    {
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

JobDriverTypeDef = TypedDict(
    "JobDriverTypeDef",
    {
        "sparkSubmitJobDriver": "SparkSubmitJobDriverTypeDef",
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

S3MonitoringConfigurationTypeDef = TypedDict(
    "S3MonitoringConfigurationTypeDef",
    {
        "logUri": str,
    },
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
        "executionRoleArn": str,
        "releaseLabel": str,
        "jobDriver": "JobDriverTypeDef",
    },
)
_OptionalStartJobRunRequestRequestTypeDef = TypedDict(
    "_OptionalStartJobRunRequestRequestTypeDef",
    {
        "name": str,
        "configurationOverrides": "ConfigurationOverridesTypeDef",
        "tags": Dict[str, str],
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

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
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
    },
    total=False,
)
