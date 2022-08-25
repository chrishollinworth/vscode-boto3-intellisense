"""
Type annotations for outposts service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/literals.html)

Usage::

    ```python
    from mypy_boto3_outposts.literals import AddressTypeType

    data: AddressTypeType = "OPERATING_ADDRESS"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AddressTypeType",
    "AssetTypeType",
    "CatalogItemClassType",
    "CatalogItemStatusType",
    "FiberOpticCableTypeType",
    "LineItemStatusType",
    "MaximumSupportedWeightLbsType",
    "OpticalStandardType",
    "OrderStatusType",
    "OrderTypeType",
    "PaymentOptionType",
    "PaymentTermType",
    "PowerConnectorType",
    "PowerDrawKvaType",
    "PowerFeedDropType",
    "PowerPhaseType",
    "ShipmentCarrierType",
    "SupportedHardwareTypeType",
    "SupportedStorageEnumType",
    "UplinkCountType",
    "UplinkGbpsType",
)

AddressTypeType = Literal["OPERATING_ADDRESS", "SHIPPING_ADDRESS"]
AssetTypeType = Literal["COMPUTE"]
CatalogItemClassType = Literal["RACK", "SERVER"]
CatalogItemStatusType = Literal["AVAILABLE", "DISCONTINUED"]
FiberOpticCableTypeType = Literal["MULTI_MODE", "SINGLE_MODE"]
LineItemStatusType = Literal[
    "BUILDING", "CANCELLED", "DELIVERED", "ERROR", "INSTALLED", "INSTALLING", "PREPARING", "SHIPPED"
]
MaximumSupportedWeightLbsType = Literal[
    "MAX_1400_LBS", "MAX_1600_LBS", "MAX_1800_LBS", "MAX_2000_LBS", "NO_LIMIT"
]
OpticalStandardType = Literal[
    "OPTIC_1000BASE_LX",
    "OPTIC_1000BASE_SX",
    "OPTIC_100GBASE_CWDM4",
    "OPTIC_100GBASE_LR4",
    "OPTIC_100GBASE_SR4",
    "OPTIC_100G_PSM4_MSA",
    "OPTIC_10GBASE_IR",
    "OPTIC_10GBASE_LR",
    "OPTIC_10GBASE_SR",
    "OPTIC_40GBASE_ESR",
    "OPTIC_40GBASE_IR4_LR4L",
    "OPTIC_40GBASE_LR4",
    "OPTIC_40GBASE_SR",
]
OrderStatusType = Literal[
    "CANCELLED",
    "COMPLETED",
    "ERROR",
    "FULFILLED",
    "INSTALLING",
    "IN_PROGRESS",
    "PENDING",
    "PREPARING",
    "PROCESSING",
    "RECEIVED",
]
OrderTypeType = Literal["OUTPOST", "REPLACEMENT"]
PaymentOptionType = Literal["ALL_UPFRONT", "NO_UPFRONT", "PARTIAL_UPFRONT"]
PaymentTermType = Literal["THREE_YEARS"]
PowerConnectorType = Literal["AH530P7W", "AH532P6W", "IEC309", "L6_30P"]
PowerDrawKvaType = Literal["POWER_10_KVA", "POWER_15_KVA", "POWER_5_KVA"]
PowerFeedDropType = Literal["ABOVE_RACK", "BELOW_RACK"]
PowerPhaseType = Literal["SINGLE_PHASE", "THREE_PHASE"]
ShipmentCarrierType = Literal["DBS", "DHL", "FEDEX", "UPS"]
SupportedHardwareTypeType = Literal["RACK", "SERVER"]
SupportedStorageEnumType = Literal["EBS", "S3"]
UplinkCountType = Literal[
    "UPLINK_COUNT_1",
    "UPLINK_COUNT_12",
    "UPLINK_COUNT_16",
    "UPLINK_COUNT_2",
    "UPLINK_COUNT_3",
    "UPLINK_COUNT_4",
    "UPLINK_COUNT_5",
    "UPLINK_COUNT_6",
    "UPLINK_COUNT_7",
    "UPLINK_COUNT_8",
]
UplinkGbpsType = Literal["UPLINK_100G", "UPLINK_10G", "UPLINK_1G", "UPLINK_40G"]
