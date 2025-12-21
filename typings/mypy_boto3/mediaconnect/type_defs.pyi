"""
Type annotations for mediaconnect service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_mediaconnect.type_defs import VpcInterfaceAttachmentTypeDef

    data: VpcInterfaceAttachmentTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    AlgorithmType,
    BridgePlacementType,
    BridgeStateType,
    ColorimetryType,
    ConnectionStatusType,
    ContentQualityAnalysisStateType,
    DayType,
    DesiredStateType,
    EncoderProfileType,
    EncodingNameType,
    EntitlementStatusType,
    FailoverInputSourcePriorityModeType,
    FailoverModeType,
    FlowSizeType,
    FlowTransitEncryptionKeyTypeType,
    ForwardErrorCorrectionStateType,
    GatewayStateType,
    InstanceStateType,
    KeyTypeType,
    MaintenanceDayType,
    MaintenanceTypeType,
    MediaLiveInputPipelineIdType,
    MediaLiveTransitEncryptionKeyTypeType,
    MediaStreamTypeType,
    NdiStateType,
    NetworkInterfaceTypeType,
    OutputStatusType,
    ProtocolType,
    RangeType,
    ReservationStateType,
    RouterInputProtocolType,
    RouterInputStateType,
    RouterInputTierType,
    RouterInputTransitEncryptionKeyTypeType,
    RouterInputTypeType,
    RouterNetworkInterfaceStateType,
    RouterNetworkInterfaceTypeType,
    RouterOutputProtocolType,
    RouterOutputRoutedStateType,
    RouterOutputStateType,
    RouterOutputTierType,
    RouterOutputTypeType,
    RoutingScopeType,
    ScanModeType,
    SourceTypeType,
    StateType,
    StatusType,
    TcsType,
    ThumbnailStateType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AddBridgeFlowSourceRequestTypeDef",
    "AddBridgeNetworkOutputRequestTypeDef",
    "AddBridgeNetworkSourceRequestTypeDef",
    "AddBridgeOutputRequestTypeDef",
    "AddBridgeOutputsRequestTypeDef",
    "AddBridgeOutputsResponseTypeDef",
    "AddBridgeSourceRequestTypeDef",
    "AddBridgeSourcesRequestTypeDef",
    "AddBridgeSourcesResponseTypeDef",
    "AddEgressGatewayBridgeRequestTypeDef",
    "AddFlowMediaStreamsRequestTypeDef",
    "AddFlowMediaStreamsResponseTypeDef",
    "AddFlowOutputsRequestTypeDef",
    "AddFlowOutputsResponseTypeDef",
    "AddFlowSourcesRequestTypeDef",
    "AddFlowSourcesResponseTypeDef",
    "AddFlowVpcInterfacesRequestTypeDef",
    "AddFlowVpcInterfacesResponseTypeDef",
    "AddIngressGatewayBridgeRequestTypeDef",
    "AddMaintenanceTypeDef",
    "AddMediaStreamRequestTypeDef",
    "AddOutputRequestTypeDef",
    "AudioMonitoringSettingTypeDef",
    "BatchGetRouterInputErrorTypeDef",
    "BatchGetRouterInputRequestTypeDef",
    "BatchGetRouterInputResponseTypeDef",
    "BatchGetRouterNetworkInterfaceErrorTypeDef",
    "BatchGetRouterNetworkInterfaceRequestTypeDef",
    "BatchGetRouterNetworkInterfaceResponseTypeDef",
    "BatchGetRouterOutputErrorTypeDef",
    "BatchGetRouterOutputRequestTypeDef",
    "BatchGetRouterOutputResponseTypeDef",
    "BlackFramesTypeDef",
    "BridgeFlowOutputTypeDef",
    "BridgeFlowSourceTypeDef",
    "BridgeNetworkOutputTypeDef",
    "BridgeNetworkSourceTypeDef",
    "BridgeOutputTypeDef",
    "BridgeSourceTypeDef",
    "BridgeTypeDef",
    "CreateBridgeRequestTypeDef",
    "CreateBridgeResponseTypeDef",
    "CreateFlowRequestTypeDef",
    "CreateFlowResponseTypeDef",
    "CreateGatewayRequestTypeDef",
    "CreateGatewayResponseTypeDef",
    "CreateRouterInputRequestTypeDef",
    "CreateRouterInputResponseTypeDef",
    "CreateRouterNetworkInterfaceRequestTypeDef",
    "CreateRouterNetworkInterfaceResponseTypeDef",
    "CreateRouterOutputRequestTypeDef",
    "CreateRouterOutputResponseTypeDef",
    "DeleteBridgeRequestTypeDef",
    "DeleteBridgeResponseTypeDef",
    "DeleteFlowRequestTypeDef",
    "DeleteFlowResponseTypeDef",
    "DeleteGatewayRequestTypeDef",
    "DeleteGatewayResponseTypeDef",
    "DeleteRouterInputRequestTypeDef",
    "DeleteRouterInputResponseTypeDef",
    "DeleteRouterNetworkInterfaceRequestTypeDef",
    "DeleteRouterNetworkInterfaceResponseTypeDef",
    "DeleteRouterOutputRequestTypeDef",
    "DeleteRouterOutputResponseTypeDef",
    "DeregisterGatewayInstanceRequestTypeDef",
    "DeregisterGatewayInstanceResponseTypeDef",
    "DescribeBridgeRequestTypeDef",
    "DescribeBridgeResponseTypeDef",
    "DescribeFlowRequestTypeDef",
    "DescribeFlowRequestWaitExtraExtraTypeDef",
    "DescribeFlowRequestWaitExtraTypeDef",
    "DescribeFlowRequestWaitTypeDef",
    "DescribeFlowResponseTypeDef",
    "DescribeFlowSourceMetadataRequestTypeDef",
    "DescribeFlowSourceMetadataResponseTypeDef",
    "DescribeFlowSourceThumbnailRequestTypeDef",
    "DescribeFlowSourceThumbnailResponseTypeDef",
    "DescribeGatewayInstanceRequestTypeDef",
    "DescribeGatewayInstanceResponseTypeDef",
    "DescribeGatewayRequestTypeDef",
    "DescribeGatewayResponseTypeDef",
    "DescribeOfferingRequestTypeDef",
    "DescribeOfferingResponseTypeDef",
    "DescribeReservationRequestTypeDef",
    "DescribeReservationResponseTypeDef",
    "DestinationConfigurationRequestTypeDef",
    "DestinationConfigurationTypeDef",
    "EgressGatewayBridgeTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EncodingParametersRequestTypeDef",
    "EncodingParametersTypeDef",
    "EncryptionTypeDef",
    "EntitlementTypeDef",
    "FailoverConfigTypeDef",
    "FailoverRouterInputConfigurationOutputTypeDef",
    "FailoverRouterInputConfigurationTypeDef",
    "FailoverRouterInputIndexedStreamDetailsTypeDef",
    "FailoverRouterInputProtocolConfigurationTypeDef",
    "FailoverRouterInputStreamDetailsTypeDef",
    "FlowTransitEncryptionKeyConfigurationOutputTypeDef",
    "FlowTransitEncryptionKeyConfigurationTypeDef",
    "FlowTransitEncryptionKeyConfigurationUnionTypeDef",
    "FlowTransitEncryptionOutputTypeDef",
    "FlowTransitEncryptionTypeDef",
    "FlowTransitEncryptionUnionTypeDef",
    "FlowTypeDef",
    "FmtpRequestTypeDef",
    "FmtpTypeDef",
    "FrameResolutionTypeDef",
    "FrozenFramesTypeDef",
    "GatewayBridgeSourceTypeDef",
    "GatewayInstanceTypeDef",
    "GatewayNetworkTypeDef",
    "GatewayTypeDef",
    "GetRouterInputRequestTypeDef",
    "GetRouterInputRequestWaitExtraExtraTypeDef",
    "GetRouterInputRequestWaitExtraTypeDef",
    "GetRouterInputRequestWaitTypeDef",
    "GetRouterInputResponseTypeDef",
    "GetRouterInputSourceMetadataRequestTypeDef",
    "GetRouterInputSourceMetadataResponseTypeDef",
    "GetRouterInputThumbnailRequestTypeDef",
    "GetRouterInputThumbnailResponseTypeDef",
    "GetRouterNetworkInterfaceRequestTypeDef",
    "GetRouterNetworkInterfaceResponseTypeDef",
    "GetRouterOutputRequestTypeDef",
    "GetRouterOutputRequestWaitExtraExtraExtraTypeDef",
    "GetRouterOutputRequestWaitExtraExtraTypeDef",
    "GetRouterOutputRequestWaitExtraTypeDef",
    "GetRouterOutputRequestWaitTypeDef",
    "GetRouterOutputResponseTypeDef",
    "GrantEntitlementRequestTypeDef",
    "GrantFlowEntitlementsRequestTypeDef",
    "GrantFlowEntitlementsResponseTypeDef",
    "IngressGatewayBridgeTypeDef",
    "InputConfigurationRequestTypeDef",
    "InputConfigurationTypeDef",
    "InterfaceRequestTypeDef",
    "InterfaceTypeDef",
    "ListBridgesRequestPaginateTypeDef",
    "ListBridgesRequestTypeDef",
    "ListBridgesResponseTypeDef",
    "ListEntitlementsRequestPaginateTypeDef",
    "ListEntitlementsRequestTypeDef",
    "ListEntitlementsResponseTypeDef",
    "ListFlowsRequestPaginateTypeDef",
    "ListFlowsRequestTypeDef",
    "ListFlowsResponseTypeDef",
    "ListGatewayInstancesRequestPaginateTypeDef",
    "ListGatewayInstancesRequestTypeDef",
    "ListGatewayInstancesResponseTypeDef",
    "ListGatewaysRequestPaginateTypeDef",
    "ListGatewaysRequestTypeDef",
    "ListGatewaysResponseTypeDef",
    "ListOfferingsRequestPaginateTypeDef",
    "ListOfferingsRequestTypeDef",
    "ListOfferingsResponseTypeDef",
    "ListReservationsRequestPaginateTypeDef",
    "ListReservationsRequestTypeDef",
    "ListReservationsResponseTypeDef",
    "ListRouterInputsRequestPaginateTypeDef",
    "ListRouterInputsRequestTypeDef",
    "ListRouterInputsResponseTypeDef",
    "ListRouterNetworkInterfacesRequestPaginateTypeDef",
    "ListRouterNetworkInterfacesRequestTypeDef",
    "ListRouterNetworkInterfacesResponseTypeDef",
    "ListRouterOutputsRequestPaginateTypeDef",
    "ListRouterOutputsRequestTypeDef",
    "ListRouterOutputsResponseTypeDef",
    "ListTagsForGlobalResourceRequestTypeDef",
    "ListTagsForGlobalResourceResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListedBridgeTypeDef",
    "ListedEntitlementTypeDef",
    "ListedFlowTypeDef",
    "ListedGatewayInstanceTypeDef",
    "ListedGatewayTypeDef",
    "ListedRouterInputTypeDef",
    "ListedRouterNetworkInterfaceTypeDef",
    "ListedRouterOutputTypeDef",
    "MaintenanceConfigurationOutputTypeDef",
    "MaintenanceConfigurationTypeDef",
    "MaintenanceConfigurationUnionTypeDef",
    "MaintenanceScheduleTypeDef",
    "MaintenanceTypeDef",
    "MediaConnectFlowRouterInputConfigurationOutputTypeDef",
    "MediaConnectFlowRouterInputConfigurationTypeDef",
    "MediaConnectFlowRouterOutputConfigurationOutputTypeDef",
    "MediaConnectFlowRouterOutputConfigurationTypeDef",
    "MediaLiveInputRouterOutputConfigurationOutputTypeDef",
    "MediaLiveInputRouterOutputConfigurationTypeDef",
    "MediaLiveTransitEncryptionKeyConfigurationOutputTypeDef",
    "MediaLiveTransitEncryptionKeyConfigurationTypeDef",
    "MediaLiveTransitEncryptionOutputTypeDef",
    "MediaLiveTransitEncryptionTypeDef",
    "MediaStreamAttributesRequestTypeDef",
    "MediaStreamAttributesTypeDef",
    "MediaStreamOutputConfigurationRequestTypeDef",
    "MediaStreamOutputConfigurationTypeDef",
    "MediaStreamSourceConfigurationRequestTypeDef",
    "MediaStreamSourceConfigurationTypeDef",
    "MediaStreamTypeDef",
    "MergeRouterInputConfigurationOutputTypeDef",
    "MergeRouterInputConfigurationTypeDef",
    "MergeRouterInputIndexedStreamDetailsTypeDef",
    "MergeRouterInputProtocolConfigurationTypeDef",
    "MergeRouterInputStreamDetailsTypeDef",
    "MessageDetailTypeDef",
    "MessagesTypeDef",
    "MonitoringConfigOutputTypeDef",
    "MonitoringConfigTypeDef",
    "MonitoringConfigUnionTypeDef",
    "MulticastSourceSettingsTypeDef",
    "NdiConfigOutputTypeDef",
    "NdiConfigTypeDef",
    "NdiConfigUnionTypeDef",
    "NdiDiscoveryServerConfigTypeDef",
    "OfferingTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "PreferredDayTimeMaintenanceConfigurationTypeDef",
    "PublicRouterNetworkInterfaceConfigurationOutputTypeDef",
    "PublicRouterNetworkInterfaceConfigurationTypeDef",
    "PublicRouterNetworkInterfaceRuleTypeDef",
    "PurchaseOfferingRequestTypeDef",
    "PurchaseOfferingResponseTypeDef",
    "RemoveBridgeOutputRequestTypeDef",
    "RemoveBridgeOutputResponseTypeDef",
    "RemoveBridgeSourceRequestTypeDef",
    "RemoveBridgeSourceResponseTypeDef",
    "RemoveFlowMediaStreamRequestTypeDef",
    "RemoveFlowMediaStreamResponseTypeDef",
    "RemoveFlowOutputRequestTypeDef",
    "RemoveFlowOutputResponseTypeDef",
    "RemoveFlowSourceRequestTypeDef",
    "RemoveFlowSourceResponseTypeDef",
    "RemoveFlowVpcInterfaceRequestTypeDef",
    "RemoveFlowVpcInterfaceResponseTypeDef",
    "ReservationTypeDef",
    "ResourceSpecificationTypeDef",
    "ResponseMetadataTypeDef",
    "RestartRouterInputRequestTypeDef",
    "RestartRouterInputResponseTypeDef",
    "RestartRouterOutputRequestTypeDef",
    "RestartRouterOutputResponseTypeDef",
    "RevokeFlowEntitlementRequestTypeDef",
    "RevokeFlowEntitlementResponseTypeDef",
    "RistRouterInputConfigurationTypeDef",
    "RistRouterOutputConfigurationTypeDef",
    "RouterInputConfigurationOutputTypeDef",
    "RouterInputConfigurationTypeDef",
    "RouterInputConfigurationUnionTypeDef",
    "RouterInputFilterTypeDef",
    "RouterInputMessageTypeDef",
    "RouterInputMetadataTypeDef",
    "RouterInputProtocolConfigurationTypeDef",
    "RouterInputSourceMetadataDetailsTypeDef",
    "RouterInputStreamDetailsTypeDef",
    "RouterInputThumbnailDetailsTypeDef",
    "RouterInputTransitEncryptionKeyConfigurationOutputTypeDef",
    "RouterInputTransitEncryptionKeyConfigurationTypeDef",
    "RouterInputTransitEncryptionOutputTypeDef",
    "RouterInputTransitEncryptionTypeDef",
    "RouterInputTransitEncryptionUnionTypeDef",
    "RouterInputTypeDef",
    "RouterNetworkInterfaceConfigurationOutputTypeDef",
    "RouterNetworkInterfaceConfigurationTypeDef",
    "RouterNetworkInterfaceConfigurationUnionTypeDef",
    "RouterNetworkInterfaceFilterTypeDef",
    "RouterNetworkInterfaceTypeDef",
    "RouterOutputConfigurationOutputTypeDef",
    "RouterOutputConfigurationTypeDef",
    "RouterOutputConfigurationUnionTypeDef",
    "RouterOutputFilterTypeDef",
    "RouterOutputMessageTypeDef",
    "RouterOutputProtocolConfigurationTypeDef",
    "RouterOutputStreamDetailsTypeDef",
    "RouterOutputTypeDef",
    "RtpRouterInputConfigurationTypeDef",
    "RtpRouterOutputConfigurationTypeDef",
    "SecretsManagerEncryptionKeyConfigurationTypeDef",
    "SetGatewayBridgeSourceRequestTypeDef",
    "SetSourceRequestTypeDef",
    "SilentAudioTypeDef",
    "SourcePriorityTypeDef",
    "SourceTypeDef",
    "SrtCallerRouterInputConfigurationTypeDef",
    "SrtCallerRouterOutputConfigurationTypeDef",
    "SrtDecryptionConfigurationTypeDef",
    "SrtEncryptionConfigurationTypeDef",
    "SrtListenerRouterInputConfigurationTypeDef",
    "SrtListenerRouterOutputConfigurationTypeDef",
    "StandardRouterInputConfigurationTypeDef",
    "StandardRouterInputStreamDetailsTypeDef",
    "StandardRouterOutputConfigurationTypeDef",
    "StandardRouterOutputStreamDetailsTypeDef",
    "StartFlowRequestTypeDef",
    "StartFlowResponseTypeDef",
    "StartRouterInputRequestTypeDef",
    "StartRouterInputResponseTypeDef",
    "StartRouterOutputRequestTypeDef",
    "StartRouterOutputResponseTypeDef",
    "StopFlowRequestTypeDef",
    "StopFlowResponseTypeDef",
    "StopRouterInputRequestTypeDef",
    "StopRouterInputResponseTypeDef",
    "StopRouterOutputRequestTypeDef",
    "StopRouterOutputResponseTypeDef",
    "TagGlobalResourceRequestTypeDef",
    "TagResourceRequestTypeDef",
    "TakeRouterInputRequestTypeDef",
    "TakeRouterInputResponseTypeDef",
    "ThumbnailDetailsTypeDef",
    "TransportMediaInfoTypeDef",
    "TransportStreamProgramTypeDef",
    "TransportStreamTypeDef",
    "TransportTypeDef",
    "UntagGlobalResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateBridgeFlowSourceRequestTypeDef",
    "UpdateBridgeNetworkOutputRequestTypeDef",
    "UpdateBridgeNetworkSourceRequestTypeDef",
    "UpdateBridgeOutputRequestTypeDef",
    "UpdateBridgeOutputResponseTypeDef",
    "UpdateBridgeRequestTypeDef",
    "UpdateBridgeResponseTypeDef",
    "UpdateBridgeSourceRequestTypeDef",
    "UpdateBridgeSourceResponseTypeDef",
    "UpdateBridgeStateRequestTypeDef",
    "UpdateBridgeStateResponseTypeDef",
    "UpdateEgressGatewayBridgeRequestTypeDef",
    "UpdateEncryptionTypeDef",
    "UpdateFailoverConfigTypeDef",
    "UpdateFlowEntitlementRequestTypeDef",
    "UpdateFlowEntitlementResponseTypeDef",
    "UpdateFlowMediaStreamRequestTypeDef",
    "UpdateFlowMediaStreamResponseTypeDef",
    "UpdateFlowOutputRequestTypeDef",
    "UpdateFlowOutputResponseTypeDef",
    "UpdateFlowRequestTypeDef",
    "UpdateFlowResponseTypeDef",
    "UpdateFlowSourceRequestTypeDef",
    "UpdateFlowSourceResponseTypeDef",
    "UpdateGatewayBridgeSourceRequestTypeDef",
    "UpdateGatewayInstanceRequestTypeDef",
    "UpdateGatewayInstanceResponseTypeDef",
    "UpdateIngressGatewayBridgeRequestTypeDef",
    "UpdateMaintenanceTypeDef",
    "UpdateRouterInputRequestTypeDef",
    "UpdateRouterInputResponseTypeDef",
    "UpdateRouterNetworkInterfaceRequestTypeDef",
    "UpdateRouterNetworkInterfaceResponseTypeDef",
    "UpdateRouterOutputRequestTypeDef",
    "UpdateRouterOutputResponseTypeDef",
    "VideoMonitoringSettingTypeDef",
    "VpcInterfaceAttachmentTypeDef",
    "VpcInterfaceRequestTypeDef",
    "VpcInterfaceTypeDef",
    "VpcRouterNetworkInterfaceConfigurationOutputTypeDef",
    "VpcRouterNetworkInterfaceConfigurationTypeDef",
    "WaiterConfigTypeDef",
    "WindowMaintenanceScheduleTypeDef",
)

class VpcInterfaceAttachmentTypeDef(TypedDict):
    VpcInterfaceName: NotRequired[str]

AddBridgeNetworkOutputRequestTypeDef = TypedDict(
    "AddBridgeNetworkOutputRequestTypeDef",
    {
        "IpAddress": str,
        "Name": str,
        "NetworkName": str,
        "Port": int,
        "Protocol": ProtocolType,
        "Ttl": int,
    },
)

class MulticastSourceSettingsTypeDef(TypedDict):
    MulticastSourceIp: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AddEgressGatewayBridgeRequestTypeDef(TypedDict):
    MaxBitrate: int

class VpcInterfaceRequestTypeDef(TypedDict):
    Name: str
    RoleArn: str
    SecurityGroupIds: Sequence[str]
    SubnetId: str
    NetworkInterfaceType: NotRequired[NetworkInterfaceTypeType]
    VpcInterfaceTags: NotRequired[Mapping[str, str]]

class VpcInterfaceTypeDef(TypedDict):
    Name: str
    NetworkInterfaceIds: List[str]
    NetworkInterfaceType: NetworkInterfaceTypeType
    RoleArn: str
    SecurityGroupIds: List[str]
    SubnetId: str

class AddIngressGatewayBridgeRequestTypeDef(TypedDict):
    MaxBitrate: int
    MaxOutputs: int

class AddMaintenanceTypeDef(TypedDict):
    MaintenanceDay: MaintenanceDayType
    MaintenanceStartHour: str

class EncryptionTypeDef(TypedDict):
    RoleArn: str
    Algorithm: NotRequired[AlgorithmType]
    ConstantInitializationVector: NotRequired[str]
    DeviceId: NotRequired[str]
    KeyType: NotRequired[KeyTypeType]
    Region: NotRequired[str]
    ResourceId: NotRequired[str]
    SecretArn: NotRequired[str]
    Url: NotRequired[str]

class SilentAudioTypeDef(TypedDict):
    State: NotRequired[StateType]
    ThresholdSeconds: NotRequired[int]

class BatchGetRouterInputErrorTypeDef(TypedDict):
    Arn: str
    Code: str
    Message: str

class BatchGetRouterInputRequestTypeDef(TypedDict):
    Arns: Sequence[str]

class BatchGetRouterNetworkInterfaceErrorTypeDef(TypedDict):
    Arn: str
    Code: str
    Message: str

class BatchGetRouterNetworkInterfaceRequestTypeDef(TypedDict):
    Arns: Sequence[str]

class BatchGetRouterOutputErrorTypeDef(TypedDict):
    Arn: str
    Code: str
    Message: str

class BatchGetRouterOutputRequestTypeDef(TypedDict):
    Arns: Sequence[str]

class BlackFramesTypeDef(TypedDict):
    State: NotRequired[StateType]
    ThresholdSeconds: NotRequired[int]

class BridgeFlowOutputTypeDef(TypedDict):
    FlowArn: str
    FlowSourceArn: str
    Name: str

BridgeNetworkOutputTypeDef = TypedDict(
    "BridgeNetworkOutputTypeDef",
    {
        "IpAddress": str,
        "Name": str,
        "NetworkName": str,
        "Port": int,
        "Protocol": ProtocolType,
        "Ttl": int,
    },
)

class EgressGatewayBridgeTypeDef(TypedDict):
    MaxBitrate: int
    InstanceId: NotRequired[str]

class IngressGatewayBridgeTypeDef(TypedDict):
    MaxBitrate: int
    MaxOutputs: int
    InstanceId: NotRequired[str]

class MessageDetailTypeDef(TypedDict):
    Code: str
    Message: str
    ResourceName: NotRequired[str]

class GatewayNetworkTypeDef(TypedDict):
    CidrBlock: str
    Name: str

class DeleteBridgeRequestTypeDef(TypedDict):
    BridgeArn: str

class DeleteFlowRequestTypeDef(TypedDict):
    FlowArn: str

class DeleteGatewayRequestTypeDef(TypedDict):
    GatewayArn: str

class DeleteRouterInputRequestTypeDef(TypedDict):
    Arn: str

class DeleteRouterNetworkInterfaceRequestTypeDef(TypedDict):
    Arn: str

class DeleteRouterOutputRequestTypeDef(TypedDict):
    Arn: str

class DeregisterGatewayInstanceRequestTypeDef(TypedDict):
    GatewayInstanceArn: str
    Force: NotRequired[bool]

class DescribeBridgeRequestTypeDef(TypedDict):
    BridgeArn: str

class DescribeFlowRequestTypeDef(TypedDict):
    FlowArn: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class MessagesTypeDef(TypedDict):
    Errors: List[str]

class DescribeFlowSourceMetadataRequestTypeDef(TypedDict):
    FlowArn: str

class DescribeFlowSourceThumbnailRequestTypeDef(TypedDict):
    FlowArn: str

class DescribeGatewayInstanceRequestTypeDef(TypedDict):
    GatewayInstanceArn: str

class DescribeGatewayRequestTypeDef(TypedDict):
    GatewayArn: str

class DescribeOfferingRequestTypeDef(TypedDict):
    OfferingArn: str

class DescribeReservationRequestTypeDef(TypedDict):
    ReservationArn: str

class InterfaceRequestTypeDef(TypedDict):
    Name: str

class InterfaceTypeDef(TypedDict):
    Name: str

class EncodingParametersRequestTypeDef(TypedDict):
    CompressionFactor: float
    EncoderProfile: EncoderProfileType

class EncodingParametersTypeDef(TypedDict):
    CompressionFactor: float
    EncoderProfile: EncoderProfileType

class SourcePriorityTypeDef(TypedDict):
    PrimarySource: NotRequired[str]

class FailoverRouterInputIndexedStreamDetailsTypeDef(TypedDict):
    SourceIndex: int
    SourceIpAddress: NotRequired[str]

class RistRouterInputConfigurationTypeDef(TypedDict):
    Port: int
    RecoveryLatencyMilliseconds: int

class RtpRouterInputConfigurationTypeDef(TypedDict):
    Port: int
    ForwardErrorCorrection: NotRequired[ForwardErrorCorrectionStateType]

class SecretsManagerEncryptionKeyConfigurationTypeDef(TypedDict):
    SecretArn: str
    RoleArn: str

class MaintenanceTypeDef(TypedDict):
    MaintenanceDay: NotRequired[MaintenanceDayType]
    MaintenanceDeadline: NotRequired[str]
    MaintenanceScheduledDate: NotRequired[str]
    MaintenanceStartHour: NotRequired[str]

class FmtpRequestTypeDef(TypedDict):
    ChannelOrder: NotRequired[str]
    Colorimetry: NotRequired[ColorimetryType]
    ExactFramerate: NotRequired[str]
    Par: NotRequired[str]
    Range: NotRequired[RangeType]
    ScanMode: NotRequired[ScanModeType]
    Tcs: NotRequired[TcsType]

class FmtpTypeDef(TypedDict):
    ChannelOrder: NotRequired[str]
    Colorimetry: NotRequired[ColorimetryType]
    ExactFramerate: NotRequired[str]
    Par: NotRequired[str]
    Range: NotRequired[RangeType]
    ScanMode: NotRequired[ScanModeType]
    Tcs: NotRequired[TcsType]

class FrameResolutionTypeDef(TypedDict):
    FrameHeight: int
    FrameWidth: int

class FrozenFramesTypeDef(TypedDict):
    State: NotRequired[StateType]
    ThresholdSeconds: NotRequired[int]

class GetRouterInputRequestTypeDef(TypedDict):
    Arn: str

class GetRouterInputSourceMetadataRequestTypeDef(TypedDict):
    Arn: str

class GetRouterInputThumbnailRequestTypeDef(TypedDict):
    Arn: str

class GetRouterNetworkInterfaceRequestTypeDef(TypedDict):
    Arn: str

class GetRouterOutputRequestTypeDef(TypedDict):
    Arn: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListBridgesRequestTypeDef(TypedDict):
    FilterArn: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListedBridgeTypeDef(TypedDict):
    BridgeArn: str
    BridgeState: BridgeStateType
    BridgeType: str
    Name: str
    PlacementArn: str

class ListEntitlementsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListedEntitlementTypeDef(TypedDict):
    EntitlementArn: str
    EntitlementName: str
    DataTransferSubscriberFeePercent: NotRequired[int]

class ListFlowsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListGatewayInstancesRequestTypeDef(TypedDict):
    FilterArn: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListedGatewayInstanceTypeDef(TypedDict):
    GatewayArn: str
    GatewayInstanceArn: str
    InstanceId: str
    InstanceState: NotRequired[InstanceStateType]

class ListGatewaysRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListedGatewayTypeDef(TypedDict):
    GatewayArn: str
    GatewayState: GatewayStateType
    Name: str

class ListOfferingsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListReservationsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class RouterInputFilterTypeDef(TypedDict):
    RegionNames: NotRequired[Sequence[str]]
    InputTypes: NotRequired[Sequence[RouterInputTypeType]]
    NameContains: NotRequired[Sequence[str]]
    NetworkInterfaceArns: NotRequired[Sequence[str]]
    RoutingScopes: NotRequired[Sequence[RoutingScopeType]]

class RouterNetworkInterfaceFilterTypeDef(TypedDict):
    RegionNames: NotRequired[Sequence[str]]
    NetworkInterfaceTypes: NotRequired[Sequence[RouterNetworkInterfaceTypeType]]
    NameContains: NotRequired[Sequence[str]]

ListedRouterNetworkInterfaceTypeDef = TypedDict(
    "ListedRouterNetworkInterfaceTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Id": str,
        "NetworkInterfaceType": RouterNetworkInterfaceTypeType,
        "AssociatedOutputCount": int,
        "AssociatedInputCount": int,
        "State": RouterNetworkInterfaceStateType,
        "RegionName": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
    },
)

class RouterOutputFilterTypeDef(TypedDict):
    RegionNames: NotRequired[Sequence[str]]
    OutputTypes: NotRequired[Sequence[RouterOutputTypeType]]
    NameContains: NotRequired[Sequence[str]]
    NetworkInterfaceArns: NotRequired[Sequence[str]]
    RoutedInputArns: NotRequired[Sequence[str]]
    RoutingScopes: NotRequired[Sequence[RoutingScopeType]]

class ListTagsForGlobalResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class PreferredDayTimeMaintenanceConfigurationTypeDef(TypedDict):
    Day: DayType
    Time: str

class WindowMaintenanceScheduleTypeDef(TypedDict):
    Start: datetime
    End: datetime
    ScheduledTime: datetime

class MergeRouterInputIndexedStreamDetailsTypeDef(TypedDict):
    SourceIndex: int
    SourceIpAddress: NotRequired[str]

class NdiDiscoveryServerConfigTypeDef(TypedDict):
    DiscoveryServerAddress: str
    VpcInterfaceAdapter: str
    DiscoveryServerPort: NotRequired[int]

class ResourceSpecificationTypeDef(TypedDict):
    ResourceType: Literal["Mbps_Outbound_Bandwidth"]
    ReservedBitrate: NotRequired[int]

TransportTypeDef = TypedDict(
    "TransportTypeDef",
    {
        "Protocol": ProtocolType,
        "CidrAllowList": NotRequired[List[str]],
        "MaxBitrate": NotRequired[int],
        "MaxLatency": NotRequired[int],
        "MaxSyncBuffer": NotRequired[int],
        "MinLatency": NotRequired[int],
        "RemoteId": NotRequired[str],
        "SenderControlPort": NotRequired[int],
        "SenderIpAddress": NotRequired[str],
        "SmoothingLatency": NotRequired[int],
        "SourceListenerAddress": NotRequired[str],
        "SourceListenerPort": NotRequired[int],
        "StreamId": NotRequired[str],
        "NdiSpeedHqQuality": NotRequired[int],
        "NdiProgramName": NotRequired[str],
    },
)

class PublicRouterNetworkInterfaceRuleTypeDef(TypedDict):
    Cidr: str

class PurchaseOfferingRequestTypeDef(TypedDict):
    OfferingArn: str
    ReservationName: str
    Start: str

class RemoveBridgeOutputRequestTypeDef(TypedDict):
    BridgeArn: str
    OutputName: str

class RemoveBridgeSourceRequestTypeDef(TypedDict):
    BridgeArn: str
    SourceName: str

class RemoveFlowMediaStreamRequestTypeDef(TypedDict):
    FlowArn: str
    MediaStreamName: str

class RemoveFlowOutputRequestTypeDef(TypedDict):
    FlowArn: str
    OutputArn: str

class RemoveFlowSourceRequestTypeDef(TypedDict):
    FlowArn: str
    SourceArn: str

class RemoveFlowVpcInterfaceRequestTypeDef(TypedDict):
    FlowArn: str
    VpcInterfaceName: str

class RestartRouterInputRequestTypeDef(TypedDict):
    Arn: str

class RestartRouterOutputRequestTypeDef(TypedDict):
    Arn: str

class RevokeFlowEntitlementRequestTypeDef(TypedDict):
    EntitlementArn: str
    FlowArn: str

class RistRouterOutputConfigurationTypeDef(TypedDict):
    DestinationAddress: str
    DestinationPort: int

class RouterInputMessageTypeDef(TypedDict):
    Code: str
    Message: str

class StandardRouterInputStreamDetailsTypeDef(TypedDict):
    SourceIpAddress: NotRequired[str]

class VpcRouterNetworkInterfaceConfigurationOutputTypeDef(TypedDict):
    SecurityGroupIds: List[str]
    SubnetId: str

class VpcRouterNetworkInterfaceConfigurationTypeDef(TypedDict):
    SecurityGroupIds: Sequence[str]
    SubnetId: str

class RouterOutputMessageTypeDef(TypedDict):
    Code: str
    Message: str

class RtpRouterOutputConfigurationTypeDef(TypedDict):
    DestinationAddress: str
    DestinationPort: int
    ForwardErrorCorrection: NotRequired[ForwardErrorCorrectionStateType]

class StandardRouterOutputStreamDetailsTypeDef(TypedDict):
    DestinationIpAddress: NotRequired[str]

class StartFlowRequestTypeDef(TypedDict):
    FlowArn: str

class StartRouterInputRequestTypeDef(TypedDict):
    Arn: str

class StartRouterOutputRequestTypeDef(TypedDict):
    Arn: str

class StopFlowRequestTypeDef(TypedDict):
    FlowArn: str

class StopRouterInputRequestTypeDef(TypedDict):
    Arn: str

class StopRouterOutputRequestTypeDef(TypedDict):
    Arn: str

class TagGlobalResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class TakeRouterInputRequestTypeDef(TypedDict):
    RouterOutputArn: str
    RouterInputArn: NotRequired[str]

class UntagGlobalResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

UpdateBridgeNetworkOutputRequestTypeDef = TypedDict(
    "UpdateBridgeNetworkOutputRequestTypeDef",
    {
        "IpAddress": NotRequired[str],
        "NetworkName": NotRequired[str],
        "Port": NotRequired[int],
        "Protocol": NotRequired[ProtocolType],
        "Ttl": NotRequired[int],
    },
)

class UpdateEgressGatewayBridgeRequestTypeDef(TypedDict):
    MaxBitrate: NotRequired[int]

class UpdateIngressGatewayBridgeRequestTypeDef(TypedDict):
    MaxBitrate: NotRequired[int]
    MaxOutputs: NotRequired[int]

class UpdateBridgeStateRequestTypeDef(TypedDict):
    BridgeArn: str
    DesiredState: DesiredStateType

class UpdateEncryptionTypeDef(TypedDict):
    Algorithm: NotRequired[AlgorithmType]
    ConstantInitializationVector: NotRequired[str]
    DeviceId: NotRequired[str]
    KeyType: NotRequired[KeyTypeType]
    Region: NotRequired[str]
    ResourceId: NotRequired[str]
    RoleArn: NotRequired[str]
    SecretArn: NotRequired[str]
    Url: NotRequired[str]

class UpdateMaintenanceTypeDef(TypedDict):
    MaintenanceDay: NotRequired[MaintenanceDayType]
    MaintenanceScheduledDate: NotRequired[str]
    MaintenanceStartHour: NotRequired[str]

class UpdateGatewayInstanceRequestTypeDef(TypedDict):
    GatewayInstanceArn: str
    BridgePlacement: NotRequired[BridgePlacementType]

class AddBridgeFlowSourceRequestTypeDef(TypedDict):
    FlowArn: str
    Name: str
    FlowVpcInterfaceAttachment: NotRequired[VpcInterfaceAttachmentTypeDef]

class BridgeFlowSourceTypeDef(TypedDict):
    FlowArn: str
    Name: str
    FlowVpcInterfaceAttachment: NotRequired[VpcInterfaceAttachmentTypeDef]
    OutputArn: NotRequired[str]

class GatewayBridgeSourceTypeDef(TypedDict):
    BridgeArn: str
    VpcInterfaceAttachment: NotRequired[VpcInterfaceAttachmentTypeDef]

class SetGatewayBridgeSourceRequestTypeDef(TypedDict):
    BridgeArn: str
    VpcInterfaceAttachment: NotRequired[VpcInterfaceAttachmentTypeDef]

class UpdateBridgeFlowSourceRequestTypeDef(TypedDict):
    FlowArn: NotRequired[str]
    FlowVpcInterfaceAttachment: NotRequired[VpcInterfaceAttachmentTypeDef]

class UpdateGatewayBridgeSourceRequestTypeDef(TypedDict):
    BridgeArn: NotRequired[str]
    VpcInterfaceAttachment: NotRequired[VpcInterfaceAttachmentTypeDef]

class AddBridgeOutputRequestTypeDef(TypedDict):
    NetworkOutput: NotRequired[AddBridgeNetworkOutputRequestTypeDef]

AddBridgeNetworkSourceRequestTypeDef = TypedDict(
    "AddBridgeNetworkSourceRequestTypeDef",
    {
        "MulticastIp": str,
        "Name": str,
        "NetworkName": str,
        "Port": int,
        "Protocol": ProtocolType,
        "MulticastSourceSettings": NotRequired[MulticastSourceSettingsTypeDef],
    },
)
BridgeNetworkSourceTypeDef = TypedDict(
    "BridgeNetworkSourceTypeDef",
    {
        "MulticastIp": str,
        "Name": str,
        "NetworkName": str,
        "Port": int,
        "Protocol": ProtocolType,
        "MulticastSourceSettings": NotRequired[MulticastSourceSettingsTypeDef],
    },
)
UpdateBridgeNetworkSourceRequestTypeDef = TypedDict(
    "UpdateBridgeNetworkSourceRequestTypeDef",
    {
        "MulticastIp": NotRequired[str],
        "MulticastSourceSettings": NotRequired[MulticastSourceSettingsTypeDef],
        "NetworkName": NotRequired[str],
        "Port": NotRequired[int],
        "Protocol": NotRequired[ProtocolType],
    },
)

class DeleteBridgeResponseTypeDef(TypedDict):
    BridgeArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFlowResponseTypeDef(TypedDict):
    FlowArn: str
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGatewayResponseTypeDef(TypedDict):
    GatewayArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRouterInputResponseTypeDef(TypedDict):
    Arn: str
    Name: str
    State: RouterInputStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRouterNetworkInterfaceResponseTypeDef(TypedDict):
    Arn: str
    Name: str
    State: RouterNetworkInterfaceStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRouterOutputResponseTypeDef(TypedDict):
    Arn: str
    Name: str
    State: RouterOutputStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterGatewayInstanceResponseTypeDef(TypedDict):
    GatewayInstanceArn: str
    InstanceState: InstanceStateType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForGlobalResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveBridgeOutputResponseTypeDef(TypedDict):
    BridgeArn: str
    OutputName: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveBridgeSourceResponseTypeDef(TypedDict):
    BridgeArn: str
    SourceName: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveFlowMediaStreamResponseTypeDef(TypedDict):
    FlowArn: str
    MediaStreamName: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveFlowOutputResponseTypeDef(TypedDict):
    FlowArn: str
    OutputArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveFlowSourceResponseTypeDef(TypedDict):
    FlowArn: str
    SourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveFlowVpcInterfaceResponseTypeDef(TypedDict):
    FlowArn: str
    NonDeletedNetworkInterfaceIds: List[str]
    VpcInterfaceName: str
    ResponseMetadata: ResponseMetadataTypeDef

class RestartRouterInputResponseTypeDef(TypedDict):
    Arn: str
    Name: str
    State: RouterInputStateType
    ResponseMetadata: ResponseMetadataTypeDef

class RestartRouterOutputResponseTypeDef(TypedDict):
    Arn: str
    Name: str
    State: RouterOutputStateType
    ResponseMetadata: ResponseMetadataTypeDef

class RevokeFlowEntitlementResponseTypeDef(TypedDict):
    EntitlementArn: str
    FlowArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartFlowResponseTypeDef(TypedDict):
    FlowArn: str
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopFlowResponseTypeDef(TypedDict):
    FlowArn: str
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopRouterInputResponseTypeDef(TypedDict):
    Arn: str
    Name: str
    State: RouterInputStateType
    ResponseMetadata: ResponseMetadataTypeDef

class StopRouterOutputResponseTypeDef(TypedDict):
    Arn: str
    Name: str
    State: RouterOutputStateType
    ResponseMetadata: ResponseMetadataTypeDef

class TakeRouterInputResponseTypeDef(TypedDict):
    RoutedState: RouterOutputRoutedStateType
    RouterOutputArn: str
    RouterOutputName: str
    RouterInputArn: str
    RouterInputName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBridgeStateResponseTypeDef(TypedDict):
    BridgeArn: str
    DesiredState: DesiredStateType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGatewayInstanceResponseTypeDef(TypedDict):
    BridgePlacement: BridgePlacementType
    GatewayInstanceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddFlowVpcInterfacesRequestTypeDef(TypedDict):
    FlowArn: str
    VpcInterfaces: Sequence[VpcInterfaceRequestTypeDef]

class AddFlowVpcInterfacesResponseTypeDef(TypedDict):
    FlowArn: str
    VpcInterfaces: List[VpcInterfaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EntitlementTypeDef(TypedDict):
    EntitlementArn: str
    Name: str
    Subscribers: List[str]
    DataTransferSubscriberFeePercent: NotRequired[int]
    Description: NotRequired[str]
    Encryption: NotRequired[EncryptionTypeDef]
    EntitlementStatus: NotRequired[EntitlementStatusType]

class GrantEntitlementRequestTypeDef(TypedDict):
    Subscribers: Sequence[str]
    DataTransferSubscriberFeePercent: NotRequired[int]
    Description: NotRequired[str]
    Encryption: NotRequired[EncryptionTypeDef]
    EntitlementStatus: NotRequired[EntitlementStatusType]
    Name: NotRequired[str]
    EntitlementTags: NotRequired[Mapping[str, str]]

class AudioMonitoringSettingTypeDef(TypedDict):
    SilentAudio: NotRequired[SilentAudioTypeDef]

class BridgeOutputTypeDef(TypedDict):
    FlowOutput: NotRequired[BridgeFlowOutputTypeDef]
    NetworkOutput: NotRequired[BridgeNetworkOutputTypeDef]

class GatewayInstanceTypeDef(TypedDict):
    BridgePlacement: BridgePlacementType
    ConnectionStatus: ConnectionStatusType
    GatewayArn: str
    GatewayInstanceArn: str
    InstanceId: str
    InstanceState: InstanceStateType
    RunningBridgeCount: int
    InstanceMessages: NotRequired[List[MessageDetailTypeDef]]

class ThumbnailDetailsTypeDef(TypedDict):
    FlowArn: str
    ThumbnailMessages: List[MessageDetailTypeDef]
    Thumbnail: NotRequired[str]
    Timecode: NotRequired[str]
    Timestamp: NotRequired[datetime]

class CreateGatewayRequestTypeDef(TypedDict):
    EgressCidrBlocks: Sequence[str]
    Name: str
    Networks: Sequence[GatewayNetworkTypeDef]

class GatewayTypeDef(TypedDict):
    EgressCidrBlocks: List[str]
    GatewayArn: str
    Name: str
    Networks: List[GatewayNetworkTypeDef]
    GatewayMessages: NotRequired[List[MessageDetailTypeDef]]
    GatewayState: NotRequired[GatewayStateType]

class DescribeFlowRequestWaitExtraExtraTypeDef(TypedDict):
    FlowArn: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeFlowRequestWaitExtraTypeDef(TypedDict):
    FlowArn: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeFlowRequestWaitTypeDef(TypedDict):
    FlowArn: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetRouterInputRequestWaitExtraExtraTypeDef(TypedDict):
    Arn: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetRouterInputRequestWaitExtraTypeDef(TypedDict):
    Arn: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetRouterInputRequestWaitTypeDef(TypedDict):
    Arn: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetRouterOutputRequestWaitExtraExtraExtraTypeDef(TypedDict):
    Arn: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetRouterOutputRequestWaitExtraExtraTypeDef(TypedDict):
    Arn: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetRouterOutputRequestWaitExtraTypeDef(TypedDict):
    Arn: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetRouterOutputRequestWaitTypeDef(TypedDict):
    Arn: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DestinationConfigurationRequestTypeDef(TypedDict):
    DestinationIp: str
    DestinationPort: int
    Interface: InterfaceRequestTypeDef

class InputConfigurationRequestTypeDef(TypedDict):
    InputPort: int
    Interface: InterfaceRequestTypeDef

class DestinationConfigurationTypeDef(TypedDict):
    DestinationIp: str
    DestinationPort: int
    Interface: InterfaceTypeDef
    OutboundIp: str

class InputConfigurationTypeDef(TypedDict):
    InputIp: str
    InputPort: int
    Interface: InterfaceTypeDef

class FailoverConfigTypeDef(TypedDict):
    FailoverMode: NotRequired[FailoverModeType]
    RecoveryWindow: NotRequired[int]
    SourcePriority: NotRequired[SourcePriorityTypeDef]
    State: NotRequired[StateType]

class UpdateFailoverConfigTypeDef(TypedDict):
    FailoverMode: NotRequired[FailoverModeType]
    RecoveryWindow: NotRequired[int]
    SourcePriority: NotRequired[SourcePriorityTypeDef]
    State: NotRequired[StateType]

class FailoverRouterInputStreamDetailsTypeDef(TypedDict):
    SourceIndexZeroStreamDetails: FailoverRouterInputIndexedStreamDetailsTypeDef
    SourceIndexOneStreamDetails: FailoverRouterInputIndexedStreamDetailsTypeDef

class MergeRouterInputProtocolConfigurationTypeDef(TypedDict):
    Rtp: NotRequired[RtpRouterInputConfigurationTypeDef]
    Rist: NotRequired[RistRouterInputConfigurationTypeDef]

class FlowTransitEncryptionKeyConfigurationOutputTypeDef(TypedDict):
    SecretsManager: NotRequired[SecretsManagerEncryptionKeyConfigurationTypeDef]
    Automatic: NotRequired[Dict[str, Any]]

class FlowTransitEncryptionKeyConfigurationTypeDef(TypedDict):
    SecretsManager: NotRequired[SecretsManagerEncryptionKeyConfigurationTypeDef]
    Automatic: NotRequired[Mapping[str, Any]]

class MediaLiveTransitEncryptionKeyConfigurationOutputTypeDef(TypedDict):
    SecretsManager: NotRequired[SecretsManagerEncryptionKeyConfigurationTypeDef]
    Automatic: NotRequired[Dict[str, Any]]

class MediaLiveTransitEncryptionKeyConfigurationTypeDef(TypedDict):
    SecretsManager: NotRequired[SecretsManagerEncryptionKeyConfigurationTypeDef]
    Automatic: NotRequired[Mapping[str, Any]]

class RouterInputTransitEncryptionKeyConfigurationOutputTypeDef(TypedDict):
    SecretsManager: NotRequired[SecretsManagerEncryptionKeyConfigurationTypeDef]
    Automatic: NotRequired[Dict[str, Any]]

class RouterInputTransitEncryptionKeyConfigurationTypeDef(TypedDict):
    SecretsManager: NotRequired[SecretsManagerEncryptionKeyConfigurationTypeDef]
    Automatic: NotRequired[Mapping[str, Any]]

class SrtDecryptionConfigurationTypeDef(TypedDict):
    EncryptionKey: SecretsManagerEncryptionKeyConfigurationTypeDef

class SrtEncryptionConfigurationTypeDef(TypedDict):
    EncryptionKey: SecretsManagerEncryptionKeyConfigurationTypeDef

class ListedFlowTypeDef(TypedDict):
    AvailabilityZone: str
    Description: str
    FlowArn: str
    Name: str
    SourceType: SourceTypeType
    Status: StatusType
    Maintenance: NotRequired[MaintenanceTypeDef]

class MediaStreamAttributesRequestTypeDef(TypedDict):
    Fmtp: NotRequired[FmtpRequestTypeDef]
    Lang: NotRequired[str]

class MediaStreamAttributesTypeDef(TypedDict):
    Fmtp: FmtpTypeDef
    Lang: NotRequired[str]

class TransportStreamTypeDef(TypedDict):
    Pid: int
    StreamType: str
    Channels: NotRequired[int]
    Codec: NotRequired[str]
    FrameRate: NotRequired[str]
    FrameResolution: NotRequired[FrameResolutionTypeDef]
    SampleRate: NotRequired[int]
    SampleSize: NotRequired[int]

class VideoMonitoringSettingTypeDef(TypedDict):
    BlackFrames: NotRequired[BlackFramesTypeDef]
    FrozenFrames: NotRequired[FrozenFramesTypeDef]

class ListBridgesRequestPaginateTypeDef(TypedDict):
    FilterArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEntitlementsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFlowsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGatewayInstancesRequestPaginateTypeDef(TypedDict):
    FilterArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGatewaysRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOfferingsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListReservationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListBridgesResponseTypeDef(TypedDict):
    Bridges: List[ListedBridgeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListEntitlementsResponseTypeDef(TypedDict):
    Entitlements: List[ListedEntitlementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListGatewayInstancesResponseTypeDef(TypedDict):
    Instances: List[ListedGatewayInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListGatewaysResponseTypeDef(TypedDict):
    Gateways: List[ListedGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListRouterInputsRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[RouterInputFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRouterInputsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Filters: NotRequired[Sequence[RouterInputFilterTypeDef]]

class ListRouterNetworkInterfacesRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[RouterNetworkInterfaceFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRouterNetworkInterfacesRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Filters: NotRequired[Sequence[RouterNetworkInterfaceFilterTypeDef]]

class ListRouterNetworkInterfacesResponseTypeDef(TypedDict):
    RouterNetworkInterfaces: List[ListedRouterNetworkInterfaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListRouterOutputsRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[RouterOutputFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRouterOutputsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Filters: NotRequired[Sequence[RouterOutputFilterTypeDef]]

class MaintenanceConfigurationOutputTypeDef(TypedDict):
    PreferredDayTime: NotRequired[PreferredDayTimeMaintenanceConfigurationTypeDef]
    Default: NotRequired[Dict[str, Any]]

class MaintenanceConfigurationTypeDef(TypedDict):
    PreferredDayTime: NotRequired[PreferredDayTimeMaintenanceConfigurationTypeDef]
    Default: NotRequired[Mapping[str, Any]]

class MaintenanceScheduleTypeDef(TypedDict):
    Window: NotRequired[WindowMaintenanceScheduleTypeDef]

class MergeRouterInputStreamDetailsTypeDef(TypedDict):
    SourceIndexZeroStreamDetails: MergeRouterInputIndexedStreamDetailsTypeDef
    SourceIndexOneStreamDetails: MergeRouterInputIndexedStreamDetailsTypeDef

class NdiConfigOutputTypeDef(TypedDict):
    NdiState: NotRequired[NdiStateType]
    MachineName: NotRequired[str]
    NdiDiscoveryServers: NotRequired[List[NdiDiscoveryServerConfigTypeDef]]

class NdiConfigTypeDef(TypedDict):
    NdiState: NotRequired[NdiStateType]
    MachineName: NotRequired[str]
    NdiDiscoveryServers: NotRequired[Sequence[NdiDiscoveryServerConfigTypeDef]]

class OfferingTypeDef(TypedDict):
    CurrencyCode: str
    Duration: int
    DurationUnits: Literal["MONTHS"]
    OfferingArn: str
    OfferingDescription: str
    PricePerUnit: str
    PriceUnits: Literal["HOURLY"]
    ResourceSpecification: ResourceSpecificationTypeDef

class ReservationTypeDef(TypedDict):
    CurrencyCode: str
    Duration: int
    DurationUnits: Literal["MONTHS"]
    End: str
    OfferingArn: str
    OfferingDescription: str
    PricePerUnit: str
    PriceUnits: Literal["HOURLY"]
    ReservationArn: str
    ReservationName: str
    ReservationState: ReservationStateType
    ResourceSpecification: ResourceSpecificationTypeDef
    Start: str

class PublicRouterNetworkInterfaceConfigurationOutputTypeDef(TypedDict):
    AllowRules: List[PublicRouterNetworkInterfaceRuleTypeDef]

class PublicRouterNetworkInterfaceConfigurationTypeDef(TypedDict):
    AllowRules: Sequence[PublicRouterNetworkInterfaceRuleTypeDef]

class RouterInputThumbnailDetailsTypeDef(TypedDict):
    ThumbnailMessages: List[RouterInputMessageTypeDef]
    Thumbnail: NotRequired[bytes]
    Timecode: NotRequired[str]
    Timestamp: NotRequired[datetime]

class RouterOutputStreamDetailsTypeDef(TypedDict):
    Standard: NotRequired[StandardRouterOutputStreamDetailsTypeDef]
    MediaConnectFlow: NotRequired[Dict[str, Any]]
    MediaLiveInput: NotRequired[Dict[str, Any]]

class UpdateBridgeOutputRequestTypeDef(TypedDict):
    BridgeArn: str
    OutputName: str
    NetworkOutput: NotRequired[UpdateBridgeNetworkOutputRequestTypeDef]

class UpdateFlowEntitlementRequestTypeDef(TypedDict):
    EntitlementArn: str
    FlowArn: str
    Description: NotRequired[str]
    Encryption: NotRequired[UpdateEncryptionTypeDef]
    EntitlementStatus: NotRequired[EntitlementStatusType]
    Subscribers: NotRequired[Sequence[str]]

class AddBridgeOutputsRequestTypeDef(TypedDict):
    BridgeArn: str
    Outputs: Sequence[AddBridgeOutputRequestTypeDef]

class AddBridgeSourceRequestTypeDef(TypedDict):
    FlowSource: NotRequired[AddBridgeFlowSourceRequestTypeDef]
    NetworkSource: NotRequired[AddBridgeNetworkSourceRequestTypeDef]

class BridgeSourceTypeDef(TypedDict):
    FlowSource: NotRequired[BridgeFlowSourceTypeDef]
    NetworkSource: NotRequired[BridgeNetworkSourceTypeDef]

class UpdateBridgeSourceRequestTypeDef(TypedDict):
    BridgeArn: str
    SourceName: str
    FlowSource: NotRequired[UpdateBridgeFlowSourceRequestTypeDef]
    NetworkSource: NotRequired[UpdateBridgeNetworkSourceRequestTypeDef]

class GrantFlowEntitlementsResponseTypeDef(TypedDict):
    Entitlements: List[EntitlementTypeDef]
    FlowArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlowEntitlementResponseTypeDef(TypedDict):
    Entitlement: EntitlementTypeDef
    FlowArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GrantFlowEntitlementsRequestTypeDef(TypedDict):
    Entitlements: Sequence[GrantEntitlementRequestTypeDef]
    FlowArn: str

class AddBridgeOutputsResponseTypeDef(TypedDict):
    BridgeArn: str
    Outputs: List[BridgeOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBridgeOutputResponseTypeDef(TypedDict):
    BridgeArn: str
    Output: BridgeOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGatewayInstanceResponseTypeDef(TypedDict):
    GatewayInstance: GatewayInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFlowSourceThumbnailResponseTypeDef(TypedDict):
    ThumbnailDetails: ThumbnailDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGatewayResponseTypeDef(TypedDict):
    Gateway: GatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGatewayResponseTypeDef(TypedDict):
    Gateway: GatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MediaStreamOutputConfigurationRequestTypeDef(TypedDict):
    EncodingName: EncodingNameType
    MediaStreamName: str
    DestinationConfigurations: NotRequired[Sequence[DestinationConfigurationRequestTypeDef]]
    EncodingParameters: NotRequired[EncodingParametersRequestTypeDef]

class MediaStreamSourceConfigurationRequestTypeDef(TypedDict):
    EncodingName: EncodingNameType
    MediaStreamName: str
    InputConfigurations: NotRequired[Sequence[InputConfigurationRequestTypeDef]]

class MediaStreamOutputConfigurationTypeDef(TypedDict):
    EncodingName: EncodingNameType
    MediaStreamName: str
    DestinationConfigurations: NotRequired[List[DestinationConfigurationTypeDef]]
    EncodingParameters: NotRequired[EncodingParametersTypeDef]

class MediaStreamSourceConfigurationTypeDef(TypedDict):
    EncodingName: EncodingNameType
    MediaStreamName: str
    InputConfigurations: NotRequired[List[InputConfigurationTypeDef]]

class UpdateBridgeRequestTypeDef(TypedDict):
    BridgeArn: str
    EgressGatewayBridge: NotRequired[UpdateEgressGatewayBridgeRequestTypeDef]
    IngressGatewayBridge: NotRequired[UpdateIngressGatewayBridgeRequestTypeDef]
    SourceFailoverConfig: NotRequired[UpdateFailoverConfigTypeDef]

class MergeRouterInputConfigurationOutputTypeDef(TypedDict):
    NetworkInterfaceArn: str
    ProtocolConfigurations: List[MergeRouterInputProtocolConfigurationTypeDef]
    MergeRecoveryWindowMilliseconds: int

class MergeRouterInputConfigurationTypeDef(TypedDict):
    NetworkInterfaceArn: str
    ProtocolConfigurations: Sequence[MergeRouterInputProtocolConfigurationTypeDef]
    MergeRecoveryWindowMilliseconds: int

class FlowTransitEncryptionOutputTypeDef(TypedDict):
    EncryptionKeyConfiguration: FlowTransitEncryptionKeyConfigurationOutputTypeDef
    EncryptionKeyType: NotRequired[FlowTransitEncryptionKeyTypeType]

FlowTransitEncryptionKeyConfigurationUnionTypeDef = Union[
    FlowTransitEncryptionKeyConfigurationTypeDef, FlowTransitEncryptionKeyConfigurationOutputTypeDef
]

class MediaLiveTransitEncryptionOutputTypeDef(TypedDict):
    EncryptionKeyConfiguration: MediaLiveTransitEncryptionKeyConfigurationOutputTypeDef
    EncryptionKeyType: NotRequired[MediaLiveTransitEncryptionKeyTypeType]

class MediaLiveTransitEncryptionTypeDef(TypedDict):
    EncryptionKeyConfiguration: MediaLiveTransitEncryptionKeyConfigurationTypeDef
    EncryptionKeyType: NotRequired[MediaLiveTransitEncryptionKeyTypeType]

class RouterInputTransitEncryptionOutputTypeDef(TypedDict):
    EncryptionKeyConfiguration: RouterInputTransitEncryptionKeyConfigurationOutputTypeDef
    EncryptionKeyType: NotRequired[RouterInputTransitEncryptionKeyTypeType]

class RouterInputTransitEncryptionTypeDef(TypedDict):
    EncryptionKeyConfiguration: RouterInputTransitEncryptionKeyConfigurationTypeDef
    EncryptionKeyType: NotRequired[RouterInputTransitEncryptionKeyTypeType]

class SrtCallerRouterInputConfigurationTypeDef(TypedDict):
    SourceAddress: str
    SourcePort: int
    MinimumLatencyMilliseconds: int
    StreamId: NotRequired[str]
    DecryptionConfiguration: NotRequired[SrtDecryptionConfigurationTypeDef]

class SrtListenerRouterInputConfigurationTypeDef(TypedDict):
    Port: int
    MinimumLatencyMilliseconds: int
    DecryptionConfiguration: NotRequired[SrtDecryptionConfigurationTypeDef]

class SrtCallerRouterOutputConfigurationTypeDef(TypedDict):
    DestinationAddress: str
    DestinationPort: int
    MinimumLatencyMilliseconds: int
    StreamId: NotRequired[str]
    EncryptionConfiguration: NotRequired[SrtEncryptionConfigurationTypeDef]

class SrtListenerRouterOutputConfigurationTypeDef(TypedDict):
    Port: int
    MinimumLatencyMilliseconds: int
    EncryptionConfiguration: NotRequired[SrtEncryptionConfigurationTypeDef]

class ListFlowsResponseTypeDef(TypedDict):
    Flows: List[ListedFlowTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AddMediaStreamRequestTypeDef(TypedDict):
    MediaStreamId: int
    MediaStreamName: str
    MediaStreamType: MediaStreamTypeType
    Attributes: NotRequired[MediaStreamAttributesRequestTypeDef]
    ClockRate: NotRequired[int]
    Description: NotRequired[str]
    VideoFormat: NotRequired[str]
    MediaStreamTags: NotRequired[Mapping[str, str]]

class UpdateFlowMediaStreamRequestTypeDef(TypedDict):
    FlowArn: str
    MediaStreamName: str
    Attributes: NotRequired[MediaStreamAttributesRequestTypeDef]
    ClockRate: NotRequired[int]
    Description: NotRequired[str]
    MediaStreamType: NotRequired[MediaStreamTypeType]
    VideoFormat: NotRequired[str]

class MediaStreamTypeDef(TypedDict):
    Fmt: int
    MediaStreamId: int
    MediaStreamName: str
    MediaStreamType: MediaStreamTypeType
    Attributes: NotRequired[MediaStreamAttributesTypeDef]
    ClockRate: NotRequired[int]
    Description: NotRequired[str]
    VideoFormat: NotRequired[str]

class TransportStreamProgramTypeDef(TypedDict):
    PcrPid: int
    ProgramNumber: int
    ProgramPid: int
    Streams: List[TransportStreamTypeDef]
    ProgramName: NotRequired[str]

class MonitoringConfigOutputTypeDef(TypedDict):
    ThumbnailState: NotRequired[ThumbnailStateType]
    AudioMonitoringSettings: NotRequired[List[AudioMonitoringSettingTypeDef]]
    ContentQualityAnalysisState: NotRequired[ContentQualityAnalysisStateType]
    VideoMonitoringSettings: NotRequired[List[VideoMonitoringSettingTypeDef]]

class MonitoringConfigTypeDef(TypedDict):
    ThumbnailState: NotRequired[ThumbnailStateType]
    AudioMonitoringSettings: NotRequired[Sequence[AudioMonitoringSettingTypeDef]]
    ContentQualityAnalysisState: NotRequired[ContentQualityAnalysisStateType]
    VideoMonitoringSettings: NotRequired[Sequence[VideoMonitoringSettingTypeDef]]

MaintenanceConfigurationUnionTypeDef = Union[
    MaintenanceConfigurationTypeDef, MaintenanceConfigurationOutputTypeDef
]
ListedRouterInputTypeDef = TypedDict(
    "ListedRouterInputTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Id": str,
        "InputType": RouterInputTypeType,
        "State": RouterInputStateType,
        "RoutedOutputs": int,
        "RegionName": str,
        "AvailabilityZone": str,
        "MaximumBitrate": int,
        "RoutingScope": RoutingScopeType,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "MessageCount": int,
        "NetworkInterfaceArn": NotRequired[str],
        "MaintenanceScheduleType": NotRequired[Literal["WINDOW"]],
        "MaintenanceSchedule": NotRequired[MaintenanceScheduleTypeDef],
    },
)
ListedRouterOutputTypeDef = TypedDict(
    "ListedRouterOutputTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Id": str,
        "OutputType": RouterOutputTypeType,
        "State": RouterOutputStateType,
        "RoutedState": RouterOutputRoutedStateType,
        "RegionName": str,
        "AvailabilityZone": str,
        "MaximumBitrate": int,
        "RoutingScope": RoutingScopeType,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "MessageCount": int,
        "RoutedInputArn": NotRequired[str],
        "NetworkInterfaceArn": NotRequired[str],
        "MaintenanceScheduleType": NotRequired[Literal["WINDOW"]],
        "MaintenanceSchedule": NotRequired[MaintenanceScheduleTypeDef],
    },
)

class StartRouterInputResponseTypeDef(TypedDict):
    Arn: str
    Name: str
    State: RouterInputStateType
    MaintenanceScheduleType: Literal["WINDOW"]
    MaintenanceSchedule: MaintenanceScheduleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartRouterOutputResponseTypeDef(TypedDict):
    Arn: str
    Name: str
    State: RouterOutputStateType
    MaintenanceScheduleType: Literal["WINDOW"]
    MaintenanceSchedule: MaintenanceScheduleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RouterInputStreamDetailsTypeDef(TypedDict):
    Standard: NotRequired[StandardRouterInputStreamDetailsTypeDef]
    Failover: NotRequired[FailoverRouterInputStreamDetailsTypeDef]
    Merge: NotRequired[MergeRouterInputStreamDetailsTypeDef]
    MediaConnectFlow: NotRequired[Dict[str, Any]]

NdiConfigUnionTypeDef = Union[NdiConfigTypeDef, NdiConfigOutputTypeDef]

class DescribeOfferingResponseTypeDef(TypedDict):
    Offering: OfferingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListOfferingsResponseTypeDef(TypedDict):
    Offerings: List[OfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeReservationResponseTypeDef(TypedDict):
    Reservation: ReservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListReservationsResponseTypeDef(TypedDict):
    Reservations: List[ReservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PurchaseOfferingResponseTypeDef(TypedDict):
    Reservation: ReservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RouterNetworkInterfaceConfigurationOutputTypeDef(TypedDict):
    Public: NotRequired[PublicRouterNetworkInterfaceConfigurationOutputTypeDef]
    Vpc: NotRequired[VpcRouterNetworkInterfaceConfigurationOutputTypeDef]

class RouterNetworkInterfaceConfigurationTypeDef(TypedDict):
    Public: NotRequired[PublicRouterNetworkInterfaceConfigurationTypeDef]
    Vpc: NotRequired[VpcRouterNetworkInterfaceConfigurationTypeDef]

class GetRouterInputThumbnailResponseTypeDef(TypedDict):
    Arn: str
    Name: str
    ThumbnailDetails: RouterInputThumbnailDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddBridgeSourcesRequestTypeDef(TypedDict):
    BridgeArn: str
    Sources: Sequence[AddBridgeSourceRequestTypeDef]

class CreateBridgeRequestTypeDef(TypedDict):
    Name: str
    PlacementArn: str
    Sources: Sequence[AddBridgeSourceRequestTypeDef]
    EgressGatewayBridge: NotRequired[AddEgressGatewayBridgeRequestTypeDef]
    IngressGatewayBridge: NotRequired[AddIngressGatewayBridgeRequestTypeDef]
    Outputs: NotRequired[Sequence[AddBridgeOutputRequestTypeDef]]
    SourceFailoverConfig: NotRequired[FailoverConfigTypeDef]

class AddBridgeSourcesResponseTypeDef(TypedDict):
    BridgeArn: str
    Sources: List[BridgeSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BridgeTypeDef(TypedDict):
    BridgeArn: str
    BridgeState: BridgeStateType
    Name: str
    PlacementArn: str
    BridgeMessages: NotRequired[List[MessageDetailTypeDef]]
    EgressGatewayBridge: NotRequired[EgressGatewayBridgeTypeDef]
    IngressGatewayBridge: NotRequired[IngressGatewayBridgeTypeDef]
    Outputs: NotRequired[List[BridgeOutputTypeDef]]
    SourceFailoverConfig: NotRequired[FailoverConfigTypeDef]
    Sources: NotRequired[List[BridgeSourceTypeDef]]

class UpdateBridgeSourceResponseTypeDef(TypedDict):
    BridgeArn: str
    Source: BridgeSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MediaConnectFlowRouterInputConfigurationOutputTypeDef(TypedDict):
    SourceTransitDecryption: FlowTransitEncryptionOutputTypeDef
    FlowArn: NotRequired[str]
    FlowOutputArn: NotRequired[str]

class MediaConnectFlowRouterOutputConfigurationOutputTypeDef(TypedDict):
    DestinationTransitEncryption: FlowTransitEncryptionOutputTypeDef
    FlowArn: NotRequired[str]
    FlowSourceArn: NotRequired[str]

class OutputTypeDef(TypedDict):
    Name: str
    OutputArn: str
    DataTransferSubscriberFeePercent: NotRequired[int]
    Description: NotRequired[str]
    Destination: NotRequired[str]
    Encryption: NotRequired[EncryptionTypeDef]
    EntitlementArn: NotRequired[str]
    ListenerAddress: NotRequired[str]
    MediaLiveInputArn: NotRequired[str]
    MediaStreamOutputConfigurations: NotRequired[List[MediaStreamOutputConfigurationTypeDef]]
    Port: NotRequired[int]
    Transport: NotRequired[TransportTypeDef]
    VpcInterfaceAttachment: NotRequired[VpcInterfaceAttachmentTypeDef]
    BridgeArn: NotRequired[str]
    BridgePorts: NotRequired[List[int]]
    OutputStatus: NotRequired[OutputStatusType]
    PeerIpAddress: NotRequired[str]
    RouterIntegrationState: NotRequired[StateType]
    RouterIntegrationTransitEncryption: NotRequired[FlowTransitEncryptionOutputTypeDef]
    ConnectedRouterInputArn: NotRequired[str]

class SourceTypeDef(TypedDict):
    Name: str
    SourceArn: str
    DataTransferSubscriberFeePercent: NotRequired[int]
    Decryption: NotRequired[EncryptionTypeDef]
    Description: NotRequired[str]
    EntitlementArn: NotRequired[str]
    IngestIp: NotRequired[str]
    IngestPort: NotRequired[int]
    MediaStreamSourceConfigurations: NotRequired[List[MediaStreamSourceConfigurationTypeDef]]
    SenderControlPort: NotRequired[int]
    SenderIpAddress: NotRequired[str]
    Transport: NotRequired[TransportTypeDef]
    VpcInterfaceName: NotRequired[str]
    WhitelistCidr: NotRequired[str]
    GatewayBridgeSource: NotRequired[GatewayBridgeSourceTypeDef]
    PeerIpAddress: NotRequired[str]
    RouterIntegrationState: NotRequired[StateType]
    RouterIntegrationTransitDecryption: NotRequired[FlowTransitEncryptionOutputTypeDef]
    ConnectedRouterOutputArn: NotRequired[str]

class FlowTransitEncryptionTypeDef(TypedDict):
    EncryptionKeyConfiguration: FlowTransitEncryptionKeyConfigurationUnionTypeDef
    EncryptionKeyType: NotRequired[FlowTransitEncryptionKeyTypeType]

class MediaLiveInputRouterOutputConfigurationOutputTypeDef(TypedDict):
    DestinationTransitEncryption: MediaLiveTransitEncryptionOutputTypeDef
    MediaLiveInputArn: NotRequired[str]
    MediaLivePipelineId: NotRequired[MediaLiveInputPipelineIdType]

class MediaLiveInputRouterOutputConfigurationTypeDef(TypedDict):
    DestinationTransitEncryption: MediaLiveTransitEncryptionTypeDef
    MediaLiveInputArn: NotRequired[str]
    MediaLivePipelineId: NotRequired[MediaLiveInputPipelineIdType]

RouterInputTransitEncryptionUnionTypeDef = Union[
    RouterInputTransitEncryptionTypeDef, RouterInputTransitEncryptionOutputTypeDef
]

class FailoverRouterInputProtocolConfigurationTypeDef(TypedDict):
    Rtp: NotRequired[RtpRouterInputConfigurationTypeDef]
    Rist: NotRequired[RistRouterInputConfigurationTypeDef]
    SrtListener: NotRequired[SrtListenerRouterInputConfigurationTypeDef]
    SrtCaller: NotRequired[SrtCallerRouterInputConfigurationTypeDef]

class RouterInputProtocolConfigurationTypeDef(TypedDict):
    Rtp: NotRequired[RtpRouterInputConfigurationTypeDef]
    Rist: NotRequired[RistRouterInputConfigurationTypeDef]
    SrtListener: NotRequired[SrtListenerRouterInputConfigurationTypeDef]
    SrtCaller: NotRequired[SrtCallerRouterInputConfigurationTypeDef]

class RouterOutputProtocolConfigurationTypeDef(TypedDict):
    Rtp: NotRequired[RtpRouterOutputConfigurationTypeDef]
    Rist: NotRequired[RistRouterOutputConfigurationTypeDef]
    SrtListener: NotRequired[SrtListenerRouterOutputConfigurationTypeDef]
    SrtCaller: NotRequired[SrtCallerRouterOutputConfigurationTypeDef]

class AddFlowMediaStreamsRequestTypeDef(TypedDict):
    FlowArn: str
    MediaStreams: Sequence[AddMediaStreamRequestTypeDef]

class AddFlowMediaStreamsResponseTypeDef(TypedDict):
    FlowArn: str
    MediaStreams: List[MediaStreamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlowMediaStreamResponseTypeDef(TypedDict):
    FlowArn: str
    MediaStream: MediaStreamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TransportMediaInfoTypeDef(TypedDict):
    Programs: List[TransportStreamProgramTypeDef]

MonitoringConfigUnionTypeDef = Union[MonitoringConfigTypeDef, MonitoringConfigOutputTypeDef]

class ListRouterInputsResponseTypeDef(TypedDict):
    RouterInputs: List[ListedRouterInputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListRouterOutputsResponseTypeDef(TypedDict):
    RouterOutputs: List[ListedRouterOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

RouterNetworkInterfaceTypeDef = TypedDict(
    "RouterNetworkInterfaceTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Id": str,
        "State": RouterNetworkInterfaceStateType,
        "NetworkInterfaceType": RouterNetworkInterfaceTypeType,
        "Configuration": RouterNetworkInterfaceConfigurationOutputTypeDef,
        "AssociatedOutputCount": int,
        "AssociatedInputCount": int,
        "RegionName": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Tags": Dict[str, str],
    },
)
RouterNetworkInterfaceConfigurationUnionTypeDef = Union[
    RouterNetworkInterfaceConfigurationTypeDef, RouterNetworkInterfaceConfigurationOutputTypeDef
]

class CreateBridgeResponseTypeDef(TypedDict):
    Bridge: BridgeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBridgeResponseTypeDef(TypedDict):
    Bridge: BridgeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBridgeResponseTypeDef(TypedDict):
    Bridge: BridgeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddFlowOutputsResponseTypeDef(TypedDict):
    FlowArn: str
    Outputs: List[OutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlowOutputResponseTypeDef(TypedDict):
    FlowArn: str
    Output: OutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddFlowSourcesResponseTypeDef(TypedDict):
    FlowArn: str
    Sources: List[SourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FlowTypeDef(TypedDict):
    AvailabilityZone: str
    Entitlements: List[EntitlementTypeDef]
    FlowArn: str
    Name: str
    Outputs: List[OutputTypeDef]
    Source: SourceTypeDef
    Status: StatusType
    Description: NotRequired[str]
    EgressIp: NotRequired[str]
    MediaStreams: NotRequired[List[MediaStreamTypeDef]]
    SourceFailoverConfig: NotRequired[FailoverConfigTypeDef]
    Sources: NotRequired[List[SourceTypeDef]]
    VpcInterfaces: NotRequired[List[VpcInterfaceTypeDef]]
    Maintenance: NotRequired[MaintenanceTypeDef]
    SourceMonitoringConfig: NotRequired[MonitoringConfigOutputTypeDef]
    FlowSize: NotRequired[FlowSizeType]
    NdiConfig: NotRequired[NdiConfigOutputTypeDef]

class UpdateFlowSourceResponseTypeDef(TypedDict):
    FlowArn: str
    Source: SourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

FlowTransitEncryptionUnionTypeDef = Union[
    FlowTransitEncryptionTypeDef, FlowTransitEncryptionOutputTypeDef
]

class MediaConnectFlowRouterInputConfigurationTypeDef(TypedDict):
    SourceTransitDecryption: FlowTransitEncryptionTypeDef
    FlowArn: NotRequired[str]
    FlowOutputArn: NotRequired[str]

class MediaConnectFlowRouterOutputConfigurationTypeDef(TypedDict):
    DestinationTransitEncryption: FlowTransitEncryptionTypeDef
    FlowArn: NotRequired[str]
    FlowSourceArn: NotRequired[str]

class FailoverRouterInputConfigurationOutputTypeDef(TypedDict):
    NetworkInterfaceArn: str
    ProtocolConfigurations: List[FailoverRouterInputProtocolConfigurationTypeDef]
    SourcePriorityMode: FailoverInputSourcePriorityModeType
    PrimarySourceIndex: NotRequired[int]

class FailoverRouterInputConfigurationTypeDef(TypedDict):
    NetworkInterfaceArn: str
    ProtocolConfigurations: Sequence[FailoverRouterInputProtocolConfigurationTypeDef]
    SourcePriorityMode: FailoverInputSourcePriorityModeType
    PrimarySourceIndex: NotRequired[int]

StandardRouterInputConfigurationTypeDef = TypedDict(
    "StandardRouterInputConfigurationTypeDef",
    {
        "NetworkInterfaceArn": str,
        "ProtocolConfiguration": RouterInputProtocolConfigurationTypeDef,
        "Protocol": NotRequired[RouterInputProtocolType],
    },
)
StandardRouterOutputConfigurationTypeDef = TypedDict(
    "StandardRouterOutputConfigurationTypeDef",
    {
        "NetworkInterfaceArn": str,
        "ProtocolConfiguration": RouterOutputProtocolConfigurationTypeDef,
        "Protocol": NotRequired[RouterOutputProtocolType],
    },
)

class DescribeFlowSourceMetadataResponseTypeDef(TypedDict):
    FlowArn: str
    Messages: List[MessageDetailTypeDef]
    Timestamp: datetime
    TransportMediaInfo: TransportMediaInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RouterInputMetadataTypeDef(TypedDict):
    TransportStreamMediaInfo: NotRequired[TransportMediaInfoTypeDef]

class UpdateFlowRequestTypeDef(TypedDict):
    FlowArn: str
    SourceFailoverConfig: NotRequired[UpdateFailoverConfigTypeDef]
    Maintenance: NotRequired[UpdateMaintenanceTypeDef]
    SourceMonitoringConfig: NotRequired[MonitoringConfigUnionTypeDef]
    NdiConfig: NotRequired[NdiConfigUnionTypeDef]
    FlowSize: NotRequired[FlowSizeType]

class BatchGetRouterNetworkInterfaceResponseTypeDef(TypedDict):
    RouterNetworkInterfaces: List[RouterNetworkInterfaceTypeDef]
    Errors: List[BatchGetRouterNetworkInterfaceErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRouterNetworkInterfaceResponseTypeDef(TypedDict):
    RouterNetworkInterface: RouterNetworkInterfaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRouterNetworkInterfaceResponseTypeDef(TypedDict):
    RouterNetworkInterface: RouterNetworkInterfaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRouterNetworkInterfaceResponseTypeDef(TypedDict):
    RouterNetworkInterface: RouterNetworkInterfaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

CreateRouterNetworkInterfaceRequestTypeDef = TypedDict(
    "CreateRouterNetworkInterfaceRequestTypeDef",
    {
        "Name": str,
        "Configuration": RouterNetworkInterfaceConfigurationUnionTypeDef,
        "RegionName": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "ClientToken": NotRequired[str],
    },
)

class UpdateRouterNetworkInterfaceRequestTypeDef(TypedDict):
    Arn: str
    Name: NotRequired[str]
    Configuration: NotRequired[RouterNetworkInterfaceConfigurationUnionTypeDef]

class CreateFlowResponseTypeDef(TypedDict):
    Flow: FlowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFlowResponseTypeDef(TypedDict):
    Flow: FlowTypeDef
    Messages: MessagesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlowResponseTypeDef(TypedDict):
    Flow: FlowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

AddOutputRequestTypeDef = TypedDict(
    "AddOutputRequestTypeDef",
    {
        "CidrAllowList": NotRequired[Sequence[str]],
        "Description": NotRequired[str],
        "Destination": NotRequired[str],
        "Encryption": NotRequired[EncryptionTypeDef],
        "MaxLatency": NotRequired[int],
        "MediaStreamOutputConfigurations": NotRequired[
            Sequence[MediaStreamOutputConfigurationRequestTypeDef]
        ],
        "MinLatency": NotRequired[int],
        "Name": NotRequired[str],
        "Port": NotRequired[int],
        "Protocol": NotRequired[ProtocolType],
        "RemoteId": NotRequired[str],
        "SenderControlPort": NotRequired[int],
        "SmoothingLatency": NotRequired[int],
        "StreamId": NotRequired[str],
        "VpcInterfaceAttachment": NotRequired[VpcInterfaceAttachmentTypeDef],
        "OutputStatus": NotRequired[OutputStatusType],
        "NdiSpeedHqQuality": NotRequired[int],
        "NdiProgramName": NotRequired[str],
        "OutputTags": NotRequired[Mapping[str, str]],
        "RouterIntegrationState": NotRequired[StateType],
        "RouterIntegrationTransitEncryption": NotRequired[FlowTransitEncryptionUnionTypeDef],
    },
)
SetSourceRequestTypeDef = TypedDict(
    "SetSourceRequestTypeDef",
    {
        "Decryption": NotRequired[EncryptionTypeDef],
        "Description": NotRequired[str],
        "EntitlementArn": NotRequired[str],
        "IngestPort": NotRequired[int],
        "MaxBitrate": NotRequired[int],
        "MaxLatency": NotRequired[int],
        "MaxSyncBuffer": NotRequired[int],
        "MediaStreamSourceConfigurations": NotRequired[
            Sequence[MediaStreamSourceConfigurationRequestTypeDef]
        ],
        "MinLatency": NotRequired[int],
        "Name": NotRequired[str],
        "Protocol": NotRequired[ProtocolType],
        "SenderControlPort": NotRequired[int],
        "SenderIpAddress": NotRequired[str],
        "SourceListenerAddress": NotRequired[str],
        "SourceListenerPort": NotRequired[int],
        "StreamId": NotRequired[str],
        "VpcInterfaceName": NotRequired[str],
        "WhitelistCidr": NotRequired[str],
        "GatewayBridgeSource": NotRequired[SetGatewayBridgeSourceRequestTypeDef],
        "SourceTags": NotRequired[Mapping[str, str]],
        "RouterIntegrationState": NotRequired[StateType],
        "RouterIntegrationTransitDecryption": NotRequired[FlowTransitEncryptionUnionTypeDef],
    },
)
UpdateFlowOutputRequestTypeDef = TypedDict(
    "UpdateFlowOutputRequestTypeDef",
    {
        "FlowArn": str,
        "OutputArn": str,
        "CidrAllowList": NotRequired[Sequence[str]],
        "Description": NotRequired[str],
        "Destination": NotRequired[str],
        "Encryption": NotRequired[UpdateEncryptionTypeDef],
        "MaxLatency": NotRequired[int],
        "MediaStreamOutputConfigurations": NotRequired[
            Sequence[MediaStreamOutputConfigurationRequestTypeDef]
        ],
        "MinLatency": NotRequired[int],
        "Port": NotRequired[int],
        "Protocol": NotRequired[ProtocolType],
        "RemoteId": NotRequired[str],
        "SenderControlPort": NotRequired[int],
        "SenderIpAddress": NotRequired[str],
        "SmoothingLatency": NotRequired[int],
        "StreamId": NotRequired[str],
        "VpcInterfaceAttachment": NotRequired[VpcInterfaceAttachmentTypeDef],
        "OutputStatus": NotRequired[OutputStatusType],
        "NdiProgramName": NotRequired[str],
        "NdiSpeedHqQuality": NotRequired[int],
        "RouterIntegrationState": NotRequired[StateType],
        "RouterIntegrationTransitEncryption": NotRequired[FlowTransitEncryptionUnionTypeDef],
    },
)
UpdateFlowSourceRequestTypeDef = TypedDict(
    "UpdateFlowSourceRequestTypeDef",
    {
        "FlowArn": str,
        "SourceArn": str,
        "Decryption": NotRequired[UpdateEncryptionTypeDef],
        "Description": NotRequired[str],
        "EntitlementArn": NotRequired[str],
        "IngestPort": NotRequired[int],
        "MaxBitrate": NotRequired[int],
        "MaxLatency": NotRequired[int],
        "MaxSyncBuffer": NotRequired[int],
        "MediaStreamSourceConfigurations": NotRequired[
            Sequence[MediaStreamSourceConfigurationRequestTypeDef]
        ],
        "MinLatency": NotRequired[int],
        "Protocol": NotRequired[ProtocolType],
        "SenderControlPort": NotRequired[int],
        "SenderIpAddress": NotRequired[str],
        "SourceListenerAddress": NotRequired[str],
        "SourceListenerPort": NotRequired[int],
        "StreamId": NotRequired[str],
        "VpcInterfaceName": NotRequired[str],
        "WhitelistCidr": NotRequired[str],
        "GatewayBridgeSource": NotRequired[UpdateGatewayBridgeSourceRequestTypeDef],
        "RouterIntegrationState": NotRequired[StateType],
        "RouterIntegrationTransitDecryption": NotRequired[FlowTransitEncryptionUnionTypeDef],
    },
)

class RouterInputConfigurationOutputTypeDef(TypedDict):
    Standard: NotRequired[StandardRouterInputConfigurationTypeDef]
    Failover: NotRequired[FailoverRouterInputConfigurationOutputTypeDef]
    Merge: NotRequired[MergeRouterInputConfigurationOutputTypeDef]
    MediaConnectFlow: NotRequired[MediaConnectFlowRouterInputConfigurationOutputTypeDef]

class RouterInputConfigurationTypeDef(TypedDict):
    Standard: NotRequired[StandardRouterInputConfigurationTypeDef]
    Failover: NotRequired[FailoverRouterInputConfigurationTypeDef]
    Merge: NotRequired[MergeRouterInputConfigurationTypeDef]
    MediaConnectFlow: NotRequired[MediaConnectFlowRouterInputConfigurationTypeDef]

class RouterOutputConfigurationOutputTypeDef(TypedDict):
    Standard: NotRequired[StandardRouterOutputConfigurationTypeDef]
    MediaConnectFlow: NotRequired[MediaConnectFlowRouterOutputConfigurationOutputTypeDef]
    MediaLiveInput: NotRequired[MediaLiveInputRouterOutputConfigurationOutputTypeDef]

class RouterOutputConfigurationTypeDef(TypedDict):
    Standard: NotRequired[StandardRouterOutputConfigurationTypeDef]
    MediaConnectFlow: NotRequired[MediaConnectFlowRouterOutputConfigurationTypeDef]
    MediaLiveInput: NotRequired[MediaLiveInputRouterOutputConfigurationTypeDef]

class RouterInputSourceMetadataDetailsTypeDef(TypedDict):
    SourceMetadataMessages: List[RouterInputMessageTypeDef]
    Timestamp: datetime
    RouterInputMetadata: NotRequired[RouterInputMetadataTypeDef]

class AddFlowOutputsRequestTypeDef(TypedDict):
    FlowArn: str
    Outputs: Sequence[AddOutputRequestTypeDef]

class AddFlowSourcesRequestTypeDef(TypedDict):
    FlowArn: str
    Sources: Sequence[SetSourceRequestTypeDef]

class CreateFlowRequestTypeDef(TypedDict):
    Name: str
    AvailabilityZone: NotRequired[str]
    Entitlements: NotRequired[Sequence[GrantEntitlementRequestTypeDef]]
    MediaStreams: NotRequired[Sequence[AddMediaStreamRequestTypeDef]]
    Outputs: NotRequired[Sequence[AddOutputRequestTypeDef]]
    Source: NotRequired[SetSourceRequestTypeDef]
    SourceFailoverConfig: NotRequired[FailoverConfigTypeDef]
    Sources: NotRequired[Sequence[SetSourceRequestTypeDef]]
    VpcInterfaces: NotRequired[Sequence[VpcInterfaceRequestTypeDef]]
    Maintenance: NotRequired[AddMaintenanceTypeDef]
    SourceMonitoringConfig: NotRequired[MonitoringConfigUnionTypeDef]
    FlowSize: NotRequired[FlowSizeType]
    NdiConfig: NotRequired[NdiConfigUnionTypeDef]
    FlowTags: NotRequired[Mapping[str, str]]

RouterInputTypeDef = TypedDict(
    "RouterInputTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Id": str,
        "State": RouterInputStateType,
        "InputType": RouterInputTypeType,
        "Configuration": RouterInputConfigurationOutputTypeDef,
        "RoutedOutputs": int,
        "RegionName": str,
        "AvailabilityZone": str,
        "MaximumBitrate": int,
        "Tier": RouterInputTierType,
        "RoutingScope": RoutingScopeType,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Messages": List[RouterInputMessageTypeDef],
        "TransitEncryption": RouterInputTransitEncryptionOutputTypeDef,
        "Tags": Dict[str, str],
        "StreamDetails": RouterInputStreamDetailsTypeDef,
        "MaintenanceType": MaintenanceTypeType,
        "MaintenanceConfiguration": MaintenanceConfigurationOutputTypeDef,
        "MaximumRoutedOutputs": NotRequired[int],
        "IpAddress": NotRequired[str],
        "MaintenanceScheduleType": NotRequired[Literal["WINDOW"]],
        "MaintenanceSchedule": NotRequired[MaintenanceScheduleTypeDef],
    },
)
RouterInputConfigurationUnionTypeDef = Union[
    RouterInputConfigurationTypeDef, RouterInputConfigurationOutputTypeDef
]
RouterOutputTypeDef = TypedDict(
    "RouterOutputTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Id": str,
        "State": RouterOutputStateType,
        "OutputType": RouterOutputTypeType,
        "Configuration": RouterOutputConfigurationOutputTypeDef,
        "RoutedState": RouterOutputRoutedStateType,
        "RegionName": str,
        "AvailabilityZone": str,
        "MaximumBitrate": int,
        "RoutingScope": RoutingScopeType,
        "Tier": RouterOutputTierType,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Messages": List[RouterOutputMessageTypeDef],
        "Tags": Dict[str, str],
        "StreamDetails": RouterOutputStreamDetailsTypeDef,
        "MaintenanceType": MaintenanceTypeType,
        "MaintenanceConfiguration": MaintenanceConfigurationOutputTypeDef,
        "IpAddress": NotRequired[str],
        "RoutedInputArn": NotRequired[str],
        "MaintenanceScheduleType": NotRequired[Literal["WINDOW"]],
        "MaintenanceSchedule": NotRequired[MaintenanceScheduleTypeDef],
    },
)
RouterOutputConfigurationUnionTypeDef = Union[
    RouterOutputConfigurationTypeDef, RouterOutputConfigurationOutputTypeDef
]

class GetRouterInputSourceMetadataResponseTypeDef(TypedDict):
    Arn: str
    Name: str
    SourceMetadataDetails: RouterInputSourceMetadataDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetRouterInputResponseTypeDef(TypedDict):
    RouterInputs: List[RouterInputTypeDef]
    Errors: List[BatchGetRouterInputErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRouterInputResponseTypeDef(TypedDict):
    RouterInput: RouterInputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRouterInputResponseTypeDef(TypedDict):
    RouterInput: RouterInputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRouterInputResponseTypeDef(TypedDict):
    RouterInput: RouterInputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

CreateRouterInputRequestTypeDef = TypedDict(
    "CreateRouterInputRequestTypeDef",
    {
        "Name": str,
        "Configuration": RouterInputConfigurationUnionTypeDef,
        "MaximumBitrate": int,
        "RoutingScope": RoutingScopeType,
        "Tier": RouterInputTierType,
        "RegionName": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "TransitEncryption": NotRequired[RouterInputTransitEncryptionUnionTypeDef],
        "MaintenanceConfiguration": NotRequired[MaintenanceConfigurationUnionTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
        "ClientToken": NotRequired[str],
    },
)

class UpdateRouterInputRequestTypeDef(TypedDict):
    Arn: str
    Name: NotRequired[str]
    Configuration: NotRequired[RouterInputConfigurationUnionTypeDef]
    MaximumBitrate: NotRequired[int]
    RoutingScope: NotRequired[RoutingScopeType]
    Tier: NotRequired[RouterInputTierType]
    TransitEncryption: NotRequired[RouterInputTransitEncryptionUnionTypeDef]
    MaintenanceConfiguration: NotRequired[MaintenanceConfigurationUnionTypeDef]

class BatchGetRouterOutputResponseTypeDef(TypedDict):
    RouterOutputs: List[RouterOutputTypeDef]
    Errors: List[BatchGetRouterOutputErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRouterOutputResponseTypeDef(TypedDict):
    RouterOutput: RouterOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRouterOutputResponseTypeDef(TypedDict):
    RouterOutput: RouterOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRouterOutputResponseTypeDef(TypedDict):
    RouterOutput: RouterOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

CreateRouterOutputRequestTypeDef = TypedDict(
    "CreateRouterOutputRequestTypeDef",
    {
        "Name": str,
        "Configuration": RouterOutputConfigurationUnionTypeDef,
        "MaximumBitrate": int,
        "RoutingScope": RoutingScopeType,
        "Tier": RouterOutputTierType,
        "RegionName": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "MaintenanceConfiguration": NotRequired[MaintenanceConfigurationUnionTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
        "ClientToken": NotRequired[str],
    },
)

class UpdateRouterOutputRequestTypeDef(TypedDict):
    Arn: str
    Name: NotRequired[str]
    Configuration: NotRequired[RouterOutputConfigurationUnionTypeDef]
    MaximumBitrate: NotRequired[int]
    RoutingScope: NotRequired[RoutingScopeType]
    Tier: NotRequired[RouterOutputTierType]
    MaintenanceConfiguration: NotRequired[MaintenanceConfigurationUnionTypeDef]
