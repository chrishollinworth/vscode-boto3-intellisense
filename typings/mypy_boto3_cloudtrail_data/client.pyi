"""
Type annotations for cloudtrail-data service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail_data/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cloudtrail_data.client import CloudTrailDataServiceClient

    session = Session()
    client: CloudTrailDataServiceClient = session.client("cloudtrail-data")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import PutAuditEventsRequestTypeDef, PutAuditEventsResponseTypeDef

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("CloudTrailDataServiceClient",)

class Exceptions(BaseClientExceptions):
    ChannelInsufficientPermission: Type[BotocoreClientError]
    ChannelNotFound: Type[BotocoreClientError]
    ChannelUnsupportedSchema: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DuplicatedAuditEventId: Type[BotocoreClientError]
    InvalidChannelARN: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]

class CloudTrailDataServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail-data.html#CloudTrailDataService.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail_data/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudTrailDataServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail-data.html#CloudTrailDataService.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail_data/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail-data/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail_data/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail-data/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail_data/client/#generate_presigned_url)
        """

    def put_audit_events(
        self, **kwargs: Unpack[PutAuditEventsRequestTypeDef]
    ) -> PutAuditEventsResponseTypeDef:
        """
        Ingests your application events into CloudTrail Lake.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail-data/client/put_audit_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail_data/client/#put_audit_events)
        """
