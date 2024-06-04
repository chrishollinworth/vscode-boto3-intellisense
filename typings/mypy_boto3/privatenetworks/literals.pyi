"""
Type annotations for privatenetworks service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/literals.html)

Usage::

    ```python
    from mypy_boto3_privatenetworks.literals import AcknowledgmentStatusType

    data: AcknowledgmentStatusType = "ACKNOWLEDGED"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AcknowledgmentStatusType",
    "CommitmentLengthType",
    "DeviceIdentifierFilterKeysType",
    "DeviceIdentifierStatusType",
    "ElevationReferenceType",
    "ElevationUnitType",
    "HealthStatusType",
    "ListDeviceIdentifiersPaginatorName",
    "ListNetworkResourcesPaginatorName",
    "ListNetworkSitesPaginatorName",
    "ListNetworksPaginatorName",
    "ListOrdersPaginatorName",
    "NetworkFilterKeysType",
    "NetworkResourceDefinitionTypeType",
    "NetworkResourceFilterKeysType",
    "NetworkResourceStatusType",
    "NetworkResourceTypeType",
    "NetworkSiteFilterKeysType",
    "NetworkSiteStatusType",
    "NetworkStatusType",
    "OrderFilterKeysType",
    "UpdateTypeType",
)

AcknowledgmentStatusType = Literal["ACKNOWLEDGED", "ACKNOWLEDGING", "UNACKNOWLEDGED"]
CommitmentLengthType = Literal["ONE_YEAR", "SIXTY_DAYS", "THREE_YEARS"]
DeviceIdentifierFilterKeysType = Literal["ORDER", "STATUS", "TRAFFIC_GROUP"]
DeviceIdentifierStatusType = Literal["ACTIVE", "INACTIVE"]
ElevationReferenceType = Literal["AGL", "AMSL"]
ElevationUnitType = Literal["FEET"]
HealthStatusType = Literal["HEALTHY", "INITIAL", "UNHEALTHY"]
ListDeviceIdentifiersPaginatorName = Literal["list_device_identifiers"]
ListNetworkResourcesPaginatorName = Literal["list_network_resources"]
ListNetworkSitesPaginatorName = Literal["list_network_sites"]
ListNetworksPaginatorName = Literal["list_networks"]
ListOrdersPaginatorName = Literal["list_orders"]
NetworkFilterKeysType = Literal["STATUS"]
NetworkResourceDefinitionTypeType = Literal["DEVICE_IDENTIFIER", "RADIO_UNIT"]
NetworkResourceFilterKeysType = Literal["ORDER", "STATUS"]
NetworkResourceStatusType = Literal[
    "AVAILABLE",
    "CREATING_SHIPPING_LABEL",
    "DELETED",
    "DELETING",
    "PENDING",
    "PENDING_RETURN",
    "PROVISIONED",
    "PROVISIONING",
    "SHIPPED",
]
NetworkResourceTypeType = Literal["RADIO_UNIT"]
NetworkSiteFilterKeysType = Literal["STATUS"]
NetworkSiteStatusType = Literal["AVAILABLE", "CREATED", "DELETED", "DEPROVISIONING", "PROVISIONING"]
NetworkStatusType = Literal["AVAILABLE", "CREATED", "DELETED", "DEPROVISIONING", "PROVISIONING"]
OrderFilterKeysType = Literal["NETWORK_SITE", "STATUS"]
UpdateTypeType = Literal["COMMITMENT", "REPLACE", "RETURN"]
