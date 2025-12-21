"""
Type annotations for rtbfabric service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_rtbfabric.client import RTBFabricClient
    from mypy_boto3_rtbfabric.waiter import (
        InboundExternalLinkActiveWaiter,
        LinkAcceptedWaiter,
        LinkActiveWaiter,
        OutboundExternalLinkActiveWaiter,
        RequesterGatewayActiveWaiter,
        RequesterGatewayDeletedWaiter,
        ResponderGatewayActiveWaiter,
        ResponderGatewayDeletedWaiter,
    )

    session = Session()
    client: RTBFabricClient = session.client("rtbfabric")

    inbound_external_link_active_waiter: InboundExternalLinkActiveWaiter = client.get_waiter("inbound_external_link_active")
    link_accepted_waiter: LinkAcceptedWaiter = client.get_waiter("link_accepted")
    link_active_waiter: LinkActiveWaiter = client.get_waiter("link_active")
    outbound_external_link_active_waiter: OutboundExternalLinkActiveWaiter = client.get_waiter("outbound_external_link_active")
    requester_gateway_active_waiter: RequesterGatewayActiveWaiter = client.get_waiter("requester_gateway_active")
    requester_gateway_deleted_waiter: RequesterGatewayDeletedWaiter = client.get_waiter("requester_gateway_deleted")
    responder_gateway_active_waiter: ResponderGatewayActiveWaiter = client.get_waiter("responder_gateway_active")
    responder_gateway_deleted_waiter: ResponderGatewayDeletedWaiter = client.get_waiter("responder_gateway_deleted")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    GetInboundExternalLinkRequestWaitTypeDef,
    GetLinkRequestWaitExtraTypeDef,
    GetLinkRequestWaitTypeDef,
    GetOutboundExternalLinkRequestWaitTypeDef,
    GetRequesterGatewayRequestWaitExtraTypeDef,
    GetRequesterGatewayRequestWaitTypeDef,
    GetResponderGatewayRequestWaitExtraTypeDef,
    GetResponderGatewayRequestWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "InboundExternalLinkActiveWaiter",
    "LinkAcceptedWaiter",
    "LinkActiveWaiter",
    "OutboundExternalLinkActiveWaiter",
    "RequesterGatewayActiveWaiter",
    "RequesterGatewayDeletedWaiter",
    "ResponderGatewayActiveWaiter",
    "ResponderGatewayDeletedWaiter",
)

class InboundExternalLinkActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/waiter/InboundExternalLinkActive.html#RTBFabric.Waiter.InboundExternalLinkActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/waiters/#inboundexternallinkactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetInboundExternalLinkRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/waiter/InboundExternalLinkActive.html#RTBFabric.Waiter.InboundExternalLinkActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/waiters/#inboundexternallinkactivewaiter)
        """

class LinkAcceptedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/waiter/LinkAccepted.html#RTBFabric.Waiter.LinkAccepted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/waiters/#linkacceptedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetLinkRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/waiter/LinkAccepted.html#RTBFabric.Waiter.LinkAccepted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/waiters/#linkacceptedwaiter)
        """

class LinkActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/waiter/LinkActive.html#RTBFabric.Waiter.LinkActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/waiters/#linkactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetLinkRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/waiter/LinkActive.html#RTBFabric.Waiter.LinkActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/waiters/#linkactivewaiter)
        """

class OutboundExternalLinkActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/waiter/OutboundExternalLinkActive.html#RTBFabric.Waiter.OutboundExternalLinkActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/waiters/#outboundexternallinkactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetOutboundExternalLinkRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/waiter/OutboundExternalLinkActive.html#RTBFabric.Waiter.OutboundExternalLinkActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/waiters/#outboundexternallinkactivewaiter)
        """

class RequesterGatewayActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/waiter/RequesterGatewayActive.html#RTBFabric.Waiter.RequesterGatewayActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/waiters/#requestergatewayactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetRequesterGatewayRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/waiter/RequesterGatewayActive.html#RTBFabric.Waiter.RequesterGatewayActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/waiters/#requestergatewayactivewaiter)
        """

class RequesterGatewayDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/waiter/RequesterGatewayDeleted.html#RTBFabric.Waiter.RequesterGatewayDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/waiters/#requestergatewaydeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetRequesterGatewayRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/waiter/RequesterGatewayDeleted.html#RTBFabric.Waiter.RequesterGatewayDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/waiters/#requestergatewaydeletedwaiter)
        """

class ResponderGatewayActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/waiter/ResponderGatewayActive.html#RTBFabric.Waiter.ResponderGatewayActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/waiters/#respondergatewayactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetResponderGatewayRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/waiter/ResponderGatewayActive.html#RTBFabric.Waiter.ResponderGatewayActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/waiters/#respondergatewayactivewaiter)
        """

class ResponderGatewayDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/waiter/ResponderGatewayDeleted.html#RTBFabric.Waiter.ResponderGatewayDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/waiters/#respondergatewaydeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetResponderGatewayRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/waiter/ResponderGatewayDeleted.html#RTBFabric.Waiter.ResponderGatewayDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/waiters/#respondergatewaydeletedwaiter)
        """
