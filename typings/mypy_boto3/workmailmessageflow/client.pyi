"""
Type annotations for workmailmessageflow service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmailmessageflow/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_workmailmessageflow.client import WorkMailMessageFlowClient

    session = Session()
    client: WorkMailMessageFlowClient = session.client("workmailmessageflow")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    GetRawMessageContentRequestTypeDef,
    GetRawMessageContentResponseTypeDef,
    PutRawMessageContentRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("WorkMailMessageFlowClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InvalidContentLocation: Type[BotocoreClientError]
    MessageFrozen: Type[BotocoreClientError]
    MessageRejected: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class WorkMailMessageFlowClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmailmessageflow.html#WorkMailMessageFlow.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmailmessageflow/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        WorkMailMessageFlowClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmailmessageflow.html#WorkMailMessageFlow.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmailmessageflow/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmailmessageflow/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmailmessageflow/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmailmessageflow/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmailmessageflow/client/#generate_presigned_url)
        """

    def get_raw_message_content(
        self, **kwargs: Unpack[GetRawMessageContentRequestTypeDef]
    ) -> GetRawMessageContentResponseTypeDef:
        """
        Retrieves the raw content of an in-transit email message, in MIME format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmailmessageflow/client/get_raw_message_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmailmessageflow/client/#get_raw_message_content)
        """

    def put_raw_message_content(
        self, **kwargs: Unpack[PutRawMessageContentRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the raw content of an in-transit email message, in MIME format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmailmessageflow/client/put_raw_message_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmailmessageflow/client/#put_raw_message_content)
        """
