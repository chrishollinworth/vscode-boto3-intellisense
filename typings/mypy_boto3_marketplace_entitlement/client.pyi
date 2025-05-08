"""
Type annotations for marketplace-entitlement service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_entitlement/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_marketplace_entitlement.client import MarketplaceEntitlementServiceClient

    session = Session()
    client: MarketplaceEntitlementServiceClient = session.client("marketplace-entitlement")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import GetEntitlementsPaginator
from .type_defs import GetEntitlementsRequestTypeDef, GetEntitlementsResultTypeDef

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("MarketplaceEntitlementServiceClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InternalServiceErrorException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class MarketplaceEntitlementServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_entitlement/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MarketplaceEntitlementServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_entitlement/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-entitlement/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_entitlement/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-entitlement/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_entitlement/client/#generate_presigned_url)
        """

    def get_entitlements(
        self, **kwargs: Unpack[GetEntitlementsRequestTypeDef]
    ) -> GetEntitlementsResultTypeDef:
        """
        GetEntitlements retrieves entitlement values for a given product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-entitlement/client/get_entitlements.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_entitlement/client/#get_entitlements)
        """

    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_entitlements"]
    ) -> GetEntitlementsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-entitlement/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_entitlement/client/#get_paginator)
        """
