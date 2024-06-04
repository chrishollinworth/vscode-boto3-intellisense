"""
Type annotations for cloudtrail-data service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail_data/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudtrail_data import CloudTrailDataServiceClient

    client: CloudTrailDataServiceClient = boto3.client("cloudtrail-data")
    ```
"""

from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import AuditEventTypeDef, PutAuditEventsResponseTypeDef

__all__ = ("CloudTrailDataServiceClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ChannelInsufficientPermission: Type[BotocoreClientError]
    ChannelNotFound: Type[BotocoreClientError]
    ChannelUnsupportedSchema: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DuplicatedAuditEventId: Type[BotocoreClientError]
    InvalidChannelARN: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]

class CloudTrailDataServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudtrail-data.html#CloudTrailDataService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail_data/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudTrailDataServiceClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudtrail-data.html#CloudTrailDataService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail_data/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudtrail-data.html#CloudTrailDataService.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail_data/client.html#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudtrail-data.html#CloudTrailDataService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail_data/client.html#generate_presigned_url)
        """

    def put_audit_events(
        self, *, auditEvents: List["AuditEventTypeDef"], channelArn: str, externalId: str = None
    ) -> PutAuditEventsResponseTypeDef:
        """
        Ingests your application events into CloudTrail Lake.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/cloudtrail-data.html#CloudTrailDataService.Client.put_audit_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail_data/client.html#put_audit_events)
        """
