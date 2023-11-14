"""
Type annotations for dax service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/type_defs.html)

Usage::

    ```python
    from mypy_boto3_dax.type_defs import ClusterTypeDef

    data: ClusterTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ChangeTypeType,
    ClusterEndpointEncryptionTypeType,
    IsModifiableType,
    ParameterTypeType,
    SourceTypeType,
    SSEStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ClusterTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateParameterGroupRequestRequestTypeDef",
    "CreateParameterGroupResponseTypeDef",
    "CreateSubnetGroupRequestRequestTypeDef",
    "CreateSubnetGroupResponseTypeDef",
    "DecreaseReplicationFactorRequestRequestTypeDef",
    "DecreaseReplicationFactorResponseTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteParameterGroupRequestRequestTypeDef",
    "DeleteParameterGroupResponseTypeDef",
    "DeleteSubnetGroupRequestRequestTypeDef",
    "DeleteSubnetGroupResponseTypeDef",
    "DescribeClustersRequestRequestTypeDef",
    "DescribeClustersResponseTypeDef",
    "DescribeDefaultParametersRequestRequestTypeDef",
    "DescribeDefaultParametersResponseTypeDef",
    "DescribeEventsRequestRequestTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeParameterGroupsRequestRequestTypeDef",
    "DescribeParameterGroupsResponseTypeDef",
    "DescribeParametersRequestRequestTypeDef",
    "DescribeParametersResponseTypeDef",
    "DescribeSubnetGroupsRequestRequestTypeDef",
    "DescribeSubnetGroupsResponseTypeDef",
    "EndpointTypeDef",
    "EventTypeDef",
    "IncreaseReplicationFactorRequestRequestTypeDef",
    "IncreaseReplicationFactorResponseTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "NodeTypeDef",
    "NodeTypeSpecificValueTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterGroupStatusTypeDef",
    "ParameterGroupTypeDef",
    "ParameterNameValueTypeDef",
    "ParameterTypeDef",
    "RebootNodeRequestRequestTypeDef",
    "RebootNodeResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SSEDescriptionTypeDef",
    "SSESpecificationTypeDef",
    "SecurityGroupMembershipTypeDef",
    "SubnetGroupTypeDef",
    "SubnetTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagResourceResponseTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UntagResourceResponseTypeDef",
    "UpdateClusterRequestRequestTypeDef",
    "UpdateClusterResponseTypeDef",
    "UpdateParameterGroupRequestRequestTypeDef",
    "UpdateParameterGroupResponseTypeDef",
    "UpdateSubnetGroupRequestRequestTypeDef",
    "UpdateSubnetGroupResponseTypeDef",
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": "EndpointTypeDef",
        "NodeIdsToRemove": List[str],
        "Nodes": List["NodeTypeDef"],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": "NotificationConfigurationTypeDef",
        "SubnetGroup": str,
        "SecurityGroups": List["SecurityGroupMembershipTypeDef"],
        "IamRoleArn": str,
        "ParameterGroup": "ParameterGroupStatusTypeDef",
        "SSEDescription": "SSEDescriptionTypeDef",
        "ClusterEndpointEncryptionType": ClusterEndpointEncryptionTypeType,
    },
    total=False,
)

_RequiredCreateClusterRequestRequestTypeDef = TypedDict(
    "_RequiredCreateClusterRequestRequestTypeDef",
    {
        "ClusterName": str,
        "NodeType": str,
        "ReplicationFactor": int,
        "IamRoleArn": str,
    },
)
_OptionalCreateClusterRequestRequestTypeDef = TypedDict(
    "_OptionalCreateClusterRequestRequestTypeDef",
    {
        "Description": str,
        "AvailabilityZones": List[str],
        "SubnetGroupName": str,
        "SecurityGroupIds": List[str],
        "PreferredMaintenanceWindow": str,
        "NotificationTopicArn": str,
        "ParameterGroupName": str,
        "Tags": List["TagTypeDef"],
        "SSESpecification": "SSESpecificationTypeDef",
        "ClusterEndpointEncryptionType": ClusterEndpointEncryptionTypeType,
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
    },
)
_OptionalCreateParameterGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateParameterGroupRequestRequestTypeDef",
    {
        "Description": str,
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

_RequiredDecreaseReplicationFactorRequestRequestTypeDef = TypedDict(
    "_RequiredDecreaseReplicationFactorRequestRequestTypeDef",
    {
        "ClusterName": str,
        "NewReplicationFactor": int,
    },
)
_OptionalDecreaseReplicationFactorRequestRequestTypeDef = TypedDict(
    "_OptionalDecreaseReplicationFactorRequestRequestTypeDef",
    {
        "AvailabilityZones": List[str],
        "NodeIdsToRemove": List[str],
    },
    total=False,
)

class DecreaseReplicationFactorRequestRequestTypeDef(
    _RequiredDecreaseReplicationFactorRequestRequestTypeDef,
    _OptionalDecreaseReplicationFactorRequestRequestTypeDef,
):
    pass

DecreaseReplicationFactorResponseTypeDef = TypedDict(
    "DecreaseReplicationFactorResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterRequestRequestTypeDef = TypedDict(
    "DeleteClusterRequestRequestTypeDef",
    {
        "ClusterName": str,
    },
)

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
        "DeletionMessage": str,
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
        "DeletionMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClustersRequestRequestTypeDef = TypedDict(
    "DescribeClustersRequestRequestTypeDef",
    {
        "ClusterNames": List[str],
        "MaxResults": int,
        "NextToken": str,
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

DescribeDefaultParametersRequestRequestTypeDef = TypedDict(
    "DescribeDefaultParametersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeDefaultParametersResponseTypeDef = TypedDict(
    "DescribeDefaultParametersResponseTypeDef",
    {
        "NextToken": str,
        "Parameters": List["ParameterTypeDef"],
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
        "ParameterGroupNames": List[str],
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
        "Source": str,
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

DescribeSubnetGroupsRequestRequestTypeDef = TypedDict(
    "DescribeSubnetGroupsRequestRequestTypeDef",
    {
        "SubnetGroupNames": List[str],
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

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "Port": int,
        "URL": str,
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

_RequiredIncreaseReplicationFactorRequestRequestTypeDef = TypedDict(
    "_RequiredIncreaseReplicationFactorRequestRequestTypeDef",
    {
        "ClusterName": str,
        "NewReplicationFactor": int,
    },
)
_OptionalIncreaseReplicationFactorRequestRequestTypeDef = TypedDict(
    "_OptionalIncreaseReplicationFactorRequestRequestTypeDef",
    {
        "AvailabilityZones": List[str],
    },
    total=False,
)

class IncreaseReplicationFactorRequestRequestTypeDef(
    _RequiredIncreaseReplicationFactorRequestRequestTypeDef,
    _OptionalIncreaseReplicationFactorRequestRequestTypeDef,
):
    pass

IncreaseReplicationFactorResponseTypeDef = TypedDict(
    "IncreaseReplicationFactorResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsRequestRequestTypeDef",
    {
        "ResourceName": str,
    },
)
_OptionalListTagsRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListTagsRequestRequestTypeDef(
    _RequiredListTagsRequestRequestTypeDef, _OptionalListTagsRequestRequestTypeDef
):
    pass

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "NodeId": str,
        "Endpoint": "EndpointTypeDef",
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)

NodeTypeSpecificValueTypeDef = TypedDict(
    "NodeTypeSpecificValueTypeDef",
    {
        "NodeType": str,
        "Value": str,
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

ParameterGroupStatusTypeDef = TypedDict(
    "ParameterGroupStatusTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "NodeIdsToReboot": List[str],
    },
    total=False,
)

ParameterGroupTypeDef = TypedDict(
    "ParameterGroupTypeDef",
    {
        "ParameterGroupName": str,
        "Description": str,
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
        "ParameterType": ParameterTypeType,
        "ParameterValue": str,
        "NodeTypeSpecificValues": List["NodeTypeSpecificValueTypeDef"],
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": IsModifiableType,
        "ChangeType": ChangeTypeType,
    },
    total=False,
)

RebootNodeRequestRequestTypeDef = TypedDict(
    "RebootNodeRequestRequestTypeDef",
    {
        "ClusterName": str,
        "NodeId": str,
    },
)

RebootNodeResponseTypeDef = TypedDict(
    "RebootNodeResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
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

SSEDescriptionTypeDef = TypedDict(
    "SSEDescriptionTypeDef",
    {
        "Status": SSEStatusType,
    },
    total=False,
)

SSESpecificationTypeDef = TypedDict(
    "SSESpecificationTypeDef",
    {
        "Enabled": bool,
    },
)

SecurityGroupMembershipTypeDef = TypedDict(
    "SecurityGroupMembershipTypeDef",
    {
        "SecurityGroupIdentifier": str,
        "Status": str,
    },
    total=False,
)

SubnetGroupTypeDef = TypedDict(
    "SubnetGroupTypeDef",
    {
        "SubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "Subnets": List["SubnetTypeDef"],
    },
    total=False,
)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": str,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceName": str,
        "Tags": List["TagTypeDef"],
    },
)

TagResourceResponseTypeDef = TypedDict(
    "TagResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
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

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceName": str,
        "TagKeys": List[str],
    },
)

UntagResourceResponseTypeDef = TypedDict(
    "UntagResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
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
        "PreferredMaintenanceWindow": str,
        "NotificationTopicArn": str,
        "NotificationTopicStatus": str,
        "ParameterGroupName": str,
        "SecurityGroupIds": List[str],
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
