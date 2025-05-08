"""
Type annotations for marketplacecommerceanalytics service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_marketplacecommerceanalytics.client import MarketplaceCommerceAnalyticsClient

    session = Session()
    client: MarketplaceCommerceAnalyticsClient = session.client("marketplacecommerceanalytics")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    GenerateDataSetRequestTypeDef,
    GenerateDataSetResultTypeDef,
    StartSupportDataExportRequestTypeDef,
    StartSupportDataExportResultTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("MarketplaceCommerceAnalyticsClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    MarketplaceCommerceAnalyticsException: Type[BotocoreClientError]

class MarketplaceCommerceAnalyticsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MarketplaceCommerceAnalyticsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplacecommerceanalytics/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplacecommerceanalytics/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/client/#generate_presigned_url)
        """

    def generate_data_set(
        self, **kwargs: Unpack[GenerateDataSetRequestTypeDef]
    ) -> GenerateDataSetResultTypeDef:
        """
        Given a data set type and data set publication date, asynchronously publishes
        the requested data set to the specified S3 bucket and notifies the specified
        SNS topic once the data is available.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplacecommerceanalytics/client/generate_data_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/client/#generate_data_set)
        """

    def start_support_data_export(
        self, **kwargs: Unpack[StartSupportDataExportRequestTypeDef]
    ) -> StartSupportDataExportResultTypeDef:
        """
        <i>This target has been deprecated.</i> Given a data set type and a from date,
        asynchronously publishes the requested customer support data to the specified
        S3 bucket and notifies the specified SNS topic once the data is available.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplacecommerceanalytics/client/start_support_data_export.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/client/#start_support_data_export)
        """
