"""
Main interface for mediaconnect service type definitions.

Usage::

    ```python
    from mypy_boto3_mediaconnect.type_defs import EncryptionTypeDef

    data: EncryptionTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "EncryptionTypeDef",
    "EntitlementTypeDef",
    "FailoverConfigTypeDef",
    "FlowTypeDef",
    "ListedEntitlementTypeDef",
    "ListedFlowTypeDef",
    "MessagesTypeDef",
    "OfferingTypeDef",
    "OutputTypeDef",
    "ReservationTypeDef",
    "ResourceSpecificationTypeDef",
    "ResponseMetadata",
    "SourceTypeDef",
    "TransportTypeDef",
    "VpcInterfaceAttachmentTypeDef",
    "VpcInterfaceTypeDef",
    "AddFlowOutputsResponseTypeDef",
    "AddFlowSourcesResponseTypeDef",
    "AddFlowVpcInterfacesResponseTypeDef",
    "AddOutputRequestTypeDef",
    "CreateFlowResponseTypeDef",
    "DeleteFlowResponseTypeDef",
    "DescribeFlowResponseTypeDef",
    "DescribeOfferingResponseTypeDef",
    "DescribeReservationResponseTypeDef",
    "GrantEntitlementRequestTypeDef",
    "GrantFlowEntitlementsResponseTypeDef",
    "ListEntitlementsResponseTypeDef",
    "ListFlowsResponseTypeDef",
    "ListOfferingsResponseTypeDef",
    "ListReservationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PurchaseOfferingResponseTypeDef",
    "RemoveFlowOutputResponseTypeDef",
    "RemoveFlowSourceResponseTypeDef",
    "RemoveFlowVpcInterfaceResponseTypeDef",
    "RevokeFlowEntitlementResponseTypeDef",
    "SetSourceRequestTypeDef",
    "StartFlowResponseTypeDef",
    "StopFlowResponseTypeDef",
    "UpdateEncryptionTypeDef",
    "UpdateFailoverConfigTypeDef",
    "UpdateFlowEntitlementResponseTypeDef",
    "UpdateFlowOutputResponseTypeDef",
    "UpdateFlowResponseTypeDef",
    "UpdateFlowSourceResponseTypeDef",
    "VpcInterfaceRequestTypeDef",
)

_RequiredEncryptionTypeDef = TypedDict(
    "_RequiredEncryptionTypeDef",
    {"Algorithm": Literal["aes128", "aes192", "aes256"], "RoleArn": str},
)
_OptionalEncryptionTypeDef = TypedDict(
    "_OptionalEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
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
    "_RequiredEntitlementTypeDef", {"EntitlementArn": str, "Name": str, "Subscribers": List[str]}
)
_OptionalEntitlementTypeDef = TypedDict(
    "_OptionalEntitlementTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": "EncryptionTypeDef",
        "EntitlementStatus": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)


class EntitlementTypeDef(_RequiredEntitlementTypeDef, _OptionalEntitlementTypeDef):
    pass


FailoverConfigTypeDef = TypedDict(
    "FailoverConfigTypeDef",
    {"RecoveryWindow": int, "State": Literal["ENABLED", "DISABLED"]},
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
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
)
_OptionalFlowTypeDef = TypedDict(
    "_OptionalFlowTypeDef",
    {
        "Description": str,
        "EgressIp": str,
        "SourceFailoverConfig": "FailoverConfigTypeDef",
        "Sources": List["SourceTypeDef"],
        "VpcInterfaces": List["VpcInterfaceTypeDef"],
    },
    total=False,
)


class FlowTypeDef(_RequiredFlowTypeDef, _OptionalFlowTypeDef):
    pass


_RequiredListedEntitlementTypeDef = TypedDict(
    "_RequiredListedEntitlementTypeDef", {"EntitlementArn": str, "EntitlementName": str}
)
_OptionalListedEntitlementTypeDef = TypedDict(
    "_OptionalListedEntitlementTypeDef", {"DataTransferSubscriberFeePercent": int}, total=False
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
        "SourceType": Literal["OWNED", "ENTITLED"],
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
)

MessagesTypeDef = TypedDict("MessagesTypeDef", {"Errors": List[str]})

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

_RequiredOutputTypeDef = TypedDict("_RequiredOutputTypeDef", {"Name": str, "OutputArn": str})
_OptionalOutputTypeDef = TypedDict(
    "_OptionalOutputTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Destination": str,
        "Encryption": "EncryptionTypeDef",
        "EntitlementArn": str,
        "MediaLiveInputArn": str,
        "Port": int,
        "Transport": "TransportTypeDef",
        "VpcInterfaceAttachment": "VpcInterfaceAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)


class OutputTypeDef(_RequiredOutputTypeDef, _OptionalOutputTypeDef):
    pass


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
        "ReservationState": Literal["ACTIVE", "EXPIRED", "PROCESSING", "CANCELED"],
        "ResourceSpecification": "ResourceSpecificationTypeDef",
        "Start": str,
    },
)

_RequiredResourceSpecificationTypeDef = TypedDict(
    "_RequiredResourceSpecificationTypeDef", {"ResourceType": Literal["Mbps_Outbound_Bandwidth"]}
)
_OptionalResourceSpecificationTypeDef = TypedDict(
    "_OptionalResourceSpecificationTypeDef", {"ReservedBitrate": int}, total=False
)


class ResourceSpecificationTypeDef(
    _RequiredResourceSpecificationTypeDef, _OptionalResourceSpecificationTypeDef
):
    pass


ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredSourceTypeDef = TypedDict("_RequiredSourceTypeDef", {"Name": str, "SourceArn": str})
_OptionalSourceTypeDef = TypedDict(
    "_OptionalSourceTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Decryption": "EncryptionTypeDef",
        "Description": str,
        "EntitlementArn": str,
        "IngestIp": str,
        "IngestPort": int,
        "Transport": "TransportTypeDef",
        "VpcInterfaceName": str,
        "WhitelistCidr": str,
    },
    total=False,
)


class SourceTypeDef(_RequiredSourceTypeDef, _OptionalSourceTypeDef):
    pass


_RequiredTransportTypeDef = TypedDict(
    "_RequiredTransportTypeDef",
    {"Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"]},
)
_OptionalTransportTypeDef = TypedDict(
    "_OptionalTransportTypeDef",
    {
        "CidrAllowList": List[str],
        "MaxBitrate": int,
        "MaxLatency": int,
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)


class TransportTypeDef(_RequiredTransportTypeDef, _OptionalTransportTypeDef):
    pass


VpcInterfaceAttachmentTypeDef = TypedDict(
    "VpcInterfaceAttachmentTypeDef", {"VpcInterfaceName": str}, total=False
)

VpcInterfaceTypeDef = TypedDict(
    "VpcInterfaceTypeDef",
    {
        "Name": str,
        "NetworkInterfaceIds": List[str],
        "RoleArn": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
    },
)

AddFlowOutputsResponseTypeDef = TypedDict(
    "AddFlowOutputsResponseTypeDef", {"FlowArn": str, "Outputs": List["OutputTypeDef"]}, total=False
)

AddFlowSourcesResponseTypeDef = TypedDict(
    "AddFlowSourcesResponseTypeDef", {"FlowArn": str, "Sources": List["SourceTypeDef"]}, total=False
)

AddFlowVpcInterfacesResponseTypeDef = TypedDict(
    "AddFlowVpcInterfacesResponseTypeDef",
    {"FlowArn": str, "VpcInterfaces": List["VpcInterfaceTypeDef"]},
    total=False,
)

_RequiredAddOutputRequestTypeDef = TypedDict(
    "_RequiredAddOutputRequestTypeDef",
    {"Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"]},
)
_OptionalAddOutputRequestTypeDef = TypedDict(
    "_OptionalAddOutputRequestTypeDef",
    {
        "CidrAllowList": List[str],
        "Description": str,
        "Destination": str,
        "Encryption": "EncryptionTypeDef",
        "MaxLatency": int,
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


CreateFlowResponseTypeDef = TypedDict(
    "CreateFlowResponseTypeDef", {"Flow": "FlowTypeDef"}, total=False
)

DeleteFlowResponseTypeDef = TypedDict(
    "DeleteFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
    total=False,
)

DescribeFlowResponseTypeDef = TypedDict(
    "DescribeFlowResponseTypeDef",
    {"Flow": "FlowTypeDef", "Messages": "MessagesTypeDef"},
    total=False,
)

DescribeOfferingResponseTypeDef = TypedDict(
    "DescribeOfferingResponseTypeDef", {"Offering": "OfferingTypeDef"}, total=False
)

DescribeReservationResponseTypeDef = TypedDict(
    "DescribeReservationResponseTypeDef", {"Reservation": "ReservationTypeDef"}, total=False
)

_RequiredGrantEntitlementRequestTypeDef = TypedDict(
    "_RequiredGrantEntitlementRequestTypeDef", {"Subscribers": List[str]}
)
_OptionalGrantEntitlementRequestTypeDef = TypedDict(
    "_OptionalGrantEntitlementRequestTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": "EncryptionTypeDef",
        "EntitlementStatus": Literal["ENABLED", "DISABLED"],
        "Name": str,
    },
    total=False,
)


class GrantEntitlementRequestTypeDef(
    _RequiredGrantEntitlementRequestTypeDef, _OptionalGrantEntitlementRequestTypeDef
):
    pass


GrantFlowEntitlementsResponseTypeDef = TypedDict(
    "GrantFlowEntitlementsResponseTypeDef",
    {"Entitlements": List["EntitlementTypeDef"], "FlowArn": str},
    total=False,
)

ListEntitlementsResponseTypeDef = TypedDict(
    "ListEntitlementsResponseTypeDef",
    {"Entitlements": List["ListedEntitlementTypeDef"], "NextToken": str},
    total=False,
)

ListFlowsResponseTypeDef = TypedDict(
    "ListFlowsResponseTypeDef", {"Flows": List["ListedFlowTypeDef"], "NextToken": str}, total=False
)

ListOfferingsResponseTypeDef = TypedDict(
    "ListOfferingsResponseTypeDef",
    {"NextToken": str, "Offerings": List["OfferingTypeDef"]},
    total=False,
)

ListReservationsResponseTypeDef = TypedDict(
    "ListReservationsResponseTypeDef",
    {"NextToken": str, "Reservations": List["ReservationTypeDef"]},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PurchaseOfferingResponseTypeDef = TypedDict(
    "PurchaseOfferingResponseTypeDef", {"Reservation": "ReservationTypeDef"}, total=False
)

RemoveFlowOutputResponseTypeDef = TypedDict(
    "RemoveFlowOutputResponseTypeDef", {"FlowArn": str, "OutputArn": str}, total=False
)

RemoveFlowSourceResponseTypeDef = TypedDict(
    "RemoveFlowSourceResponseTypeDef", {"FlowArn": str, "SourceArn": str}, total=False
)

RemoveFlowVpcInterfaceResponseTypeDef = TypedDict(
    "RemoveFlowVpcInterfaceResponseTypeDef",
    {"FlowArn": str, "NonDeletedNetworkInterfaceIds": List[str], "VpcInterfaceName": str},
    total=False,
)

RevokeFlowEntitlementResponseTypeDef = TypedDict(
    "RevokeFlowEntitlementResponseTypeDef", {"EntitlementArn": str, "FlowArn": str}, total=False
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
        "Name": str,
        "Protocol": Literal["zixi-push", "rtp-fec", "rtp", "zixi-pull", "rist"],
        "StreamId": str,
        "VpcInterfaceName": str,
        "WhitelistCidr": str,
    },
    total=False,
)

StartFlowResponseTypeDef = TypedDict(
    "StartFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
    total=False,
)

StopFlowResponseTypeDef = TypedDict(
    "StopFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": Literal[
            "STANDBY", "ACTIVE", "UPDATING", "DELETING", "STARTING", "STOPPING", "ERROR"
        ],
    },
    total=False,
)

UpdateEncryptionTypeDef = TypedDict(
    "UpdateEncryptionTypeDef",
    {
        "Algorithm": Literal["aes128", "aes192", "aes256"],
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": Literal["speke", "static-key"],
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
    {"RecoveryWindow": int, "State": Literal["ENABLED", "DISABLED"]},
    total=False,
)

UpdateFlowEntitlementResponseTypeDef = TypedDict(
    "UpdateFlowEntitlementResponseTypeDef",
    {"Entitlement": "EntitlementTypeDef", "FlowArn": str},
    total=False,
)

UpdateFlowOutputResponseTypeDef = TypedDict(
    "UpdateFlowOutputResponseTypeDef", {"FlowArn": str, "Output": "OutputTypeDef"}, total=False
)

UpdateFlowResponseTypeDef = TypedDict(
    "UpdateFlowResponseTypeDef", {"Flow": "FlowTypeDef"}, total=False
)

UpdateFlowSourceResponseTypeDef = TypedDict(
    "UpdateFlowSourceResponseTypeDef", {"FlowArn": str, "Source": "SourceTypeDef"}, total=False
)

VpcInterfaceRequestTypeDef = TypedDict(
    "VpcInterfaceRequestTypeDef",
    {"Name": str, "RoleArn": str, "SecurityGroupIds": List[str], "SubnetId": str},
)
