"""
Type annotations for connect-contact-lens service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect_contact_lens/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_connect_contact_lens import ConnectContactLensClient

    client: ConnectContactLensClient = boto3.client("connect-contact-lens")
    ```
"""
from typing import Any, Dict, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import ListRealtimeContactAnalysisSegmentsResponseTypeDef

__all__ = ("ConnectContactLensClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class ConnectContactLensClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/connect-contact-lens.html#ConnectContactLens.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect_contact_lens/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ConnectContactLensClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/connect-contact-lens.html#ConnectContactLens.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect_contact_lens/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/connect-contact-lens.html#ConnectContactLens.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect_contact_lens/client.html#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/connect-contact-lens.html#ConnectContactLens.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect_contact_lens/client.html#generate_presigned_url)
        """
    def list_realtime_contact_analysis_segments(
        self, *, InstanceId: str, ContactId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListRealtimeContactAnalysisSegmentsResponseTypeDef:
        """
        Provides a list of analysis segments for a real-time analysis session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/connect-contact-lens.html#ConnectContactLens.Client.list_realtime_contact_analysis_segments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect_contact_lens/client.html#list_realtime_contact_analysis_segments)
        """
