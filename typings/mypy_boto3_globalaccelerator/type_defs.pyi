"""
Type annotations for globalaccelerator service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_globalaccelerator.type_defs import AcceleratorAttributesTypeDef

    data: AcceleratorAttributesTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    AcceleratorStatusType,
    ByoipCidrStateType,
    ClientAffinityType,
    CustomRoutingAcceleratorStatusType,
    CustomRoutingDestinationTrafficStateType,
    CustomRoutingProtocolType,
    HealthCheckProtocolType,
    HealthStateType,
    IpAddressFamilyType,
    IpAddressTypeType,
    ProtocolType,
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
    "AcceleratorAttributesTypeDef",
    "AcceleratorEventTypeDef",
    "AcceleratorTypeDef",
    "AddCustomRoutingEndpointsRequestTypeDef",
    "AddCustomRoutingEndpointsResponseTypeDef",
    "AddEndpointsRequestTypeDef",
    "AddEndpointsResponseTypeDef",
    "AdvertiseByoipCidrRequestTypeDef",
    "AdvertiseByoipCidrResponseTypeDef",
    "AllowCustomRoutingTrafficRequestTypeDef",
    "AttachmentTypeDef",
    "ByoipCidrEventTypeDef",
    "ByoipCidrTypeDef",
    "CidrAuthorizationContextTypeDef",
    "CreateAcceleratorRequestTypeDef",
    "CreateAcceleratorResponseTypeDef",
    "CreateCrossAccountAttachmentRequestTypeDef",
    "CreateCrossAccountAttachmentResponseTypeDef",
    "CreateCustomRoutingAcceleratorRequestTypeDef",
    "CreateCustomRoutingAcceleratorResponseTypeDef",
    "CreateCustomRoutingEndpointGroupRequestTypeDef",
    "CreateCustomRoutingEndpointGroupResponseTypeDef",
    "CreateCustomRoutingListenerRequestTypeDef",
    "CreateCustomRoutingListenerResponseTypeDef",
    "CreateEndpointGroupRequestTypeDef",
    "CreateEndpointGroupResponseTypeDef",
    "CreateListenerRequestTypeDef",
    "CreateListenerResponseTypeDef",
    "CrossAccountResourceTypeDef",
    "CustomRoutingAcceleratorAttributesTypeDef",
    "CustomRoutingAcceleratorTypeDef",
    "CustomRoutingDestinationConfigurationTypeDef",
    "CustomRoutingDestinationDescriptionTypeDef",
    "CustomRoutingEndpointConfigurationTypeDef",
    "CustomRoutingEndpointDescriptionTypeDef",
    "CustomRoutingEndpointGroupTypeDef",
    "CustomRoutingListenerTypeDef",
    "DeleteAcceleratorRequestTypeDef",
    "DeleteCrossAccountAttachmentRequestTypeDef",
    "DeleteCustomRoutingAcceleratorRequestTypeDef",
    "DeleteCustomRoutingEndpointGroupRequestTypeDef",
    "DeleteCustomRoutingListenerRequestTypeDef",
    "DeleteEndpointGroupRequestTypeDef",
    "DeleteListenerRequestTypeDef",
    "DenyCustomRoutingTrafficRequestTypeDef",
    "DeprovisionByoipCidrRequestTypeDef",
    "DeprovisionByoipCidrResponseTypeDef",
    "DescribeAcceleratorAttributesRequestTypeDef",
    "DescribeAcceleratorAttributesResponseTypeDef",
    "DescribeAcceleratorRequestTypeDef",
    "DescribeAcceleratorResponseTypeDef",
    "DescribeCrossAccountAttachmentRequestTypeDef",
    "DescribeCrossAccountAttachmentResponseTypeDef",
    "DescribeCustomRoutingAcceleratorAttributesRequestTypeDef",
    "DescribeCustomRoutingAcceleratorAttributesResponseTypeDef",
    "DescribeCustomRoutingAcceleratorRequestTypeDef",
    "DescribeCustomRoutingAcceleratorResponseTypeDef",
    "DescribeCustomRoutingEndpointGroupRequestTypeDef",
    "DescribeCustomRoutingEndpointGroupResponseTypeDef",
    "DescribeCustomRoutingListenerRequestTypeDef",
    "DescribeCustomRoutingListenerResponseTypeDef",
    "DescribeEndpointGroupRequestTypeDef",
    "DescribeEndpointGroupResponseTypeDef",
    "DescribeListenerRequestTypeDef",
    "DescribeListenerResponseTypeDef",
    "DestinationPortMappingTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EndpointConfigurationTypeDef",
    "EndpointDescriptionTypeDef",
    "EndpointGroupTypeDef",
    "EndpointIdentifierTypeDef",
    "IpSetTypeDef",
    "ListAcceleratorsRequestPaginateTypeDef",
    "ListAcceleratorsRequestTypeDef",
    "ListAcceleratorsResponseTypeDef",
    "ListByoipCidrsRequestPaginateTypeDef",
    "ListByoipCidrsRequestTypeDef",
    "ListByoipCidrsResponseTypeDef",
    "ListCrossAccountAttachmentsRequestPaginateTypeDef",
    "ListCrossAccountAttachmentsRequestTypeDef",
    "ListCrossAccountAttachmentsResponseTypeDef",
    "ListCrossAccountResourceAccountsResponseTypeDef",
    "ListCrossAccountResourcesRequestPaginateTypeDef",
    "ListCrossAccountResourcesRequestTypeDef",
    "ListCrossAccountResourcesResponseTypeDef",
    "ListCustomRoutingAcceleratorsRequestPaginateTypeDef",
    "ListCustomRoutingAcceleratorsRequestTypeDef",
    "ListCustomRoutingAcceleratorsResponseTypeDef",
    "ListCustomRoutingEndpointGroupsRequestPaginateTypeDef",
    "ListCustomRoutingEndpointGroupsRequestTypeDef",
    "ListCustomRoutingEndpointGroupsResponseTypeDef",
    "ListCustomRoutingListenersRequestPaginateTypeDef",
    "ListCustomRoutingListenersRequestTypeDef",
    "ListCustomRoutingListenersResponseTypeDef",
    "ListCustomRoutingPortMappingsByDestinationRequestPaginateTypeDef",
    "ListCustomRoutingPortMappingsByDestinationRequestTypeDef",
    "ListCustomRoutingPortMappingsByDestinationResponseTypeDef",
    "ListCustomRoutingPortMappingsRequestPaginateTypeDef",
    "ListCustomRoutingPortMappingsRequestTypeDef",
    "ListCustomRoutingPortMappingsResponseTypeDef",
    "ListEndpointGroupsRequestPaginateTypeDef",
    "ListEndpointGroupsRequestTypeDef",
    "ListEndpointGroupsResponseTypeDef",
    "ListListenersRequestPaginateTypeDef",
    "ListListenersRequestTypeDef",
    "ListListenersResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListenerTypeDef",
    "PaginatorConfigTypeDef",
    "PortMappingTypeDef",
    "PortOverrideTypeDef",
    "PortRangeTypeDef",
    "ProvisionByoipCidrRequestTypeDef",
    "ProvisionByoipCidrResponseTypeDef",
    "RemoveCustomRoutingEndpointsRequestTypeDef",
    "RemoveEndpointsRequestTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "SocketAddressTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAcceleratorAttributesRequestTypeDef",
    "UpdateAcceleratorAttributesResponseTypeDef",
    "UpdateAcceleratorRequestTypeDef",
    "UpdateAcceleratorResponseTypeDef",
    "UpdateCrossAccountAttachmentRequestTypeDef",
    "UpdateCrossAccountAttachmentResponseTypeDef",
    "UpdateCustomRoutingAcceleratorAttributesRequestTypeDef",
    "UpdateCustomRoutingAcceleratorAttributesResponseTypeDef",
    "UpdateCustomRoutingAcceleratorRequestTypeDef",
    "UpdateCustomRoutingAcceleratorResponseTypeDef",
    "UpdateCustomRoutingListenerRequestTypeDef",
    "UpdateCustomRoutingListenerResponseTypeDef",
    "UpdateEndpointGroupRequestTypeDef",
    "UpdateEndpointGroupResponseTypeDef",
    "UpdateListenerRequestTypeDef",
    "UpdateListenerResponseTypeDef",
    "WithdrawByoipCidrRequestTypeDef",
    "WithdrawByoipCidrResponseTypeDef",
)

class AcceleratorAttributesTypeDef(TypedDict):
    FlowLogsEnabled: NotRequired[bool]
    FlowLogsS3Bucket: NotRequired[str]
    FlowLogsS3Prefix: NotRequired[str]

class AcceleratorEventTypeDef(TypedDict):
    Message: NotRequired[str]
    Timestamp: NotRequired[datetime]

class IpSetTypeDef(TypedDict):
    IpFamily: NotRequired[str]
    IpAddresses: NotRequired[List[str]]
    IpAddressFamily: NotRequired[IpAddressFamilyType]

class CustomRoutingEndpointConfigurationTypeDef(TypedDict):
    EndpointId: NotRequired[str]
    AttachmentArn: NotRequired[str]

class CustomRoutingEndpointDescriptionTypeDef(TypedDict):
    EndpointId: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class EndpointConfigurationTypeDef(TypedDict):
    EndpointId: NotRequired[str]
    Weight: NotRequired[int]
    ClientIPPreservationEnabled: NotRequired[bool]
    AttachmentArn: NotRequired[str]

class EndpointDescriptionTypeDef(TypedDict):
    EndpointId: NotRequired[str]
    Weight: NotRequired[int]
    HealthState: NotRequired[HealthStateType]
    HealthReason: NotRequired[str]
    ClientIPPreservationEnabled: NotRequired[bool]

class AdvertiseByoipCidrRequestTypeDef(TypedDict):
    Cidr: str

class AllowCustomRoutingTrafficRequestTypeDef(TypedDict):
    EndpointGroupArn: str
    EndpointId: str
    DestinationAddresses: NotRequired[Sequence[str]]
    DestinationPorts: NotRequired[Sequence[int]]
    AllowAllTrafficToEndpoint: NotRequired[bool]

class ResourceTypeDef(TypedDict):
    EndpointId: NotRequired[str]
    Cidr: NotRequired[str]
    Region: NotRequired[str]

class ByoipCidrEventTypeDef(TypedDict):
    Message: NotRequired[str]
    Timestamp: NotRequired[datetime]

class CidrAuthorizationContextTypeDef(TypedDict):
    Message: str
    Signature: str

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class CustomRoutingDestinationConfigurationTypeDef(TypedDict):
    FromPort: int
    ToPort: int
    Protocols: Sequence[CustomRoutingProtocolType]

class PortRangeTypeDef(TypedDict):
    FromPort: NotRequired[int]
    ToPort: NotRequired[int]

class PortOverrideTypeDef(TypedDict):
    ListenerPort: NotRequired[int]
    EndpointPort: NotRequired[int]

class CrossAccountResourceTypeDef(TypedDict):
    EndpointId: NotRequired[str]
    Cidr: NotRequired[str]
    AttachmentArn: NotRequired[str]

class CustomRoutingAcceleratorAttributesTypeDef(TypedDict):
    FlowLogsEnabled: NotRequired[bool]
    FlowLogsS3Bucket: NotRequired[str]
    FlowLogsS3Prefix: NotRequired[str]

class CustomRoutingDestinationDescriptionTypeDef(TypedDict):
    FromPort: NotRequired[int]
    ToPort: NotRequired[int]
    Protocols: NotRequired[List[ProtocolType]]

class DeleteAcceleratorRequestTypeDef(TypedDict):
    AcceleratorArn: str

class DeleteCrossAccountAttachmentRequestTypeDef(TypedDict):
    AttachmentArn: str

class DeleteCustomRoutingAcceleratorRequestTypeDef(TypedDict):
    AcceleratorArn: str

class DeleteCustomRoutingEndpointGroupRequestTypeDef(TypedDict):
    EndpointGroupArn: str

class DeleteCustomRoutingListenerRequestTypeDef(TypedDict):
    ListenerArn: str

class DeleteEndpointGroupRequestTypeDef(TypedDict):
    EndpointGroupArn: str

class DeleteListenerRequestTypeDef(TypedDict):
    ListenerArn: str

class DenyCustomRoutingTrafficRequestTypeDef(TypedDict):
    EndpointGroupArn: str
    EndpointId: str
    DestinationAddresses: NotRequired[Sequence[str]]
    DestinationPorts: NotRequired[Sequence[int]]
    DenyAllTrafficToEndpoint: NotRequired[bool]

class DeprovisionByoipCidrRequestTypeDef(TypedDict):
    Cidr: str

class DescribeAcceleratorAttributesRequestTypeDef(TypedDict):
    AcceleratorArn: str

class DescribeAcceleratorRequestTypeDef(TypedDict):
    AcceleratorArn: str

class DescribeCrossAccountAttachmentRequestTypeDef(TypedDict):
    AttachmentArn: str

class DescribeCustomRoutingAcceleratorAttributesRequestTypeDef(TypedDict):
    AcceleratorArn: str

class DescribeCustomRoutingAcceleratorRequestTypeDef(TypedDict):
    AcceleratorArn: str

class DescribeCustomRoutingEndpointGroupRequestTypeDef(TypedDict):
    EndpointGroupArn: str

class DescribeCustomRoutingListenerRequestTypeDef(TypedDict):
    ListenerArn: str

class DescribeEndpointGroupRequestTypeDef(TypedDict):
    EndpointGroupArn: str

class DescribeListenerRequestTypeDef(TypedDict):
    ListenerArn: str

class SocketAddressTypeDef(TypedDict):
    IpAddress: NotRequired[str]
    Port: NotRequired[int]

class EndpointIdentifierTypeDef(TypedDict):
    EndpointId: str
    ClientIPPreservationEnabled: NotRequired[bool]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAcceleratorsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListByoipCidrsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListCrossAccountAttachmentsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListCrossAccountResourcesRequestTypeDef(TypedDict):
    ResourceOwnerAwsAccountId: str
    AcceleratorArn: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListCustomRoutingAcceleratorsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListCustomRoutingEndpointGroupsRequestTypeDef(TypedDict):
    ListenerArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListCustomRoutingListenersRequestTypeDef(TypedDict):
    AcceleratorArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListCustomRoutingPortMappingsByDestinationRequestTypeDef(TypedDict):
    EndpointId: str
    DestinationAddress: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListCustomRoutingPortMappingsRequestTypeDef(TypedDict):
    AcceleratorArn: str
    EndpointGroupArn: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListEndpointGroupsRequestTypeDef(TypedDict):
    ListenerArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListListenersRequestTypeDef(TypedDict):
    AcceleratorArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class RemoveCustomRoutingEndpointsRequestTypeDef(TypedDict):
    EndpointIds: Sequence[str]
    EndpointGroupArn: str

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateAcceleratorAttributesRequestTypeDef(TypedDict):
    AcceleratorArn: str
    FlowLogsEnabled: NotRequired[bool]
    FlowLogsS3Bucket: NotRequired[str]
    FlowLogsS3Prefix: NotRequired[str]

class UpdateAcceleratorRequestTypeDef(TypedDict):
    AcceleratorArn: str
    Name: NotRequired[str]
    IpAddressType: NotRequired[IpAddressTypeType]
    IpAddresses: NotRequired[Sequence[str]]
    Enabled: NotRequired[bool]

class UpdateCustomRoutingAcceleratorAttributesRequestTypeDef(TypedDict):
    AcceleratorArn: str
    FlowLogsEnabled: NotRequired[bool]
    FlowLogsS3Bucket: NotRequired[str]
    FlowLogsS3Prefix: NotRequired[str]

class UpdateCustomRoutingAcceleratorRequestTypeDef(TypedDict):
    AcceleratorArn: str
    Name: NotRequired[str]
    IpAddressType: NotRequired[IpAddressTypeType]
    IpAddresses: NotRequired[Sequence[str]]
    Enabled: NotRequired[bool]

class WithdrawByoipCidrRequestTypeDef(TypedDict):
    Cidr: str

class AcceleratorTypeDef(TypedDict):
    AcceleratorArn: NotRequired[str]
    Name: NotRequired[str]
    IpAddressType: NotRequired[IpAddressTypeType]
    Enabled: NotRequired[bool]
    IpSets: NotRequired[List[IpSetTypeDef]]
    DnsName: NotRequired[str]
    Status: NotRequired[AcceleratorStatusType]
    CreatedTime: NotRequired[datetime]
    LastModifiedTime: NotRequired[datetime]
    DualStackDnsName: NotRequired[str]
    Events: NotRequired[List[AcceleratorEventTypeDef]]

class CustomRoutingAcceleratorTypeDef(TypedDict):
    AcceleratorArn: NotRequired[str]
    Name: NotRequired[str]
    IpAddressType: NotRequired[IpAddressTypeType]
    Enabled: NotRequired[bool]
    IpSets: NotRequired[List[IpSetTypeDef]]
    DnsName: NotRequired[str]
    Status: NotRequired[CustomRoutingAcceleratorStatusType]
    CreatedTime: NotRequired[datetime]
    LastModifiedTime: NotRequired[datetime]

class AddCustomRoutingEndpointsRequestTypeDef(TypedDict):
    EndpointConfigurations: Sequence[CustomRoutingEndpointConfigurationTypeDef]
    EndpointGroupArn: str

class AddCustomRoutingEndpointsResponseTypeDef(TypedDict):
    EndpointDescriptions: List[CustomRoutingEndpointDescriptionTypeDef]
    EndpointGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAcceleratorAttributesResponseTypeDef(TypedDict):
    AcceleratorAttributes: AcceleratorAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ListCrossAccountResourceAccountsResponseTypeDef(TypedDict):
    ResourceOwnerAwsAccountIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAcceleratorAttributesResponseTypeDef(TypedDict):
    AcceleratorAttributes: AcceleratorAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddEndpointsRequestTypeDef(TypedDict):
    EndpointConfigurations: Sequence[EndpointConfigurationTypeDef]
    EndpointGroupArn: str

class AddEndpointsResponseTypeDef(TypedDict):
    EndpointDescriptions: List[EndpointDescriptionTypeDef]
    EndpointGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AttachmentTypeDef(TypedDict):
    AttachmentArn: NotRequired[str]
    Name: NotRequired[str]
    Principals: NotRequired[List[str]]
    Resources: NotRequired[List[ResourceTypeDef]]
    LastModifiedTime: NotRequired[datetime]
    CreatedTime: NotRequired[datetime]

class UpdateCrossAccountAttachmentRequestTypeDef(TypedDict):
    AttachmentArn: str
    Name: NotRequired[str]
    AddPrincipals: NotRequired[Sequence[str]]
    RemovePrincipals: NotRequired[Sequence[str]]
    AddResources: NotRequired[Sequence[ResourceTypeDef]]
    RemoveResources: NotRequired[Sequence[ResourceTypeDef]]

class ByoipCidrTypeDef(TypedDict):
    Cidr: NotRequired[str]
    State: NotRequired[ByoipCidrStateType]
    Events: NotRequired[List[ByoipCidrEventTypeDef]]

class ProvisionByoipCidrRequestTypeDef(TypedDict):
    Cidr: str
    CidrAuthorizationContext: CidrAuthorizationContextTypeDef

class CreateAcceleratorRequestTypeDef(TypedDict):
    Name: str
    IdempotencyToken: str
    IpAddressType: NotRequired[IpAddressTypeType]
    IpAddresses: NotRequired[Sequence[str]]
    Enabled: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateCrossAccountAttachmentRequestTypeDef(TypedDict):
    Name: str
    IdempotencyToken: str
    Principals: NotRequired[Sequence[str]]
    Resources: NotRequired[Sequence[ResourceTypeDef]]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateCustomRoutingAcceleratorRequestTypeDef(TypedDict):
    Name: str
    IdempotencyToken: str
    IpAddressType: NotRequired[IpAddressTypeType]
    IpAddresses: NotRequired[Sequence[str]]
    Enabled: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateCustomRoutingEndpointGroupRequestTypeDef(TypedDict):
    ListenerArn: str
    EndpointGroupRegion: str
    DestinationConfigurations: Sequence[CustomRoutingDestinationConfigurationTypeDef]
    IdempotencyToken: str

class CreateCustomRoutingListenerRequestTypeDef(TypedDict):
    AcceleratorArn: str
    PortRanges: Sequence[PortRangeTypeDef]
    IdempotencyToken: str

CreateListenerRequestTypeDef = TypedDict(
    "CreateListenerRequestTypeDef",
    {
        "AcceleratorArn": str,
        "PortRanges": Sequence[PortRangeTypeDef],
        "Protocol": ProtocolType,
        "IdempotencyToken": str,
        "ClientAffinity": NotRequired[ClientAffinityType],
    },
)

class CustomRoutingListenerTypeDef(TypedDict):
    ListenerArn: NotRequired[str]
    PortRanges: NotRequired[List[PortRangeTypeDef]]

ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "ListenerArn": NotRequired[str],
        "PortRanges": NotRequired[List[PortRangeTypeDef]],
        "Protocol": NotRequired[ProtocolType],
        "ClientAffinity": NotRequired[ClientAffinityType],
    },
)

class UpdateCustomRoutingListenerRequestTypeDef(TypedDict):
    ListenerArn: str
    PortRanges: Sequence[PortRangeTypeDef]

UpdateListenerRequestTypeDef = TypedDict(
    "UpdateListenerRequestTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": NotRequired[Sequence[PortRangeTypeDef]],
        "Protocol": NotRequired[ProtocolType],
        "ClientAffinity": NotRequired[ClientAffinityType],
    },
)

class CreateEndpointGroupRequestTypeDef(TypedDict):
    ListenerArn: str
    EndpointGroupRegion: str
    IdempotencyToken: str
    EndpointConfigurations: NotRequired[Sequence[EndpointConfigurationTypeDef]]
    TrafficDialPercentage: NotRequired[float]
    HealthCheckPort: NotRequired[int]
    HealthCheckProtocol: NotRequired[HealthCheckProtocolType]
    HealthCheckPath: NotRequired[str]
    HealthCheckIntervalSeconds: NotRequired[int]
    ThresholdCount: NotRequired[int]
    PortOverrides: NotRequired[Sequence[PortOverrideTypeDef]]

class EndpointGroupTypeDef(TypedDict):
    EndpointGroupArn: NotRequired[str]
    EndpointGroupRegion: NotRequired[str]
    EndpointDescriptions: NotRequired[List[EndpointDescriptionTypeDef]]
    TrafficDialPercentage: NotRequired[float]
    HealthCheckPort: NotRequired[int]
    HealthCheckProtocol: NotRequired[HealthCheckProtocolType]
    HealthCheckPath: NotRequired[str]
    HealthCheckIntervalSeconds: NotRequired[int]
    ThresholdCount: NotRequired[int]
    PortOverrides: NotRequired[List[PortOverrideTypeDef]]

class UpdateEndpointGroupRequestTypeDef(TypedDict):
    EndpointGroupArn: str
    EndpointConfigurations: NotRequired[Sequence[EndpointConfigurationTypeDef]]
    TrafficDialPercentage: NotRequired[float]
    HealthCheckPort: NotRequired[int]
    HealthCheckProtocol: NotRequired[HealthCheckProtocolType]
    HealthCheckPath: NotRequired[str]
    HealthCheckIntervalSeconds: NotRequired[int]
    ThresholdCount: NotRequired[int]
    PortOverrides: NotRequired[Sequence[PortOverrideTypeDef]]

class ListCrossAccountResourcesResponseTypeDef(TypedDict):
    CrossAccountResources: List[CrossAccountResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeCustomRoutingAcceleratorAttributesResponseTypeDef(TypedDict):
    AcceleratorAttributes: CustomRoutingAcceleratorAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCustomRoutingAcceleratorAttributesResponseTypeDef(TypedDict):
    AcceleratorAttributes: CustomRoutingAcceleratorAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CustomRoutingEndpointGroupTypeDef(TypedDict):
    EndpointGroupArn: NotRequired[str]
    EndpointGroupRegion: NotRequired[str]
    DestinationDescriptions: NotRequired[List[CustomRoutingDestinationDescriptionTypeDef]]
    EndpointDescriptions: NotRequired[List[CustomRoutingEndpointDescriptionTypeDef]]

class DestinationPortMappingTypeDef(TypedDict):
    AcceleratorArn: NotRequired[str]
    AcceleratorSocketAddresses: NotRequired[List[SocketAddressTypeDef]]
    EndpointGroupArn: NotRequired[str]
    EndpointId: NotRequired[str]
    EndpointGroupRegion: NotRequired[str]
    DestinationSocketAddress: NotRequired[SocketAddressTypeDef]
    IpAddressType: NotRequired[IpAddressTypeType]
    DestinationTrafficState: NotRequired[CustomRoutingDestinationTrafficStateType]

class PortMappingTypeDef(TypedDict):
    AcceleratorPort: NotRequired[int]
    EndpointGroupArn: NotRequired[str]
    EndpointId: NotRequired[str]
    DestinationSocketAddress: NotRequired[SocketAddressTypeDef]
    Protocols: NotRequired[List[CustomRoutingProtocolType]]
    DestinationTrafficState: NotRequired[CustomRoutingDestinationTrafficStateType]

class RemoveEndpointsRequestTypeDef(TypedDict):
    EndpointIdentifiers: Sequence[EndpointIdentifierTypeDef]
    EndpointGroupArn: str

class ListAcceleratorsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListByoipCidrsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCrossAccountAttachmentsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCrossAccountResourcesRequestPaginateTypeDef(TypedDict):
    ResourceOwnerAwsAccountId: str
    AcceleratorArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCustomRoutingAcceleratorsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCustomRoutingEndpointGroupsRequestPaginateTypeDef(TypedDict):
    ListenerArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCustomRoutingListenersRequestPaginateTypeDef(TypedDict):
    AcceleratorArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCustomRoutingPortMappingsByDestinationRequestPaginateTypeDef(TypedDict):
    EndpointId: str
    DestinationAddress: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCustomRoutingPortMappingsRequestPaginateTypeDef(TypedDict):
    AcceleratorArn: str
    EndpointGroupArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEndpointGroupsRequestPaginateTypeDef(TypedDict):
    ListenerArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListListenersRequestPaginateTypeDef(TypedDict):
    AcceleratorArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class CreateAcceleratorResponseTypeDef(TypedDict):
    Accelerator: AcceleratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAcceleratorResponseTypeDef(TypedDict):
    Accelerator: AcceleratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAcceleratorsResponseTypeDef(TypedDict):
    Accelerators: List[AcceleratorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateAcceleratorResponseTypeDef(TypedDict):
    Accelerator: AcceleratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomRoutingAcceleratorResponseTypeDef(TypedDict):
    Accelerator: CustomRoutingAcceleratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCustomRoutingAcceleratorResponseTypeDef(TypedDict):
    Accelerator: CustomRoutingAcceleratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomRoutingAcceleratorsResponseTypeDef(TypedDict):
    Accelerators: List[CustomRoutingAcceleratorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateCustomRoutingAcceleratorResponseTypeDef(TypedDict):
    Accelerator: CustomRoutingAcceleratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCrossAccountAttachmentResponseTypeDef(TypedDict):
    CrossAccountAttachment: AttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCrossAccountAttachmentResponseTypeDef(TypedDict):
    CrossAccountAttachment: AttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCrossAccountAttachmentsResponseTypeDef(TypedDict):
    CrossAccountAttachments: List[AttachmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateCrossAccountAttachmentResponseTypeDef(TypedDict):
    CrossAccountAttachment: AttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AdvertiseByoipCidrResponseTypeDef(TypedDict):
    ByoipCidr: ByoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeprovisionByoipCidrResponseTypeDef(TypedDict):
    ByoipCidr: ByoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListByoipCidrsResponseTypeDef(TypedDict):
    ByoipCidrs: List[ByoipCidrTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ProvisionByoipCidrResponseTypeDef(TypedDict):
    ByoipCidr: ByoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class WithdrawByoipCidrResponseTypeDef(TypedDict):
    ByoipCidr: ByoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomRoutingListenerResponseTypeDef(TypedDict):
    Listener: CustomRoutingListenerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCustomRoutingListenerResponseTypeDef(TypedDict):
    Listener: CustomRoutingListenerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomRoutingListenersResponseTypeDef(TypedDict):
    Listeners: List[CustomRoutingListenerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateCustomRoutingListenerResponseTypeDef(TypedDict):
    Listener: CustomRoutingListenerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateListenerResponseTypeDef(TypedDict):
    Listener: ListenerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeListenerResponseTypeDef(TypedDict):
    Listener: ListenerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListListenersResponseTypeDef(TypedDict):
    Listeners: List[ListenerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateListenerResponseTypeDef(TypedDict):
    Listener: ListenerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEndpointGroupResponseTypeDef(TypedDict):
    EndpointGroup: EndpointGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEndpointGroupResponseTypeDef(TypedDict):
    EndpointGroup: EndpointGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEndpointGroupsResponseTypeDef(TypedDict):
    EndpointGroups: List[EndpointGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateEndpointGroupResponseTypeDef(TypedDict):
    EndpointGroup: EndpointGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomRoutingEndpointGroupResponseTypeDef(TypedDict):
    EndpointGroup: CustomRoutingEndpointGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCustomRoutingEndpointGroupResponseTypeDef(TypedDict):
    EndpointGroup: CustomRoutingEndpointGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomRoutingEndpointGroupsResponseTypeDef(TypedDict):
    EndpointGroups: List[CustomRoutingEndpointGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListCustomRoutingPortMappingsByDestinationResponseTypeDef(TypedDict):
    DestinationPortMappings: List[DestinationPortMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListCustomRoutingPortMappingsResponseTypeDef(TypedDict):
    PortMappings: List[PortMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
