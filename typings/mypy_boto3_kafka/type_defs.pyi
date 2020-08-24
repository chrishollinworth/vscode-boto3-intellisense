"""
Main interface for kafka service type definitions.

Usage::

    ```python
    from mypy_boto3_kafka.type_defs import BrokerEBSVolumeInfoTypeDef

    data: BrokerEBSVolumeInfoTypeDef = {...}
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
    "EBSStorageInfoTypeDef",
    "EncryptionAtRestTypeDef",
    "EncryptionInTransitTypeDef",
    "EncryptionInfoTypeDef",
    "ErrorInfoTypeDef",
    "FirehoseTypeDef",
    "JmxExporterInfoTypeDef",
    "JmxExporterTypeDef",
    "KafkaVersionTypeDef",
    "LoggingInfoTypeDef",
    "MutableClusterInfoTypeDef",
    "NodeExporterInfoTypeDef",
    "NodeExporterTypeDef",
    "NodeInfoTypeDef",
    "OpenMonitoringTypeDef",
    "PrometheusInfoTypeDef",
    "PrometheusTypeDef",
    "S3TypeDef",
    "StateInfoTypeDef",
    "StorageInfoTypeDef",
    "TlsTypeDef",
    "ZookeeperNodeInfoTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateConfigurationResponseTypeDef",
    "DeleteClusterResponseTypeDef",
    "DescribeClusterOperationResponseTypeDef",
    "DescribeClusterResponseTypeDef",
    "DescribeConfigurationResponseTypeDef",
    "DescribeConfigurationRevisionResponseTypeDef",
    "GetBootstrapBrokersResponseTypeDef",
    "GetCompatibleKafkaVersionsResponseTypeDef",
    "ListClusterOperationsResponseTypeDef",
    "ListClustersResponseTypeDef",
    "ListConfigurationRevisionsResponseTypeDef",
    "ListConfigurationsResponseTypeDef",
    "ListKafkaVersionsResponseTypeDef",
    "ListNodesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OpenMonitoringInfoTypeDef",
    "PaginatorConfigTypeDef",
    "RebootBrokerResponseTypeDef",
    "UpdateBrokerCountResponseTypeDef",
    "UpdateBrokerStorageResponseTypeDef",
    "UpdateClusterConfigurationResponseTypeDef",
    "UpdateClusterKafkaVersionResponseTypeDef",
    "UpdateMonitoringResponseTypeDef",
)

BrokerEBSVolumeInfoTypeDef = TypedDict(
    "BrokerEBSVolumeInfoTypeDef", {"KafkaBrokerNodeId": str, "VolumeSizeGB": int}
)

BrokerLogsTypeDef = TypedDict(
    "BrokerLogsTypeDef",
    {"CloudWatchLogs": "CloudWatchLogsTypeDef", "Firehose": "FirehoseTypeDef", "S3": "S3TypeDef"},
    total=False,
)

_RequiredBrokerNodeGroupInfoTypeDef = TypedDict(
    "_RequiredBrokerNodeGroupInfoTypeDef", {"ClientSubnets": List[str], "InstanceType": str}
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
    {"ConfigurationArn": str, "ConfigurationRevision": int, "KafkaVersion": str},
    total=False,
)

ClientAuthenticationTypeDef = TypedDict(
    "ClientAuthenticationTypeDef", {"Tls": "TlsTypeDef"}, total=False
)

_RequiredCloudWatchLogsTypeDef = TypedDict("_RequiredCloudWatchLogsTypeDef", {"Enabled": bool})
_OptionalCloudWatchLogsTypeDef = TypedDict(
    "_OptionalCloudWatchLogsTypeDef", {"LogGroup": str}, total=False
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
        "EnhancedMonitoring": Literal["DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER"],
        "OpenMonitoring": "OpenMonitoringTypeDef",
        "LoggingInfo": "LoggingInfoTypeDef",
        "NumberOfBrokerNodes": int,
        "State": Literal["ACTIVE", "CREATING", "UPDATING", "DELETING", "FAILED"],
        "StateInfo": "StateInfoTypeDef",
        "Tags": Dict[str, str],
        "ZookeeperConnectString": str,
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
    "ClusterOperationStepInfoTypeDef", {"StepStatus": str}, total=False
)

ClusterOperationStepTypeDef = TypedDict(
    "ClusterOperationStepTypeDef",
    {"StepInfo": "ClusterOperationStepInfoTypeDef", "StepName": str},
    total=False,
)

CompatibleKafkaVersionTypeDef = TypedDict(
    "CompatibleKafkaVersionTypeDef",
    {"SourceVersion": str, "TargetVersions": List[str]},
    total=False,
)

ConfigurationInfoTypeDef = TypedDict("ConfigurationInfoTypeDef", {"Arn": str, "Revision": int})

_RequiredConfigurationRevisionTypeDef = TypedDict(
    "_RequiredConfigurationRevisionTypeDef", {"CreationTime": datetime, "Revision": int}
)
_OptionalConfigurationRevisionTypeDef = TypedDict(
    "_OptionalConfigurationRevisionTypeDef", {"Description": str}, total=False
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
    },
)

EBSStorageInfoTypeDef = TypedDict("EBSStorageInfoTypeDef", {"VolumeSize": int}, total=False)

EncryptionAtRestTypeDef = TypedDict("EncryptionAtRestTypeDef", {"DataVolumeKMSKeyId": str})

EncryptionInTransitTypeDef = TypedDict(
    "EncryptionInTransitTypeDef",
    {"ClientBroker": Literal["TLS", "TLS_PLAINTEXT", "PLAINTEXT"], "InCluster": bool},
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
    "ErrorInfoTypeDef", {"ErrorCode": str, "ErrorString": str}, total=False
)

_RequiredFirehoseTypeDef = TypedDict("_RequiredFirehoseTypeDef", {"Enabled": bool})
_OptionalFirehoseTypeDef = TypedDict(
    "_OptionalFirehoseTypeDef", {"DeliveryStream": str}, total=False
)


class FirehoseTypeDef(_RequiredFirehoseTypeDef, _OptionalFirehoseTypeDef):
    pass


JmxExporterInfoTypeDef = TypedDict("JmxExporterInfoTypeDef", {"EnabledInBroker": bool})

JmxExporterTypeDef = TypedDict("JmxExporterTypeDef", {"EnabledInBroker": bool})

KafkaVersionTypeDef = TypedDict(
    "KafkaVersionTypeDef", {"Version": str, "Status": Literal["ACTIVE", "DEPRECATED"]}, total=False
)

LoggingInfoTypeDef = TypedDict("LoggingInfoTypeDef", {"BrokerLogs": "BrokerLogsTypeDef"})

MutableClusterInfoTypeDef = TypedDict(
    "MutableClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List["BrokerEBSVolumeInfoTypeDef"],
        "ConfigurationInfo": "ConfigurationInfoTypeDef",
        "NumberOfBrokerNodes": int,
        "EnhancedMonitoring": Literal["DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER"],
        "OpenMonitoring": "OpenMonitoringTypeDef",
        "KafkaVersion": str,
        "LoggingInfo": "LoggingInfoTypeDef",
    },
    total=False,
)

NodeExporterInfoTypeDef = TypedDict("NodeExporterInfoTypeDef", {"EnabledInBroker": bool})

NodeExporterTypeDef = TypedDict("NodeExporterTypeDef", {"EnabledInBroker": bool})

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

OpenMonitoringTypeDef = TypedDict("OpenMonitoringTypeDef", {"Prometheus": "PrometheusTypeDef"})

PrometheusInfoTypeDef = TypedDict(
    "PrometheusInfoTypeDef",
    {"JmxExporter": "JmxExporterInfoTypeDef", "NodeExporter": "NodeExporterInfoTypeDef"},
    total=False,
)

PrometheusTypeDef = TypedDict(
    "PrometheusTypeDef",
    {"JmxExporter": "JmxExporterTypeDef", "NodeExporter": "NodeExporterTypeDef"},
    total=False,
)

_RequiredS3TypeDef = TypedDict("_RequiredS3TypeDef", {"Enabled": bool})
_OptionalS3TypeDef = TypedDict("_OptionalS3TypeDef", {"Bucket": str, "Prefix": str}, total=False)


class S3TypeDef(_RequiredS3TypeDef, _OptionalS3TypeDef):
    pass


StateInfoTypeDef = TypedDict("StateInfoTypeDef", {"Code": str, "Message": str}, total=False)

StorageInfoTypeDef = TypedDict(
    "StorageInfoTypeDef", {"EbsStorageInfo": "EBSStorageInfoTypeDef"}, total=False
)

TlsTypeDef = TypedDict("TlsTypeDef", {"CertificateAuthorityArnList": List[str]}, total=False)

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

CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterName": str,
        "State": Literal["ACTIVE", "CREATING", "UPDATING", "DELETING", "FAILED"],
    },
    total=False,
)

CreateConfigurationResponseTypeDef = TypedDict(
    "CreateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
    },
    total=False,
)

DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef",
    {"ClusterArn": str, "State": Literal["ACTIVE", "CREATING", "UPDATING", "DELETING", "FAILED"]},
    total=False,
)

DescribeClusterOperationResponseTypeDef = TypedDict(
    "DescribeClusterOperationResponseTypeDef",
    {"ClusterOperationInfo": "ClusterOperationInfoTypeDef"},
    total=False,
)

DescribeClusterResponseTypeDef = TypedDict(
    "DescribeClusterResponseTypeDef", {"ClusterInfo": "ClusterInfoTypeDef"}, total=False
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
    },
    total=False,
)

DescribeConfigurationRevisionResponseTypeDef = TypedDict(
    "DescribeConfigurationRevisionResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "Revision": int,
        "ServerProperties": bytes,
    },
    total=False,
)

GetBootstrapBrokersResponseTypeDef = TypedDict(
    "GetBootstrapBrokersResponseTypeDef",
    {"BootstrapBrokerString": str, "BootstrapBrokerStringTls": str},
    total=False,
)

GetCompatibleKafkaVersionsResponseTypeDef = TypedDict(
    "GetCompatibleKafkaVersionsResponseTypeDef",
    {"CompatibleKafkaVersions": List["CompatibleKafkaVersionTypeDef"]},
    total=False,
)

ListClusterOperationsResponseTypeDef = TypedDict(
    "ListClusterOperationsResponseTypeDef",
    {"ClusterOperationInfoList": List["ClusterOperationInfoTypeDef"], "NextToken": str},
    total=False,
)

ListClustersResponseTypeDef = TypedDict(
    "ListClustersResponseTypeDef",
    {"ClusterInfoList": List["ClusterInfoTypeDef"], "NextToken": str},
    total=False,
)

ListConfigurationRevisionsResponseTypeDef = TypedDict(
    "ListConfigurationRevisionsResponseTypeDef",
    {"NextToken": str, "Revisions": List["ConfigurationRevisionTypeDef"]},
    total=False,
)

ListConfigurationsResponseTypeDef = TypedDict(
    "ListConfigurationsResponseTypeDef",
    {"Configurations": List["ConfigurationTypeDef"], "NextToken": str},
    total=False,
)

ListKafkaVersionsResponseTypeDef = TypedDict(
    "ListKafkaVersionsResponseTypeDef",
    {"KafkaVersions": List["KafkaVersionTypeDef"], "NextToken": str},
    total=False,
)

ListNodesResponseTypeDef = TypedDict(
    "ListNodesResponseTypeDef",
    {"NextToken": str, "NodeInfoList": List["NodeInfoTypeDef"]},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

OpenMonitoringInfoTypeDef = TypedDict(
    "OpenMonitoringInfoTypeDef", {"Prometheus": "PrometheusInfoTypeDef"}
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RebootBrokerResponseTypeDef = TypedDict(
    "RebootBrokerResponseTypeDef", {"ClusterArn": str, "ClusterOperationArn": str}, total=False
)

UpdateBrokerCountResponseTypeDef = TypedDict(
    "UpdateBrokerCountResponseTypeDef", {"ClusterArn": str, "ClusterOperationArn": str}, total=False
)

UpdateBrokerStorageResponseTypeDef = TypedDict(
    "UpdateBrokerStorageResponseTypeDef",
    {"ClusterArn": str, "ClusterOperationArn": str},
    total=False,
)

UpdateClusterConfigurationResponseTypeDef = TypedDict(
    "UpdateClusterConfigurationResponseTypeDef",
    {"ClusterArn": str, "ClusterOperationArn": str},
    total=False,
)

UpdateClusterKafkaVersionResponseTypeDef = TypedDict(
    "UpdateClusterKafkaVersionResponseTypeDef",
    {"ClusterArn": str, "ClusterOperationArn": str},
    total=False,
)

UpdateMonitoringResponseTypeDef = TypedDict(
    "UpdateMonitoringResponseTypeDef", {"ClusterArn": str, "ClusterOperationArn": str}, total=False
)
