"""
Type annotations for iotsecuretunneling service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_iotsecuretunneling import IoTSecureTunnelingClient

    client: IoTSecureTunnelingClient = boto3.client("iotsecuretunneling")
    ```
"""

from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import ClientModeType
from .type_defs import (
    DescribeTunnelResponseTypeDef,
    DestinationConfigTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTunnelsResponseTypeDef,
    OpenTunnelResponseTypeDef,
    RotateTunnelAccessTokenResponseTypeDef,
    TagTypeDef,
    TimeoutConfigTypeDef,
)

__all__ = ("IoTSecureTunnelingClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class IoTSecureTunnelingClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IoTSecureTunnelingClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client.html#close)
        """

    def close_tunnel(self, *, tunnelId: str, delete: bool = None) -> Dict[str, Any]:
        """
        Closes a tunnel identified by the unique tunnel id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.close_tunnel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client.html#close_tunnel)
        """

    def describe_tunnel(self, *, tunnelId: str) -> DescribeTunnelResponseTypeDef:
        """
        Gets information about a tunnel identified by the unique tunnel id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.describe_tunnel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client.html#describe_tunnel)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client.html#generate_presigned_url)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client.html#list_tags_for_resource)
        """

    def list_tunnels(
        self, *, thingName: str = None, maxResults: int = None, nextToken: str = None
    ) -> ListTunnelsResponseTypeDef:
        """
        List all tunnels for an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.list_tunnels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client.html#list_tunnels)
        """

    def open_tunnel(
        self,
        *,
        description: str = None,
        tags: List["TagTypeDef"] = None,
        destinationConfig: "DestinationConfigTypeDef" = None,
        timeoutConfig: "TimeoutConfigTypeDef" = None
    ) -> OpenTunnelResponseTypeDef:
        """
        Creates a new tunnel, and returns two client access tokens for clients to use to
        connect to the IoT Secure Tunneling proxy server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.open_tunnel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client.html#open_tunnel)
        """

    def rotate_tunnel_access_token(
        self,
        *,
        tunnelId: str,
        clientMode: ClientModeType,
        destinationConfig: "DestinationConfigTypeDef" = None
    ) -> RotateTunnelAccessTokenResponseTypeDef:
        """
        Revokes the current client access token (CAT) and returns new CAT for clients to
        use when reconnecting to secure tunneling to access the same tunnel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.rotate_tunnel_access_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client.html#rotate_tunnel_access_token)
        """

    def tag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        A resource tag.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client.html#untag_resource)
        """
