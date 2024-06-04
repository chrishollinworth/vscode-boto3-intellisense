"""
Type annotations for kafkaconnect service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kafkaconnect.type_defs import ApacheKafkaClusterDescriptionTypeDef

    data: ApacheKafkaClusterDescriptionTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ConnectorStateType,
    CustomPluginContentTypeType,
    CustomPluginStateType,
    KafkaClusterClientAuthenticationTypeType,
    KafkaClusterEncryptionInTransitTypeType,
    WorkerConfigurationStateType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ApacheKafkaClusterDescriptionTypeDef",
    "ApacheKafkaClusterTypeDef",
    "AutoScalingDescriptionTypeDef",
    "AutoScalingTypeDef",
    "AutoScalingUpdateTypeDef",
    "CapacityDescriptionTypeDef",
    "CapacityTypeDef",
    "CapacityUpdateTypeDef",
    "CloudWatchLogsLogDeliveryDescriptionTypeDef",
    "CloudWatchLogsLogDeliveryTypeDef",
    "ConnectorSummaryTypeDef",
    "CreateConnectorRequestRequestTypeDef",
    "CreateConnectorResponseTypeDef",
    "CreateCustomPluginRequestRequestTypeDef",
    "CreateCustomPluginResponseTypeDef",
    "CreateWorkerConfigurationRequestRequestTypeDef",
    "CreateWorkerConfigurationResponseTypeDef",
    "CustomPluginDescriptionTypeDef",
    "CustomPluginFileDescriptionTypeDef",
    "CustomPluginLocationDescriptionTypeDef",
    "CustomPluginLocationTypeDef",
    "CustomPluginRevisionSummaryTypeDef",
    "CustomPluginSummaryTypeDef",
    "CustomPluginTypeDef",
    "DeleteConnectorRequestRequestTypeDef",
    "DeleteConnectorResponseTypeDef",
    "DeleteCustomPluginRequestRequestTypeDef",
    "DeleteCustomPluginResponseTypeDef",
    "DeleteWorkerConfigurationRequestRequestTypeDef",
    "DeleteWorkerConfigurationResponseTypeDef",
    "DescribeConnectorRequestRequestTypeDef",
    "DescribeConnectorResponseTypeDef",
    "DescribeCustomPluginRequestRequestTypeDef",
    "DescribeCustomPluginResponseTypeDef",
    "DescribeWorkerConfigurationRequestRequestTypeDef",
    "DescribeWorkerConfigurationResponseTypeDef",
    "FirehoseLogDeliveryDescriptionTypeDef",
    "FirehoseLogDeliveryTypeDef",
    "KafkaClusterClientAuthenticationDescriptionTypeDef",
    "KafkaClusterClientAuthenticationTypeDef",
    "KafkaClusterDescriptionTypeDef",
    "KafkaClusterEncryptionInTransitDescriptionTypeDef",
    "KafkaClusterEncryptionInTransitTypeDef",
    "KafkaClusterTypeDef",
    "ListConnectorsRequestRequestTypeDef",
    "ListConnectorsResponseTypeDef",
    "ListCustomPluginsRequestRequestTypeDef",
    "ListCustomPluginsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWorkerConfigurationsRequestRequestTypeDef",
    "ListWorkerConfigurationsResponseTypeDef",
    "LogDeliveryDescriptionTypeDef",
    "LogDeliveryTypeDef",
    "PaginatorConfigTypeDef",
    "PluginDescriptionTypeDef",
    "PluginTypeDef",
    "ProvisionedCapacityDescriptionTypeDef",
    "ProvisionedCapacityTypeDef",
    "ProvisionedCapacityUpdateTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationDescriptionTypeDef",
    "S3LocationTypeDef",
    "S3LogDeliveryDescriptionTypeDef",
    "S3LogDeliveryTypeDef",
    "ScaleInPolicyDescriptionTypeDef",
    "ScaleInPolicyTypeDef",
    "ScaleInPolicyUpdateTypeDef",
    "ScaleOutPolicyDescriptionTypeDef",
    "ScaleOutPolicyTypeDef",
    "ScaleOutPolicyUpdateTypeDef",
    "StateDescriptionTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateConnectorRequestRequestTypeDef",
    "UpdateConnectorResponseTypeDef",
    "VpcDescriptionTypeDef",
    "VpcTypeDef",
    "WorkerConfigurationDescriptionTypeDef",
    "WorkerConfigurationRevisionDescriptionTypeDef",
    "WorkerConfigurationRevisionSummaryTypeDef",
    "WorkerConfigurationSummaryTypeDef",
    "WorkerConfigurationTypeDef",
    "WorkerLogDeliveryDescriptionTypeDef",
    "WorkerLogDeliveryTypeDef",
)

ApacheKafkaClusterDescriptionTypeDef = TypedDict(
    "ApacheKafkaClusterDescriptionTypeDef",
    {
        "bootstrapServers": str,
        "vpc": "VpcDescriptionTypeDef",
    },
    total=False,
)

ApacheKafkaClusterTypeDef = TypedDict(
    "ApacheKafkaClusterTypeDef",
    {
        "bootstrapServers": str,
        "vpc": "VpcTypeDef",
    },
)

AutoScalingDescriptionTypeDef = TypedDict(
    "AutoScalingDescriptionTypeDef",
    {
        "maxWorkerCount": int,
        "mcuCount": int,
        "minWorkerCount": int,
        "scaleInPolicy": "ScaleInPolicyDescriptionTypeDef",
        "scaleOutPolicy": "ScaleOutPolicyDescriptionTypeDef",
    },
    total=False,
)

_RequiredAutoScalingTypeDef = TypedDict(
    "_RequiredAutoScalingTypeDef",
    {
        "maxWorkerCount": int,
        "mcuCount": int,
        "minWorkerCount": int,
    },
)
_OptionalAutoScalingTypeDef = TypedDict(
    "_OptionalAutoScalingTypeDef",
    {
        "scaleInPolicy": "ScaleInPolicyTypeDef",
        "scaleOutPolicy": "ScaleOutPolicyTypeDef",
    },
    total=False,
)

class AutoScalingTypeDef(_RequiredAutoScalingTypeDef, _OptionalAutoScalingTypeDef):
    pass

AutoScalingUpdateTypeDef = TypedDict(
    "AutoScalingUpdateTypeDef",
    {
        "maxWorkerCount": int,
        "mcuCount": int,
        "minWorkerCount": int,
        "scaleInPolicy": "ScaleInPolicyUpdateTypeDef",
        "scaleOutPolicy": "ScaleOutPolicyUpdateTypeDef",
    },
)

CapacityDescriptionTypeDef = TypedDict(
    "CapacityDescriptionTypeDef",
    {
        "autoScaling": "AutoScalingDescriptionTypeDef",
        "provisionedCapacity": "ProvisionedCapacityDescriptionTypeDef",
    },
    total=False,
)

CapacityTypeDef = TypedDict(
    "CapacityTypeDef",
    {
        "autoScaling": "AutoScalingTypeDef",
        "provisionedCapacity": "ProvisionedCapacityTypeDef",
    },
    total=False,
)

CapacityUpdateTypeDef = TypedDict(
    "CapacityUpdateTypeDef",
    {
        "autoScaling": "AutoScalingUpdateTypeDef",
        "provisionedCapacity": "ProvisionedCapacityUpdateTypeDef",
    },
    total=False,
)

CloudWatchLogsLogDeliveryDescriptionTypeDef = TypedDict(
    "CloudWatchLogsLogDeliveryDescriptionTypeDef",
    {
        "enabled": bool,
        "logGroup": str,
    },
    total=False,
)

_RequiredCloudWatchLogsLogDeliveryTypeDef = TypedDict(
    "_RequiredCloudWatchLogsLogDeliveryTypeDef",
    {
        "enabled": bool,
    },
)
_OptionalCloudWatchLogsLogDeliveryTypeDef = TypedDict(
    "_OptionalCloudWatchLogsLogDeliveryTypeDef",
    {
        "logGroup": str,
    },
    total=False,
)

class CloudWatchLogsLogDeliveryTypeDef(
    _RequiredCloudWatchLogsLogDeliveryTypeDef, _OptionalCloudWatchLogsLogDeliveryTypeDef
):
    pass

ConnectorSummaryTypeDef = TypedDict(
    "ConnectorSummaryTypeDef",
    {
        "capacity": "CapacityDescriptionTypeDef",
        "connectorArn": str,
        "connectorDescription": str,
        "connectorName": str,
        "connectorState": ConnectorStateType,
        "creationTime": datetime,
        "currentVersion": str,
        "kafkaCluster": "KafkaClusterDescriptionTypeDef",
        "kafkaClusterClientAuthentication": "KafkaClusterClientAuthenticationDescriptionTypeDef",
        "kafkaClusterEncryptionInTransit": "KafkaClusterEncryptionInTransitDescriptionTypeDef",
        "kafkaConnectVersion": str,
        "logDelivery": "LogDeliveryDescriptionTypeDef",
        "plugins": List["PluginDescriptionTypeDef"],
        "serviceExecutionRoleArn": str,
        "workerConfiguration": "WorkerConfigurationDescriptionTypeDef",
    },
    total=False,
)

_RequiredCreateConnectorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConnectorRequestRequestTypeDef",
    {
        "capacity": "CapacityTypeDef",
        "connectorConfiguration": Dict[str, str],
        "connectorName": str,
        "kafkaCluster": "KafkaClusterTypeDef",
        "kafkaClusterClientAuthentication": "KafkaClusterClientAuthenticationTypeDef",
        "kafkaClusterEncryptionInTransit": "KafkaClusterEncryptionInTransitTypeDef",
        "kafkaConnectVersion": str,
        "plugins": List["PluginTypeDef"],
        "serviceExecutionRoleArn": str,
    },
)
_OptionalCreateConnectorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConnectorRequestRequestTypeDef",
    {
        "connectorDescription": str,
        "logDelivery": "LogDeliveryTypeDef",
        "tags": Dict[str, str],
        "workerConfiguration": "WorkerConfigurationTypeDef",
    },
    total=False,
)

class CreateConnectorRequestRequestTypeDef(
    _RequiredCreateConnectorRequestRequestTypeDef, _OptionalCreateConnectorRequestRequestTypeDef
):
    pass

CreateConnectorResponseTypeDef = TypedDict(
    "CreateConnectorResponseTypeDef",
    {
        "connectorArn": str,
        "connectorName": str,
        "connectorState": ConnectorStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCustomPluginRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCustomPluginRequestRequestTypeDef",
    {
        "contentType": CustomPluginContentTypeType,
        "location": "CustomPluginLocationTypeDef",
        "name": str,
    },
)
_OptionalCreateCustomPluginRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCustomPluginRequestRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateCustomPluginRequestRequestTypeDef(
    _RequiredCreateCustomPluginRequestRequestTypeDef,
    _OptionalCreateCustomPluginRequestRequestTypeDef,
):
    pass

CreateCustomPluginResponseTypeDef = TypedDict(
    "CreateCustomPluginResponseTypeDef",
    {
        "customPluginArn": str,
        "customPluginState": CustomPluginStateType,
        "name": str,
        "revision": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWorkerConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWorkerConfigurationRequestRequestTypeDef",
    {
        "name": str,
        "propertiesFileContent": str,
    },
)
_OptionalCreateWorkerConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWorkerConfigurationRequestRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateWorkerConfigurationRequestRequestTypeDef(
    _RequiredCreateWorkerConfigurationRequestRequestTypeDef,
    _OptionalCreateWorkerConfigurationRequestRequestTypeDef,
):
    pass

CreateWorkerConfigurationResponseTypeDef = TypedDict(
    "CreateWorkerConfigurationResponseTypeDef",
    {
        "creationTime": datetime,
        "latestRevision": "WorkerConfigurationRevisionSummaryTypeDef",
        "name": str,
        "workerConfigurationArn": str,
        "workerConfigurationState": WorkerConfigurationStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomPluginDescriptionTypeDef = TypedDict(
    "CustomPluginDescriptionTypeDef",
    {
        "customPluginArn": str,
        "revision": int,
    },
    total=False,
)

CustomPluginFileDescriptionTypeDef = TypedDict(
    "CustomPluginFileDescriptionTypeDef",
    {
        "fileMd5": str,
        "fileSize": int,
    },
    total=False,
)

CustomPluginLocationDescriptionTypeDef = TypedDict(
    "CustomPluginLocationDescriptionTypeDef",
    {
        "s3Location": "S3LocationDescriptionTypeDef",
    },
    total=False,
)

CustomPluginLocationTypeDef = TypedDict(
    "CustomPluginLocationTypeDef",
    {
        "s3Location": "S3LocationTypeDef",
    },
)

CustomPluginRevisionSummaryTypeDef = TypedDict(
    "CustomPluginRevisionSummaryTypeDef",
    {
        "contentType": CustomPluginContentTypeType,
        "creationTime": datetime,
        "description": str,
        "fileDescription": "CustomPluginFileDescriptionTypeDef",
        "location": "CustomPluginLocationDescriptionTypeDef",
        "revision": int,
    },
    total=False,
)

CustomPluginSummaryTypeDef = TypedDict(
    "CustomPluginSummaryTypeDef",
    {
        "creationTime": datetime,
        "customPluginArn": str,
        "customPluginState": CustomPluginStateType,
        "description": str,
        "latestRevision": "CustomPluginRevisionSummaryTypeDef",
        "name": str,
    },
    total=False,
)

CustomPluginTypeDef = TypedDict(
    "CustomPluginTypeDef",
    {
        "customPluginArn": str,
        "revision": int,
    },
)

_RequiredDeleteConnectorRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteConnectorRequestRequestTypeDef",
    {
        "connectorArn": str,
    },
)
_OptionalDeleteConnectorRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteConnectorRequestRequestTypeDef",
    {
        "currentVersion": str,
    },
    total=False,
)

class DeleteConnectorRequestRequestTypeDef(
    _RequiredDeleteConnectorRequestRequestTypeDef, _OptionalDeleteConnectorRequestRequestTypeDef
):
    pass

DeleteConnectorResponseTypeDef = TypedDict(
    "DeleteConnectorResponseTypeDef",
    {
        "connectorArn": str,
        "connectorState": ConnectorStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCustomPluginRequestRequestTypeDef = TypedDict(
    "DeleteCustomPluginRequestRequestTypeDef",
    {
        "customPluginArn": str,
    },
)

DeleteCustomPluginResponseTypeDef = TypedDict(
    "DeleteCustomPluginResponseTypeDef",
    {
        "customPluginArn": str,
        "customPluginState": CustomPluginStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteWorkerConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteWorkerConfigurationRequestRequestTypeDef",
    {
        "workerConfigurationArn": str,
    },
)

DeleteWorkerConfigurationResponseTypeDef = TypedDict(
    "DeleteWorkerConfigurationResponseTypeDef",
    {
        "workerConfigurationArn": str,
        "workerConfigurationState": WorkerConfigurationStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectorRequestRequestTypeDef = TypedDict(
    "DescribeConnectorRequestRequestTypeDef",
    {
        "connectorArn": str,
    },
)

DescribeConnectorResponseTypeDef = TypedDict(
    "DescribeConnectorResponseTypeDef",
    {
        "capacity": "CapacityDescriptionTypeDef",
        "connectorArn": str,
        "connectorConfiguration": Dict[str, str],
        "connectorDescription": str,
        "connectorName": str,
        "connectorState": ConnectorStateType,
        "creationTime": datetime,
        "currentVersion": str,
        "kafkaCluster": "KafkaClusterDescriptionTypeDef",
        "kafkaClusterClientAuthentication": "KafkaClusterClientAuthenticationDescriptionTypeDef",
        "kafkaClusterEncryptionInTransit": "KafkaClusterEncryptionInTransitDescriptionTypeDef",
        "kafkaConnectVersion": str,
        "logDelivery": "LogDeliveryDescriptionTypeDef",
        "plugins": List["PluginDescriptionTypeDef"],
        "serviceExecutionRoleArn": str,
        "stateDescription": "StateDescriptionTypeDef",
        "workerConfiguration": "WorkerConfigurationDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCustomPluginRequestRequestTypeDef = TypedDict(
    "DescribeCustomPluginRequestRequestTypeDef",
    {
        "customPluginArn": str,
    },
)

DescribeCustomPluginResponseTypeDef = TypedDict(
    "DescribeCustomPluginResponseTypeDef",
    {
        "creationTime": datetime,
        "customPluginArn": str,
        "customPluginState": CustomPluginStateType,
        "description": str,
        "latestRevision": "CustomPluginRevisionSummaryTypeDef",
        "name": str,
        "stateDescription": "StateDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkerConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeWorkerConfigurationRequestRequestTypeDef",
    {
        "workerConfigurationArn": str,
    },
)

DescribeWorkerConfigurationResponseTypeDef = TypedDict(
    "DescribeWorkerConfigurationResponseTypeDef",
    {
        "creationTime": datetime,
        "description": str,
        "latestRevision": "WorkerConfigurationRevisionDescriptionTypeDef",
        "name": str,
        "workerConfigurationArn": str,
        "workerConfigurationState": WorkerConfigurationStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FirehoseLogDeliveryDescriptionTypeDef = TypedDict(
    "FirehoseLogDeliveryDescriptionTypeDef",
    {
        "deliveryStream": str,
        "enabled": bool,
    },
    total=False,
)

_RequiredFirehoseLogDeliveryTypeDef = TypedDict(
    "_RequiredFirehoseLogDeliveryTypeDef",
    {
        "enabled": bool,
    },
)
_OptionalFirehoseLogDeliveryTypeDef = TypedDict(
    "_OptionalFirehoseLogDeliveryTypeDef",
    {
        "deliveryStream": str,
    },
    total=False,
)

class FirehoseLogDeliveryTypeDef(
    _RequiredFirehoseLogDeliveryTypeDef, _OptionalFirehoseLogDeliveryTypeDef
):
    pass

KafkaClusterClientAuthenticationDescriptionTypeDef = TypedDict(
    "KafkaClusterClientAuthenticationDescriptionTypeDef",
    {
        "authenticationType": KafkaClusterClientAuthenticationTypeType,
    },
    total=False,
)

KafkaClusterClientAuthenticationTypeDef = TypedDict(
    "KafkaClusterClientAuthenticationTypeDef",
    {
        "authenticationType": KafkaClusterClientAuthenticationTypeType,
    },
)

KafkaClusterDescriptionTypeDef = TypedDict(
    "KafkaClusterDescriptionTypeDef",
    {
        "apacheKafkaCluster": "ApacheKafkaClusterDescriptionTypeDef",
    },
    total=False,
)

KafkaClusterEncryptionInTransitDescriptionTypeDef = TypedDict(
    "KafkaClusterEncryptionInTransitDescriptionTypeDef",
    {
        "encryptionType": KafkaClusterEncryptionInTransitTypeType,
    },
    total=False,
)

KafkaClusterEncryptionInTransitTypeDef = TypedDict(
    "KafkaClusterEncryptionInTransitTypeDef",
    {
        "encryptionType": KafkaClusterEncryptionInTransitTypeType,
    },
)

KafkaClusterTypeDef = TypedDict(
    "KafkaClusterTypeDef",
    {
        "apacheKafkaCluster": "ApacheKafkaClusterTypeDef",
    },
)

ListConnectorsRequestRequestTypeDef = TypedDict(
    "ListConnectorsRequestRequestTypeDef",
    {
        "connectorNamePrefix": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListConnectorsResponseTypeDef = TypedDict(
    "ListConnectorsResponseTypeDef",
    {
        "connectors": List["ConnectorSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomPluginsRequestRequestTypeDef = TypedDict(
    "ListCustomPluginsRequestRequestTypeDef",
    {
        "maxResults": int,
        "namePrefix": str,
        "nextToken": str,
    },
    total=False,
)

ListCustomPluginsResponseTypeDef = TypedDict(
    "ListCustomPluginsResponseTypeDef",
    {
        "customPlugins": List["CustomPluginSummaryTypeDef"],
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

ListWorkerConfigurationsRequestRequestTypeDef = TypedDict(
    "ListWorkerConfigurationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "namePrefix": str,
        "nextToken": str,
    },
    total=False,
)

ListWorkerConfigurationsResponseTypeDef = TypedDict(
    "ListWorkerConfigurationsResponseTypeDef",
    {
        "nextToken": str,
        "workerConfigurations": List["WorkerConfigurationSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogDeliveryDescriptionTypeDef = TypedDict(
    "LogDeliveryDescriptionTypeDef",
    {
        "workerLogDelivery": "WorkerLogDeliveryDescriptionTypeDef",
    },
    total=False,
)

LogDeliveryTypeDef = TypedDict(
    "LogDeliveryTypeDef",
    {
        "workerLogDelivery": "WorkerLogDeliveryTypeDef",
    },
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

PluginDescriptionTypeDef = TypedDict(
    "PluginDescriptionTypeDef",
    {
        "customPlugin": "CustomPluginDescriptionTypeDef",
    },
    total=False,
)

PluginTypeDef = TypedDict(
    "PluginTypeDef",
    {
        "customPlugin": "CustomPluginTypeDef",
    },
)

ProvisionedCapacityDescriptionTypeDef = TypedDict(
    "ProvisionedCapacityDescriptionTypeDef",
    {
        "mcuCount": int,
        "workerCount": int,
    },
    total=False,
)

ProvisionedCapacityTypeDef = TypedDict(
    "ProvisionedCapacityTypeDef",
    {
        "mcuCount": int,
        "workerCount": int,
    },
)

ProvisionedCapacityUpdateTypeDef = TypedDict(
    "ProvisionedCapacityUpdateTypeDef",
    {
        "mcuCount": int,
        "workerCount": int,
    },
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

S3LocationDescriptionTypeDef = TypedDict(
    "S3LocationDescriptionTypeDef",
    {
        "bucketArn": str,
        "fileKey": str,
        "objectVersion": str,
    },
    total=False,
)

_RequiredS3LocationTypeDef = TypedDict(
    "_RequiredS3LocationTypeDef",
    {
        "bucketArn": str,
        "fileKey": str,
    },
)
_OptionalS3LocationTypeDef = TypedDict(
    "_OptionalS3LocationTypeDef",
    {
        "objectVersion": str,
    },
    total=False,
)

class S3LocationTypeDef(_RequiredS3LocationTypeDef, _OptionalS3LocationTypeDef):
    pass

S3LogDeliveryDescriptionTypeDef = TypedDict(
    "S3LogDeliveryDescriptionTypeDef",
    {
        "bucket": str,
        "enabled": bool,
        "prefix": str,
    },
    total=False,
)

_RequiredS3LogDeliveryTypeDef = TypedDict(
    "_RequiredS3LogDeliveryTypeDef",
    {
        "enabled": bool,
    },
)
_OptionalS3LogDeliveryTypeDef = TypedDict(
    "_OptionalS3LogDeliveryTypeDef",
    {
        "bucket": str,
        "prefix": str,
    },
    total=False,
)

class S3LogDeliveryTypeDef(_RequiredS3LogDeliveryTypeDef, _OptionalS3LogDeliveryTypeDef):
    pass

ScaleInPolicyDescriptionTypeDef = TypedDict(
    "ScaleInPolicyDescriptionTypeDef",
    {
        "cpuUtilizationPercentage": int,
    },
    total=False,
)

ScaleInPolicyTypeDef = TypedDict(
    "ScaleInPolicyTypeDef",
    {
        "cpuUtilizationPercentage": int,
    },
)

ScaleInPolicyUpdateTypeDef = TypedDict(
    "ScaleInPolicyUpdateTypeDef",
    {
        "cpuUtilizationPercentage": int,
    },
)

ScaleOutPolicyDescriptionTypeDef = TypedDict(
    "ScaleOutPolicyDescriptionTypeDef",
    {
        "cpuUtilizationPercentage": int,
    },
    total=False,
)

ScaleOutPolicyTypeDef = TypedDict(
    "ScaleOutPolicyTypeDef",
    {
        "cpuUtilizationPercentage": int,
    },
)

ScaleOutPolicyUpdateTypeDef = TypedDict(
    "ScaleOutPolicyUpdateTypeDef",
    {
        "cpuUtilizationPercentage": int,
    },
)

StateDescriptionTypeDef = TypedDict(
    "StateDescriptionTypeDef",
    {
        "code": str,
        "message": str,
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

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateConnectorRequestRequestTypeDef = TypedDict(
    "UpdateConnectorRequestRequestTypeDef",
    {
        "capacity": "CapacityUpdateTypeDef",
        "connectorArn": str,
        "currentVersion": str,
    },
)

UpdateConnectorResponseTypeDef = TypedDict(
    "UpdateConnectorResponseTypeDef",
    {
        "connectorArn": str,
        "connectorState": ConnectorStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcDescriptionTypeDef = TypedDict(
    "VpcDescriptionTypeDef",
    {
        "securityGroups": List[str],
        "subnets": List[str],
    },
    total=False,
)

_RequiredVpcTypeDef = TypedDict(
    "_RequiredVpcTypeDef",
    {
        "subnets": List[str],
    },
)
_OptionalVpcTypeDef = TypedDict(
    "_OptionalVpcTypeDef",
    {
        "securityGroups": List[str],
    },
    total=False,
)

class VpcTypeDef(_RequiredVpcTypeDef, _OptionalVpcTypeDef):
    pass

WorkerConfigurationDescriptionTypeDef = TypedDict(
    "WorkerConfigurationDescriptionTypeDef",
    {
        "revision": int,
        "workerConfigurationArn": str,
    },
    total=False,
)

WorkerConfigurationRevisionDescriptionTypeDef = TypedDict(
    "WorkerConfigurationRevisionDescriptionTypeDef",
    {
        "creationTime": datetime,
        "description": str,
        "propertiesFileContent": str,
        "revision": int,
    },
    total=False,
)

WorkerConfigurationRevisionSummaryTypeDef = TypedDict(
    "WorkerConfigurationRevisionSummaryTypeDef",
    {
        "creationTime": datetime,
        "description": str,
        "revision": int,
    },
    total=False,
)

WorkerConfigurationSummaryTypeDef = TypedDict(
    "WorkerConfigurationSummaryTypeDef",
    {
        "creationTime": datetime,
        "description": str,
        "latestRevision": "WorkerConfigurationRevisionSummaryTypeDef",
        "name": str,
        "workerConfigurationArn": str,
        "workerConfigurationState": WorkerConfigurationStateType,
    },
    total=False,
)

WorkerConfigurationTypeDef = TypedDict(
    "WorkerConfigurationTypeDef",
    {
        "revision": int,
        "workerConfigurationArn": str,
    },
)

WorkerLogDeliveryDescriptionTypeDef = TypedDict(
    "WorkerLogDeliveryDescriptionTypeDef",
    {
        "cloudWatchLogs": "CloudWatchLogsLogDeliveryDescriptionTypeDef",
        "firehose": "FirehoseLogDeliveryDescriptionTypeDef",
        "s3": "S3LogDeliveryDescriptionTypeDef",
    },
    total=False,
)

WorkerLogDeliveryTypeDef = TypedDict(
    "WorkerLogDeliveryTypeDef",
    {
        "cloudWatchLogs": "CloudWatchLogsLogDeliveryTypeDef",
        "firehose": "FirehoseLogDeliveryTypeDef",
        "s3": "S3LogDeliveryTypeDef",
    },
    total=False,
)
