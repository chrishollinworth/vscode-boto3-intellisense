# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for meteringmarketplace service client

Usage::

    ```python
    import boto3
    from mypy_boto3_meteringmarketplace import MarketplaceMeteringClient

    client: MarketplaceMeteringClient = boto3.client("meteringmarketplace")
    ```
"""
from datetime import datetime
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_meteringmarketplace.type_defs import (
    BatchMeterUsageResultTypeDef,
    MeterUsageResultTypeDef,
    RegisterUsageResultTypeDef,
    ResolveCustomerResultTypeDef,
    UsageAllocationTypeDef,
    UsageRecordTypeDef,
)

__all__ = ("MarketplaceMeteringClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    CustomerNotEntitledException: Type[BotocoreClientError]
    DisabledApiException: Type[BotocoreClientError]
    DuplicateRequestException: Type[BotocoreClientError]
    ExpiredTokenException: Type[BotocoreClientError]
    InternalServiceErrorException: Type[BotocoreClientError]
    InvalidCustomerIdentifierException: Type[BotocoreClientError]
    InvalidEndpointRegionException: Type[BotocoreClientError]
    InvalidProductCodeException: Type[BotocoreClientError]
    InvalidPublicKeyVersionException: Type[BotocoreClientError]
    InvalidRegionException: Type[BotocoreClientError]
    InvalidTagException: Type[BotocoreClientError]
    InvalidTokenException: Type[BotocoreClientError]
    InvalidUsageAllocationsException: Type[BotocoreClientError]
    InvalidUsageDimensionException: Type[BotocoreClientError]
    PlatformNotSupportedException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TimestampOutOfBoundsException: Type[BotocoreClientError]


class MarketplaceMeteringClient:
    """
    [MarketplaceMetering.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/meteringmarketplace.html#MarketplaceMetering.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_meter_usage(
        self, UsageRecords: List["UsageRecordTypeDef"], ProductCode: str
    ) -> BatchMeterUsageResultTypeDef:
        """
        [Client.batch_meter_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.batch_meter_usage)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.generate_presigned_url)
        """

    def meter_usage(
        self,
        ProductCode: str,
        Timestamp: datetime,
        UsageDimension: str,
        UsageQuantity: int = None,
        DryRun: bool = None,
        UsageAllocations: List["UsageAllocationTypeDef"] = None,
    ) -> MeterUsageResultTypeDef:
        """
        [Client.meter_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.meter_usage)
        """

    def register_usage(
        self, ProductCode: str, PublicKeyVersion: int, Nonce: str = None
    ) -> RegisterUsageResultTypeDef:
        """
        [Client.register_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.register_usage)
        """

    def resolve_customer(self, RegistrationToken: str) -> ResolveCustomerResultTypeDef:
        """
        [Client.resolve_customer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.resolve_customer)
        """
