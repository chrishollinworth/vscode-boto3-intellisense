# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for globalaccelerator service client

Usage::

    ```python
    import boto3
    from mypy_boto3_globalaccelerator import GlobalAcceleratorClient

    client: GlobalAcceleratorClient = boto3.client("globalaccelerator")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_globalaccelerator.paginator import (
    ListAcceleratorsPaginator,
    ListEndpointGroupsPaginator,
    ListListenersPaginator,
)
from mypy_boto3_globalaccelerator.type_defs import (
    AdvertiseByoipCidrResponseTypeDef,
    CidrAuthorizationContextTypeDef,
    CreateAcceleratorResponseTypeDef,
    CreateEndpointGroupResponseTypeDef,
    CreateListenerResponseTypeDef,
    DeprovisionByoipCidrResponseTypeDef,
    DescribeAcceleratorAttributesResponseTypeDef,
    DescribeAcceleratorResponseTypeDef,
    DescribeEndpointGroupResponseTypeDef,
    DescribeListenerResponseTypeDef,
    EndpointConfigurationTypeDef,
    ListAcceleratorsResponseTypeDef,
    ListByoipCidrsResponseTypeDef,
    ListEndpointGroupsResponseTypeDef,
    ListListenersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PortRangeTypeDef,
    ProvisionByoipCidrResponseTypeDef,
    TagTypeDef,
    UpdateAcceleratorAttributesResponseTypeDef,
    UpdateAcceleratorResponseTypeDef,
    UpdateEndpointGroupResponseTypeDef,
    UpdateListenerResponseTypeDef,
    WithdrawByoipCidrResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GlobalAcceleratorClient",)


class Exceptions:
    AcceleratorNotDisabledException: Type[Boto3ClientError]
    AcceleratorNotFoundException: Type[Boto3ClientError]
    AccessDeniedException: Type[Boto3ClientError]
    AssociatedEndpointGroupFoundException: Type[Boto3ClientError]
    AssociatedListenerFoundException: Type[Boto3ClientError]
    ByoipCidrNotFoundException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    EndpointGroupAlreadyExistsException: Type[Boto3ClientError]
    EndpointGroupNotFoundException: Type[Boto3ClientError]
    IncorrectCidrStateException: Type[Boto3ClientError]
    InternalServiceErrorException: Type[Boto3ClientError]
    InvalidArgumentException: Type[Boto3ClientError]
    InvalidNextTokenException: Type[Boto3ClientError]
    InvalidPortRangeException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    ListenerNotFoundException: Type[Boto3ClientError]


class GlobalAcceleratorClient:
    """
    [GlobalAccelerator.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client)
    """

    exceptions: Exceptions

    def advertise_byoip_cidr(self, Cidr: str) -> AdvertiseByoipCidrResponseTypeDef:
        """
        [Client.advertise_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.advertise_byoip_cidr)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.can_paginate)
        """

    def create_accelerator(
        self,
        Name: str,
        IdempotencyToken: str,
        IpAddressType: Literal["IPV4"] = None,
        IpAddresses: List[str] = None,
        Enabled: bool = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateAcceleratorResponseTypeDef:
        """
        [Client.create_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_accelerator)
        """

    def create_endpoint_group(
        self,
        ListenerArn: str,
        EndpointGroupRegion: str,
        IdempotencyToken: str,
        EndpointConfigurations: List[EndpointConfigurationTypeDef] = None,
        TrafficDialPercentage: float = None,
        HealthCheckPort: int = None,
        HealthCheckProtocol: Literal["TCP", "HTTP", "HTTPS"] = None,
        HealthCheckPath: str = None,
        HealthCheckIntervalSeconds: int = None,
        ThresholdCount: int = None,
    ) -> CreateEndpointGroupResponseTypeDef:
        """
        [Client.create_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_endpoint_group)
        """

    def create_listener(
        self,
        AcceleratorArn: str,
        PortRanges: List["PortRangeTypeDef"],
        Protocol: Literal["TCP", "UDP"],
        IdempotencyToken: str,
        ClientAffinity: Literal["NONE", "SOURCE_IP"] = None,
    ) -> CreateListenerResponseTypeDef:
        """
        [Client.create_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_listener)
        """

    def delete_accelerator(self, AcceleratorArn: str) -> None:
        """
        [Client.delete_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_accelerator)
        """

    def delete_endpoint_group(self, EndpointGroupArn: str) -> None:
        """
        [Client.delete_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_endpoint_group)
        """

    def delete_listener(self, ListenerArn: str) -> None:
        """
        [Client.delete_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_listener)
        """

    def deprovision_byoip_cidr(self, Cidr: str) -> DeprovisionByoipCidrResponseTypeDef:
        """
        [Client.deprovision_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.deprovision_byoip_cidr)
        """

    def describe_accelerator(self, AcceleratorArn: str) -> DescribeAcceleratorResponseTypeDef:
        """
        [Client.describe_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_accelerator)
        """

    def describe_accelerator_attributes(
        self, AcceleratorArn: str
    ) -> DescribeAcceleratorAttributesResponseTypeDef:
        """
        [Client.describe_accelerator_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_accelerator_attributes)
        """

    def describe_endpoint_group(
        self, EndpointGroupArn: str
    ) -> DescribeEndpointGroupResponseTypeDef:
        """
        [Client.describe_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_endpoint_group)
        """

    def describe_listener(self, ListenerArn: str) -> DescribeListenerResponseTypeDef:
        """
        [Client.describe_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_listener)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.generate_presigned_url)
        """

    def list_accelerators(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListAcceleratorsResponseTypeDef:
        """
        [Client.list_accelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_accelerators)
        """

    def list_byoip_cidrs(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListByoipCidrsResponseTypeDef:
        """
        [Client.list_byoip_cidrs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_byoip_cidrs)
        """

    def list_endpoint_groups(
        self, ListenerArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListEndpointGroupsResponseTypeDef:
        """
        [Client.list_endpoint_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_endpoint_groups)
        """

    def list_listeners(
        self, AcceleratorArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListListenersResponseTypeDef:
        """
        [Client.list_listeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_listeners)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_tags_for_resource)
        """

    def provision_byoip_cidr(
        self, Cidr: str, CidrAuthorizationContext: CidrAuthorizationContextTypeDef
    ) -> ProvisionByoipCidrResponseTypeDef:
        """
        [Client.provision_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.provision_byoip_cidr)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.untag_resource)
        """

    def update_accelerator(
        self,
        AcceleratorArn: str,
        Name: str = None,
        IpAddressType: Literal["IPV4"] = None,
        Enabled: bool = None,
    ) -> UpdateAcceleratorResponseTypeDef:
        """
        [Client.update_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_accelerator)
        """

    def update_accelerator_attributes(
        self,
        AcceleratorArn: str,
        FlowLogsEnabled: bool = None,
        FlowLogsS3Bucket: str = None,
        FlowLogsS3Prefix: str = None,
    ) -> UpdateAcceleratorAttributesResponseTypeDef:
        """
        [Client.update_accelerator_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_accelerator_attributes)
        """

    def update_endpoint_group(
        self,
        EndpointGroupArn: str,
        EndpointConfigurations: List[EndpointConfigurationTypeDef] = None,
        TrafficDialPercentage: float = None,
        HealthCheckPort: int = None,
        HealthCheckProtocol: Literal["TCP", "HTTP", "HTTPS"] = None,
        HealthCheckPath: str = None,
        HealthCheckIntervalSeconds: int = None,
        ThresholdCount: int = None,
    ) -> UpdateEndpointGroupResponseTypeDef:
        """
        [Client.update_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_endpoint_group)
        """

    def update_listener(
        self,
        ListenerArn: str,
        PortRanges: List["PortRangeTypeDef"] = None,
        Protocol: Literal["TCP", "UDP"] = None,
        ClientAffinity: Literal["NONE", "SOURCE_IP"] = None,
    ) -> UpdateListenerResponseTypeDef:
        """
        [Client.update_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_listener)
        """

    def withdraw_byoip_cidr(self, Cidr: str) -> WithdrawByoipCidrResponseTypeDef:
        """
        [Client.withdraw_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Client.withdraw_byoip_cidr)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_accelerators"]
    ) -> ListAcceleratorsPaginator:
        """
        [Paginator.ListAccelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListAccelerators)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_endpoint_groups"]
    ) -> ListEndpointGroupsPaginator:
        """
        [Paginator.ListEndpointGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListEndpointGroups)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_listeners"]) -> ListListenersPaginator:
        """
        [Paginator.ListListeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListListeners)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
