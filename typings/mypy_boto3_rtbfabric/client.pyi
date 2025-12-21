"""
Type annotations for rtbfabric service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_rtbfabric.client import RTBFabricClient

    session = Session()
    client: RTBFabricClient = session.client("rtbfabric")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListLinksPaginator,
    ListRequesterGatewaysPaginator,
    ListResponderGatewaysPaginator,
)
from .type_defs import (
    AcceptLinkRequestTypeDef,
    AcceptLinkResponseTypeDef,
    CreateInboundExternalLinkRequestTypeDef,
    CreateInboundExternalLinkResponseTypeDef,
    CreateLinkRequestTypeDef,
    CreateLinkResponseTypeDef,
    CreateOutboundExternalLinkRequestTypeDef,
    CreateOutboundExternalLinkResponseTypeDef,
    CreateRequesterGatewayRequestTypeDef,
    CreateRequesterGatewayResponseTypeDef,
    CreateResponderGatewayRequestTypeDef,
    CreateResponderGatewayResponseTypeDef,
    DeleteInboundExternalLinkRequestTypeDef,
    DeleteInboundExternalLinkResponseTypeDef,
    DeleteLinkRequestTypeDef,
    DeleteLinkResponseTypeDef,
    DeleteOutboundExternalLinkRequestTypeDef,
    DeleteOutboundExternalLinkResponseTypeDef,
    DeleteRequesterGatewayRequestTypeDef,
    DeleteRequesterGatewayResponseTypeDef,
    DeleteResponderGatewayRequestTypeDef,
    DeleteResponderGatewayResponseTypeDef,
    GetInboundExternalLinkRequestTypeDef,
    GetInboundExternalLinkResponseTypeDef,
    GetLinkRequestTypeDef,
    GetLinkResponseTypeDef,
    GetOutboundExternalLinkRequestTypeDef,
    GetOutboundExternalLinkResponseTypeDef,
    GetRequesterGatewayRequestTypeDef,
    GetRequesterGatewayResponseTypeDef,
    GetResponderGatewayRequestTypeDef,
    GetResponderGatewayResponseTypeDef,
    ListLinksRequestTypeDef,
    ListLinksResponseTypeDef,
    ListRequesterGatewaysRequestTypeDef,
    ListRequesterGatewaysResponseTypeDef,
    ListResponderGatewaysRequestTypeDef,
    ListResponderGatewaysResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    RejectLinkRequestTypeDef,
    RejectLinkResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateLinkModuleFlowRequestTypeDef,
    UpdateLinkModuleFlowResponseTypeDef,
    UpdateLinkRequestTypeDef,
    UpdateLinkResponseTypeDef,
    UpdateRequesterGatewayRequestTypeDef,
    UpdateRequesterGatewayResponseTypeDef,
    UpdateResponderGatewayRequestTypeDef,
    UpdateResponderGatewayResponseTypeDef,
)
from .waiter import (
    InboundExternalLinkActiveWaiter,
    LinkAcceptedWaiter,
    LinkActiveWaiter,
    OutboundExternalLinkActiveWaiter,
    RequesterGatewayActiveWaiter,
    RequesterGatewayDeletedWaiter,
    ResponderGatewayActiveWaiter,
    ResponderGatewayDeletedWaiter,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("RTBFabricClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class RTBFabricClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric.html#RTBFabric.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        RTBFabricClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric.html#RTBFabric.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#generate_presigned_url)
        """

    def accept_link(self, **kwargs: Unpack[AcceptLinkRequestTypeDef]) -> AcceptLinkResponseTypeDef:
        """
        Accepts a link request between gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/accept_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#accept_link)
        """

    def create_inbound_external_link(
        self, **kwargs: Unpack[CreateInboundExternalLinkRequestTypeDef]
    ) -> CreateInboundExternalLinkResponseTypeDef:
        """
        Creates an inbound external link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/create_inbound_external_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#create_inbound_external_link)
        """

    def create_link(self, **kwargs: Unpack[CreateLinkRequestTypeDef]) -> CreateLinkResponseTypeDef:
        """
        Creates a new link between gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/create_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#create_link)
        """

    def create_outbound_external_link(
        self, **kwargs: Unpack[CreateOutboundExternalLinkRequestTypeDef]
    ) -> CreateOutboundExternalLinkResponseTypeDef:
        """
        Creates an outbound external link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/create_outbound_external_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#create_outbound_external_link)
        """

    def create_requester_gateway(
        self, **kwargs: Unpack[CreateRequesterGatewayRequestTypeDef]
    ) -> CreateRequesterGatewayResponseTypeDef:
        """
        Creates a requester gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/create_requester_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#create_requester_gateway)
        """

    def create_responder_gateway(
        self, **kwargs: Unpack[CreateResponderGatewayRequestTypeDef]
    ) -> CreateResponderGatewayResponseTypeDef:
        """
        Creates a responder gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/create_responder_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#create_responder_gateway)
        """

    def delete_inbound_external_link(
        self, **kwargs: Unpack[DeleteInboundExternalLinkRequestTypeDef]
    ) -> DeleteInboundExternalLinkResponseTypeDef:
        """
        Deletes an inbound external link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/delete_inbound_external_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#delete_inbound_external_link)
        """

    def delete_link(self, **kwargs: Unpack[DeleteLinkRequestTypeDef]) -> DeleteLinkResponseTypeDef:
        """
        Deletes a link between gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/delete_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#delete_link)
        """

    def delete_outbound_external_link(
        self, **kwargs: Unpack[DeleteOutboundExternalLinkRequestTypeDef]
    ) -> DeleteOutboundExternalLinkResponseTypeDef:
        """
        Deletes an outbound external link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/delete_outbound_external_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#delete_outbound_external_link)
        """

    def delete_requester_gateway(
        self, **kwargs: Unpack[DeleteRequesterGatewayRequestTypeDef]
    ) -> DeleteRequesterGatewayResponseTypeDef:
        """
        Deletes a requester gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/delete_requester_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#delete_requester_gateway)
        """

    def delete_responder_gateway(
        self, **kwargs: Unpack[DeleteResponderGatewayRequestTypeDef]
    ) -> DeleteResponderGatewayResponseTypeDef:
        """
        Deletes a responder gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/delete_responder_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#delete_responder_gateway)
        """

    def get_inbound_external_link(
        self, **kwargs: Unpack[GetInboundExternalLinkRequestTypeDef]
    ) -> GetInboundExternalLinkResponseTypeDef:
        """
        Retrieves information about an inbound external link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/get_inbound_external_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#get_inbound_external_link)
        """

    def get_link(self, **kwargs: Unpack[GetLinkRequestTypeDef]) -> GetLinkResponseTypeDef:
        """
        Retrieves information about a link between gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/get_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#get_link)
        """

    def get_outbound_external_link(
        self, **kwargs: Unpack[GetOutboundExternalLinkRequestTypeDef]
    ) -> GetOutboundExternalLinkResponseTypeDef:
        """
        Retrieves information about an outbound external link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/get_outbound_external_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#get_outbound_external_link)
        """

    def get_requester_gateway(
        self, **kwargs: Unpack[GetRequesterGatewayRequestTypeDef]
    ) -> GetRequesterGatewayResponseTypeDef:
        """
        Retrieves information about a requester gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/get_requester_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#get_requester_gateway)
        """

    def get_responder_gateway(
        self, **kwargs: Unpack[GetResponderGatewayRequestTypeDef]
    ) -> GetResponderGatewayResponseTypeDef:
        """
        Retrieves information about a responder gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/get_responder_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#get_responder_gateway)
        """

    def list_links(self, **kwargs: Unpack[ListLinksRequestTypeDef]) -> ListLinksResponseTypeDef:
        """
        Lists links associated with gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/list_links.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#list_links)
        """

    def list_requester_gateways(
        self, **kwargs: Unpack[ListRequesterGatewaysRequestTypeDef]
    ) -> ListRequesterGatewaysResponseTypeDef:
        """
        Lists requester gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/list_requester_gateways.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#list_requester_gateways)
        """

    def list_responder_gateways(
        self, **kwargs: Unpack[ListResponderGatewaysRequestTypeDef]
    ) -> ListResponderGatewaysResponseTypeDef:
        """
        Lists reponder gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/list_responder_gateways.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#list_responder_gateways)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#list_tags_for_resource)
        """

    def reject_link(self, **kwargs: Unpack[RejectLinkRequestTypeDef]) -> RejectLinkResponseTypeDef:
        """
        Rejects a link request between gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/reject_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#reject_link)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a tag or tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#untag_resource)
        """

    def update_link(self, **kwargs: Unpack[UpdateLinkRequestTypeDef]) -> UpdateLinkResponseTypeDef:
        """
        Updates the configuration of a link between gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/update_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#update_link)
        """

    def update_link_module_flow(
        self, **kwargs: Unpack[UpdateLinkModuleFlowRequestTypeDef]
    ) -> UpdateLinkModuleFlowResponseTypeDef:
        """
        Updates a link module flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/update_link_module_flow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#update_link_module_flow)
        """

    def update_requester_gateway(
        self, **kwargs: Unpack[UpdateRequesterGatewayRequestTypeDef]
    ) -> UpdateRequesterGatewayResponseTypeDef:
        """
        Updates a requester gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/update_requester_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#update_requester_gateway)
        """

    def update_responder_gateway(
        self, **kwargs: Unpack[UpdateResponderGatewayRequestTypeDef]
    ) -> UpdateResponderGatewayResponseTypeDef:
        """
        Updates a responder gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/update_responder_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#update_responder_gateway)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_links"]
    ) -> ListLinksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_requester_gateways"]
    ) -> ListRequesterGatewaysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_responder_gateways"]
    ) -> ListResponderGatewaysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["inbound_external_link_active"]
    ) -> InboundExternalLinkActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["link_accepted"]
    ) -> LinkAcceptedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["link_active"]
    ) -> LinkActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["outbound_external_link_active"]
    ) -> OutboundExternalLinkActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["requester_gateway_active"]
    ) -> RequesterGatewayActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["requester_gateway_deleted"]
    ) -> RequesterGatewayDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["responder_gateway_active"]
    ) -> ResponderGatewayActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["responder_gateway_deleted"]
    ) -> ResponderGatewayDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/client/#get_waiter)
        """
