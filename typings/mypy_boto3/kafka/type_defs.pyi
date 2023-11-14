"""
Type annotations for kafka service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafka/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kafka.type_defs import AmazonMskClusterTypeDef

    data: AmazonMskClusterTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ClientBrokerType,
    ClusterStateType,
    ClusterTypeType,
    ConfigurationStateType,
    EnhancedMonitoringType,
    KafkaVersionStatusType,
    ReplicatorStateType,
    StorageModeType,
    TargetCompressionTypeType,
    UserIdentityTypeType,
    VpcConnectionStateType,
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
    "AmazonMskClusterTypeDef",
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
    "ClientVpcConnectionTypeDef",
    "CloudWatchLogsTypeDef",
    "ClusterInfoTypeDef",
    "ClusterOperationInfoTypeDef",
    "ClusterOperationStepInfoTypeDef",
    "ClusterOperationStepTypeDef",
    "ClusterOperationV2ProvisionedTypeDef",
    "ClusterOperationV2ServerlessTypeDef",
    "ClusterOperationV2SummaryTypeDef",
    "ClusterOperationV2TypeDef",
    "ClusterTypeDef",
    "CompatibleKafkaVersionTypeDef",
    "ConfigurationInfoTypeDef",
    "ConfigurationRevisionTypeDef",
    "ConfigurationTypeDef",
    "ConnectivityInfoTypeDef",
    "ConsumerGroupReplicationTypeDef",
    "ConsumerGroupReplicationUpdateTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateClusterV2RequestRequestTypeDef",
    "CreateClusterV2ResponseTypeDef",
    "CreateConfigurationRequestRequestTypeDef",
    "CreateConfigurationResponseTypeDef",
    "CreateReplicatorRequestRequestTypeDef",
    "CreateReplicatorResponseTypeDef",
    "CreateVpcConnectionRequestRequestTypeDef",
    "CreateVpcConnectionResponseTypeDef",
    "DeleteClusterPolicyRequestRequestTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteConfigurationRequestRequestTypeDef",
    "DeleteConfigurationResponseTypeDef",
    "DeleteReplicatorRequestRequestTypeDef",
    "DeleteReplicatorResponseTypeDef",
    "DeleteVpcConnectionRequestRequestTypeDef",
    "DeleteVpcConnectionResponseTypeDef",
    "DescribeClusterOperationRequestRequestTypeDef",
    "DescribeClusterOperationResponseTypeDef",
    "DescribeClusterOperationV2RequestRequestTypeDef",
    "DescribeClusterOperationV2ResponseTypeDef",
    "DescribeClusterRequestRequestTypeDef",
    "DescribeClusterResponseTypeDef",
    "DescribeClusterV2RequestRequestTypeDef",
    "DescribeClusterV2ResponseTypeDef",
    "DescribeConfigurationRequestRequestTypeDef",
    "DescribeConfigurationResponseTypeDef",
    "DescribeConfigurationRevisionRequestRequestTypeDef",
    "DescribeConfigurationRevisionResponseTypeDef",
    "DescribeReplicatorRequestRequestTypeDef",
    "DescribeReplicatorResponseTypeDef",
    "DescribeVpcConnectionRequestRequestTypeDef",
    "DescribeVpcConnectionResponseTypeDef",
    "EBSStorageInfoTypeDef",
    "EncryptionAtRestTypeDef",
    "EncryptionInTransitTypeDef",
    "EncryptionInfoTypeDef",
    "ErrorInfoTypeDef",
    "FirehoseTypeDef",
    "GetBootstrapBrokersRequestRequestTypeDef",
    "GetBootstrapBrokersResponseTypeDef",
    "GetClusterPolicyRequestRequestTypeDef",
    "GetClusterPolicyResponseTypeDef",
    "GetCompatibleKafkaVersionsRequestRequestTypeDef",
    "GetCompatibleKafkaVersionsResponseTypeDef",
    "IamTypeDef",
    "JmxExporterInfoTypeDef",
    "JmxExporterTypeDef",
    "KafkaClusterClientVpcConfigTypeDef",
    "KafkaClusterDescriptionTypeDef",
    "KafkaClusterSummaryTypeDef",
    "KafkaClusterTypeDef",
    "KafkaVersionTypeDef",
    "ListClientVpcConnectionsRequestRequestTypeDef",
    "ListClientVpcConnectionsResponseTypeDef",
    "ListClusterOperationsRequestRequestTypeDef",
    "ListClusterOperationsResponseTypeDef",
    "ListClusterOperationsV2RequestRequestTypeDef",
    "ListClusterOperationsV2ResponseTypeDef",
    "ListClustersRequestRequestTypeDef",
    "ListClustersResponseTypeDef",
    "ListClustersV2RequestRequestTypeDef",
    "ListClustersV2ResponseTypeDef",
    "ListConfigurationRevisionsRequestRequestTypeDef",
    "ListConfigurationRevisionsResponseTypeDef",
    "ListConfigurationsRequestRequestTypeDef",
    "ListConfigurationsResponseTypeDef",
    "ListKafkaVersionsRequestRequestTypeDef",
    "ListKafkaVersionsResponseTypeDef",
    "ListNodesRequestRequestTypeDef",
    "ListNodesResponseTypeDef",
    "ListReplicatorsRequestRequestTypeDef",
    "ListReplicatorsResponseTypeDef",
    "ListScramSecretsRequestRequestTypeDef",
    "ListScramSecretsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVpcConnectionsRequestRequestTypeDef",
    "ListVpcConnectionsResponseTypeDef",
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
    "ProvisionedRequestTypeDef",
    "ProvisionedThroughputTypeDef",
    "ProvisionedTypeDef",
    "PublicAccessTypeDef",
    "PutClusterPolicyRequestRequestTypeDef",
    "PutClusterPolicyResponseTypeDef",
    "RebootBrokerRequestRequestTypeDef",
    "RebootBrokerResponseTypeDef",
    "RejectClientVpcConnectionRequestRequestTypeDef",
    "ReplicationInfoDescriptionTypeDef",
    "ReplicationInfoSummaryTypeDef",
    "ReplicationInfoTypeDef",
    "ReplicationStateInfoTypeDef",
    "ReplicatorSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "S3TypeDef",
    "SaslTypeDef",
    "ScramTypeDef",
    "ServerlessClientAuthenticationTypeDef",
    "ServerlessRequestTypeDef",
    "ServerlessSaslTypeDef",
    "ServerlessTypeDef",
    "StateInfoTypeDef",
    "StorageInfoTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TlsTypeDef",
    "TopicReplicationTypeDef",
    "TopicReplicationUpdateTypeDef",
    "UnauthenticatedTypeDef",
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
    "UpdateConnectivityRequestRequestTypeDef",
    "UpdateConnectivityResponseTypeDef",
    "UpdateMonitoringRequestRequestTypeDef",
    "UpdateMonitoringResponseTypeDef",
    "UpdateReplicationInfoRequestRequestTypeDef",
    "UpdateReplicationInfoResponseTypeDef",
    "UpdateSecurityRequestRequestTypeDef",
    "UpdateSecurityResponseTypeDef",
    "UpdateStorageRequestRequestTypeDef",
    "UpdateStorageResponseTypeDef",
    "UserIdentityTypeDef",
    "VpcConfigTypeDef",
    "VpcConnectionInfoServerlessTypeDef",
    "VpcConnectionInfoTypeDef",
    "VpcConnectionTypeDef",
    "VpcConnectivityClientAuthenticationTypeDef",
    "VpcConnectivityIamTypeDef",
    "VpcConnectivitySaslTypeDef",
    "VpcConnectivityScramTypeDef",
    "VpcConnectivityTlsTypeDef",
    "VpcConnectivityTypeDef",
    "ZookeeperNodeInfoTypeDef",
)

AmazonMskClusterTypeDef = TypedDict(
    "AmazonMskClusterTypeDef",
    {
        "MskClusterArn": str,
    },
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

_RequiredBrokerEBSVolumeInfoTypeDef = TypedDict(
    "_RequiredBrokerEBSVolumeInfoTypeDef",
    {
        "KafkaBrokerNodeId": str,
    },
)
_OptionalBrokerEBSVolumeInfoTypeDef = TypedDict(
    "_OptionalBrokerEBSVolumeInfoTypeDef",
    {
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
        "VolumeSizeGB": int,
    },
    total=False,
)

class BrokerEBSVolumeInfoTypeDef(
    _RequiredBrokerEBSVolumeInfoTypeDef, _OptionalBrokerEBSVolumeInfoTypeDef
):
    pass

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
        "ConnectivityInfo": "ConnectivityInfoTypeDef",
        "ZoneIds": List[str],
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
        "Unauthenticated": "UnauthenticatedTypeDef",
    },
    total=False,
)

_RequiredClientVpcConnectionTypeDef = TypedDict(
    "_RequiredClientVpcConnectionTypeDef",
    {
        "VpcConnectionArn": str,
    },
)
_OptionalClientVpcConnectionTypeDef = TypedDict(
    "_OptionalClientVpcConnectionTypeDef",
    {
        "Authentication": str,
        "CreationTime": datetime,
        "State": VpcConnectionStateType,
        "Owner": str,
    },
    total=False,
)

class ClientVpcConnectionTypeDef(
    _RequiredClientVpcConnectionTypeDef, _OptionalClientVpcConnectionTypeDef
):
    pass

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
        "StorageMode": StorageModeType,
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
        "VpcConnectionInfo": "VpcConnectionInfoTypeDef",
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

ClusterOperationV2ProvisionedTypeDef = TypedDict(
    "ClusterOperationV2ProvisionedTypeDef",
    {
        "OperationSteps": List["ClusterOperationStepTypeDef"],
        "SourceClusterInfo": "MutableClusterInfoTypeDef",
        "TargetClusterInfo": "MutableClusterInfoTypeDef",
        "VpcConnectionInfo": "VpcConnectionInfoTypeDef",
    },
    total=False,
)

ClusterOperationV2ServerlessTypeDef = TypedDict(
    "ClusterOperationV2ServerlessTypeDef",
    {
        "VpcConnectionInfo": "VpcConnectionInfoServerlessTypeDef",
    },
    total=False,
)

ClusterOperationV2SummaryTypeDef = TypedDict(
    "ClusterOperationV2SummaryTypeDef",
    {
        "ClusterArn": str,
        "ClusterType": ClusterTypeType,
        "StartTime": datetime,
        "EndTime": datetime,
        "OperationArn": str,
        "OperationState": str,
        "OperationType": str,
    },
    total=False,
)

ClusterOperationV2TypeDef = TypedDict(
    "ClusterOperationV2TypeDef",
    {
        "ClusterArn": str,
        "ClusterType": ClusterTypeType,
        "StartTime": datetime,
        "EndTime": datetime,
        "ErrorInfo": "ErrorInfoTypeDef",
        "OperationArn": str,
        "OperationState": str,
        "OperationType": str,
        "Provisioned": "ClusterOperationV2ProvisionedTypeDef",
        "Serverless": "ClusterOperationV2ServerlessTypeDef",
    },
    total=False,
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "ActiveOperationArn": str,
        "ClusterType": ClusterTypeType,
        "ClusterArn": str,
        "ClusterName": str,
        "CreationTime": datetime,
        "CurrentVersion": str,
        "State": ClusterStateType,
        "StateInfo": "StateInfoTypeDef",
        "Tags": Dict[str, str],
        "Provisioned": "ProvisionedTypeDef",
        "Serverless": "ServerlessTypeDef",
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

ConnectivityInfoTypeDef = TypedDict(
    "ConnectivityInfoTypeDef",
    {
        "PublicAccess": "PublicAccessTypeDef",
        "VpcConnectivity": "VpcConnectivityTypeDef",
    },
    total=False,
)

_RequiredConsumerGroupReplicationTypeDef = TypedDict(
    "_RequiredConsumerGroupReplicationTypeDef",
    {
        "ConsumerGroupsToReplicate": List[str],
    },
)
_OptionalConsumerGroupReplicationTypeDef = TypedDict(
    "_OptionalConsumerGroupReplicationTypeDef",
    {
        "ConsumerGroupsToExclude": List[str],
        "DetectAndCopyNewConsumerGroups": bool,
        "SynchroniseConsumerGroupOffsets": bool,
    },
    total=False,
)

class ConsumerGroupReplicationTypeDef(
    _RequiredConsumerGroupReplicationTypeDef, _OptionalConsumerGroupReplicationTypeDef
):
    pass

ConsumerGroupReplicationUpdateTypeDef = TypedDict(
    "ConsumerGroupReplicationUpdateTypeDef",
    {
        "ConsumerGroupsToExclude": List[str],
        "ConsumerGroupsToReplicate": List[str],
        "DetectAndCopyNewConsumerGroups": bool,
        "SynchroniseConsumerGroupOffsets": bool,
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
        "StorageMode": StorageModeType,
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

_RequiredCreateClusterV2RequestRequestTypeDef = TypedDict(
    "_RequiredCreateClusterV2RequestRequestTypeDef",
    {
        "ClusterName": str,
    },
)
_OptionalCreateClusterV2RequestRequestTypeDef = TypedDict(
    "_OptionalCreateClusterV2RequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
        "Provisioned": "ProvisionedRequestTypeDef",
        "Serverless": "ServerlessRequestTypeDef",
    },
    total=False,
)

class CreateClusterV2RequestRequestTypeDef(
    _RequiredCreateClusterV2RequestRequestTypeDef, _OptionalCreateClusterV2RequestRequestTypeDef
):
    pass

CreateClusterV2ResponseTypeDef = TypedDict(
    "CreateClusterV2ResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterName": str,
        "State": ClusterStateType,
        "ClusterType": ClusterTypeType,
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

_RequiredCreateReplicatorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateReplicatorRequestRequestTypeDef",
    {
        "KafkaClusters": List["KafkaClusterTypeDef"],
        "ReplicationInfoList": List["ReplicationInfoTypeDef"],
        "ReplicatorName": str,
        "ServiceExecutionRoleArn": str,
    },
)
_OptionalCreateReplicatorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateReplicatorRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateReplicatorRequestRequestTypeDef(
    _RequiredCreateReplicatorRequestRequestTypeDef, _OptionalCreateReplicatorRequestRequestTypeDef
):
    pass

CreateReplicatorResponseTypeDef = TypedDict(
    "CreateReplicatorResponseTypeDef",
    {
        "ReplicatorArn": str,
        "ReplicatorName": str,
        "ReplicatorState": ReplicatorStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVpcConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVpcConnectionRequestRequestTypeDef",
    {
        "TargetClusterArn": str,
        "Authentication": str,
        "VpcId": str,
        "ClientSubnets": List[str],
        "SecurityGroups": List[str],
    },
)
_OptionalCreateVpcConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVpcConnectionRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateVpcConnectionRequestRequestTypeDef(
    _RequiredCreateVpcConnectionRequestRequestTypeDef,
    _OptionalCreateVpcConnectionRequestRequestTypeDef,
):
    pass

CreateVpcConnectionResponseTypeDef = TypedDict(
    "CreateVpcConnectionResponseTypeDef",
    {
        "VpcConnectionArn": str,
        "State": VpcConnectionStateType,
        "Authentication": str,
        "VpcId": str,
        "ClientSubnets": List[str],
        "SecurityGroups": List[str],
        "CreationTime": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterPolicyRequestRequestTypeDef = TypedDict(
    "DeleteClusterPolicyRequestRequestTypeDef",
    {
        "ClusterArn": str,
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

_RequiredDeleteReplicatorRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteReplicatorRequestRequestTypeDef",
    {
        "ReplicatorArn": str,
    },
)
_OptionalDeleteReplicatorRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteReplicatorRequestRequestTypeDef",
    {
        "CurrentVersion": str,
    },
    total=False,
)

class DeleteReplicatorRequestRequestTypeDef(
    _RequiredDeleteReplicatorRequestRequestTypeDef, _OptionalDeleteReplicatorRequestRequestTypeDef
):
    pass

DeleteReplicatorResponseTypeDef = TypedDict(
    "DeleteReplicatorResponseTypeDef",
    {
        "ReplicatorArn": str,
        "ReplicatorState": ReplicatorStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVpcConnectionRequestRequestTypeDef = TypedDict(
    "DeleteVpcConnectionRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

DeleteVpcConnectionResponseTypeDef = TypedDict(
    "DeleteVpcConnectionResponseTypeDef",
    {
        "VpcConnectionArn": str,
        "State": VpcConnectionStateType,
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

DescribeClusterOperationV2RequestRequestTypeDef = TypedDict(
    "DescribeClusterOperationV2RequestRequestTypeDef",
    {
        "ClusterOperationArn": str,
    },
)

DescribeClusterOperationV2ResponseTypeDef = TypedDict(
    "DescribeClusterOperationV2ResponseTypeDef",
    {
        "ClusterOperationInfo": "ClusterOperationV2TypeDef",
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

DescribeClusterV2RequestRequestTypeDef = TypedDict(
    "DescribeClusterV2RequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)

DescribeClusterV2ResponseTypeDef = TypedDict(
    "DescribeClusterV2ResponseTypeDef",
    {
        "ClusterInfo": "ClusterTypeDef",
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

DescribeReplicatorRequestRequestTypeDef = TypedDict(
    "DescribeReplicatorRequestRequestTypeDef",
    {
        "ReplicatorArn": str,
    },
)

DescribeReplicatorResponseTypeDef = TypedDict(
    "DescribeReplicatorResponseTypeDef",
    {
        "CreationTime": datetime,
        "CurrentVersion": str,
        "IsReplicatorReference": bool,
        "KafkaClusters": List["KafkaClusterDescriptionTypeDef"],
        "ReplicationInfoList": List["ReplicationInfoDescriptionTypeDef"],
        "ReplicatorArn": str,
        "ReplicatorDescription": str,
        "ReplicatorName": str,
        "ReplicatorResourceArn": str,
        "ReplicatorState": ReplicatorStateType,
        "ServiceExecutionRoleArn": str,
        "StateInfo": "ReplicationStateInfoTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcConnectionRequestRequestTypeDef = TypedDict(
    "DescribeVpcConnectionRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

DescribeVpcConnectionResponseTypeDef = TypedDict(
    "DescribeVpcConnectionResponseTypeDef",
    {
        "VpcConnectionArn": str,
        "TargetClusterArn": str,
        "State": VpcConnectionStateType,
        "Authentication": str,
        "VpcId": str,
        "Subnets": List[str],
        "SecurityGroups": List[str],
        "CreationTime": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EBSStorageInfoTypeDef = TypedDict(
    "EBSStorageInfoTypeDef",
    {
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
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
        "BootstrapBrokerStringPublicTls": str,
        "BootstrapBrokerStringPublicSaslScram": str,
        "BootstrapBrokerStringPublicSaslIam": str,
        "BootstrapBrokerStringVpcConnectivityTls": str,
        "BootstrapBrokerStringVpcConnectivitySaslScram": str,
        "BootstrapBrokerStringVpcConnectivitySaslIam": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetClusterPolicyRequestRequestTypeDef = TypedDict(
    "GetClusterPolicyRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)

GetClusterPolicyResponseTypeDef = TypedDict(
    "GetClusterPolicyResponseTypeDef",
    {
        "CurrentVersion": str,
        "Policy": str,
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

_RequiredKafkaClusterClientVpcConfigTypeDef = TypedDict(
    "_RequiredKafkaClusterClientVpcConfigTypeDef",
    {
        "SubnetIds": List[str],
    },
)
_OptionalKafkaClusterClientVpcConfigTypeDef = TypedDict(
    "_OptionalKafkaClusterClientVpcConfigTypeDef",
    {
        "SecurityGroupIds": List[str],
    },
    total=False,
)

class KafkaClusterClientVpcConfigTypeDef(
    _RequiredKafkaClusterClientVpcConfigTypeDef, _OptionalKafkaClusterClientVpcConfigTypeDef
):
    pass

KafkaClusterDescriptionTypeDef = TypedDict(
    "KafkaClusterDescriptionTypeDef",
    {
        "AmazonMskCluster": "AmazonMskClusterTypeDef",
        "KafkaClusterAlias": str,
        "VpcConfig": "KafkaClusterClientVpcConfigTypeDef",
    },
    total=False,
)

KafkaClusterSummaryTypeDef = TypedDict(
    "KafkaClusterSummaryTypeDef",
    {
        "AmazonMskCluster": "AmazonMskClusterTypeDef",
        "KafkaClusterAlias": str,
    },
    total=False,
)

KafkaClusterTypeDef = TypedDict(
    "KafkaClusterTypeDef",
    {
        "AmazonMskCluster": "AmazonMskClusterTypeDef",
        "VpcConfig": "KafkaClusterClientVpcConfigTypeDef",
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

_RequiredListClientVpcConnectionsRequestRequestTypeDef = TypedDict(
    "_RequiredListClientVpcConnectionsRequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)
_OptionalListClientVpcConnectionsRequestRequestTypeDef = TypedDict(
    "_OptionalListClientVpcConnectionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListClientVpcConnectionsRequestRequestTypeDef(
    _RequiredListClientVpcConnectionsRequestRequestTypeDef,
    _OptionalListClientVpcConnectionsRequestRequestTypeDef,
):
    pass

ListClientVpcConnectionsResponseTypeDef = TypedDict(
    "ListClientVpcConnectionsResponseTypeDef",
    {
        "ClientVpcConnections": List["ClientVpcConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredListClusterOperationsV2RequestRequestTypeDef = TypedDict(
    "_RequiredListClusterOperationsV2RequestRequestTypeDef",
    {
        "ClusterArn": str,
    },
)
_OptionalListClusterOperationsV2RequestRequestTypeDef = TypedDict(
    "_OptionalListClusterOperationsV2RequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListClusterOperationsV2RequestRequestTypeDef(
    _RequiredListClusterOperationsV2RequestRequestTypeDef,
    _OptionalListClusterOperationsV2RequestRequestTypeDef,
):
    pass

ListClusterOperationsV2ResponseTypeDef = TypedDict(
    "ListClusterOperationsV2ResponseTypeDef",
    {
        "ClusterOperationInfoList": List["ClusterOperationV2SummaryTypeDef"],
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

ListClustersV2RequestRequestTypeDef = TypedDict(
    "ListClustersV2RequestRequestTypeDef",
    {
        "ClusterNameFilter": str,
        "ClusterTypeFilter": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListClustersV2ResponseTypeDef = TypedDict(
    "ListClustersV2ResponseTypeDef",
    {
        "ClusterInfoList": List["ClusterTypeDef"],
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

ListReplicatorsRequestRequestTypeDef = TypedDict(
    "ListReplicatorsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ReplicatorNameFilter": str,
    },
    total=False,
)

ListReplicatorsResponseTypeDef = TypedDict(
    "ListReplicatorsResponseTypeDef",
    {
        "NextToken": str,
        "Replicators": List["ReplicatorSummaryTypeDef"],
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

ListVpcConnectionsRequestRequestTypeDef = TypedDict(
    "ListVpcConnectionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListVpcConnectionsResponseTypeDef = TypedDict(
    "ListVpcConnectionsResponseTypeDef",
    {
        "VpcConnections": List["VpcConnectionTypeDef"],
        "NextToken": str,
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
        "ClientAuthentication": "ClientAuthenticationTypeDef",
        "EncryptionInfo": "EncryptionInfoTypeDef",
        "ConnectivityInfo": "ConnectivityInfoTypeDef",
        "StorageMode": StorageModeType,
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

_RequiredProvisionedRequestTypeDef = TypedDict(
    "_RequiredProvisionedRequestTypeDef",
    {
        "BrokerNodeGroupInfo": "BrokerNodeGroupInfoTypeDef",
        "KafkaVersion": str,
        "NumberOfBrokerNodes": int,
    },
)
_OptionalProvisionedRequestTypeDef = TypedDict(
    "_OptionalProvisionedRequestTypeDef",
    {
        "ClientAuthentication": "ClientAuthenticationTypeDef",
        "ConfigurationInfo": "ConfigurationInfoTypeDef",
        "EncryptionInfo": "EncryptionInfoTypeDef",
        "EnhancedMonitoring": EnhancedMonitoringType,
        "OpenMonitoring": "OpenMonitoringInfoTypeDef",
        "LoggingInfo": "LoggingInfoTypeDef",
        "StorageMode": StorageModeType,
    },
    total=False,
)

class ProvisionedRequestTypeDef(
    _RequiredProvisionedRequestTypeDef, _OptionalProvisionedRequestTypeDef
):
    pass

ProvisionedThroughputTypeDef = TypedDict(
    "ProvisionedThroughputTypeDef",
    {
        "Enabled": bool,
        "VolumeThroughput": int,
    },
    total=False,
)

_RequiredProvisionedTypeDef = TypedDict(
    "_RequiredProvisionedTypeDef",
    {
        "BrokerNodeGroupInfo": "BrokerNodeGroupInfoTypeDef",
        "NumberOfBrokerNodes": int,
    },
)
_OptionalProvisionedTypeDef = TypedDict(
    "_OptionalProvisionedTypeDef",
    {
        "CurrentBrokerSoftwareInfo": "BrokerSoftwareInfoTypeDef",
        "ClientAuthentication": "ClientAuthenticationTypeDef",
        "EncryptionInfo": "EncryptionInfoTypeDef",
        "EnhancedMonitoring": EnhancedMonitoringType,
        "OpenMonitoring": "OpenMonitoringInfoTypeDef",
        "LoggingInfo": "LoggingInfoTypeDef",
        "ZookeeperConnectString": str,
        "ZookeeperConnectStringTls": str,
        "StorageMode": StorageModeType,
    },
    total=False,
)

class ProvisionedTypeDef(_RequiredProvisionedTypeDef, _OptionalProvisionedTypeDef):
    pass

PublicAccessTypeDef = TypedDict(
    "PublicAccessTypeDef",
    {
        "Type": str,
    },
    total=False,
)

_RequiredPutClusterPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutClusterPolicyRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "Policy": str,
    },
)
_OptionalPutClusterPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutClusterPolicyRequestRequestTypeDef",
    {
        "CurrentVersion": str,
    },
    total=False,
)

class PutClusterPolicyRequestRequestTypeDef(
    _RequiredPutClusterPolicyRequestRequestTypeDef, _OptionalPutClusterPolicyRequestRequestTypeDef
):
    pass

PutClusterPolicyResponseTypeDef = TypedDict(
    "PutClusterPolicyResponseTypeDef",
    {
        "CurrentVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

RejectClientVpcConnectionRequestRequestTypeDef = TypedDict(
    "RejectClientVpcConnectionRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "VpcConnectionArn": str,
    },
)

ReplicationInfoDescriptionTypeDef = TypedDict(
    "ReplicationInfoDescriptionTypeDef",
    {
        "ConsumerGroupReplication": "ConsumerGroupReplicationTypeDef",
        "SourceKafkaClusterAlias": str,
        "TargetCompressionType": TargetCompressionTypeType,
        "TargetKafkaClusterAlias": str,
        "TopicReplication": "TopicReplicationTypeDef",
    },
    total=False,
)

ReplicationInfoSummaryTypeDef = TypedDict(
    "ReplicationInfoSummaryTypeDef",
    {
        "SourceKafkaClusterAlias": str,
        "TargetKafkaClusterAlias": str,
    },
    total=False,
)

ReplicationInfoTypeDef = TypedDict(
    "ReplicationInfoTypeDef",
    {
        "ConsumerGroupReplication": "ConsumerGroupReplicationTypeDef",
        "SourceKafkaClusterArn": str,
        "TargetCompressionType": TargetCompressionTypeType,
        "TargetKafkaClusterArn": str,
        "TopicReplication": "TopicReplicationTypeDef",
    },
)

ReplicationStateInfoTypeDef = TypedDict(
    "ReplicationStateInfoTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

ReplicatorSummaryTypeDef = TypedDict(
    "ReplicatorSummaryTypeDef",
    {
        "CreationTime": datetime,
        "CurrentVersion": str,
        "IsReplicatorReference": bool,
        "KafkaClustersSummary": List["KafkaClusterSummaryTypeDef"],
        "ReplicationInfoSummaryList": List["ReplicationInfoSummaryTypeDef"],
        "ReplicatorArn": str,
        "ReplicatorName": str,
        "ReplicatorResourceArn": str,
        "ReplicatorState": ReplicatorStateType,
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

ServerlessClientAuthenticationTypeDef = TypedDict(
    "ServerlessClientAuthenticationTypeDef",
    {
        "Sasl": "ServerlessSaslTypeDef",
    },
    total=False,
)

_RequiredServerlessRequestTypeDef = TypedDict(
    "_RequiredServerlessRequestTypeDef",
    {
        "VpcConfigs": List["VpcConfigTypeDef"],
    },
)
_OptionalServerlessRequestTypeDef = TypedDict(
    "_OptionalServerlessRequestTypeDef",
    {
        "ClientAuthentication": "ServerlessClientAuthenticationTypeDef",
    },
    total=False,
)

class ServerlessRequestTypeDef(
    _RequiredServerlessRequestTypeDef, _OptionalServerlessRequestTypeDef
):
    pass

ServerlessSaslTypeDef = TypedDict(
    "ServerlessSaslTypeDef",
    {
        "Iam": "IamTypeDef",
    },
    total=False,
)

_RequiredServerlessTypeDef = TypedDict(
    "_RequiredServerlessTypeDef",
    {
        "VpcConfigs": List["VpcConfigTypeDef"],
    },
)
_OptionalServerlessTypeDef = TypedDict(
    "_OptionalServerlessTypeDef",
    {
        "ClientAuthentication": "ServerlessClientAuthenticationTypeDef",
    },
    total=False,
)

class ServerlessTypeDef(_RequiredServerlessTypeDef, _OptionalServerlessTypeDef):
    pass

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
        "Enabled": bool,
    },
    total=False,
)

_RequiredTopicReplicationTypeDef = TypedDict(
    "_RequiredTopicReplicationTypeDef",
    {
        "TopicsToReplicate": List[str],
    },
)
_OptionalTopicReplicationTypeDef = TypedDict(
    "_OptionalTopicReplicationTypeDef",
    {
        "CopyAccessControlListsForTopics": bool,
        "CopyTopicConfigurations": bool,
        "DetectAndCopyNewTopics": bool,
        "TopicsToExclude": List[str],
    },
    total=False,
)

class TopicReplicationTypeDef(_RequiredTopicReplicationTypeDef, _OptionalTopicReplicationTypeDef):
    pass

TopicReplicationUpdateTypeDef = TypedDict(
    "TopicReplicationUpdateTypeDef",
    {
        "CopyAccessControlListsForTopics": bool,
        "CopyTopicConfigurations": bool,
        "DetectAndCopyNewTopics": bool,
        "TopicsToExclude": List[str],
        "TopicsToReplicate": List[str],
    },
)

UnauthenticatedTypeDef = TypedDict(
    "UnauthenticatedTypeDef",
    {
        "Enabled": bool,
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

UpdateConnectivityRequestRequestTypeDef = TypedDict(
    "UpdateConnectivityRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "ConnectivityInfo": "ConnectivityInfoTypeDef",
        "CurrentVersion": str,
    },
)

UpdateConnectivityResponseTypeDef = TypedDict(
    "UpdateConnectivityResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
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

_RequiredUpdateReplicationInfoRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateReplicationInfoRequestRequestTypeDef",
    {
        "CurrentVersion": str,
        "ReplicatorArn": str,
        "SourceKafkaClusterArn": str,
        "TargetKafkaClusterArn": str,
    },
)
_OptionalUpdateReplicationInfoRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateReplicationInfoRequestRequestTypeDef",
    {
        "ConsumerGroupReplication": "ConsumerGroupReplicationUpdateTypeDef",
        "TopicReplication": "TopicReplicationUpdateTypeDef",
    },
    total=False,
)

class UpdateReplicationInfoRequestRequestTypeDef(
    _RequiredUpdateReplicationInfoRequestRequestTypeDef,
    _OptionalUpdateReplicationInfoRequestRequestTypeDef,
):
    pass

UpdateReplicationInfoResponseTypeDef = TypedDict(
    "UpdateReplicationInfoResponseTypeDef",
    {
        "ReplicatorArn": str,
        "ReplicatorState": ReplicatorStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSecurityRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSecurityRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
    },
)
_OptionalUpdateSecurityRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSecurityRequestRequestTypeDef",
    {
        "ClientAuthentication": "ClientAuthenticationTypeDef",
        "EncryptionInfo": "EncryptionInfoTypeDef",
    },
    total=False,
)

class UpdateSecurityRequestRequestTypeDef(
    _RequiredUpdateSecurityRequestRequestTypeDef, _OptionalUpdateSecurityRequestRequestTypeDef
):
    pass

UpdateSecurityResponseTypeDef = TypedDict(
    "UpdateSecurityResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateStorageRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateStorageRequestRequestTypeDef",
    {
        "ClusterArn": str,
        "CurrentVersion": str,
    },
)
_OptionalUpdateStorageRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateStorageRequestRequestTypeDef",
    {
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
        "StorageMode": StorageModeType,
        "VolumeSizeGB": int,
    },
    total=False,
)

class UpdateStorageRequestRequestTypeDef(
    _RequiredUpdateStorageRequestRequestTypeDef, _OptionalUpdateStorageRequestRequestTypeDef
):
    pass

UpdateStorageResponseTypeDef = TypedDict(
    "UpdateStorageResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterOperationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserIdentityTypeDef = TypedDict(
    "UserIdentityTypeDef",
    {
        "Type": UserIdentityTypeType,
        "PrincipalId": str,
    },
    total=False,
)

_RequiredVpcConfigTypeDef = TypedDict(
    "_RequiredVpcConfigTypeDef",
    {
        "SubnetIds": List[str],
    },
)
_OptionalVpcConfigTypeDef = TypedDict(
    "_OptionalVpcConfigTypeDef",
    {
        "SecurityGroupIds": List[str],
    },
    total=False,
)

class VpcConfigTypeDef(_RequiredVpcConfigTypeDef, _OptionalVpcConfigTypeDef):
    pass

VpcConnectionInfoServerlessTypeDef = TypedDict(
    "VpcConnectionInfoServerlessTypeDef",
    {
        "CreationTime": datetime,
        "Owner": str,
        "UserIdentity": "UserIdentityTypeDef",
        "VpcConnectionArn": str,
    },
    total=False,
)

VpcConnectionInfoTypeDef = TypedDict(
    "VpcConnectionInfoTypeDef",
    {
        "VpcConnectionArn": str,
        "Owner": str,
        "UserIdentity": "UserIdentityTypeDef",
        "CreationTime": datetime,
    },
    total=False,
)

_RequiredVpcConnectionTypeDef = TypedDict(
    "_RequiredVpcConnectionTypeDef",
    {
        "VpcConnectionArn": str,
        "TargetClusterArn": str,
    },
)
_OptionalVpcConnectionTypeDef = TypedDict(
    "_OptionalVpcConnectionTypeDef",
    {
        "CreationTime": datetime,
        "Authentication": str,
        "VpcId": str,
        "State": VpcConnectionStateType,
    },
    total=False,
)

class VpcConnectionTypeDef(_RequiredVpcConnectionTypeDef, _OptionalVpcConnectionTypeDef):
    pass

VpcConnectivityClientAuthenticationTypeDef = TypedDict(
    "VpcConnectivityClientAuthenticationTypeDef",
    {
        "Sasl": "VpcConnectivitySaslTypeDef",
        "Tls": "VpcConnectivityTlsTypeDef",
    },
    total=False,
)

VpcConnectivityIamTypeDef = TypedDict(
    "VpcConnectivityIamTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

VpcConnectivitySaslTypeDef = TypedDict(
    "VpcConnectivitySaslTypeDef",
    {
        "Scram": "VpcConnectivityScramTypeDef",
        "Iam": "VpcConnectivityIamTypeDef",
    },
    total=False,
)

VpcConnectivityScramTypeDef = TypedDict(
    "VpcConnectivityScramTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

VpcConnectivityTlsTypeDef = TypedDict(
    "VpcConnectivityTlsTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

VpcConnectivityTypeDef = TypedDict(
    "VpcConnectivityTypeDef",
    {
        "ClientAuthentication": "VpcConnectivityClientAuthenticationTypeDef",
    },
    total=False,
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
