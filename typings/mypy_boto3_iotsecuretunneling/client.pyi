# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for iotsecuretunneling service client

Usage::

    ```python
    import boto3
    from mypy_boto3_iotsecuretunneling import IoTSecureTunnelingClient

    client: IoTSecureTunnelingClient = boto3.client("iotsecuretunneling")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_iotsecuretunneling.type_defs import (
    DescribeTunnelResponseTypeDef,
    DestinationConfigTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTunnelsResponseTypeDef,
    OpenTunnelResponseTypeDef,
    TagTypeDef,
    TimeoutConfigTypeDef,
)

__all__ = ("IoTSecureTunnelingClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]


class IoTSecureTunnelingClient:
    """
    [IoTSecureTunneling.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.can_paginate)
        """

    def close_tunnel(self, tunnelId: str, delete: bool = None) -> Dict[str, Any]:
        """
        [Client.close_tunnel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.close_tunnel)
        """

    def describe_tunnel(self, tunnelId: str) -> DescribeTunnelResponseTypeDef:
        """
        [Client.describe_tunnel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.describe_tunnel)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.generate_presigned_url)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.list_tags_for_resource)
        """

    def list_tunnels(
        self, thingName: str = None, maxResults: int = None, nextToken: str = None
    ) -> ListTunnelsResponseTypeDef:
        """
        [Client.list_tunnels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.list_tunnels)
        """

    def open_tunnel(
        self,
        description: str = None,
        tags: List["TagTypeDef"] = None,
        destinationConfig: "DestinationConfigTypeDef" = None,
        timeoutConfig: "TimeoutConfigTypeDef" = None,
    ) -> OpenTunnelResponseTypeDef:
        """
        [Client.open_tunnel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.open_tunnel)
        """

    def tag_resource(self, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client.untag_resource)
        """
