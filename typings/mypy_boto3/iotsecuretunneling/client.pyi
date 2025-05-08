"""
Type annotations for iotsecuretunneling service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_iotsecuretunneling.client import IoTSecureTunnelingClient

    session = Session()
    client: IoTSecureTunnelingClient = session.client("iotsecuretunneling")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    CloseTunnelRequestTypeDef,
    DescribeTunnelRequestTypeDef,
    DescribeTunnelResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTunnelsRequestTypeDef,
    ListTunnelsResponseTypeDef,
    OpenTunnelRequestTypeDef,
    OpenTunnelResponseTypeDef,
    RotateTunnelAccessTokenRequestTypeDef,
    RotateTunnelAccessTokenResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
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

__all__ = ("IoTSecureTunnelingClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class IoTSecureTunnelingClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IoTSecureTunnelingClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling.html#IoTSecureTunneling.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client/#generate_presigned_url)
        """

    def close_tunnel(self, **kwargs: Unpack[CloseTunnelRequestTypeDef]) -> Dict[str, Any]:
        """
        Closes a tunnel identified by the unique tunnel id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling/client/close_tunnel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client/#close_tunnel)
        """

    def describe_tunnel(
        self, **kwargs: Unpack[DescribeTunnelRequestTypeDef]
    ) -> DescribeTunnelResponseTypeDef:
        """
        Gets information about a tunnel identified by the unique tunnel id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling/client/describe_tunnel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client/#describe_tunnel)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client/#list_tags_for_resource)
        """

    def list_tunnels(
        self, **kwargs: Unpack[ListTunnelsRequestTypeDef]
    ) -> ListTunnelsResponseTypeDef:
        """
        List all tunnels for an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling/client/list_tunnels.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client/#list_tunnels)
        """

    def open_tunnel(self, **kwargs: Unpack[OpenTunnelRequestTypeDef]) -> OpenTunnelResponseTypeDef:
        """
        Creates a new tunnel, and returns two client access tokens for clients to use
        to connect to the IoT Secure Tunneling proxy server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling/client/open_tunnel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client/#open_tunnel)
        """

    def rotate_tunnel_access_token(
        self, **kwargs: Unpack[RotateTunnelAccessTokenRequestTypeDef]
    ) -> RotateTunnelAccessTokenResponseTypeDef:
        """
        Revokes the current client access token (CAT) and returns new CAT for clients
        to use when reconnecting to secure tunneling to access the same tunnel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling/client/rotate_tunnel_access_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client/#rotate_tunnel_access_token)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        A resource tag.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a tag from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/client/#untag_resource)
        """
