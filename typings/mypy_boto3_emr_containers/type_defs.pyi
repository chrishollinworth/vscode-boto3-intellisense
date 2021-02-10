"""
Main interface for emr-containers service type definitions.

Usage::

    ```python
    from mypy_boto3_emr_containers.type_defs import CloudWatchMonitoringConfigurationTypeDef

    data: CloudWatchMonitoringConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CloudWatchMonitoringConfigurationTypeDef",
    "ConfigurationOverridesTypeDef",
    "ContainerInfoTypeDef",
    "ContainerProviderTypeDef",
    "EksInfoTypeDef",
    "EndpointTypeDef",
    "JobDriverTypeDef",
    "JobRunTypeDef",
    "MonitoringConfigurationTypeDef",
    "S3MonitoringConfigurationTypeDef",
    "SparkSubmitJobDriverTypeDef",
    "VirtualClusterTypeDef",
    "CancelJobRunResponseTypeDef",
    "CreateManagedEndpointResponseTypeDef",
    "CreateVirtualClusterResponseTypeDef",
    "DeleteManagedEndpointResponseTypeDef",
    "DeleteVirtualClusterResponseTypeDef",
    "DescribeJobRunResponseTypeDef",
    "DescribeManagedEndpointResponseTypeDef",
    "DescribeVirtualClusterResponseTypeDef",
    "ConfigurationTypeDef",
    "ListJobRunsResponseTypeDef",
    "ListManagedEndpointsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVirtualClustersResponseTypeDef",
    "PaginatorConfigTypeDef",
    "StartJobRunResponseTypeDef",
)

_RequiredCloudWatchMonitoringConfigurationTypeDef = TypedDict(
    "_RequiredCloudWatchMonitoringConfigurationTypeDef", {"logGroupName": str}
)
_OptionalCloudWatchMonitoringConfigurationTypeDef = TypedDict(
    "_OptionalCloudWatchMonitoringConfigurationTypeDef", {"logStreamNamePrefix": str}, total=False
)


class CloudWatchMonitoringConfigurationTypeDef(
    _RequiredCloudWatchMonitoringConfigurationTypeDef,
    _OptionalCloudWatchMonitoringConfigurationTypeDef,
):
    pass


ConfigurationOverridesTypeDef = TypedDict(
    "ConfigurationOverridesTypeDef",
    {
        "applicationConfiguration": List[Dict[str, Any]],
        "monitoringConfiguration": "MonitoringConfigurationTypeDef",
    },
    total=False,
)

ContainerInfoTypeDef = TypedDict("ContainerInfoTypeDef", {"eksInfo": "EksInfoTypeDef"}, total=False)

_RequiredContainerProviderTypeDef = TypedDict(
    "_RequiredContainerProviderTypeDef", {"type": Literal["EKS"], "id": str}
)
_OptionalContainerProviderTypeDef = TypedDict(
    "_OptionalContainerProviderTypeDef", {"info": "ContainerInfoTypeDef"}, total=False
)


class ContainerProviderTypeDef(
    _RequiredContainerProviderTypeDef, _OptionalContainerProviderTypeDef
):
    pass


EksInfoTypeDef = TypedDict("EksInfoTypeDef", {"namespace": str}, total=False)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "virtualClusterId": str,
        "type": str,
        "state": Literal[
            "CREATING", "ACTIVE", "TERMINATING", "TERMINATED", "TERMINATED_WITH_ERRORS"
        ],
        "releaseLabel": str,
        "executionRoleArn": str,
        "certificateArn": str,
        "configurationOverrides": "ConfigurationOverridesTypeDef",
        "serverUrl": str,
        "createdAt": datetime,
        "securityGroup": str,
        "subnetIds": List[str],
        "tags": Dict[str, str],
    },
    total=False,
)

JobDriverTypeDef = TypedDict(
    "JobDriverTypeDef", {"sparkSubmitJobDriver": "SparkSubmitJobDriverTypeDef"}, total=False
)

JobRunTypeDef = TypedDict(
    "JobRunTypeDef",
    {
        "id": str,
        "name": str,
        "virtualClusterId": str,
        "arn": str,
        "state": Literal[
            "PENDING", "SUBMITTED", "RUNNING", "FAILED", "CANCELLED", "CANCEL_PENDING", "COMPLETED"
        ],
        "clientToken": str,
        "executionRoleArn": str,
        "releaseLabel": str,
        "configurationOverrides": "ConfigurationOverridesTypeDef",
        "jobDriver": "JobDriverTypeDef",
        "createdAt": datetime,
        "createdBy": str,
        "finishedAt": datetime,
        "stateDetails": str,
        "failureReason": Literal[
            "INTERNAL_ERROR", "USER_ERROR", "VALIDATION_ERROR", "CLUSTER_UNAVAILABLE"
        ],
        "tags": Dict[str, str],
    },
    total=False,
)

MonitoringConfigurationTypeDef = TypedDict(
    "MonitoringConfigurationTypeDef",
    {
        "persistentAppUI": Literal["ENABLED", "DISABLED"],
        "cloudWatchMonitoringConfiguration": "CloudWatchMonitoringConfigurationTypeDef",
        "s3MonitoringConfiguration": "S3MonitoringConfigurationTypeDef",
    },
    total=False,
)

S3MonitoringConfigurationTypeDef = TypedDict("S3MonitoringConfigurationTypeDef", {"logUri": str})

_RequiredSparkSubmitJobDriverTypeDef = TypedDict(
    "_RequiredSparkSubmitJobDriverTypeDef", {"entryPoint": str}
)
_OptionalSparkSubmitJobDriverTypeDef = TypedDict(
    "_OptionalSparkSubmitJobDriverTypeDef",
    {"entryPointArguments": List[str], "sparkSubmitParameters": str},
    total=False,
)


class SparkSubmitJobDriverTypeDef(
    _RequiredSparkSubmitJobDriverTypeDef, _OptionalSparkSubmitJobDriverTypeDef
):
    pass


VirtualClusterTypeDef = TypedDict(
    "VirtualClusterTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "state": Literal["RUNNING", "TERMINATING", "TERMINATED", "ARRESTED"],
        "containerProvider": "ContainerProviderTypeDef",
        "createdAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

CancelJobRunResponseTypeDef = TypedDict(
    "CancelJobRunResponseTypeDef", {"id": str, "virtualClusterId": str}, total=False
)

CreateManagedEndpointResponseTypeDef = TypedDict(
    "CreateManagedEndpointResponseTypeDef",
    {"id": str, "name": str, "arn": str, "virtualClusterId": str},
    total=False,
)

CreateVirtualClusterResponseTypeDef = TypedDict(
    "CreateVirtualClusterResponseTypeDef", {"id": str, "name": str, "arn": str}, total=False
)

DeleteManagedEndpointResponseTypeDef = TypedDict(
    "DeleteManagedEndpointResponseTypeDef", {"id": str, "virtualClusterId": str}, total=False
)

DeleteVirtualClusterResponseTypeDef = TypedDict(
    "DeleteVirtualClusterResponseTypeDef", {"id": str}, total=False
)

DescribeJobRunResponseTypeDef = TypedDict(
    "DescribeJobRunResponseTypeDef", {"jobRun": "JobRunTypeDef"}, total=False
)

DescribeManagedEndpointResponseTypeDef = TypedDict(
    "DescribeManagedEndpointResponseTypeDef", {"endpoint": "EndpointTypeDef"}, total=False
)

DescribeVirtualClusterResponseTypeDef = TypedDict(
    "DescribeVirtualClusterResponseTypeDef",
    {"virtualCluster": "VirtualClusterTypeDef"},
    total=False,
)

_RequiredConfigurationTypeDef = TypedDict("_RequiredConfigurationTypeDef", {"classification": str})
_OptionalConfigurationTypeDef = TypedDict(
    "_OptionalConfigurationTypeDef",
    {"properties": Dict[str, str], "configurations": List[Dict[str, Any]]},
    total=False,
)


class ConfigurationTypeDef(_RequiredConfigurationTypeDef, _OptionalConfigurationTypeDef):
    pass


ListJobRunsResponseTypeDef = TypedDict(
    "ListJobRunsResponseTypeDef", {"jobRuns": List["JobRunTypeDef"], "nextToken": str}, total=False
)

ListManagedEndpointsResponseTypeDef = TypedDict(
    "ListManagedEndpointsResponseTypeDef",
    {"endpoints": List["EndpointTypeDef"], "nextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ListVirtualClustersResponseTypeDef = TypedDict(
    "ListVirtualClustersResponseTypeDef",
    {"virtualClusters": List["VirtualClusterTypeDef"], "nextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

StartJobRunResponseTypeDef = TypedDict(
    "StartJobRunResponseTypeDef",
    {"id": str, "name": str, "arn": str, "virtualClusterId": str},
    total=False,
)
