"""
Type annotations for mediaconnect service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mediaconnect.type_defs import AddFlowMediaStreamsRequestRequestTypeDef

    data: AddFlowMediaStreamsRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    AlgorithmType,
    ColorimetryType,
    EncoderProfileType,
    EncodingNameType,
    EntitlementStatusType,
    FailoverModeType,
    KeyTypeType,
    MediaStreamTypeType,
    NetworkInterfaceTypeType,
    ProtocolType,
    RangeType,
    ReservationStateType,
    ScanModeType,
    SourceTypeType,
    StateType,
    StatusType,
    TcsType,
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
    "AddFlowMediaStreamsRequestRequestTypeDef",
    "AddFlowMediaStreamsResponseTypeDef",
    "AddFlowOutputsRequestRequestTypeDef",
    "AddFlowOutputsResponseTypeDef",
    "AddFlowSourcesRequestRequestTypeDef",
    "AddFlowSourcesResponseTypeDef",
    "AddFlowVpcInterfacesRequestRequestTypeDef",
    "AddFlowVpcInterfacesResponseTypeDef",
    "AddMediaStreamRequestTypeDef",
    "AddOutputRequestTypeDef",
    "CreateFlowRequestRequestTypeDef",
    "CreateFlowResponseTypeDef",
    "DeleteFlowRequestRequestTypeDef",
    "DeleteFlowResponseTypeDef",
    "DescribeFlowRequestRequestTypeDef",
    "DescribeFlowResponseTypeDef",
    "DescribeOfferingRequestRequestTypeDef",
    "DescribeOfferingResponseTypeDef",
    "DescribeReservationRequestRequestTypeDef",
    "DescribeReservationResponseTypeDef",
    "DestinationConfigurationRequestTypeDef",
    "DestinationConfigurationTypeDef",
    "EncodingParametersRequestTypeDef",
    "EncodingParametersTypeDef",
    "EncryptionTypeDef",
    "EntitlementTypeDef",
    "FailoverConfigTypeDef",
    "FlowTypeDef",
    "FmtpRequestTypeDef",
    "FmtpTypeDef",
    "GrantEntitlementRequestTypeDef",
    "GrantFlowEntitlementsRequestRequestTypeDef",
    "GrantFlowEntitlementsResponseTypeDef",
    "InputConfigurationRequestTypeDef",
    "InputConfigurationTypeDef",
    "InterfaceRequestTypeDef",
    "InterfaceTypeDef",
    "ListEntitlementsRequestRequestTypeDef",
    "ListEntitlementsResponseTypeDef",
    "ListFlowsRequestRequestTypeDef",
    "ListFlowsResponseTypeDef",
    "ListOfferingsRequestRequestTypeDef",
    "ListOfferingsResponseTypeDef",
    "ListReservationsRequestRequestTypeDef",
    "ListReservationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListedEntitlementTypeDef",
    "ListedFlowTypeDef",
    "MediaStreamAttributesRequestTypeDef",
    "MediaStreamAttributesTypeDef",
    "MediaStreamOutputConfigurationRequestTypeDef",
    "MediaStreamOutputConfigurationTypeDef",
    "MediaStreamSourceConfigurationRequestTypeDef",
    "MediaStreamSourceConfigurationTypeDef",
    "MediaStreamTypeDef",
    "MessagesTypeDef",
    "OfferingTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "PurchaseOfferingRequestRequestTypeDef",
    "PurchaseOfferingResponseTypeDef",
    "RemoveFlowMediaStreamRequestRequestTypeDef",
    "RemoveFlowMediaStreamResponseTypeDef",
    "RemoveFlowOutputRequestRequestTypeDef",
    "RemoveFlowOutputResponseTypeDef",
    "RemoveFlowSourceRequestRequestTypeDef",
    "RemoveFlowSourceResponseTypeDef",
    "RemoveFlowVpcInterfaceRequestRequestTypeDef",
    "RemoveFlowVpcInterfaceResponseTypeDef",
    "ReservationTypeDef",
    "ResourceSpecificationTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeFlowEntitlementRequestRequestTypeDef",
    "RevokeFlowEntitlementResponseTypeDef",
    "SetSourceRequestTypeDef",
    "SourcePriorityTypeDef",
    "SourceTypeDef",
    "StartFlowRequestRequestTypeDef",
    "StartFlowResponseTypeDef",
    "StopFlowRequestRequestTypeDef",
    "StopFlowResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TransportTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateEncryptionTypeDef",
    "UpdateFailoverConfigTypeDef",
    "UpdateFlowEntitlementRequestRequestTypeDef",
    "UpdateFlowEntitlementResponseTypeDef",
    "UpdateFlowMediaStreamRequestRequestTypeDef",
    "UpdateFlowMediaStreamResponseTypeDef",
    "UpdateFlowOutputRequestRequestTypeDef",
    "UpdateFlowOutputResponseTypeDef",
    "UpdateFlowRequestRequestTypeDef",
    "UpdateFlowResponseTypeDef",
    "UpdateFlowSourceRequestRequestTypeDef",
    "UpdateFlowSourceResponseTypeDef",
    "VpcInterfaceAttachmentTypeDef",
    "VpcInterfaceRequestTypeDef",
    "VpcInterfaceTypeDef",
    "WaiterConfigTypeDef",
)

AddFlowMediaStreamsRequestRequestTypeDef = TypedDict(
    "AddFlowMediaStreamsRequestRequestTypeDef",
    {
        "FlowArn": str,
        "MediaStreams": List["AddMediaStreamRequestTypeDef"],
    },
)

AddFlowMediaStreamsResponseTypeDef = TypedDict(
    "AddFlowMediaStreamsResponseTypeDef",
    {
        "FlowArn": str,
        "MediaStreams": List["MediaStreamTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddFlowOutputsRequestRequestTypeDef = TypedDict(
    "AddFlowOutputsRequestRequestTypeDef",
    {
        "FlowArn": str,
        "Outputs": List["AddOutputRequestTypeDef"],
    },
)

AddFlowOutputsResponseTypeDef = TypedDict(
    "AddFlowOutputsResponseTypeDef",
    {
        "FlowArn": str,
        "Outputs": List["OutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddFlowSourcesRequestRequestTypeDef = TypedDict(
    "AddFlowSourcesRequestRequestTypeDef",
    {
        "FlowArn": str,
        "Sources": List["SetSourceRequestTypeDef"],
    },
)

AddFlowSourcesResponseTypeDef = TypedDict(
    "AddFlowSourcesResponseTypeDef",
    {
        "FlowArn": str,
        "Sources": List["SourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddFlowVpcInterfacesRequestRequestTypeDef = TypedDict(
    "AddFlowVpcInterfacesRequestRequestTypeDef",
    {
        "FlowArn": str,
        "VpcInterfaces": List["VpcInterfaceRequestTypeDef"],
    },
)

AddFlowVpcInterfacesResponseTypeDef = TypedDict(
    "AddFlowVpcInterfacesResponseTypeDef",
    {
        "FlowArn": str,
        "VpcInterfaces": List["VpcInterfaceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAddMediaStreamRequestTypeDef = TypedDict(
    "_RequiredAddMediaStreamRequestTypeDef",
    {
        "MediaStreamId": int,
        "MediaStreamName": str,
        "MediaStreamType": MediaStreamTypeType,
    },
)
_OptionalAddMediaStreamRequestTypeDef = TypedDict(
    "_OptionalAddMediaStreamRequestTypeDef",
    {
        "Attributes": "MediaStreamAttributesRequestTypeDef",
        "ClockRate": int,
        "Description": str,
        "VideoFormat": str,
    },
    total=False,
)

class AddMediaStreamRequestTypeDef(
    _RequiredAddMediaStreamRequestTypeDef, _OptionalAddMediaStreamRequestTypeDef
):
    pass

_RequiredAddOutputRequestTypeDef = TypedDict(
    "_RequiredAddOutputRequestTypeDef",
    {
        "Protocol": ProtocolType,
    },
)
_OptionalAddOutputRequestTypeDef = TypedDict(
    "_OptionalAddOutputRequestTypeDef",
    {
        "CidrAllowList": List[str],
        "Description": str,
        "Destination": str,
        "Encryption": "EncryptionTypeDef",
        "MaxLatency": int,
        "MediaStreamOutputConfigurations": List["MediaStreamOutputConfigurationRequestTypeDef"],
        "MinLatency": int,
        "Name": str,
        "Port": int,
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
        "VpcInterfaceAttachment": "VpcInterfaceAttachmentTypeDef",
    },
    total=False,
)

class AddOutputRequestTypeDef(_RequiredAddOutputRequestTypeDef, _OptionalAddOutputRequestTypeDef):
    pass

_RequiredCreateFlowRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFlowRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateFlowRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFlowRequestRequestTypeDef",
    {
        "AvailabilityZone": str,
        "Entitlements": List["GrantEntitlementRequestTypeDef"],
        "MediaStreams": List["AddMediaStreamRequestTypeDef"],
        "Outputs": List["AddOutputRequestTypeDef"],
        "Source": "SetSourceRequestTypeDef",
        "SourceFailoverConfig": "FailoverConfigTypeDef",
        "Sources": List["SetSourceRequestTypeDef"],
        "VpcInterfaces": List["VpcInterfaceRequestTypeDef"],
    },
    total=False,
)

class CreateFlowRequestRequestTypeDef(
    _RequiredCreateFlowRequestRequestTypeDef, _OptionalCreateFlowRequestRequestTypeDef
):
    pass

CreateFlowResponseTypeDef = TypedDict(
    "CreateFlowResponseTypeDef",
    {
        "Flow": "FlowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFlowRequestRequestTypeDef = TypedDict(
    "DeleteFlowRequestRequestTypeDef",
    {
        "FlowArn": str,
    },
)

DeleteFlowResponseTypeDef = TypedDict(
    "DeleteFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFlowRequestRequestTypeDef = TypedDict(
    "DescribeFlowRequestRequestTypeDef",
    {
        "FlowArn": str,
    },
)

DescribeFlowResponseTypeDef = TypedDict(
    "DescribeFlowResponseTypeDef",
    {
        "Flow": "FlowTypeDef",
        "Messages": "MessagesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOfferingRequestRequestTypeDef = TypedDict(
    "DescribeOfferingRequestRequestTypeDef",
    {
        "OfferingArn": str,
    },
)

DescribeOfferingResponseTypeDef = TypedDict(
    "DescribeOfferingResponseTypeDef",
    {
        "Offering": "OfferingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservationRequestRequestTypeDef = TypedDict(
    "DescribeReservationRequestRequestTypeDef",
    {
        "ReservationArn": str,
    },
)

DescribeReservationResponseTypeDef = TypedDict(
    "DescribeReservationResponseTypeDef",
    {
        "Reservation": "ReservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationConfigurationRequestTypeDef = TypedDict(
    "DestinationConfigurationRequestTypeDef",
    {
        "DestinationIp": str,
        "DestinationPort": int,
        "Interface": "InterfaceRequestTypeDef",
    },
)

DestinationConfigurationTypeDef = TypedDict(
    "DestinationConfigurationTypeDef",
    {
        "DestinationIp": str,
        "DestinationPort": int,
        "Interface": "InterfaceTypeDef",
        "OutboundIp": str,
    },
)

EncodingParametersRequestTypeDef = TypedDict(
    "EncodingParametersRequestTypeDef",
    {
        "CompressionFactor": float,
        "EncoderProfile": EncoderProfileType,
    },
)

EncodingParametersTypeDef = TypedDict(
    "EncodingParametersTypeDef",
    {
        "CompressionFactor": float,
        "EncoderProfile": EncoderProfileType,
    },
)

_RequiredEncryptionTypeDef = TypedDict(
    "_RequiredEncryptionTypeDef",
    {
        "RoleArn": str,
    },
)
_OptionalEncryptionTypeDef = TypedDict(
    "_OptionalEncryptionTypeDef",
    {
        "Algorithm": AlgorithmType,
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": KeyTypeType,
        "Region": str,
        "ResourceId": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)

class EncryptionTypeDef(_RequiredEncryptionTypeDef, _OptionalEncryptionTypeDef):
    pass

_RequiredEntitlementTypeDef = TypedDict(
    "_RequiredEntitlementTypeDef",
    {
        "EntitlementArn": str,
        "Name": str,
        "Subscribers": List[str],
    },
)
_OptionalEntitlementTypeDef = TypedDict(
    "_OptionalEntitlementTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": "EncryptionTypeDef",
        "EntitlementStatus": EntitlementStatusType,
    },
    total=False,
)

class EntitlementTypeDef(_RequiredEntitlementTypeDef, _OptionalEntitlementTypeDef):
    pass

FailoverConfigTypeDef = TypedDict(
    "FailoverConfigTypeDef",
    {
        "FailoverMode": FailoverModeType,
        "RecoveryWindow": int,
        "SourcePriority": "SourcePriorityTypeDef",
        "State": StateType,
    },
    total=False,
)

_RequiredFlowTypeDef = TypedDict(
    "_RequiredFlowTypeDef",
    {
        "AvailabilityZone": str,
        "Entitlements": List["EntitlementTypeDef"],
        "FlowArn": str,
        "Name": str,
        "Outputs": List["OutputTypeDef"],
        "Source": "SourceTypeDef",
        "Status": StatusType,
    },
)
_OptionalFlowTypeDef = TypedDict(
    "_OptionalFlowTypeDef",
    {
        "Description": str,
        "EgressIp": str,
        "MediaStreams": List["MediaStreamTypeDef"],
        "SourceFailoverConfig": "FailoverConfigTypeDef",
        "Sources": List["SourceTypeDef"],
        "VpcInterfaces": List["VpcInterfaceTypeDef"],
    },
    total=False,
)

class FlowTypeDef(_RequiredFlowTypeDef, _OptionalFlowTypeDef):
    pass

FmtpRequestTypeDef = TypedDict(
    "FmtpRequestTypeDef",
    {
        "ChannelOrder": str,
        "Colorimetry": ColorimetryType,
        "ExactFramerate": str,
        "Par": str,
        "Range": RangeType,
        "ScanMode": ScanModeType,
        "Tcs": TcsType,
    },
    total=False,
)

FmtpTypeDef = TypedDict(
    "FmtpTypeDef",
    {
        "ChannelOrder": str,
        "Colorimetry": ColorimetryType,
        "ExactFramerate": str,
        "Par": str,
        "Range": RangeType,
        "ScanMode": ScanModeType,
        "Tcs": TcsType,
    },
    total=False,
)

_RequiredGrantEntitlementRequestTypeDef = TypedDict(
    "_RequiredGrantEntitlementRequestTypeDef",
    {
        "Subscribers": List[str],
    },
)
_OptionalGrantEntitlementRequestTypeDef = TypedDict(
    "_OptionalGrantEntitlementRequestTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": "EncryptionTypeDef",
        "EntitlementStatus": EntitlementStatusType,
        "Name": str,
    },
    total=False,
)

class GrantEntitlementRequestTypeDef(
    _RequiredGrantEntitlementRequestTypeDef, _OptionalGrantEntitlementRequestTypeDef
):
    pass

GrantFlowEntitlementsRequestRequestTypeDef = TypedDict(
    "GrantFlowEntitlementsRequestRequestTypeDef",
    {
        "Entitlements": List["GrantEntitlementRequestTypeDef"],
        "FlowArn": str,
    },
)

GrantFlowEntitlementsResponseTypeDef = TypedDict(
    "GrantFlowEntitlementsResponseTypeDef",
    {
        "Entitlements": List["EntitlementTypeDef"],
        "FlowArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputConfigurationRequestTypeDef = TypedDict(
    "InputConfigurationRequestTypeDef",
    {
        "InputPort": int,
        "Interface": "InterfaceRequestTypeDef",
    },
)

InputConfigurationTypeDef = TypedDict(
    "InputConfigurationTypeDef",
    {
        "InputIp": str,
        "InputPort": int,
        "Interface": "InterfaceTypeDef",
    },
)

InterfaceRequestTypeDef = TypedDict(
    "InterfaceRequestTypeDef",
    {
        "Name": str,
    },
)

InterfaceTypeDef = TypedDict(
    "InterfaceTypeDef",
    {
        "Name": str,
    },
)

ListEntitlementsRequestRequestTypeDef = TypedDict(
    "ListEntitlementsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListEntitlementsResponseTypeDef = TypedDict(
    "ListEntitlementsResponseTypeDef",
    {
        "Entitlements": List["ListedEntitlementTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFlowsRequestRequestTypeDef = TypedDict(
    "ListFlowsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListFlowsResponseTypeDef = TypedDict(
    "ListFlowsResponseTypeDef",
    {
        "Flows": List["ListedFlowTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOfferingsRequestRequestTypeDef = TypedDict(
    "ListOfferingsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListOfferingsResponseTypeDef = TypedDict(
    "ListOfferingsResponseTypeDef",
    {
        "NextToken": str,
        "Offerings": List["OfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReservationsRequestRequestTypeDef = TypedDict(
    "ListReservationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListReservationsResponseTypeDef = TypedDict(
    "ListReservationsResponseTypeDef",
    {
        "NextToken": str,
        "Reservations": List["ReservationTypeDef"],
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

_RequiredListedEntitlementTypeDef = TypedDict(
    "_RequiredListedEntitlementTypeDef",
    {
        "EntitlementArn": str,
        "EntitlementName": str,
    },
)
_OptionalListedEntitlementTypeDef = TypedDict(
    "_OptionalListedEntitlementTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
    },
    total=False,
)

class ListedEntitlementTypeDef(
    _RequiredListedEntitlementTypeDef, _OptionalListedEntitlementTypeDef
):
    pass

ListedFlowTypeDef = TypedDict(
    "ListedFlowTypeDef",
    {
        "AvailabilityZone": str,
        "Description": str,
        "FlowArn": str,
        "Name": str,
        "SourceType": SourceTypeType,
        "Status": StatusType,
    },
)

MediaStreamAttributesRequestTypeDef = TypedDict(
    "MediaStreamAttributesRequestTypeDef",
    {
        "Fmtp": "FmtpRequestTypeDef",
        "Lang": str,
    },
    total=False,
)

_RequiredMediaStreamAttributesTypeDef = TypedDict(
    "_RequiredMediaStreamAttributesTypeDef",
    {
        "Fmtp": "FmtpTypeDef",
    },
)
_OptionalMediaStreamAttributesTypeDef = TypedDict(
    "_OptionalMediaStreamAttributesTypeDef",
    {
        "Lang": str,
    },
    total=False,
)

class MediaStreamAttributesTypeDef(
    _RequiredMediaStreamAttributesTypeDef, _OptionalMediaStreamAttributesTypeDef
):
    pass

_RequiredMediaStreamOutputConfigurationRequestTypeDef = TypedDict(
    "_RequiredMediaStreamOutputConfigurationRequestTypeDef",
    {
        "EncodingName": EncodingNameType,
        "MediaStreamName": str,
    },
)
_OptionalMediaStreamOutputConfigurationRequestTypeDef = TypedDict(
    "_OptionalMediaStreamOutputConfigurationRequestTypeDef",
    {
        "DestinationConfigurations": List["DestinationConfigurationRequestTypeDef"],
        "EncodingParameters": "EncodingParametersRequestTypeDef",
    },
    total=False,
)

class MediaStreamOutputConfigurationRequestTypeDef(
    _RequiredMediaStreamOutputConfigurationRequestTypeDef,
    _OptionalMediaStreamOutputConfigurationRequestTypeDef,
):
    pass

_RequiredMediaStreamOutputConfigurationTypeDef = TypedDict(
    "_RequiredMediaStreamOutputConfigurationTypeDef",
    {
        "EncodingName": EncodingNameType,
        "MediaStreamName": str,
    },
)
_OptionalMediaStreamOutputConfigurationTypeDef = TypedDict(
    "_OptionalMediaStreamOutputConfigurationTypeDef",
    {
        "DestinationConfigurations": List["DestinationConfigurationTypeDef"],
        "EncodingParameters": "EncodingParametersTypeDef",
    },
    total=False,
)

class MediaStreamOutputConfigurationTypeDef(
    _RequiredMediaStreamOutputConfigurationTypeDef, _OptionalMediaStreamOutputConfigurationTypeDef
):
    pass

_RequiredMediaStreamSourceConfigurationRequestTypeDef = TypedDict(
    "_RequiredMediaStreamSourceConfigurationRequestTypeDef",
    {
        "EncodingName": EncodingNameType,
        "MediaStreamName": str,
    },
)
_OptionalMediaStreamSourceConfigurationRequestTypeDef = TypedDict(
    "_OptionalMediaStreamSourceConfigurationRequestTypeDef",
    {
        "InputConfigurations": List["InputConfigurationRequestTypeDef"],
    },
    total=False,
)

class MediaStreamSourceConfigurationRequestTypeDef(
    _RequiredMediaStreamSourceConfigurationRequestTypeDef,
    _OptionalMediaStreamSourceConfigurationRequestTypeDef,
):
    pass

_RequiredMediaStreamSourceConfigurationTypeDef = TypedDict(
    "_RequiredMediaStreamSourceConfigurationTypeDef",
    {
        "EncodingName": EncodingNameType,
        "MediaStreamName": str,
    },
)
_OptionalMediaStreamSourceConfigurationTypeDef = TypedDict(
    "_OptionalMediaStreamSourceConfigurationTypeDef",
    {
        "InputConfigurations": List["InputConfigurationTypeDef"],
    },
    total=False,
)

class MediaStreamSourceConfigurationTypeDef(
    _RequiredMediaStreamSourceConfigurationTypeDef, _OptionalMediaStreamSourceConfigurationTypeDef
):
    pass

_RequiredMediaStreamTypeDef = TypedDict(
    "_RequiredMediaStreamTypeDef",
    {
        "Fmt": int,
        "MediaStreamId": int,
        "MediaStreamName": str,
        "MediaStreamType": MediaStreamTypeType,
    },
)
_OptionalMediaStreamTypeDef = TypedDict(
    "_OptionalMediaStreamTypeDef",
    {
        "Attributes": "MediaStreamAttributesTypeDef",
        "ClockRate": int,
        "Description": str,
        "VideoFormat": str,
    },
    total=False,
)

class MediaStreamTypeDef(_RequiredMediaStreamTypeDef, _OptionalMediaStreamTypeDef):
    pass

MessagesTypeDef = TypedDict(
    "MessagesTypeDef",
    {
        "Errors": List[str],
    },
)

OfferingTypeDef = TypedDict(
    "OfferingTypeDef",
    {
        "CurrencyCode": str,
        "Duration": int,
        "DurationUnits": Literal["MONTHS"],
        "OfferingArn": str,
        "OfferingDescription": str,
        "PricePerUnit": str,
        "PriceUnits": Literal["HOURLY"],
        "ResourceSpecification": "ResourceSpecificationTypeDef",
    },
)

_RequiredOutputTypeDef = TypedDict(
    "_RequiredOutputTypeDef",
    {
        "Name": str,
        "OutputArn": str,
    },
)
_OptionalOutputTypeDef = TypedDict(
    "_OptionalOutputTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Destination": str,
        "Encryption": "EncryptionTypeDef",
        "EntitlementArn": str,
        "ListenerAddress": str,
        "MediaLiveInputArn": str,
        "MediaStreamOutputConfigurations": List["MediaStreamOutputConfigurationTypeDef"],
        "Port": int,
        "Transport": "TransportTypeDef",
        "VpcInterfaceAttachment": "VpcInterfaceAttachmentTypeDef",
    },
    total=False,
)

class OutputTypeDef(_RequiredOutputTypeDef, _OptionalOutputTypeDef):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PurchaseOfferingRequestRequestTypeDef = TypedDict(
    "PurchaseOfferingRequestRequestTypeDef",
    {
        "OfferingArn": str,
        "ReservationName": str,
        "Start": str,
    },
)

PurchaseOfferingResponseTypeDef = TypedDict(
    "PurchaseOfferingResponseTypeDef",
    {
        "Reservation": "ReservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFlowMediaStreamRequestRequestTypeDef = TypedDict(
    "RemoveFlowMediaStreamRequestRequestTypeDef",
    {
        "FlowArn": str,
        "MediaStreamName": str,
    },
)

RemoveFlowMediaStreamResponseTypeDef = TypedDict(
    "RemoveFlowMediaStreamResponseTypeDef",
    {
        "FlowArn": str,
        "MediaStreamName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFlowOutputRequestRequestTypeDef = TypedDict(
    "RemoveFlowOutputRequestRequestTypeDef",
    {
        "FlowArn": str,
        "OutputArn": str,
    },
)

RemoveFlowOutputResponseTypeDef = TypedDict(
    "RemoveFlowOutputResponseTypeDef",
    {
        "FlowArn": str,
        "OutputArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFlowSourceRequestRequestTypeDef = TypedDict(
    "RemoveFlowSourceRequestRequestTypeDef",
    {
        "FlowArn": str,
        "SourceArn": str,
    },
)

RemoveFlowSourceResponseTypeDef = TypedDict(
    "RemoveFlowSourceResponseTypeDef",
    {
        "FlowArn": str,
        "SourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFlowVpcInterfaceRequestRequestTypeDef = TypedDict(
    "RemoveFlowVpcInterfaceRequestRequestTypeDef",
    {
        "FlowArn": str,
        "VpcInterfaceName": str,
    },
)

RemoveFlowVpcInterfaceResponseTypeDef = TypedDict(
    "RemoveFlowVpcInterfaceResponseTypeDef",
    {
        "FlowArn": str,
        "NonDeletedNetworkInterfaceIds": List[str],
        "VpcInterfaceName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReservationTypeDef = TypedDict(
    "ReservationTypeDef",
    {
        "CurrencyCode": str,
        "Duration": int,
        "DurationUnits": Literal["MONTHS"],
        "End": str,
        "OfferingArn": str,
        "OfferingDescription": str,
        "PricePerUnit": str,
        "PriceUnits": Literal["HOURLY"],
        "ReservationArn": str,
        "ReservationName": str,
        "ReservationState": ReservationStateType,
        "ResourceSpecification": "ResourceSpecificationTypeDef",
        "Start": str,
    },
)

_RequiredResourceSpecificationTypeDef = TypedDict(
    "_RequiredResourceSpecificationTypeDef",
    {
        "ResourceType": Literal["Mbps_Outbound_Bandwidth"],
    },
)
_OptionalResourceSpecificationTypeDef = TypedDict(
    "_OptionalResourceSpecificationTypeDef",
    {
        "ReservedBitrate": int,
    },
    total=False,
)

class ResourceSpecificationTypeDef(
    _RequiredResourceSpecificationTypeDef, _OptionalResourceSpecificationTypeDef
):
    pass

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

RevokeFlowEntitlementRequestRequestTypeDef = TypedDict(
    "RevokeFlowEntitlementRequestRequestTypeDef",
    {
        "EntitlementArn": str,
        "FlowArn": str,
    },
)

RevokeFlowEntitlementResponseTypeDef = TypedDict(
    "RevokeFlowEntitlementResponseTypeDef",
    {
        "EntitlementArn": str,
        "FlowArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetSourceRequestTypeDef = TypedDict(
    "SetSourceRequestTypeDef",
    {
        "Decryption": "EncryptionTypeDef",
        "Description": str,
        "EntitlementArn": str,
        "IngestPort": int,
        "MaxBitrate": int,
        "MaxLatency": int,
        "MaxSyncBuffer": int,
        "MediaStreamSourceConfigurations": List["MediaStreamSourceConfigurationRequestTypeDef"],
        "MinLatency": int,
        "Name": str,
        "Protocol": ProtocolType,
        "StreamId": str,
        "VpcInterfaceName": str,
        "WhitelistCidr": str,
    },
    total=False,
)

SourcePriorityTypeDef = TypedDict(
    "SourcePriorityTypeDef",
    {
        "PrimarySource": str,
    },
    total=False,
)

_RequiredSourceTypeDef = TypedDict(
    "_RequiredSourceTypeDef",
    {
        "Name": str,
        "SourceArn": str,
    },
)
_OptionalSourceTypeDef = TypedDict(
    "_OptionalSourceTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Decryption": "EncryptionTypeDef",
        "Description": str,
        "EntitlementArn": str,
        "IngestIp": str,
        "IngestPort": int,
        "MediaStreamSourceConfigurations": List["MediaStreamSourceConfigurationTypeDef"],
        "Transport": "TransportTypeDef",
        "VpcInterfaceName": str,
        "WhitelistCidr": str,
    },
    total=False,
)

class SourceTypeDef(_RequiredSourceTypeDef, _OptionalSourceTypeDef):
    pass

StartFlowRequestRequestTypeDef = TypedDict(
    "StartFlowRequestRequestTypeDef",
    {
        "FlowArn": str,
    },
)

StartFlowResponseTypeDef = TypedDict(
    "StartFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopFlowRequestRequestTypeDef = TypedDict(
    "StopFlowRequestRequestTypeDef",
    {
        "FlowArn": str,
    },
)

StopFlowResponseTypeDef = TypedDict(
    "StopFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

_RequiredTransportTypeDef = TypedDict(
    "_RequiredTransportTypeDef",
    {
        "Protocol": ProtocolType,
    },
)
_OptionalTransportTypeDef = TypedDict(
    "_OptionalTransportTypeDef",
    {
        "CidrAllowList": List[str],
        "MaxBitrate": int,
        "MaxLatency": int,
        "MaxSyncBuffer": int,
        "MinLatency": int,
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)

class TransportTypeDef(_RequiredTransportTypeDef, _OptionalTransportTypeDef):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateEncryptionTypeDef = TypedDict(
    "UpdateEncryptionTypeDef",
    {
        "Algorithm": AlgorithmType,
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": KeyTypeType,
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)

UpdateFailoverConfigTypeDef = TypedDict(
    "UpdateFailoverConfigTypeDef",
    {
        "FailoverMode": FailoverModeType,
        "RecoveryWindow": int,
        "SourcePriority": "SourcePriorityTypeDef",
        "State": StateType,
    },
    total=False,
)

_RequiredUpdateFlowEntitlementRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFlowEntitlementRequestRequestTypeDef",
    {
        "EntitlementArn": str,
        "FlowArn": str,
    },
)
_OptionalUpdateFlowEntitlementRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFlowEntitlementRequestRequestTypeDef",
    {
        "Description": str,
        "Encryption": "UpdateEncryptionTypeDef",
        "EntitlementStatus": EntitlementStatusType,
        "Subscribers": List[str],
    },
    total=False,
)

class UpdateFlowEntitlementRequestRequestTypeDef(
    _RequiredUpdateFlowEntitlementRequestRequestTypeDef,
    _OptionalUpdateFlowEntitlementRequestRequestTypeDef,
):
    pass

UpdateFlowEntitlementResponseTypeDef = TypedDict(
    "UpdateFlowEntitlementResponseTypeDef",
    {
        "Entitlement": "EntitlementTypeDef",
        "FlowArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFlowMediaStreamRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFlowMediaStreamRequestRequestTypeDef",
    {
        "FlowArn": str,
        "MediaStreamName": str,
    },
)
_OptionalUpdateFlowMediaStreamRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFlowMediaStreamRequestRequestTypeDef",
    {
        "Attributes": "MediaStreamAttributesRequestTypeDef",
        "ClockRate": int,
        "Description": str,
        "MediaStreamType": MediaStreamTypeType,
        "VideoFormat": str,
    },
    total=False,
)

class UpdateFlowMediaStreamRequestRequestTypeDef(
    _RequiredUpdateFlowMediaStreamRequestRequestTypeDef,
    _OptionalUpdateFlowMediaStreamRequestRequestTypeDef,
):
    pass

UpdateFlowMediaStreamResponseTypeDef = TypedDict(
    "UpdateFlowMediaStreamResponseTypeDef",
    {
        "FlowArn": str,
        "MediaStream": "MediaStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFlowOutputRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFlowOutputRequestRequestTypeDef",
    {
        "FlowArn": str,
        "OutputArn": str,
    },
)
_OptionalUpdateFlowOutputRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFlowOutputRequestRequestTypeDef",
    {
        "CidrAllowList": List[str],
        "Description": str,
        "Destination": str,
        "Encryption": "UpdateEncryptionTypeDef",
        "MaxLatency": int,
        "MediaStreamOutputConfigurations": List["MediaStreamOutputConfigurationRequestTypeDef"],
        "MinLatency": int,
        "Port": int,
        "Protocol": ProtocolType,
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
        "VpcInterfaceAttachment": "VpcInterfaceAttachmentTypeDef",
    },
    total=False,
)

class UpdateFlowOutputRequestRequestTypeDef(
    _RequiredUpdateFlowOutputRequestRequestTypeDef, _OptionalUpdateFlowOutputRequestRequestTypeDef
):
    pass

UpdateFlowOutputResponseTypeDef = TypedDict(
    "UpdateFlowOutputResponseTypeDef",
    {
        "FlowArn": str,
        "Output": "OutputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFlowRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFlowRequestRequestTypeDef",
    {
        "FlowArn": str,
    },
)
_OptionalUpdateFlowRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFlowRequestRequestTypeDef",
    {
        "SourceFailoverConfig": "UpdateFailoverConfigTypeDef",
    },
    total=False,
)

class UpdateFlowRequestRequestTypeDef(
    _RequiredUpdateFlowRequestRequestTypeDef, _OptionalUpdateFlowRequestRequestTypeDef
):
    pass

UpdateFlowResponseTypeDef = TypedDict(
    "UpdateFlowResponseTypeDef",
    {
        "Flow": "FlowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFlowSourceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFlowSourceRequestRequestTypeDef",
    {
        "FlowArn": str,
        "SourceArn": str,
    },
)
_OptionalUpdateFlowSourceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFlowSourceRequestRequestTypeDef",
    {
        "Decryption": "UpdateEncryptionTypeDef",
        "Description": str,
        "EntitlementArn": str,
        "IngestPort": int,
        "MaxBitrate": int,
        "MaxLatency": int,
        "MaxSyncBuffer": int,
        "MediaStreamSourceConfigurations": List["MediaStreamSourceConfigurationRequestTypeDef"],
        "MinLatency": int,
        "Protocol": ProtocolType,
        "StreamId": str,
        "VpcInterfaceName": str,
        "WhitelistCidr": str,
    },
    total=False,
)

class UpdateFlowSourceRequestRequestTypeDef(
    _RequiredUpdateFlowSourceRequestRequestTypeDef, _OptionalUpdateFlowSourceRequestRequestTypeDef
):
    pass

UpdateFlowSourceResponseTypeDef = TypedDict(
    "UpdateFlowSourceResponseTypeDef",
    {
        "FlowArn": str,
        "Source": "SourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcInterfaceAttachmentTypeDef = TypedDict(
    "VpcInterfaceAttachmentTypeDef",
    {
        "VpcInterfaceName": str,
    },
    total=False,
)

_RequiredVpcInterfaceRequestTypeDef = TypedDict(
    "_RequiredVpcInterfaceRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
    },
)
_OptionalVpcInterfaceRequestTypeDef = TypedDict(
    "_OptionalVpcInterfaceRequestTypeDef",
    {
        "NetworkInterfaceType": NetworkInterfaceTypeType,
    },
    total=False,
)

class VpcInterfaceRequestTypeDef(
    _RequiredVpcInterfaceRequestTypeDef, _OptionalVpcInterfaceRequestTypeDef
):
    pass

VpcInterfaceTypeDef = TypedDict(
    "VpcInterfaceTypeDef",
    {
        "Name": str,
        "NetworkInterfaceIds": List[str],
        "NetworkInterfaceType": NetworkInterfaceTypeType,
        "RoleArn": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
