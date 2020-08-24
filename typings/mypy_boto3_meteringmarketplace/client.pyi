# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
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

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_meteringmarketplace.type_defs import (
    BatchMeterUsageResultTypeDef,
    MeterUsageResultTypeDef,
    RegisterUsageResultTypeDef,
    ResolveCustomerResultTypeDef,
    UsageRecordTypeDef,
)

__all__ = ("MarketplaceMeteringClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    CustomerNotEntitledException: Type[Boto3ClientError]
    DisabledApiException: Type[Boto3ClientError]
    DuplicateRequestException: Type[Boto3ClientError]
    ExpiredTokenException: Type[Boto3ClientError]
    InternalServiceErrorException: Type[Boto3ClientError]
    InvalidCustomerIdentifierException: Type[Boto3ClientError]
    InvalidEndpointRegionException: Type[Boto3ClientError]
    InvalidProductCodeException: Type[Boto3ClientError]
    InvalidPublicKeyVersionException: Type[Boto3ClientError]
    InvalidRegionException: Type[Boto3ClientError]
    InvalidTokenException: Type[Boto3ClientError]
    InvalidUsageDimensionException: Type[Boto3ClientError]
    PlatformNotSupportedException: Type[Boto3ClientError]
    ThrottlingException: Type[Boto3ClientError]
    TimestampOutOfBoundsException: Type[Boto3ClientError]


class MarketplaceMeteringClient:
    """
    [MarketplaceMetering.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/meteringmarketplace.html#MarketplaceMetering.Client)
    """

    exceptions: Exceptions

    def batch_meter_usage(
        self, UsageRecords: List["UsageRecordTypeDef"], ProductCode: str
    ) -> BatchMeterUsageResultTypeDef:
        """
        [Client.batch_meter_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.batch_meter_usage)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.generate_presigned_url)
        """

    def meter_usage(
        self,
        ProductCode: str,
        Timestamp: datetime,
        UsageDimension: str,
        UsageQuantity: int = None,
        DryRun: bool = None,
    ) -> MeterUsageResultTypeDef:
        """
        [Client.meter_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.meter_usage)
        """

    def register_usage(
        self, ProductCode: str, PublicKeyVersion: int, Nonce: str = None
    ) -> RegisterUsageResultTypeDef:
        """
        [Client.register_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.register_usage)
        """

    def resolve_customer(self, RegistrationToken: str) -> ResolveCustomerResultTypeDef:
        """
        [Client.resolve_customer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.resolve_customer)
        """
