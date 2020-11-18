# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for dax service client

Usage::

    ```python
    import boto3
    from mypy_boto3_dax import DAXClient

    client: DAXClient = boto3.client("dax")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_dax.paginator import (
    DescribeClustersPaginator,
    DescribeDefaultParametersPaginator,
    DescribeEventsPaginator,
    DescribeParameterGroupsPaginator,
    DescribeParametersPaginator,
    DescribeSubnetGroupsPaginator,
    ListTagsPaginator,
)
from mypy_boto3_dax.type_defs import (
    CreateClusterResponseTypeDef,
    CreateParameterGroupResponseTypeDef,
    CreateSubnetGroupResponseTypeDef,
    DecreaseReplicationFactorResponseTypeDef,
    DeleteClusterResponseTypeDef,
    DeleteParameterGroupResponseTypeDef,
    DeleteSubnetGroupResponseTypeDef,
    DescribeClustersResponseTypeDef,
    DescribeDefaultParametersResponseTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeParameterGroupsResponseTypeDef,
    DescribeParametersResponseTypeDef,
    DescribeSubnetGroupsResponseTypeDef,
    IncreaseReplicationFactorResponseTypeDef,
    ListTagsResponseTypeDef,
    ParameterNameValueTypeDef,
    RebootNodeResponseTypeDef,
    SSESpecificationTypeDef,
    TagResourceResponseTypeDef,
    TagTypeDef,
    UntagResourceResponseTypeDef,
    UpdateClusterResponseTypeDef,
    UpdateParameterGroupResponseTypeDef,
    UpdateSubnetGroupResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DAXClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ClusterAlreadyExistsFault: Type[BotocoreClientError]
    ClusterNotFoundFault: Type[BotocoreClientError]
    ClusterQuotaForCustomerExceededFault: Type[BotocoreClientError]
    InsufficientClusterCapacityFault: Type[BotocoreClientError]
    InvalidARNFault: Type[BotocoreClientError]
    InvalidClusterStateFault: Type[BotocoreClientError]
    InvalidParameterCombinationException: Type[BotocoreClientError]
    InvalidParameterGroupStateFault: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidSubnet: Type[BotocoreClientError]
    InvalidVPCNetworkStateFault: Type[BotocoreClientError]
    NodeNotFoundFault: Type[BotocoreClientError]
    NodeQuotaForClusterExceededFault: Type[BotocoreClientError]
    NodeQuotaForCustomerExceededFault: Type[BotocoreClientError]
    ParameterGroupAlreadyExistsFault: Type[BotocoreClientError]
    ParameterGroupNotFoundFault: Type[BotocoreClientError]
    ParameterGroupQuotaExceededFault: Type[BotocoreClientError]
    ServiceLinkedRoleNotFoundFault: Type[BotocoreClientError]
    SubnetGroupAlreadyExistsFault: Type[BotocoreClientError]
    SubnetGroupInUseFault: Type[BotocoreClientError]
    SubnetGroupNotFoundFault: Type[BotocoreClientError]
    SubnetGroupQuotaExceededFault: Type[BotocoreClientError]
    SubnetInUse: Type[BotocoreClientError]
    SubnetQuotaExceededFault: Type[BotocoreClientError]
    TagNotFoundFault: Type[BotocoreClientError]
    TagQuotaPerResourceExceeded: Type[BotocoreClientError]


class DAXClient:
    """
    [DAX.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client.can_paginate)
        """

    def create_cluster(
        self,
        ClusterName: str,
        NodeType: str,
        ReplicationFactor: int,
        IamRoleArn: str,
        Description: str = None,
        AvailabilityZones: List[str] = None,
        SubnetGroupName: str = None,
        SecurityGroupIds: List[str] = None,
        PreferredMaintenanceWindow: str = None,
        NotificationTopicArn: str = None,
        ParameterGroupName: str = None,
        Tags: List["TagTypeDef"] = None,
        SSESpecification: SSESpecificationTypeDef = None,
    ) -> CreateClusterResponseTypeDef:
        """
        [Client.create_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client.create_cluster)
        """

    def create_parameter_group(
        self, ParameterGroupName: str, Description: str = None
    ) -> CreateParameterGroupResponseTypeDef:
        """
        [Client.create_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client.create_parameter_group)
        """

    def create_subnet_group(
        self, SubnetGroupName: str, SubnetIds: List[str], Description: str = None
    ) -> CreateSubnetGroupResponseTypeDef:
        """
        [Client.create_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client.create_subnet_group)
        """

    def decrease_replication_factor(
        self,
        ClusterName: str,
        NewReplicationFactor: int,
        AvailabilityZones: List[str] = None,
        NodeIdsToRemove: List[str] = None,
    ) -> DecreaseReplicationFactorResponseTypeDef:
        """
        [Client.decrease_replication_factor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client.decrease_replication_factor)
        """

    def delete_cluster(self, ClusterName: str) -> DeleteClusterResponseTypeDef:
        """
        [Client.delete_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client.delete_cluster)
        """

    def delete_parameter_group(
        self, ParameterGroupName: str
    ) -> DeleteParameterGroupResponseTypeDef:
        """
        [Client.delete_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client.delete_parameter_group)
        """

    def delete_subnet_group(self, SubnetGroupName: str) -> DeleteSubnetGroupResponseTypeDef:
        """
        [Client.delete_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client.delete_subnet_group)
        """

    def describe_clusters(
        self, ClusterNames: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeClustersResponseTypeDef:
        """
        [Client.describe_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client.describe_clusters)
        """

    def describe_default_parameters(
        self, MaxResults: int = None, NextToken: str = None
    ) -> DescribeDefaultParametersResponseTypeDef:
        """
        [Client.describe_default_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client.describe_default_parameters)
        """

    def describe_events(
        self,
        SourceName: str = None,
        SourceType: Literal["CLUSTER", "PARAMETER_GROUP", "SUBNET_GROUP"] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeEventsResponseTypeDef:
        """
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client.describe_events)
        """

    def describe_parameter_groups(
        self, ParameterGroupNames: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeParameterGroupsResponseTypeDef:
        """
        [Client.describe_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client.describe_parameter_groups)
        """

    def describe_parameters(
        self,
        ParameterGroupName: str,
        Source: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeParametersResponseTypeDef:
        """
        [Client.describe_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client.describe_parameters)
        """

    def describe_subnet_groups(
        self, SubnetGroupNames: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeSubnetGroupsResponseTypeDef:
        """
        [Client.describe_subnet_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client.describe_subnet_groups)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client.generate_presigned_url)
        """

    def increase_replication_factor(
        self, ClusterName: str, NewReplicationFactor: int, AvailabilityZones: List[str] = None
    ) -> IncreaseReplicationFactorResponseTypeDef:
        """
        [Client.increase_replication_factor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client.increase_replication_factor)
        """

    def list_tags(self, ResourceName: str, NextToken: str = None) -> ListTagsResponseTypeDef:
        """
        [Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client.list_tags)
        """

    def reboot_node(self, ClusterName: str, NodeId: str) -> RebootNodeResponseTypeDef:
        """
        [Client.reboot_node documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client.reboot_node)
        """

    def tag_resource(
        self, ResourceName: str, Tags: List["TagTypeDef"]
    ) -> TagResourceResponseTypeDef:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client.tag_resource)
        """

    def untag_resource(self, ResourceName: str, TagKeys: List[str]) -> UntagResourceResponseTypeDef:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client.untag_resource)
        """

    def update_cluster(
        self,
        ClusterName: str,
        Description: str = None,
        PreferredMaintenanceWindow: str = None,
        NotificationTopicArn: str = None,
        NotificationTopicStatus: str = None,
        ParameterGroupName: str = None,
        SecurityGroupIds: List[str] = None,
    ) -> UpdateClusterResponseTypeDef:
        """
        [Client.update_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client.update_cluster)
        """

    def update_parameter_group(
        self, ParameterGroupName: str, ParameterNameValues: List[ParameterNameValueTypeDef]
    ) -> UpdateParameterGroupResponseTypeDef:
        """
        [Client.update_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client.update_parameter_group)
        """

    def update_subnet_group(
        self, SubnetGroupName: str, Description: str = None, SubnetIds: List[str] = None
    ) -> UpdateSubnetGroupResponseTypeDef:
        """
        [Client.update_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Client.update_subnet_group)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_clusters"]
    ) -> DescribeClustersPaginator:
        """
        [Paginator.DescribeClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Paginator.DescribeClusters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_default_parameters"]
    ) -> DescribeDefaultParametersPaginator:
        """
        [Paginator.DescribeDefaultParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Paginator.DescribeDefaultParameters)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Paginator.DescribeEvents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_parameter_groups"]
    ) -> DescribeParameterGroupsPaginator:
        """
        [Paginator.DescribeParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Paginator.DescribeParameterGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_parameters"]
    ) -> DescribeParametersPaginator:
        """
        [Paginator.DescribeParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Paginator.DescribeParameters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_subnet_groups"]
    ) -> DescribeSubnetGroupsPaginator:
        """
        [Paginator.DescribeSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Paginator.DescribeSubnetGroups)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tags"]) -> ListTagsPaginator:
        """
        [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/dax.html#DAX.Paginator.ListTags)
        """
