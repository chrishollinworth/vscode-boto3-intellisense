"""
Type annotations for dax service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dax/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_dax.type_defs import EndpointTypeDef

    data: EndpointTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ChangeTypeType,
    ClusterEndpointEncryptionTypeType,
    IsModifiableType,
    ParameterTypeType,
    SourceTypeType,
    SSEStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ClusterTypeDef",
    "CreateClusterRequestTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateParameterGroupRequestTypeDef",
    "CreateParameterGroupResponseTypeDef",
    "CreateSubnetGroupRequestTypeDef",
    "CreateSubnetGroupResponseTypeDef",
    "DecreaseReplicationFactorRequestTypeDef",
    "DecreaseReplicationFactorResponseTypeDef",
    "DeleteClusterRequestTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteParameterGroupRequestTypeDef",
    "DeleteParameterGroupResponseTypeDef",
    "DeleteSubnetGroupRequestTypeDef",
    "DeleteSubnetGroupResponseTypeDef",
    "DescribeClustersRequestPaginateTypeDef",
    "DescribeClustersRequestTypeDef",
    "DescribeClustersResponseTypeDef",
    "DescribeDefaultParametersRequestPaginateTypeDef",
    "DescribeDefaultParametersRequestTypeDef",
    "DescribeDefaultParametersResponseTypeDef",
    "DescribeEventsRequestPaginateTypeDef",
    "DescribeEventsRequestTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeParameterGroupsRequestPaginateTypeDef",
    "DescribeParameterGroupsRequestTypeDef",
    "DescribeParameterGroupsResponseTypeDef",
    "DescribeParametersRequestPaginateTypeDef",
    "DescribeParametersRequestTypeDef",
    "DescribeParametersResponseTypeDef",
    "DescribeSubnetGroupsRequestPaginateTypeDef",
    "DescribeSubnetGroupsRequestTypeDef",
    "DescribeSubnetGroupsResponseTypeDef",
    "EndpointTypeDef",
    "EventTypeDef",
    "IncreaseReplicationFactorRequestTypeDef",
    "IncreaseReplicationFactorResponseTypeDef",
    "ListTagsRequestPaginateTypeDef",
    "ListTagsRequestTypeDef",
    "ListTagsResponseTypeDef",
    "NodeTypeDef",
    "NodeTypeSpecificValueTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterGroupStatusTypeDef",
    "ParameterGroupTypeDef",
    "ParameterNameValueTypeDef",
    "ParameterTypeDef",
    "RebootNodeRequestTypeDef",
    "RebootNodeResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SSEDescriptionTypeDef",
    "SSESpecificationTypeDef",
    "SecurityGroupMembershipTypeDef",
    "SubnetGroupTypeDef",
    "SubnetTypeDef",
    "TagResourceRequestTypeDef",
    "TagResourceResponseTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UntagResourceResponseTypeDef",
    "UpdateClusterRequestTypeDef",
    "UpdateClusterResponseTypeDef",
    "UpdateParameterGroupRequestTypeDef",
    "UpdateParameterGroupResponseTypeDef",
    "UpdateSubnetGroupRequestTypeDef",
    "UpdateSubnetGroupResponseTypeDef",
)

class EndpointTypeDef(TypedDict):
    Address: NotRequired[str]
    Port: NotRequired[int]
    URL: NotRequired[str]

class NotificationConfigurationTypeDef(TypedDict):
    TopicArn: NotRequired[str]
    TopicStatus: NotRequired[str]

class ParameterGroupStatusTypeDef(TypedDict):
    ParameterGroupName: NotRequired[str]
    ParameterApplyStatus: NotRequired[str]
    NodeIdsToReboot: NotRequired[List[str]]

class SSEDescriptionTypeDef(TypedDict):
    Status: NotRequired[SSEStatusType]

class SecurityGroupMembershipTypeDef(TypedDict):
    SecurityGroupIdentifier: NotRequired[str]
    Status: NotRequired[str]

class SSESpecificationTypeDef(TypedDict):
    Enabled: bool

class TagTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateParameterGroupRequestTypeDef(TypedDict):
    ParameterGroupName: str
    Description: NotRequired[str]

class ParameterGroupTypeDef(TypedDict):
    ParameterGroupName: NotRequired[str]
    Description: NotRequired[str]

class CreateSubnetGroupRequestTypeDef(TypedDict):
    SubnetGroupName: str
    SubnetIds: Sequence[str]
    Description: NotRequired[str]

class DecreaseReplicationFactorRequestTypeDef(TypedDict):
    ClusterName: str
    NewReplicationFactor: int
    AvailabilityZones: NotRequired[Sequence[str]]
    NodeIdsToRemove: NotRequired[Sequence[str]]

class DeleteClusterRequestTypeDef(TypedDict):
    ClusterName: str

class DeleteParameterGroupRequestTypeDef(TypedDict):
    ParameterGroupName: str

class DeleteSubnetGroupRequestTypeDef(TypedDict):
    SubnetGroupName: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeClustersRequestTypeDef(TypedDict):
    ClusterNames: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeDefaultParametersRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class EventTypeDef(TypedDict):
    SourceName: NotRequired[str]
    SourceType: NotRequired[SourceTypeType]
    Message: NotRequired[str]
    Date: NotRequired[datetime]

class DescribeParameterGroupsRequestTypeDef(TypedDict):
    ParameterGroupNames: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeParametersRequestTypeDef(TypedDict):
    ParameterGroupName: str
    Source: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeSubnetGroupsRequestTypeDef(TypedDict):
    SubnetGroupNames: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class IncreaseReplicationFactorRequestTypeDef(TypedDict):
    ClusterName: str
    NewReplicationFactor: int
    AvailabilityZones: NotRequired[Sequence[str]]

class ListTagsRequestTypeDef(TypedDict):
    ResourceName: str
    NextToken: NotRequired[str]

class NodeTypeSpecificValueTypeDef(TypedDict):
    NodeType: NotRequired[str]
    Value: NotRequired[str]

class ParameterNameValueTypeDef(TypedDict):
    ParameterName: NotRequired[str]
    ParameterValue: NotRequired[str]

class RebootNodeRequestTypeDef(TypedDict):
    ClusterName: str
    NodeId: str

class SubnetTypeDef(TypedDict):
    SubnetIdentifier: NotRequired[str]
    SubnetAvailabilityZone: NotRequired[str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceName: str
    TagKeys: Sequence[str]

class UpdateClusterRequestTypeDef(TypedDict):
    ClusterName: str
    Description: NotRequired[str]
    PreferredMaintenanceWindow: NotRequired[str]
    NotificationTopicArn: NotRequired[str]
    NotificationTopicStatus: NotRequired[str]
    ParameterGroupName: NotRequired[str]
    SecurityGroupIds: NotRequired[Sequence[str]]

class UpdateSubnetGroupRequestTypeDef(TypedDict):
    SubnetGroupName: str
    Description: NotRequired[str]
    SubnetIds: NotRequired[Sequence[str]]

class NodeTypeDef(TypedDict):
    NodeId: NotRequired[str]
    Endpoint: NotRequired[EndpointTypeDef]
    NodeCreateTime: NotRequired[datetime]
    AvailabilityZone: NotRequired[str]
    NodeStatus: NotRequired[str]
    ParameterGroupStatus: NotRequired[str]

class CreateClusterRequestTypeDef(TypedDict):
    ClusterName: str
    NodeType: str
    ReplicationFactor: int
    IamRoleArn: str
    Description: NotRequired[str]
    AvailabilityZones: NotRequired[Sequence[str]]
    SubnetGroupName: NotRequired[str]
    SecurityGroupIds: NotRequired[Sequence[str]]
    PreferredMaintenanceWindow: NotRequired[str]
    NotificationTopicArn: NotRequired[str]
    ParameterGroupName: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    SSESpecification: NotRequired[SSESpecificationTypeDef]
    ClusterEndpointEncryptionType: NotRequired[ClusterEndpointEncryptionTypeType]

class TagResourceRequestTypeDef(TypedDict):
    ResourceName: str
    Tags: Sequence[TagTypeDef]

class DeleteParameterGroupResponseTypeDef(TypedDict):
    DeletionMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSubnetGroupResponseTypeDef(TypedDict):
    DeletionMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class TagResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UntagResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateParameterGroupResponseTypeDef(TypedDict):
    ParameterGroup: ParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeParameterGroupsResponseTypeDef(TypedDict):
    ParameterGroups: List[ParameterGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateParameterGroupResponseTypeDef(TypedDict):
    ParameterGroup: ParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeClustersRequestPaginateTypeDef(TypedDict):
    ClusterNames: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDefaultParametersRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeParameterGroupsRequestPaginateTypeDef(TypedDict):
    ParameterGroupNames: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeParametersRequestPaginateTypeDef(TypedDict):
    ParameterGroupName: str
    Source: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeSubnetGroupsRequestPaginateTypeDef(TypedDict):
    SubnetGroupNames: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsRequestPaginateTypeDef(TypedDict):
    ResourceName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEventsRequestPaginateTypeDef(TypedDict):
    SourceName: NotRequired[str]
    SourceType: NotRequired[SourceTypeType]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    Duration: NotRequired[int]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEventsRequestTypeDef(TypedDict):
    SourceName: NotRequired[str]
    SourceType: NotRequired[SourceTypeType]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    Duration: NotRequired[int]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeEventsResponseTypeDef(TypedDict):
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ParameterTypeDef(TypedDict):
    ParameterName: NotRequired[str]
    ParameterType: NotRequired[ParameterTypeType]
    ParameterValue: NotRequired[str]
    NodeTypeSpecificValues: NotRequired[List[NodeTypeSpecificValueTypeDef]]
    Description: NotRequired[str]
    Source: NotRequired[str]
    DataType: NotRequired[str]
    AllowedValues: NotRequired[str]
    IsModifiable: NotRequired[IsModifiableType]
    ChangeType: NotRequired[ChangeTypeType]

class UpdateParameterGroupRequestTypeDef(TypedDict):
    ParameterGroupName: str
    ParameterNameValues: Sequence[ParameterNameValueTypeDef]

class SubnetGroupTypeDef(TypedDict):
    SubnetGroupName: NotRequired[str]
    Description: NotRequired[str]
    VpcId: NotRequired[str]
    Subnets: NotRequired[List[SubnetTypeDef]]

class ClusterTypeDef(TypedDict):
    ClusterName: NotRequired[str]
    Description: NotRequired[str]
    ClusterArn: NotRequired[str]
    TotalNodes: NotRequired[int]
    ActiveNodes: NotRequired[int]
    NodeType: NotRequired[str]
    Status: NotRequired[str]
    ClusterDiscoveryEndpoint: NotRequired[EndpointTypeDef]
    NodeIdsToRemove: NotRequired[List[str]]
    Nodes: NotRequired[List[NodeTypeDef]]
    PreferredMaintenanceWindow: NotRequired[str]
    NotificationConfiguration: NotRequired[NotificationConfigurationTypeDef]
    SubnetGroup: NotRequired[str]
    SecurityGroups: NotRequired[List[SecurityGroupMembershipTypeDef]]
    IamRoleArn: NotRequired[str]
    ParameterGroup: NotRequired[ParameterGroupStatusTypeDef]
    SSEDescription: NotRequired[SSEDescriptionTypeDef]
    ClusterEndpointEncryptionType: NotRequired[ClusterEndpointEncryptionTypeType]

class DescribeDefaultParametersResponseTypeDef(TypedDict):
    Parameters: List[ParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeParametersResponseTypeDef(TypedDict):
    Parameters: List[ParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateSubnetGroupResponseTypeDef(TypedDict):
    SubnetGroup: SubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSubnetGroupsResponseTypeDef(TypedDict):
    SubnetGroups: List[SubnetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateSubnetGroupResponseTypeDef(TypedDict):
    SubnetGroup: SubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterResponseTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DecreaseReplicationFactorResponseTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterResponseTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeClustersResponseTypeDef(TypedDict):
    Clusters: List[ClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class IncreaseReplicationFactorResponseTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RebootNodeResponseTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterResponseTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
