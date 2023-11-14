"""
Type annotations for snowball service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/literals.html)

Usage::

    ```python
    from mypy_boto3_snowball.literals import AddressTypeType

    data: AddressTypeType = "AWS_SHIP"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AddressTypeType",
    "ClusterStateType",
    "DescribeAddressesPaginatorName",
    "DeviceServiceNameType",
    "ImpactLevelType",
    "JobStateType",
    "JobTypeType",
    "ListClusterJobsPaginatorName",
    "ListClustersPaginatorName",
    "ListCompatibleImagesPaginatorName",
    "ListJobsPaginatorName",
    "ListLongTermPricingPaginatorName",
    "LongTermPricingTypeType",
    "RemoteManagementType",
    "ServiceNameType",
    "ShipmentStateType",
    "ShippingLabelStatusType",
    "ShippingOptionType",
    "SnowballCapacityType",
    "SnowballTypeType",
    "StorageUnitType",
    "TransferOptionType",
)

AddressTypeType = Literal["AWS_SHIP", "CUST_PICKUP"]
ClusterStateType = Literal["AwaitingQuorum", "Cancelled", "Complete", "InUse", "Pending"]
DescribeAddressesPaginatorName = Literal["describe_addresses"]
DeviceServiceNameType = Literal["NFS_ON_DEVICE_SERVICE", "S3_ON_DEVICE_SERVICE"]
ImpactLevelType = Literal["IL2", "IL4", "IL5", "IL6", "IL99"]
JobStateType = Literal[
    "Cancelled",
    "Complete",
    "InProgress",
    "InTransitToAWS",
    "InTransitToCustomer",
    "Listing",
    "New",
    "Pending",
    "PreparingAppliance",
    "PreparingShipment",
    "WithAWS",
    "WithAWSSortingFacility",
    "WithCustomer",
]
JobTypeType = Literal["EXPORT", "IMPORT", "LOCAL_USE"]
ListClusterJobsPaginatorName = Literal["list_cluster_jobs"]
ListClustersPaginatorName = Literal["list_clusters"]
ListCompatibleImagesPaginatorName = Literal["list_compatible_images"]
ListJobsPaginatorName = Literal["list_jobs"]
ListLongTermPricingPaginatorName = Literal["list_long_term_pricing"]
LongTermPricingTypeType = Literal["OneMonth", "OneYear", "ThreeYear"]
RemoteManagementType = Literal["INSTALLED_AUTOSTART", "INSTALLED_ONLY", "NOT_INSTALLED"]
ServiceNameType = Literal["EKS_ANYWHERE", "KUBERNETES"]
ShipmentStateType = Literal["RECEIVED", "RETURNED"]
ShippingLabelStatusType = Literal["Failed", "InProgress", "Succeeded", "TimedOut"]
ShippingOptionType = Literal["EXPRESS", "NEXT_DAY", "SECOND_DAY", "STANDARD"]
SnowballCapacityType = Literal[
    "NoPreference", "T100", "T13", "T14", "T240", "T32", "T42", "T50", "T8", "T80", "T98"
]
SnowballTypeType = Literal[
    "EDGE",
    "EDGE_C",
    "EDGE_CG",
    "EDGE_S",
    "RACK_5U_C",
    "SNC1_HDD",
    "SNC1_SSD",
    "STANDARD",
    "V3_5C",
    "V3_5S",
]
StorageUnitType = Literal["TB"]
TransferOptionType = Literal["EXPORT", "IMPORT", "LOCAL_USE"]
