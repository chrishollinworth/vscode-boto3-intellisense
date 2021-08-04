"""
Type annotations for kafka service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafka/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kafka.type_defs import BatchAssociateScramSecretRequestRequestTypeDef

    data: BatchAssociateScramSecretRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ClientBrokerType,
    ClusterStateType,
    ConfigurationStateType,
    EnhancedMonitoringType,
    KafkaVersionStatusType,
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
    "BatchAssociateScramSecretRequestRequestTypeDef",
    "BatchAssociateScramSecretResponseTypeDef",
    "BatchDisassociateScramSecretRequestRequestTypeDef",
    "BatchDisassociateScramSecretResponseTypeDef",
    "BrokerEBSVolumeInfoTypeDef",
    "BrokerLogsTypeDef",
    "BrokerNodeGroupInfoTypeDef",
    "BrokerNodeInfoTypeDef",
    "BrokerSoftwareInfoTypeDef",
    "ClientAuthenticationTypeDef",
    "CloudWatchLogsTypeDef",
    "ClusterInfoTypeDef",
    "ClusterOperationInfoTypeDef",
    "ClusterOperationStepInfoTypeDef",
    "ClusterOperationStepTypeDef",
    "CompatibleKafkaVersionTypeDef",
    "ConfigurationInfoTypeDef",
    "ConfigurationRevisionTypeDef",
    "ConfigurationTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateConfigurationRequestRequestTypeDef",
    "CreateConfigurationResponseTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteConfigurationRequestRequestTypeDef",
    "DeleteConfigurationResponseTypeDef",
    "DescribeClusterOperationRequestRequestTypeDef",
    "DescribeClusterOperationResponseTypeDef",
    "DescribeClusterRequestRequestTypeDef",
    "DescribeClusterResponseTypeDef",
    "DescribeConfigurationRequestRequestTypeDef",
    "DescribeConfigurationResponseTypeDef",
    "DescribeConfigurationRevisionRequestRequestTypeDef",
    "DescribeConfigurationRevisionResponseTypeDef",
    "EBSStorageInfoTypeDef",
    "EncryptionAtRestTypeDef",
    "EncryptionInTransitTypeDef",
    "EncryptionInfoTypeDef",
    "ErrorInfoTypeDef",
    "FirehoseTypeDef",
    "GetBootstrapBrokersRequestRequestTypeDef",
    "GetBootstrapBrokersResponseTypeDef",
    "GetCompatibleKafkaVersionsRequestRequestTypeDef",
    "GetCompatibleKafkaVersionsResponseTypeDef",
    "IamTypeDef",
    "JmxExporterInfoTypeDef",
    "JmxExporterTypeDef",
    "KafkaVersionTypeDef",
    "ListClusterOperationsRequestRequestTypeDef",
    "ListClusterOperationsResponseTypeDef",
    "ListClustersRequestRequestTypeDef",
    "ListClustersResponseTypeDef",
    "ListConfigurationRevisionsRequestRequestTypeDef",
    "ListConfigurationRevisionsResponseTypeDef",
    "ListConfigurationsRequestRequestTypeDef",
    "ListConfigurationsResponseTypeDef",
    "ListKafkaVersionsRequestRequestTypeDef",
    "ListKafkaVersionsResponseTypeDef",
    "ListNodesRequestRequestTypeDef",
    "ListNodesResponseTypeDef",
    "ListScramSecretsRequestRequestTypeDef",
    "ListScramSecretsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LoggingInfoTypeDef",
    "MutableClusterInfoTypeDef",
    "NodeExporterInfoTypeDef",
    "NodeExporterTypeDef",
    "NodeInfoTypeDef",
    "OpenMonitoringInfoTypeDef",
    "OpenMonitoringTypeDef",
    "PaginatorConfigTypeDef",
    "PrometheusInfoTypeDef",
    "PrometheusTypeDef",
    "RebootBrokerRequestRequestTypeDef",
    "RebootBrokerResponseTypeDef",
    "ResponseMetadataTypeDef",
    "S3TypeDef",
    "SaslTypeDef",
    "ScramTypeDef",
    "StateInfoTypeDef",
    "StorageInfoTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TlsTypeDef",
    "UnprocessedScramSecretTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateBrokerCountRequestRequestTypeDef",
    "UpdateBrokerCountResponseTypeDef",
    "UpdateBrokerStorageRequestRequestTypeDef",
    "UpdateBrokerStorageResponseTypeDef",
    "UpdateBrokerTypeRequestRequestTypeDef",
    "UpdateBrokerTypeResponseTypeDef",
    "UpdateClusterConfigurationRequestRequestTypeDef",
    "UpdateClusterConfigurationResponseTypeDef",
    "UpdateClusterKafkaVersionRequestRequestTypeDef",
    "UpdateClusterKafkaVersionResponseTypeDef",
    "UpdateConfigurationRequestRequestTypeDef",
    "UpdateConfigurationResponseTypeDef",
    "UpdateMonitoringRequestRequestTypeDef",
    "UpdateMonitoringResponseTypeDef",
    "ZookeeperNodeInfoTypeDef",
)

BatchAssociateScramSecretRequestRequestTypeDef = TypedDict(
    "BatchAssociateScramSecretRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "SecretArnList": List[str],
    },
)

BatchAssociateScramSecretResponseTypeDef = TypedDict(
    "BatchAssociateScramSecretResponseTypeDef",
    {
        "ClusterArn": str,
        "UnprocessedScramSecrets": List["UnprocessedScramSecretTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDisassociateScramSecretRequestRequestTypeDef = TypedDict(
    "BatchDisassociateScramSecretRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "SecretArnList": List[str],
    },
)

BatchDisassociateScramSecretResponseTypeDef = TypedDict(
    "BatchDisassociateScramSecretResponseTypeDef",
    {
        "ClusterArn": str,
        "UnprocessedScramSecrets": List["UnprocessedScramSecretTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BrokerEBSVolumeInfoTypeDef = TypedDict(
    "BrokerEBSVolumeInfoTypeDef",
    {
        "KafkaBrokerNodeId": str,
        "VolumeSizeGB": int,
    },
)

BrokerLogsTypeDef = TypedDict(
    "BrokerLogsTypeDef",
    {
        "CloudWatchLogs": "CloudWatchLogsTypeDef",
        "Firehose": "FirehoseTypeDef",
        "S3": "S3TypeDef",
    },
    total=False,
)

_RequiredBrokerNodeGroupInfoTypeDef = TypedDict(
    "_RequiredBrokerNodeGroupInfoTypeDef",
    {
        "ClientSubnets": List[str],
        "InstanceType": str,
    },
)
_OptionalBrokerNodeGroupInfoTypeDef = TypedDict(
    "_OptionalBrokerNodeGroupInfoTypeDef",
    {
        "BrokerAZDistribution": Literal["DEFAULT"],
        "SecurityGroups": List[str],
        "StorageInfo": "StorageInfoTypeDef",
    },
    total=False,
)

class BrokerNodeGroupInfoTypeDef(
    _RequiredBrokerNodeGroupInfoTypeDef, _OptionalBrokerNodeGroupInfoTypeDef
):
    pass

BrokerNodeInfoTypeDef = TypedDict(
    "BrokerNodeInfoTypeDef",
    {
        "AttachedENIId": str,
        "BrokerId": float,
        "ClientSubnet": str,
        "ClientVpcIpAddress": str,
        "CurrentBrokerSoftwareInfo": "BrokerSoftwareInfoTypeDef",
        "Endpoints": List[str],
    },
    total=False,
)

BrokerSoftwareInfoTypeDef = TypedDict(
    "BrokerSoftwareInfoTypeDef",
    {
        "ConfigurationArn": str,
        "ConfigurationRevision": int,
        "KafkaVersion": str,
    },
    total=False,
)

ClientAuthenticationTypeDef = TypedDict(
    "ClientAuthenticationTypeDef",
    {
        "Sasl": "SaslTypeDef",
        "Tls": "TlsTypeDef",
    },
    total=False,
)

_RequiredCloudWatchLogsTypeDef = TypedDict(
    "_RequiredCloudWatchLogsTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalCloudWatchLogsTypeDef = TypedDict(
    "_OptionalCloudWatchLogsTypeDef",
    {
        "LogGroup": str,
    },
    total=False,
)

class CloudWatchLogsTypeDef(_RequiredCloudWatchLogsTypeDef, _OptionalCloudWatchLogsTypeDef):
    pass

ClusterInfoTypeDef = TypedDict(
    "ClusterInfoTypeDef",
    {
        "ActiveOperationArn": str,
        "BrokerNodeGroupInfo": "BrokerNodeGroupInfoTypeDef",
        "ClientAuthentication": "ClientAuthenticationTypeDef",
        "ClusterArn": str,
        "ClusterName": str,
        "CreationTime": datetime,
        "CurrentBrokerSoftwareInfo": "BrokerSoftwareInfoTypeDef",
        "CurrentVersion": str,
        "EncryptionInfo": "EncryptionInfoTypeDef",
        "EnhancedMonitoring": EnhancedMonitoringType,
        "OpenMonitoring": "OpenMonitoringTypeDef",
        "LoggingInfo": "LoggingInfoTypeDef",
        "NumberOfBrokerNodes": int,
        "State": ClusterStateType,
        "StateInfo": "StateInfoTypeDef",
        "Tags": Dict[str, str],
        "ZookeeperConnectString": str,
        "ZookeeperConnectStringTls": str,
    },
    total=False,
)

ClusterOperationInfoTypeDef = TypedDict(
    "ClusterOperationInfoTypeDef",
    {
        "ClientRequestId": str,
        "ClusterArn": str,
        "CreationTime": datetime,
        "EndTime": datetime,
        "ErrorInfo": "ErrorInfoTypeDef",
        "OperationArn": str,
        "OperationState": str,
        "OperationSteps": List["ClusterOperationStepTypeDef"],
        "OperationType": str,
        "SourceClusterInfo": "MutableClusterInfoTypeDef",
        "TargetClusterInfo": "MutableClusterInfoTypeDef",
    },
    total=False,
)

ClusterOperationStepInfoTypeDef = TypedDict(
    "ClusterOperationStepInfoTypeDef",
    {
        "StepStatus": str,
    },
    total=False,
)

ClusterOperationStepTypeDef = TypedDict(
    "ClusterOperationStepTypeDef",
    {
        "StepInfo": "ClusterOperationStepInfoTypeDef",
        "StepName": str,
    },
    total=False,
)

CompatibleKafkaVersionTypeDef = TypedDict(
    "CompatibleKafkaVersionTypeDef",
    {
        "SourceVersion": str,
        "TargetVersions": List[str],
    },
    total=False,
)

ConfigurationInfoTypeDef = TypedDict(
    "ConfigurationInfoTypeDef",
    {
        "Arn": str,
        "Revision": int,
    },
)

_RequiredConfigurationRevisionTypeDef = TypedDict(
    "_RequiredConfigurationRevisionTypeDef",
    {
        "CreationTime": datetime,
        "Revision": int,
    },
)
_OptionalConfigurationRevisionTypeDef = TypedDict(
    "_OptionalConfigurationRevisionTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class ConfigurationRevisionTypeDef(
    _RequiredConfigurationRevisionTypeDef, _OptionalConfigurationRevisionTypeDef
):
    pass

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "KafkaVersions": List[str],
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "State": ConfigurationStateType,
    },
)

_RequiredCreateClusterRequestRequestTypeDef = TypedDict(
    "_RequiredCreateClusterRequestRequestTypeDef",
    {
        "BrokerNodeGroupInfo": "BrokerNodeGroupInfoTypeDef",
        "ClusterName": str,
        "KafkaVersion": str,
        "NumberOfBrokerNodes": int,
    },
)
_OptionalCreateClusterRequestRequestTypeDef = TypedDict(
    "_OptionalCreateClusterRequestRequestTypeDef",
    {
        "ClientAuthentication": "ClientAuthenticationTypeDef",
        "ConfigurationInfo": "ConfigurationInfoTypeDef",
        "EncryptionInfo": "EncryptionInfoTypeDef",
        "EnhancedMonitoring": EnhancedMonitoringType,
        "OpenMonitoring": "OpenMonitoringInfoTypeDef",
        "LoggingInfo": "LoggingInfoTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateClusterRequestRequestTypeDef(
    _RequiredCreateClusterRequestRequestTypeDef, _OptionalCreateClusterRequestRequestTypeDef
):
    pass

CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterName": str,
        "State": ClusterStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConfigurationRequestRequestTypeDef",
    {
        "Name": str,
        "ServerProperties": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalCreateConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConfigurationRequestRequestTypeDef",
    {
        "Description": str,
        "KafkaVersions": List[str],
    },
    total=False,
)

class CreateConfigurationRequestRequestTypeDef(
    _RequiredCreateConfigurationRequestRequestTypeDef,
    _OptionalCreateConfigurationRequestRequestTypeDef,
):
    pass

CreateConfigurationResponseTypeDef = TypedDict(
    "CreateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "State": ConfigurationStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteClusterRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteClusterRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)
_OptionalDeleteClusterRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteClusterRequestRequestTypeDef",
    {
        "CurrentVersion": str,
    },
    total=False,
)

class DeleteClusterRequestRequestTypeDef(
    _RequiredDeleteClusterRequestRequestTypeDef, _OptionalDeleteClusterRequestRequestTypeDef
):
    pass

DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef",
    {
        "ClusterArn": str,
        "State": ClusterStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

DeleteConfigurationResponseTypeDef = TypedDict(
    "DeleteConfigurationResponseTypeDef",
    {
        "Arn": str,
        "State": ConfigurationStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClusterOperationRequestRequestTypeDef = TypedDict(
    "DescribeClusterOperationRequestRequestTypeDef",
    {
        "ClusterOperationArn": str,
    },
)

DescribeClusterOperationResponseTypeDef = TypedDict(
    "DescribeClusterOperationResponseTypeDef",
    {
        "ClusterOperationInfo": "ClusterOperationInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClusterRequestRequestTypeDef = TypedDict(
    "DescribeClusterRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)

DescribeClusterResponseTypeDef = TypedDict(
    "DescribeClusterResponseTypeDef",
    {
        "ClusterInfo": "ClusterInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

DescribeConfigurationResponseTypeDef = TypedDict(
    "DescribeConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "KafkaVersions": List[str],
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "State": ConfigurationStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationRevisionRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationRevisionRequestRequestTypeDef",
    {
        "Arn": str,
        "Revision": int,
    },
)

DescribeConfigurationRevisionResponseTypeDef = TypedDict(
    "DescribeConfigurationRevisionResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "Revision": int,
        "ServerProperties": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EBSStorageInfoTypeDef = TypedDict(
    "EBSStorageInfoTypeDef",
    {
        "VolumeSize": int,
    },
    total=False,
)

EncryptionAtRestTypeDef = TypedDict(
    "EncryptionAtRestTypeDef",
    {
        "DataVolumeKMSKeyId": str,
    },
)

EncryptionInTransitTypeDef = TypedDict(
    "EncryptionInTransitTypeDef",
    {
        "ClientBroker": ClientBrokerType,
        "InCluster": bool,
    },
    total=False,
)

EncryptionInfoTypeDef = TypedDict(
    "EncryptionInfoTypeDef",
    {
        "EncryptionAtRest": "EncryptionAtRestTypeDef",
        "EncryptionInTransit": "EncryptionInTransitTypeDef",
    },
    total=False,
)

ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "ErrorCode": str,
        "ErrorString": str,
    },
    total=False,
)

_RequiredFirehoseTypeDef = TypedDict(
    "_RequiredFirehoseTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalFirehoseTypeDef = TypedDict(
    "_OptionalFirehoseTypeDef",
    {
        "DeliveryStream": str,
    },
    total=False,
)

class FirehoseTypeDef(_RequiredFirehoseTypeDef, _OptionalFirehoseTypeDef):
    pass

GetBootstrapBrokersRequestRequestTypeDef = TypedDict(
    "GetBootstrapBrokersRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)

GetBootstrapBrokersResponseTypeDef = TypedDict(
    "GetBootstrapBrokersResponseTypeDef",
    {
        "BootstrapBrokerString": str,
        "BootstrapBrokerStringTls": str,
        "BootstrapBrokerStringSaslScram": str,
        "BootstrapBrokerStringSaslIam": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCompatibleKafkaVersionsRequestRequestTypeDef = TypedDict(
    "GetCompatibleKafkaVersionsRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
    total=False,
)

GetCompatibleKafkaVersionsResponseTypeDef = TypedDict(
    "GetCompatibleKafkaVersionsResponseTypeDef",
    {
        "CompatibleKafkaVersions": List["CompatibleKafkaVersionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IamTypeDef = TypedDict(
    "IamTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

JmxExporterInfoTypeDef = TypedDict(
    "JmxExporterInfoTypeDef",
    {
        "EnabledInBroker": bool,
    },
)

JmxExporterTypeDef = TypedDict(
    "JmxExporterTypeDef",
    {
        "EnabledInBroker": bool,
    },
)

KafkaVersionTypeDef = TypedDict(
    "KafkaVersionTypeDef",
    {
        "Version": str,
        "Status": KafkaVersionStatusType,
    },
    total=False,
)

_RequiredListClusterOperationsRequestRequestTypeDef = TypedDict(
    "_RequiredListClusterOperationsRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)
_OptionalListClusterOperationsRequestRequestTypeDef = TypedDict(
    "_OptionalListClusterOperationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListClusterOperationsRequestRequestTypeDef(
    _RequiredListClusterOperationsRequestRequestTypeDef,
    _OptionalListClusterOperationsRequestRequestTypeDef,
):
    pass

ListClusterOperationsResponseTypeDef = TypedDict(
    "ListClusterOperationsResponseTypeDef",
    {
        "ClusterOperationInfoList": List["ClusterOperationInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListClustersRequestRequestTypeDef = TypedDict(
    "ListClustersRequestRequestTypeDef",
    {
        "ClusterNameFilter": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListClustersResponseTypeDef = TypedDict(
    "ListClustersResponseTypeDef",
    {
        "ClusterInfoList": List["ClusterInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListConfigurationRevisionsRequestRequestTypeDef = TypedDict(
    "_RequiredListConfigurationRevisionsRequestRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalListConfigurationRevisionsRequestRequestTypeDef = TypedDict(
    "_OptionalListConfigurationRevisionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListConfigurationRevisionsRequestRequestTypeDef(
    _RequiredListConfigurationRevisionsRequestRequestTypeDef,
    _OptionalListConfigurationRevisionsRequestRequestTypeDef,
):
    pass

ListConfigurationRevisionsResponseTypeDef = TypedDict(
    "ListConfigurationRevisionsResponseTypeDef",
    {
        "NextToken": str,
        "Revisions": List["ConfigurationRevisionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConfigurationsRequestRequestTypeDef = TypedDict(
    "ListConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListConfigurationsResponseTypeDef = TypedDict(
    "ListConfigurationsResponseTypeDef",
    {
        "Configurations": List["ConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListKafkaVersionsRequestRequestTypeDef = TypedDict(
    "ListKafkaVersionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListKafkaVersionsResponseTypeDef = TypedDict(
    "ListKafkaVersionsResponseTypeDef",
    {
        "KafkaVersions": List["KafkaVersionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListNodesRequestRequestTypeDef = TypedDict(
    "_RequiredListNodesRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)
_OptionalListNodesRequestRequestTypeDef = TypedDict(
    "_OptionalListNodesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListNodesRequestRequestTypeDef(
    _RequiredListNodesRequestRequestTypeDef, _OptionalListNodesRequestRequestTypeDef
):
    pass

ListNodesResponseTypeDef = TypedDict(
    "ListNodesResponseTypeDef",
    {
        "NextToken": str,
        "NodeInfoList": List["NodeInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListScramSecretsRequestRequestTypeDef = TypedDict(
    "_RequiredListScramSecretsRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)
_OptionalListScramSecretsRequestRequestTypeDef = TypedDict(
    "_OptionalListScramSecretsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListScramSecretsRequestRequestTypeDef(
    _RequiredListScramSecretsRequestRequestTypeDef, _OptionalListScramSecretsRequestRequestTypeDef
):
    pass

ListScramSecretsResponseTypeDef = TypedDict(
    "ListScramSecretsResponseTypeDef",
    {
        "NextToken": str,
        "SecretArnList": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingInfoTypeDef = TypedDict(
    "LoggingInfoTypeDef",
    {
        "BrokerLogs": "BrokerLogsTypeDef",
    },
)

MutableClusterInfoTypeDef = TypedDict(
    "MutableClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List["BrokerEBSVolumeInfoTypeDef"],
        "ConfigurationInfo": "ConfigurationInfoTypeDef",
        "NumberOfBrokerNodes": int,
        "EnhancedMonitoring": EnhancedMonitoringType,
        "OpenMonitoring": "OpenMonitoringTypeDef",
        "KafkaVersion": str,
        "LoggingInfo": "LoggingInfoTypeDef",
        "InstanceType": str,
    },
    total=False,
)

NodeExporterInfoTypeDef = TypedDict(
    "NodeExporterInfoTypeDef",
    {
        "EnabledInBroker": bool,
    },
)

NodeExporterTypeDef = TypedDict(
    "NodeExporterTypeDef",
    {
        "EnabledInBroker": bool,
    },
)

NodeInfoTypeDef = TypedDict(
    "NodeInfoTypeDef",
    {
        "AddedToClusterTime": str,
        "BrokerNodeInfo": "BrokerNodeInfoTypeDef",
        "InstanceType": str,
        "NodeARN": str,
        "NodeType": Literal["BROKER"],
        "ZookeeperNodeInfo": "ZookeeperNodeInfoTypeDef",
    },
    total=False,
)

OpenMonitoringInfoTypeDef = TypedDict(
    "OpenMonitoringInfoTypeDef",
    {
        "Prometheus": "PrometheusInfoTypeDef",
    },
)

OpenMonitoringTypeDef = TypedDict(
    "OpenMonitoringTypeDef",
    {
        "Prometheus": "PrometheusTypeDef",
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

PrometheusInfoTypeDef = TypedDict(
    "PrometheusInfoTypeDef",
    {
        "JmxExporter": "JmxExporterInfoTypeDef",
        "NodeExporter": "NodeExporterInfoTypeDef",
    },
    total=False,
)

PrometheusTypeDef = TypedDict(
    "PrometheusTypeDef",
    {
        "JmxExporter": "JmxExporterTypeDef",
        "NodeExporter": "NodeExporterTypeDef",
    },
    total=False,
)

RebootBrokerRequestRequestTypeDef = TypedDict(
    "RebootBrokerRequestRequestTypeDef",
    {
        "BrokerIds": List[str],
        "ClusterArn": str,
    },
)

RebootBrokerResponseTypeDef = TypedDict(
    "RebootBrokerResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

_RequiredS3TypeDef = TypedDict(
    "_RequiredS3TypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalS3TypeDef = TypedDict(
    "_OptionalS3TypeDef",
    {
        "Bucket": str,
        "Prefix": str,
    },
    total=False,
)

class S3TypeDef(_RequiredS3TypeDef, _OptionalS3TypeDef):
    pass

SaslTypeDef = TypedDict(
    "SaslTypeDef",
    {
        "Scram": "ScramTypeDef",
        "Iam": "IamTypeDef",
    },
    total=False,
)

ScramTypeDef = TypedDict(
    "ScramTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

StateInfoTypeDef = TypedDict(
    "StateInfoTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

StorageInfoTypeDef = TypedDict(
    "StorageInfoTypeDef",
    {
        "EbsStorageInfo": "EBSStorageInfoTypeDef",
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

TlsTypeDef = TypedDict(
    "TlsTypeDef",
    {
        "CertificateAuthorityArnList": List[str],
    },
    total=False,
)

UnprocessedScramSecretTypeDef = TypedDict(
    "UnprocessedScramSecretTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "SecretArn": str,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateBrokerCountRequestRequestTypeDef = TypedDict(
    "UpdateBrokerCountRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
        "TargetNumberOfBrokerNodes": int,
    },
)

UpdateBrokerCountResponseTypeDef = TypedDict(
    "UpdateBrokerCountResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBrokerStorageRequestRequestTypeDef = TypedDict(
    "UpdateBrokerStorageRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
        "TargetBrokerEBSVolumeInfo": List["BrokerEBSVolumeInfoTypeDef"],
    },
)

UpdateBrokerStorageResponseTypeDef = TypedDict(
    "UpdateBrokerStorageResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBrokerTypeRequestRequestTypeDef = TypedDict(
    "UpdateBrokerTypeRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
        "TargetInstanceType": str,
    },
)

UpdateBrokerTypeResponseTypeDef = TypedDict(
    "UpdateBrokerTypeResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateClusterConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateClusterConfigurationRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "ConfigurationInfo": "ConfigurationInfoTypeDef",
        "CurrentVersion": str,
    },
)

UpdateClusterConfigurationResponseTypeDef = TypedDict(
    "UpdateClusterConfigurationResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateClusterKafkaVersionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateClusterKafkaVersionRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
        "TargetKafkaVersion": str,
    },
)
_OptionalUpdateClusterKafkaVersionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateClusterKafkaVersionRequestRequestTypeDef",
    {
        "ConfigurationInfo": "ConfigurationInfoTypeDef",
    },
    total=False,
)

class UpdateClusterKafkaVersionRequestRequestTypeDef(
    _RequiredUpdateClusterKafkaVersionRequestRequestTypeDef,
    _OptionalUpdateClusterKafkaVersionRequestRequestTypeDef,
):
    pass

UpdateClusterKafkaVersionResponseTypeDef = TypedDict(
    "UpdateClusterKafkaVersionResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateConfigurationRequestRequestTypeDef",
    {
        "Arn": str,
        "ServerProperties": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalUpdateConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateConfigurationRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateConfigurationRequestRequestTypeDef(
    _RequiredUpdateConfigurationRequestRequestTypeDef,
    _OptionalUpdateConfigurationRequestRequestTypeDef,
):
    pass

UpdateConfigurationResponseTypeDef = TypedDict(
    "UpdateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMonitoringRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMonitoringRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
    },
)
_OptionalUpdateMonitoringRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMonitoringRequestRequestTypeDef",
    {
        "EnhancedMonitoring": EnhancedMonitoringType,
        "OpenMonitoring": "OpenMonitoringInfoTypeDef",
        "LoggingInfo": "LoggingInfoTypeDef",
    },
    total=False,
)

class UpdateMonitoringRequestRequestTypeDef(
    _RequiredUpdateMonitoringRequestRequestTypeDef, _OptionalUpdateMonitoringRequestRequestTypeDef
):
    pass

UpdateMonitoringResponseTypeDef = TypedDict(
    "UpdateMonitoringResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ZookeeperNodeInfoTypeDef = TypedDict(
    "ZookeeperNodeInfoTypeDef",
    {
        "AttachedENIId": str,
        "ClientVpcIpAddress": str,
        "Endpoints": List[str],
        "ZookeeperId": float,
        "ZookeeperVersion": str,
    },
    total=False,
)
