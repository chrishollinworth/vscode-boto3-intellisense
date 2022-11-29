"""
Type annotations for meteringmarketplace service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_meteringmarketplace import MarketplaceMeteringClient

    client: MarketplaceMeteringClient = boto3.client("meteringmarketplace")
    ```
"""
from datetime import datetime
from typing import Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
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

class MarketplaceMeteringClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/meteringmarketplace.html#MarketplaceMetering.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MarketplaceMeteringClient exceptions.
        """
    def batch_meter_usage(
        self, *, UsageRecords: List["UsageRecordTypeDef"], ProductCode: str
    ) -> BatchMeterUsageResultTypeDef:
        """
        `BatchMeterUsage` is called from a SaaS application listed on AWS Marketplace to
        post metering records for a set of customers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.batch_meter_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/client.html#batch_meter_usage)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/client.html#close)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/client.html#generate_presigned_url)
        """
    def meter_usage(
        self,
        *,
        ProductCode: str,
        Timestamp: Union[datetime, str],
        UsageDimension: str,
        UsageQuantity: int = None,
        DryRun: bool = None,
        UsageAllocations: List["UsageAllocationTypeDef"] = None
    ) -> MeterUsageResultTypeDef:
        """
        API to emit metering records.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.meter_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/client.html#meter_usage)
        """
    def register_usage(
        self, *, ProductCode: str, PublicKeyVersion: int, Nonce: str = None
    ) -> RegisterUsageResultTypeDef:
        """
        Paid container software products sold through AWS Marketplace must integrate
        with the AWS Marketplace Metering Service and call the `RegisterUsage` operation
        for software entitlement and metering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.register_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/client.html#register_usage)
        """
    def resolve_customer(self, *, RegistrationToken: str) -> ResolveCustomerResultTypeDef:
        """
        `ResolveCustomer` is called by a SaaS application during the registration
        process.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.resolve_customer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/client.html#resolve_customer)
        """
