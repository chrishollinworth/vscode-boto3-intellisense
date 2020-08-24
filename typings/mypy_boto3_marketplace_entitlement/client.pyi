# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for marketplace-entitlement service client

Usage::

    ```python
    import boto3
    from mypy_boto3_marketplace_entitlement import MarketplaceEntitlementServiceClient

    client: MarketplaceEntitlementServiceClient = boto3.client("marketplace-entitlement")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_marketplace_entitlement.paginator import GetEntitlementsPaginator
from mypy_boto3_marketplace_entitlement.type_defs import GetEntitlementsResultTypeDef

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MarketplaceEntitlementServiceClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    InternalServiceErrorException: Type[Boto3ClientError]
    InvalidParameterException: Type[Boto3ClientError]
    ThrottlingException: Type[Boto3ClientError]


class MarketplaceEntitlementServiceClient:
    """
    [MarketplaceEntitlementService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Client.generate_presigned_url)
        """

    def get_entitlements(
        self,
        ProductCode: str,
        Filter: Dict[Literal["CUSTOMER_IDENTIFIER", "DIMENSION"], List[str]] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetEntitlementsResultTypeDef:
        """
        [Client.get_entitlements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Client.get_entitlements)
        """

    def get_paginator(
        self, operation_name: Literal["get_entitlements"]
    ) -> GetEntitlementsPaginator:
        """
        [Paginator.GetEntitlements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Paginator.GetEntitlements)
        """
