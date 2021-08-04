"""
Type annotations for elasticache service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/type_defs.html)

Usage::

    ```python
    from mypy_boto3_elasticache.type_defs import AddTagsToResourceMessageRequestTypeDef

    data: AddTagsToResourceMessageRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AuthenticationTypeType,
    AuthTokenUpdateStatusType,
    AuthTokenUpdateStrategyTypeType,
    AutomaticFailoverStatusType,
    AZModeType,
    ChangeTypeType,
    DestinationTypeType,
    LogDeliveryConfigurationStatusType,
    LogFormatType,
    MultiAZStatusType,
    NodeUpdateInitiatedByType,
    NodeUpdateStatusType,
    OutpostModeType,
    PendingAutomaticFailoverStatusType,
    ServiceUpdateSeverityType,
    ServiceUpdateStatusType,
    SlaMetType,
    SourceTypeType,
    UpdateActionStatusType,
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
    "AddTagsToResourceMessageRequestTypeDef",
    "AllowedNodeTypeModificationsMessageTypeDef",
    "AuthenticationTypeDef",
    "AuthorizeCacheSecurityGroupIngressMessageRequestTypeDef",
    "AuthorizeCacheSecurityGroupIngressResultTypeDef",
    "AvailabilityZoneTypeDef",
    "BatchApplyUpdateActionMessageRequestTypeDef",
    "BatchStopUpdateActionMessageRequestTypeDef",
    "CacheClusterMessageTypeDef",
    "CacheClusterTypeDef",
    "CacheEngineVersionMessageTypeDef",
    "CacheEngineVersionTypeDef",
    "CacheNodeTypeDef",
    "CacheNodeTypeSpecificParameterTypeDef",
    "CacheNodeTypeSpecificValueTypeDef",
    "CacheNodeUpdateStatusTypeDef",
    "CacheParameterGroupDetailsTypeDef",
    "CacheParameterGroupNameMessageTypeDef",
    "CacheParameterGroupStatusTypeDef",
    "CacheParameterGroupTypeDef",
    "CacheParameterGroupsMessageTypeDef",
    "CacheSecurityGroupMembershipTypeDef",
    "CacheSecurityGroupMessageTypeDef",
    "CacheSecurityGroupTypeDef",
    "CacheSubnetGroupMessageTypeDef",
    "CacheSubnetGroupTypeDef",
    "CloudWatchLogsDestinationDetailsTypeDef",
    "CompleteMigrationMessageRequestTypeDef",
    "CompleteMigrationResponseTypeDef",
    "ConfigureShardTypeDef",
    "CopySnapshotMessageRequestTypeDef",
    "CopySnapshotResultTypeDef",
    "CreateCacheClusterMessageRequestTypeDef",
    "CreateCacheClusterResultTypeDef",
    "CreateCacheParameterGroupMessageRequestTypeDef",
    "CreateCacheParameterGroupResultTypeDef",
    "CreateCacheSecurityGroupMessageRequestTypeDef",
    "CreateCacheSecurityGroupResultTypeDef",
    "CreateCacheSubnetGroupMessageRequestTypeDef",
    "CreateCacheSubnetGroupResultTypeDef",
    "CreateGlobalReplicationGroupMessageRequestTypeDef",
    "CreateGlobalReplicationGroupResultTypeDef",
    "CreateReplicationGroupMessageRequestTypeDef",
    "CreateReplicationGroupResultTypeDef",
    "CreateSnapshotMessageRequestTypeDef",
    "CreateSnapshotResultTypeDef",
    "CreateUserGroupMessageRequestTypeDef",
    "CreateUserMessageRequestTypeDef",
    "CustomerNodeEndpointTypeDef",
    "DecreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef",
    "DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef",
    "DecreaseReplicaCountMessageRequestTypeDef",
    "DecreaseReplicaCountResultTypeDef",
    "DeleteCacheClusterMessageRequestTypeDef",
    "DeleteCacheClusterResultTypeDef",
    "DeleteCacheParameterGroupMessageRequestTypeDef",
    "DeleteCacheSecurityGroupMessageRequestTypeDef",
    "DeleteCacheSubnetGroupMessageRequestTypeDef",
    "DeleteGlobalReplicationGroupMessageRequestTypeDef",
    "DeleteGlobalReplicationGroupResultTypeDef",
    "DeleteReplicationGroupMessageRequestTypeDef",
    "DeleteReplicationGroupResultTypeDef",
    "DeleteSnapshotMessageRequestTypeDef",
    "DeleteSnapshotResultTypeDef",
    "DeleteUserGroupMessageRequestTypeDef",
    "DeleteUserMessageRequestTypeDef",
    "DescribeCacheClustersMessageRequestTypeDef",
    "DescribeCacheEngineVersionsMessageRequestTypeDef",
    "DescribeCacheParameterGroupsMessageRequestTypeDef",
    "DescribeCacheParametersMessageRequestTypeDef",
    "DescribeCacheSecurityGroupsMessageRequestTypeDef",
    "DescribeCacheSubnetGroupsMessageRequestTypeDef",
    "DescribeEngineDefaultParametersMessageRequestTypeDef",
    "DescribeEngineDefaultParametersResultTypeDef",
    "DescribeEventsMessageRequestTypeDef",
    "DescribeGlobalReplicationGroupsMessageRequestTypeDef",
    "DescribeGlobalReplicationGroupsResultTypeDef",
    "DescribeReplicationGroupsMessageRequestTypeDef",
    "DescribeReservedCacheNodesMessageRequestTypeDef",
    "DescribeReservedCacheNodesOfferingsMessageRequestTypeDef",
    "DescribeServiceUpdatesMessageRequestTypeDef",
    "DescribeSnapshotsListMessageTypeDef",
    "DescribeSnapshotsMessageRequestTypeDef",
    "DescribeUpdateActionsMessageRequestTypeDef",
    "DescribeUserGroupsMessageRequestTypeDef",
    "DescribeUserGroupsResultTypeDef",
    "DescribeUsersMessageRequestTypeDef",
    "DescribeUsersResultTypeDef",
    "DestinationDetailsTypeDef",
    "DisassociateGlobalReplicationGroupMessageRequestTypeDef",
    "DisassociateGlobalReplicationGroupResultTypeDef",
    "EC2SecurityGroupTypeDef",
    "EndpointTypeDef",
    "EngineDefaultsTypeDef",
    "EventTypeDef",
    "EventsMessageTypeDef",
    "FailoverGlobalReplicationGroupMessageRequestTypeDef",
    "FailoverGlobalReplicationGroupResultTypeDef",
    "FilterTypeDef",
    "GlobalNodeGroupTypeDef",
    "GlobalReplicationGroupInfoTypeDef",
    "GlobalReplicationGroupMemberTypeDef",
    "GlobalReplicationGroupTypeDef",
    "IncreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef",
    "IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef",
    "IncreaseReplicaCountMessageRequestTypeDef",
    "IncreaseReplicaCountResultTypeDef",
    "KinesisFirehoseDestinationDetailsTypeDef",
    "ListAllowedNodeTypeModificationsMessageRequestTypeDef",
    "ListTagsForResourceMessageRequestTypeDef",
    "LogDeliveryConfigurationRequestTypeDef",
    "LogDeliveryConfigurationTypeDef",
    "ModifyCacheClusterMessageRequestTypeDef",
    "ModifyCacheClusterResultTypeDef",
    "ModifyCacheParameterGroupMessageRequestTypeDef",
    "ModifyCacheSubnetGroupMessageRequestTypeDef",
    "ModifyCacheSubnetGroupResultTypeDef",
    "ModifyGlobalReplicationGroupMessageRequestTypeDef",
    "ModifyGlobalReplicationGroupResultTypeDef",
    "ModifyReplicationGroupMessageRequestTypeDef",
    "ModifyReplicationGroupResultTypeDef",
    "ModifyReplicationGroupShardConfigurationMessageRequestTypeDef",
    "ModifyReplicationGroupShardConfigurationResultTypeDef",
    "ModifyUserGroupMessageRequestTypeDef",
    "ModifyUserMessageRequestTypeDef",
    "NodeGroupConfigurationTypeDef",
    "NodeGroupMemberTypeDef",
    "NodeGroupMemberUpdateStatusTypeDef",
    "NodeGroupTypeDef",
    "NodeGroupUpdateStatusTypeDef",
    "NodeSnapshotTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterNameValueTypeDef",
    "ParameterTypeDef",
    "PendingLogDeliveryConfigurationTypeDef",
    "PendingModifiedValuesTypeDef",
    "ProcessedUpdateActionTypeDef",
    "PurchaseReservedCacheNodesOfferingMessageRequestTypeDef",
    "PurchaseReservedCacheNodesOfferingResultTypeDef",
    "RebalanceSlotsInGlobalReplicationGroupMessageRequestTypeDef",
    "RebalanceSlotsInGlobalReplicationGroupResultTypeDef",
    "RebootCacheClusterMessageRequestTypeDef",
    "RebootCacheClusterResultTypeDef",
    "RecurringChargeTypeDef",
    "RegionalConfigurationTypeDef",
    "RemoveTagsFromResourceMessageRequestTypeDef",
    "ReplicationGroupMessageTypeDef",
    "ReplicationGroupPendingModifiedValuesTypeDef",
    "ReplicationGroupTypeDef",
    "ReservedCacheNodeMessageTypeDef",
    "ReservedCacheNodeTypeDef",
    "ReservedCacheNodesOfferingMessageTypeDef",
    "ReservedCacheNodesOfferingTypeDef",
    "ResetCacheParameterGroupMessageRequestTypeDef",
    "ReshardingConfigurationTypeDef",
    "ReshardingStatusTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeCacheSecurityGroupIngressMessageRequestTypeDef",
    "RevokeCacheSecurityGroupIngressResultTypeDef",
    "SecurityGroupMembershipTypeDef",
    "ServiceUpdateTypeDef",
    "ServiceUpdatesMessageTypeDef",
    "SlotMigrationTypeDef",
    "SnapshotTypeDef",
    "StartMigrationMessageRequestTypeDef",
    "StartMigrationResponseTypeDef",
    "SubnetOutpostTypeDef",
    "SubnetTypeDef",
    "TagListMessageTypeDef",
    "TagTypeDef",
    "TestFailoverMessageRequestTypeDef",
    "TestFailoverResultTypeDef",
    "TimeRangeFilterTypeDef",
    "UnprocessedUpdateActionTypeDef",
    "UpdateActionResultsMessageTypeDef",
    "UpdateActionTypeDef",
    "UpdateActionsMessageTypeDef",
    "UserGroupPendingChangesTypeDef",
    "UserGroupResponseMetadataTypeDef",
    "UserGroupTypeDef",
    "UserGroupsUpdateStatusTypeDef",
    "UserResponseMetadataTypeDef",
    "UserTypeDef",
    "WaiterConfigTypeDef",
)

AddTagsToResourceMessageRequestTypeDef = TypedDict(
    "AddTagsToResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
        "Tags": List["TagTypeDef"],
    },
)

AllowedNodeTypeModificationsMessageTypeDef = TypedDict(
    "AllowedNodeTypeModificationsMessageTypeDef",
    {
        "ScaleUpModifications": List[str],
        "ScaleDownModifications": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AuthenticationTypeDef = TypedDict(
    "AuthenticationTypeDef",
    {
        "Type": AuthenticationTypeType,
        "PasswordCount": int,
    },
    total=False,
)

AuthorizeCacheSecurityGroupIngressMessageRequestTypeDef = TypedDict(
    "AuthorizeCacheSecurityGroupIngressMessageRequestTypeDef",
    {
        "CacheSecurityGroupName": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
    },
)

AuthorizeCacheSecurityGroupIngressResultTypeDef = TypedDict(
    "AuthorizeCacheSecurityGroupIngressResultTypeDef",
    {
        "CacheSecurityGroup": "CacheSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": str,
    },
    total=False,
)

_RequiredBatchApplyUpdateActionMessageRequestTypeDef = TypedDict(
    "_RequiredBatchApplyUpdateActionMessageRequestTypeDef",
    {
        "ServiceUpdateName": str,
    },
)
_OptionalBatchApplyUpdateActionMessageRequestTypeDef = TypedDict(
    "_OptionalBatchApplyUpdateActionMessageRequestTypeDef",
    {
        "ReplicationGroupIds": List[str],
        "CacheClusterIds": List[str],
    },
    total=False,
)

class BatchApplyUpdateActionMessageRequestTypeDef(
    _RequiredBatchApplyUpdateActionMessageRequestTypeDef,
    _OptionalBatchApplyUpdateActionMessageRequestTypeDef,
):
    pass

_RequiredBatchStopUpdateActionMessageRequestTypeDef = TypedDict(
    "_RequiredBatchStopUpdateActionMessageRequestTypeDef",
    {
        "ServiceUpdateName": str,
    },
)
_OptionalBatchStopUpdateActionMessageRequestTypeDef = TypedDict(
    "_OptionalBatchStopUpdateActionMessageRequestTypeDef",
    {
        "ReplicationGroupIds": List[str],
        "CacheClusterIds": List[str],
    },
    total=False,
)

class BatchStopUpdateActionMessageRequestTypeDef(
    _RequiredBatchStopUpdateActionMessageRequestTypeDef,
    _OptionalBatchStopUpdateActionMessageRequestTypeDef,
):
    pass

CacheClusterMessageTypeDef = TypedDict(
    "CacheClusterMessageTypeDef",
    {
        "Marker": str,
        "CacheClusters": List["CacheClusterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CacheClusterTypeDef = TypedDict(
    "CacheClusterTypeDef",
    {
        "CacheClusterId": str,
        "ConfigurationEndpoint": "EndpointTypeDef",
        "ClientDownloadLandingPage": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheClusterStatus": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "PreferredOutpostArn": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": "PendingModifiedValuesTypeDef",
        "NotificationConfiguration": "NotificationConfigurationTypeDef",
        "CacheSecurityGroups": List["CacheSecurityGroupMembershipTypeDef"],
        "CacheParameterGroup": "CacheParameterGroupStatusTypeDef",
        "CacheSubnetGroupName": str,
        "CacheNodes": List["CacheNodeTypeDef"],
        "AutoMinorVersionUpgrade": bool,
        "SecurityGroups": List["SecurityGroupMembershipTypeDef"],
        "ReplicationGroupId": str,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "ARN": str,
        "ReplicationGroupLogDeliveryEnabled": bool,
        "LogDeliveryConfigurations": List["LogDeliveryConfigurationTypeDef"],
    },
    total=False,
)

CacheEngineVersionMessageTypeDef = TypedDict(
    "CacheEngineVersionMessageTypeDef",
    {
        "Marker": str,
        "CacheEngineVersions": List["CacheEngineVersionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CacheEngineVersionTypeDef = TypedDict(
    "CacheEngineVersionTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "CacheParameterGroupFamily": str,
        "CacheEngineDescription": str,
        "CacheEngineVersionDescription": str,
    },
    total=False,
)

CacheNodeTypeDef = TypedDict(
    "CacheNodeTypeDef",
    {
        "CacheNodeId": str,
        "CacheNodeStatus": str,
        "CacheNodeCreateTime": datetime,
        "Endpoint": "EndpointTypeDef",
        "ParameterGroupStatus": str,
        "SourceCacheNodeId": str,
        "CustomerAvailabilityZone": str,
        "CustomerOutpostArn": str,
    },
    total=False,
)

CacheNodeTypeSpecificParameterTypeDef = TypedDict(
    "CacheNodeTypeSpecificParameterTypeDef",
    {
        "ParameterName": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "CacheNodeTypeSpecificValues": List["CacheNodeTypeSpecificValueTypeDef"],
        "ChangeType": ChangeTypeType,
    },
    total=False,
)

CacheNodeTypeSpecificValueTypeDef = TypedDict(
    "CacheNodeTypeSpecificValueTypeDef",
    {
        "CacheNodeType": str,
        "Value": str,
    },
    total=False,
)

CacheNodeUpdateStatusTypeDef = TypedDict(
    "CacheNodeUpdateStatusTypeDef",
    {
        "CacheNodeId": str,
        "NodeUpdateStatus": NodeUpdateStatusType,
        "NodeDeletionDate": datetime,
        "NodeUpdateStartDate": datetime,
        "NodeUpdateEndDate": datetime,
        "NodeUpdateInitiatedBy": NodeUpdateInitiatedByType,
        "NodeUpdateInitiatedDate": datetime,
        "NodeUpdateStatusModifiedDate": datetime,
    },
    total=False,
)

CacheParameterGroupDetailsTypeDef = TypedDict(
    "CacheParameterGroupDetailsTypeDef",
    {
        "Marker": str,
        "Parameters": List["ParameterTypeDef"],
        "CacheNodeTypeSpecificParameters": List["CacheNodeTypeSpecificParameterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CacheParameterGroupNameMessageTypeDef = TypedDict(
    "CacheParameterGroupNameMessageTypeDef",
    {
        "CacheParameterGroupName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CacheParameterGroupStatusTypeDef = TypedDict(
    "CacheParameterGroupStatusTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)

CacheParameterGroupTypeDef = TypedDict(
    "CacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "CacheParameterGroupFamily": str,
        "Description": str,
        "IsGlobal": bool,
        "ARN": str,
    },
    total=False,
)

CacheParameterGroupsMessageTypeDef = TypedDict(
    "CacheParameterGroupsMessageTypeDef",
    {
        "Marker": str,
        "CacheParameterGroups": List["CacheParameterGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CacheSecurityGroupMembershipTypeDef = TypedDict(
    "CacheSecurityGroupMembershipTypeDef",
    {
        "CacheSecurityGroupName": str,
        "Status": str,
    },
    total=False,
)

CacheSecurityGroupMessageTypeDef = TypedDict(
    "CacheSecurityGroupMessageTypeDef",
    {
        "Marker": str,
        "CacheSecurityGroups": List["CacheSecurityGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CacheSecurityGroupTypeDef = TypedDict(
    "CacheSecurityGroupTypeDef",
    {
        "OwnerId": str,
        "CacheSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List["EC2SecurityGroupTypeDef"],
        "ARN": str,
    },
    total=False,
)

CacheSubnetGroupMessageTypeDef = TypedDict(
    "CacheSubnetGroupMessageTypeDef",
    {
        "Marker": str,
        "CacheSubnetGroups": List["CacheSubnetGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CacheSubnetGroupTypeDef = TypedDict(
    "CacheSubnetGroupTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": str,
        "VpcId": str,
        "Subnets": List["SubnetTypeDef"],
        "ARN": str,
    },
    total=False,
)

CloudWatchLogsDestinationDetailsTypeDef = TypedDict(
    "CloudWatchLogsDestinationDetailsTypeDef",
    {
        "LogGroup": str,
    },
    total=False,
)

_RequiredCompleteMigrationMessageRequestTypeDef = TypedDict(
    "_RequiredCompleteMigrationMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
    },
)
_OptionalCompleteMigrationMessageRequestTypeDef = TypedDict(
    "_OptionalCompleteMigrationMessageRequestTypeDef",
    {
        "Force": bool,
    },
    total=False,
)

class CompleteMigrationMessageRequestTypeDef(
    _RequiredCompleteMigrationMessageRequestTypeDef, _OptionalCompleteMigrationMessageRequestTypeDef
):
    pass

CompleteMigrationResponseTypeDef = TypedDict(
    "CompleteMigrationResponseTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredConfigureShardTypeDef = TypedDict(
    "_RequiredConfigureShardTypeDef",
    {
        "NodeGroupId": str,
        "NewReplicaCount": int,
    },
)
_OptionalConfigureShardTypeDef = TypedDict(
    "_OptionalConfigureShardTypeDef",
    {
        "PreferredAvailabilityZones": List[str],
        "PreferredOutpostArns": List[str],
    },
    total=False,
)

class ConfigureShardTypeDef(_RequiredConfigureShardTypeDef, _OptionalConfigureShardTypeDef):
    pass

_RequiredCopySnapshotMessageRequestTypeDef = TypedDict(
    "_RequiredCopySnapshotMessageRequestTypeDef",
    {
        "SourceSnapshotName": str,
        "TargetSnapshotName": str,
    },
)
_OptionalCopySnapshotMessageRequestTypeDef = TypedDict(
    "_OptionalCopySnapshotMessageRequestTypeDef",
    {
        "TargetBucket": str,
        "KmsKeyId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CopySnapshotMessageRequestTypeDef(
    _RequiredCopySnapshotMessageRequestTypeDef, _OptionalCopySnapshotMessageRequestTypeDef
):
    pass

CopySnapshotResultTypeDef = TypedDict(
    "CopySnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCacheClusterMessageRequestTypeDef = TypedDict(
    "_RequiredCreateCacheClusterMessageRequestTypeDef",
    {
        "CacheClusterId": str,
    },
)
_OptionalCreateCacheClusterMessageRequestTypeDef = TypedDict(
    "_OptionalCreateCacheClusterMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "AZMode": AZModeType,
        "PreferredAvailabilityZone": str,
        "PreferredAvailabilityZones": List[str],
        "NumCacheNodes": int,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheParameterGroupName": str,
        "CacheSubnetGroupName": str,
        "CacheSecurityGroupNames": List[str],
        "SecurityGroupIds": List[str],
        "Tags": List["TagTypeDef"],
        "SnapshotArns": List[str],
        "SnapshotName": str,
        "PreferredMaintenanceWindow": str,
        "Port": int,
        "NotificationTopicArn": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthToken": str,
        "OutpostMode": OutpostModeType,
        "PreferredOutpostArn": str,
        "PreferredOutpostArns": List[str],
        "LogDeliveryConfigurations": List["LogDeliveryConfigurationRequestTypeDef"],
    },
    total=False,
)

class CreateCacheClusterMessageRequestTypeDef(
    _RequiredCreateCacheClusterMessageRequestTypeDef,
    _OptionalCreateCacheClusterMessageRequestTypeDef,
):
    pass

CreateCacheClusterResultTypeDef = TypedDict(
    "CreateCacheClusterResultTypeDef",
    {
        "CacheCluster": "CacheClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCacheParameterGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCreateCacheParameterGroupMessageRequestTypeDef",
    {
        "CacheParameterGroupName": str,
        "CacheParameterGroupFamily": str,
        "Description": str,
    },
)
_OptionalCreateCacheParameterGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCreateCacheParameterGroupMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateCacheParameterGroupMessageRequestTypeDef(
    _RequiredCreateCacheParameterGroupMessageRequestTypeDef,
    _OptionalCreateCacheParameterGroupMessageRequestTypeDef,
):
    pass

CreateCacheParameterGroupResultTypeDef = TypedDict(
    "CreateCacheParameterGroupResultTypeDef",
    {
        "CacheParameterGroup": "CacheParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCacheSecurityGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCreateCacheSecurityGroupMessageRequestTypeDef",
    {
        "CacheSecurityGroupName": str,
        "Description": str,
    },
)
_OptionalCreateCacheSecurityGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCreateCacheSecurityGroupMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateCacheSecurityGroupMessageRequestTypeDef(
    _RequiredCreateCacheSecurityGroupMessageRequestTypeDef,
    _OptionalCreateCacheSecurityGroupMessageRequestTypeDef,
):
    pass

CreateCacheSecurityGroupResultTypeDef = TypedDict(
    "CreateCacheSecurityGroupResultTypeDef",
    {
        "CacheSecurityGroup": "CacheSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCacheSubnetGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCreateCacheSubnetGroupMessageRequestTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": str,
        "SubnetIds": List[str],
    },
)
_OptionalCreateCacheSubnetGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCreateCacheSubnetGroupMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateCacheSubnetGroupMessageRequestTypeDef(
    _RequiredCreateCacheSubnetGroupMessageRequestTypeDef,
    _OptionalCreateCacheSubnetGroupMessageRequestTypeDef,
):
    pass

CreateCacheSubnetGroupResultTypeDef = TypedDict(
    "CreateCacheSubnetGroupResultTypeDef",
    {
        "CacheSubnetGroup": "CacheSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCreateGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupIdSuffix": str,
        "PrimaryReplicationGroupId": str,
    },
)
_OptionalCreateGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCreateGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupDescription": str,
    },
    total=False,
)

class CreateGlobalReplicationGroupMessageRequestTypeDef(
    _RequiredCreateGlobalReplicationGroupMessageRequestTypeDef,
    _OptionalCreateGlobalReplicationGroupMessageRequestTypeDef,
):
    pass

CreateGlobalReplicationGroupResultTypeDef = TypedDict(
    "CreateGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReplicationGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCreateReplicationGroupMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "ReplicationGroupDescription": str,
    },
)
_OptionalCreateReplicationGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCreateReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "PrimaryClusterId": str,
        "AutomaticFailoverEnabled": bool,
        "MultiAZEnabled": bool,
        "NumCacheClusters": int,
        "PreferredCacheClusterAZs": List[str],
        "NumNodeGroups": int,
        "ReplicasPerNodeGroup": int,
        "NodeGroupConfiguration": List["NodeGroupConfigurationTypeDef"],
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheParameterGroupName": str,
        "CacheSubnetGroupName": str,
        "CacheSecurityGroupNames": List[str],
        "SecurityGroupIds": List[str],
        "Tags": List["TagTypeDef"],
        "SnapshotArns": List[str],
        "SnapshotName": str,
        "PreferredMaintenanceWindow": str,
        "Port": int,
        "NotificationTopicArn": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthToken": str,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
        "UserGroupIds": List[str],
        "LogDeliveryConfigurations": List["LogDeliveryConfigurationRequestTypeDef"],
    },
    total=False,
)

class CreateReplicationGroupMessageRequestTypeDef(
    _RequiredCreateReplicationGroupMessageRequestTypeDef,
    _OptionalCreateReplicationGroupMessageRequestTypeDef,
):
    pass

CreateReplicationGroupResultTypeDef = TypedDict(
    "CreateReplicationGroupResultTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSnapshotMessageRequestTypeDef = TypedDict(
    "_RequiredCreateSnapshotMessageRequestTypeDef",
    {
        "SnapshotName": str,
    },
)
_OptionalCreateSnapshotMessageRequestTypeDef = TypedDict(
    "_OptionalCreateSnapshotMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "KmsKeyId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateSnapshotMessageRequestTypeDef(
    _RequiredCreateSnapshotMessageRequestTypeDef, _OptionalCreateSnapshotMessageRequestTypeDef
):
    pass

CreateSnapshotResultTypeDef = TypedDict(
    "CreateSnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCreateUserGroupMessageRequestTypeDef",
    {
        "UserGroupId": str,
        "Engine": str,
    },
)
_OptionalCreateUserGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCreateUserGroupMessageRequestTypeDef",
    {
        "UserIds": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateUserGroupMessageRequestTypeDef(
    _RequiredCreateUserGroupMessageRequestTypeDef, _OptionalCreateUserGroupMessageRequestTypeDef
):
    pass

_RequiredCreateUserMessageRequestTypeDef = TypedDict(
    "_RequiredCreateUserMessageRequestTypeDef",
    {
        "UserId": str,
        "UserName": str,
        "Engine": str,
        "AccessString": str,
    },
)
_OptionalCreateUserMessageRequestTypeDef = TypedDict(
    "_OptionalCreateUserMessageRequestTypeDef",
    {
        "Passwords": List[str],
        "NoPasswordRequired": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateUserMessageRequestTypeDef(
    _RequiredCreateUserMessageRequestTypeDef, _OptionalCreateUserMessageRequestTypeDef
):
    pass

CustomerNodeEndpointTypeDef = TypedDict(
    "CustomerNodeEndpointTypeDef",
    {
        "Address": str,
        "Port": int,
    },
    total=False,
)

_RequiredDecreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "_RequiredDecreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "NodeGroupCount": int,
        "ApplyImmediately": bool,
    },
)
_OptionalDecreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "_OptionalDecreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalNodeGroupsToRemove": List[str],
        "GlobalNodeGroupsToRetain": List[str],
    },
    total=False,
)

class DecreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef(
    _RequiredDecreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef,
    _OptionalDecreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef,
):
    pass

DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef = TypedDict(
    "DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDecreaseReplicaCountMessageRequestTypeDef = TypedDict(
    "_RequiredDecreaseReplicaCountMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "ApplyImmediately": bool,
    },
)
_OptionalDecreaseReplicaCountMessageRequestTypeDef = TypedDict(
    "_OptionalDecreaseReplicaCountMessageRequestTypeDef",
    {
        "NewReplicaCount": int,
        "ReplicaConfiguration": List["ConfigureShardTypeDef"],
        "ReplicasToRemove": List[str],
    },
    total=False,
)

class DecreaseReplicaCountMessageRequestTypeDef(
    _RequiredDecreaseReplicaCountMessageRequestTypeDef,
    _OptionalDecreaseReplicaCountMessageRequestTypeDef,
):
    pass

DecreaseReplicaCountResultTypeDef = TypedDict(
    "DecreaseReplicaCountResultTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteCacheClusterMessageRequestTypeDef = TypedDict(
    "_RequiredDeleteCacheClusterMessageRequestTypeDef",
    {
        "CacheClusterId": str,
    },
)
_OptionalDeleteCacheClusterMessageRequestTypeDef = TypedDict(
    "_OptionalDeleteCacheClusterMessageRequestTypeDef",
    {
        "FinalSnapshotIdentifier": str,
    },
    total=False,
)

class DeleteCacheClusterMessageRequestTypeDef(
    _RequiredDeleteCacheClusterMessageRequestTypeDef,
    _OptionalDeleteCacheClusterMessageRequestTypeDef,
):
    pass

DeleteCacheClusterResultTypeDef = TypedDict(
    "DeleteCacheClusterResultTypeDef",
    {
        "CacheCluster": "CacheClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCacheParameterGroupMessageRequestTypeDef = TypedDict(
    "DeleteCacheParameterGroupMessageRequestTypeDef",
    {
        "CacheParameterGroupName": str,
    },
)

DeleteCacheSecurityGroupMessageRequestTypeDef = TypedDict(
    "DeleteCacheSecurityGroupMessageRequestTypeDef",
    {
        "CacheSecurityGroupName": str,
    },
)

DeleteCacheSubnetGroupMessageRequestTypeDef = TypedDict(
    "DeleteCacheSubnetGroupMessageRequestTypeDef",
    {
        "CacheSubnetGroupName": str,
    },
)

DeleteGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "DeleteGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "RetainPrimaryReplicationGroup": bool,
    },
)

DeleteGlobalReplicationGroupResultTypeDef = TypedDict(
    "DeleteGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteReplicationGroupMessageRequestTypeDef = TypedDict(
    "_RequiredDeleteReplicationGroupMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
    },
)
_OptionalDeleteReplicationGroupMessageRequestTypeDef = TypedDict(
    "_OptionalDeleteReplicationGroupMessageRequestTypeDef",
    {
        "RetainPrimaryCluster": bool,
        "FinalSnapshotIdentifier": str,
    },
    total=False,
)

class DeleteReplicationGroupMessageRequestTypeDef(
    _RequiredDeleteReplicationGroupMessageRequestTypeDef,
    _OptionalDeleteReplicationGroupMessageRequestTypeDef,
):
    pass

DeleteReplicationGroupResultTypeDef = TypedDict(
    "DeleteReplicationGroupResultTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSnapshotMessageRequestTypeDef = TypedDict(
    "DeleteSnapshotMessageRequestTypeDef",
    {
        "SnapshotName": str,
    },
)

DeleteSnapshotResultTypeDef = TypedDict(
    "DeleteSnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteUserGroupMessageRequestTypeDef = TypedDict(
    "DeleteUserGroupMessageRequestTypeDef",
    {
        "UserGroupId": str,
    },
)

DeleteUserMessageRequestTypeDef = TypedDict(
    "DeleteUserMessageRequestTypeDef",
    {
        "UserId": str,
    },
)

DescribeCacheClustersMessageRequestTypeDef = TypedDict(
    "DescribeCacheClustersMessageRequestTypeDef",
    {
        "CacheClusterId": str,
        "MaxRecords": int,
        "Marker": str,
        "ShowCacheNodeInfo": bool,
        "ShowCacheClustersNotInReplicationGroups": bool,
    },
    total=False,
)

DescribeCacheEngineVersionsMessageRequestTypeDef = TypedDict(
    "DescribeCacheEngineVersionsMessageRequestTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "CacheParameterGroupFamily": str,
        "MaxRecords": int,
        "Marker": str,
        "DefaultOnly": bool,
    },
    total=False,
)

DescribeCacheParameterGroupsMessageRequestTypeDef = TypedDict(
    "DescribeCacheParameterGroupsMessageRequestTypeDef",
    {
        "CacheParameterGroupName": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

_RequiredDescribeCacheParametersMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeCacheParametersMessageRequestTypeDef",
    {
        "CacheParameterGroupName": str,
    },
)
_OptionalDescribeCacheParametersMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeCacheParametersMessageRequestTypeDef",
    {
        "Source": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class DescribeCacheParametersMessageRequestTypeDef(
    _RequiredDescribeCacheParametersMessageRequestTypeDef,
    _OptionalDescribeCacheParametersMessageRequestTypeDef,
):
    pass

DescribeCacheSecurityGroupsMessageRequestTypeDef = TypedDict(
    "DescribeCacheSecurityGroupsMessageRequestTypeDef",
    {
        "CacheSecurityGroupName": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeCacheSubnetGroupsMessageRequestTypeDef = TypedDict(
    "DescribeCacheSubnetGroupsMessageRequestTypeDef",
    {
        "CacheSubnetGroupName": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

_RequiredDescribeEngineDefaultParametersMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeEngineDefaultParametersMessageRequestTypeDef",
    {
        "CacheParameterGroupFamily": str,
    },
)
_OptionalDescribeEngineDefaultParametersMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeEngineDefaultParametersMessageRequestTypeDef",
    {
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class DescribeEngineDefaultParametersMessageRequestTypeDef(
    _RequiredDescribeEngineDefaultParametersMessageRequestTypeDef,
    _OptionalDescribeEngineDefaultParametersMessageRequestTypeDef,
):
    pass

DescribeEngineDefaultParametersResultTypeDef = TypedDict(
    "DescribeEngineDefaultParametersResultTypeDef",
    {
        "EngineDefaults": "EngineDefaultsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventsMessageRequestTypeDef = TypedDict(
    "DescribeEventsMessageRequestTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": SourceTypeType,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Duration": int,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeGlobalReplicationGroupsMessageRequestTypeDef = TypedDict(
    "DescribeGlobalReplicationGroupsMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "MaxRecords": int,
        "Marker": str,
        "ShowMemberInfo": bool,
    },
    total=False,
)

DescribeGlobalReplicationGroupsResultTypeDef = TypedDict(
    "DescribeGlobalReplicationGroupsResultTypeDef",
    {
        "Marker": str,
        "GlobalReplicationGroups": List["GlobalReplicationGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationGroupsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationGroupsMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReservedCacheNodesMessageRequestTypeDef = TypedDict(
    "DescribeReservedCacheNodesMessageRequestTypeDef",
    {
        "ReservedCacheNodeId": str,
        "ReservedCacheNodesOfferingId": str,
        "CacheNodeType": str,
        "Duration": str,
        "ProductDescription": str,
        "OfferingType": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReservedCacheNodesOfferingsMessageRequestTypeDef = TypedDict(
    "DescribeReservedCacheNodesOfferingsMessageRequestTypeDef",
    {
        "ReservedCacheNodesOfferingId": str,
        "CacheNodeType": str,
        "Duration": str,
        "ProductDescription": str,
        "OfferingType": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeServiceUpdatesMessageRequestTypeDef = TypedDict(
    "DescribeServiceUpdatesMessageRequestTypeDef",
    {
        "ServiceUpdateName": str,
        "ServiceUpdateStatus": List[ServiceUpdateStatusType],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeSnapshotsListMessageTypeDef = TypedDict(
    "DescribeSnapshotsListMessageTypeDef",
    {
        "Marker": str,
        "Snapshots": List["SnapshotTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSnapshotsMessageRequestTypeDef = TypedDict(
    "DescribeSnapshotsMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "SnapshotName": str,
        "SnapshotSource": str,
        "Marker": str,
        "MaxRecords": int,
        "ShowNodeGroupConfig": bool,
    },
    total=False,
)

DescribeUpdateActionsMessageRequestTypeDef = TypedDict(
    "DescribeUpdateActionsMessageRequestTypeDef",
    {
        "ServiceUpdateName": str,
        "ReplicationGroupIds": List[str],
        "CacheClusterIds": List[str],
        "Engine": str,
        "ServiceUpdateStatus": List[ServiceUpdateStatusType],
        "ServiceUpdateTimeRange": "TimeRangeFilterTypeDef",
        "UpdateActionStatus": List[UpdateActionStatusType],
        "ShowNodeLevelUpdateStatus": bool,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeUserGroupsMessageRequestTypeDef = TypedDict(
    "DescribeUserGroupsMessageRequestTypeDef",
    {
        "UserGroupId": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeUserGroupsResultTypeDef = TypedDict(
    "DescribeUserGroupsResultTypeDef",
    {
        "UserGroups": List["UserGroupTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUsersMessageRequestTypeDef = TypedDict(
    "DescribeUsersMessageRequestTypeDef",
    {
        "Engine": str,
        "UserId": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeUsersResultTypeDef = TypedDict(
    "DescribeUsersResultTypeDef",
    {
        "Users": List["UserTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationDetailsTypeDef = TypedDict(
    "DestinationDetailsTypeDef",
    {
        "CloudWatchLogsDetails": "CloudWatchLogsDestinationDetailsTypeDef",
        "KinesisFirehoseDetails": "KinesisFirehoseDestinationDetailsTypeDef",
    },
    total=False,
)

DisassociateGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "DisassociateGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "ReplicationGroupId": str,
        "ReplicationGroupRegion": str,
    },
)

DisassociateGlobalReplicationGroupResultTypeDef = TypedDict(
    "DisassociateGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EC2SecurityGroupTypeDef = TypedDict(
    "EC2SecurityGroupTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
    },
    total=False,
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "Port": int,
    },
    total=False,
)

EngineDefaultsTypeDef = TypedDict(
    "EngineDefaultsTypeDef",
    {
        "CacheParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List["ParameterTypeDef"],
        "CacheNodeTypeSpecificParameters": List["CacheNodeTypeSpecificParameterTypeDef"],
    },
    total=False,
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": SourceTypeType,
        "Message": str,
        "Date": datetime,
    },
    total=False,
)

EventsMessageTypeDef = TypedDict(
    "EventsMessageTypeDef",
    {
        "Marker": str,
        "Events": List["EventTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailoverGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "FailoverGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "PrimaryRegion": str,
        "PrimaryReplicationGroupId": str,
    },
)

FailoverGlobalReplicationGroupResultTypeDef = TypedDict(
    "FailoverGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
)

GlobalNodeGroupTypeDef = TypedDict(
    "GlobalNodeGroupTypeDef",
    {
        "GlobalNodeGroupId": str,
        "Slots": str,
    },
    total=False,
)

GlobalReplicationGroupInfoTypeDef = TypedDict(
    "GlobalReplicationGroupInfoTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "GlobalReplicationGroupMemberRole": str,
    },
    total=False,
)

GlobalReplicationGroupMemberTypeDef = TypedDict(
    "GlobalReplicationGroupMemberTypeDef",
    {
        "ReplicationGroupId": str,
        "ReplicationGroupRegion": str,
        "Role": str,
        "AutomaticFailover": AutomaticFailoverStatusType,
        "Status": str,
    },
    total=False,
)

GlobalReplicationGroupTypeDef = TypedDict(
    "GlobalReplicationGroupTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "GlobalReplicationGroupDescription": str,
        "Status": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "Members": List["GlobalReplicationGroupMemberTypeDef"],
        "ClusterEnabled": bool,
        "GlobalNodeGroups": List["GlobalNodeGroupTypeDef"],
        "AuthTokenEnabled": bool,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "ARN": str,
    },
    total=False,
)

_RequiredIncreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "_RequiredIncreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "NodeGroupCount": int,
        "ApplyImmediately": bool,
    },
)
_OptionalIncreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "_OptionalIncreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef",
    {
        "RegionalConfigurations": List["RegionalConfigurationTypeDef"],
    },
    total=False,
)

class IncreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef(
    _RequiredIncreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef,
    _OptionalIncreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef,
):
    pass

IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef = TypedDict(
    "IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredIncreaseReplicaCountMessageRequestTypeDef = TypedDict(
    "_RequiredIncreaseReplicaCountMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "ApplyImmediately": bool,
    },
)
_OptionalIncreaseReplicaCountMessageRequestTypeDef = TypedDict(
    "_OptionalIncreaseReplicaCountMessageRequestTypeDef",
    {
        "NewReplicaCount": int,
        "ReplicaConfiguration": List["ConfigureShardTypeDef"],
    },
    total=False,
)

class IncreaseReplicaCountMessageRequestTypeDef(
    _RequiredIncreaseReplicaCountMessageRequestTypeDef,
    _OptionalIncreaseReplicaCountMessageRequestTypeDef,
):
    pass

IncreaseReplicaCountResultTypeDef = TypedDict(
    "IncreaseReplicaCountResultTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KinesisFirehoseDestinationDetailsTypeDef = TypedDict(
    "KinesisFirehoseDestinationDetailsTypeDef",
    {
        "DeliveryStream": str,
    },
    total=False,
)

ListAllowedNodeTypeModificationsMessageRequestTypeDef = TypedDict(
    "ListAllowedNodeTypeModificationsMessageRequestTypeDef",
    {
        "CacheClusterId": str,
        "ReplicationGroupId": str,
    },
    total=False,
)

ListTagsForResourceMessageRequestTypeDef = TypedDict(
    "ListTagsForResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
    },
)

LogDeliveryConfigurationRequestTypeDef = TypedDict(
    "LogDeliveryConfigurationRequestTypeDef",
    {
        "LogType": Literal["slow-log"],
        "DestinationType": DestinationTypeType,
        "DestinationDetails": "DestinationDetailsTypeDef",
        "LogFormat": LogFormatType,
        "Enabled": bool,
    },
    total=False,
)

LogDeliveryConfigurationTypeDef = TypedDict(
    "LogDeliveryConfigurationTypeDef",
    {
        "LogType": Literal["slow-log"],
        "DestinationType": DestinationTypeType,
        "DestinationDetails": "DestinationDetailsTypeDef",
        "LogFormat": LogFormatType,
        "Status": LogDeliveryConfigurationStatusType,
        "Message": str,
    },
    total=False,
)

_RequiredModifyCacheClusterMessageRequestTypeDef = TypedDict(
    "_RequiredModifyCacheClusterMessageRequestTypeDef",
    {
        "CacheClusterId": str,
    },
)
_OptionalModifyCacheClusterMessageRequestTypeDef = TypedDict(
    "_OptionalModifyCacheClusterMessageRequestTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "AZMode": AZModeType,
        "NewAvailabilityZones": List[str],
        "CacheSecurityGroupNames": List[str],
        "SecurityGroupIds": List[str],
        "PreferredMaintenanceWindow": str,
        "NotificationTopicArn": str,
        "CacheParameterGroupName": str,
        "NotificationTopicStatus": str,
        "ApplyImmediately": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "CacheNodeType": str,
        "AuthToken": str,
        "AuthTokenUpdateStrategy": AuthTokenUpdateStrategyTypeType,
        "LogDeliveryConfigurations": List["LogDeliveryConfigurationRequestTypeDef"],
    },
    total=False,
)

class ModifyCacheClusterMessageRequestTypeDef(
    _RequiredModifyCacheClusterMessageRequestTypeDef,
    _OptionalModifyCacheClusterMessageRequestTypeDef,
):
    pass

ModifyCacheClusterResultTypeDef = TypedDict(
    "ModifyCacheClusterResultTypeDef",
    {
        "CacheCluster": "CacheClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyCacheParameterGroupMessageRequestTypeDef = TypedDict(
    "ModifyCacheParameterGroupMessageRequestTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterNameValues": List["ParameterNameValueTypeDef"],
    },
)

_RequiredModifyCacheSubnetGroupMessageRequestTypeDef = TypedDict(
    "_RequiredModifyCacheSubnetGroupMessageRequestTypeDef",
    {
        "CacheSubnetGroupName": str,
    },
)
_OptionalModifyCacheSubnetGroupMessageRequestTypeDef = TypedDict(
    "_OptionalModifyCacheSubnetGroupMessageRequestTypeDef",
    {
        "CacheSubnetGroupDescription": str,
        "SubnetIds": List[str],
    },
    total=False,
)

class ModifyCacheSubnetGroupMessageRequestTypeDef(
    _RequiredModifyCacheSubnetGroupMessageRequestTypeDef,
    _OptionalModifyCacheSubnetGroupMessageRequestTypeDef,
):
    pass

ModifyCacheSubnetGroupResultTypeDef = TypedDict(
    "ModifyCacheSubnetGroupResultTypeDef",
    {
        "CacheSubnetGroup": "CacheSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "_RequiredModifyGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "ApplyImmediately": bool,
    },
)
_OptionalModifyGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "_OptionalModifyGlobalReplicationGroupMessageRequestTypeDef",
    {
        "CacheNodeType": str,
        "EngineVersion": str,
        "CacheParameterGroupName": str,
        "GlobalReplicationGroupDescription": str,
        "AutomaticFailoverEnabled": bool,
    },
    total=False,
)

class ModifyGlobalReplicationGroupMessageRequestTypeDef(
    _RequiredModifyGlobalReplicationGroupMessageRequestTypeDef,
    _OptionalModifyGlobalReplicationGroupMessageRequestTypeDef,
):
    pass

ModifyGlobalReplicationGroupResultTypeDef = TypedDict(
    "ModifyGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyReplicationGroupMessageRequestTypeDef = TypedDict(
    "_RequiredModifyReplicationGroupMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
    },
)
_OptionalModifyReplicationGroupMessageRequestTypeDef = TypedDict(
    "_OptionalModifyReplicationGroupMessageRequestTypeDef",
    {
        "ReplicationGroupDescription": str,
        "PrimaryClusterId": str,
        "SnapshottingClusterId": str,
        "AutomaticFailoverEnabled": bool,
        "MultiAZEnabled": bool,
        "NodeGroupId": str,
        "CacheSecurityGroupNames": List[str],
        "SecurityGroupIds": List[str],
        "PreferredMaintenanceWindow": str,
        "NotificationTopicArn": str,
        "CacheParameterGroupName": str,
        "NotificationTopicStatus": str,
        "ApplyImmediately": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "CacheNodeType": str,
        "AuthToken": str,
        "AuthTokenUpdateStrategy": AuthTokenUpdateStrategyTypeType,
        "UserGroupIdsToAdd": List[str],
        "UserGroupIdsToRemove": List[str],
        "RemoveUserGroups": bool,
        "LogDeliveryConfigurations": List["LogDeliveryConfigurationRequestTypeDef"],
    },
    total=False,
)

class ModifyReplicationGroupMessageRequestTypeDef(
    _RequiredModifyReplicationGroupMessageRequestTypeDef,
    _OptionalModifyReplicationGroupMessageRequestTypeDef,
):
    pass

ModifyReplicationGroupResultTypeDef = TypedDict(
    "ModifyReplicationGroupResultTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyReplicationGroupShardConfigurationMessageRequestTypeDef = TypedDict(
    "_RequiredModifyReplicationGroupShardConfigurationMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "NodeGroupCount": int,
        "ApplyImmediately": bool,
    },
)
_OptionalModifyReplicationGroupShardConfigurationMessageRequestTypeDef = TypedDict(
    "_OptionalModifyReplicationGroupShardConfigurationMessageRequestTypeDef",
    {
        "ReshardingConfiguration": List["ReshardingConfigurationTypeDef"],
        "NodeGroupsToRemove": List[str],
        "NodeGroupsToRetain": List[str],
    },
    total=False,
)

class ModifyReplicationGroupShardConfigurationMessageRequestTypeDef(
    _RequiredModifyReplicationGroupShardConfigurationMessageRequestTypeDef,
    _OptionalModifyReplicationGroupShardConfigurationMessageRequestTypeDef,
):
    pass

ModifyReplicationGroupShardConfigurationResultTypeDef = TypedDict(
    "ModifyReplicationGroupShardConfigurationResultTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyUserGroupMessageRequestTypeDef = TypedDict(
    "_RequiredModifyUserGroupMessageRequestTypeDef",
    {
        "UserGroupId": str,
    },
)
_OptionalModifyUserGroupMessageRequestTypeDef = TypedDict(
    "_OptionalModifyUserGroupMessageRequestTypeDef",
    {
        "UserIdsToAdd": List[str],
        "UserIdsToRemove": List[str],
    },
    total=False,
)

class ModifyUserGroupMessageRequestTypeDef(
    _RequiredModifyUserGroupMessageRequestTypeDef, _OptionalModifyUserGroupMessageRequestTypeDef
):
    pass

_RequiredModifyUserMessageRequestTypeDef = TypedDict(
    "_RequiredModifyUserMessageRequestTypeDef",
    {
        "UserId": str,
    },
)
_OptionalModifyUserMessageRequestTypeDef = TypedDict(
    "_OptionalModifyUserMessageRequestTypeDef",
    {
        "AccessString": str,
        "AppendAccessString": str,
        "Passwords": List[str],
        "NoPasswordRequired": bool,
    },
    total=False,
)

class ModifyUserMessageRequestTypeDef(
    _RequiredModifyUserMessageRequestTypeDef, _OptionalModifyUserMessageRequestTypeDef
):
    pass

NodeGroupConfigurationTypeDef = TypedDict(
    "NodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
        "PrimaryOutpostArn": str,
        "ReplicaOutpostArns": List[str],
    },
    total=False,
)

NodeGroupMemberTypeDef = TypedDict(
    "NodeGroupMemberTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": "EndpointTypeDef",
        "PreferredAvailabilityZone": str,
        "PreferredOutpostArn": str,
        "CurrentRole": str,
    },
    total=False,
)

NodeGroupMemberUpdateStatusTypeDef = TypedDict(
    "NodeGroupMemberUpdateStatusTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "NodeUpdateStatus": NodeUpdateStatusType,
        "NodeDeletionDate": datetime,
        "NodeUpdateStartDate": datetime,
        "NodeUpdateEndDate": datetime,
        "NodeUpdateInitiatedBy": NodeUpdateInitiatedByType,
        "NodeUpdateInitiatedDate": datetime,
        "NodeUpdateStatusModifiedDate": datetime,
    },
    total=False,
)

NodeGroupTypeDef = TypedDict(
    "NodeGroupTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": "EndpointTypeDef",
        "ReaderEndpoint": "EndpointTypeDef",
        "Slots": str,
        "NodeGroupMembers": List["NodeGroupMemberTypeDef"],
    },
    total=False,
)

NodeGroupUpdateStatusTypeDef = TypedDict(
    "NodeGroupUpdateStatusTypeDef",
    {
        "NodeGroupId": str,
        "NodeGroupMemberUpdateStatus": List["NodeGroupMemberUpdateStatusTypeDef"],
    },
    total=False,
)

NodeSnapshotTypeDef = TypedDict(
    "NodeSnapshotTypeDef",
    {
        "CacheClusterId": str,
        "NodeGroupId": str,
        "CacheNodeId": str,
        "NodeGroupConfiguration": "NodeGroupConfigurationTypeDef",
        "CacheSize": str,
        "CacheNodeCreateTime": datetime,
        "SnapshotCreateTime": datetime,
    },
    total=False,
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "TopicArn": str,
        "TopicStatus": str,
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

ParameterNameValueTypeDef = TypedDict(
    "ParameterNameValueTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
    },
    total=False,
)

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ChangeType": ChangeTypeType,
    },
    total=False,
)

PendingLogDeliveryConfigurationTypeDef = TypedDict(
    "PendingLogDeliveryConfigurationTypeDef",
    {
        "LogType": Literal["slow-log"],
        "DestinationType": DestinationTypeType,
        "DestinationDetails": "DestinationDetailsTypeDef",
        "LogFormat": LogFormatType,
    },
    total=False,
)

PendingModifiedValuesTypeDef = TypedDict(
    "PendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": AuthTokenUpdateStatusType,
        "LogDeliveryConfigurations": List["PendingLogDeliveryConfigurationTypeDef"],
    },
    total=False,
)

ProcessedUpdateActionTypeDef = TypedDict(
    "ProcessedUpdateActionTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "UpdateActionStatus": UpdateActionStatusType,
    },
    total=False,
)

_RequiredPurchaseReservedCacheNodesOfferingMessageRequestTypeDef = TypedDict(
    "_RequiredPurchaseReservedCacheNodesOfferingMessageRequestTypeDef",
    {
        "ReservedCacheNodesOfferingId": str,
    },
)
_OptionalPurchaseReservedCacheNodesOfferingMessageRequestTypeDef = TypedDict(
    "_OptionalPurchaseReservedCacheNodesOfferingMessageRequestTypeDef",
    {
        "ReservedCacheNodeId": str,
        "CacheNodeCount": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class PurchaseReservedCacheNodesOfferingMessageRequestTypeDef(
    _RequiredPurchaseReservedCacheNodesOfferingMessageRequestTypeDef,
    _OptionalPurchaseReservedCacheNodesOfferingMessageRequestTypeDef,
):
    pass

PurchaseReservedCacheNodesOfferingResultTypeDef = TypedDict(
    "PurchaseReservedCacheNodesOfferingResultTypeDef",
    {
        "ReservedCacheNode": "ReservedCacheNodeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RebalanceSlotsInGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "RebalanceSlotsInGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "ApplyImmediately": bool,
    },
)

RebalanceSlotsInGlobalReplicationGroupResultTypeDef = TypedDict(
    "RebalanceSlotsInGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RebootCacheClusterMessageRequestTypeDef = TypedDict(
    "RebootCacheClusterMessageRequestTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeIdsToReboot": List[str],
    },
)

RebootCacheClusterResultTypeDef = TypedDict(
    "RebootCacheClusterResultTypeDef",
    {
        "CacheCluster": "CacheClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {
        "RecurringChargeAmount": float,
        "RecurringChargeFrequency": str,
    },
    total=False,
)

RegionalConfigurationTypeDef = TypedDict(
    "RegionalConfigurationTypeDef",
    {
        "ReplicationGroupId": str,
        "ReplicationGroupRegion": str,
        "ReshardingConfiguration": List["ReshardingConfigurationTypeDef"],
    },
)

RemoveTagsFromResourceMessageRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
        "TagKeys": List[str],
    },
)

ReplicationGroupMessageTypeDef = TypedDict(
    "ReplicationGroupMessageTypeDef",
    {
        "Marker": str,
        "ReplicationGroups": List["ReplicationGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "ReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": PendingAutomaticFailoverStatusType,
        "Resharding": "ReshardingStatusTypeDef",
        "AuthTokenStatus": AuthTokenUpdateStatusType,
        "UserGroups": "UserGroupsUpdateStatusTypeDef",
        "LogDeliveryConfigurations": List["PendingLogDeliveryConfigurationTypeDef"],
    },
    total=False,
)

ReplicationGroupTypeDef = TypedDict(
    "ReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "GlobalReplicationGroupInfo": "GlobalReplicationGroupInfoTypeDef",
        "Status": str,
        "PendingModifiedValues": "ReplicationGroupPendingModifiedValuesTypeDef",
        "MemberClusters": List[str],
        "NodeGroups": List["NodeGroupTypeDef"],
        "SnapshottingClusterId": str,
        "AutomaticFailover": AutomaticFailoverStatusType,
        "MultiAZ": MultiAZStatusType,
        "ConfigurationEndpoint": "EndpointTypeDef",
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "MemberClustersOutpostArns": List[str],
        "KmsKeyId": str,
        "ARN": str,
        "UserGroupIds": List[str],
        "LogDeliveryConfigurations": List["LogDeliveryConfigurationTypeDef"],
    },
    total=False,
)

ReservedCacheNodeMessageTypeDef = TypedDict(
    "ReservedCacheNodeMessageTypeDef",
    {
        "Marker": str,
        "ReservedCacheNodes": List["ReservedCacheNodeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReservedCacheNodeTypeDef = TypedDict(
    "ReservedCacheNodeTypeDef",
    {
        "ReservedCacheNodeId": str,
        "ReservedCacheNodesOfferingId": str,
        "CacheNodeType": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CacheNodeCount": int,
        "ProductDescription": str,
        "OfferingType": str,
        "State": str,
        "RecurringCharges": List["RecurringChargeTypeDef"],
        "ReservationARN": str,
    },
    total=False,
)

ReservedCacheNodesOfferingMessageTypeDef = TypedDict(
    "ReservedCacheNodesOfferingMessageTypeDef",
    {
        "Marker": str,
        "ReservedCacheNodesOfferings": List["ReservedCacheNodesOfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReservedCacheNodesOfferingTypeDef = TypedDict(
    "ReservedCacheNodesOfferingTypeDef",
    {
        "ReservedCacheNodesOfferingId": str,
        "CacheNodeType": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "ProductDescription": str,
        "OfferingType": str,
        "RecurringCharges": List["RecurringChargeTypeDef"],
    },
    total=False,
)

_RequiredResetCacheParameterGroupMessageRequestTypeDef = TypedDict(
    "_RequiredResetCacheParameterGroupMessageRequestTypeDef",
    {
        "CacheParameterGroupName": str,
    },
)
_OptionalResetCacheParameterGroupMessageRequestTypeDef = TypedDict(
    "_OptionalResetCacheParameterGroupMessageRequestTypeDef",
    {
        "ResetAllParameters": bool,
        "ParameterNameValues": List["ParameterNameValueTypeDef"],
    },
    total=False,
)

class ResetCacheParameterGroupMessageRequestTypeDef(
    _RequiredResetCacheParameterGroupMessageRequestTypeDef,
    _OptionalResetCacheParameterGroupMessageRequestTypeDef,
):
    pass

ReshardingConfigurationTypeDef = TypedDict(
    "ReshardingConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "PreferredAvailabilityZones": List[str],
    },
    total=False,
)

ReshardingStatusTypeDef = TypedDict(
    "ReshardingStatusTypeDef",
    {
        "SlotMigration": "SlotMigrationTypeDef",
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

RevokeCacheSecurityGroupIngressMessageRequestTypeDef = TypedDict(
    "RevokeCacheSecurityGroupIngressMessageRequestTypeDef",
    {
        "CacheSecurityGroupName": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
    },
)

RevokeCacheSecurityGroupIngressResultTypeDef = TypedDict(
    "RevokeCacheSecurityGroupIngressResultTypeDef",
    {
        "CacheSecurityGroup": "CacheSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SecurityGroupMembershipTypeDef = TypedDict(
    "SecurityGroupMembershipTypeDef",
    {
        "SecurityGroupId": str,
        "Status": str,
    },
    total=False,
)

ServiceUpdateTypeDef = TypedDict(
    "ServiceUpdateTypeDef",
    {
        "ServiceUpdateName": str,
        "ServiceUpdateReleaseDate": datetime,
        "ServiceUpdateEndDate": datetime,
        "ServiceUpdateSeverity": ServiceUpdateSeverityType,
        "ServiceUpdateRecommendedApplyByDate": datetime,
        "ServiceUpdateStatus": ServiceUpdateStatusType,
        "ServiceUpdateDescription": str,
        "ServiceUpdateType": Literal["security-update"],
        "Engine": str,
        "EngineVersion": str,
        "AutoUpdateAfterRecommendedApplyByDate": bool,
        "EstimatedUpdateTime": str,
    },
    total=False,
)

ServiceUpdatesMessageTypeDef = TypedDict(
    "ServiceUpdatesMessageTypeDef",
    {
        "Marker": str,
        "ServiceUpdates": List["ServiceUpdateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SlotMigrationTypeDef = TypedDict(
    "SlotMigrationTypeDef",
    {
        "ProgressPercentage": float,
    },
    total=False,
)

SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "SnapshotName": str,
        "ReplicationGroupId": str,
        "ReplicationGroupDescription": str,
        "CacheClusterId": str,
        "SnapshotStatus": str,
        "SnapshotSource": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "PreferredOutpostArn": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "TopicArn": str,
        "Port": int,
        "CacheParameterGroupName": str,
        "CacheSubnetGroupName": str,
        "VpcId": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "NumNodeGroups": int,
        "AutomaticFailover": AutomaticFailoverStatusType,
        "NodeSnapshots": List["NodeSnapshotTypeDef"],
        "KmsKeyId": str,
        "ARN": str,
    },
    total=False,
)

StartMigrationMessageRequestTypeDef = TypedDict(
    "StartMigrationMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "CustomerNodeEndpointList": List["CustomerNodeEndpointTypeDef"],
    },
)

StartMigrationResponseTypeDef = TypedDict(
    "StartMigrationResponseTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubnetOutpostTypeDef = TypedDict(
    "SubnetOutpostTypeDef",
    {
        "SubnetOutpostArn": str,
    },
    total=False,
)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": "AvailabilityZoneTypeDef",
        "SubnetOutpost": "SubnetOutpostTypeDef",
    },
    total=False,
)

TagListMessageTypeDef = TypedDict(
    "TagListMessageTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

TestFailoverMessageRequestTypeDef = TypedDict(
    "TestFailoverMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "NodeGroupId": str,
    },
)

TestFailoverResultTypeDef = TypedDict(
    "TestFailoverResultTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TimeRangeFilterTypeDef = TypedDict(
    "TimeRangeFilterTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
    total=False,
)

UnprocessedUpdateActionTypeDef = TypedDict(
    "UnprocessedUpdateActionTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "ErrorType": str,
        "ErrorMessage": str,
    },
    total=False,
)

UpdateActionResultsMessageTypeDef = TypedDict(
    "UpdateActionResultsMessageTypeDef",
    {
        "ProcessedUpdateActions": List["ProcessedUpdateActionTypeDef"],
        "UnprocessedUpdateActions": List["UnprocessedUpdateActionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateActionTypeDef = TypedDict(
    "UpdateActionTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "ServiceUpdateReleaseDate": datetime,
        "ServiceUpdateSeverity": ServiceUpdateSeverityType,
        "ServiceUpdateStatus": ServiceUpdateStatusType,
        "ServiceUpdateRecommendedApplyByDate": datetime,
        "ServiceUpdateType": Literal["security-update"],
        "UpdateActionAvailableDate": datetime,
        "UpdateActionStatus": UpdateActionStatusType,
        "NodesUpdated": str,
        "UpdateActionStatusModifiedDate": datetime,
        "SlaMet": SlaMetType,
        "NodeGroupUpdateStatus": List["NodeGroupUpdateStatusTypeDef"],
        "CacheNodeUpdateStatus": List["CacheNodeUpdateStatusTypeDef"],
        "EstimatedUpdateTime": str,
        "Engine": str,
    },
    total=False,
)

UpdateActionsMessageTypeDef = TypedDict(
    "UpdateActionsMessageTypeDef",
    {
        "Marker": str,
        "UpdateActions": List["UpdateActionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserGroupPendingChangesTypeDef = TypedDict(
    "UserGroupPendingChangesTypeDef",
    {
        "UserIdsToRemove": List[str],
        "UserIdsToAdd": List[str],
    },
    total=False,
)

UserGroupResponseMetadataTypeDef = TypedDict(
    "UserGroupResponseMetadataTypeDef",
    {
        "UserGroupId": str,
        "Status": str,
        "Engine": str,
        "UserIds": List[str],
        "PendingChanges": "UserGroupPendingChangesTypeDef",
        "ReplicationGroups": List[str],
        "ARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserGroupTypeDef = TypedDict(
    "UserGroupTypeDef",
    {
        "UserGroupId": str,
        "Status": str,
        "Engine": str,
        "UserIds": List[str],
        "PendingChanges": "UserGroupPendingChangesTypeDef",
        "ReplicationGroups": List[str],
        "ARN": str,
    },
    total=False,
)

UserGroupsUpdateStatusTypeDef = TypedDict(
    "UserGroupsUpdateStatusTypeDef",
    {
        "UserGroupIdsToAdd": List[str],
        "UserGroupIdsToRemove": List[str],
    },
    total=False,
)

UserResponseMetadataTypeDef = TypedDict(
    "UserResponseMetadataTypeDef",
    {
        "UserId": str,
        "UserName": str,
        "Status": str,
        "Engine": str,
        "AccessString": str,
        "UserGroupIds": List[str],
        "Authentication": "AuthenticationTypeDef",
        "ARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "UserId": str,
        "UserName": str,
        "Status": str,
        "Engine": str,
        "AccessString": str,
        "UserGroupIds": List[str],
        "Authentication": "AuthenticationTypeDef",
        "ARN": str,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
