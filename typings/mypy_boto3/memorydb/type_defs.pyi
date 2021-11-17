"""
Type annotations for memorydb service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/type_defs.html)

Usage::

    ```python
    from mypy_boto3_memorydb.type_defs import ACLPendingChangesTypeDef

    data: ACLPendingChangesTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import AuthenticationTypeType, AZStatusType, ServiceUpdateStatusType, SourceTypeType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ACLPendingChangesTypeDef",
    "ACLTypeDef",
    "ACLsUpdateStatusTypeDef",
    "AuthenticationModeTypeDef",
    "AuthenticationTypeDef",
    "AvailabilityZoneTypeDef",
    "BatchUpdateClusterRequestRequestTypeDef",
    "BatchUpdateClusterResponseTypeDef",
    "ClusterConfigurationTypeDef",
    "ClusterPendingUpdatesTypeDef",
    "ClusterTypeDef",
    "CopySnapshotRequestRequestTypeDef",
    "CopySnapshotResponseTypeDef",
    "CreateACLRequestRequestTypeDef",
    "CreateACLResponseTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateParameterGroupRequestRequestTypeDef",
    "CreateParameterGroupResponseTypeDef",
    "CreateSnapshotRequestRequestTypeDef",
    "CreateSnapshotResponseTypeDef",
    "CreateSubnetGroupRequestRequestTypeDef",
    "CreateSubnetGroupResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CreateUserResponseTypeDef",
    "DeleteACLRequestRequestTypeDef",
    "DeleteACLResponseTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteParameterGroupRequestRequestTypeDef",
    "DeleteParameterGroupResponseTypeDef",
    "DeleteSnapshotRequestRequestTypeDef",
    "DeleteSnapshotResponseTypeDef",
    "DeleteSubnetGroupRequestRequestTypeDef",
    "DeleteSubnetGroupResponseTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DeleteUserResponseTypeDef",
    "DescribeACLsRequestRequestTypeDef",
    "DescribeACLsResponseTypeDef",
    "DescribeClustersRequestRequestTypeDef",
    "DescribeClustersResponseTypeDef",
    "DescribeEngineVersionsRequestRequestTypeDef",
    "DescribeEngineVersionsResponseTypeDef",
    "DescribeEventsRequestRequestTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeParameterGroupsRequestRequestTypeDef",
    "DescribeParameterGroupsResponseTypeDef",
    "DescribeParametersRequestRequestTypeDef",
    "DescribeParametersResponseTypeDef",
    "DescribeServiceUpdatesRequestRequestTypeDef",
    "DescribeServiceUpdatesResponseTypeDef",
    "DescribeSnapshotsRequestRequestTypeDef",
    "DescribeSnapshotsResponseTypeDef",
    "DescribeSubnetGroupsRequestRequestTypeDef",
    "DescribeSubnetGroupsResponseTypeDef",
    "DescribeUsersRequestRequestTypeDef",
    "DescribeUsersResponseTypeDef",
    "EndpointTypeDef",
    "EngineVersionInfoTypeDef",
    "EventTypeDef",
    "FailoverShardRequestRequestTypeDef",
    "FailoverShardResponseTypeDef",
    "FilterTypeDef",
    "ListAllowedNodeTypeUpdatesRequestRequestTypeDef",
    "ListAllowedNodeTypeUpdatesResponseTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "NodeTypeDef",
    "ParameterGroupTypeDef",
    "ParameterNameValueTypeDef",
    "ParameterTypeDef",
    "PendingModifiedServiceUpdateTypeDef",
    "ReplicaConfigurationRequestTypeDef",
    "ResetParameterGroupRequestRequestTypeDef",
    "ResetParameterGroupResponseTypeDef",
    "ReshardingStatusTypeDef",
    "ResponseMetadataTypeDef",
    "SecurityGroupMembershipTypeDef",
    "ServiceUpdateRequestTypeDef",
    "ServiceUpdateTypeDef",
    "ShardConfigurationRequestTypeDef",
    "ShardConfigurationTypeDef",
    "ShardDetailTypeDef",
    "ShardTypeDef",
    "SlotMigrationTypeDef",
    "SnapshotTypeDef",
    "SubnetGroupTypeDef",
    "SubnetTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagResourceResponseTypeDef",
    "TagTypeDef",
    "UnprocessedClusterTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UntagResourceResponseTypeDef",
    "UpdateACLRequestRequestTypeDef",
    "UpdateACLResponseTypeDef",
    "UpdateClusterRequestRequestTypeDef",
    "UpdateClusterResponseTypeDef",
    "UpdateParameterGroupRequestRequestTypeDef",
    "UpdateParameterGroupResponseTypeDef",
    "UpdateSubnetGroupRequestRequestTypeDef",
    "UpdateSubnetGroupResponseTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UpdateUserResponseTypeDef",
    "UserTypeDef",
)

ACLPendingChangesTypeDef = TypedDict(
    "ACLPendingChangesTypeDef",
    {
        "UserNamesToRemove": List[str],
        "UserNamesToAdd": List[str],
    },
    total=False,
)

ACLTypeDef = TypedDict(
    "ACLTypeDef",
    {
        "Name": str,
        "Status": str,
        "UserNames": List[str],
        "MinimumEngineVersion": str,
        "PendingChanges": "ACLPendingChangesTypeDef",
        "Clusters": List[str],
        "ARN": str,
    },
    total=False,
)

ACLsUpdateStatusTypeDef = TypedDict(
    "ACLsUpdateStatusTypeDef",
    {
        "ACLToApply": str,
    },
    total=False,
)

AuthenticationModeTypeDef = TypedDict(
    "AuthenticationModeTypeDef",
    {
        "Type": Literal["password"],
        "Passwords": List[str],
    },
    total=False,
)

AuthenticationTypeDef = TypedDict(
    "AuthenticationTypeDef",
    {
        "Type": AuthenticationTypeType,
        "PasswordCount": int,
    },
    total=False,
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": str,
    },
    total=False,
)

_RequiredBatchUpdateClusterRequestRequestTypeDef = TypedDict(
    "_RequiredBatchUpdateClusterRequestRequestTypeDef",
    {
        "ClusterNames": List[str],
    },
)
_OptionalBatchUpdateClusterRequestRequestTypeDef = TypedDict(
    "_OptionalBatchUpdateClusterRequestRequestTypeDef",
    {
        "ServiceUpdate": "ServiceUpdateRequestTypeDef",
    },
    total=False,
)

class BatchUpdateClusterRequestRequestTypeDef(
    _RequiredBatchUpdateClusterRequestRequestTypeDef,
    _OptionalBatchUpdateClusterRequestRequestTypeDef,
):
    pass

BatchUpdateClusterResponseTypeDef = TypedDict(
    "BatchUpdateClusterResponseTypeDef",
    {
        "ProcessedClusters": List["ClusterTypeDef"],
        "UnprocessedClusters": List["UnprocessedClusterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClusterConfigurationTypeDef = TypedDict(
    "ClusterConfigurationTypeDef",
    {
        "Name": str,
        "Description": str,
        "NodeType": str,
        "EngineVersion": str,
        "MaintenanceWindow": str,
        "TopicArn": str,
        "Port": int,
        "ParameterGroupName": str,
        "SubnetGroupName": str,
        "VpcId": str,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "NumShards": int,
        "Shards": List["ShardDetailTypeDef"],
    },
    total=False,
)

ClusterPendingUpdatesTypeDef = TypedDict(
    "ClusterPendingUpdatesTypeDef",
    {
        "Resharding": "ReshardingStatusTypeDef",
        "ACLs": "ACLsUpdateStatusTypeDef",
        "ServiceUpdates": List["PendingModifiedServiceUpdateTypeDef"],
    },
    total=False,
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "Name": str,
        "Description": str,
        "Status": str,
        "PendingUpdates": "ClusterPendingUpdatesTypeDef",
        "NumberOfShards": int,
        "Shards": List["ShardTypeDef"],
        "AvailabilityMode": AZStatusType,
        "ClusterEndpoint": "EndpointTypeDef",
        "NodeType": str,
        "EngineVersion": str,
        "EnginePatchVersion": str,
        "ParameterGroupName": str,
        "ParameterGroupStatus": str,
        "SecurityGroups": List["SecurityGroupMembershipTypeDef"],
        "SubnetGroupName": str,
        "TLSEnabled": bool,
        "KmsKeyId": str,
        "ARN": str,
        "SnsTopicArn": str,
        "SnsTopicStatus": str,
        "SnapshotRetentionLimit": int,
        "MaintenanceWindow": str,
        "SnapshotWindow": str,
        "ACLName": str,
        "AutoMinorVersionUpgrade": bool,
    },
    total=False,
)

_RequiredCopySnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredCopySnapshotRequestRequestTypeDef",
    {
        "SourceSnapshotName": str,
        "TargetSnapshotName": str,
    },
)
_OptionalCopySnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalCopySnapshotRequestRequestTypeDef",
    {
        "TargetBucket": str,
        "KmsKeyId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CopySnapshotRequestRequestTypeDef(
    _RequiredCopySnapshotRequestRequestTypeDef, _OptionalCopySnapshotRequestRequestTypeDef
):
    pass

CopySnapshotResponseTypeDef = TypedDict(
    "CopySnapshotResponseTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateACLRequestRequestTypeDef = TypedDict(
    "_RequiredCreateACLRequestRequestTypeDef",
    {
        "ACLName": str,
    },
)
_OptionalCreateACLRequestRequestTypeDef = TypedDict(
    "_OptionalCreateACLRequestRequestTypeDef",
    {
        "UserNames": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateACLRequestRequestTypeDef(
    _RequiredCreateACLRequestRequestTypeDef, _OptionalCreateACLRequestRequestTypeDef
):
    pass

CreateACLResponseTypeDef = TypedDict(
    "CreateACLResponseTypeDef",
    {
        "ACL": "ACLTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateClusterRequestRequestTypeDef = TypedDict(
    "_RequiredCreateClusterRequestRequestTypeDef",
    {
        "ClusterName": str,
        "NodeType": str,
        "ACLName": str,
    },
)
_OptionalCreateClusterRequestRequestTypeDef = TypedDict(
    "_OptionalCreateClusterRequestRequestTypeDef",
    {
        "ParameterGroupName": str,
        "Description": str,
        "NumShards": int,
        "NumReplicasPerShard": int,
        "SubnetGroupName": str,
        "SecurityGroupIds": List[str],
        "MaintenanceWindow": str,
        "Port": int,
        "SnsTopicArn": str,
        "TLSEnabled": bool,
        "KmsKeyId": str,
        "SnapshotArns": List[str],
        "SnapshotName": str,
        "SnapshotRetentionLimit": int,
        "Tags": List["TagTypeDef"],
        "SnapshotWindow": str,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
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
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateParameterGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateParameterGroupRequestRequestTypeDef",
    {
        "ParameterGroupName": str,
        "Family": str,
    },
)
_OptionalCreateParameterGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateParameterGroupRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateParameterGroupRequestRequestTypeDef(
    _RequiredCreateParameterGroupRequestRequestTypeDef,
    _OptionalCreateParameterGroupRequestRequestTypeDef,
):
    pass

CreateParameterGroupResponseTypeDef = TypedDict(
    "CreateParameterGroupResponseTypeDef",
    {
        "ParameterGroup": "ParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSnapshotRequestRequestTypeDef",
    {
        "ClusterName": str,
        "SnapshotName": str,
    },
)
_OptionalCreateSnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSnapshotRequestRequestTypeDef",
    {
        "KmsKeyId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateSnapshotRequestRequestTypeDef(
    _RequiredCreateSnapshotRequestRequestTypeDef, _OptionalCreateSnapshotRequestRequestTypeDef
):
    pass

CreateSnapshotResponseTypeDef = TypedDict(
    "CreateSnapshotResponseTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSubnetGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSubnetGroupRequestRequestTypeDef",
    {
        "SubnetGroupName": str,
        "SubnetIds": List[str],
    },
)
_OptionalCreateSubnetGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSubnetGroupRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateSubnetGroupRequestRequestTypeDef(
    _RequiredCreateSubnetGroupRequestRequestTypeDef, _OptionalCreateSubnetGroupRequestRequestTypeDef
):
    pass

CreateSubnetGroupResponseTypeDef = TypedDict(
    "CreateSubnetGroupResponseTypeDef",
    {
        "SubnetGroup": "SubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AuthenticationMode": "AuthenticationModeTypeDef",
        "AccessString": str,
    },
)
_OptionalCreateUserRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateUserRequestRequestTypeDef(
    _RequiredCreateUserRequestRequestTypeDef, _OptionalCreateUserRequestRequestTypeDef
):
    pass

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteACLRequestRequestTypeDef = TypedDict(
    "DeleteACLRequestRequestTypeDef",
    {
        "ACLName": str,
    },
)

DeleteACLResponseTypeDef = TypedDict(
    "DeleteACLResponseTypeDef",
    {
        "ACL": "ACLTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteClusterRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteClusterRequestRequestTypeDef",
    {
        "ClusterName": str,
    },
)
_OptionalDeleteClusterRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteClusterRequestRequestTypeDef",
    {
        "FinalSnapshotName": str,
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
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteParameterGroupRequestRequestTypeDef = TypedDict(
    "DeleteParameterGroupRequestRequestTypeDef",
    {
        "ParameterGroupName": str,
    },
)

DeleteParameterGroupResponseTypeDef = TypedDict(
    "DeleteParameterGroupResponseTypeDef",
    {
        "ParameterGroup": "ParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteSnapshotRequestRequestTypeDef",
    {
        "SnapshotName": str,
    },
)

DeleteSnapshotResponseTypeDef = TypedDict(
    "DeleteSnapshotResponseTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSubnetGroupRequestRequestTypeDef = TypedDict(
    "DeleteSubnetGroupRequestRequestTypeDef",
    {
        "SubnetGroupName": str,
    },
)

DeleteSubnetGroupResponseTypeDef = TypedDict(
    "DeleteSubnetGroupResponseTypeDef",
    {
        "SubnetGroup": "SubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "UserName": str,
    },
)

DeleteUserResponseTypeDef = TypedDict(
    "DeleteUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeACLsRequestRequestTypeDef = TypedDict(
    "DescribeACLsRequestRequestTypeDef",
    {
        "ACLName": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeACLsResponseTypeDef = TypedDict(
    "DescribeACLsResponseTypeDef",
    {
        "ACLs": List["ACLTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClustersRequestRequestTypeDef = TypedDict(
    "DescribeClustersRequestRequestTypeDef",
    {
        "ClusterName": str,
        "MaxResults": int,
        "NextToken": str,
        "ShowShardDetails": bool,
    },
    total=False,
)

DescribeClustersResponseTypeDef = TypedDict(
    "DescribeClustersResponseTypeDef",
    {
        "NextToken": str,
        "Clusters": List["ClusterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEngineVersionsRequestRequestTypeDef = TypedDict(
    "DescribeEngineVersionsRequestRequestTypeDef",
    {
        "EngineVersion": str,
        "ParameterGroupFamily": str,
        "MaxResults": int,
        "NextToken": str,
        "DefaultOnly": bool,
    },
    total=False,
)

DescribeEngineVersionsResponseTypeDef = TypedDict(
    "DescribeEngineVersionsResponseTypeDef",
    {
        "NextToken": str,
        "EngineVersions": List["EngineVersionInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventsRequestRequestTypeDef = TypedDict(
    "DescribeEventsRequestRequestTypeDef",
    {
        "SourceName": str,
        "SourceType": SourceTypeType,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Duration": int,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeEventsResponseTypeDef = TypedDict(
    "DescribeEventsResponseTypeDef",
    {
        "NextToken": str,
        "Events": List["EventTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeParameterGroupsRequestRequestTypeDef = TypedDict(
    "DescribeParameterGroupsRequestRequestTypeDef",
    {
        "ParameterGroupName": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeParameterGroupsResponseTypeDef = TypedDict(
    "DescribeParameterGroupsResponseTypeDef",
    {
        "NextToken": str,
        "ParameterGroups": List["ParameterGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeParametersRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeParametersRequestRequestTypeDef",
    {
        "ParameterGroupName": str,
    },
)
_OptionalDescribeParametersRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeParametersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeParametersRequestRequestTypeDef(
    _RequiredDescribeParametersRequestRequestTypeDef,
    _OptionalDescribeParametersRequestRequestTypeDef,
):
    pass

DescribeParametersResponseTypeDef = TypedDict(
    "DescribeParametersResponseTypeDef",
    {
        "NextToken": str,
        "Parameters": List["ParameterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServiceUpdatesRequestRequestTypeDef = TypedDict(
    "DescribeServiceUpdatesRequestRequestTypeDef",
    {
        "ServiceUpdateName": str,
        "ClusterNames": List[str],
        "Status": List[ServiceUpdateStatusType],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeServiceUpdatesResponseTypeDef = TypedDict(
    "DescribeServiceUpdatesResponseTypeDef",
    {
        "NextToken": str,
        "ServiceUpdates": List["ServiceUpdateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSnapshotsRequestRequestTypeDef = TypedDict(
    "DescribeSnapshotsRequestRequestTypeDef",
    {
        "ClusterName": str,
        "SnapshotName": str,
        "Source": str,
        "NextToken": str,
        "MaxResults": int,
        "ShowDetail": bool,
    },
    total=False,
)

DescribeSnapshotsResponseTypeDef = TypedDict(
    "DescribeSnapshotsResponseTypeDef",
    {
        "NextToken": str,
        "Snapshots": List["SnapshotTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSubnetGroupsRequestRequestTypeDef = TypedDict(
    "DescribeSubnetGroupsRequestRequestTypeDef",
    {
        "SubnetGroupName": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeSubnetGroupsResponseTypeDef = TypedDict(
    "DescribeSubnetGroupsResponseTypeDef",
    {
        "NextToken": str,
        "SubnetGroups": List["SubnetGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUsersRequestRequestTypeDef = TypedDict(
    "DescribeUsersRequestRequestTypeDef",
    {
        "UserName": str,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeUsersResponseTypeDef = TypedDict(
    "DescribeUsersResponseTypeDef",
    {
        "Users": List["UserTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "Port": int,
    },
    total=False,
)

EngineVersionInfoTypeDef = TypedDict(
    "EngineVersionInfoTypeDef",
    {
        "EngineVersion": str,
        "EnginePatchVersion": str,
        "ParameterGroupFamily": str,
    },
    total=False,
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceName": str,
        "SourceType": SourceTypeType,
        "Message": str,
        "Date": datetime,
    },
    total=False,
)

FailoverShardRequestRequestTypeDef = TypedDict(
    "FailoverShardRequestRequestTypeDef",
    {
        "ClusterName": str,
        "ShardName": str,
    },
)

FailoverShardResponseTypeDef = TypedDict(
    "FailoverShardResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
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

ListAllowedNodeTypeUpdatesRequestRequestTypeDef = TypedDict(
    "ListAllowedNodeTypeUpdatesRequestRequestTypeDef",
    {
        "ClusterName": str,
    },
)

ListAllowedNodeTypeUpdatesResponseTypeDef = TypedDict(
    "ListAllowedNodeTypeUpdatesResponseTypeDef",
    {
        "ScaleUpNodeTypes": List[str],
        "ScaleDownNodeTypes": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsRequestRequestTypeDef = TypedDict(
    "ListTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "Name": str,
        "Status": str,
        "AvailabilityZone": str,
        "CreateTime": datetime,
        "Endpoint": "EndpointTypeDef",
    },
    total=False,
)

ParameterGroupTypeDef = TypedDict(
    "ParameterGroupTypeDef",
    {
        "Name": str,
        "Family": str,
        "Description": str,
        "ARN": str,
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
        "Name": str,
        "Value": str,
        "Description": str,
        "DataType": str,
        "AllowedValues": str,
        "MinimumEngineVersion": str,
    },
    total=False,
)

PendingModifiedServiceUpdateTypeDef = TypedDict(
    "PendingModifiedServiceUpdateTypeDef",
    {
        "ServiceUpdateName": str,
        "Status": ServiceUpdateStatusType,
    },
    total=False,
)

ReplicaConfigurationRequestTypeDef = TypedDict(
    "ReplicaConfigurationRequestTypeDef",
    {
        "ReplicaCount": int,
    },
    total=False,
)

_RequiredResetParameterGroupRequestRequestTypeDef = TypedDict(
    "_RequiredResetParameterGroupRequestRequestTypeDef",
    {
        "ParameterGroupName": str,
    },
)
_OptionalResetParameterGroupRequestRequestTypeDef = TypedDict(
    "_OptionalResetParameterGroupRequestRequestTypeDef",
    {
        "AllParameters": bool,
        "ParameterNames": List[str],
    },
    total=False,
)

class ResetParameterGroupRequestRequestTypeDef(
    _RequiredResetParameterGroupRequestRequestTypeDef,
    _OptionalResetParameterGroupRequestRequestTypeDef,
):
    pass

ResetParameterGroupResponseTypeDef = TypedDict(
    "ResetParameterGroupResponseTypeDef",
    {
        "ParameterGroup": "ParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

SecurityGroupMembershipTypeDef = TypedDict(
    "SecurityGroupMembershipTypeDef",
    {
        "SecurityGroupId": str,
        "Status": str,
    },
    total=False,
)

ServiceUpdateRequestTypeDef = TypedDict(
    "ServiceUpdateRequestTypeDef",
    {
        "ServiceUpdateNameToApply": str,
    },
    total=False,
)

ServiceUpdateTypeDef = TypedDict(
    "ServiceUpdateTypeDef",
    {
        "ClusterName": str,
        "ServiceUpdateName": str,
        "ReleaseDate": datetime,
        "Description": str,
        "Status": ServiceUpdateStatusType,
        "Type": Literal["security-update"],
        "NodesUpdated": str,
        "AutoUpdateStartDate": datetime,
    },
    total=False,
)

ShardConfigurationRequestTypeDef = TypedDict(
    "ShardConfigurationRequestTypeDef",
    {
        "ShardCount": int,
    },
    total=False,
)

ShardConfigurationTypeDef = TypedDict(
    "ShardConfigurationTypeDef",
    {
        "Slots": str,
        "ReplicaCount": int,
    },
    total=False,
)

ShardDetailTypeDef = TypedDict(
    "ShardDetailTypeDef",
    {
        "Name": str,
        "Configuration": "ShardConfigurationTypeDef",
        "Size": str,
        "SnapshotCreationTime": datetime,
    },
    total=False,
)

ShardTypeDef = TypedDict(
    "ShardTypeDef",
    {
        "Name": str,
        "Status": str,
        "Slots": str,
        "Nodes": List["NodeTypeDef"],
        "NumberOfNodes": int,
    },
    total=False,
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
        "Name": str,
        "Status": str,
        "Source": str,
        "KmsKeyId": str,
        "ARN": str,
        "ClusterConfiguration": "ClusterConfigurationTypeDef",
    },
    total=False,
)

SubnetGroupTypeDef = TypedDict(
    "SubnetGroupTypeDef",
    {
        "Name": str,
        "Description": str,
        "VpcId": str,
        "Subnets": List["SubnetTypeDef"],
        "ARN": str,
    },
    total=False,
)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "Identifier": str,
        "AvailabilityZone": "AvailabilityZoneTypeDef",
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagResourceResponseTypeDef = TypedDict(
    "TagResourceResponseTypeDef",
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

UnprocessedClusterTypeDef = TypedDict(
    "UnprocessedClusterTypeDef",
    {
        "ClusterName": str,
        "ErrorType": str,
        "ErrorMessage": str,
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

UntagResourceResponseTypeDef = TypedDict(
    "UntagResourceResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateACLRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateACLRequestRequestTypeDef",
    {
        "ACLName": str,
    },
)
_OptionalUpdateACLRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateACLRequestRequestTypeDef",
    {
        "UserNamesToAdd": List[str],
        "UserNamesToRemove": List[str],
    },
    total=False,
)

class UpdateACLRequestRequestTypeDef(
    _RequiredUpdateACLRequestRequestTypeDef, _OptionalUpdateACLRequestRequestTypeDef
):
    pass

UpdateACLResponseTypeDef = TypedDict(
    "UpdateACLResponseTypeDef",
    {
        "ACL": "ACLTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateClusterRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateClusterRequestRequestTypeDef",
    {
        "ClusterName": str,
    },
)
_OptionalUpdateClusterRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateClusterRequestRequestTypeDef",
    {
        "Description": str,
        "SecurityGroupIds": List[str],
        "MaintenanceWindow": str,
        "SnsTopicArn": str,
        "SnsTopicStatus": str,
        "ParameterGroupName": str,
        "SnapshotWindow": str,
        "SnapshotRetentionLimit": int,
        "NodeType": str,
        "EngineVersion": str,
        "ReplicaConfiguration": "ReplicaConfigurationRequestTypeDef",
        "ShardConfiguration": "ShardConfigurationRequestTypeDef",
        "ACLName": str,
    },
    total=False,
)

class UpdateClusterRequestRequestTypeDef(
    _RequiredUpdateClusterRequestRequestTypeDef, _OptionalUpdateClusterRequestRequestTypeDef
):
    pass

UpdateClusterResponseTypeDef = TypedDict(
    "UpdateClusterResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateParameterGroupRequestRequestTypeDef = TypedDict(
    "UpdateParameterGroupRequestRequestTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterNameValues": List["ParameterNameValueTypeDef"],
    },
)

UpdateParameterGroupResponseTypeDef = TypedDict(
    "UpdateParameterGroupResponseTypeDef",
    {
        "ParameterGroup": "ParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSubnetGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSubnetGroupRequestRequestTypeDef",
    {
        "SubnetGroupName": str,
    },
)
_OptionalUpdateSubnetGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSubnetGroupRequestRequestTypeDef",
    {
        "Description": str,
        "SubnetIds": List[str],
    },
    total=False,
)

class UpdateSubnetGroupRequestRequestTypeDef(
    _RequiredUpdateSubnetGroupRequestRequestTypeDef, _OptionalUpdateSubnetGroupRequestRequestTypeDef
):
    pass

UpdateSubnetGroupResponseTypeDef = TypedDict(
    "UpdateSubnetGroupResponseTypeDef",
    {
        "SubnetGroup": "SubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserRequestRequestTypeDef",
    {
        "UserName": str,
    },
)
_OptionalUpdateUserRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserRequestRequestTypeDef",
    {
        "AuthenticationMode": "AuthenticationModeTypeDef",
        "AccessString": str,
    },
    total=False,
)

class UpdateUserRequestRequestTypeDef(
    _RequiredUpdateUserRequestRequestTypeDef, _OptionalUpdateUserRequestRequestTypeDef
):
    pass

UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Name": str,
        "Status": str,
        "AccessString": str,
        "ACLNames": List[str],
        "MinimumEngineVersion": str,
        "Authentication": "AuthenticationTypeDef",
        "ARN": str,
    },
    total=False,
)
