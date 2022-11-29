"""
Type annotations for dax service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_dax import DAXClient

    client: DAXClient = boto3.client("dax")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import ClusterEndpointEncryptionTypeType, SourceTypeType
from .paginator import (
    DescribeClustersPaginator,
    DescribeDefaultParametersPaginator,
    DescribeEventsPaginator,
    DescribeParameterGroupsPaginator,
    DescribeParametersPaginator,
    DescribeSubnetGroupsPaginator,
    ListTagsPaginator,
)
from .type_defs import (
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
    ServiceQuotaExceededException: Type[BotocoreClientError]
    SubnetGroupAlreadyExistsFault: Type[BotocoreClientError]
    SubnetGroupInUseFault: Type[BotocoreClientError]
    SubnetGroupNotFoundFault: Type[BotocoreClientError]
    SubnetGroupQuotaExceededFault: Type[BotocoreClientError]
    SubnetInUse: Type[BotocoreClientError]
    SubnetQuotaExceededFault: Type[BotocoreClientError]
    TagNotFoundFault: Type[BotocoreClientError]
    TagQuotaPerResourceExceeded: Type[BotocoreClientError]

class DAXClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DAXClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#close)
        """
    def create_cluster(
        self,
        *,
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
        SSESpecification: "SSESpecificationTypeDef" = None,
        ClusterEndpointEncryptionType: ClusterEndpointEncryptionTypeType = None
    ) -> CreateClusterResponseTypeDef:
        """
        Creates a DAX cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.create_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#create_cluster)
        """
    def create_parameter_group(
        self, *, ParameterGroupName: str, Description: str = None
    ) -> CreateParameterGroupResponseTypeDef:
        """
        Creates a new parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.create_parameter_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#create_parameter_group)
        """
    def create_subnet_group(
        self, *, SubnetGroupName: str, SubnetIds: List[str], Description: str = None
    ) -> CreateSubnetGroupResponseTypeDef:
        """
        Creates a new subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.create_subnet_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#create_subnet_group)
        """
    def decrease_replication_factor(
        self,
        *,
        ClusterName: str,
        NewReplicationFactor: int,
        AvailabilityZones: List[str] = None,
        NodeIdsToRemove: List[str] = None
    ) -> DecreaseReplicationFactorResponseTypeDef:
        """
        Removes one or more nodes from a DAX cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.decrease_replication_factor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#decrease_replication_factor)
        """
    def delete_cluster(self, *, ClusterName: str) -> DeleteClusterResponseTypeDef:
        """
        Deletes a previously provisioned DAX cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.delete_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#delete_cluster)
        """
    def delete_parameter_group(
        self, *, ParameterGroupName: str
    ) -> DeleteParameterGroupResponseTypeDef:
        """
        Deletes the specified parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.delete_parameter_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#delete_parameter_group)
        """
    def delete_subnet_group(self, *, SubnetGroupName: str) -> DeleteSubnetGroupResponseTypeDef:
        """
        Deletes a subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.delete_subnet_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#delete_subnet_group)
        """
    def describe_clusters(
        self, *, ClusterNames: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeClustersResponseTypeDef:
        """
        Returns information about all provisioned DAX clusters if no cluster identifier
        is specified, or about a specific DAX cluster if a cluster identifier is
        supplied.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.describe_clusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#describe_clusters)
        """
    def describe_default_parameters(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> DescribeDefaultParametersResponseTypeDef:
        """
        Returns the default system parameter information for the DAX caching software.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.describe_default_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#describe_default_parameters)
        """
    def describe_events(
        self,
        *,
        SourceName: str = None,
        SourceType: SourceTypeType = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        Duration: int = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeEventsResponseTypeDef:
        """
        Returns events related to DAX clusters and parameter groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.describe_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#describe_events)
        """
    def describe_parameter_groups(
        self,
        *,
        ParameterGroupNames: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeParameterGroupsResponseTypeDef:
        """
        Returns a list of parameter group descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.describe_parameter_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#describe_parameter_groups)
        """
    def describe_parameters(
        self,
        *,
        ParameterGroupName: str,
        Source: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeParametersResponseTypeDef:
        """
        Returns the detailed parameter list for a particular parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.describe_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#describe_parameters)
        """
    def describe_subnet_groups(
        self, *, SubnetGroupNames: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeSubnetGroupsResponseTypeDef:
        """
        Returns a list of subnet group descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.describe_subnet_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#describe_subnet_groups)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#generate_presigned_url)
        """
    def increase_replication_factor(
        self, *, ClusterName: str, NewReplicationFactor: int, AvailabilityZones: List[str] = None
    ) -> IncreaseReplicationFactorResponseTypeDef:
        """
        Adds one or more nodes to a DAX cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.increase_replication_factor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#increase_replication_factor)
        """
    def list_tags(self, *, ResourceName: str, NextToken: str = None) -> ListTagsResponseTypeDef:
        """
        List all of the tags for a DAX cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.list_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#list_tags)
        """
    def reboot_node(self, *, ClusterName: str, NodeId: str) -> RebootNodeResponseTypeDef:
        """
        Reboots a single node of a DAX cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.reboot_node)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#reboot_node)
        """
    def tag_resource(
        self, *, ResourceName: str, Tags: List["TagTypeDef"]
    ) -> TagResourceResponseTypeDef:
        """
        Associates a set of tags with a DAX resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#tag_resource)
        """
    def untag_resource(
        self, *, ResourceName: str, TagKeys: List[str]
    ) -> UntagResourceResponseTypeDef:
        """
        Removes the association of tags from a DAX resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#untag_resource)
        """
    def update_cluster(
        self,
        *,
        ClusterName: str,
        Description: str = None,
        PreferredMaintenanceWindow: str = None,
        NotificationTopicArn: str = None,
        NotificationTopicStatus: str = None,
        ParameterGroupName: str = None,
        SecurityGroupIds: List[str] = None
    ) -> UpdateClusterResponseTypeDef:
        """
        Modifies the settings for a DAX cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.update_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#update_cluster)
        """
    def update_parameter_group(
        self, *, ParameterGroupName: str, ParameterNameValues: List["ParameterNameValueTypeDef"]
    ) -> UpdateParameterGroupResponseTypeDef:
        """
        Modifies the parameters of a parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.update_parameter_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#update_parameter_group)
        """
    def update_subnet_group(
        self, *, SubnetGroupName: str, Description: str = None, SubnetIds: List[str] = None
    ) -> UpdateSubnetGroupResponseTypeDef:
        """
        Modifies an existing subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Client.update_subnet_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/client.html#update_subnet_group)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_clusters"]
    ) -> DescribeClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Paginator.DescribeClusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/paginators.html#describeclusterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_default_parameters"]
    ) -> DescribeDefaultParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Paginator.DescribeDefaultParameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/paginators.html#describedefaultparameterspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Paginator.DescribeEvents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/paginators.html#describeeventspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_parameter_groups"]
    ) -> DescribeParameterGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Paginator.DescribeParameterGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/paginators.html#describeparametergroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_parameters"]
    ) -> DescribeParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Paginator.DescribeParameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/paginators.html#describeparameterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_subnet_groups"]
    ) -> DescribeSubnetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Paginator.DescribeSubnetGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/paginators.html#describesubnetgroupspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_tags"]) -> ListTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/dax.html#DAX.Paginator.ListTags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/paginators.html#listtagspaginator)
        """
